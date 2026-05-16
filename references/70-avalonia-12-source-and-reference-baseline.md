# Avalonia 12 Source and Reference Baseline

Use this file before relying on any Avalonia API or third-party product pattern in this plugin.

## Source Baseline

The authoritative Avalonia 12 source tree for this plugin is:

`/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia`

Current evidence:

| Evidence | Value |
| --- | --- |
| Git commit | `837e1aa91dd34bbd9e4d4c932a18878be2a4d753` |
| Source branch | `master` |
| Version file | `build/SharedVersion.props` |
| Version value | `12.1.999` |
| Target framework file | `build/TargetFrameworks.props` |
| Current target framework | `net10.0` |

Rules:

- Treat this source tree as the final authority for Avalonia 12 APIs, platform services, controls, styles, diagnostics, tests, and build behavior.
- Use generated API indexes only as lookup helpers. If an index disagrees with this source tree, the source tree wins.
- Do not use Avalonia 11.x APIs as default guidance. They are valid only when explicitly discussing legacy migration or compatibility.

## Allowed Product References

Default product references must come from projects that clearly use Avalonia 12 packages.

| Project | Evidence | Default Use |
| --- | --- | --- |
| `mnemo` | `third_party/ai_desktop_refs/mnemo/Mnemo.UI/Mnemo.UI.csproj` uses `Avalonia` `12.0.2` and targets `net10.0`. | Primary reference for AI workbench layout, module navigation, right-side assistant, overlays, and theme organization. |
| `Netor.Cartana` | `third_party/ai_desktop_refs/Netor.Cartana/Src/Netor.Cortana.UI/Netor.Cortana.UI.csproj` uses `Avalonia` `12.0.1` and targets `net10.0`. | Chinese AI assistant UX, drawers, settings center, floating entry, speech bubble, plugin/MCP information architecture. |
| `ClippyAI` | `third_party/ai_desktop_refs/ClippyAI/ClippyAI/ClippyAI.csproj` uses `Avalonia` `12.0.2`; notification library uses `12.0.1`. | Local reference for small tool windows, tray visibility, clipboard workflows, task templates, and notification wrapping. |

Detailed product-reference evidence lives in:

`/Volumes/程序开发/Du-Framework/Du.Ingest/docs/reference/ai-desktop-projects.md`

Pattern-level AI desktop experience extracted from those projects lives in:

`references/73-avalonia-12-ai-desktop-product-patterns.md`

Use that file for workbench, assistant, settings center, plugin/MCP, tray, floating entry, overlay, notification, theme-token, View/ViewModel, platform-service, and anti-copy guidance. It remains project-pattern evidence; source facts still come from `frameworks/Avalonia`.

## Excluded from Default Guidance

These projects may be useful for migration comparison or product inspiration, but they must not be used as default Avalonia 12 API examples:

| Project | Reason |
| --- | --- |
| `Everywhere` | `Directory.Packages.props` pins `AvaloniaVersion` to `11.3.12`. |
| `StabilityMatrix` | `Directory.Build.props` pins `AvaloniaVersion` to `11.3.7`. |
| `avallama` | `avallama.csproj` pins `AvaloniaVersion` to `11.3.9`. |
| `WhisperVoiceInput` | `WhisperVoiceInput.csproj` references Avalonia `11.2.4`. |

When referencing an excluded project, label it as legacy contrast, migration comparison, or product inspiration. Do not present its XAML, APIs, or package assumptions as Avalonia 12 defaults.

## Verification Commands

```bash
git -C /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia rev-parse HEAD
sed -n '1,80p' /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia/build/SharedVersion.props
sed -n '1,80p' /Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia/build/TargetFrameworks.props
rg -n "<AvaloniaVersion>|PackageVersion Include=\"Avalonia\"|PackageReference Include=\"Avalonia\"" /Volumes/程序开发/Du-Framework/Du.Ingest/third_party/ai_desktop_refs -g '*.csproj' -g '*.props'
```
