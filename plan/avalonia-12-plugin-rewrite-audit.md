# Avalonia 12 Plugin Rewrite Audit

Date: 2026-05-16

## Goal

Rewrite this plugin so its default guidance targets Avalonia 12, using the local source baseline at:

`/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`

Current source evidence:

- Git commit: `837e1aa91dd34bbd9e4d4c932a18878be2a4d753`
- Version: `12.1.999`
- Current target framework: `net10.0`

## Completed Changes

### A. Avalonia 12 Source Baseline

- Added `references/70-avalonia-12-source-and-reference-baseline.md`.
- Declared the local Avalonia source tree as the final authority for APIs, platform services, controls, styles, diagnostics, tests, and build behavior.
- Updated `AGENTS.md`, `README.md`, `SKILL.md`, and `references/compendium.md` to route default guidance through the local Avalonia 12 baseline.

### B. Avalonia 12 Product References

- Rewrote `/Volumes/程序开发/Du-Framework/Du.Ingest/docs/reference/ai-desktop-projects.md` as an Avalonia 12-only evidence report.
- Default references are now limited to:
  - `mnemo`: Avalonia `12.0.2`, `net10.0`
  - `Netor.Cartana`: Avalonia `12.0.1`, `net10.0`
  - `ClippyAI`: Avalonia `12.0.2` / `12.0.1`, `net10.0`
- Excluded from default guidance:
  - `Everywhere`: Avalonia `11.3.12`
  - `StabilityMatrix`: Avalonia `11.3.7`
  - `avallama`: Avalonia `11.3.9`
  - `WhisperVoiceInput`: Avalonia `11.2.4`

### C. Plugin Entry Points

- Updated `.codex-plugin/plugin.json` to describe Avalonia 12 app build, port, and review workflows.
- Updated `.agents/skills/development-plugin-for-avalonia/SKILL.md` and its `agents/openai.yaml` to route broad Avalonia 12 work.
- Updated root `SKILL.md` so Avalonia 12 is the default and legacy migration is a separate path.

### D. Specialist Skills

- Added `references/70-avalonia-12-source-and-reference-baseline.md` to every `skills/*/SKILL.md` start list.
- Updated all `skills/*/agents/openai.yaml` display and default prompt text to expose Avalonia 12-specific workflows.
- Kept `skills/avalonia-12-migration` as the legacy Avalonia 11.x-to-12 migration lane.

### E. References and Generated Artifacts

- Regenerated `references/api-index-generated.md` from the local Avalonia source baseline:
  - Files scanned: `2666`
  - Public signatures captured: `11303`
- Regenerated `references/69-avalonia-12-breaking-changes-and-new-api-catalog.md`:
  - From ref: `11.3.12`
  - To ref: `HEAD`
  - Approved compatibility suppressions: `2`
  - Added public signatures: `1243`
  - Removed public signatures in parser view: `885`
- Regenerated `references/controls/*`:
  - Controls documented: `144`
  - New Avalonia 12 control references include `CommandBar`, `Page`, `NavigationPage`, `DrawerPage`, `PipsPager`, and related page/navigation controls.
- Removed stale `references/api-index-12.0.0-rc1-generated.md` from the default reference set.
- Updated high-risk default references so old `11.3.12` statements are either removed or explicitly framed as legacy migration contrast.

## Verification

Commands run:

```bash
git -C /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia rev-parse HEAD
sed -n '1,30p' /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia/build/SharedVersion.props
sed -n '1,25p' /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia/build/TargetFrameworks.props

python3 scripts/generate_api_index.py \
  --repo /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia \
  --git-ref HEAD \
  --output references/api-index-generated.md \
  --max-per-file 100000

python3 scripts/generate_api_migration_report.py \
  --repo /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia \
  --from-ref 11.3.12 \
  --to-ref HEAD \
  --output references/69-avalonia-12-breaking-changes-and-new-api-catalog.md

python3 scripts/generate_control_reference_docs.py \
  --repo /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia \
  --git-ref HEAD \
  --output-dir references/controls

python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
python3 -m unittest scripts.test_generate_api_migration_report scripts.test_find_uncovered_apis
python3 -m json.tool .codex-plugin/plugin.json
git diff --check

rg -n 'api-index-12\.0\.0-rc1|Repository: `Avalonia@11\.3\.12`|Avalonia git ref: `11\.3\.12`|default guidance pinned to Avalonia `11\.3\.12`|default 11|stable lane' .
```

Observed results:

- Avalonia source commit: `837e1aa91dd34bbd9e4d4c932a18878be2a4d753`
- Avalonia source version: `12.1.999`
- Avalonia current target framework: `net10.0`
- API coverage scan: `10345` parsed signatures, `5746` covered, `4599` not covered
- Unit tests: `15` tests passed
- Plugin JSON: valid
- Diff check: clean
- Default 11.x/stale rc search: no default guidance hits; remaining `11.x` mentions are legacy migration, exclusion evidence, or migration command inputs

## Remaining Boundary

This audit does not claim every deep reference chapter has been manually re-authored line-by-line. The rewrite makes the plugin default path Avalonia 12-specific by:

- forcing every skill through the Avalonia 12 baseline reference,
- replacing stale generated API and controls data,
- removing stale rc API index routing,
- converting default entry points and high-risk references away from `11.3.12`,
- retaining legacy version references only in migration or exclusion contexts.
