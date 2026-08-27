# Replication Instructions

This document provides step-by-step instructions to reproduce the analysis results. A reviewer can follow these steps to validate the analysis without AI assistance.

_It should be filled in as you make your way through the PROGRESS.md steps._

# Document Structure

- Describe data. 
- Scripts to run in order.
- Manual edits and selections (with reasoning)
- Should enable reproduction without AI assistance

# Overview

- **Analysis name:** Sample Run - Triangle Examples
- **Prepared by:** Bryce
- **Draft Date:** 08/27/2026
- **Interaction mode:** Fully Automatic (no pauses; AI makes all selections)

# Steps to Reproduce

## Step 1: Project Setup

- Folders created: `raw-data/`, `processed-data/`, `selections/`, `scripts/`, `ultimates/`
- Interaction mode selected: Fully Automatic
- Triangle file copied to `raw-data/Triangle_Examples_1.xlsx`

## Step 2: Exploratory Data Analysis

- Reviewed `raw-data/Triangle_Examples_1.xlsx` using `preview_data_file()`. Sheets found: Tri 1 (metadata: Line WC, clerical/low hazard risk, payroll $100M-$500M), Paid 1 (paid loss triangle), Inc 1 (incurred loss triangle), Ct 1 (claim count triangle), Exposure (Accident Year x Payroll).
- No ELR file, no prior LDF/tail selections, no closed-count triangle identified during review.

## Step 3: Data Intake

- Input files in `raw-data/`: `Triangle_Examples_1.xlsx` (single workbook containing Paid, Incurred, Reported Count, and Exposure/payroll data by accident year).
- Scripts run (in order): `1a-load-and-validate.py`, `1b-calculate-ldfs.py`, `1c-diagnostics.py`, `1d-ldf-averages.py`.
- Customizations made to `1a-load-and-validate.py`:
  - Implemented `_read_wide_triangle()` to parse the workbook's wide triangle layout: on the Paid 1/Inc 1 sheets there is a title row ("Age of Evaluation") above the real header row; the real header row has "Accident Year" in column A and development ages (months) across the remaining columns. The parser locates the "Accident Year" row dynamically, then melts to long format.
  - The Ct 1 (count) sheet has no title row above its header (header is the first row) - same melt logic applied directly.
  - Ct 1 classified as measure = "Reported Count" (no "Closed" qualifier present in headers/context, per the default assumption in the script docstring).
  - Exposure sheet loaded in simple 2-column format (period, value), with age=None, unit_type="Dollars" (annual payroll).
  - `TRIANGLE_FILE` variable set to `"Triangle_Examples_1.xlsx"`; `DATA_FILE_PATH`/`OUTPUT_PATH` left at their `modules/config.py` defaults (`../raw-data/`, `../processed-data/`), which were already correct for this project's folder layout.
- No prior LDF selections, no prior tail factor selections, and no Expected Loss Rate (ELR) file were available. User selected the ELR fallback option: `3-ie-ultimates.py`'s built-in 3-year rolling average of empirical loss-per-payroll, by accident year, used as the a priori expectation for Initial Expected/BF methods.
- Output files created in `processed-data/`: `1_triangles.csv` (924 rows), `2_enhanced.csv` (LDFs by AY/age), `3_diagnostics.csv` (diagnostic ratios), `4_ldf_averages.csv` (LDF averages: simple, volume-weighted, exclude-high-low, over 3/5/10-yr and all-year windows, plus CV and slope stability metrics).
- Data validation confirmed by user on 2026-08-27 ("Looks good").

## Step 4: Chain Ladder LDF Selections

