# Assignment — Advanced track (EU-SILC, self-sourced)
## Find real EU microdata, add an equality dimension, and analyse it properly
### NBS Data-Science Course — final workshop coding challenge

**This track is for confident teams only.** It involves finding and downloading real EU microdata, understanding a complex multi-file structure, and analysing it with survey weights. If your team isn't comfortable, take the Georgia track — a clean answer there beats a broken advanced one here.

**Trainers: keep a pre-downloaded copy of one country's PUF on a USB stick as a fallback.** If a team burns 45 minutes fighting the download, hand it over so they can get to the analysis.

---

## 1. Find and download the data (a real skill in itself)

Eurostat publishes **EU-SILC public use files (PUFs)** — fully synthetic microdata that mirror the structure and variable names of the real survey, published for training. Your first task is to find them.

- Start at Eurostat's microdata pages and look for **public microdata → EU-SILC**. The direct page is:
  `https://ec.europa.eu/eurostat/web/microdata/public-microdata/statistics-on-income-and-living-conditions`
- Download the PUF zip for **one country** (e.g. `EE_PUF_EUSILC.zip` for Estonia, or `HU_PUF_EUSILC.zip` for Hungary). Check the availability table for what exists. (Link verified 2026-07-03; the trainers also have the Estonia zip on a USB stick.)
- Unzip it. The zip holds **many years** (Estonia: 2004–2013), with **four CSV files per year**:
  - **D** — household register, **H** — household data, **R** — personal register, **P** — personal data.
  - **Pick one year** (the latest is a sensible default) and say which you picked.

**Reality checks as you go** (this is where the learning is):
- These files use coded variable names (e.g. `PB040` = personal weight, `PL031` = activity status). You will need the **metadata / codebook** to know what each column means — download it alongside the data.
- **The PUF is a stripped-down version of the full survey.** Don't assume a variable from the full SILC codebook exists here — check. Some columns are missing entirely, and some that exist are **empty shells** (they parse fine and contain nothing). Before you build on any column, verify it actually contains data — a column that is 100% blank will not throw an error, it will just quietly poison everything downstream. If a variable you need is empty, look for the documented components it is derived from and compute it yourself.
- **Region is anonymised in the PUF** (a single constant value), so regional breakdowns are not possible on this track.

---

## 2. Understand the structure before you analyse

Ask Claude Code to help you answer these before computing anything:
- Which file is which level — **household** vs **individual**? What are the ID columns that link them?
- Where are the **survey weights**, and which weight applies to which unit? (Watch out: the register weight covers all persons; the personal-data weight covers only those aged 16+.)
- Where is **equivalised disposable income** (a household attribute)? Check the obvious candidate *actually contains data* — if not, derive it from total household disposable income and the equivalised household size (both are in the H file).
- What real **integration-relevant** variables actually exist in *your* PUF? (In the Estonia file it is **citizenship** — `PB220A`, already grouped to EE / EU / Other, asked of persons 16+ only. Country of birth is *not* in the PUF, whatever the full codebook says.)

**Two rules this data forces on you** (the same traps as the practice file):
- **It is a survey with weights** — all population estimates must be weighted. Never report unweighted national figures.
- **Equivalised income is per household** — analyse it one row per household, not averaged over individuals.

---

## 3. Add the equality dimension

SILC does **not** collect ethnicity. You have two options — decide as a team:

**Option A — use the real variable (simpler).** Use `citizenship` (`PB220A`: EE / EU / Other) as the integration dimension. This is real, defensible, and needs no fabrication. Note it exists only for persons 16+.

**Option B — add synthetic ethnicity (richer, for the minority framing).** If you want an explicit minority dimension (as in the Moldova/Georgia work), fabricate one. Use the provided template `add_synthetic_ethnicity_silc.py` (in this folder — run it next to the extracted CSVs), or build it with Claude Code from this specification:

> **Synthetic ethnicity — specification**
> - Assign ethnicity at the **household level** — everyone in a household shares it (as in reality).
> - Make it **correlate with citizenship**, so the synthetic minority is plausible. (Region cannot be used — it is anonymised in the PUF.)
> - Use realistic **shares** for the country you picked (look up the actual ethnic composition).
> - **Label it clearly as synthetic** in the column name and in every output. It is fabricated for training and must never be presented as real.

Whichever you choose, **state in your findings that this dimension is real (Option A) or fabricated (Option B).** That honesty is part of the exercise.

---

## 4. Analyse — weighted and household-correct

Pick one question:
- Weighted **at-risk-of-poverty rate** (equiv. income < 60% of the weighted median), by citizenship / synthetic ethnicity.
- Weighted **median income gap** between citizen groups (or majority vs synthetic minority).
- Weighted **activity-status** differences (employment, unemployment) across the integration dimension.

Every figure weighted; income work at household level; sample sizes (unweighted n) shown beside weighted estimates; small groups caveated.

---

## 5. What you must produce

1. A one-sentence question, and a note on **where you got the data** (which country/year PUF, from where).
2. A **merged, analysis-ready table** built from the D/R/H/P files, with the join documented.
3. Your equality dimension (real or synthetic — stated), correctly keyed.
4. Weighted results, with unweighted n shown; at least one clear chart.
5. A reproducible, commented script and the **mini equality report** in Markdown (`equality_report.md`, structure in `Assignment_Final.md`), including its ~150-word dissemination text — honestly caveated.

Deliverable format, the final verification pass, the **5-minute presentation**
and how to **upload your results** are the same for both tracks — see
`Assignment_Final.md`.

---

## 6. Honest caveats to carry

- These PUFs are **synthetic and explicitly not for inference** — Eurostat says so. Your findings describe the *file*, not the real country. Say this plainly.
- If you fabricated ethnicity, **nothing about the ethnic dimension is real** — it is a teaching device.
- Describe differences; don't explain causes; caveat small groups; check framing for anything that could stigmatise.

---

## 7. What "good" looks like

A team that finds the data themselves, correctly merges the four files, applies weights and household-level logic properly, adds a clearly-labelled equality dimension, produces a weighted result with sample sizes and one clear chart, and is transparent about what is real vs synthetic — has done genuinely advanced, honest work. That is a high bar; clearing it even part-way is a real achievement.
