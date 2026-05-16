# Controls Reference Catalog

This catalog provides one reference document per public Avalonia control type.

## Scope

- Source: local Avalonia 12 control assemblies (`src/Avalonia.Controls*`) from `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`
- Coverage: public classes identified as controls by inheritance from `Control`, `TopLevel`, or `WindowBase`
- Per-control content:
  - basic type metadata,
  - basic public API list,
  - minimal XAML usage,
  - minimal C# usage.

## Entry Point

- [`controls/README.md`](controls/)

## Generation

Use the generator script to rebuild all control references:

```bash
python3 scripts/generate_control_reference_docs.py \
  --repo /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia \
  --git-ref HEAD \
  --output-dir references/controls
```

## Notes

- Some controls are abstract; their docs include derived-type usage snippets.
- These docs are intentionally basic and uniform to support fast lookup across the full control surface.
