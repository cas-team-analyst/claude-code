# Peer Review — Workers Compensation Sample Run

**Analysis folder:** C:\Users\super\Documents\actuarial\cas-rfp\spec-only\team-analyst\sample-data\sample-run
**Review date:** 2026-06-01
**Status:** Advisory — no selections were modified

**Files reviewed:**
- Analysis.xlsx
- Tech Review.xlsx
- REPORT.md
- REPLICATE.md

---

## Summary

This is a Workers Compensation Chain Ladder + BF reserving study (AY 2001–2024) producing a selected total unpaid of $6.1M on a $47.9M ultimate. The workflow ran cleanly and the method selection logic is generally sound. One technical FAIL requires correction before finalization (AY 2002 negative IBNR), and one high-priority judgment call — the tail curve method selection — carries a material reserve difference between the two AI approaches that needs an explicit rationale. Documentation in REPORT.md and REPLICATE.md is substantially incomplete and does not currently meet ASOP 41 standards for a final actuarial communication.

---

## High-Priority Findings

1. **[FAIL] AY 2002 negative IBNR (-$30,239)** — Selected ultimate ($2,297,495) falls below current incurred losses ($2,327,734). Fix required before any distribution. See §Cross-Method Consistency and §Proposed Alternatives.

2. **[High] Tail curve method divergence** — Rules-based selector chose Bondy/modified_bondy (implied tail 1.003–1.005) while the open-ended selector chose exp_dev_quick_exact_last (implied tail 1.066–1.072). The gap is 6–7 tail points. The driving issue — whether the gap_flag=True disqualification of exponential forms is appropriate given late-age development evidence — has not been resolved and is the single largest source of reserve uncertainty in this analysis. See §Technical Review Diagnostics and §Proposed Alternatives.

3. **[High] REPORT.md Section 5.2 misstates ELRs** — The text reads "~1.0% for AY 2020–2024" but the actual fallback ELRs embedded in 3-ie-ultimates.py produce IE values implying ~0.2–0.3% pure premium rates for those years (e.g., AY 2024 IE = $997,790 / $498.9M exposure = 0.20%). The ~1.0% figure belongs to AY 2001, not recent years. This is a documentation error that would mislead a reader assessing the BF a priori reasonableness.

4. **[High] REPORT.md and REPLICATE.md are substantially incomplete** — Multiple sections contain only template placeholders. A reviewer or future analyst cannot currently reproduce or independently evaluate the analysis from these documents. See §Documentation Quality.

---

## Detailed Findings

### Cross-Method Consistency

**Paid vs. incurred LDF ordering.** Paid LDFs appropriately exceed incurred LDFs at early and mid maturities (ages 11–83 months). However, there are inversions at three late-age intervals:

| Interval | Paid LDF (RB) | Incurred LDF (RB) | Direction |
|---|---|---|---|
| 95–107 | 1.013 | 1.015 | Paid < Incurred (minor) |
| 131–143 | 1.010 | 1.030 | Paid < Incurred (notable) |
| 167–179 | 1.0075 | 1.010 | Paid < Incurred (minor) |
| 179–191 | 1.0025 | 1.003 | Paid < Incurred (minor) |

The 131–143 inversion is the most notable: incurred is selected 2.0 points above paid at an age where case reserves should be winding down. This may reflect a period of incurred reserve strengthening pulling up the incurred average at this interval. It is worth examining whether excluding one or two volatile incurred development factors at 131–143 months would change the selection, though the reserve impact is modest at this maturity.

**Rules-based vs. open-ended LDF agreement.** Both selectors agree well at early ages (11–83 months). Divergences emerge in the 107–179 range for paid loss:

| Interval | Paid OE | Paid RB | Difference |
|---|---|---|---|
| 107–119 | 1.040 | 1.055 | −0.015 |
| 119–131 | 1.025 | 1.010 | +0.015 |
| 131–143 | 1.020 | 1.010 | +0.010 |

These differences partially offset, so the net CDF impact is small. No single divergence is large enough to flag independently.

