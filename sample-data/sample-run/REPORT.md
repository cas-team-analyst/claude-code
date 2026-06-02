# Reserving Analysis — Working Draft

_This is a draft report that should be filled in as you make your way through the PROGRESS.md steps._

**Analysis:** Sample Run
**Valuation Date:** [MM/DD/YYYY]
**Draft Version:** v0.1 — Initial Draft
**Prepared by:** Bryce
**Submitted to:** [Reviewing Actuary Name]
**Draft Date:** 2026-06-01

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

- **What this analysis covers:** Workers Compensation reserving analysis (AY 2001–2024) using Chain Ladder, Initial Expected (ELR fallback), and Bornhuetter-Ferguson methods. Produced as a sample run of the TeamAnalyst plugin.
- **What changed since last review:** Not applicable — initial analysis.
- **Where I want the most scrutiny:** (1) Tail curve method: rules-based chose Bondy (1.003/1.005) vs. open-ended's exp_dev_quick_exact_last (1.072/1.066) — material difference in implied IBNR. (2) AY 2007 large-loss year selected at full CL weight — verify this is appropriate. (3) AY 2024 BF selection is almost entirely a priori-driven given only 11 months of development.
- **Open questions for reviewer:** See Section 11

---

## 1. Purpose and Scope

### 1.1 Purpose of the Analysis
Sample reserving analysis demonstrating the TeamAnalyst plugin workflow. Full actuarial conclusions are for demonstration purposes only.

### 1.2 Scope
| Item | Detail |
|---|---|
| Segment(s) / LOB | Workers Compensation (WC) — clerical, relatively low hazard |
| Accident / Underwriting years | 2001 - 2024 |
| Coverages | Loss (Paid and Incurred), Claim Counts |
| Basis | Gross (not specified in data) |
| Currency | USD |
| Geography | Not specified |

### 1.3 Intended Internal Users
Internal reserving team. This analysis is a sample run using the TeamAnalyst plugin.

---

## 2. Summary of Indications

*Placeholder numbers — subject to review.*

| Segment | Paid to Date | Case Reserves | IBNR | Total Unpaid | Ultimate |
|---|---|---|---|---|---|
| Loss (WC) | $41,767,854 | $1,848,541 | $4,276,695 | $6,125,236 | $47,893,090 |
| Count (Reported) | 9,716 | — | 27 | 27 | ~9,743 |

**Comparison to prior estimate:**

| Segment | Prior Ultimate | Current Ultimate | Change | % |
|---|---|---|---|---|
| Loss (WC) | N/A | $47,893,090 | N/A | N/A |
| Count (Reported) | N/A | ~9,743 | N/A | N/A |

**Key drivers of change:** Not applicable — no prior estimate available for comparison.

---

## 3. Data

### 3.1 Data Used
| Data Element | Source | As-of Date | Notes |
|---|---|---|---|
| Paid loss triangles | Triangle Examples 1.xlsx (Paid 1 sheet) | ~Nov 2024 (AY 2024 at age 11mo) | AY 2001-2024, 24 evaluation ages (11-287 mo) |
| Incurred loss triangles | Triangle Examples 1.xlsx (Inc 1 sheet) | ~Nov 2024 | AY 2001-2024, same structure as paid |
| Claim counts (reported) | Triangle Examples 1.xlsx (Ct 1 sheet) | ~Nov 2024 | AY 2001-2024, same structure |
| Payroll exposure | Triangle Examples 1.xlsx (Exposure sheet) | 2024 | AY 2001-2024, annual payroll in USD |
| Case reserves | Embedded in incurred triangle (incurred = paid + case) | ~Nov 2024 | Not provided separately |
| Rate change history | Not provided | — | Not applicable for this sample run |
| Expected loss rates | Not provided | — | Fallback: 3-yr rolling avg of empirical rates |

### 3.2 Data Reconciliation
- Not reconciled to external source — data accepted as provided from Triangle Examples 1.xlsx.
- Reconciliation result: Not performed.

### 3.3 Data Quality Observations
*Per ASOP No. 23 — flag anything unusual.*

- No material outliers, negative development, or coding anomalies observed during initial review. Data appears clean and complete.
- No adjustments or exclusions required.

### 3.4 Data Limitations
- No separate closed count triangle — only reported counts available. Closed-count-based CDFs cannot be calculated. - No ELR file provided — using 3-year rolling average of empirical loss rates as fallback for Initial Expected/BF methods. No closed count data — only reported counts available.

---

## 4. Methodology

### 4.1 Methods Applied
| Method | Segments Applied | Why Selected |
|---|---|---|
| Paid LDF | [ ] | |
| Reported LDF | [ ] | |
| Paid B-F | [ ] | |
| Reported B-F | [ ] | |
| Expected Loss Ratio | [ ] | |
| Frequency-Severity | [ ] | |
| [Other] | | |

### 4.2 Method Weighting / Selection Logic
[Describe how methods were weighted by maturity, and any segment-specific logic. Call out where judgment was applied vs. formulaic selection.]

