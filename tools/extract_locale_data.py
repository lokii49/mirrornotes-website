#!/usr/bin/env python3
"""Pull the per-language sample journals, the app's fixed reflection/digest/Ask phrasing,
the translated mood names and the current page metadata into tools/locale-data.json.

Sources (the app repo, a sibling of website/):
  mirror/mirror/Core/Utilities/StoreDemoSeed.swift   the demo journals (StoreDemoSeed.demos)
  mirror/mirror/Core/Services/InsightService.swift  groundedLocales + weeklyDigestSectionLabels
  mirror/mirror/Localizable.xcstrings               mood names

Run from website/:  python3 tools/extract_locale_data.py
Then build the pages: python3 tools/build_locales.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
WEB = HERE.parent
APP = WEB.parent / "mirror" / "mirror"
CODES = ["de", "es", "fr", "it", "pt", "ja", "ko", "ru", "zh"]
XC = {"de": "de", "es": "es", "fr": "fr", "it": "it", "pt": "pt-BR", "ja": "ja", "ko": "ko", "ru": "ru", "zh": "zh-Hans"}
MOODS = ["Joyful", "Grateful", "Peaceful", "Content", "Energized", "Hopeful", "Anxious", "Overwhelmed", "Frustrated", "Drained", "Sad", "Numb"]


def unesc(s):
    s = re.sub(r"\\u\{([0-9A-Fa-f]+)\}", lambda m: chr(int(m.group(1), 16)), s)
    return s.replace('\\"', '"').replace("\\n", "\n").replace("\\'", "'").replace("\\\\", "\\")


def strs(block):
    return [unesc(m) for m in re.findall(r'"((?:[^"\\]|\\.)*)"', block)]


def demo(seed, code):
    body = re.search(r'"%s": Demo\((.*?)\n        \),?\n' % code, seed, re.S).group(1)

    def field(name):
        m = re.search(name + r':\s*(\[.*?\]|"(?:[^"\\]|\\.)*")\s*,?\s*\n', body, re.S)
        return m.group(1) if m else None

    d = {}
    for f in ["entries", "tags", "digestPicks", "englishDigest", "askQuotes", "checklist"]:
        v = field(f)
        d[f] = strs(v) if v else []
    for f in ["reflectionQuote", "feeling", "askQuestion", "askAnswer", "draftTitle", "draftBody"]:
        v = field(f)
        d[f] = strs(v)[0] if v and strs(v) else ""
    return d


def grounded(svc, code):
    gl = re.search(r"static let groundedLocales: \[String: GroundedLocale\] = \[(.*?)\n    \]\n", svc, re.S).group(1)
    body = re.search(r'"%s": GroundedLocale\((.*?)\n        \),?' % code, gl, re.S).group(1)

    def s(name):
        m = re.search(r"\n\s+" + name + r': ("(?:[^"\\]|\\.)*")', body)
        return strs(m.group(1))[0] if m else None

    def d(name, key):
        m = re.search(r"\n\s+" + name + r": \[(.*?)\],?\n", body, re.S)
        if not m:
            return None
        mk = re.search(r"\." + key + r': (\[(?:[^\]]*)\]|"(?:[^"\\]|\\.)*")', m.group(1), re.S)
        vals = strs(mk.group(1)) if mk else []
        return vals[0] if vals else None

    def l(name):
        m = re.search(r"\n\s+" + name + r": \[(.*?)\],?\n", body, re.S)
        return strs(m.group(1)) if m else []

    return dict(open=s("open"), close=s("close"), joiner=s("joiner"), youWrote=s("youWrote"),
                feelGood=d("feel", "good"), themeGood=d("theme", "good"), energyHard=s("energyHard"), energyGood=s("energyGood"),
                buildingSuffix=s("buildingSuffix"), watchSuffix=s("watchSuffix"), boostGood=d("boost", "good"), nextWeekGood=d("nextWeek", "good"),
                askPrefix=s("askPrefix"), followUp=l("followUpQuestion"))


def digest_labels(svc):
    block = re.search(r"static let weeklyDigestSectionLabels: \[\[String: String\]\] = \[(.*?)\n    \]\n", svc, re.S).group(1)
    out = []
    for grp in re.findall(r"\[(.*?)\]", block, re.S):
        out.append(dict(re.findall(r'"([a-z]{2})": "([^"]*)"', grp)))
    return out


def head(code):
    h = (WEB / code / "index.html").read_text()

    def g(pat):
        m = re.search(pat, h)
        return m.group(1) if m else None

    m = re.search(r"const PROMPTS = \[(.*?)\];", h, re.S)
    prompts = [p.replace('\\"', '"') for p in re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))] if m else []
    return dict(lang=g(r'<html lang="([^"]+)"'), title=g(r"<title>([^<]+)</title>"), description=g(r'<meta name="description" content="([^"]+)"'),
                ogTitle=g(r'<meta property="og:title" content="([^"]+)"'), ogDesc=g(r'<meta property="og:description" content="([^"]+)"'),
                twTitle=g(r'<meta name="twitter:title" content="([^"]+)"'), twDesc=g(r'<meta name="twitter:description" content="([^"]+)"')), prompts


def main():
    seed = (APP / "Core/Utilities/StoreDemoSeed.swift").read_text()
    svc = (APP / "Core/Services/InsightService.swift").read_text()
    xc = json.load(open(APP / "Localizable.xcstrings"))
    labels = digest_labels(svc)
    out = {"digestLabels": labels}
    for code in CODES:
        hd, prompts = head(code)
        out[code] = {
            "demo": demo(seed, code),
            "g": grounded(svc, code),
            "moods": {m: (xc["strings"].get(m, {}).get("localizations", {}).get(XC[code], {}).get("stringUnit", {}).get("value") or m) for m in MOODS},
            "head": hd,
            "prompts": prompts,
            "pages": sorted(p.name for p in (WEB / code).glob("*.html")),
        }
        d = out[code]["demo"]
        assert len(d["entries"]) == 18 and d["reflectionQuote"] in d["entries"][0] and len(d["digestPicks"]) == 3 and len(prompts) == 30, code
    (HERE / "locale-data.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print("wrote", HERE / "locale-data.json", "for", ", ".join(CODES))


if __name__ == "__main__":
    sys.exit(main())
