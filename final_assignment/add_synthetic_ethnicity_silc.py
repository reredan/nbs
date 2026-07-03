"""Add a SYNTHETIC ethnicity column to an EU-SILC PUF — teaching template.

The EU-SILC public use files contain no ethnicity variable. For the minority
framing of the workshop, this script fabricates one. Everything it produces is
FAKE and exists only so you can practise the analysis mechanics. The column is
named `ethnicity_SYNTHETIC` on purpose — keep that name in every output so no
reader can mistake it for real data.

Spec it implements (from the assignment brief):
- Ethnicity is assigned at the HOUSEHOLD level — all members share it.
- It correlates with the one real integration variable in the PUF, citizenship
  (PB220A: EE / EU / Other). NOTE: region (DB040) is anonymised to a constant
  in the PUF, so region cannot be used — verified on the real file.
- Shares are roughly calibrated to Estonia's real ethnic composition (about
  two-thirds Estonian, a quarter Russian) so national tables look plausible —
  but do not treat the exact shares as real.
- Deterministic: same input -> same output (fixed random seed).

Usage (from the folder containing the extracted PUF CSVs):
    uv run python add_synthetic_ethnicity_silc.py EE_2013

It reads  <PREFIX>d_EUSILC.csv and <PREFIX>p_EUSILC.csv
and writes <PREFIX>_household_ethnicity_SYNTHETIC.csv  (one row per household).

Merge it onto any file via the household ID (HB030 / RX030 / DB030).
"""

import sys

import numpy as np
import pandas as pd

SEED = 20260703  # fixed: rerunning must give identical output

# P(ethnicity | household citizenship mix). Households with any non-EE citizen
# are overwhelmingly assigned minority ethnicity; all-EE households mostly not
# (many ethnic-Russian residents hold Estonian citizenship, so the all-EE group
# still gets a substantial Russian share).
PROFILES = {
    "any_non_EE": {"Estonian": 0.05, "Russian": 0.83, "Other": 0.12},
    "all_EE":     {"Estonian": 0.815, "Russian": 0.15, "Other": 0.035},
}


def main(prefix):
    d = pd.read_csv(f"{prefix}d_EUSILC.csv")
    p = pd.read_csv(f"{prefix}p_EUSILC.csv")

    # Household citizenship mix from the persons interviewed (16+). PX030 is the
    # person's household ID in the P file.
    hh_col = "PX030" if "PX030" in p.columns else "PHID"
    non_ee = (p.assign(non_ee=p.PB220A.ne("EE") & p.PB220A.notna())
                .groupby(hh_col)["non_ee"].any())

    hh = d[["DB030"]].copy()
    hh["any_non_EE_citizen"] = hh.DB030.map(non_ee).fillna(False)

    rng = np.random.default_rng(SEED)
    def draw(is_mixed):
        prof = PROFILES["any_non_EE" if is_mixed else "all_EE"]
        return rng.choice(list(prof), p=list(prof.values()))
    hh["ethnicity_SYNTHETIC"] = [draw(m) for m in hh.any_non_EE_citizen]

    out = f"{prefix}_household_ethnicity_SYNTHETIC.csv"
    hh.to_csv(out, index=False)

    print(f"Wrote {out} ({len(hh):,} households).")
    print("\nHousehold-level shares (UNWEIGHTED — weight any real table you publish):")
    print(hh.ethnicity_SYNTHETIC.value_counts(normalize=True).round(3).to_string())
    print("\nREMINDER: this column is fabricated for training. Label it as synthetic")
    print("in every table, chart and sentence that uses it.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python add_synthetic_ethnicity_silc.py <PREFIX e.g. EE_2013>")
    main(sys.argv[1])
