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

## Systematic Reclose

Date: 2026-05-16

### Scope

This reclose covers the plugin as an Avalonia 12 focused Codex plugin across:

- `README.md`, `AGENTS.md`, `SKILL.md`
- `.codex-plugin/plugin.json`
- `.agents/*`
- `skills/*`
- `references/*`
- `evals/*`
- `examples/*`
- `scripts/*`
- `plan/*`

Required evidence boundaries:

- Avalonia 12 source facts come from `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.
- Current source signals are `12.1.999` and `net10.0`.
- Default Avalonia 12 product references are limited to `mnemo`, `Netor.Cartana`, and `ClippyAI` as recorded in `docs/reference/ai-desktop-projects.md`.
- Avalonia 11.x and early Avalonia 12 preview material is migration contrast only.

### Findings

- The current plugin entrypoints already route through the Avalonia 12 baseline and the three evidence classes.
- All 19 specialist skills include the Avalonia 12 source baseline reference and evidence discipline markers.
- The plugin manifest is Avalonia 12 explicit and points at `./skills/`.
- The existing quality gate passed before this reclose, but it did not verify the semantic status of `plan/*`.
- Two old preview2 planning files were still framed as completed preview-lane work and could be mistaken for current planning material.
- The migration guide contained one package example that still used a historical release-candidate package version in an "After" block.

### Changes

- Reframed the two preview2 plan files as explicitly superseded historical context.
- Updated the migration guide example so Avalonia package guidance stays aligned with the application's Avalonia 12 package line instead of copying a historical release-candidate version.
- Extended `scripts/validate_plugin_quality.py` with a plan-scope check so superseded plan files and this reclose report are part of the executable quality gate.

### Verification

Commands to run before declaring this reclose complete:

```bash
python3 scripts/validate_plugin_quality.py
python3 -m json.tool .codex-plugin/plugin.json
python3 -m unittest scripts.test_generate_api_migration_report scripts.test_find_uncovered_apis
git diff --check
```

Expected outcome:

- quality gate includes `plan-scope=ok`,
- plugin manifest parses as JSON,
- migration and coverage helper tests pass,
- whitespace check is clean.

### Residual Risks

- The generated API index is parser-based and remains a lookup helper; important API claims still require direct verification in `frameworks/Avalonia`.
- The quality gate verifies structural evidence discipline, not actual model behavior on the eval prompts.
- Deep reference chapters are broad; this reclose fixes routing, boundary, and plan drift, but it is not a line-by-line rewrite of every reference page.
- Default product-pattern extraction is still document-governed; copying third-party code is prohibited but not automatically diff-detected.

## AI Desktop Pattern Reclose

Date: 2026-05-16

### Scope

This reclose covers systematic extraction of Avalonia 12 AI desktop product experience from the allowed default references in `/Volumes/程序开发/Du-Framework/Du.Ingest/docs/reference/ai-desktop-projects.md`:

- `mnemo`
- `Netor.Cartana`
- `ClippyAI`

The extracted experience is pattern evidence only. Avalonia API, XAML, platform-service, resource, and control claims still resolve back to `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia` at `12.1.999 / net10.0`.

### Findings

- `mnemo` provides the strongest pattern evidence for a full AI workbench: shell composition, left navigation, central workspace, right assistant, overlay host, toast history, and theme resource layering.
- `Netor.Cartana` provides the strongest pattern evidence for Chinese assistant UX, drawer panels, settings center information architecture, floating entry, bubble status, plugin lifecycle, and MCP configuration.
- `ClippyAI` provides local utility evidence for tray-first visibility, transparent topmost small windows, clipboard task flows, configuration dialogs, and cross-platform notification wrapping.
- `Everywhere`, `StabilityMatrix`, `avallama`, and `WhisperVoiceInput` remain excluded from default guidance because their Avalonia versions are 11.x.

### Changes

- Added `references/73-avalonia-12-ai-desktop-product-patterns.md` with sections for workbench architecture, AI assistant interaction, plugins/settings, tray/floating entry, overlays/notifications, theme tokens, View/ViewModel organization, platform service isolation, transferable anti-patterns, source verification points, and no-copy rules.
- Routed the new experience library through `README.md`, `SKILL.md`, `references/compendium.md`, `references/70-avalonia-12-source-and-reference-baseline.md`, and `references/71-skill-routing-and-evaluation.md`.
- Connected AI desktop product-pattern routing to `avalonia-design-systems`, `avalonia-controls-and-windowing`, `avalonia-views-and-templating`, `avalonia-platform-services`, `avalonia-styling-and-resources`, and `avalonia-testing-diagnostics-and-performance`.
- Extended `evals/avalonia-12-plugin-prompts.md` and `examples/avalonia-12-task-samples.md` with workbench, tray utility, plugin/MCP, overlay, notification, and no-copy scenarios.
- Extended `scripts/validate_plugin_quality.py` with `ai-desktop-patterns=ok` checks for source coverage, required sections, excluded 11.x references, no-copy constraints, routing, evals, and examples.

### Verification

Latest command result:

```text
python3 scripts/validate_plugin_quality.py
OK: source-baseline=12.1.999/net10.0, reference-projects=3-default-avalonia-12, skills=19, plugin-manifest=ok, evals>=8, samples>=5, ai-desktop-patterns=ok, plan-scope=ok, default-11x-scan-files=503
```

### Residual Risks

- The pattern library captures representative source files and architecture signals; it is not a full code audit of every line in the three projects.
- The quality gate verifies structure and routing, not actual model responses on live eval execution.
- Third-party code copying is explicitly prohibited and structurally documented, but automated copy-detection is still outside this plugin gate.

## AI Desktop Deepening Reclose

Date: 2026-05-16

### Scope

This reclose deepens the AI desktop pattern library into executable evaluation, reusable acceptance checklists, and finer recipes while preserving the original evidence boundary:

- `mnemo`, `Netor.Cartana`, and `ClippyAI` are the only default Avalonia 12 project-pattern references.
- `Everywhere`, `StabilityMatrix`, `avallama`, and `WhisperVoiceInput` remain Avalonia 11.x migration contrast only.
- Avalonia API, XAML, platform-service, control, and resource claims still resolve back to `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia` at `12.1.999 / net10.0`.
- Third-party code, resources, plugin protocols, prompt text, visual constants, and implementation bodies remain prohibited copying sources.

### Changes

- Added `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md` with recipes and acceptance checklists for workspace navigation, right assistant, plugin/MCP settings, tray/floating windows, overlay/toast, system notifications, clipboard utility flow, and settings center.
- Added `evals/avalonia-12-ai-desktop-eval-checklist.md` so AI desktop evals can record expected route, actual route, evidence classes, no-copy result, Avalonia source verification, and notes.
- Added `scripts/run_ai_desktop_eval_checklist.py` with `--check` and `--json` modes to validate or emit the checklist structure.
- Updated `README.md`, `SKILL.md`, `references/70-avalonia-12-source-and-reference-baseline.md`, `references/71-skill-routing-and-evaluation.md`, `references/73-avalonia-12-ai-desktop-product-patterns.md`, `references/compendium.md`, six AI desktop-related specialist skills, `evals/avalonia-12-plugin-prompts.md`, and `examples/avalonia-12-task-samples.md` to route the new recipes and checklist layer.
- Extended `scripts/validate_plugin_quality.py` with `ai-desktop-deepening=ok` and `copy-risk-scan-files=5`.

### Verification

Latest command result:

```text
python3 scripts/run_ai_desktop_eval_checklist.py --check
OK: ai-desktop-eval-checklist=ok

python3 scripts/validate_plugin_quality.py
OK: source-baseline=12.1.999/net10.0, reference-projects=3-default-avalonia-12, skills=19, plugin-manifest=ok, evals>=8, samples>=5, ai-desktop-patterns=ok, ai-desktop-deepening=ok, copy-risk-scan-files=5, plan-scope=ok, default-11x-scan-files=505
```

### Residual Risks

- The eval checklist records actual route and evidence quality, but it does not automatically run the installed plugin against a model; that remains a manual or harness-driven step.
- The copy-risk scan catches obvious pasted XAML/C# body markers only; it is not full plagiarism detection.
- The recipes are acceptance-level guidance, not generated implementation code.

## AI Desktop Reference Sync Reclose

Date: 2026-05-16

### Scope

This reclose syncs the plugin after pulling updated `third_party/ai_desktop_refs/mnemo` and `third_party/ai_desktop_refs/Netor.Cartana` references:

- `mnemo`: `359451d72c6ccb9b28afa131471ff7b41c54c4e3` -> `5e78976ee6514f7b61287a8232ff796754276892`
- `Netor.Cartana`: `ac32533f8ddf414581c3c2362cc3375dcad48e2a` -> `490c61d4379eb78a77e30d7f2d3e9887084a67b7`

### Findings

- `mnemo` added project-pattern evidence for `AiAssistantToolHost`, chat `ItemsRepeater` virtualization, `PerfDiagnosticsService`, `PerfDiagnosticsScope`, and `PerfDiagnosticsOverlay`.
- `Netor.Cartana` moved plugin docs under `Plugins/docs/参考文档/` and added project-pattern evidence for design tokens, shared styles, empty state, realtime process cards, workspace task views, HITL approval, workflow executor/checkpoint layers, and PluginBus event transport.

### Changes

- Updated `/Volumes/程序开发/Du-Framework/Du.Ingest/docs/reference/ai-desktop-projects.md` with current commits, package evidence, key files, and new pattern summaries.
- Updated `references/73-avalonia-12-ai-desktop-product-patterns.md` and `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md` with diagnostics/performance, AI tool gating, chat virtualization, design token, realtime process, PluginBus, workflow, and HITL workspace patterns.
- Updated `evals/avalonia-12-plugin-prompts.md`, `evals/avalonia-12-ai-desktop-eval-checklist.md`, `examples/avalonia-12-task-samples.md`, `scripts/run_ai_desktop_eval_checklist.py`, and `scripts/validate_plugin_quality.py` so the new patterns are routable and structurally gated.

### Verification

Commands to run:

```bash
python3 scripts/run_ai_desktop_eval_checklist.py --check
python3 scripts/validate_plugin_quality.py
python3 -m json.tool .codex-plugin/plugin.json
python3 -m unittest scripts.test_generate_api_migration_report scripts.test_find_uncovered_apis
git diff --check
```

### Residual Risks

- The sync updates plugin evidence and recipes, not the third-party implementations themselves.
- New `Netor.Cartana` workflow/PluginBus patterns are large and still treated as pattern evidence only; no protocol fields or implementation bodies should be copied.
- `mnemo` diagnostics patterns are useful for developer tooling, but production telemetry/privacy policy remains target-application specific.
