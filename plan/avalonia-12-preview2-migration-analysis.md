# Superseded Avalonia 12 Preview2 Migration Analysis

## Status

This analysis is retained as historical context only.

The plugin no longer has a preview2 migration lane as a current route. The default route is the Avalonia 12 source-backed route documented in:

- `references/70-avalonia-12-source-and-reference-baseline.md`
- `references/71-skill-routing-and-evaluation.md`
- `references/72-avalonia-12-skill-quality-audit.md`

Current baseline:

- source tree: `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`
- version signal: `12.1.999`
- current target framework: `net10.0`

## What Was Preserved

The earlier preview analysis established useful migration themes that remain valid as review categories:

- binding and metadata migration risk,
- compiled binding defaults,
- platform-service modernization,
- window and root-host architecture changes,
- Android bootstrap changes,
- larger new control families such as page navigation and command surfaces.

Those themes are now handled through the current migration guide and generated catalogs, not through preview-specific generated artifacts.

## What Must Not Be Reused As Current Guidance

- Do not treat preview2 package versions, preview API indexes, or preview generated catalogs as current guidance or current plugin evidence.
- Do not treat the old Avalonia 11.x default baseline as the plugin default.
- Do not route users to removed preview-specific reference names.

## Current Replacement

Use:

- `references/68-avalonia-12-migration-guide.md`
- `references/69-avalonia-12-breaking-changes-and-new-api-catalog.md`
- `references/api-index-generated.md`

Important API or behavior claims still need direct verification in `frameworks/Avalonia`.