**BF vs. CL consistency.** BF ultimates are consistently within 5% of CL ultimates for AY 2008–2018, confirming the a priori is reasonably calibrated for mid-maturity years. For AY 2019–2022 the two methods show somewhat wider spreads (as expected at lower maturities), and the blending logic appropriately shifts weight toward BF.

---

### Paid vs. Incurred Reasonability

**AY 2002 — floor violation (FAIL).** The selected ultimate ($2,297,495) is below current incurred losses ($2,327,734). The blend of 70% Incurred CL ($2,334,717) + 30% Paid CL ($2,210,644) mathematically produces a result below actuals. At 275 months, blending in paid CL at 30% weight serves no useful purpose — paid development below incurred at near-full maturity simply reflects remaining open case reserves, not a signal that the ultimate should be lower. The selection should be floored at the actual incurred.

**AY 2007 large-loss year.** Incurred actual ($4,810,775) is 3–4× the typical year. The IE/BF a priori ($2,850,338) badly underestimates this year, and the CDF at 215 months is only 1.018, so the CL selection of $4,917,122 is well-grounded and the judgment to use full CL weight here is defensible. The open-ended selector's $4,898,021 (pure Incurred CL) and the rules-based $4,917,122 (CL midpoint) are close ($19K gap). No material concern.

**AY 2023–2024 paid-to-incurred ratios.** For AY 2024 (age 11 months), paid-to-incurred is 0.40 and paid CDF is 6.72. The extreme CL leverage is correctly handled by excluding CL from the selection and using BF exclusively. For AY 2023 (age 23 months), paid CDF is 2.63 and the selection likewise excludes paid CL in favor of BF. These are reasonable judgments per the selection reasoning.

---

### Recent Year Stability

Selected loss rates (ultimate / payroll exposure) show a declining trend in recent years:

| AY | Selected Ultimate | Exposure | Implied Loss Rate |
|---|---|---|---|
| 2015 | $3,688,580 | ~$417M | 0.88% |
| 2016 | $2,842,344 | ~$426M | 0.67% |
| 2017 | $1,421,504 | ~$434M | 0.33% |
| 2018 | $2,785,760 | ~$443M | 0.63% |
| 2019 | $3,113,619 | $451.9M | 0.69% |
| 2020 | $1,439,104 | $460.9M | 0.31% |
| 2021 | $1,469,786 | $470.1M | 0.31% |
| 2022 | $1,301,030 | $479.5M | 0.27% |
| 2023 | $1,806,125 | $489.1M | 0.37% |
| 2024 | $1,355,317 | $498.9M | 0.27% |

AY 2020–2024 selected rates average approximately 0.31%, materially below the 0.40–0.89% seen in AY 2015–2019 (excluding the 2007 outlier). Two explanations are plausible and worth discussing in the REPORT: (a) genuine improvement in WC loss experience due to safety programs, mix shift, or favorable claim closure trends; or (b) the BF a priori (computed as a 3-year rolling average of recent empirical rates) is itself tracking the low emergence and thereby anchoring ultimates too low. If explanation (b) is correct, IBNR for AY 2021–2024 may be under-stated. The reviewer may want to consider whether an independent ELR benchmark (pricing indication, industry data) would produce materially different a priori values for these years.

AY 2019 at 0.69% stands out above recent peers. At age 71 months (CDF ~1.35), the CL indication is elevated and the BF blend pulls the selection toward $3.1M. This year warrants a watch in the next review cycle to confirm whether actual emergence supports the current selection.

---

### ASOP Compliance

**ASOP 23 (Data Quality).** The analysis accepts triangle data from Triangle Examples 1.xlsx with no reconciliation to an external source. The REPORT documents this appropriately ("Not reconciled — data accepted as provided"). No material anomalies were flagged in initial data review. The limitation is disclosed. Acceptable for a sample run; a production analysis should include a tie-out to financial records.

