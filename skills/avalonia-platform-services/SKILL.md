---
name: avalonia-platform-services
description: Integrate or troubleshoot Avalonia platform services such as storage provider, clipboard, launcher, drag/drop, screens, and top-level runtime helpers. Use for file pickers, external-open flows, clipboard or data-transfer bugs, multi-screen behavior, or platform service abstractions.
---

# Avalonia Platform Services

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/29-storage-provider-and-file-pickers.md`
- `../../references/31-clipboard-and-data-transfer.md`
- `../../references/32-launcher-and-external-open.md`
- `../../references/33-screens-and-display-awareness.md`
- `../../references/73-avalonia-12-ai-desktop-product-patterns.md` when AI desktop patterns involve tray visibility, floating windows, clipboard tools, notifications, plugin processes, MCP servers, or workspace file services.
- `../../references/74-avalonia-12-ai-desktop-recipes-and-checklists.md` when platform-service acceptance criteria must cover tray, floating windows, clipboard, notifications, plugin processes, MCP, files, screens, or cross-platform risks.

Load these when workflow overlap exists:

- `../../references/34-dragdrop-workflows.md`
- `../../references/48-toplevel-window-and-runtime-services.md`

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Resolve which top-level or window owns the service interaction.
2. Keep platform-service abstractions thin and centered on Avalonia APIs.
3. Model data-transfer contracts explicitly for drag/drop and clipboard flows.
4. Validate multi-window, multi-screen, and external-open behavior on the target platform.

## Rules

- Prefer Avalonia service abstractions over platform-specific escape hatches.
- Keep file-picker and launcher flows async and user-driven.
- Treat clipboard and drag/drop formats as part of the app contract.
