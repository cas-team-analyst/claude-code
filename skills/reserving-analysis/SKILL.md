---
name: reserving-analysis
description: Actuarial reserving analysis workflow. Use when the user requests reserving. Do NOT use for peer review (separate skill exists).
---
# Reserving Analysis Workflow

## Startup Steps

**Follow Every Time BEFORE reading PROGRESS.md**

1. Confirm to the user which version of the skill this is: v20260826.

2. Determine whether you're running as a local Cowork agent (VM/filesystem access to the user's machine) or a cloud Claude agent (no access to the user's local folders). If Cowork: Identify and mount the project folder. Do not use your own folder (may cause max path length issues), ask the user to select one. Obtain permission to modify it. Identify and mount the plugin skill folder (if applicable, NOT the anthropic-skills folder) so you can copy files from it into the project folder.

3. Check for existing `PROGRESS.md` file in the project folder and use it to understand what the next step is.

4. Only if no `PROGRESS.md` exists:
   - Copy PROGRESS.md, REPORT.md, and REPLICATE.md from `assets/` to project directory. Use copy commands, do NOT read and write the files.

5. Begin the next incomplete step in PROGRESS.md.

## Cloud Agent Guidelines

- Share documents with the user as you update them: PROGRESS.md, REPORT.md, REPLICATE.md.

## Cowork Agent Guidelines

Applies only when running as a Cowork agent (see Startup Steps).

- File operations: To work from assets file: mount skill folder first, then copy files with `cp {BASE_DIRECTORY}/{skill_path} {PROJECT_FOLDER}/{target_path}`. DO NOT use `create_file` or Write tool for copying files from assets. Convert Windows paths to Unix: `C:\Users\...` → `/mnt/c/Users/...` If copy fails, STOP and debug.

- Fix bugs with targeted edits AFTER copying - NEVER rewrite entire files.

- Cache out of date? Suggest close/reopen Cowork.

- Never use unicode symbols in commands.


## Supporting Files

**Skill folder structure:**

- `assets/` - Templates (PROGRESS.md, REPORT.md, REPLICATE.md, welcome message, etc.).
- `scripts/` - Numbered Python workflow scripts and modules/ subdirectory with shared utilities.
- `agents/` - Selector subagents for LDF, tail curve, and ultimate selections, each with framework and open-ended variants.
