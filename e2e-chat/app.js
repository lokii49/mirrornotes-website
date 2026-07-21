const go = new Go();
const wasmReady = (async () => {
  const resp = await fetch("e2echat.wasm");
  const bytes = await resp.arrayBuffer();
  const result = await WebAssembly.instantiate(bytes, go.importObject);
  go.run(result.instance); // does not resolve while the module is alive — don't await it
})();

function log(text, cls) {
  const li = document.createElement("li");
  li.textContent = text;
  if (cls) li.className = cls;
  const list = document.getElementById("log");
  list.appendChild(li);
  list.scrollTop = list.scrollHeight;
}

// logDownload appends a log entry with a click-to-download link for a
// received file, rather than plain text — the browser has no filesystem
// path to write to, so URL.createObjectURL + an <a download> is the
// equivalent of the CLI writing under <identity-dir>/received/.
function logDownload(text, file) {
  const li = document.createElement("li");
  const a = document.createElement("a");
  const blob = new Blob([file.data], { type: file.mimetype || "application/octet-stream" });
  a.href = URL.createObjectURL(blob);
  a.download = file.filename;
  a.textContent = text;
  li.appendChild(a);
  const list = document.getElementById("log");
  list.appendChild(li);
  list.scrollTop = list.scrollHeight;
}

function unwrap(result, what) {
  if (result.error) {
    log(`[error] ${what}: ${result.error}`, "err");
    throw new Error(`${what}: ${result.error}`);
  }
  return result.value;
}

let identity = null;
let session = null;
let reassembler = null;
let established = false;
let ws = null;

document.getElementById("generate-btn").addEventListener("click", async () => {
  await wasmReady;
  const nickname = document.getElementById("nickname").value || "anon";
  identity = unwrap(e2echat.generateIdentity(nickname), "generateIdentity");
  document.getElementById("fingerprint").textContent = identity.fingerprint;
  log(`identity generated: ${identity.nickname} (${identity.fingerprint})`);
});

document.getElementById("connect-btn").addEventListener("click", async () => {
  await wasmReady;
  if (!identity) {
    log("generate an identity first", "err");
    return;
  }
  const peerFP = document.getElementById("peer-fp").value.trim();
  if (!peerFP) {
    log("enter the peer's fingerprint first", "err");
    return;
  }

  session = unwrap(identity.newSession(), "newSession");
  reassembler = unwrap(e2echat.newReassembler(), "newReassembler");
  established = false;

  const relayURL = document.getElementById("relay-url").value;
  ws = new WebSocket(relayURL);
  ws.binaryType = "arraybuffer";

  ws.onopen = () => {
    document.getElementById("status").textContent = "connected to relay, pairing...";
    const pairReq = unwrap(e2echat.pairRequest(identity.fingerprint, peerFP), "pairRequest");
    ws.send(pairReq);
    const hello = unwrap(session.helloBytes(), "helloBytes");
    ws.send(hello);
  };

  ws.onmessage = (event) => {
    const bytes = new Uint8Array(event.data);

    if (!established) {
      const res = session.completePeerHello(bytes, peerFP);
      if (res.error) {
        log(`handshake failed: ${res.error}`, "err");
        return;
      }
      established = true;
      document.getElementById("status").textContent =
        `connected — double ratchet established with ${session.peerNickname()}`;
      document.getElementById("message").disabled = false;
      document.getElementById("send-btn").disabled = false;
      document.getElementById("file-input").disabled = false;
      document.getElementById("send-file-btn").disabled = false;
      return;
    }

    const decrypted = session.decrypt(bytes);
    if (decrypted.error) {
      log("dropped a message that failed to decrypt/authenticate", "warn");
      return;
    }
    const msg = unwrap(e2echat.unwrapMessage(decrypted.value), "unwrapMessage");

    if (msg.kind === e2echat.KindText) {
      log(`${session.peerNickname()}: ${new TextDecoder().decode(msg.body)}`);
    } else if (msg.kind === e2echat.KindFileChunk) {
      handleFileChunk(msg.body);
    } else {
      log(`dropped a message of unknown kind ${msg.kind}`, "warn");
    }
  };

  ws.onerror = () => log("websocket error", "err");
  ws.onclose = () => {
    document.getElementById("status").textContent = "disconnected";
    document.getElementById("message").disabled = true;
    document.getElementById("send-btn").disabled = true;
    document.getElementById("file-input").disabled = true;
    document.getElementById("send-file-btn").disabled = true;
  };
});

function handleFileChunk(body) {
  const chunkRes = e2echat.decodeFileChunk(body);
  if (chunkRes.error) {
    log(`[file] dropped a bad chunk: ${chunkRes.error}`, "err");
    return;
  }
  const chunk = chunkRes.value;
  log(`[file] receiving "${chunk.filename}" from ${session.peerNickname()}: chunk ${chunk.index + 1}/${chunk.total}`);

  const fileRes = reassembler.addChunk(chunk);
  if (fileRes.error) {
    log(`[file] transfer of "${chunk.filename}" failed: ${fileRes.error}`, "err");
    return;
  }
  const file = fileRes.value;
  if (!file) return; // still in progress

  logDownload(
    `[file] received "${file.filename}" (${file.data.length} bytes) from ${session.peerNickname()} — click to download`,
    file
  );
}

function sendMessage() {
  const input = document.getElementById("message");
  const text = input.value;
  if (!text || !session || !established) return;
  const wrapped = unwrap(e2echat.wrapText(new TextEncoder().encode(text)), "wrapText");
  const frame = unwrap(session.encrypt(wrapped), "encrypt");
  ws.send(frame);
  log(`me: ${text}`);
  input.value = "";
}
document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("message").addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});

async function sendFile() {
  if (!session || !established) return;
  const fileInput = document.getElementById("file-input");
  const file = fileInput.files[0];
  if (!file) {
    log("choose a file first", "err");
    return;
  }

  const data = new Uint8Array(await file.arrayBuffer());
  const transferID = crypto.randomUUID();
  const mimetype = file.type || "application/octet-stream";
  const chunks = unwrap(e2echat.chunkFile(transferID, file.name, mimetype, data), "chunkFile");

  log(`[file] sending "${file.name}" (${data.length} bytes, ${chunks.length} chunk(s))`);
  for (const chunk of chunks) {
    const wrapped = unwrap(e2echat.wrapFileChunk(chunk), "wrapFileChunk");
    const frame = unwrap(session.encrypt(wrapped), "encrypt");
    ws.send(frame);
  }
  log(`[file] sent "${file.name}"`);
  fileInput.value = "";
}
document.getElementById("send-file-btn").addEventListener("click", () => {
  sendFile().catch(() => {}); // errors are already logged by unwrap()
});
