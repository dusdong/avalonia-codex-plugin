---
name: avalonia-design-systems
description: Design polished Avalonia design systems with reusable tokens, typography, spacing, shell composition, dense workflow UX, motion, and governance rules. Use for professional UI direction, design-token architecture, responsive layout systems, information architecture, or high-quality desktop workflow design.
---

# Avalonia Design Systems

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/66-professional-ui-design-tokens-and-themes.md`
- `../../references/professional-design/README.md`
- `../../references/73-avalonia-12-ai-desktop-product-patterns.md` when the design task is an AI desktop workbench, assistant shell, settings center, plugin surface, tray entry, overlay, or notification flow.

Load only the lane chapters that fit the task:

- token architecture and layering
- typography, iconography, and hierarchy
- color, elevation, and shell surfaces
- responsive layout, density, feedback, and forms
- motion, accessibility, inclusive design, and quality gates

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Define tokens and resource layering before component styling proliferates.
2. Establish shell structure, information architecture, and density rules early.
3. Tie motion and feedback decisions to task flow, not decoration.
4. Keep design language and governance rules explicit so later work stays consistent.

## Rules

- Prefer reusable tokens over ad-hoc brush or spacing values.
- Treat accessibility, localization, and mixed-input ergonomics as first-class design constraints.
- Use this lane for professional product surfaces, not only visual polish.
