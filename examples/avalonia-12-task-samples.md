# Avalonia 12 Task Samples

These samples describe the expected shape of plugin responses. They are intentionally pattern-level examples and do not copy code from third-party reference projects.

## Sample 1: Create an Avalonia 12 Desktop App

Expected route: `avalonia-bootstrap-and-lifetime` -> `avalonia-bindings-and-xaml` -> `avalonia-styling-and-resources`.

Expected output:

- state that the source baseline is `frameworks/Avalonia` with `12.1.999 / net10.0`,
- create or update app startup, `App.axaml`, root window, and view model wiring,
- prefer compiled bindings with `x:DataType`,
- verify uncertain APIs against local source before finalizing.

## Sample 2: Build a Dense AI Desktop Shell

Expected route: `avalonia-controls-and-windowing` -> `avalonia-layout-and-virtualization` -> `avalonia-design-systems`.

Expected output:

- use Avalonia 12 controls and layout primitives as source-backed facts,
- extract product patterns only from allowed Avalonia 12 projects,
- keep action surfaces compact and task-oriented,
- avoid copying project code or styling from references.

## Sample 3: Diagnose XAML and Binding Failures

Expected route: `avalonia-bindings-and-xaml` -> `avalonia-testing-diagnostics-and-performance`.

Expected output:

- separate XAML compile errors, runtime binding errors, data-context mistakes, and trimming/AOT risks,
- inspect source-backed binding APIs when the failure depends on a signature,
- provide a minimal repro or focused verification command where possible.

## Sample 4: Migrate Avalonia 11.x to Avalonia 12

Expected route: `avalonia-12-migration`.

Expected output:

- treat Avalonia 11.x code as legacy input only,
- identify removed or changed APIs,
- map each change to an Avalonia 12 source-backed replacement or redesign,
- keep old APIs out of default new-app advice.

## Sample 5: Port WPF Shell Patterns

Expected route: `wpf-to-avalonia` -> relevant app-building skill.

Expected output:

- translate WPF concepts before writing Avalonia guidance,
- call out missing direct parity for `CommandManager`, triggers, and native-host assumptions,
- use Avalonia 12 source facts for the target implementation,
- reserve WPF details for migration contrast.

## Sample 6: Verify a Source-Level API Claim

Expected route: `source-reference` through the active specialist skill.

Expected output:

- search `references/api-index-generated.md` for a fast first pass,
- verify important signatures or behavior under `frameworks/Avalonia/src`,
- cite the relevant local source path or generated reference,
- mark any unresolved API claim as provisional instead of presenting it as default guidance.
