# Avalonia 12 AI Desktop Recipes and Checklists

本文件是 `73-avalonia-12-ai-desktop-product-patterns.md` 的执行层补充。它把 `mnemo`、`Netor.Cartana`、`ClippyAI` 的 Avalonia 12 project patterns 转成可复用 recipes 和验收清单，但仍然只提炼模式，不复制也不得照搬第三方 XAML、C#、资源、协议、图标、字符串、布局常量或命名体系。

## Evidence and No-Copy Contract

- 默认来源项目只能是 `mnemo`、`Netor.Cartana`、`ClippyAI`。
- `Everywhere`、`StabilityMatrix`、`avallama`、`WhisperVoiceInput` 只可作为 Avalonia 11.x 迁移对比，不得进入默认参考。
- 每个 recipe 必须同时记录：来源项目、关键文件、Avalonia 12 源码验证点、交互状态、失败态、可访问性/焦点/多屏/平台差异风险。
- 实现时从目标产品需求重新设计；不得复制 third-party 项目代码、资源、插件协议、prompt、窗口尺寸、z-index、样式 key 或视觉常量。

## Recipe 1: Workspace Navigation

| Field | Guidance |
| --- | --- |
| 来源项目 | `mnemo` |
| 关键文件 | `Mnemo.UI/Views/MainWindow.axaml`, `Mnemo.UI/ViewModels/MainWindowViewModel.cs`, `Mnemo.UI/Components/Sidebar/Sidebar.axaml`, `Mnemo.UI/Components/Sidebar/SidebarViewModel.cs` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/ContentControl.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Templates/DataTemplates.cs`, `frameworks/Avalonia/src/Avalonia.Controls/SplitView/SplitView.cs` |
| 交互状态 | collapsed/expanded sidebar, selected module, badge/status, quick action, keyboard navigation, active workspace content |
| 失败态 | missing view mapping, stale selected item, invalid workspace VM, navigation command rejected, empty module list |
| 可访问性/焦点风险 | collapsed icon-only navigation must expose automation names and tooltips; focus return must land on active workspace after navigation |
| 多屏/平台差异风险 | window restore and density should not assume one fixed screen size |

验收清单：

- [ ] Shell VM 只组合 navigation、workspace、assistant、overlay、toast 等服务，不承载业务流程。
- [ ] Module view is hosted through source-backed Avalonia content/template APIs.
- [ ] Selected state, focus state, disabled state, and empty state are explicit.
- [ ] Keyboard and pointer navigation are both defined.
- [ ] No `mnemo` XAML, resource keys, widths, command names, or component names are copied.

## Recipe 2: Right Assistant

| Field | Guidance |
| --- | --- |
| 来源项目 | `mnemo`, `Netor.Cartana` |
| 关键文件 | `Mnemo.UI/Components/RightSidebar/RightSidebar.axaml`, `Mnemo.UI/Components/RightSidebar/RightSidebarViewModel.cs`, `Src/Netor.Cortana.UI/Views/MainWindow.axaml`, `Src/Netor.Cortana.UI/Views/MainWindow.axaml.cs` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/TextBox.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Button.cs`, `frameworks/Avalonia/src/Avalonia.Controls/ItemsControl.cs`, `frameworks/Avalonia/src/Avalonia.Base/Input/Platform/IClipboard.cs` |
| 交互状态 | collapsed, expanded, streaming, stopped, retryable error, attachment selected, model/mode selected, conversation empty |
| 失败态 | provider unavailable, streaming cancellation, bad attachment, context too large, no workspace selected |
| 可访问性/焦点风险 | stop/send button label changes must be announced; stream updates should not steal focus from text input |
| 多屏/平台差异风险 | assistant width should use responsive constraints and remember per-window state |

验收清单：

- [ ] Assistant VM owns chat state; platform services and model providers are adapters.
- [ ] Send/stop/new-chat states are mutually coherent.
- [ ] Attachment and workspace-context failure messages are explicit.
- [ ] Streaming output has cancellation and retry paths.
- [ ] No third-party prompt, message template, suggestion text, or visual constants are copied.

## Recipe 3: Plugin and MCP Settings Center

