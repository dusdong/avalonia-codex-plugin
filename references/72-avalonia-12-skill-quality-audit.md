# Avalonia 12 Skill Quality Audit

Date: 2026-05-16

## Goal

Move `frameworks/avalonia-codex-plugin` from an Avalonia 12 knowledge plugin into an executable, verifiable, and evaluable Avalonia 12 Codex plugin.

## Source Baseline

- Avalonia source repository: `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`
- Source commit during this audit: `837e1aa91dd34bbd9e4d4c932a18878be2a4d753`
- Version signal: `build/SharedVersion.props` -> `12.1.999`
- Target framework signal: `build/TargetFrameworks.props` -> `net10.0`

## Reference Project Boundary

Default product references remain limited to the Avalonia 12 projects recorded in `/Volumes/程序开发/Du-Framework/Du.Ingest/docs/reference/ai-desktop-projects.md`:

- `mnemo`
- `Netor.Cartana`
- `ClippyAI`

Avalonia 11.x projects remain migration contrast, exclusion evidence, or product-form inspiration only. They are not default API, XAML, styling, or architecture authorities for this plugin.

## Added Capability Layer

The plugin now has an explicit capability model:

- `umbrella`: classify intent and route to the narrowest specialist skill.
- `app-building`: create or modify Avalonia 12 apps with source-backed APIs.
- `migration`: port legacy Avalonia, WPF, WinForms, WinUI, or HTML/CSS inputs to Avalonia 12.
- `debugging`: diagnose build, XAML, binding, styling, rendering, platform, and performance failures.
- `source-reference`: verify uncertain API and behavior claims against `frameworks/Avalonia`.
- `ui-patterns`: extract architecture and UI patterns from allowed Avalonia 12 projects without copying code.

The AI desktop product-pattern layer is now explicit in `references/73-avalonia-12-ai-desktop-product-patterns.md`. It extracts reusable patterns from `mnemo`, `Netor.Cartana`, and `ClippyAI` while keeping Avalonia 12 source facts, project patterns, and Avalonia 11.x migration contrast separate.

The AI desktop execution layer is now explicit in `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`, `evals/avalonia-12-ai-desktop-eval-checklist.md`, and `scripts/run_ai_desktop_eval_checklist.py`. It turns the pattern library into recipes, acceptance checklists, eval result recording fields, and a local checklist validator.

Primary documentation:

- `references/71-skill-routing-and-evaluation.md`
- `references/73-avalonia-12-ai-desktop-product-patterns.md`
- `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`
- `evals/avalonia-12-ai-desktop-eval-checklist.md`
- `SKILL.md`
- `README.md`
- `AGENTS.md`
- `.agents/skills/avalonia-codex-plugin/SKILL.md`

## Changed File Groups

- Routing and operator docs: `SKILL.md`, `README.md`, `AGENTS.md`, `.agents/skills/avalonia-codex-plugin/SKILL.md`
- Specialist skills: all 19 `skills/*/SKILL.md` files
- References: `references/compendium.md`, `references/71-skill-routing-and-evaluation.md`, `references/72-avalonia-12-skill-quality-audit.md`
- AI desktop product patterns: `references/73-avalonia-12-ai-desktop-product-patterns.md`
- AI desktop recipes and eval checklist: `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`, `evals/avalonia-12-ai-desktop-eval-checklist.md`
- Executable validation: `scripts/validate_plugin_quality.py`
- Eval checklist runner: `scripts/run_ai_desktop_eval_checklist.py`
- Evaluation assets: `evals/avalonia-12-plugin-prompts.md`, `examples/avalonia-12-task-samples.md`

## Skill Evidence Discipline

All 19 specialist skills now include the same evidence discipline section:

- Avalonia 12 source facts
- Avalonia 12 project patterns
- Avalonia 11.x migration contrast

This gives each skill a shared rule for separating source-backed facts, allowed product-reference patterns, and legacy comparison material.

## Executable Quality Gate

Added:

- `scripts/validate_plugin_quality.py`

The gate checks:

