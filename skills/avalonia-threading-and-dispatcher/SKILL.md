---
name: avalonia-threading-and-dispatcher
description: Design or review Avalonia reactive flows, dispatcher usage, timers, async UI coordination, and thread-affinity boundaries. Use for `Dispatcher.UIThread`, background work handoff, timer selection, reactive pipeline fixes, or UI-thread correctness bugs.
---

# Avalonia Threading and Dispatcher

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/03-reactive-threading.md`
- `../../references/47-dispatcher-priority-operations-and-timers.md`

Load these when quality hardening matters:

- `../../references/08-performance-checklist.md`
- `../../references/27-diagnostics-profiling-and-devtools.md`

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Identify which state is allowed off-thread and which UI mutations must stay on the UI thread.
2. Pick the right dispatch primitive: immediate post, prioritized operation, or timer.
3. Keep reactive or async chains explicit about scheduler and dispatch boundaries.
4. Verify cancellation, teardown, and shutdown behavior for long-lived subscriptions or timers.

## Rules

- Never hide UI-thread assumptions in helper layers.
- Prefer explicit dispatcher boundaries over accidental thread capture.
- Use timers and background loops sparingly and always with disposal or cancellation.