| Field | Guidance |
| --- | --- |
| 来源项目 | `Netor.Cartana` |
| 关键文件 | `Src/Netor.Cortana.UI/Views/SettingsWindow.axaml`, `Src/Netor.Cortana.UI/Providers/PluginManagementProvider.cs`, `Src/Netor.Cortana.Plugin/Core/PluginManifest.cs`, `Src/Netor.Cortana.Plugin/PluginLoader.cs`, `Plugins/docs/参考文档/plugin-mcp.md`, `Plugins/docs/参考文档/native-plugin-dev-guide.md`, `Src/Netor.Cortana.Networks/WebSockets/*PluginBus*` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/ContentControl.cs`, `frameworks/Avalonia/src/Avalonia.Controls/ListBox.cs`, `frameworks/Avalonia/src/Avalonia.Controls/TabControl.cs`, `frameworks/Avalonia/src/Avalonia.Base/Platform/Storage/IStorageProvider.cs`, `frameworks/Avalonia/src/Avalonia.Base/Platform/Storage/ILauncher.cs` |
| 交互状态 | provider configured, model enabled, agent selected, MCP connected/disconnected, plugin loaded/unloaded/reloaded, auth missing |
| 失败态 | invalid manifest, runtime unavailable, permission denied, MCP transport timeout, plugin crash, version mismatch |
| 可访问性/焦点风险 | settings navigation must expose selected category and validation summaries |
| 多屏/平台差异风险 | external process and file path handling must be platform-aware |

验收清单：

- [ ] Settings IA separates system, providers, models, agents, MCP/tools, plugin auth, diagnostics.
- [ ] Plugin runtime state is explicit and observable.
- [ ] Destructive actions require confirmation and audit-friendly feedback.
- [ ] MCP transport, command, env, URL, and API key fields are validated without leaking secrets.
- [ ] No `Netor.Cartana` plugin protocol, manifest schema, field names, package names, or generated code are copied.

## Recipe 4: Tray and Floating Window

| Field | Guidance |
| --- | --- |
| 来源项目 | `ClippyAI`, `Netor.Cartana` |
| 关键文件 | `ClippyAI/App.axaml.cs`, `ClippyAI/Views/MainWindow.axaml`, `ClippyAI/Views/MainWindow.axaml.cs`, `Src/Netor.Cortana.UI/Views/FloatWindow.axaml`, `Src/Netor.Cortana.UI/Views/BubbleWindow.axaml` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/TrayIcon.cs`, `frameworks/Avalonia/src/Avalonia.Controls/NativeMenu.cs`, `frameworks/Avalonia/src/Avalonia.Controls/TopLevel.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Window.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Screens.cs` |
| 交互状态 | hidden, visible, activated from tray, moved, pinned, topmost requested, restored after display change |
| 失败态 | tray unavailable, screen missing, off-screen restore, focus denied, icon load failure |
| 可访问性/焦点风险 | floating entry needs keyboard reachable alternative and automation names |
| 多屏/平台差异风险 | screen bounds, tray behavior, focus activation, transparent windows, and topmost behavior vary by platform |

验收清单：

- [ ] Tray controls only window visibility and app commands; AI task logic stays outside tray handlers.
- [ ] Floating entry has non-floating fallback access.
- [ ] Position restore validates target screen and work area.
- [ ] Topmost is opt-in and reversible.
- [ ] No fixed positions, negative margins, glow constants, or third-party icons are copied.

## Recipe 5: Overlay and Toast

