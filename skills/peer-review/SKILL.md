---
name: peer-review
description: Peer review of completed reserve analysis. Use after reserving-analysis workflow finishes. Do NOT use during initial analysis (separate skill exists).
---

# Actuarial Peer Review

**Key principles:**
- **Advisory only** - propose, never override. Use language like "consider whether…" and "this may warrant…"
- **Materiality-first** - focus on largest reserves and widest method spreads
- **ASOP-grounded** - check against ASOP 23, 25, 36, 41, 43 standards
- **Show your work** - when proposing alternatives, include the numeric comparison
- **Clear feedback** - findings actionable by both AI and human users

# Startup Steps

**Follow Every Time BEFORE reading PEER_REVIEW_PROGRESS.md**

1. Identify and mount the plugin skill folder (if applicable, NOT the anthropic-skills folder).
2. Identify the analysis folder - where the completed analysis lives (project root folder).
3. Check for an existing `PEER_REVIEW_PROGRESS.md` in the analysis folder and use it to understand what the next step is.
4. Only if no `PEER_REVIEW_PROGRESS.md` exists: use bash cp to copy `PEER_REVIEW_PROGRESS.md` from skill assets into the analysis folder. Do NOT read or write it to copy it. Send it to the user as a file so they can see it. Track the PEER_REVIEW_PROGRESS.md steps in the task list as you go.
5. Begin the next incomplete step in `PEER_REVIEW_PROGRESS.md`.

# Cowork Agent Guidelines

Applies only when running as a Cowork agent (see Startup Steps).

- **File operations:** Use `cp` for file operations. Convert Windows paths to Unix: `C:\Users\...` → `/mnt/c/Users/...`. Mount skill folder first if accessing templates.
- **Output:** Write findings to `PEER_REVIEW_REPORT.md` in the analysis folder root (alongside REPORT.md, REPLICATE.md, PROGRESS.md, PEER_REVIEW_PROGRESS.md).
- **Other:** Cache out of date? Suggest close/reopen Cowork. Never use unicode symbols in commands.