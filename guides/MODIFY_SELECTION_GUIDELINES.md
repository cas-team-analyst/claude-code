## Customizing Selection Logic

The TeamAnalyst plugin uses customizable selection logic frameworks for LDF selections, tail factors, and ultimates. These frameworks live directly in the selector agent files, not in a separate skill:

| File | Purpose |
|---|---|
| [`selector-chain-ladder-ldf-ai-framework.agent.md`](https://github.com/cas-team-analyst/team-analyst/blob/main/skills/reserving-analysis/agents/selector-chain-ladder-ldf-ai-framework.agent.md) | LDF selection framework (criteria + diagnostic adjustment rules) |
| [`selector-tail-curve-ai-framework.agent.md`](https://github.com/cas-team-analyst/team-analyst/blob/main/skills/reserving-analysis/agents/selector-tail-curve-ai-framework.agent.md) | Tail factor selection framework |
| [`selector-ultimates-ai-framework.agent.md`](https://github.com/cas-team-analyst/team-analyst/blob/main/skills/reserving-analysis/agents/selector-ultimates-ai-framework.agent.md) | Ultimates selection framework |

**To view or modify:** open the relevant file above (requires write access via Claude Code, the IDE extension, or a local editor; plugin files are read-only in Cowork), or ask Claude to read and explain/edit it for you. Each file documents its own thresholds, decision hierarchy, and criteria, so read it directly for specifics on what can be changed.

After modifying, run `python plugins/create_plugin_zip_cowork.py` (and `python skills-import/create_skills_zips.py` if you also distribute per-skill zips) to rebuild the packaged artifacts.
