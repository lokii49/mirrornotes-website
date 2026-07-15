# SEO Loop State

## Backlog

Locale gap matrix — English SEO pages × locale dirs missing translations.
Pages: day-one-alternative, rosebud-alternative, reflect-alternative, adhd-journaling-app, offline-journal-app, private-journal-app
Locales: es, fr, de, it, pt, ja, ko, ru, zh

Priority order: work through locales left-to-right, one page per locale per pass, then move to the next page.

- [x] day-one-alternative × es (shipped 2026-07-07)
- [x] day-one-alternative × fr (shipped 2026-07-08)
- [x] day-one-alternative × de (shipped 2026-07-09)
- [x] day-one-alternative × it (shipped 2026-07-10)
- [x] day-one-alternative × pt (shipped 2026-07-11)
- [x] day-one-alternative × ja (shipped 2026-07-12)
- [x] day-one-alternative × ko (shipped 2026-07-13)
- [x] day-one-alternative × ru (shipped 2026-07-14)
- [x] day-one-alternative × zh (shipped 2026-07-15)
- [ ] rosebud-alternative × es
- [ ] rosebud-alternative × fr
- [ ] rosebud-alternative × de
- [ ] rosebud-alternative × it
- [ ] rosebud-alternative × pt
- [ ] rosebud-alternative × ja
- [ ] rosebud-alternative × ko
- [ ] rosebud-alternative × ru
- [ ] rosebud-alternative × zh
- [ ] reflect-alternative × es
- [ ] reflect-alternative × fr
- [ ] reflect-alternative × de
- [ ] reflect-alternative × it
- [ ] reflect-alternative × pt
- [ ] reflect-alternative × ja
- [ ] reflect-alternative × ko
- [ ] reflect-alternative × ru
- [ ] reflect-alternative × zh
- [ ] adhd-journaling-app × es
- [ ] adhd-journaling-app × fr
- [ ] adhd-journaling-app × de
- [ ] adhd-journaling-app × it
- [ ] adhd-journaling-app × pt
- [ ] adhd-journaling-app × ja
- [ ] adhd-journaling-app × ko
- [ ] adhd-journaling-app × ru
- [ ] adhd-journaling-app × zh
- [ ] offline-journal-app × es
- [ ] offline-journal-app × fr
- [ ] offline-journal-app × de
- [ ] offline-journal-app × it
- [ ] offline-journal-app × pt
- [ ] offline-journal-app × ja
- [ ] offline-journal-app × ko
- [ ] offline-journal-app × ru
- [ ] offline-journal-app × zh
- [ ] private-journal-app × es
- [ ] private-journal-app × fr
- [ ] private-journal-app × de
- [ ] private-journal-app × it
- [ ] private-journal-app × pt
- [ ] private-journal-app × ja
- [ ] private-journal-app × ko
- [ ] private-journal-app × ru
- [ ] private-journal-app × zh

Once locale matrix is full, move to new English keyword pages (candidates: apple-journal-alternative, journey-alternative, stoic-alternative, ai-journal-app, gratitude-journal-app).

## Log

- 2026-07-07: Shipped es/day-one-alternative.html — full Spanish translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy). Structure/CSS byte-identical to English source. Nav-back and footer "Inicio"/"Privacidad" link within es/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages (no es equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.
- 2026-07-08: Shipped fr/day-one-alternative.html — full French translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy). Structure/CSS byte-identical to English source. Nav-back and footer "Accueil"/"Confidentialité" link within fr/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no fr equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.
- 2026-07-09: Shipped de/day-one-alternative.html — full German translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy), terminology matched to existing de/index.html and de/privacy.html ("Startseite", "Datenschutz"). Structure/CSS byte-identical to English source. Nav-back and footer "Startseite"/"Datenschutz" link within de/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no de equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.
- 2026-07-10: Shipped it/day-one-alternative.html — full Italian translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy), terminology matched to existing it/index.html ("Diario", "Privacy", "Scarica"). Structure/CSS byte-identical to English source. Nav-back and footer "Home"/"Privacy" link within it/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no it equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.
- 2026-07-11: Shipped pt/day-one-alternative.html — full Brazilian Portuguese translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy), terminology matched to existing pt/index.html and pt/privacy.html ("Início", "Privacidade", "Diário", "TDAH" for ADHD). Structure/CSS byte-identical to English source (verified byte-diff on style block). Nav-back and footer "Início"/"Privacidade" link within pt/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no pt equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.
- 2026-07-12: Shipped ja/day-one-alternative.html — full Japanese translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy), terminology matched to existing ja/index.html and ja/privacy.html ("日記", "オンデバイス", "デイリーナッジ", "ホーム", "プライバシー"). Structure/CSS byte-identical to English source (verified byte-diff on style block). Nav-back and footer "ホーム"/"プライバシー" link within ja/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no ja equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.
- 2026-07-13: Shipped ko/day-one-alternative.html — full Korean translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy), terminology matched to existing ko/index.html and ko/privacy.html ("일기", "온디바이스", "데일리 넛지", "저널에게 물어보기", "홈", "개인정보"). Structure/CSS byte-identical to English source (verified via python3 html.parser + meta/JSON-LD/link checks). Nav-back and footer "홈"/"개인정보" link within ko/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no ko equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.

- 2026-07-14: Shipped ru/day-one-alternative.html — full Russian translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy), terminology matched to existing ru/index.html and ru/privacy.html ("Дневник", "на устройстве", "Ежедневная подсказка", "Спросите свой дневник", "Главная", "Конфиденциальность", "СДВГ" for ADHD). Structure/CSS byte-identical to English source (verified via diff on style block + python3 html.parser + JSON-LD parse). Nav-back and footer "Главная"/"Конфиденциальность" link within ru/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no ru equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.
- 2026-07-15: Shipped zh/day-one-alternative.html — full Simplified Chinese translation of day-one-alternative.html (title, meta, OG, FAQ JSON-LD, all visible copy), terminology matched to existing zh/index.html and zh/privacy.html ("每日启发" for Daily Nudge, "向日记提问" for Ask your journal, "情绪时间线", "每周摘要", "首页", "隐私"). Used full-width Chinese punctuation (，。；：「」) throughout to match zh/index.html style. Structure/CSS byte-identical to English source (verified via diff on style block + python3 html.parser + JSON-LD parse). Nav-back and footer "首页"/"隐私" link within zh/ (both exist); "vs Rosebud"/ADHD/Offline footer links point to English root pages via ../ (no zh equivalents yet). No hreflang added (English source page has none). Added to sitemap.xml, validated with xmllint.

## Blocked

(none)
