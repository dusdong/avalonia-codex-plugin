---
name: development-plugin-for-avalonia
description: Umbrella skill for building, reviewing, designing, porting, and migrating Avalonia 12 applications with modern XAML/C# patterns. Use when the request is broad Avalonia 12 work or when another specialist skill has not yet been selected; route quickly to focused skills for startup, bindings, styling, controls, layout, rendering, testing, design systems, or HTML/WinForms/WPF/WinUI/legacy Avalonia migration work.
---

# Development Plugin for Avalonia

Use this as the canonical umbrella workflow source for broad Avalonia work in this repository.

Discovery entrypoints:

- repo-local skill: `.agents/skills/development-plugin-for-avalonia/SKILL.md`
- plugin discovery: focused skills under `skills/` via `.codex-plugin/plugin.json`

Do not treat this root file as the repo-local discovery entrypoint. Keep it as the canonical routing workflow that the repo-local wrapper can load without duplicating the full guidance.

Resolve the task category, load the smallest specialist skill that fits, and keep the shared references as the single source of truth.

Primary shared indexes:

- `references/compendium.md`
- `references/70-avalonia-12-source-and-reference-baseline.md`
- `references/00-api-map.md`
- `references/api-index-generated.md` as broad signature lookup regenerated from the local Avalonia 12 source tree.

## Default Working Rules

- Keep default implementation guidance pinned to the local Avalonia 12 source baseline at `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.
- Treat `references/68-avalonia-12-migration-guide.md` as a legacy-app migration aid, not as the default Avalonia 12 guidance source.
- Use only the Avalonia 12 projects listed in `references/70-avalonia-12-source-and-reference-baseline.md` as default product references.
- Prefer XAML-first examples unless the user explicitly asks for code-only UI construction.
- Prefer compiled bindings with `x:DataType`.
- Keep UI-thread work explicit and keep AOT/trimming tradeoffs visible.

## Routing Rules

Route to the first specialist skill that matches the request and do not keep broad orchestration in scope longer than needed.

- Startup, `AppBuilder`, platform entrypoints, lifetimes, build configuration:
  `skills/avalonia-bootstrap-and-lifetime/SKILL.md`
- Compiled bindings, runtime XAML, converters, dynamic resources, AOT-safe markup:
  `skills/avalonia-bindings-and-xaml/SKILL.md`
- Reactive flows, dispatcher usage, timers, UI-thread correctness:
  `skills/avalonia-threading-and-dispatcher/SKILL.md`
- Styles, themes, resources, property system, asset packaging:
  `skills/avalonia-styling-and-resources/SKILL.md`
- View location, templates, templated parents, tree traversal:
  `skills/avalonia-views-and-templating/SKILL.md`
- Input, commands, focus, gestures, drag/drop, text editing:
  `skills/avalonia-input-and-commands/SKILL.md`
- Controls, popups, menus, windows, tray, notifications:
  `skills/avalonia-controls-and-windowing/SKILL.md`
- Layout, panels, measure/arrange, virtualization, large item surfaces:
  `skills/avalonia-layout-and-virtualization/SKILL.md`
- Animation, compositor, drawing, Skia, rendering interop:
  `skills/avalonia-rendering-and-graphics/SKILL.md`
- File pickers, clipboard, launcher, screens, platform integration:
  `skills/avalonia-platform-services/SKILL.md`
- Validation, accessibility, automation semantics:
  `skills/avalonia-accessibility-and-validation/SKILL.md`
- Tests, diagnostics, profiling, troubleshooting, performance hardening:
  `skills/avalonia-testing-diagnostics-and-performance/SKILL.md`
- Professional design systems, tokens, motion, dense workflow UX:
  `skills/avalonia-design-systems/SKILL.md`
- Microsoft Fluent design, `FluentTheme`, palette and shell guidance:
  `skills/avalonia-fluent-design/SKILL.md`
- HTML/CSS to Avalonia migration:
  `skills/html-css-to-avalonia/SKILL.md`
- WinForms to Avalonia migration:
  `skills/winforms-to-avalonia/SKILL.md`
- WPF to Avalonia migration:
  `skills/wpf-to-avalonia/SKILL.md`
- WinUI to Avalonia migration:
  `skills/winui-to-avalonia/SKILL.md`
- Legacy Avalonia 11 to Avalonia 12 migration planning and execution:
  `skills/avalonia-12-migration/SKILL.md`

## First Pass Workflow

1. Identify whether the user is building new UI, fixing an existing app, or porting from another stack.
2. Pick the narrowest specialist skill that fits the task.
3. Load only the reference documents that specialist skill points to.
4. For any broad or design-heavy task, load `references/70-avalonia-12-source-and-reference-baseline.md` before using third-party product references.
5. Use generated API indexes only when signature-level lookup is required; verify important signatures against `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`.
6. Escalate to the legacy migration lane only when the request explicitly involves upgrading older Avalonia code.

## Output Expectations

- For broad requests, state which specialist path you are taking and why.
- For implementation work, keep architecture, view/viewmodel, and styling concerns separated.
- For migration work, anchor comparisons in the source framework's idioms and call out Avalonia equivalents explicitly.
