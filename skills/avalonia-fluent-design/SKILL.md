---
name: avalonia-fluent-design
description: Build or refine Avalonia UIs that follow Microsoft Fluent guidance with `FluentTheme`, palette customization, density tuning, Fluent shells, iconography, motion, and language-system patterns. Use for FluentTheme adoption, brand mapping onto Fluent tokens, Fluent shell design, or Fluent-specific accessibility and motion work.
---

# Avalonia Fluent Design

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/67-microsoft-fluent-design-and-fluenttheme.md`
- `../../references/fluent-design/README.md`

Load only the needed Fluent chapters:

- theme bootstrap, density, and palette customization
- brand or alias-token mapping
- Fluent shells, controls, command surfaces, and motion
- content language, onboarding, notifications, and icons

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Confirm that Fluent is the intended visual system before tuning tokens.
2. Start with `FluentTheme` bootstrap, density, and palette rules.
3. Apply Fluent shell, command, and motion patterns consistently across the surface.
4. Verify that localization, inclusive content, and mixed-input behavior still hold after styling.

## Rules

- Do not bolt Fluent visuals onto a conflicting token system without an explicit mapping layer.
- Keep Fluent motion and materials purposeful, not ornamental.
- Use the Fluent-specific lane when the request is about Fluent design, not generic styling.
