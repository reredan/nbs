# Final assignment — one finding, honestly reported
## NBS Data-Science Course · Final workshop · Day 2

Produce **one equality finding** from real data, write it up as a short
**equality report with dissemination text**, and present it in 5 minutes.

## 1. Pick a track

- **Foundation — Georgia**: real 2024 census Excel tables → tidy data → a
  linguistic-integration indicator. Brief: `Assignment_Georgia_Census.md`.
- **Advanced — Estonia**: real Eurostat EU-SILC microdata → weighted poverty or
  income gap by citizenship. Brief: `Assignment_Estonia_SILC_selfdownload.md`.

A clean Foundation answer beats a broken Advanced one. Stuck? Tell a trainer —
there's a fallback dataset so you can still present. Briefs and emergency data
copies: **https://github.com/reredan/nbs** (`final_assignment/`).

## 2. Ground rules (from yesterday's debrief)

1. **Verify the download first** — row counts / totals against a published figure.
2. **No silent cleaning** — every change reported. If there's no code, there's no finding.
3. **n beside every number**; small groups get caveats, not headlines.
4. **Describe, don't explain** — no causes, no framing that could stigmatise.
5. **Save the script and rerun it** — your headline number must reproduce
   from the raw file before you present.

Work on **Opus**. When your finding is ready, switch (`/model`) to **Fable** —
if the trainers say the budget allows; otherwise a fresh Opus session — and run
one sceptic pass: *"Recompute my headline number independently. What would a
sceptical statistician attack? Don't be polite."* Fix what it finds.

## 3. The deliverable: `equality_report.md`

One page, **Markdown**, written like a statistics office would publish it:

1. **Headline finding** — one plain sentence, the number, the n.
2. **Data & method** — source and download date; who is in and out; how
   missing/invalid values and weights were handled; what is real vs synthetic.
3. **Results** — one small table with an n column, one clear chart.
4. **Limitations** — small groups, what this data cannot say.
5. **Dissemination text** (~150 words) — the section we grade hardest.

### The dissemination text

The paragraph a journalist or ministry official actually reads — written to the
UNECE guidance on disseminating equality data:

- **Self-identification**: use the categories people reported ("persons who
  reported Armenian as their native language"), not shorthand ("the Armenians").
- **Outcomes, not group behaviour** — nothing that reads as blame.
- **Evidence in-text**: indicator, date, source, group sizes — in plain words,
  no jargon or variable codes.
- **Limits stated, no causal language** ("is associated with", never "because").

Then attack it: *"Read this as a hostile journalist looking for a stigmatising
headline — what would you quote, and how do we fix it?"*

## 4. Present — 5 minutes, 4 slides

1. **Question** — and what the data is.
2. **The chart** — full screen; it should carry the story alone.
3. **Dissemination text** — read it aloud, exactly as written. The room plays
   hostile journalist.
4. **How we know it's right** — what you checked, and one thing Claude got
   wrong today.

## 5. Hand in

Open **http://\<instructor-ip\>:8000** (address on the board), enter your team
name, upload: `equality_report.md`, script, chart, `CLAUDE.md`, slides.

*One warning for fast teams: ten charts and significance tests are scope creep —
and on census data (a full count) significance tests are wrong anyway. One
question, one chart, defended.*
