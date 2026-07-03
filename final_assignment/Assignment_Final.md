# Final assignment — the coding challenge
## NBS Data-Science Course · Final workshop · Day 2

You will produce one honest, checkable equality finding from data your team has
never seen — and present it to the room. This is everything from the course in
one exercise: directing Claude Code, cleaning and verifying, disaggregating
responsibly, and standing behind a number.

---

## 1. Pick your track

| | Foundation — Georgia | Advanced — Estonia |
|---|---|---|
| Data | **Real** 2024 census tables from Geostat (aggregated Excel) | **Real** Eurostat EU-SILC public use file (microdata, 4 linked files) |
| Core skill | Parsing messy official Excel into tidy data | Survey weights, household vs person level, multi-file joins |
| Brief | `Assignment_Georgia_Census.md` | `Assignment_Estonia_SILC_selfdownload.md` |

**A clean Foundation answer beats a broken Advanced one.** If your team gets
badly stuck, tell a trainer: there is a fallback dataset (a simple synthetic CSV
with a ready-made CLAUDE.md) so you can still present a finding. No shame in it —
the presentation is about *how you know you're right*, not which track you took.

Both briefs, the synthetic-ethnicity template and emergency copies of the data
live in the course repo: **https://github.com/reredan/nbs** (`final_assignment/`
folder). Prefer the original sources — downloading real data is part of the
exercise — but if a site is down, the repo is your lifeline.

## 2. Rules of the road (what the first assignment taught us)

These are the habits from yesterday's debrief. They are now requirements:

1. **Check the toolchain first.** First prompt of the session: *"check that
   Python and pandas are available via uv, and install them if not; tell me
   what you did."*
2. **One canonical data path**, written into your `CLAUDE.md` (exact filename,
   exact spelling — only `CLAUDE.md` is auto-loaded).
3. **Verify the download before anything else.** Row counts, file size, totals
   against a published figure. A wrong file makes everything after it worthless.
4. **No silent cleaning.** Every transformation reported: what changed, how many
   rows/cells affected.
5. **"Show me the code you ran."** If there is no code, there is no finding.
6. **n beside every number.** Small groups get caveats, not headlines.
7. **Describe, don't explain.** Cross-sections show differences, not causes.
   Check every sentence for framing that could stigmatise a group.
8. **Save the script, rerun the script.** Before you present, your whole
   analysis must rerun from the raw file and reproduce your headline number.
   If it doesn't, you don't have a finding yet.

## 3. Which model to use

- **Do the day's work on Opus** — exploring, cleaning, analysing, charting.
  Check what you're actually running with `/model` (remember yesterday: if you
  don't know which model produced your analysis, that's a red flag).
- **The final check runs on Fable.** When your script and finding are ready,
  switch with `/model` to Fable 5 and run one adversarial verification pass:

  > *"Re-read my script and equality report with fresh eyes. Recompute the headline
  > number independently. What would a sceptical statistician attack — wrong
  > denominator, silent cleaning, small n, causal wording, a total that doesn't
  > reconcile? List concrete problems; don't be polite."*

- Fable is the strongest and most expensive model, so **the trainers will
  announce whether the Fable pass is on**, depending on the remaining budget.
  If it's off, run the same pass on Opus in a *fresh session* (fresh eyes matter
  more than the model).
- Fix what the check finds, rerun the script, and only then build your slides.

## 4. What you must produce: a mini equality report

The central deliverable is **`equality_report.md`** — a short equality report
in **Markdown** (not Word), 1–2 pages, written the way a statistics office
would publish it. Structure:

1. **Headline finding** — one plain sentence with the number and the n.
2. **Data** — exact source, download date, reference date, what one row/cell
   represents, and whether anything is synthetic (PUF, fabricated column).
3. **Method** — the pipeline decisions: who is in and out, definitions,
   weights, how invalid/missing values were handled.
4. **Results** — one small table (with an n column) and **one clear chart**.
5. **Limitations** — small groups, missingness, undercount, what the data
   cannot say.
6. **Dissemination text** — see below. This is the section we grade hardest.
7. **Annex: verification** — the checks you ran, and what Claude got wrong.

Alongside the report: your **reproducible script**, the **chart file**, your
**`CLAUDE.md`**, and your **presentation** (section 5).

### The dissemination text (~150 words)

Write the short public-facing text a statistics office would release with this
finding — the paragraph a journalist or ministry official actually reads. Follow
the UNECE guidance on disseminating equality and disaggregated data (the CES
*Guide to Data Disaggregation*, the *Making Data Meaningful* guides, and the
census recommendations on ethno-cultural characteristics). Concretely, your text
must:

- **Respect self-identification**: use the categories and labels people
  reported, not your own shorthand ("persons who reported Armenian as their
  native language", not "the Armenians").
- **Describe outcomes, not group behaviour** — no deficit framing, nothing that
  reads as blaming a group; check the sentence survives being read aloud by a
  journalist about your own community.
- **Carry its evidence**: the indicator definition, the reference date, the
  source, and the group sizes — in words a non-statistician understands.
- **State limits plainly**: small groups, what a count/survey can and cannot
  show, no causal language ("is associated with", never "because").
- **Be plain language**: one message per paragraph, meaningful rounding, no
  jargon (no "AROP", no variable codes).

Ask Claude to draft it, then attack it: *"Read this as a hostile journalist
looking for a stigmatising headline — what would you quote, and how do we fix
it?"*

## 5. The presentation — 5 minutes, 4 slides max

Every team presents at the end of the day. The slides are your report,
condensed — every number on them must trace to it. Format is fixed:

1. **The question** — one sentence, plus what the data is and where you got it.
2. **The chart** — your one chart, full screen. It should carry the story alone.
3. **The finding & the dissemination text** — read your public-facing paragraph
   to the room, exactly as written. The room plays hostile journalist.
4. **"How we know it's right"** — the verification story: what you checked,
   what the sceptic-pass found, and **one thing Claude got wrong today and how
   you caught it**. This slide is the one we'll remember.

Tip: ask Claude Code to build the slides for you (it can generate a PPTX or an
HTML deck from your report) — but every number on them must come from your
rerun script, not from memory of the chat.

## 6. Handing in

When you're done (and before presenting), upload everything from a browser:

> **http://<instructor-ip>:8000** ← the trainer writes the real address on the board

Enter your team name, drop in: `equality_report.md`, script, chart,
`CLAUDE.md`, slides. You can upload as often as you like; nothing is
overwritten. Terminal
fans can use curl instead:

```bash
curl -F team="YOUR TEAM" -F files=@analysis.py -F files=@chart.png http://<instructor-ip>:8000/upload
```

## 7. What "good" looks like

A team that frames one sharp question, gets real data in cleanly, can show the
code behind every number, presents one honest chart with the n on it, and reads
out a dissemination text that respects the people it describes while carrying
its own caveats — and can say what they checked and what the tool got wrong —
has done professional statistical work. Scope is not the
goal; **a small finding you can defend beats a dashboard you can't.**

One warning for strong teams: resist the urge to let Claude produce ten charts,
significance tests and a 20-page report. Unrequested output is scope creep, and
on census data (a full count, not a sample) significance tests are conceptually
wrong anyway. One question, one chart, defended — that's the assignment.
