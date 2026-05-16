# Upstream And Maintenance Boundary

This repository is maintained independently as `dusdong/avalonia-codex-plugin`.

## Upstream Repository

- Original upstream: [wieslawsoltes/development-plugin-for-avalonia](https://github.com/wieslawsoltes/development-plugin-for-avalonia)
- Local remote name: `upstream`
- Maintained repository: [dusdong/avalonia-codex-plugin](https://github.com/dusdong/avalonia-codex-plugin)
- Local remote name: `origin`

## Maintenance Scope

This repository is no longer a generic Avalonia development plugin. It is maintained as an Avalonia 12 focused Codex plugin.

Default guidance is pinned to the local Avalonia 12 source baseline documented in `references/70-avalonia-12-source-and-reference-baseline.md`.

Avalonia 11.x material is allowed only for migration contrast, compatibility analysis, or historical context. It must not become the default implementation recommendation.

## Upstream Sync Policy

Upstream changes may be reviewed and selectively ported when they improve the Avalonia 12 plugin. Do not merge upstream changes wholesale if they reintroduce old default version assumptions or broaden the plugin away from the Avalonia 12 scope.

Keep original license notices intact when carrying forward upstream material.