### 4.3 LAE Treatment
**Not applicable.** This analysis assumes loss triangles include LAE (loss and allocated loss adjustment expense combined), or LAE is not being estimated separately. If LAE needs to be estimated separately, that is outside the scope of this workflow.

- **DCC / ALAE:** Not separately estimated
- **A&O / ULAE:** Not separately estimated

---

## 5. Key Assumptions

### 5.1 Development Patterns
- **Selection basis:** [e.g., volume-weighted 5-year average with outlier adjustment]
- **Tail:** [Source — curve fit, industry benchmark, judgment]

### 5.2 Expected Loss Ratios (for B-F and ELR methods)
No ELR file provided. A 3-year rolling average of empirical loss rates (actual losses / payroll exposure) is used as a fallback expected loss rate for the Initial Expected and Bornhuetter-Ferguson methods. Fallback ELRs (3-yr rolling avg of empirical incurred loss / payroll): AY 2001 ~1.0%, graduating to ~0.9% in mid-years, ~1.0% for AY 2020-2024. Values computed automatically by 3-ie-ultimates.py.

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
- **LDF selections:** Based on volume-weighted averages with rule-based framework (14 criteria) and AI cross-check. See Section 4.2 and LDF selection workbooks for detailed reasoning.
- **Tail factors:** Based on curve fitting (Bondy, Exponential Decay, etc.) with leave-one-out validation. See tail selection workbook for detailed reasoning.
- **Expected loss ratios (if used):** [Fill in source if BF/IE methods were used, otherwise note "Not applicable - CL only"]

*Any assumption primarily judgment-driven should be flagged in Section 11.*

---

## 6. Results by Segment

### 6.1 Loss (Workers Compensation — Paid + Incurred)
- **Selected ultimates:** See Ultimates.xlsx, Losses sheet
- **Method weighting:** Mature years (AY 2001–2015) use Chain Ladder (Incurred or Paid) at 100%; mid-maturity years (AY 2016–2020) blend CL 55–80% / BF 20–45%; immature years (AY 2021–2024) are BF-dominated (50–70%), with CL limited to a cross-check
- **Notable judgment calls:** AY 2007 shows materially elevated incurred ($4.81M vs ~$1.5M typical) — CL selected at full weight since IE/BF a priori cannot reflect this event; AY 2024 (11 months) uses Paid BF exclusively due to extreme CL leverage

### 6.2 Count (Workers Compensation — Reported)
- **Selected ultimates:** See Ultimates.xlsx, Counts sheet
- **Method weighting:** AY 2001–2022 fully developed (CDF=1.000) — actuals equal ultimates; AY 2023–2024 use BF with CL cross-check
- **Notable judgment calls:** None — count development is near-trivial beyond 35 months
---

## 7. Diagnostics and Reasonableness Checks

- [ ] Loss ratios by AY — reasonable progression?
- [ ] Frequency / severity trends — consistent with assumptions?
- [ ] Implied paid and reported development — consistent with patterns?
- [ ] Actual vs. expected emergence since prior review
- [ ] Comparison to independent benchmark (if available)
- [ ] Hindsight test on prior ultimates
- [ ] Ratio of IBNR to case reserves — reasonable?

**Anomalies to investigate:** [List anything the diagnostics flagged]

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

- Process / parameter / model / systemic risk commentary as applicable
- Segment-specific risk factors: [ ]

---

## 9. Reliance on Others

| Source | Information Relied Upon |
|---|---|
| [Claims / Underwriting / Finance contact] | [ ] |
| [External benchmark or data source] | [ ] |

---

## 10. Information Date and Subsequent Events

- **Information Date:** [ ]
- **Subsequent events considered:** [None known / Describe]

---

## 11. Open Questions for Reviewer

*The key section — where you flag judgment calls you want a second opinion on.*

1. [Specific question with context — e.g., "AY 2023 paid emergence is 15% below expected; I kept selections unchanged pending more data. Agree?"]
2. [ ]
3. [ ]

**Items I'm flagging as low-confidence:**
- [ ]

**Items I think should be escalated to [Chief Actuary / Committee]:**
- [ ]

**AY 2002 negative IBNR (fix required):** Rules-based ultimate blend ($2,297,495) falls below incurred actual ($2,327,734) due to low Paid CL pulling the blend. Selected ultimate should be floored at max(incurred, paid) actual — currently shows IBNR = -$30,239.

**Tail curve method divergence (high priority):** Rules-based selector chose conservative Bondy tail for Incurred Loss (1.003) and Paid Loss (1.005), while open-ended selector chose exp_dev_quick_exact_last (1.072/1.066). Reviewer should evaluate which is more appropriate given late-age development patterns.

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
| 2 | v0.1 | 2026-06-01 | Bryce | Initial draft — full workflow run via TeamAnalyst plugin |

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
| v0.1 | | | Initial draft |
| v0.2 | | | |

---

## Appendices (in accompanying workbook)

- A. Triangles (paid, reported, counts)
- B. Development factor selections
- C. Method indications by segment / AY
- D. Diagnostic exhibits
- E. Data reconciliation worksheet

---

*End of working draft.*