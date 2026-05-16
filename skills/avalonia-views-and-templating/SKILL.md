---
name: avalonia-views-and-templating
description: Build or refactor Avalonia view composition, view-location strategies, templates, templated content, and tree-inspection patterns. Use for view locator work, `DataTemplate` or `IDataTemplate` selection, templated parent issues, logical or visual tree traversal, or content-template architecture.
---

# Avalonia Views and Templating

Start with:

- `../../references/70-avalonia-12-source-and-reference-baseline.md`
- `../../references/11-user-views-locator-and-tree-patterns.md`
- `../../references/38-data-templates-and-idatatemplate-selector-patterns.md`
- `../../references/51-template-content-and-func-template-patterns.md`
- `../../references/73-avalonia-12-ai-desktop-product-patterns.md` when view composition involves AI workbench modules, assistant panels, settings pages, plugin pages, or compact utility views.
- `../../references/74-avalonia-12-ai-desktop-recipes-and-checklists.md` when view composition needs checklist-level coverage for workspace navigation, settings pages, plugin/MCP pages, or utility views.

Load these when lookup or debugging matters:

- `../../references/39-visual-tree-inspection-and-traversal.md`
- `../../references/40-logical-tree-inspection-and-traversal.md`

## Evidence Discipline

- Avalonia 12 source facts: verify APIs, package behavior, target frameworks, and platform behavior against `../../references/70-avalonia-12-source-and-reference-baseline.md` and the local `frameworks/Avalonia` source tree before making default recommendations.
- Avalonia 12 project patterns: use only the allowed Avalonia 12 projects named in the baseline/reference-project evidence for product architecture, UI composition, and engineering patterns.
- Avalonia 11.x migration contrast: mention legacy Avalonia 11.x behavior only when the task is explicitly about migration, compatibility risk, or anti-patterns; never promote it as default Avalonia 12 guidance.

## Workflow

1. Choose whether composition belongs in views, templates, or view-location infrastructure.
2. Keep template selection deterministic and typed when possible.
3. Use logical or visual tree traversal deliberately and only where ownership is clear.
4. Separate reusable templates from app-specific shell composition.

## Rules

- Prefer simple `DataTemplate` and `x:DataType` flows before custom selector infrastructure.
- Keep tree walking out of hot paths when a direct reference or binding can do the job.
- Make template-part and templated-parent assumptions explicit.
