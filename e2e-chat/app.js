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

function unwrap(result, what) {
  if (result.error) {
    log(`[error] ${what}: ${result.error}`, "err");
    throw new Error(`${what}: ${result.error}`);
  }
  return result.value;
}

let identity = null;
let session = null;
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
      return;
    }

    const res = session.decrypt(bytes);
    if (res.error) {
      log("dropped a message that failed to decrypt/authenticate", "warn");
      return;
    }
    log(`${session.peerNickname()}: ${new TextDecoder().decode(res.value)}`);
  };

  ws.onerror = () => log("websocket error", "err");
  ws.onclose = () => {
    document.getElementById("status").textContent = "disconnected";
    document.getElementById("message").disabled = true;
    document.getElementById("send-btn").disabled = true;
  };
});

function sendMessage() {
  const input = document.getElementById("message");
  const text = input.value;
  if (!text || !session || !established) return;
  const frame = unwrap(session.encrypt(new TextEncoder().encode(text)), "encrypt");
  ws.send(frame);
  log(`me: ${text}`);
  input.value = "";
}
document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("message").addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});
