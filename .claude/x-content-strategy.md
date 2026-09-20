# X (Twitter) Content Strategy — MirrorNotes

Goal priority, in order:
1. Followers (primary)
2. Content people genuinely like
3. Eligibility for X's Original Content Rewards Program
4. Money (explicitly last)

Constraint: **no on-camera video.** Every format below works with text,
screenshots, charts, screen recordings of the app, and terminal output.

---

## 0. Program facts (verify before relying on them)

X replaced Creator Revenue Sharing with the **Original Content Rewards
Program** in Aug–Sep 2026. Details gathered from reporting and search
summaries — `help.x.com` was not directly reachable from this environment,
so **confirm on the official help page before making decisions**:
https://help.x.com/en/using-x/original-content-rewards

Reported gates:

| Gate | Reported value |
| --- | --- |
| Verified followers | 500 (followers who are Premium subscribers) |
| Qualified impressions | 500,000 in trailing 90 days |
| Subscription | Premium / Premium+ / Premium Business |
| Age / region | 18+, supported region |
| Payout cadence | every 2 weeks, $30 minimum |

**Qualified impression** = unique impression, from a *Premium* user, on the
*Home Timeline*, with ≥50% of the post visible. Excluded: replies, repeat
impressions from the same account, paid/promoted, artificial.

### The two things most people get wrong

1. **Replies do not count toward the 500K.** Replies are still the single
   best follower-growth tool on X — but they earn nothing and count for
   nothing. Treat replies as the acquisition channel and original posts as
   the monetized channel. Do not conflate them.

2. **Qualified impressions are a small slice of total impressions.** Only
   Premium users, only Home Timeline, only ≥50% visible. X does not publish
   the ratio. A working assumption of **5–15%** of total impressions is a
   guess, not a fact — but if it is roughly right, 500K qualified over 90
   days implies somewhere around **3–10M total impressions per quarter**.
   Track your own ratio in analytics once payouts start and replace this
   guess with the real number.

   The good news: that ratio is *audience-dependent*, and the audiences
   MirrorNotes naturally speaks to — iOS devs, ML engineers, indie hackers,
   privacy people — are unusually Premium-dense. A tech audience is worth
   several times a general audience under this scoring.

### Originality standard

Qualifies: commentary, analysis, reaction, memes, creative interpretation —
*when you add perspective, expertise, humor, or context.*

Does not qualify: content copied wholesale; content "minimally modified"
(a word changed, a filter, a text overlay, a speed change); aggregated
content that compiles others' work without substantial new framing;
material downloaded from another platform and reuploaded; content generated
by automated means.

**Implication:** the generic-advice / quote-graphic / thread-aggregator
playbook is exactly what this program was built to stop paying. Every
pillar below is deliberately built on material only the person who built
MirrorNotes can produce.

---

## 1. The account question: use your real, single, named account

**Recommendation: one account, your real name, openly the builder of
MirrorNotes.** Not an alt, not a pseudonym, not a brand-only account.

Reasons, strongest first:

1. **Your unfair advantage is non-transferable.** "I ran a 1B model on an
   iPhone for 30 days, here is the battery data" is only interesting
   because you did it. An anonymous account posting the same numbers is
   asking to be believed; you are showing receipts. Authority is the whole
   asset, and an alt throws it away.

2. **The program now scores exactly what an alt is bad at.** Originality,
   authenticity, first-person contribution. A persona account drifts toward
   aggregation because it has no proprietary material to draw on.
   Aggregation is now explicitly disqualified.

3. **Verified followers come faster from a builder identity.** The 500
   verified-follower gate is the one most people stall on. Premium
   subscribers on X skew toward devs, founders, and ML people — precisely
   the crowd that follows people who ship things. They do not follow
   faceless quote accounts.

4. **You are one person.** Two accounts halve your posting quality and
   double your overhead. Nothing about your content needs distance from
   your name.

5. **"No video of yourself" costs you nothing here.** The formats that win
   in this niche — packet captures, Instruments traces, charts, code,
   screen recordings of the app — have no face in them anyway. A talking
   head would actually be *off-register* for this audience.