- local Avalonia source baseline is `12.1.999 / net10.0`,
- the allowed Avalonia 12 reference-project evidence is present,
- the expected 19 specialist skills exist,
- every specialist skill references the Avalonia 12 baseline,
- every specialist skill contains the three evidence classes,
- every `agents/openai.yaml` remains Avalonia 12 explicit,
- root `SKILL.md` routes every specialist skill,
- `.codex-plugin/plugin.json` is valid and Avalonia 12 explicit,
- evaluation prompts and real task samples exist,
- default 11.x drift markers are absent from plugin guidance/config files outside explicitly superseded historical planning context.
- `plan/*` preview2 files are explicitly marked superseded and the tracked reclose report is present.
- AI desktop pattern evidence exists, includes all three allowed Avalonia 12 projects, covers required product-pattern sections, excludes Avalonia 11.x projects from default guidance, and routes through README, SKILL, compendium, baseline, routing docs, six specialist skills, evals, and examples.
- AI desktop recipes/checklists exist, cover workspace navigation, right assistant, plugin/MCP, tray, floating window, overlay, toast, notification, clipboard utility, and settings center surfaces.
- The AI desktop eval checklist can be validated with `python3 scripts/run_ai_desktop_eval_checklist.py --check`.
- A text-level copy-risk scan checks the AI desktop reference/eval/sample assets for obvious third-party XAML/C# body patterns.

Latest result:

```text
OK: source-baseline=12.1.999/net10.0, reference-projects=3-default-avalonia-12, skills=19, plugin-manifest=ok, evals>=8, samples>=5, ai-desktop-patterns=ok, ai-desktop-deepening=ok, copy-risk-scan-files=5, plan-scope=ok, default-11x-scan-files=505
```

## Evaluation Assets

Added:

- `evals/avalonia-12-plugin-prompts.md`
- `examples/avalonia-12-task-samples.md`

Coverage:

- new app bootstrap,
- binding failure diagnosis,
- command bar / dense AI desktop UI,
- WPF migration,
- Avalonia 11.x migration,
- source-level API uncertainty,
- product-reference filtering,
- performance review,
- HTML/CSS conversion,
- Fluent theme guidance,
- AI desktop workbench pattern extraction,
- tray-first utility and plugin/MCP settings review,
- overlay/notification acceptance review,
- plugin/MCP settings acceptance review,
- diagnostics/HITL workspace review,
- checklist-based eval result recording,
- reference-sync sample for updated `mnemo` / `Netor.Cartana` submodule evidence.

## Verification Commands

```bash
python3 scripts/validate_plugin_quality.py
python3 scripts/run_ai_desktop_eval_checklist.py --check
python3 -m json.tool .codex-plugin/plugin.json
python3 -m unittest scripts.test_generate_api_migration_report scripts.test_find_uncovered_apis
git diff --check
```

Results:

- plugin quality gate: passed,
- AI desktop eval checklist runner: passed,
- plugin JSON validation: passed,
- unit tests: `Ran 15 tests ... OK`,
- diff whitespace check: passed.

The unit test output includes `error: unknown ref: bad-ref`; that string is emitted by an intentional negative test and does not indicate a failing test run.

## Residual Risks

- The quality gate verifies routing and evidence discipline structurally; it does not run the prompts through an actual model evaluator.
- The generated API index remains a parser-based helper. Important API claims still need local source verification.
- Historical `plan/` files may still describe old work, but the quality gate now requires preview2 plan files to be explicitly superseded and tied back to the current Avalonia 12 baseline.
- The plugin still carries broad reference chapters from earlier work. This audit improves their routing and validation surface, but it is not a line-by-line rewrite of every deep reference chapter.
- The AI desktop pattern library is evidence-based and structurally gated, but it is not a license to copy third-party source; implementations must redesign against the target product and verify APIs against the local Avalonia 12 source tree.
- The copy-risk scan is intentionally lightweight. It catches obvious pasted XAML/C# body markers, not semantic plagiarism or externally generated near-duplicates.

## Reference Sync: mnemo and Netor.Cartana

Date: 2026-05-16

Latest synchronized evidence:

- `mnemo`: `5e78976ee6514f7b61287a8232ff796754276892`, `v0.6.3-5-g5e78976`
- `Netor.Cartana`: `490c61d4379eb78a77e30d7f2d3e9887084a67b7`, `v1.3.7-22-g490c61d`

Synchronized pattern additions:

- `mnemo`: AI tool gating through `AiAssistantToolHost`, chat virtualization through `Avalonia.Controls.ItemsRepeater`, and developer performance diagnostics through `PerfDiagnosticsService` / `PerfDiagnosticsOverlay`.
- `Netor.Cartana`: `DesignTokens.axaml`, `SharedStyles.axaml`, `EmptyState`, `RealtimeProcessCard`, workspace/HITL ViewModels, workflow executor patterns, and PluginBus/WebSocket consolidation.

Path correction:

- Plugin/MCP docs moved from `Plugins/docs/plugin-mcp.md` and `Plugins/docs/native-plugin-dev-guide.md` to `Plugins/docs/参考文档/plugin-mcp.md` and `Plugins/docs/参考文档/native-plugin-dev-guide.md`.

The synchronized material remains Avalonia 12 project-pattern evidence only. API correctness still comes from `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.
