# Avalonia 12 Skill Routing and Evaluation

This reference turns the plugin from a static knowledge pack into a routable and testable Avalonia 12 workflow.

## Evidence Classes

Every specialist skill must keep these three evidence classes separate:

- **Avalonia 12 source facts**: APIs, target frameworks, package behavior, build behavior, and platform services verified against `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.
- **Avalonia 12 project patterns**: architecture, UI composition, and engineering patterns extracted from the allowed Avalonia 12 projects in `docs/reference/ai-desktop-projects.md`; AI desktop product patterns are normalized in `73-avalonia-12-ai-desktop-product-patterns.md`, with executable recipes and checklists in `74-avalonia-12-ai-desktop-recipes-and-checklists.md`.
- **Avalonia 11.x migration contrast**: legacy behavior or examples used only to explain upgrade risk, compatibility gaps, or anti-patterns.

If a response cannot identify which class supports a recommendation, it should treat the recommendation as provisional and verify it before presenting it as default guidance.

## Skill Lanes

| Lane | Entry | Responsibility | Verification |
| --- | --- | --- | --- |
| `umbrella` | `SKILL.md` | Identify the user intent and route to one narrow specialist skill. | The selected route appears in `SKILL.md` and the specialist skill exists under `skills/`. |
| `app-building` | bootstrap, bindings, styling, controls, layout, platform, testing skills | Build or modify Avalonia 12 apps with source-backed APIs and current `net10.0` assumptions. | Examples compile conceptually against the local Avalonia 12 source baseline; important APIs are source-checked. |
| `migration` | `avalonia-12-migration`, WPF, WinForms, WinUI, HTML/CSS skills | Port older UI stacks or legacy Avalonia code to Avalonia 12. | Legacy APIs are clearly labeled as source-side input or contrast, not default Avalonia 12 guidance. |
| `debugging` | `avalonia-testing-diagnostics-and-performance` plus the active domain skill | Diagnose build, XAML, binding, styling, rendering, platform, or performance failures. | The answer names the likely failure layer and the concrete file/API to inspect. |
| `source-reference` | any specialist skill plus generated references | Confirm uncertain APIs and behaviors against `frameworks/Avalonia`. | Generated indexes are helper artifacts; local source wins on conflict. |
| `ui-patterns` | design-systems, fluent-design, controls, layout skills | Extract design and engineering patterns from allowed Avalonia 12 projects; use `73-avalonia-12-ai-desktop-product-patterns.md` and `74-avalonia-12-ai-desktop-recipes-and-checklists.md` for AI desktop workbench, assistant, plugin, tray, overlay, notification, theme, ViewModel organization, acceptance checks, and product-pattern QA. | The answer names the source project, keeps project patterns separate from source facts, records checklist risks when asked, and avoids copying third-party code. |

## Routing Rules

1. Start with the umbrella lane only long enough to classify the task.
2. Route to the smallest specialist skill that can answer the current request.
3. Load `70-avalonia-12-source-and-reference-baseline.md` before using product references.
4. Use `docs/reference/ai-desktop-projects.md` only for the projects marked as Avalonia 12 default references.
5. Load `73-avalonia-12-ai-desktop-product-patterns.md` and `74-avalonia-12-ai-desktop-recipes-and-checklists.md` when the request asks for AI desktop product architecture, assistant interactions, settings/plugin/MCP surfaces, tray/floating entry, overlays, notifications, clipboard utility flows, eval recording, or product-pattern review.
6. Escalate to source-reference when the request depends on API existence, signature shape, package version, target framework, or platform behavior.
7. Escalate to migration only when the user supplies legacy Avalonia 11.x, WPF, WinForms, WinUI, or HTML/CSS source context.

## Evaluation Contract

The plugin passes the local quality gate when:

- all specialist skills include the Avalonia 12 baseline reference,
- all specialist skills include the three evidence classes,
- the root umbrella skill routes every specialist skill,
- `plugin.json` remains valid and Avalonia 12 explicit,
- evaluation prompts cover app-building, migration, debugging, source-reference, and UI-patterns,
- real task samples show expected outputs without copying third-party project code,
- the AI desktop product-pattern library exists, includes `mnemo`, `Netor.Cartana`, and `ClippyAI`, covers the required pattern sections, and is routed by relevant specialist skills,
- the AI desktop recipe/checklist layer exists, covers the required product surfaces, and can be checked with `python3 scripts/run_ai_desktop_eval_checklist.py --check`,
- no forbidden default Avalonia 11.x marker is present outside explicit migration or exclusion context.

Run:

```bash
python3 scripts/validate_plugin_quality.py
```

Use this gate before publishing plugin changes or declaring the plugin ready for another migration/reference refresh.
