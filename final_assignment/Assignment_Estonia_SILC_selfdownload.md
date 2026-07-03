# Advanced track — Estonia
## A weighted equality indicator from real EU-SILC microdata

**For confident teams only.** Real Eurostat microdata: multi-file structure,
coded variables, survey weights. If in doubt, take the Georgia track — a clean
answer there beats a broken one here.

## 1. Get the data

From Eurostat's public microdata page (verified 2026-07-03; trainers have a USB copy):
`https://ec.europa.eu/eurostat/web/microdata/public-microdata/statistics-on-income-and-living-conditions`

Download **`EE_PUF_EUSILC.zip`** and the **codebook/metadata** next to it. The
zip holds **ten years (2004–2013)** — pick **one** (2013 is a sensible default).
Each year has four linked CSVs: **D** (household register), **H** (household),
**R** (personal register), **P** (personal, 16+ only).

## 2. Understand before you compute

Answer these with Claude Code first — each hides a trap:

- Which ID columns link households to persons?
- Which **weight** applies to which unit? (The register weight covers everyone;
  the personal-data weight covers only 16+.)
- Where is **equivalised disposable income**? Check your candidate column
  **actually contains data** — some PUF columns are empty shells that parse
  fine and quietly poison everything downstream. If it's empty, derive it from
  the H file (total disposable income ÷ equivalised household size).
- Which integration variables really exist here? (Citizenship `PB220A`:
  EE / EU / Other, 16+ only. Country of birth is **not** in the PUF; region is
  anonymised to a constant.)

Two hard rules: **all population estimates weighted**, and **equivalised income
is a household attribute** — one value per household, never averaged over
individuals as if personal.

## 3. The equality dimension

- **Option A (recommended):** use real **citizenship** (`PB220A`).
- **Option B:** fabricate a household-level **synthetic ethnicity** with the
  provided `add_synthetic_ethnicity_silc.py` (run it next to the extracted
  CSVs). It correlates with citizenship and is labelled `_SYNTHETIC` — keep
  that label in every output.

Either way, **state in your report which it is — real or fabricated.** That
honesty is part of the exercise.

## 4. Compute one question

Weighted, with unweighted n shown beside every estimate:

- **At-risk-of-poverty rate** (equiv. income < 60% of the weighted median) by
  citizenship / synthetic ethnicity, **or**
- weighted **median income gap** or **activity-status gap** across the dimension.

Then the equality report, chart and sceptic pass per `Assignment_Final.md`.

## 5. Honest caveats to carry

- The PUF is **synthetic and not for inference** — your finding describes the
  file, not Estonia. Don't be surprised if it mismatches Eurostat's published
  figures; say so in the report.
- Caveat small groups (one citizenship group is tiny — check before headlining it).
- Describe differences; don't explain causes; check framing for stigma.
