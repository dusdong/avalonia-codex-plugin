# AGENTS.md

## Purpose

This repository defines and maintains the `avalonia-codex-plugin` plugin, its repo-local wrapper skill, its repo marketplace metadata, and its focused Avalonia skills.

Primary goals:
- keep guidance accurate to the pinned Avalonia 12 source baseline,
- split broad Avalonia guidance into granular, reusable skills,
- keep app-development references shared instead of duplicated across skills,
- maintain clear navigation across `.agents/skills/avalonia-codex-plugin/SKILL.md`, `SKILL.md`, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, `skills/*/SKILL.md`, `README.md`, and `references/`.

## Source of Truth

Use these files in this order:
1. `.agents/skills/avalonia-codex-plugin/SKILL.md` (repo-local discovery entrypoint)
2. `SKILL.md` (canonical umbrella routing workflow and default behavior)
3. `.codex-plugin/plugin.json` (plugin package metadata, branding, and bundled component paths)
4. `.agents/plugins/marketplace.json` (repo marketplace metadata and local install path)
5. `skills/*/SKILL.md` (focused workflows for the active lane)
6. `references/compendium.md` (reference index and task navigation)
7. `references/00-api-map.md` (curated app-facing API map)
8. `references/70-avalonia-12-source-and-reference-baseline.md` (Avalonia 12 source and product-reference baseline)
9. `references/api-index-generated.md` (broad signature lookup regenerated from the local Avalonia 12 source tree)

If they conflict, align all skills and docs to the Avalonia 12 baseline and update the conflicting files.

## Version Pinning

- Target Avalonia version line: Avalonia 12.
- Source baseline: `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.
- Current source signal: `build/SharedVersion.props` reports `12.1.999`; `build/TargetFrameworks.props` reports `net10.0`.
- Default guidance may use the local Avalonia `master` source baseline, but any source-backed claim must cite or name the relevant source path.
- Keep version statements in top-level docs (`README.md`, `SKILL.md`) and `references/70-avalonia-12-source-and-reference-baseline.md`, not repeated everywhere.

Regenerate API index from the local source baseline when signature lookup needs to become authoritative:

```bash
python3 scripts/generate_api_index.py \
  --repo /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia \
  --git-ref HEAD \
  --output references/api-index-generated.md \
  --max-per-file 100000
```

After regeneration, `references/api-index-generated.md` is the default local-source signature index. Still verify important guidance against the source tree before presenting it as authoritative.

## Skill Authoring Rules

- Repo-local skill entrypoints live under `.agents/skills/<skill-name>/`.
- Repo marketplace metadata lives under `.agents/plugins/marketplace.json`.
- Specialist skills live under `skills/<skill-name>/`.
- Keep skill names lower-case hyphen-case.
- Each discovered skill entrypoint should have:
  - `SKILL.md`
  - `agents/openai.yaml`
- Keep the repo-local wrapper thin and route into the canonical umbrella workflow or focused plugin skills.
- Keep `SKILL.md` bodies short and route to shared references instead of copying large content into each skill.
- Put trigger conditions in frontmatter descriptions, not in long body sections.
- Keep the repo marketplace `name` distinct from the plugin `name` so catalog and cache identity stay stable, even if the visible marketplace `displayName` intentionally matches the plugin brand.
- If the repo root itself is the plugin root, keep the marketplace `source.path` at `./` and document that choice in `README.md`.
- When adding, renaming, or removing a skill, update all relevant navigation points:
  - `.agents/skills/avalonia-codex-plugin/SKILL.md`
  - `SKILL.md`
  - `.codex-plugin/plugin.json` if bundle paths or install-surface metadata change
  - `.agents/plugins/marketplace.json` if the plugin path or marketplace presentation changes
  - `README.md`
  - any other skill that routes to it

## Reference Authoring Rules

- Reference docs live under the `references/` folder using `NN-topic-name` filename patterns.
- Keep numbering and filenames stable and sequential.
- When adding or renaming a reference, update all relevant navigation:
  - `references/compendium.md`
  - any specialist skill that links to that reference
  - `README.md` when the lane is part of the published catalog
- Prefer relative paths in docs and examples inside this repo.
- Keep content app-development-focused; avoid low-value API tail coverage unless needed for practical usage.

## Reference Content Standard

Each new or expanded reference should include:
- clear scope and primary APIs,
- realistic XAML and/or C# examples,
- AOT/trimming notes where relevant,
- practical do/don't guidance,
- troubleshooting or edge-case notes for common mistakes.

Default guidance bias:
- compiled bindings + `x:DataType`,
- XAML-first patterns unless the user requests code-only,
- explicit UI-thread and dispatcher behavior for async/reactive flows.

## API Coverage Workflow

Use coverage tooling after significant reference updates.

1. Recompute gaps:

```bash
python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
```

2. Run parser tests:

```bash
python3 -m unittest scripts.test_find_uncovered_apis
```

3. Refresh planning/report docs as needed:
- `plan/api-coverage-detailed-report.md`
- `plan/api-coverage-reference-update-plan.md`

Coverage target is practical completeness for app development, not 100% signature parity.

## Change Review Checklist

Before finalizing changes:
1. Verify repo-local, root, and specialist skill routing still matches the current skill catalog.
2. Verify plugin manifest paths, branding assets, and legal links still resolve from `.codex-plugin/plugin.json`.
3. Verify repo marketplace metadata still points at the intended plugin root and uses a marketplace identity distinct from the plugin identity.
4. Verify new or renamed skills are reflected in `README.md` and any routing skill that mentions them.
5. Verify examples use APIs available in the local Avalonia 12 source baseline, or explicitly label them as legacy migration contrast.
6. Re-run coverage tooling when API-focused references changed.
7. Ensure no accidental drift back to Avalonia 11.x as the default guidance.

## Commits

- Keep commits granular and topic-based (one logical change set per commit).
- Avoid mixing script changes, coverage artifacts, and large doc rewrites in a single commit when separable.
