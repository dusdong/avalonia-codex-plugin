---
name: avalonia-12-migration
description: Plan and execute migration from legacy Avalonia 11.x code to the plugin's default Avalonia 12 source baseline. Use for breaking-change review, source-backed API delta lookup, migration sequencing, and upgrades that should stay grounded in the local Avalonia 12 source tree.
---

# Avalonia 12 Migration

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/68-avalonia-12-migration-guide.md`
- `../../references/69-avalonia-12-breaking-changes-and-new-api-catalog.md`
- `../../references/api-index-generated.md`

Use the default Avalonia 12 skills for current implementation guidance. Use this skill only when the request is about upgrading older Avalonia code.

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Confirm the source app's actual Avalonia version and note whether it is `11.x`, prerelease `12.x`, or another baseline.
2. Read the curated migration guide before touching code so sequencing is correct.
3. Use the breaking-change catalog for impact review and the generated Avalonia 12 index for initial signature lookup.
4. Verify final API guidance against `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.

## Rules

- Keep migration guidance grounded in the local Avalonia 12 source baseline.
- Do not let legacy Avalonia 11.x patterns leak back into default Avalonia 12 skills.
- Separate required break fixes from optional modernizations.
