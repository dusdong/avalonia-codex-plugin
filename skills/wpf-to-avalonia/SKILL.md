---
name: wpf-to-avalonia
description: Port WPF applications and patterns to Avalonia, including dependency-property mapping, bindings, resources, templates, layout, rendering, and shell behavior. Use for `DependencyProperty`, routed-command, trigger, `Frame` or `Page`, `OnRender`, `HwndHost`, or other WPF-to-Avalonia migration work.
---

# WPF to Avalonia

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/64-wpf-to-avalonia-modern-ui-conversion-index.md`
- `../../references/wpf-to-avalonia/README.md`

Prioritize the chapters that match the WPF source:

- property system, bindings, resources, styles, and templates
- layout, navigation, windows, dialogs, and dispatcher workflows
- rendering, animation, popup, interop, and document workflows
- advanced control families, selection models, and platform services

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Map the WPF concept first, then choose the Avalonia equivalent or redesign.
2. Call out where Avalonia does not preserve a WPF subsystem directly, especially triggers, navigation, and interop.
3. Replace resource, layout, and rendering assumptions before doing control-by-control cleanup.
4. Keep the migration narrative explicit about what stays familiar and what changes materially.

## Rules

- Do not promise WPF trigger, `CommandManager`, or `HwndHost` parity where it does not exist.
- Use Avalonia selectors, templates, and state patterns rather than recreating WPF internals.
- Keep document and printing workflows in a separate explicit decision track.
