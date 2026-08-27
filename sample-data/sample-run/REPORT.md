# Reserving Analysis — Working Draft

_This is a draft report that should be filled in as you make your way through the PROGRESS.md steps._

**Analysis:** Sample Run - Triangle Examples
**Valuation Date:** Not explicitly stated in source data - latest diagonal corresponds to 287 months of development for AY 2001 (see Section 10)
**Draft Version:** v0.2 — For Peer Review
**Prepared by:** Bryce
**Submitted to:** N/A - internal/demonstration run, no reviewer assigned
**Draft Date:** 08/27/2026

> **Draft status:** This is a working document prepared for internal peer review. It has many blank sections because the project only runs a basic reserving workflow, not a full analysis. It is not a final actuarial communication and should not be distributed outside the review team. Numbers, selections, and commentary are subject to change based on reviewer feedback.

---

## Table of Contents

- [0. Reviewer Quick-Start](#0-reviewer-quick-start)
- [1. Purpose and Scope](#1-purpose-and-scope)
- [2. Summary of Indications](#2-summary-of-indications)
- [3. Data](#3-data)
- [4. Methodology](#4-methodology)
- [5. Key Assumptions](#5-key-assumptions)
- [6. Results by Segment](#6-results-by-segment)
- [7. Diagnostics and Reasonableness Checks](#7-diagnostics-and-reasonableness-checks)
- [8. Sensitivity and Uncertainty](#8-sensitivity-and-uncertainty)
- [9. Reliance on Others](#9-reliance-on-others)
- [10. Information Date and Subsequent Events](#10-information-date-and-subsequent-events)
- [11. Open Questions for Reviewer](#11-open-questions-for-reviewer)
- [12. ASOP Self-Check (for reviewer)](#12-asop-self-check-for-reviewer)
- [13. Peer Review Log](#13-peer-review-log)
- [14. Version History](#14-version-history)
- [Appendices](#appendices-in-accompanying-workbook)

---

## 0. Reviewer Quick-Start

*A short orientation so the reviewer can get into the work quickly.*

- **What this analysis covers:** Workers' Compensation reserve analysis for AY 2001-2024 (sample/demonstration dataset) using Chain Ladder, Initial Expected, and Bornhuetter-Ferguson methods, selecting one ultimate per accident year for Loss and Count.
- **What changed since last review:** Not applicable - this is the first (v0.1) draft of this analysis.
- **Where I want the most scrutiny:** (1) The LDF empirical cutoff age divergence between Framework AI and Open-Ended AI selectors, especially for Reported Count (Section 11, item 1); (2) AY 2023-2024 loss ultimates, where CL and BF diverge materially at very low maturity and the ELR used is an empirical fallback rather than a pricing-based a priori (Section 11, item 2).
- **Open questions for reviewer:** See Section 11

---

## 1. Purpose and Scope

### 1.1 Purpose of the Analysis
Sample/demonstration run of the TeamAnalyst reserving workflow, using the sample triangle data provided ("Triangle Examples 1.xlsx"), run in Fully Automatic mode.

### 1.2 Scope
| Item | Detail |
|---|---|
| Segment(s) / LOB | Workers' Compensation (clerical, relatively low hazard; payroll range $100M-$500M) |
| Accident / Underwriting years | 2001-2024 (accident years) |
| Coverages | Paid Loss, Incurred Loss, Reported Claim Counts, Exposure (payroll); DCC/A&O/ULAE not separately identified - assumed combined with loss per Section 4.3 |
| Basis | Not specified in source data (assumed as provided - likely gross) |
| Currency | Not specified in source data (assumed USD) |
| Geography | Not specified in source data |

### 1.3 Intended Internal Users
Internal review / demonstration of the reserving workflow. This draft is not intended for external distribution in its current form.

---

## 2. Summary of Indications

| Segment | Paid to Date | Case | IBNR | Total Unpaid | Ultimate |
|---|---|---|---|---|---|
| Loss (WC) | $41,767,854 | $1,848,541 | $4,688,269 | $6,536,810 | $48,304,664 |
| Count (Reported) | 9,716 | — | 35 | 35 | ~9,751 |

**Comparison to prior estimate:**

| Segment | Prior Ultimate | Current Ultimate | Change | % |
|---|---|---|---|---|
| Not applicable | | | | |

Not applicable - no prior estimate is available for comparison (this is the first analysis of this sample dataset).

**Key drivers of change:** Not applicable - no prior estimate to compare against.

---

## 3. Data

### 3.1 Data Used
| Data Element | Source | As-of Date | Notes |
|---|---|---|---|
| Paid loss triangle | Triangle_Examples_1.xlsx, sheet "Paid 1" | Latest diagonal (age 287 mo.) | AY 2001-2024, ages 11-287 months (annual valuations); confirmed by user 2026-08-27 |
| Incurred loss triangle | Triangle_Examples_1.xlsx, sheet "Inc 1" | Latest diagonal (age 287 mo.) | AY 2001-2024, same shape as Paid; confirmed by user 2026-08-27 |
| Reported claim counts | Triangle_Examples_1.xlsx, sheet "Ct 1" | Latest diagonal (age 287 mo.) | AY 2001-2024; single count triangle, classified as Reported Count (no "Closed" qualifier present); values are non-integer - confirmed by user 2026-08-27 |
| Earned premium / exposures | Triangle_Examples_1.xlsx, sheet "Exposure" | 2001-2024 | Annual payroll by accident year (Workers' Compensation); confirmed by user 2026-08-27 |
| Case reserves | Not provided | | Derivable as Incurred - Paid if needed |
| Rate change history | Not provided | | |
| Line of Business context | Triangle_Examples_1.xlsx, sheet "Tri 1" | | Line: WC; Risk type: clerical, relatively low hazard; Payroll range: $100M-$500M |

### 3.2 Data Reconciliation
Not reconciled - data accepted as provided by the user (sample/example triangle file).

### 3.3 Data Quality Observations
*Per ASOP No. 23 — flag anything unusual.*

- Standard 24x24 loss development triangle shape (AY 2001-2024, ages 11-287 months in ~12-month increments); upper-right sparsity is the expected pattern for a triangle, not a data issue.
- No Expected Loss Rate (ELR) file or exposure-based pricing loss ratios were provided; a separate Exposure (payroll) sheet is available, which supports a fallback empirical approach for BF if needed.
- No prior LDF or tail factor selections were provided.
- No closed claim count triangle - only a single claim count triangle is available, so closure-rate-based diagnostics will be limited.
- No material outliers, negative development, or coding anomalies were observed during initial preview.
- `1a-load-and-validate.py` was customized: the workbook uses a wide triangle layout with an extra title row above the header on the Paid/Incurred sheets; a custom parser (`_read_wide_triangle`) locates the "Accident Year" header row dynamically. The claim count sheet ("Ct 1") lacks the title row present on Paid/Incurred; handled as a distinct case. Reported claim counts are non-integer (e.g., 637.3668) - loaded as-is, flagged for reviewer awareness. Data validation was reviewed and confirmed by the user on 2026-08-27.

### 3.4 Data Limitations
- No ELR file provided - using 3-year rolling average of empirical loss rates as fallback for Initial Expected/BF methods.
- No prior LDF or tail factor selections were available for reference/comparison.
- No closed claim count triangle - unable to estimate closure rates or use Closed Count as a maturity measure; only Reported Count is available.
- No case reserve data provided directly (derivable as Incurred - Paid).

---

## 4. Methodology

### 4.1 Methods Applied
| Method | Segments Applied | Why Selected |
|---|---|---|
| Paid LDF (Chain Ladder) | Paid Loss | Selected via framework with AI cross-check - mature year primary method. |
| Incurred LDF (Chain Ladder) | Incurred Loss | Selected via framework with AI cross-check - mature year primary method. |
| Reported Count LDF (Chain Ladder) | Reported Count | Selected via framework with AI cross-check - mature year primary method. |
| Paid B-F | Paid Loss | Ran successfully using ELR fallback (empirical 3-yr rolling average of Incurred Loss / payroll). |
| Incurred B-F | Incurred Loss | Ran successfully using ELR fallback. |
| Reported Count B-F | Reported Count | Ran successfully using expected-frequency fallback (3-yr rolling average of Reported Count / payroll). |
| Initial Expected | Paid Loss, Incurred Loss, Reported Count, Closed Count | Ran successfully using ELR/frequency fallback; Closed Count IE uses Reported Count expected frequency as proxy (no Closed Count triangle available). |
| Frequency-Severity | Not used | Not part of this workflow's method set. |

### 4.2 Method Weighting / Selection Logic
LDF selections were made using a structured 14-criteria decision framework (see `/selection-logic` for full detail), applied independently per measure and development interval, with an open-ended AI selector providing an independent cross-check for each measure. The Framework AI Selection is what feeds the Chain Ladder ultimates calculation; the Open-Ended AI Selection is shown alongside for comparison and is used only as a fallback if the Framework row is blank.

All three methods (Chain Ladder, Initial Expected, BF) ran successfully for all measures at the AY level. Maturity-based weighting into a single selected ultimate per accident year is determined in Step 7 (Ultimate Selections).

### 4.3 LAE Treatment
**Not applicable.** This analysis assumes loss triangles include LAE (loss and allocated loss adjustment expense combined), or LAE is not being estimated separately. If LAE needs to be estimated separately, that is outside the scope of this workflow.

- **DCC / ALAE:** Not separately estimated
- **A&O / ULAE:** Not separately estimated

---

## 5. Key Assumptions

### 5.1 Development Patterns
- **Selection basis:** Volume-weighted averages with averaging windows from 3-year to all-year. Framework selected optimal window per age based on stability, volume, and fit diagnostics.
- **Empirical selection cutoff (Framework AI, per-measure LDF row):** Paid Loss and Incurred Loss selected through 191-203 months. Reported Count selected through 59-71 months. Note: the tail-fitting step (below) fills any gap between the Framework AI cutoff and the last available Open-Ended AI selection, so the effective empirical cutoff used for curve fitting was 275 months (Paid Loss, Incurred Loss) and 263 months (Reported Count).
- **Tail:** Curve method selected from curve fitting diagnostics using the Framework AI Selection (with Open-Ended AI cross-check). Framework AI selections: Paid Loss - Modified Bondy (double deviation), tail factor 1.0140; Incurred Loss - Bondy, tail factor 1.0000; Reported Count - Bondy, tail factor 1.0000. All three measures rejected the exponential-decay curve family under the framework's gap-discontinuity rule (large jump between the fitted curve and the last observed factor, gap far above threshold) despite moderate R² (0.46-0.84.) Skurnick was rejected on poor fit (R² 0.07-0.46) and materiality grounds. Leave-one-out testing corroborated the Bondy family as the most stable choice given the near-fully-developed empirical patterns. Open-Ended AI cross-check: Paid Loss - Bondy (tail ~1.007, close to Framework); Incurred Loss - McClenahan (tail ~1.0000, agrees with Framework); Reported Count - Bondy (tail 1.0000, agrees with Framework). See `selections/Chain Ladder Selections - Tail.xlsx` for full diagnostics.

### 5.2 Expected Loss Ratios (for B-F and ELR methods)
No ELR file was provided. Per user decision, a fallback approximation is used: for each accident year, the diagonal actual Incurred Loss per dollar of exposure (payroll) is computed and smoothed with a 3-year rolling average, used as the expected loss rate for Initial Expected/BF methods (`3-ie-ultimates.py` default). An analogous 3-year rolling average of Reported Count / payroll was used as the expected frequency.

| AY | ELR | Basis |
|---|---|---|
| 2001 | 0.0100 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2002 | 0.0090 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2003 | 0.0080 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2004 | 0.0050 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2005 | 0.0050 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2006 | 0.0050 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2007 | 0.0080 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2008 | 0.0070 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2009 | 0.0070 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2010 | 0.0030 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2011 | 0.0040 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2012 | 0.0040 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2013 | 0.0030 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2014 | 0.0030 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2015 | 0.0040 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2016 | 0.0060 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2017 | 0.0060 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2018 | 0.0050 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2019 | 0.0050 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2020 | 0.0040 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2021 | 0.0030 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2022 | 0.0020 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2023 | 0.0020 | 3-yr rolling avg. of Incurred Loss / payroll |
| 2024 | 0.0020 | 3-yr rolling avg. of Incurred Loss / payroll |

### 5.3 Trend Assumptions
**Not implemented in this analysis.** The current workflow does not include trend selection or application. Loss development methods (Chain Ladder, BF, IE) rely on historical development patterns without explicit trending adjustments.

| Segment | Frequency | Severity | Pure Premium |
|---|---|---|---|
| N/A | N/A | N/A | N/A |

### 5.4 Other Assumptions
- **Rate change:** Not explicitly modeled in this analysis
- **Case reserve adequacy:** Assumed stable (no adjustments applied)
- **Settlement rate / claim closing patterns:** Patterns emerge from historical triangle development; no explicit assumptions
- **Mix / law / tort environment:** Not explicitly modeled

### 5.5 Assumption Rationale
**Material assumptions in this analysis:**
- **LDF selections:** Based on volume-weighted averages with framework (14 criteria) and AI cross-check. See Section 4.2 and LDF selection workbooks for detailed reasoning.
- **Tail factors:** Based on curve fitting (Bondy, Exponential Decay, etc.) with leave-one-out validation. See tail selection workbook for detailed reasoning.
- **Expected loss ratios:** No pricing ELR file was available. User elected to use the empirical fallback: 3-year rolling average of diagonal actual loss per dollar of exposure (payroll), by accident year, as the a priori expectation for Initial Expected/BF methods. This is a less forward-looking approximation than a pricing ELR.

*Any assumption primarily judgment-driven should be flagged in Section 11.*

---

## 6. Results by Segment

*Detailed exhibits live in the accompanying workbook; summarize selections and rationale here.*

### 6.1 Loss (Workers' Compensation)
- Selected ultimates: See `selections/Ultimates.xlsx`, "Losses" sheet (choosing between Incurred and Paid CL/BF/IE indications per accident year). Selected ultimate total: $48,304,664.
- Method weighting: Chain Ladder used as primary for mature/tail years (2001-~2015); a Chain Ladder/BF blend for mid-maturity years with meaningful remaining development; a shift toward BF and the a priori/IE indication for the greenest years (2023-2024), where Chain Ladder was deemed unstable/not credible given very low maturity. Incurred selected over Paid throughout by the AI selectors (more responsive; the two converge at full maturity).
- Notable judgment calls: AY 2023 and 2024 show large CL-vs-BF divergence (54% and 89% respectively) reflecting very low maturity - the selectors moved away from raw CL toward BF/IE for these years. See Section 11.

### 6.2 Count (Reported)
- Selected ultimates: See `selections/Ultimates.xlsx`, "Counts" sheet. Selected ultimate total: ~9,751 claims.
- Method weighting: Only Reported Count is available (no Closed Count triangle in the source data). Nearly all accident years (2001-2023) are fully or near-fully developed (CDF close to 1.00), so Chain Ladder was used directly; only AY 2024 (11 months maturity) needed a Benktander/BF blend.
- Notable judgment calls: None material - count development completes very early for this book (empirical cutoff ~71-83 months per the Framework AI LDF selector), so count ultimates are low-uncertainty relative to loss ultimates.

---

## 7. Diagnostics and Reasonableness Checks

Automated technical review (`scripts/7-tech-review.py`) ran 94 checks against `Analysis.xlsx`: 64 PASS, 30 WARN, 0 FAIL. Full detail saved to `Tech Review.xlsx`.

- [x] Loss ratios by AY — Reviewed - progression is reasonable (Loss Rate range 0.002-0.014, no outliers per tech review Group 9).
- [x] Frequency / severity trends — YoY severity spikes flagged in 14 periods (e.g., "period 3: 45%, period 4: 101%, period 6: 232%" - see tech review Group 15); a frequency spike >2x median was also flagged in 5 periods. Not fully consistent with a smooth historical pattern - see Anomalies below.
- [x] Implied paid and reported development — Patterns generally consistent with selections; tech review flagged some non-decreasing/reversal warnings in the CL triangles and average LDFs (Groups 10-11), all within tolerance (0 FAIL).
- [x] Actual vs. expected emergence since prior review — Not applicable - no prior estimate exists for this analysis.
- [x] Comparison to independent benchmark — Not performed.
- [x] Hindsight test on prior ultimates — Not performed (no prior ultimates available).
- [x] Ratio of IBNR to case reserves — Reviewed - IBNR and case reserves both non-negative and internally consistent (Groups 4-5, 12-13 all PASS on core identities); some Average IBNR/Unpaid triangle cells showed WARN-level negatives, noted below.

**Anomalies to investigate:**
- Tech review WARN: YoY severity spikes of 45%, 101%, 232% (and more) in several periods (Group 15) - worth confirming whether these reflect genuine large claims or data/parsing artifacts.
- Tech review WARN: 104 cells with negative "Average IBNR" and 98 cells with negative "Average Unpaid" in the diagnostic triangles (Group 8), with 115 reversals (non-increasing as maturity increases) in each - a common artifact of averaging across accident years with different development speeds, but worth spot-checking.
- Tech review WARN: 98 "Reported-to-Ult" cells and 8 "Incurred-to-Ult" cells exceed 1.0 (Group 7) - can occur when a CDF component (e.g., a sub-1.0 tail factor on counts) pushes the ratio slightly above 1; not flagged as FAIL but worth reviewer awareness.
- Tech review WARN: Link ratios exceeding the diagnostic ceiling (1.05) at the youngest ages (11->23 months) for all three measures (Group 11) - expected given the steep early-development pattern in this WC book, but the ceiling itself may need recalibrating for this dataset.
- Tech review WARN: Count Selection IBNR% shows 11 maturity-order reversals (exceeds the N/5=4 tolerance) - see Section 11.

---

## 8. Sensitivity and Uncertainty

### 8.1 Sensitivity to Key Assumptions
**Not implemented in this analysis.** Sensitivity testing would require re-running projections with varied assumptions. This can be added in future iterations.

| Assumption | Change | Impact on Total Ultimate |
|---|---|---|
| Tail factor | ± (not tested) | (not tested) |
| ELR | ± (not tested) | (not tested) |
| LDF selections | ± (not tested) | (not tested) |

### 8.2 Sources of Uncertainty
*Per ASOP No. 43 — discuss the risks that could cause actuals to differ from estimate.*

- **Process risk:** Limited development history for recent years (AY 2023-2024 have only 11-23 months of maturity) increases parameter uncertainty in those years' ultimates, which rely heavily on the BF/IE blend rather than pure Chain Ladder.
- **Parameter risk:** Tail factor uncertainty is modest for this book - Framework AI tail factors are small (1.0000-1.0140) and the alternative curve families (exponential decay) were explicitly rejected for poor fit/large discontinuities, so the practical range of plausible tail factors is narrow. LDF selection uncertainty is higher: the Framework AI and Open-Ended AI selectors diverged materially on the empirical cutoff age (Section 11, item 1), which affects how much of the tail is empirical vs. curve-fitted.
- **Model risk:** Method selection for the greenest years (2023-2024) drives material reserve differences - CL and BF diverge by 54-89% for Incurred Loss in those years (Section 11, item 2). The ELR used for BF/IE is an empirical fallback, not a pricing-based a priori, adding another layer of model risk specific to this analysis.
- **Systemic risk:** Tech review flagged large YoY severity spikes in several periods (up to 232%) that could indicate large claims, a mix shift, or a data artifact - not separately investigated or excluded in this workflow (see Section 7, Anomalies to investigate). If these represent large claims, they were not separately estimated and could affect ultimate volatility if similar claims recur.
- **Segment-specific risk factors:** This is a single WC segment (clerical, low-hazard risk); no cross-segment risk diversification considerations apply.

---

## 9. Reliance on Others

No external sources relied upon beyond the sample triangle dataset provided by the user (`Triangle_Examples_1.xlsx`), which was accepted as provided (see Section 3.2, Data Reconciliation).

| Source | Information Relied Upon |
|---|---|
| User-provided sample dataset | Paid/Incurred loss triangles, reported claim counts, and payroll exposure (Triangle_Examples_1.xlsx) |

---

## 10. Information Date and Subsequent Events

- **Information Date:** Latest available diagonal in the source triangles is age 287 months for AY 2001 (i.e., a valuation date consistent with the most mature accident year's latest evaluation); exact calendar valuation date not stated in the source file.
- **Subsequent events considered:** None known as of the draft date (08/27/2026).

---

## 11. Open Questions for Reviewer

*The key section — where you flag judgment calls you want a second opinion on.*

1. **Material divergence between Framework AI and Open-Ended AI on the LDF empirical cutoff age (Step 4).** For Paid Loss and Incurred Loss, the Framework AI selector stopped empirical selections at 191-203 months (cutoff 203-215), while the Open-Ended AI selector continued to 263-275 months (cutoff 275-287) - an ~80-month difference. For Reported Count, the divergence is much larger: Framework AI cut off at 71-83 months (essentially fully developed, near-1.000 factors), while Open-Ended AI continued selecting through 251-263 months (cutoff 263-275). Since the Framework AI Selection row drives the tail curve fitting in Step 5 and ultimate LDFs in Step 6, this cutoff choice materially affects how much of the tail is empirical vs. curve-fitted. Reviewer should confirm the shorter Framework cutoff (particularly for Reported Count, where it implies claims are essentially fully reported by ~83 months) is reasonable for this WC book, or whether the Open-Ended AI's longer empirical window should be preferred.
2. **Material CL-vs-BF divergence for the most recent accident years (Step 7, Incurred Loss).** AY 2024 shows an 89% difference between the Chain Ladder ultimate ($3.01M) and BF ultimate ($1.59M); AY 2023 shows a 54% difference ($3.28M CL vs $2.14M BF). Both years are very immature (11 and 23 months respectively), so CL is highly leveraged off a thin diagonal. The AI selectors moved toward BF/IE for these years rather than raw CL - reviewer should confirm this is the right call, particularly given the ELR used for BF/IE is itself only an empirical fallback (Section 5.2), not a pricing-based a priori.
3. **Fractional (non-integer) claim counts in the Reported Count triangle** (e.g., 637.3668 - see Section 3.3). Loaded as-is since no explanation for the non-integer values was available; reviewer should confirm whether this reflects a legitimate weighting/estimation convention in the source data or an artifact that should be corrected.
4. **Count Selection IBNR% shows 11 maturity-order reversals** (exceeds the tech review's tolerance of 4; see Section 7). This means IBNR as a percentage of ultimate does not consistently decrease as accident years mature, which is somewhat atypical. Given the fractional-count anomaly (item 3 above) may be a contributing factor, reviewer should assess whether these two issues are related.

**Items I'm flagging as low-confidence:**
- LDF selection cutoff ages diverge materially between the two AI selectors (see Item 1 above) - this is a judgment call with meaningful downstream impact on tail factor magnitude, especially for Reported Count.
- AY 2023-2024 loss ultimates (see Item 2 above) - very immature years with large method divergence and an ELR fallback that is not a true pricing-based a priori.
- Count Selection IBNR% maturity reversals (see Item 4 above), possibly linked to the fractional claim count anomaly.

**Items I think should be escalated to Chief Actuary / Committee:**
- None identified - this is a sample/demonstration run; no items rise to the level of formal escalation.

---

## 12. ASOP Self-Check (for reviewer)

| Standard | Addressed In | Notes |
|---|---|---|
| ASOP 23 (Data Quality) | §3 | |
| ASOP 25 (Credibility) | §4, §5 | |
| ASOP 41 (Communications) | Throughout | Draft — not a final communication |
| ASOP 43 (Unpaid Claim Estimates) | §4, §5, §8 | |
| ASOP 56 (Modeling) | §4 | If applicable |

---

## 13. Peer Review Log

*Reviewer fills this in; analyst responds and updates the draft.*

| # | Date | Reviewer Comment | Analyst Response | Status |
|---|---|---|---|---|
| 1 | | | | Open / Addressed / Deferred |
| 2 | | | | |

**Sign-off checklist (to be completed before moving to final):**
- [ ] All reviewer comments addressed or deferred with rationale
- [ ] Numbers reconcile to supporting workbook
- [ ] Exhibits match narrative
- [ ] Open questions closed or escalated
- [ ] Version history updated

---

## 14. Version History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| v0.1 | 08/27/2026 | Bryce | Initial draft |
| v0.2 | 08/27/2026 | Bryce | Added ultimate selections (Step 7) and completed initial analysis through Step 8 (Analysis.xlsx built) |

---

## Appendices (in accompanying workbook)

- A. Triangles (paid, reported, counts)
- B. Development factor selections
- C. Method indications by segment / AY
- D. Diagnostic exhibits
- E. Data reconciliation worksheet

---

*End of working draft.*