**Personal account vs. a @MirrorNotes brand account:** run the personal one
as primary. People follow people. Keep a brand account if you like, but as
a low-effort utility: release notes, status, support replies. Do not split
your real content across both.

**When an alt would actually be correct** — only these cases:
- You need separation from an employer, visa/immigration situation, or
  family for reasons unrelated to the product.
- You want to run a deliberately high-volume, low-personal-stake content
  account as a *separate business*, accepting that it will be weaker under
  the new originality rules.

Neither appears to apply. Use your name.

One caveat worth being clear-eyed about: posting privacy teardowns under
your real name means criticism lands on you personally, and the privacy
niche on X argues hard. Section 3 covers how to make that survivable.

---

## 2. Positioning

> The developer who put a language model *inside* an iPhone so that nobody —
> including him — can read your journal.

That is a genuinely scarce identity on X. It sits on top of three trends
that all have large, Premium-heavy audiences: on-device/small-model AI,
privacy vs. Big Tech, and indie building-in-public. Almost nobody occupies
the intersection.

Bio should say, plainly: what you build, what makes it unusual, and one
proof point. Pin a post that is a *demonstration*, not a pitch.

Optimize for **follow-rate per impression**, not impressions. A post that
reaches 2M general-audience people and converts 0.05% is worse for your
actual goal than one that reaches 200K engineers and converts 2%. This
matters because the primary goal is followers, and it is the most common
way people waste a viral hit.

---

## 3. Content pillars

Suggested mix per week: 40% Pillar A, 20% B, 20% C, 10% D, 10% E.

### Pillar A — On-device AI engineering receipts (highest value)

The most under-supplied, most Premium-dense content available to you.
Hard to fake, impossible to aggregate, trivially originality-compliant.

Post ideas:
- "I ran Gemma 3 1B on an iPhone every day for 30 days. Here's the battery
  cost." — one chart, real numbers, methodology in the replies.
- Tokens/sec across A17 Pro vs A18 vs A18 Pro. Table. No adjectives.
- Quantization ladder: what actually breaks at Q4 vs Q8 for journaling
  summarization, with side-by-side model outputs on the same input.
- Thermal throttling curve during a Monthly Deep Report generation.
- Memory ceiling: what iOS kills you at, and how you stay under it.
- "CoreML vs llama.cpp on the same model, same device" — with the numbers
  that made you choose.
- The Neural Engine's actual constraints, written for people who have only
  ever deployed to a GPU.
- A postmortem of a specific inference bug, with the Instruments trace.
- Prompt-engineering-for-1B-models: what works at 1B that does not at 70B.
- Cost comparison: on-device inference at $0/request vs what the same
  feature would cost on an API at your user count. Show the arithmetic.

Format: screenshot of a chart or a trace + 3–6 lines of plain text. Put
methodology in the first reply so critics have something to engage with
rather than something to dunk on.

### Pillar B — Proof-of-privacy artifacts

Your strongest *shareable* asset, because it is a demonstration rather than
a claim.

- Screen recording: phone in airplane mode, full AI reflection generated,
  no network. 15 seconds. No narration needed.
- Packet capture (Charles / Little Snitch / Proxyman) over a full session,
  showing zero journal bytes leaving. Post the capture, invite people to
  reproduce it.
- "Here is how to verify my claim yourself, in 4 steps" — this is the post
  that earns the privacy crowd permanently.
- A standing offer: "if anyone catches MirrorNotes sending journal text
  anywhere, I'll say so publicly and refund everyone." Only post this if
  you mean it; it is the highest-trust, highest-risk post in the deck.

### Pillar C — Privacy teardowns (highest reach, highest risk)

Your existing blog posts — encryption theater, what a journal app can be
subpoenaed for, your therapist has confidentiality — are the seeds. This
pillar reaches the furthest and is the one most likely to cause trouble.

Rules for doing it safely:
- **Quote verbatim, screenshot the source, link the source, date it.**
- **State facts; let readers draw the conclusion.** Zero adjectives about
  the other company. "Clause 7.2 says X" beats "they're lying."
- **Punch up or sideways, never down.** Large platforms and category-wide
  practices are fair comment. Do not build an audience by attacking small
  indie competitors; it reads badly and it is a bad neighborhood to live in.