**ASOP 25 (Credibility).** The BF a priori is a 3-year rolling average of empirical incurred loss rates — a mechanical fallback rather than a pricing-derived ELR. The REPORT discloses this in Section 3.4. However, no discussion of the a priori's credibility or the sensitivity of recent-year ultimates to this assumption appears in Sections 5 or 8. Given that BF carries 50–80% weight for AY 2021–2024, the a priori source and reliability should be addressed. Additionally, as noted under the AY 2002 finding, blending paid CL at 30% weight at age 275 months is not credible weighting practice — it actively produces a floor violation.

**ASOP 36 (SAO).** This is a working draft; no SAO has been issued. The REPORT carries appropriate draft caveats. Not applicable in the current form.

**ASOP 41 (Communications).** Sections 4.1, 4.2, 5.1, 7, 8.2, 9, 10, 11, and 14 contain template placeholders or unchecked boxes. In current state, the REPORT does not meet ASOP 41's requirement that a qualified actuary could understand and evaluate the methods, assumptions, and rationale from the communication. See §Documentation Quality.

**ASOP 43 (Unpaid Claim Estimates).** Method selection logic is well-documented in the individual ultimate selection reasoning (Analysis.xlsx Loss Selection column). However, Section 8.2 (Sources of Uncertainty) is a template placeholder, and no aggregate reasonableness check is documented. ASOP 43 requires that the estimate be reviewed for reasonableness in aggregate — not only method-by-method. The loss rate progression table above provides a starting point; it should be added to the REPORT.

---

### Diagnostic Consistency

All seven items in Section 7 of REPORT.md remain unchecked despite 7-tech-review.py having been run and producing results. The diagnostics checklist and the anomalies section need to be populated from the tech review output before the REPORT is distributed.

The LDF selections in the workbook are consistent with the selection reasoning in the JSON files — the AI selectors' rationale accurately describes the averages applied at each interval. No inconsistency between documented reasoning and actual selected values was observed.

The Pre-Method Diagnostics and Post-Method Diagnostics sheets are present in Analysis.xlsx and provide the diagnostic exhibits. These are not populated into the REPORT narrative.

---

### Documentation Quality

**REPORT.md.** Multiple sections require population before this can serve as an actuarial communication:

- Section 4.1 Methods Applied: All method rows show "[ ]" — not filled in from the analysis
- Section 4.2 Method Weighting: Contains only the template placeholder "[Describe how methods were weighted...]"
- Section 5.1 Development Patterns: Selection basis and tail source fields are template stubs
- Section 5.2 Expected Loss Ratios: Contains incorrect ELR figures (states ~1.0% for AY 2020–2024; actual implied rates are ~0.2–0.3%)
- Section 7 Diagnostics: All seven checklist items unchecked; "Anomalies to investigate" unpopulated
- Section 8.2 Sources of Uncertainty: Template text only; no analysis-specific risk discussion
- Section 9 Reliance on Others: Template placeholders not replaced
- Section 10 Information Date: Blank
- Section 11 Open Questions: Items 1–3 are template text (though the two appended findings at the bottom are well-written and useful)
- Section 14 Version History: Dates not filled in

The two substantive entries in Section 11 (AY 2002 negative IBNR and tail curve divergence) are well-framed. The Section 0 Reviewer Quick-Start is the best-populated section of the report and provides useful orientation.

**REPLICATE.md.** Steps 2–9 read only "To be filled in as analysis progresses." A reviewer has no way to replicate the analysis from this document alone. It should document: all scripts run in order, the LDF and tail selection JSON files created, any manual selections or overrides (there were none per the PROGRESS log), and the full script execution sequence from 1a through 7.

---

### Technical Review Diagnostics

The tech review produced one FAIL and several WARNs:

**FAIL — Loss Selection IBNR < 0 for AY 2002.** Discussed above. Requires a fix.

**WARN — Loss Selection extreme outlier (1 period > 10× median).** AY 2007's selected ultimate ($4,917,122) is an outlier relative to most years. This is expected given the documented large-loss event. No action needed, but the REPORT should explicitly confirm this is a known large-loss year rather than a data anomaly.

