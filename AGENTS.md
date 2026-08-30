@./skills/reserving-analysis/SKILL.md
@./skills/peer-review/SKILL.md

Use caveman ultra mode unless asked not to.

Start with `/reserving-analysis` for the main workflow.

Skills live in `skills/`. Selector and reference subagent prompts live in `skills/reserving-analysis/agents/`.

When modifying the workflow itself, treat the files in `skills/` as the primary generalized behavior and use `sample-data/sample-run/` for smoke tests against specific sample data.