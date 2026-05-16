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

Primary documentation:

- `references/71-skill-routing-and-evaluation.md`
- `SKILL.md`
- `README.md`
- `AGENTS.md`
- `.agents/skills/avalonia-codex-plugin/SKILL.md`

## Changed File Groups

- Routing and operator docs: `SKILL.md`, `README.md`, `AGENTS.md`, `.agents/skills/avalonia-codex-plugin/SKILL.md`
- Specialist skills: all 19 `skills/*/SKILL.md` files
- References: `references/compendium.md`, `references/71-skill-routing-and-evaluation.md`, `references/72-avalonia-12-skill-quality-audit.md`
- Executable validation: `scripts/validate_plugin_quality.py`
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

Latest result:

```text
OK: source-baseline=12.1.999/net10.0, reference-projects=3-default-avalonia-12, skills=19, plugin-manifest=ok, evals>=8, samples>=5, plan-scope=ok, default-11x-scan-files=502
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
- Fluent theme guidance.

## Verification Commands

```bash
python3 scripts/validate_plugin_quality.py
python3 -m json.tool .codex-plugin/plugin.json
python3 -m unittest scripts.test_generate_api_migration_report scripts.test_find_uncovered_apis
git diff --check
```

Results:

- plugin quality gate: passed,
- plugin JSON validation: passed,
- unit tests: `Ran 15 tests ... OK`,
- diff whitespace check: passed.

The unit test output includes `error: unknown ref: bad-ref`; that string is emitted by an intentional negative test and does not indicate a failing test run.

## Residual Risks

- The quality gate verifies routing and evidence discipline structurally; it does not run the prompts through an actual model evaluator.
- The generated API index remains a parser-based helper. Important API claims still need local source verification.
- Historical `plan/` files may still describe old work, but the quality gate now requires preview2 plan files to be explicitly superseded and tied back to the current Avalonia 12 baseline.
- The plugin still carries broad reference chapters from earlier work. This audit improves their routing and validation surface, but it is not a line-by-line rewrite of every deep reference chapter.
