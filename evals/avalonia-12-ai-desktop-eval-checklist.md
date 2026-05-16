# Avalonia 12 AI Desktop Eval Checklist

This checklist makes the AI desktop evals executable by recording the expected route, actual route, evidence classes, no-copy result, and source verification result for each scenario. It is a human-or-agent evaluation artifact; it does not require copying third-party project code.

## Execution Rules

- Use only `mnemo`, `Netor.Cartana`, and `ClippyAI` as default Avalonia 12 project-pattern evidence.
- Treat `Everywhere`, `StabilityMatrix`, `avallama`, and `WhisperVoiceInput` as Avalonia 11.x migration contrast only.
- Load `references/73-avalonia-12-ai-desktop-product-patterns.md` and `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`.
- For each eval, record `Expected route`, `Actual route`, `Evidence classes`, `No-copy result`, `Avalonia source verification`, and `Notes`.
- A passing result must separate Avalonia 12 source facts, Avalonia 12 project patterns, and Avalonia 11.x migration contrast.

## Eval Case: AI Desktop Workbench

- Prompt source: `evals/avalonia-12-plugin-prompts.md` Eval 11
- Expected route: `ui-patterns` plus `app-building`; `avalonia-design-systems`, `avalonia-controls-and-windowing`, `avalonia-views-and-templating`, `references/73-avalonia-12-ai-desktop-product-patterns.md`, `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`
- Expected evidence classes: Avalonia 12 source facts; Avalonia 12 project patterns; no Avalonia 11.x default guidance
- Required source projects: `mnemo`, `Netor.Cartana`, `ClippyAI`
- Required checklist topics: workspace navigation, right assistant, overlay, toast, settings center, plugin/MCP
- Actual route:
- Evidence classes observed:
- No-copy result:
- Avalonia source verification:
- Notes:

## Eval Case: Tray Utility and Clipboard Flow

- Prompt source: `evals/avalonia-12-plugin-prompts.md` Eval 12
- Expected route: `ui-patterns` plus `debugging`; `avalonia-platform-services`, `avalonia-controls-and-windowing`, `avalonia-testing-diagnostics-and-performance`, `references/73-avalonia-12-ai-desktop-product-patterns.md`, `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`
- Expected evidence classes: Avalonia 12 source facts; `ClippyAI` as local utility pattern evidence; `Netor.Cartana` as plugin/MCP settings evidence; `mnemo` as overlay/toast evidence
- Required source projects: `ClippyAI`, `Netor.Cartana`, `mnemo`
- Required checklist topics: tray, floating window, clipboard utility, system notification wrapper, plugin/MCP
- Actual route:
- Evidence classes observed:
- No-copy result:
- Avalonia source verification:
- Notes:

## Eval Case: Overlay and Notification Review

- Prompt: Review an Avalonia 12 AI desktop overlay/toast/notification design for focus, modal behavior, queueing, fallback, and platform risks.
- Expected route: `ui-patterns` plus `debugging`; `avalonia-controls-and-windowing`, `avalonia-testing-diagnostics-and-performance`, `references/73-avalonia-12-ai-desktop-product-patterns.md`, `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`
- Expected evidence classes: Avalonia 12 source facts for popup/notification APIs; `mnemo` overlay/toast project patterns; `ClippyAI` notification wrapper project patterns
- Required source projects: `mnemo`, `ClippyAI`
- Required checklist topics: overlay, toast, system notification wrapper, accessibility/focus, platform fallback
- Actual route:
- Evidence classes observed:
- No-copy result:
- Avalonia source verification:
- Notes:

## Eval Case: Plugin MCP Settings

- Prompt: Design an Avalonia 12 settings center for model providers, agents, MCP servers, plugin lifecycle, auth state, and diagnostics without copying third-party protocols.
- Expected route: `ui-patterns` plus `app-building`; `avalonia-design-systems`, `avalonia-views-and-templating`, `avalonia-platform-services`, `references/73-avalonia-12-ai-desktop-product-patterns.md`, `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md`
- Expected evidence classes: Avalonia 12 source facts for settings UI/platform services; `Netor.Cartana` project patterns for plugin/MCP information architecture
- Required source projects: `Netor.Cartana`
- Required checklist topics: settings center, plugin/MCP, failure states, secret handling, platform process/file risks
- Actual route:
- Evidence classes observed:
- No-copy result:
- Avalonia source verification:
- Notes:

## Result Summary Template

| Eval Case | Expected route | Actual route | Evidence classes OK | No-copy OK | Source verification OK | Result |
| --- | --- | --- | --- | --- | --- | --- |
| AI Desktop Workbench |  |  |  |  |  |  |
| Tray Utility and Clipboard Flow |  |  |  |  |  |  |
| Overlay and Notification Review |  |  |  |  |  |  |
| Plugin MCP Settings |  |  |  |  |  |  |
