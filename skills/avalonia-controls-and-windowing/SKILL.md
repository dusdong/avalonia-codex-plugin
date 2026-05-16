---
name: avalonia-controls-and-windowing
description: Build or troubleshoot Avalonia controls, control themes, windows, popups, menus, tray integration, native menus, top-level services, and notification surfaces. Use for templated control authoring, popup behavior, custom chrome, dialog flows, menu systems, or per-control API guidance.
---

# Avalonia Controls and Windowing

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/10-templated-controls-and-control-themes.md`
- `../../references/13-windowing-and-custom-decorations.md`
- `../../references/48-toplevel-window-and-runtime-services.md`

Load these based on the requested surface:

- `../../references/25-popups-flyouts-tooltips-and-overlays.md`
- `../../references/52-controls-reference-catalog.md`
- `../../references/53-menu-controls-contextmenu-and-menuflyout-patterns.md`
- `../../references/54-native-menu-and-native-menubar-integration.md`
- `../../references/55-tray-icons-and-system-tray-integration.md`
- `../../references/56-managed-notifications-and-window-notification-manager.md`

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Separate control contract, template, and host surface concerns.
2. Pick the right top-level surface: window, popup, flyout, native menu, tray, or in-app notification.
3. Use the controls catalog only as a quick lookup after the workflow docs have narrowed the direction.
4. Validate platform-specific window or popup behavior explicitly.

## Rules

- Keep template parts and visual states documented in the implementation.
- Avoid mixing shell, popup, and notification logic into one control when host services are a better fit.
- Treat per-platform chrome and tray behavior as opt-in integration work.