| Field | Guidance |
| --- | --- |
| 来源项目 | `mnemo` |
| 关键文件 | `Mnemo.UI/Components/OverlayPopupHost.axaml`, `Mnemo.UI/Services/OverlayService.cs`, `Mnemo.UI/Components/ToastHost.axaml`, `Mnemo.UI/Services/ToastService.cs` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/Primitives/Popup.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Primitives/PopupRoot.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Flyouts/PopupFlyoutBase.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Notifications/WindowNotificationManager.cs` |
| 交互状态 | overlay opened, modal backdrop, child overlay, close requested, dialog completed, timed toast, sticky toast, toast history |
| 失败态 | owner window closed, child overlay orphaned, close denied, toast capacity exceeded, timer disposed |
| 可访问性/焦点风险 | modal overlay must trap/restore focus; toast should not interrupt text entry |
| 多屏/平台差异风险 | window-level overlays must respect host bounds and scaling |

验收清单：

- [ ] Overlay service separates host collection, dialog completion, close policy, and visual template.
- [ ] Toast service separates timed/sticky/history and capacity rules.
- [ ] Focus restore and escape/close behavior are explicit.
- [ ] Overlay, toast, dialog, and system notification are not collapsed into one control.
- [ ] No z-index constants, templates, resource keys, or toast text are copied.

## Recipe 6: System Notification Wrapper

| Field | Guidance |
| --- | --- |
| 来源项目 | `ClippyAI` |
| 关键文件 | `Libs/DesktopNotificationsNet8/DesktopNotifications.Avalonia/AppBuilderExtensions.cs`, `Libs/DesktopNotificationsNet8/*` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/Notifications/WindowNotificationManager.cs`, `frameworks/Avalonia/src/Avalonia.Controls/TopLevel.cs` |
| 交互状态 | notification queued, shown, activated, dismissed, failed, fallback-to-in-app |
| 失败态 | platform backend unavailable, permission denied, app not foregrounded, activation payload invalid |
| 可访问性/焦点风险 | activation should land in a predictable view; dismissal should be non-destructive |
| 多屏/平台差异风险 | OS notification permissions and activation semantics differ per desktop platform |

验收清单：

- [ ] Notification manager is injected as a platform service.
- [ ] In-app fallback exists when system notification cannot be shown.
- [ ] Activation payload is typed and validated.
- [ ] Dismissal and activation are logged without leaking content.
- [ ] No platform notification implementation from `ClippyAI` is copied.

## Recipe 7: Clipboard Utility Flow

| Field | Guidance |
| --- | --- |
| 来源项目 | `ClippyAI` |
| 关键文件 | `ClippyAI/Views/MainView.axaml`, `ClippyAI/ViewModels/MainViewModel.cs`, `ClippyAI/Views/ConfigurationDialog.axaml`, `ClippyAI/ViewModels/ConfigurationDialogViewModel.cs` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Base/Input/Platform/IClipboard.cs`, `frameworks/Avalonia/src/Avalonia.Controls/TextBox.cs`, `frameworks/Avalonia/src/Avalonia.Controls/ComboBox.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Button.cs` |
| 交互状态 | clipboard loaded, task selected, running, cancelled, output ready, retry, image available, configuration open |
| 失败态 | clipboard denied, empty input, unsupported format, model failure, cancellation timeout, stale task config |
| 可访问性/焦点风险 | start/stop state must be reachable and announced; output navigation must not depend only on icons |
| 多屏/平台差异风险 | clipboard format and image availability differ per platform |

验收清单：

- [ ] Clipboard access is user-triggered or privacy-reviewed; polling is avoided unless explicitly justified.
- [ ] Task presets are data-driven and validated.
- [ ] Running/cancelled/completed/error states are mutually exclusive.
- [ ] Configuration changes cannot corrupt an active run.
- [ ] No `ClippyAI` fixed widths, negative margins, task names, prompts, or UI constants are copied.

## Recipe 8: Settings Center

| Field | Guidance |
| --- | --- |
| 来源项目 | `Netor.Cartana`, `ClippyAI` |
| 关键文件 | `Src/Netor.Cortana.UI/Views/SettingsWindow.axaml`, `ClippyAI/Views/ConfigurationDialog.axaml`, `ClippyAI/ViewModels/ConfigurationDialogViewModel.cs` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/ContentControl.cs`, `frameworks/Avalonia/src/Avalonia.Controls/ListBox.cs`, `frameworks/Avalonia/src/Avalonia.Controls/TabControl.cs`, `frameworks/Avalonia/src/Avalonia.Controls/ScrollViewer.cs` |
| 交互状态 | category selected, dirty form, validation error, save, reset, provider test, secret edited |
| 失败态 | invalid endpoint, missing secret, failed provider test, read-only config, save conflict |
| 可访问性/焦点风险 | validation summary and category changes must be screen-reader discoverable |
| 多屏/平台差异风险 | settings window sizing and modal ownership must respect current owner window |

验收清单：

- [ ] Settings categories match product mental model, not project reference naming.
- [ ] Dirty state and save/cancel semantics are explicit.
- [ ] Secrets are masked and never written to eval output.
- [ ] Long setting pages are scrollable without nested card clutter.
- [ ] No third-party labels, section order, or storage schema are copied.

## Recipe 9: Diagnostics and Performance Overlay

| Field | Guidance |
| --- | --- |
| 来源项目 | `mnemo`, `Netor.Cartana` |
| 关键文件 | `Mnemo.UI/Services/PerfDiagnosticsService.cs`, `Mnemo.UI/Services/PerfDiagnosticsScope.cs`, `Mnemo.UI/Components/Overlays/PerfDiagnosticsOverlay.axaml`, `Mnemo.UI/Modules/Chat/Views/ChatView.axaml`, `Mnemo.UI/Services/AiAssistantToolHost.cs`, `Src/Netor.Cortana.UI/Controls/RealtimeProcessCard.axaml` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/ItemsRepeater`, `frameworks/Avalonia/src/Avalonia.Controls/Primitives/Popup.cs`, `frameworks/Avalonia/src/Avalonia.Threading/DispatcherTimer.cs` |
| 交互状态 | diagnostics disabled, enabled, startup timings buffered, overlay opened, report refreshed, memory snapshot captured, chat list virtualized, AI tools loaded/unloaded |
| 失败态 | diagnostics unavailable, overlay owner closed, report empty, memory metric unavailable, tool load failed, long chat list jank |
| 可访问性/焦点风险 | diagnostics overlay must not steal focus from active text entry unless explicitly opened; report text should be selectable and readable |
| 多屏/平台差异风险 | process memory metrics and console/log output can vary by platform and sandbox |

验收清单：

- [ ] Diagnostics collection is service-owned and opt-in except safe startup buffering.
- [ ] Overlay is read-only, refreshable, and closeable without disrupting the active task.
- [ ] Chat/message surfaces with large histories use virtualization or equivalent load-shedding.
- [ ] AI tool registration has enable/disable cleanup and failure rollback.
- [ ] No `mnemo` metric names, report format, overlay layout, ring buffer constants, or tool registration code are copied.

## Recipe 10: Multi-Agent Workflow and HITL Workspace

| Field | Guidance |
| --- | --- |
| 来源项目 | `Netor.Cartana` |
| 关键文件 | `Src/Netor.Cortana.UI/Views/Workspace/WorkspaceTab.axaml`, `Src/Netor.Cortana.UI/ViewModels/Workspace/WorkflowTaskListVm.cs`, `Src/Netor.Cortana.UI/ViewModels/Workspace/WorkflowTaskApprovalVm.cs`, `Src/Netor.Cortana.AI/Workflow/*`, `Src/Netor.Cortana.Entitys/Entities/OrchestrationTaskEntity.cs`, `Src/Netor.Cortana.Networks/WebSockets/*PluginBus*` |
| Avalonia 12 源码验证点 | `frameworks/Avalonia/src/Avalonia.Controls/ContentControl.cs`, `frameworks/Avalonia/src/Avalonia.Controls/ItemsControl.cs`, `frameworks/Avalonia/src/Avalonia.Controls/ScrollViewer.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Button.cs` |
| 交互状态 | task list empty, task selected, steps streaming, paused for approval, approved, revision requested, rejected/cancelled, completed, failed |
| 失败态 | stale HITL request, checkpoint load failed, workflow executor unavailable, PluginBus disconnected, task title generation failed |
| 可访问性/焦点风险 | approval card must announce blocking state and return focus after approve/reject/revise |
| 多屏/平台差异风险 | long-running workflow notifications and window activation differ by desktop platform |

验收清单：

- [ ] Task list, detail, steps, approval, executor, checkpoint, and event transport are separate responsibilities.
- [ ] HITL actions are idempotent and guard against stale request IDs.
- [ ] Realtime process cards are presentation-only and do not own orchestration.
- [ ] Failure and cancellation states are visible in both task list and detail.
- [ ] No `Netor.Cartana` workflow protocol, entity schema, PluginBus message fields, styles, or button text are copied.

## Cross-Cutting Copy-Risk Scan

Run this as a review checklist before committing AI desktop guidance:

- [ ] No copied XAML element tree from `mnemo`, `Netor.Cartana`, or `ClippyAI`.
- [ ] No copied C# class body, method body, generated plugin code, notification backend, or platform implementation.
- [ ] No copied resource keys, brush names, animation names, icon assets, string literals, prompt text, plugin manifest schema, or model/provider names.
- [ ] Third-party file paths appear only as evidence citations.
- [ ] Every implementation suggestion maps back to Avalonia 12 source facts or plugin-owned design decisions.
