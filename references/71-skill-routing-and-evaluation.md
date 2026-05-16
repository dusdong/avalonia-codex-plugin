# Avalonia 12 Skill Routing and Evaluation

This reference turns the plugin from a static knowledge pack into a routable and testable Avalonia 12 workflow.

## Evidence Classes

Every specialist skill must keep these three evidence classes separate:

- **Avalonia 12 source facts**: APIs, target frameworks, package behavior, build behavior, and platform services verified against `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.
- **Avalonia 12 project patterns**: architecture, UI composition, and engineering patterns extracted from the allowed Avalonia 12 projects in `docs/reference/ai-desktop-projects.md`.
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
| `ui-patterns` | design-systems, fluent-design, controls, layout skills | Extract design and engineering patterns from allowed Avalonia 12 projects. | The answer names the source project and avoids copying third-party code. |

## Routing Rules

1. Start with the umbrella lane only long enough to classify the task.
2. Route to the smallest specialist skill that can answer the current request.
3. Load `70-avalonia-12-source-and-reference-baseline.md` before using product references.
4. Use `docs/reference/ai-desktop-projects.md` only for the projects marked as Avalonia 12 default references.
5. Escalate to source-reference when the request depends on API existence, signature shape, package version, target framework, or platform behavior.
6. Escalate to migration only when the user supplies legacy Avalonia 11.x, WPF, WinForms, WinUI, or HTML/CSS source context.

## Evaluation Contract

The plugin passes the local quality gate when:

- all specialist skills include the Avalonia 12 baseline reference,
- all specialist skills include the three evidence classes,
- the root umbrella skill routes every specialist skill,
- `plugin.json` remains valid and Avalonia 12 explicit,
- evaluation prompts cover app-building, migration, debugging, source-reference, and UI-patterns,
- real task samples show expected outputs without copying third-party project code,
- no forbidden default Avalonia 11.x marker is present outside explicit migration or exclusion context.

Run:

```bash
python3 scripts/validate_plugin_quality.py
```

Use this gate before publishing plugin changes or declaring the plugin ready for another migration/reference refresh.
