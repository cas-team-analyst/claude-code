---
name: reserving-analysis
description: Actuarial reserving analysis workflow. Use when the user requests reserving. Do NOT use for peer review (separate skill exists).
---

# Reserving Analysis Workflow

## Startup Steps 

**Follow Every Time BEFORE reading PROGRESS.md**

1. Confirm to the user which version of the skill this is: v20260601-04
2. Identify and mount the project folder. Do not use your own folder (may cause max path length issues), ask the user to select one. Obtain permission to modify it. 
3. Identify and mount the plugin skill folder (if applicable, NOT the anthropic-skills folder) so you can copy files from it into the project folder.
4. Check for existing `PROGRESS.md` file in the project folder and use it to understand what the next step is.
5. Only if no `PROGRESS.md` exists:
   - Copy PROGRESS.md, REPORT.md, and REPLICATE.md from `assets/` to project directory. Use copy commands, do NOT read and write the files.
   - Start steps in PROGRESS.md. Mark them in progress/complete as you go.

Then, process to complete each step:
1. Mark status as "In Progress [yyyy-mm-dd]"
2. Inform the user about the step. 
3. Perform the requested action. Keep the user informed as you work.
4. When complete
    - Update REPORT.md
    - Update REPLICATE.md
    - Mark the step as complete with [X]
5. Move on to the next step.

## Cowork Agent Guidelines

- File operations: To work from assets file: mount skill folder first, then copy files with `cp {BASE_DIRECTORY}/{skill_path} {PROJECT_FOLDER}/{target_path}`. DO NOT use `create_file` or Write tool for copying files from assets. Convert Windows paths to Unix: `C:\Users\...` → `/mnt/c/Users/...` If copy fails, STOP and debug. 
- Fix bugs with targeted edits AFTER copying - never rewrite entire files.
- Cache out of date? Suggest close/reopen Cowork. 
- Never use unicode symbols in commands.

## Supporting Files

**Skill folder structure:**
- `assets/` - Templates (PROGRESS.md, REPORT.md, REPLICATE.md, welcome message) and selection framework guide
- `scripts/` - Numbered Python workflow scripts (1a-7) and modules/ subdirectory with shared utilities
- `agents/` - Selector subagents for LDF, tail curve method, and ultimate selections (rules-based and open-ended variants)