- Correct yourself publicly and fast if you get a detail wrong. One
  retraction buys more credibility than ten accusations.

Post ideas:
- "What 'end-to-end encrypted' means in journaling apps, and the three
  places it usually isn't." Category-level, no names needed.
- A plain-English annotated read of one *large* platform's data retention
  clause.
- "What a court order to a journaling company can actually reach" — your
  strongest piece; it's a genuine public-interest explainer.
- Therapist confidentiality vs. app terms of service, as a comparison table.
- "Your mood data is health data everywhere except in your app's privacy
  policy."

### Pillar D — Build-in-public numbers

The indie-hacker audience on X is huge and Premium-dense, and it rewards
honesty over success.

- Your programmatic SEO story is genuinely good content: ~99 landing pages
  across 9 locales, shipped on an automated loop. Post the traffic curve at
  90 days — *including* the pages that got zero.
- MRR, conversion, churn, refund rate. Real charts.
- "What it costs to ship an on-device AI app solo."
- App Store review rejections and how you got past them.
- Failures explicitly: the pricing experiment that lost money, the feature
  nobody used, the locale that flopped.
- "Why I wait 7 days before showing any AI" — a product-decision post; you
  already have the argument written.

### Pillar E — Counter-consensus AI takes

Reply-generating, cheap to produce, keeps you visible between heavier posts.

- "A 1B model on your phone beats a frontier model in the cloud — for this
  specific job. Here's where the line is."
- "Most AI products are a prompt and a database. Mine is too. The
  difference is where it runs."
- "On-device is not a privacy feature. It's an architecture that makes the
  privacy promise unbreakable. Those are different things."
- "The cloud AI journaling business model requires reading your journal.
  That's not a bug in their ethics, it's a line item."

Have an actual argument. Do not post bait you cannot defend in the replies —
the replies are where followers are won.

---

## 4. Mechanics

**Replies are the growth engine.** 10–20 substantive replies/day to
accounts in on-device ML, iOS dev, privacy, and indie hacking. Be early
(first 10 minutes) and add something — a number, a correction, a
counter-example. Never "great post." Replies do not earn, but they are how
people find your profile.

**Original posts are the earning engine.** 1–3/day. Every one should be
something only you could write.

**Long-form Articles** (Premium feature) are worth testing for the
teardowns and the engineering deep dives — they keep the reader on X, which
the Home-Timeline impression model rewards. Repurpose the existing blog
posts rather than writing new ones.

**Repurpose everything you already have.** The blog is eight solid posts.
Each one is 5–10 X posts. That's your first six weeks of Pillar C and D
with no new research.

**Do not:** buy followers, use engagement pods, run reply-bait loops, or
automate posting. All of it is explicitly named as disqualifying, and
suspension from the program is the stated penalty.

---

## 5. Expectations

Be honest with yourself about the timeline:

- **Weeks 1–8:** 500 verified followers is the real first gate. Reply
  volume, not post volume, gets you there.
- **Months 2–6:** first genuinely large post — realistically a Pillar B
  proof artifact or a Pillar C teardown. Single posts reaching 1M+ are
  achievable a few times a year in this niche.
- **Months 6–12:** 500K qualified impressions/90 days becomes plausible
  *if* the audience is tech-heavy.

"Millions of people" is a reachable outcome, but it arrives as a few
outlier posts on top of a consistent base — not as a repeatable weekly
result. Anyone promising otherwise is selling something.

Measure weekly: follows per 1,000 impressions; qualified-to-total
impression ratio; verified follower count. The first is the goal, the
second is the payout, the third is the gate.

---

## Sources

- https://help.x.com/en/using-x/original-content-rewards (official — verify here)
- https://help.x.com/en/using-x/creator-revenue-sharing
- https://techcrunch.com/2026/08/08/x-replaces-misaligned-revenue-sharing-program-with-original-content-rewards/
- https://www.tubefilter.com/2026/08/11/x-monetization-original-content-rewards-program-creators/
- https://influencermarketinghub.com/x-is-turning-creator-monetization-into-an-originality-test/
- https://www.techi.com/x-original-content-rewards-premium-impressions/
