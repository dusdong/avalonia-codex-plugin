# Superseded Avalonia 12 Preview2 Migration Reference Update Plan

## Status

This file is retained as historical planning context only.

It is superseded by the current Avalonia 12 source baseline:

- source tree: `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`
- version signal: `12.1.999`
- current target framework: `net10.0`
- default generated API index: `references/api-index-generated.md`
- default breaking/new API catalog: `references/69-avalonia-12-breaking-changes-and-new-api-catalog.md`

Do not use the old preview2 lane as current guidance for default implementation, migration, or package-version decisions.

## Historical Purpose

The original plan created a dedicated migration lane for an early Avalonia 12 preview while the repository still had an Avalonia 11.x default baseline. That work is no longer the plugin's current operating model.

Historical artifacts from that lane may still be useful only as migration archaeology when explaining how the plugin evolved from Avalonia 11.x and early Avalonia 12 preview assumptions toward the current source-backed Avalonia 12 baseline.

## Current Replacement

Use these files instead:

- `README.md`
- `SKILL.md`
- `AGENTS.md`
- `references/70-avalonia-12-source-and-reference-baseline.md`
- `references/71-skill-routing-and-evaluation.md`
- `references/72-avalonia-12-skill-quality-audit.md`
- `evals/avalonia-12-plugin-prompts.md`
- `examples/avalonia-12-task-samples.md`

## Boundary

- Avalonia 12 source facts must come from `frameworks/Avalonia`.
- Default product patterns must come only from `mnemo`, `Netor.Cartana`, and `ClippyAI` as recorded in `docs/reference/ai-desktop-projects.md`.
- Avalonia 11.x and early preview material may appear only as explicitly labeled migration contrast.