- Ran `2a-chainladder-create-excel.py` to create `selections/Chain Ladder Selections - LDFs.xlsx` and export per-measure context files (`chainladder-context-incurred_loss.md`, `chainladder-context-paid_loss.md`, `chainladder-context-reported_count.md`).
- Framework AI selector (`selector-chain-ladder-ldf-ai-framework`) and Open-Ended AI selector (`selector-chain-ladder-ldf-ai-open-ended`) were each invoked once, independently, across all three measures. Six JSON files were created (`chainladder-ai-framework-<measure>.json`, `chainladder-ai-open-ended-<measure>.json`).
- Ran `2b-chainladder-update-selections.py` to populate the Excel workbook with both selection rows (Framework: 40 selections across 3 measures; Open-Ended: 68 selections across 3 measures).
- **All selections are from the Framework AI Selection row** (no user overrides in this Fully Automatic run). Framework AI cutoff ages: Paid/Incurred Loss cut off at 203-215 months (last selected interval 191-203); Reported Count cut off at 71-83 months (last selected interval 59-71).
- To replicate: Extract final selections from the User Selection row if present, otherwise use the Framework AI Selection row. Do not re-run the AI selector.

## Step 5: Chain Ladder Tail Curve Method Selections

- Ran `2c-tail-methods-diagnostics.py` to fit tail curves (Bondy, Modified Bondy variants, Exponential Decay variants, McClenahan, Skurnick) and generate diagnostics. Note: the script's cutoff-age logic falls back Framework AI Selection -> Open-Ended AI Selection per interval, so where Framework AI selections stopped early, Open-Ended AI selections filled the gap, extending the effective cutoff used for curve fitting to 275 months (Paid Loss, Incurred Loss) and 263 months (Reported Count).
- Ran `2d-tail-create-excel.py` to create `selections/Chain Ladder Selections - Tail.xlsx` and export context files (`tail-context-incurred_loss.md`, `tail-context-paid_loss.md`, `tail-context-reported_count.md`). No prior tail selections existed.
- Framework tail selector (`selector-tail-curve-ai-framework`) and Open-Ended tail selector (`selector-tail-curve-ai-open-ended`) were each invoked once, independently, across all three measures. Six JSON files were created (`tail-curve-ai-framework-<measure>.json`, `tail-curve-ai-open-ended-<measure>.json`).
- Ran `2e-tail-update-selections.py` to populate the Excel workbook with both selection rows.
- **All selections are from the Framework AI Selection row** (no user overrides in this Fully Automatic run):
  - Paid Loss: Modified Bondy (double deviation), tail factor 1.0140
  - Incurred Loss: Bondy, tail factor 1.0000
  - Reported Count: Bondy, tail factor 1.0000
- To replicate: Extract final tail curve methods from the User Selection row if present, otherwise use the Framework AI Selection row. Fitted LDFs are generated by `2f-chainladder-ultimates.py` using the selected curve method. Do not re-run the AI selector.

## Step 6: Calculate Method Projections

- Ran `2f-chainladder-ultimates.py`: read empirical LDFs from `selections/Chain Ladder Selections - LDFs.xlsx` (Framework AI Selection row, falling back to Open-Ended AI Selection per interval where Framework AI is blank), read tail curve methods from `selections/Chain Ladder Selections - Tail.xlsx` (Framework AI Selection row), loaded curve parameters from `processed-data/tail-scenarios.csv`, built complete CDFs, and calculated Chain Ladder ultimates. Output: `ultimates/projected-ultimates.csv` (columns `ultimate_cl`, `ibnr_cl` added, 96 rows: 24 periods x 4 measures including Exposure).
- Ran `3-ie-ultimates.py`: no ELR file was found, so it used its built-in fallback (3-year rolling average of Incurred Loss actual / payroll for expected loss rate; 3-year rolling average of Reported Count / payroll for expected frequency). Computed Initial Expected ultimates for Paid Loss, Incurred Loss, Reported Count, and Closed Count (using Reported Count frequency as proxy, since no Closed Count triangle exists). Output columns `ultimate_ie`, `ibnr_ie` added to `ultimates/projected-ultimates.csv` (120 rows after merge).
- Ran `4-bf-ultimates.py`: combined Chain Ladder and Initial Expected ultimates into Bornhuetter-Ferguson ultimates for Paid Loss, Incurred Loss, Reported Count. Output columns `ultimate_bf`, `ibnr_bf` added to `ultimates/projected-ultimates.csv`.
- No methods were skipped — all three ran successfully because Exposure (payroll) data was available to support the ELR fallback.
- Output file: `ultimates/projected-ultimates.csv` with columns from all three methods (`ultimate_cl`/`ibnr_cl`, `ultimate_ie`/`ibnr_ie`, `ultimate_bf`/`ibnr_bf`) alongside `actual`, `cdf`, `pct_developed` by period and measure.

