---
name: help
description: Get oriented with the TeamAnalyst plugin and explore available skills. Use when first getting started, checking what analysis capabilities are available, or surveying skills before beginning work. Trigger phrases "start", "get started", "what can you do", "help", "overview", "show skills".
---

# TeamAnalyst Help

## Quick Reference

**Main workflow:** `/reserving-analysis` — end-to-end loss reserving (data → methods → selections → projections)  
**Peer review:** `/peer-review` — validate completed analysis against ASOP standards  

---

## Step 1: Welcome

Greet the user and briefly introduce the plugin:

TeamAnalyst is an AI-powered actuarial analyst. It walks you through loss reserving — from raw data to development factor selections and ultimate projections — entirely through conversation.

## Step 2: Describe the Available Skills

- **`/reserving-analysis`** — the core workflow. Runs data prep, actuarial methods (Chain Ladder, Initial Expected, Bornhuetter-Ferguson), LDF and tail factor selections, and ultimate projections. Every analysis produces three standard documents: **REPORT.md** (deliverable), **PROGRESS.md** (workflow checklist), and **REPLICATE.md** (reproducibility log). The LDF and tail factor decision frameworks it applies live in the selector agent files under `skills/reserving-analysis/agents/`.
- **`/peer-review`** — reviews a completed analysis against cross-method consistency checks and ASOP standards; produces an advisory findings report without modifying selections.

## Step 3: Explain Interaction Modes

When running `/reserving-analysis`, the user chooses how much control they want:

1. **Careful** — step-by-step review at each stage, full user control over every decision
2. **Selections Only** — automated data prep and calculations, user input only for LDF selections
3. **Fully Automated** — end-to-end execution with no manual intervention

## Step 4: Ask How to Help

Ask what the user is working on and guide them to the right skill. Explain that they can invoke any skill by typing its name (e.g. `/reserving-analysis`).

---

## Reference Sources

If the user asks about specific topics, read the relevant file to answer accurately:

- **ASOP standards** (13, 23, 25, 36, 41, 43) — see the `peer-review` skill
- **Tail curve methods** (Bondy, Exponential Decay, McClenahan, Skurnick, etc.) — see the tail curve selector agents in the `reserving-analysis` skill
- **LDF and tail selection criteria and diagnostic rules** — read the selector agent files directly in `skills/reserving-analysis/agents/` (framework and open-ended variants for LDF, tail curve, and ultimates)

If the referenced skill isn't installed/available, tell the user it's needed for that information rather than guessing at its content.
