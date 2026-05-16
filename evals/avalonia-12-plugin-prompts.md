# Avalonia 12 Plugin Evaluation Prompts

Use these prompts to verify that the plugin routes work correctly and does not drift back to Avalonia 11.x defaults.

## Eval 1: New App Bootstrap

Prompt: Build a new Avalonia desktop shell with `net10.0`, compiled bindings, a main window, and explicit lifetime setup.

Expected route: `app-building` via `avalonia-bootstrap-and-lifetime`, then `avalonia-bindings-and-xaml`.

Expected evidence: Avalonia 12 source facts for version and target framework; no Avalonia 11.x package suggestion.

## Eval 2: Binding Failure

Prompt: My compiled binding fails after refactoring a view model. Diagnose the likely Avalonia issue.

Expected route: `debugging` via `avalonia-bindings-and-xaml` plus `avalonia-testing-diagnostics-and-performance`.

Expected evidence: source-reference for compiled binding behavior; no generic WPF binding advice unless explicitly labeled as migration contrast.

## Eval 3: Command Bar UI

Prompt: Design a dense desktop AI assistant toolbar using Avalonia 12 controls.

Expected route: `ui-patterns` via `avalonia-controls-and-windowing` plus `avalonia-design-systems`.

Expected evidence: source facts for Avalonia 12 controls such as `CommandBar`; project patterns may reference only allowed Avalonia 12 projects.

## Eval 4: WPF Migration

Prompt: Port this WPF `DependencyProperty`, `CommandManager`, and `HwndHost` usage to Avalonia.

Expected route: `migration` via `wpf-to-avalonia`.

Expected evidence: WPF concepts as source-side input, Avalonia 12 equivalents as target guidance, explicit warning for missing parity.

## Eval 5: Legacy Avalonia Upgrade

Prompt: Upgrade an Avalonia 11.3.x app that uses removed file dialog APIs and old window chrome patterns.

Expected route: `migration` via `avalonia-12-migration`.

Expected evidence: Avalonia 11.x migration contrast plus Avalonia 12 source facts; do not recommend the old APIs as defaults.

## Eval 6: API Uncertainty

Prompt: Does Avalonia 12 expose the same runtime service from `TopLevel` that our Avalonia 11 code used?

Expected route: `source-reference` via the active domain skill and `references/api-index-generated.md`.

Expected evidence: answer must say to verify important signatures against `frameworks/Avalonia`; generated index is not the final authority.

## Eval 7: Product Reference Filtering

Prompt: Use the AI desktop reference projects to recommend an Avalonia app architecture.

Expected route: `ui-patterns` via `avalonia-design-systems` and `71-skill-routing-and-evaluation.md`.

Expected evidence: only `mnemo`, `Netor.Cartana`, and `ClippyAI` are default product references; Avalonia 11.x projects are excluded or contrast only.

## Eval 8: Performance Review

Prompt: Review an Avalonia 12 data-heavy page for virtualization, dispatcher, and rendering risks.

Expected route: `debugging` plus `app-building` via layout, threading, rendering, and testing skills.

Expected evidence: source facts for controls/layout behavior; recommendations separated into UI-thread, layout, and rendering layers.

## Eval 9: HTML/CSS Conversion

Prompt: Convert a responsive HTML/CSS dashboard into Avalonia 12 views and styles.

Expected route: `migration` via `html-css-to-avalonia`, then styling/layout skills.

Expected evidence: HTML/CSS is source-side input; Avalonia 12 XAML, styles, and layout are target guidance.

## Eval 10: Fluent Theme

Prompt: Build a Fluent-themed Avalonia 12 settings window with theme variants and design tokens.

Expected route: `ui-patterns` plus `app-building` via `avalonia-fluent-design` and `avalonia-styling-and-resources`.

Expected evidence: Avalonia 12 source facts for theme APIs; design-token guidance must not depend on Avalonia 11.x defaults.

## Eval 11: AI Desktop Workbench Patterns

Prompt: Build an Avalonia 12 AI workbench with left module navigation, central workspace, right assistant, overlay dialogs, toast history, and a settings/plugin center using the AI desktop reference projects.

Expected route: `ui-patterns` plus `app-building` via `avalonia-design-systems`, `avalonia-controls-and-windowing`, `avalonia-views-and-templating`, `73-avalonia-12-ai-desktop-product-patterns.md`, and `74-avalonia-12-ai-desktop-recipes-and-checklists.md`.

Expected evidence: extract patterns from `mnemo`, `Netor.Cartana`, and `ClippyAI`; name source projects and key files; verify API choices against `frameworks/Avalonia`; do not copy third-party XAML, code, resources, plugin protocol, or visual constants.

## Eval 12: AI Desktop Tray and Utility Review

Prompt: Review a compact Avalonia 12 tray-first clipboard AI utility with a floating window, notification wrapper, task presets, and MCP plugin settings.

Expected route: `ui-patterns` plus `debugging` via `avalonia-platform-services`, `avalonia-controls-and-windowing`, `avalonia-testing-diagnostics-and-performance`, `73-avalonia-12-ai-desktop-product-patterns.md`, and `74-avalonia-12-ai-desktop-recipes-and-checklists.md`.

Expected evidence: use `ClippyAI` only as local utility pattern evidence, use `Netor.Cartana` for plugin/MCP settings information architecture, use `mnemo` for overlay/toast service layering; flag polling, fixed sizing, Topmost defaults, and direct platform calls in ViewModels as risks.

## Eval 13: AI Desktop Overlay and Notification Acceptance

Prompt: Validate an Avalonia 12 AI desktop overlay, toast, and system-notification design for focus restore, modal behavior, queue capacity, fallback, and platform risks.

Expected route: `ui-patterns` plus `debugging` via `avalonia-controls-and-windowing`, `avalonia-testing-diagnostics-and-performance`, `73-avalonia-12-ai-desktop-product-patterns.md`, and `74-avalonia-12-ai-desktop-recipes-and-checklists.md`.

Expected evidence: use `mnemo` only as overlay/toast service-pattern evidence and `ClippyAI` only as notification-wrapper evidence; verify popup and notification APIs against `frameworks/Avalonia`; record checklist result fields for expected route, actual route, evidence classes, no-copy result, and source verification.

## Eval 14: AI Desktop Plugin MCP Settings Acceptance

Prompt: Design and review an Avalonia 12 settings center for providers, agents, MCP servers, plugin lifecycle, auth state, diagnostics, and failure recovery.

Expected route: `ui-patterns` plus `app-building` via `avalonia-design-systems`, `avalonia-views-and-templating`, `avalonia-platform-services`, `73-avalonia-12-ai-desktop-product-patterns.md`, and `74-avalonia-12-ai-desktop-recipes-and-checklists.md`.

Expected evidence: use `Netor.Cartana` only for plugin/MCP information-architecture patterns; do not copy its plugin protocol, manifest schema, fields, package names, or generator assumptions; verify settings UI and platform service APIs against `frameworks/Avalonia`.
