---
name: avalonia-codex-plugin
description: Repo-local umbrella skill for building, reviewing, designing, porting, and migrating Avalonia 12 applications with modern XAML/C# patterns. Use when working inside this repository and the request is broad Avalonia 12 work; route quickly to the focused plugin skills for startup, bindings, styling, controls, layout, rendering, testing, design systems, or HTML/WinForms/WPF/WinUI/legacy Avalonia migration work.
---

# Avalonia Codex Plugin

Use this as the repo-local entrypoint when Codex is operating inside this repository.

This wrapper keeps repo-local skill discovery separate from plugin skill discovery:

- repo-local discovery entrypoint: `.agents/skills/avalonia-codex-plugin/SKILL.md`
- plugin manifest: `../../../.codex-plugin/plugin.json`
- plugin skills: `../../../skills/`
- shared references: `../../../references/`
- routing/evaluation contract: `../../../references/71-skill-routing-and-evaluation.md`

Load the canonical umbrella workflow from:

- `../../../SKILL.md`

Then follow the routing rules from `../../../SKILL.md` instead of copying the full routing table here. The focused plugin skills under `../../../skills/` and the shared references under `../../../references/` remain the actual implementation surface.

Keep default guidance pinned to the local Avalonia 12 source baseline at `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`. Treat Avalonia 11.x material as legacy migration contrast, not as default guidance.

When the request is about this plugin's quality or readiness, run `python3 scripts/validate_plugin_quality.py` from the repository root and inspect `../../../evals/avalonia-12-plugin-prompts.md`.
