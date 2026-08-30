# Peer Review Progress Tracking

ALWAYS COME BACK TO THIS FILE TO MARK A [] STEP COMPLETE BEFORE STARTING THE NEXT [] STEP.

Process to complete each step:
1. Mark status as "In Progress [yyyy-mm-dd]"
2. Inform the user about the step.
3. Perform the requested action. Keep the user informed as you work.
4. When complete, mark the step as complete with [X].
5. Move on to the next step.

# Step 1: Setup and Readiness Check

- [ ] Use bash cp to copy PEER_REVIEW_PROGRESS.md from skill assets into the analysis folder, if not already present. Do NOT read or write it to copy it. Send it to the user as a file so they can see it. Track the PEER_REVIEW_PROGRESS.md steps in the task list as you go.

- [ ] Use bash cp to copy `PEER_REVIEW_REPORT.template.md` from skill assets into the analysis folder root as `PEER_REVIEW_REPORT.md` (do NOT read or write it to copy it). Fill in the header fields: Analysis folder (path), Review date (today), and the Files reviewed list. Send it to the user as a file so they can see it. 

- [ ] Verify required files exist in the analysis folder: `Analysis.xlsx`, `Tech Review.xlsx`, `REPORT.md`, `REPLICATE.md`, `PROGRESS.md`.

- [ ] Confirm the analysis is ready for review: steps in PROGRESS.md are complete. If the analysis is incomplete, stop and advise the user to finish reserving-analysis first.

# Step 2: Read Source Files

- [ ] Read `Analysis.xlsx`, `Tech Review.xlsx`, `REPORT.md`, and `REPLICATE.md` from the analysis folder. This is a review only - never edit these source files.

# Step 3: Run Checks

- [ ] Prioritize high-materiality segments - largest reserves, widest method spreads.

- [ ] **Check 1 - Cross-Method Consistency:** Paid development factors should generally exceed incurred - flag if violated consistently across accident periods. If one method is consistently higher or lower than another across all periods, the tail or selections may need adjustment (methods alternating higher/lower one year to the next is not a systematic bias). If BF is consistently higher/lower than development methods, the expected loss ratio seed may be mis-calibrated.

- [ ] Update PEER_REVIEW_REPORT.md's "Cross-Method Consistency" section with findings from Check 1. Frame as advisory - "you may want to consider..." not "you must change...".

- [ ] **Check 2 - Paid vs Incurred Ultimate Reasonability:** If paid ultimate < incurred losses, the paid method likely shouldn't be averaged in - unless the incurred triangle shows significant negative development, in which case a lower paid ultimate may be appropriate. Flag these situations and note the incurred development pattern.

- [ ] Update PEER_REVIEW_REPORT.md's "Paid vs Incurred Ultimate Reasonability" section with findings from Check 2.

- [ ] **Check 3 - Recent Year Loss Ratio / Loss Rate Stability:** Compare the implied loss ratio (or loss rate) from the most recent 2 accident years against more mature years. If recent years produce ratios materially higher or lower, flag it - this often indicates LDFs are too highly leveraged and BF methods should be preferred for those years.

- [ ] Update PEER_REVIEW_REPORT.md's "Recent Year Loss Ratio / Loss Rate Stability" section with findings from Check 3.

- [ ] **Check 4 - ASOP Review:** List the ASOP reference files in skill assets (e.g. `ls assets/asop-*.md`). Add one new item to this document and to the task-list for each file found. Each new item should follow this template: "- [ ] Review ASOP [asop_number]. Send it to the user as a file so they can review it while waiting. Check the analysis against its Key Requirements, Red Flags, Disclosure / Documentation Checks, and Common Misapplications. Update PEER_REVIEW_REPORT.md's "ASOP Review" section with findings." Then proceed with the first new step and go from there.

- [ ] **Check 5 - Diagnostic Consistency:** Do selected factors align with the diagnostic exhibits (e.g., residual plots, weighted averages, volume-weighted averages)? Are outlier exclusions documented and justified?

- [ ] Update PEER_REVIEW_REPORT.md's "Diagnostic Consistency" section with findings from Check 5.

- [ ] **Check 6 - Documentation Quality:** Are all REPORT.md sections filled in (not just boilerplate), with assumptions, methods, and rationale documented? Can another actuary reproduce the analysis from REPLICATE.md (scripts, manual edits, data sources listed)? Actuarial communication standards (ASOP 41) were already checked.

- [ ] Update PEER_REVIEW_REPORT.md's "Documentation Quality" section with findings from Check 6.

- [ ] **Check 7 - Technical Review Diagnostics:** Confirm all automated diagnostic tests in Tech Review.xlsx passed or were appropriately addressed. Are any flagged issues properly documented in REPORT.md Section 7? Review loss ratio progression, frequency/severity trends, and actual vs expected emergence.

- [ ] Update PEER_REVIEW_REPORT.md's "Technical Review Diagnostics" section with findings from Check 7.

# Step 4: Document Findings

- [ ] Fill in PEER_REVIEW_REPORT.md's "Summary" (2-3 sentence overall assessment) and "High-Priority Findings" sections, drawing on the per-check findings already recorded in Step 3. Frame all feedback as advisory - "you may want to consider..." not "you must change...".

- [ ] Fill in PEER_REVIEW_REPORT.md's "Proposed Alternatives" section: where the reviewer would select differently, show both the analyst's selection and the proposed alternative with rationale. Do NOT apply changes.

- [ ] Send `PEER_REVIEW_REPORT.md` to the user as a file so they can review the findings.

# Step 5: Wrap Up

- [ ] Summarize the high-priority findings to the user directly in chat.

- [ ] Mark this progress file complete and ask the user if they have questions about any finding.
