---
name: avalonia-accessibility-and-validation
description: Design or review Avalonia validation, data-error presentation, accessibility semantics, automation properties, focus order, and testable UI metadata. Use for validation pipelines, screen-reader support, keyboard-only UX, automation-tree issues, or accessibility hardening.
---

# Avalonia Accessibility and Validation

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/22-validation-pipeline-and-data-errors.md`
- `../../references/23-accessibility-and-automation.md`
- `../../references/60-automation-properties-and-attached-behavior-patterns.md`

Load these when keyboard behavior is involved:

- `../../references/19-focus-and-keyboard-navigation.md`

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Define how validation state is surfaced in the viewmodel, control, and visual layer.
2. Verify labels, focus order, and automation metadata together instead of as isolated fixes.
3. Keep automation names, help text, and control relationships stable.
4. Make the final accessibility contract easy to test.

## Rules

- Prefer `INotifyDataErrorInfo`-friendly flows for rich validation.
- Do not treat automation metadata as optional polish.
- Keep keyboard-only navigation credible before declaring a surface accessible.
