#!/usr/bin/env python3
"""Give the article pages (the compare/alt pages in English and the nine languages) the homepage's
component styling by replacing their inline <style> block with tools/altpage.css.

Targets: every page with class="page-wrap" + class="tldr" + class="cta-card" (the shared template).
Blog, support, terms and mcp pages use other classes and are left alone.

Run from website/:  python3 tools/apply_altpage_css.py
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
WEB = HERE.parent
CSS = (HERE / "altpage.css").read_text()
CJK_SERIF = {
    "ja": "ui-serif, 'Hiragino Mincho ProN', 'Yu Mincho', 'Noto Serif JP', 'New York', Georgia, serif",
    "ko": "ui-serif, 'Apple SD Gothic Neo', 'Noto Serif KR', 'New York', Georgia, serif",
    "zh": "ui-serif, 'Songti SC', 'PingFang SC', 'Noto Serif SC', 'New York', Georgia, serif",
}


def main():
    n = 0
    for f in sorted(list(WEB.glob("*.html")) + list(WEB.glob("*/*.html"))):
        s = f.read_text()
        if not ('class="page-wrap"' in s and 'class="tldr"' in s and 'class="cta-card"' in s):
            continue
        css = CSS
        lang = f.parent.name if f.parent != WEB else "en"
        if lang in CJK_SERIF:
            css = css.replace("--serif: ui-serif, 'New York', 'Iowan Old Style', Georgia, serif;", f"--serif: {CJK_SERIF[lang]};")
            css = css.replace("letter-spacing: -0.02em; line-height: 1.1;", "letter-spacing: 0; line-height: 1.3;")
        new, k = re.subn(r"  <style>\n.*?\n  </style>", "  <style>\n" + css.rstrip("\n") + "\n  </style>", s, count=1, flags=re.S)
        assert k == 1, f
        if new != s:
            f.write_text(new); n += 1
    print("restyled", n, "pages")


if __name__ == "__main__":
    sys.exit(main())
