---
name: winui-to-avalonia
description: Port WinUI or Windows App SDK applications to Avalonia, including shell design, dependency-property patterns, theme resources, composition, commands, dialogs, and platform integration. Use for `NavigationView`, `ContentDialog`, `ThemeResource`, `VisualStateManager`, `ItemsRepeater`, `AppWindow`, or broader WinUI-to-Avalonia migration work.
---

# WinUI to Avalonia

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/65-winui-to-avalonia-modern-ui-conversion-index.md`
- `../../references/winui-to-avalonia/README.md`

Prioritize the chapters that match the source app:

- object or property system, bindings, resources, and state mapping
- `NavigationView`, dialog, titlebar, and multi-window shell behavior
- composition, rendering, scroll, gesture, and advanced control migration
- platform services, activation, storage, notifications, and WebView boundaries

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Identify the WinUI shell and state model before moving individual controls.
2. Translate `ThemeResource`, `VisualStateManager`, and composition assumptions explicitly.
3. Rebuild platform integration through Avalonia services rather than Windows-only primitives.
4. Keep modern-shell decisions intentional instead of chasing one-to-one surface parity.

## Rules

- Do not treat `NavigationView`, `ContentDialog`, or `AppWindow` as direct API renames.
- Separate composition effects from essential interaction behavior.
- Make Windows-specific contracts and Avalonia cross-platform replacements explicit.