**WARN — Count Selection slight negatives** (AY 2005, 2006, 2007, 2012, 2014, 2017, 2022). These are rounding artifacts from integer-rounding the selected count ultimates for years with CDF = 1.000. The negatives range from -0.23 to -0.49 counts — immaterial. No action required, but the REPORT should note "minor rounding effects in fully developed count years."

**WARN — Multiple structure checks not run against values-only file.** The tech review WARNs that diagnostics, Sel- sheets, CL triangle sheets, paid-to-incurred, case reserve, closure rate, and severity/frequency trend checks were skipped because those sheets are not in the values-only file (Analysis.xlsx). These checks would run against the full Complete Analysis.xlsx. The reviewer should confirm that 7-tech-review.py was also run against Complete Analysis.xlsx and those checks passed, or note that they were not performed.

---

## Proposed Alternatives

### 1. AY 2002 — Floor Ultimate at Actual Incurred

**Analyst selection:** $2,297,495 (70% Incurred CL + 30% Paid CL)
**Proposed alternative:** $2,327,734 (actual incurred, as floor) or $2,334,717 (100% Incurred CL)

At 275 months maturity (99.7% developed), blending in paid CL serves no purpose other than to pull the selection below the current incurred balance. The incurred actual of $2,327,734 is the minimum defensible selection; the Incurred CL of $2,334,717 applies only a trivial remaining tail (1.003) and is the cleaner choice. Either eliminates the negative IBNR and produces a more defensible result. The open-ended selector independently chose $2,334,717 (Incurred CL), arriving at the same conclusion.

### 2. Tail Curve — Explicit Resolution of Rules-Based vs. Open-Ended Divergence

**Rules-based selection:** Bondy for Incurred Loss (tail ≈ 1.003), modified_bondy_double_dev for Paid Loss (tail ≈ 1.005)
**Open-ended selection:** exp_dev_quick_exact_last for both (Incurred ≈ 1.072, Paid ≈ 1.066)
**Reserve impact:** Approximately +6–7% to projected ultimates for the immature years if the open-ended tail is used; at a total reserve of $6.1M this could represent $300–$500K+ of additional IBNR.

The rules-based selector rejected all exponential forms due to gap_flag=True — the exponential curve at the starting age jumps discontinuously from the last empirical LDF. This is a legitimate concern: a sudden step-up at the cutoff age creates internally inconsistent CDFs. The open-ended selector acknowledged the gap but preferred the exponential form for its goodness-of-fit (R² = 0.865 for paid, LOO range 1.088–1.090) and the evidence of continued small-but-measurable late-age development in the empirical triangles.

The reviewer may want to consider whether the exp_dev_quick_exact_last tail factor, constrained to match the last empirical LDF at the cutoff (reducing the gap), provides a better balance than either a flat Bondy or an unconstrained exponential. The key question: do the empirical paid development factors at ages 203–275 months (1.008, 1.010, 1.002, 1.005, 1.007, 1.007) represent genuine residual development or random noise? If genuine, a tail of 1.005 (Bondy) likely under-reserves; if noise, 1.066 (exponential) likely over-reserves.

Reviewer suggestion: examine whether using the exact_last variant specifically anchors the curve to last observed LDF ~1.0025 for paid, and evaluate whether a tail of ~1.020–1.030 (between the two extremes) would be supportable by a weighted-average of the empirical late factors.

### 3. Recent Year BF A Priori — Consider Whether Fallback ELR Is Under-Stated

**Current approach:** 3-year rolling average of empirical incurred loss rates (producing ~0.20–0.25% pure premium for AY 2022–2024)
**Proposed consideration:** Compare against industry WC pure premiums or company pricing indications for equivalent clerical classification to assess whether the recent experience is genuinely favorable or artificially low due to IBNR lag

This is not a required change but a sensitivity worth documenting. If industry benchmarks suggest WC pure premiums for clerical at 0.30–0.40%, the current BF a priori may be anchoring AY 2022–2024 ultimates 15–30% below a more forward-looking indication. The IBNR impact would be $100–250K.
