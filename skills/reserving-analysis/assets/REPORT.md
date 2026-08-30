# Reserving Analysis — Working Draft

_This is a draft report populated by the reserving-analysis workflow. Sections marked **[Manual]** are not populated by the workflow and require input from the analyst or peer reviewer._

<!-- AI (Phase 1): Fill in Analysis (segment/program name), Valuation Date, Prepared by (analyst name from setup form), and Draft Date (today's date). Leave Draft Version as "v0.1" and Submitted to blank for now. -->
**Analysis:** [Segment / Program Name]
**Valuation Date:** [MM/DD/YYYY]
**Draft Version:** [e.g., v0.3 — For Peer Review]
**Prepared by:** [Analyst Name]
**Submitted to:** [Reviewing Actuary Name]
**Draft Date:** [MM/DD/YYYY]

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

<!-- AI (Phase 8): Write "What this analysis covers" as 1-2 sentences (segment, accident years, methods used). Fill "Where I want the most scrutiny" with the key judgment calls from selections. -->
*A short orientation so the reviewer can get into the work quickly.*

- **What this analysis covers:** [1–2 sentences]
- **What changed since last review (if applicable):** [Bullet the deltas]
- **Where I want the most scrutiny:** [Point the reviewer at the judgment calls]
- **Open questions for reviewer:** See Section 11

---

## 1. Purpose and Scope

### 1.1 Purpose of the Analysis
<!-- AI (Phase 1): Fill in with the purpose from the setup form (e.g., "quarterly reserve review for internal management"). -->
[Why is this analysis being performed? e.g., quarterly reserve review, year-end booking, pricing support, reinsurance renewal, etc.]

### 1.2 Scope
<!-- AI (Phase 1): Fill in Segment/LOB, Basis, Currency, Geography from the setup form. Leave Accident/Underwriting years blank until Phase 3.
     AI (Phase 3): Fill in Accident/Underwriting years range once confirmed from processed data. -->
| Item | Detail |
|---|---|
| Segment(s) / LOB | [ ] |
| Accident / Underwriting years | [ ] |
| Coverages | [Loss / DCC / A&O / ULAE] |
| Basis | [Gross / Ceded / Net] |
| Currency | [ ] |
| Geography | [ ] |

### 1.3 Intended Internal Users
<!-- AI (Phase 1): Fill in with the audience from the setup form. -->
[e.g., Chief Actuary, Reserving Committee, CFO]. This draft is not intended for external distribution in its current form.

---

## 2. Summary of Indications

<!-- AI (Phase 7): Fill in the indications table using totals from selections/Ultimates.xlsx. Fill in Comparison to prior if prior data is available, otherwise note "Not applicable." Fill in Key drivers of change.
     AI (Phase 8): Verify these numbers match the final output from 6-analysis-create-excel.py. -->
*Placeholder numbers — subject to review.*

| Segment | Paid to Date | Case | IBNR | Total Unpaid | Ultimate |
|---|---|---|---|---|---|
| [ ] | | | | | |
| [ ] | | | | | |
| **Total** | | | | | |

**Comparison to prior estimate:**

| Segment | Prior Ultimate | Current Ultimate | Change | % |
|---|---|---|---|---|
| [ ] | | | | |

**Key drivers of change:** [Brief narrative — emergence vs. expected, assumption changes, new data, etc.]

---

## 3. Data

### 3.1 Data Used
<!-- AI (Phase 2): Add one row per data file found during exploration. Include triangle files and any other inputs (source name, as-of date, notes on format/coverage).
     AI (Phase 3): Update to confirm triangle types used. Add a row for the ELR file if present; note if absent. -->
| Data Element | Source | As-of Date | Notes |
|---|---|---|---|
| Paid loss triangles | [ ] | [ ] | |
| Reported loss triangles | [ ] | [ ] | |
| Claim counts (reported/closed) | [ ] | [ ] | |
| Earned premium / exposures | [ ] | [ ] | |
| Case reserves | [ ] | [ ] | |
| Rate change history | [ ] | [ ] | |
| [Other] | | | |

### 3.2 Data Reconciliation
<!-- AI (Phase 2): Note whether data was reconciled to a prior valuation or financial system. If no reconciliation was done, write "Not reconciled — data accepted as provided by [source]." -->
- Reconciled to [financial system / prior valuation / GL] as of [date].
- Reconciliation result: [Clean / Differences of $X explained by Y].

### 3.3 Data Quality Observations
<!-- AI (Phase 2): Note any outliers, gaps, negative development, or unusual patterns noticed during exploration. If none, write "No material data quality issues observed during initial review."
     AI (Phase 3): Add any adjustments made to 1a-load-and-validate.py (e.g., outlier exclusions, negative development corrections). -->
*Per ASOP No. 23 — flag anything unusual.*

- [Outliers, negative development, coding changes, mix shifts, gaps, etc.]
- [Anything you had to adjust or exclude, and why]

### 3.4 Data Limitations
<!-- AI (Phase 3): Note missing data types and how they impact the analysis. Examples: "No closed count data — unable to estimate closure rates", "No ELR file provided — IE/BF methods skipped", "No prior selections available". If ELR fallback was used, add a note here. -->
- [Known limitations and how they were handled]

---

## 4. Methodology

### 4.1 Methods Applied
<!-- AI (Phase 4): Add rows for each method and triangle measure used. Note "Selected via framework with AI cross-check" in Why Selected.
     AI (Phase 6): Update to confirm which methods actually ran vs. were skipped. If IE or BF were skipped, note why. -->
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
<!-- AI (Phase 4): Describe the 14-criteria framework used for LDF selections and the maturity-based weighting approach (e.g., CL for mature years, BF blend for immature). -->
[Describe how methods were weighted by maturity, and any segment-specific logic. Call out where judgment was applied vs. formulaic selection.]

### 4.3 LAE Treatment
**Not applicable.** This analysis assumes loss triangles include LAE (loss and allocated loss adjustment expense combined), or LAE is not being estimated separately. If LAE needs to be estimated separately, that is outside the scope of this workflow.

- **DCC / ALAE:** Not separately estimated
- **A&O / ULAE:** Not separately estimated

---

## 5. Key Assumptions

### 5.1 Development Patterns
<!-- AI (Phase 4): Fill in selection basis (volume-weighted averages, averaging windows, framework method).
     AI (Phase 5): Add tail curve details: which method was selected for each measure (Bondy, Exponential Decay, etc.) with R² values and leave-one-out test results. -->
- **Selection basis:** [e.g., volume-weighted 5-year average with outlier adjustment]
- **Tail:** [Source — curve fit, industry benchmark, judgment]

### 5.2 Expected Loss Ratios (for B-F and ELR methods)
<!-- AI (Phase 6/7): If IE/BF ran, populate this table with the a priori ELRs by accident year. If these methods were skipped, write "Not applicable — IE/BF not used." -->
| AY | ELR | Basis |
|---|---|---|
| | | |

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
<!-- AI (Phase 3): If ELR fallback was used, note the source in the ELR bullet below.
     AI (Phase 7): Fill in the ELR source if BF/IE ran, otherwise confirm "Not applicable — CL only". -->
**Material assumptions in this analysis:**
- **LDF selections:** Based on volume-weighted averages with framework (14 criteria) and AI cross-check. See Section 4.2 and LDF selection workbooks for detailed reasoning.
- **Tail factors:** Based on curve fitting (Bondy, Exponential Decay, etc.) with leave-one-out validation. See tail selection workbook for detailed reasoning.
- **Expected loss ratios (if used):** [Fill in source if BF/IE methods were used, otherwise note "Not applicable - CL only"]

*Any assumption primarily judgment-driven should be flagged in Section 11.*

---

## 6. Results by Segment

<!-- AI (Phase 7): Create one subsection per category (Loss, Count). For each: reference the ultimates file, summarize method weighting (e.g., "CL for mature years, BF for immature"), and list any notable judgment calls or manual overrides from Ultimates.xlsx. -->
*Detailed exhibits live in the accompanying workbook; summarize selections and rationale here.*

### 6.1 [Segment A]
- Selected ultimates: [Reference exhibit]
- Method weighting: [Summary]
- Notable judgment calls: [ ]

### 6.2 [Segment B]
- [ ]

---

## 7. Diagnostics and Reasonableness Checks

<!-- AI (Phase 9): Check off each item below and add brief notes. Under "Anomalies to investigate", list all FAIL and WARN items from 7-tech-review.py output. -->
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

> **[Manual]** This section is not populated by the workflow. If you perform sensitivity testing after the workflow completes, fill in the table below.

**Not implemented in this analysis.** Sensitivity testing would require re-running projections with varied assumptions. This can be added in future iterations.

| Assumption | Change | Impact on Total Ultimate |
|---|---|---|
| Tail factor | ± (not tested) | (not tested) |
| ELR | ± (not tested) | (not tested) |
| LDF selections | ± (not tested) | (not tested) |

### 8.2 Sources of Uncertainty
<!-- AI (Phase 9): Describe key risk factors from the tech review. Cover process risk (thin data, recent years), parameter risk (tail uncertainty, LDF volatility), model risk (CL vs. BF choice for immature years), and any systemic flags (large losses, etc.). -->
*Per ASOP No. 43 — discuss the risks that could cause actuals to differ from estimate.*

- Process / parameter / model / systemic risk commentary as applicable
- Segment-specific risk factors: [ ]

---

## 9. Reliance on Others

<!-- AI (Phase 8): List data sources and contacts relied upon (e.g., "Claims Department — triangle data as of [date]"). If no external reliance, write "No external sources relied upon beyond internal company data systems." -->
| Source | Information Relied Upon |
|---|---|
| [Claims / Underwriting / Finance contact] | [ ] |
| [External benchmark or data source] | [ ] |

---

## 10. Information Date and Subsequent Events

<!-- AI (Phase 8): Fill in the valuation/as-of date. Under Subsequent events, write "None known as of [draft date]" or describe any known events. -->
- **Information Date:** [ ]
- **Subsequent events considered:** [None known / Describe]

---

## 11. Open Questions for Reviewer

<!-- AI (Phase 4): Add any LDF selections flagged as low-confidence or where framework and AI selections diverged materially.
     AI (Phase 5): Add any tail selections where curve fit diagnostics were poor (R² < 0.85) or framework/AI diverged.
     AI (Phase 7): Add any accident years where method indications diverged materially (>20% between CL and BF) or required significant judgment. -->
*The key section — where you flag judgment calls you want a second opinion on.*

1. [Specific question with context — e.g., "AY 2023 paid emergence is 15% below expected; I kept selections unchanged pending more data. Agree?"]
2. [ ]
3. [ ]

**Items I'm flagging as low-confidence:**
- [ ]

**Items I think should be escalated to [Chief Actuary / Committee]:**
- [ ]

---

## 12. ASOP Self-Check (for reviewer)

> **[Manual — reviewer]** This section is completed by the peer reviewer, not the workflow. The reviewer fills in the Notes column during the `/peer-review` session.

| Standard | Addressed In | Notes |
|---|---|---|
| ASOP 23 (Data Quality) | §3 | |
| ASOP 25 (Credibility) | §4, §5 | |
| ASOP 41 (Communications) | Throughout | Draft — not a final communication |
| ASOP 43 (Unpaid Claim Estimates) | §4, §5, §8 | |
| ASOP 56 (Modeling) | §4 | If applicable |

---

## 13. Peer Review Log

> **[Manual — reviewer]** This section is completed during the peer review process. Use `/peer-review` in a new chat to generate reviewer comments; bring them back here to track and respond.

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

<!-- AI (Phase 1): Add the analyst name and today's date to the v0.1 row.
     AI (Phase 8): Add a new row with today's date and a summary of changes since v0.1. -->
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