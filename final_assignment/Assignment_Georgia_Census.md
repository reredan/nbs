# Assignment — Foundation track (Georgia)
## Measuring the linguistic integration of ethnic minorities, from real census data
### NBS Data-Science Course — final workshop coding challenge

This track uses **real, official data** from the National Statistics Office of Georgia (Geostat): the 2024 Population Census, "Demographic and Social Characteristics."

**Important — what this data is.** These are **aggregated census tables** (counts by region × category), not individual microdata. So your job is not to clean raw records — it is to **parse the official Excel tables, reshape them into tidy data, and build integration indicators** from them. That is exactly the kind of work a statistics office does every day.

---

## 1. Get the data

Download from:
`https://www.geostat.ge/en/modules/categories/910/demographic-and-social-characteristics`

Download the **XLSX** files for at least these two tables (both are on that page;
links verified 2026-07-03):
- **Table 4: Population by regions, self-governed units, sex and nationality** — this is the ethnicity data.
- **Table 5: Population by regions, self-governed units, native language and Georgian language knowledge level** — this is the language / integration data.

Put both files in your project folder. Do not edit them by hand — let Claude Code
do the work, so it's reproducible. If the site is slow or blocked, the trainers
have the files on a USB stick.

**Your anchor number:** the census total population is **3,929,581** (as of
14 November 2024, excluding the occupied territories). Whatever you extract must
reconcile with that figure — it's your first and best sanity check.

---

## 2. The question

> **Across Georgia's regions, how linguistically integrated are ethnic minorities — that is, where are the main minorities (Azerbaijani, Armenian) concentrated, and to what extent do they speak the Georgian state language?**

This is a real integration indicator: proficiency in the state language among minority-language speakers is one of the clearest measures of linguistic integration, and it is central to the course's integration-measurement framework.

You may narrow it (e.g. focus on Kvemo Kartli and Samtskhe-Javakheti, where the Azerbaijani and Armenian communities are concentrated) — a narrow question fully answered beats a broad one half-done.

---

## 3. How to work — the seven stages (adapted for census tables)

1. **Frame.** Write your one-sentence question and decide which indicator answers it (e.g. "share of the population reporting a non-Georgian native language who know Georgian, by region").
2. **Set up the project.** Put the two XLSX files and a `CLAUDE.md` in your folder. Start Claude Code there.
3. **Explore / parse.** This is the hard part with census tables. Ask Claude Code to open each file, show you the sheets, and describe the layout — **expect merged cells, multi-row headers, a title row, and total rows mixed in with categories.** Have it identify the actual data grid before anything else.
4. **Reshape to tidy.** Get each table into a clean long format: one row per (region, category, count). Ask it to show you the tidy result and check the totals match the published totals.
5. **Join & compute.** Join the nationality and language tables on region (watch for region-name mismatches and the region / self-governed-unit hierarchy — decide which level you're working at). Compute your integration indicator, **with the underlying counts shown**.
6. **Visualise.** One clear chart — e.g. Georgian-language knowledge among minority-language speakers, by region, sorted. Show the table behind it.
7. **Interpret, document, save.** Write the findings note; save the commented script; note what you did so you could re-run it.

At every stage: **sanity-check.** Do regional counts sum to the national total? Do shares fall between 0 and 100%? If a number surprises you, ask Claude Code to show its working.

---

## 4. Specific challenges to expect (this is where the learning is)

- **Messy headers.** Census XLSX tables have titles, merged header cells, and sometimes two header rows. Getting the data out cleanly is most of the work.
- **Totals mixed with categories.** Rows like "Total" or "Georgia" sit alongside real categories — don't double-count them.
- **Region hierarchy.** "Regions" and "self-governed units" are nested. Pick one level and be consistent.
- **Matching across tables.** Region names must match exactly to join the nationality and language tables — capitalisation, spelling, or transliteration may differ.
- **Bilingual files.** Sheets or labels may be in Georgian and/or English.

---

## 5. What you must produce

1. A one-sentence question.
2. Two tidy tables (nationality-by-region, language-by-region) extracted from the raw Excel, with the cleaning/reshaping steps recorded.
3. At least one clear chart of your integration indicator.
4. A saved, commented Python script that reproduces everything from the raw XLSX files.
5. The **mini equality report** in Markdown (`equality_report.md`, structure in `Assignment_Final.md`), including its ~150-word dissemination text — descriptive, with the underlying counts, and honestly caveated.

Deliverable format, the final verification pass, the **5-minute presentation**
and how to **upload your results** are the same for both tracks — see
`Assignment_Final.md`.

---

## 6. Responsible use (specific to this data)

- **Census is a count, not a sample** — there is no sampling error, so don't talk about "significance." But **small cells still warrant care**: a region with very few of a group can produce a noisy-looking share.
- **Census undercount is real.** Some groups (e.g. hard-to-reach or marginalised communities) are under-counted in censuses everywhere. Note this as a caveat rather than treating counts as perfect.
- **Describe, don't explain.** "Minorities in region X report lower Georgian-language knowledge" is a finding. Why that is — schooling, isolation, history — is not something this table can tell you. Don't let the tool supply a causal story.
- **Framing.** Linguistic integration is an outcome people experience, not a judgement about a group. Check that your chart and sentence couldn't be read as blaming a minority.

---

## 7. What "good" looks like

A team that extracts two clean tables from messy official Excel, computes a defensible linguistic-integration indicator by region, shows one clear chart, states the finding plainly with the counts behind it, and can explain how they got the data out of the spreadsheet — has succeeded. Elegance of code is not the point; a trustworthy, reproducible indicator is.
