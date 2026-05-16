---
name: avalonia-testing-diagnostics-and-performance
description: Validate Avalonia applications with headless tests, render or UI tests, diagnostics tooling, troubleshooting workflows, and performance reviews. Use for test strategy, DevTools or profiler usage, performance regressions, rendering investigations, or production hardening passes.
---

# Avalonia Testing, Diagnostics, and Performance

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/26-testing-stack-headless-render-and-ui-tests.md`
- `../../references/27-diagnostics-profiling-and-devtools.md`
- `../../references/08-performance-checklist.md`
- `../../references/07-troubleshooting.md`
- `../../references/73-avalonia-12-ai-desktop-product-patterns.md` when validating AI desktop product-pattern regressions such as overlay stacking, assistant streaming state, tray restore behavior, notification routing, plugin settings, or clipboard utility loops.

Load this when an integrated sample helps:

- `../../references/09-end-to-end-examples.md`

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Pick the right confidence level: unit, headless render, UI, or manual diagnostics.
2. Reproduce the issue before optimizing or broadening the fix.
3. Use diagnostics output to narrow the subsystem before rewriting code.
4. End with a concrete regression-safety plan.

## Rules

- Measure first when performance is the claimed problem.
- Keep troubleshooting steps tied to reproducible symptoms.
- Add tests for bug classes, not only the single observed path.
