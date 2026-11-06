"""Re-skin mirrornotes.org from the violet theme to Plum & Paper (app commit 8219b52).
Pass 1 rewrites whole token lines by role (some old hexes had two roles); pass 2 maps
remaining literals. Run from the website repo root."""
import re, subprocess, sys
SKIP = ("e2e-chat/", "timer/", "shipra/", "partners/", "timer.html", "node_modules/")
files = [f for f in subprocess.run(["git","ls-files"],capture_output=True,text=True).stdout.split("\n")
         if re.search(r"\.(html|css|svg|webmanifest)$", f) and not f.startswith(SKIP)]

LINES = [  # exact token lines (role-aware)
 ("--bg: #F2EEF8; --surface: #FFFFFF; --surface2: #F8F5FF; --surface3: #EDE8FC;",
  "--bg: #F6F2F3; --surface: #FFFFFF; --surface2: #FAF6F8; --surface3: #F4E4EE;"),
 ("--accent: #6341CC; --accent-lt: #7C5CE4; --accent-btn: #6341CC; --accent-btn-hover: #7C5CE4; --accent-tint: rgba(99,65,204,0.10);",
  "--accent: #8E3A6E; --accent-lt: #9B4C85; --accent-btn: #8E3A6E; --accent-btn-hover: #9A4478; --accent-tint: rgba(142,58,110,0.10);"),
 ("--text: #16112A; --text-2: #5B5170; --text-3: #6E6587;",
  "--text: #1D1419; --text-2: #61525C; --text-3: #71636B;"),
 ("--bg: #08060F; --surface: #110E1C; --surface2: #1C1830; --surface3: #241F3D;",
  "--bg: #0E0A0D; --surface: #1A1418; --surface2: #241C22; --surface3: #31252F;"),
 ("--accent: #8B6CF0; --accent-lt: #A78BFA; --accent-btn: #6E4FE0; --accent-btn-hover: #7C5CE4; --accent-tint: rgba(139,108,240,0.16);",
  "--accent: #C98BC6; --accent-lt: #D8A3D4; --accent-btn: #8A3769; --accent-btn-hover: #9A4478; --accent-tint: rgba(201,139,198,0.16);"),
 ("--text: #EDE9F8; --text-2: #A39BC0; --text-3: #9087B0;",
  "--text: #F0E8EC; --text-2: #AB9CA8; --text-3: #9C8D99;"),
 ('cg.addColorStop(0, "#A78BFA"); cg.addColorStop(1, "#5B3FC2");',
  'cg.addColorStop(0, "#DDA9D9"); cg.addColorStop(1, "#8A3769");'),
]
LIT = {  # remaining literals, one role each
 "#6341CC":"#8E3A6E", "#8B6CF0":"#C98BC6", "#7C5CE4":"#9A4478", "#A78BFA":"#D8A3D4", "#6E4FE0":"#8A3769",
 "#F2EEF8":"#F6F2F3", "#F8F5FF":"#FAF6F8", "#EDE8FC":"#F4E4EE",
 "#08060F":"#0E0A0D", "#110E1C":"#1A1418", "#1C1830":"#241C22", "#241F3D":"#31252F",
 "#16112A":"#1D1419", "#5B5170":"#61525C", "#6E6587":"#71636B", "#8E85A8":"#71636B",
 "#EDE9F8":"#F0E8EC", "#A39BC0":"#AB9CA8", "#9087B0":"#9C8D99", "#7A7098":"#9C8D99",
}
RGBA = {"99,65,204":"142,58,110", "139,108,240":"201,139,198", "237,233,248":"240,232,236",
        "22,17,42":"29,20,25", "40,24,90":"52,24,42", "8,6,15":"14,10,13", "242,238,248":"246,242,243",
        "250,249,246":"246,242,243"}
lit_re = re.compile("|".join(map(re.escape, LIT)), re.I)
rgba_re = re.compile(r"rgba\(\s*(" + "|".join(re.escape(k).replace(",", r",\s*") for k in RGBA) + r")\s*,", re.I)
changed = 0
for f in files:
    t = open(f, encoding="utf8").read(); o = t
    for a, b in LINES: t = t.replace(a, b)
    t = lit_re.sub(lambda m: LIT[m.group(0).upper()], t)
    t = rgba_re.sub(lambda m: "rgba(" + RGBA[re.sub(r"\s", "", m.group(1))] + ",", t)
    if t != o: open(f, "w", encoding="utf8").write(t); changed += 1
print("files changed:", changed)