## Step 7: Ultimate Selections

- Ran `scripts/5a-ultimates-create-excel.py` to create `selections/Ultimates.xlsx` with **Losses** (Incurred + Paid) and **Counts** (Reported + Closed) sheets, and export context files (`ultimates-context-loss.md`, `ultimates-context-count.md`).
- Framework ultimates selector (`selector-ultimates-ai-framework`) and Open-Ended ultimates selector (`selector-ultimates-ai-open-ended`) were each invoked once, independently, covering both categories (Loss and Count) across all 24 accident years. Four JSON files were created (`ultimates-ai-framework-loss.json`, `ultimates-ai-framework-count.json`, `ultimates-ai-open-ended-loss.json`, `ultimates-ai-open-ended-count.json`).
- Ran `scripts/5b-ultimates-update-selections.py` to populate the Excel workbook with both selection columns (48 framework updates, 48 open-ended updates).
- Ran `scripts/5c-summary-indications.py` to compute headline indications from the selected ultimates. Output: `selections/summary-indications.json`, plus the markdown tables recorded in PROGRESS.md ("Headline Indications") and REPORT.md (Section 2).
- **All selections are from the Framework AI Selection column** (no user overrides in this Fully Automatic run):
  - Loss: Incurred selected throughout; Chain Ladder for mature years, CL/BF blend for mid-maturity years, BF/IE-weighted for the greenest years (2023-2024, CL disqualified as unstable).
  - Count: Reported Count used throughout (no Closed Count triangle available); Chain Ladder for fully-developed years (2001-2023), CL/BF blend for 2024.
- To replicate: Extract final ultimates from the User Selection column if present, otherwise use the Framework AI Selection column. Do not re-run the AI selector.

## Step 8: Build Analysis Workbook

- Ran `scripts/6-analysis-create-excel.py`. It read `ultimates/projected-ultimates.csv` and `selections/Ultimates.xlsx` (48 selections loaded), plus LDF/CDF detail and tail selections for all 3 measures.
- Output file created: `Analysis.xlsx` (in the project root, not `output/` - despite `config.OUTPUT` pointing there, the script writes to `../Analysis.xlsx` relative to `scripts/`). Contains: Loss sheets (Chain Ladder / Initial Expected / BF for Incurred and Paid), Counts sheets (Chain Ladder / Initial Expected / BF for Reported Count; Closed Count CL sheet skipped - no data), CL LDF triangle sheets, Pre-Method Diagnostics, Post-Method Diagnostics, and a Notes sheet.
- Key Outputs: `Analysis.xlsx` is the primary numerical deliverable, consolidating all methods, selections, and diagnostics into one workbook alongside the standalone selection workbooks (`selections/Chain Ladder Selections - LDFs.xlsx`, `selections/Chain Ladder Selections - Tail.xlsx`, `selections/Ultimates.xlsx`) and `REPORT.md` as the narrative deliverable.

## Step 9: Technical Review & Peer Review

- Ran `scripts/7-tech-review.py` against `Analysis.xlsx`. Result: 94 checks run, 64 PASS, 30 WARN, 0 FAIL. Full detail saved to `Tech Review.xlsx`.
- Notable WARN-level flags: YoY severity spikes (up to 232%) in several periods; negative cells and maturity-order reversals in the "Average IBNR"/"Average Unpaid" diagnostic triangles; several X-to-Ult ratio cells exceeding 1.0; link ratios exceeding the diagnostic ceiling at the youngest development ages; 11 maturity-order reversals in Count Selection IBNR% (exceeds the tolerance of 4). None were FAIL-level.
- No issues required correcting the data or rerunning upstream scripts - all flags were noted in REPORT.md (Section 7 Anomalies, Section 8.2 Sources of Uncertainty, Section 11 Open Questions) for reviewer awareness.
- Suggested to the user that they run `/peer-review` in a separate session for an independent AI review of the completed analysis.