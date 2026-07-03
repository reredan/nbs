# Foundation track — Georgia
## How linguistically integrated are ethnic minorities? (real 2024 census data)

Real, official data from Geostat: aggregated census tables (counts by region ×
category), not microdata. Your job is to **parse messy official Excel into tidy
data and build an integration indicator** — exactly what a statistics office
does every day.

## 1. Get the data

From `https://www.geostat.ge/en/modules/categories/910/demographic-and-social-characteristics`
download the **XLSX** for (links verified 2026-07-03; trainers have USB copies):

- **Table 4** — Population by regions, self-governed units, sex and **nationality**.
- **Table 5** — Population by regions, self-governed units, **native language and
  Georgian language knowledge level**.

Don't edit them by hand — let Claude Code do everything, so it's reproducible.

**Your anchor number: total population 3,929,581** (14 Nov 2024, excluding the
occupied territories). Whatever you extract must reconcile to it — that's your
first and best sanity check.

## 2. The question

> Where are the main minorities (Azerbaijani, Armenian) concentrated, and to
> what extent do they speak the Georgian state language?

Narrowing it (e.g. one or two regions) is fine — a narrow question fully
answered beats a broad one half-done.

## 3. How to work

1. **Parse** — ask Claude to describe each sheet's layout first: expect title
   rows, **merged multi-row headers**, and national/regional/municipal rows
   mixed in one column with no level markers.
2. **Reshape to tidy** — one row per (unit, category, count). **Check the
   totals**: do your regions sum to 3,929,581? Are "Total"/"Georgia" rows
   double-counted? Which rows are regions and which are sub-units?
3. **Compute** — your integration indicator (e.g. share of people reporting a
   minority native language who know Georgian, by region), with counts shown.
   Careful with the denominator: who exactly was asked about Georgian knowledge?
4. **Chart, report, verify** — one clear chart, then the equality report and
   sceptic pass per `Assignment_Final.md`.

## 4. Responsible use

- A census is a **count, not a sample** — no significance tests; but small cells
  still deserve caution, and census **undercount** of marginalised groups is real.
- **Ethnicity and native language are different variables** — say which one your
  indicator uses.
- Describe, don't explain: *why* knowledge is lower somewhere is not in this table.
