# Avalonia 12 AI Desktop Product Patterns

本文件把 `docs/reference/ai-desktop-projects.md` 中允许作为默认参考的三个 Avalonia 12 AI 桌面项目沉淀为插件经验库。它只提炼产品架构、交互组织和工程边界，不复制也不得照搬 third-party 项目代码、样式、资源、命名或实现细节。

执行层 recipes、验收清单和 eval 记录入口见 `references/74-avalonia-12-ai-desktop-recipes-and-checklists.md` 与 `evals/avalonia-12-ai-desktop-eval-checklist.md`。

## Evidence Boundary

- 默认参考项目只能是 `mnemo`、`Netor.Cartana`、`ClippyAI`。
- `Everywhere`、`StabilityMatrix`、`avallama`、`WhisperVoiceInput` 只可作为 Avalonia 11.x 迁移对比或产品灵感，不得进入默认 Avalonia 12 API/XAML 建议。
- API、控件、平台服务、主题行为和 XAML 语义必须回到 `/Volumes/程序开发/Du-Framework/Du.Ingest/frameworks/Avalonia` 验证。
- 第三方项目的 XAML/C# 只能作为模式证据；回答或实现时不得复制代码、控件模板、资源字典、图标、字符串或布局常量。

## Source Project Coverage

| Project | Role | Key files read for patterns | Main use |
| --- | --- | --- | --- |
| `mnemo` | 主参考 | `Mnemo.UI/Views/MainWindow.axaml`, `Mnemo.UI/ViewModels/MainWindowViewModel.cs`, `Mnemo.UI/Components/Sidebar/Sidebar.axaml`, `Mnemo.UI/Components/RightSidebar/RightSidebar.axaml`, `Mnemo.UI/Components/OverlayPopupHost.axaml`, `Mnemo.UI/Services/OverlayService.cs`, `Mnemo.UI/Components/ToastHost.axaml`, `Mnemo.UI/Services/ToastService.cs`, `Mnemo.UI/Services/AiAssistantToolHost.cs`, `Mnemo.UI/Components/Overlays/PerfDiagnosticsOverlay.axaml`, `Mnemo.UI/Services/PerfDiagnosticsService.cs`, `Mnemo.UI/Modules/Chat/Views/ChatView.axaml` | 复杂 AI 工作台、左导航、中央工作区、右侧助手、覆盖层、toast、AI tool gating、聊天虚拟化、性能诊断 overlay、主题资源组织。 |
| `Netor.Cartana` | 辅助参考 | `Src/Netor.Cortana.UI/Views/MainWindow.axaml`, `Src/Netor.Cortana.UI/Views/MainWindow.axaml.cs`, `Src/Netor.Cortana.UI/Views/SettingsWindow.axaml`, `Src/Netor.Cortana.UI/Controls/ChatHistoryPanel.axaml`, `Src/Netor.Cortana.UI/Controls/WorkspaceExplorer.axaml`, `Src/Netor.Cortana.UI/Views/FloatWindow.axaml`, `Src/Netor.Cortana.UI/Views/BubbleWindow.axaml`, `Src/Netor.Cortana.UI/Styles/DesignTokens.axaml`, `Src/Netor.Cortana.UI/Styles/SharedStyles.axaml`, `Src/Netor.Cortana.UI/Controls/EmptyState.axaml`, `Src/Netor.Cortana.UI/Controls/RealtimeProcessCard.axaml`, `Src/Netor.Cortana.UI/Views/Workspace/WorkspaceTab.axaml`, `Src/Netor.Cortana.UI/Providers/PluginManagementProvider.cs`, `Src/Netor.Cortana.Plugin/Core/PluginManifest.cs`, `Src/Netor.Cortana.Plugin/PluginLoader.cs`, `Plugins/docs/参考文档/plugin-mcp.md`, `Plugins/docs/参考文档/native-plugin-dev-guide.md` | 中文 AI 助手、抽屉面板、设置中心、悬浮入口、字幕气泡、设计 token、空状态、实时过程卡片、多智能体工作台、插件/MCP 配置信息架构。 |
| `ClippyAI` | 局部参考 | `ClippyAI/App.axaml.cs`, `ClippyAI/Views/MainWindow.axaml`, `ClippyAI/Views/MainWindow.axaml.cs`, `ClippyAI/Views/MainView.axaml`, `ClippyAI/ViewModels/MainViewModel.cs`, `ClippyAI/Views/ConfigurationDialog.axaml`, `ClippyAI/ViewModels/ConfigurationDialogViewModel.cs`, `Libs/DesktopNotificationsNet8/DesktopNotifications.Avalonia/AppBuilderExtensions.cs`, `Libs/DesktopNotificationsNet8/*` | 剪贴板小工具、置顶小窗、托盘显隐、任务配置、跨平台通知封装。 |

## Workbench Architecture

- 来源项目：`mnemo` 的 `Mnemo.UI/Views/MainWindow.axaml` 与 `MainWindowViewModel.cs`。
- 经验：AI 工作台应把 shell 视作组合根，典型结构是左导航、顶部命令区、中央 `ContentControl` 工作区、右侧 AI 助手和 window-level overlay/toast 层。主窗口只编排区域和服务，不承载业务流程。
- 新增证据：`Netor.Cartana` 的 `WorkspaceTab.axaml` 与 `ViewModels/Workspace/*` 展示了多智能体任务列表、任务详情、步骤流和 HITL 批准卡片如何进入工作台；它适合提炼任务工作区信息架构，不适合复制内联样式或事件处理。
- 适用场景：需要模块导航、复杂工作区、AI 助手并存的生产力桌面应用。
- 不可照搬风险：不要复制 `mnemo` 的列宽、资源键、组件命名、快捷键和视觉常量；也不要把它的服务聚合方式当成唯一 MVVM 结构。
- Avalonia 12 源码验证点：`src/Avalonia.Controls/ContentControl.cs`, `src/Avalonia.Controls/SplitView/SplitView.cs`, `src/Avalonia.Controls/Grid.cs`, `src/Avalonia.Controls/TopLevel.cs`。

## AI Assistant Interaction

- 来源项目：`mnemo` 的 `RightSidebar.axaml` / `RightSidebarViewModel.cs` / `AiAssistantToolHost.cs`，`Netor.Cartana` 的 `MainWindow.axaml` / `MainWindow.axaml.cs`。
- 经验：AI 助手不只是聊天框，应包含模式选择、模型/路由提示、流式状态、停止生成、新建会话、建议操作、附件/文件引用、历史入口和可恢复的折叠状态。
- 新增证据：`mnemo` 将 AI tool / skill 注册延迟到 `AI.EnableAssistant` 开启后，并在关闭时卸载，适合提炼“功能门控 + 延迟加载 + 禁用清理”的助手能力边界。
- 适用场景：侧栏助手、窄窗口助手、中央聊天应用、带工作区上下文的 Copilot 体验。
- 不可照搬风险：不要复制第三方 prompt、agent 列表、快捷词、分段 code-behind 或聊天消息模板；应按目标产品重新定义交互契约和状态机。
- Avalonia 12 源码验证点：`src/Avalonia.Controls/TextBox.cs`, `src/Avalonia.Controls/Button.cs`, `src/Avalonia.Controls/ItemsControl.cs`, `src/Avalonia.Controls/Presenters/ItemsPresenter.cs`, `src/Avalonia.Base/Input/Platform/IClipboard.cs`。

## Plugins and Settings Center

- 来源项目：`Netor.Cartana` 的 `SettingsWindow.axaml`, `PluginManagementProvider.cs`, `PluginManifest.cs`, `PluginLoader.cs`, `Plugins/docs/参考文档/plugin-mcp.md`, `Plugins/docs/参考文档/native-plugin-dev-guide.md`, `Src/Netor.Cortana.Networks/WebSockets/*PluginBus*`。
- 经验：AI 桌面插件中心应把系统设置、模型供应商、智能体、MCP 服务、工具、插件授权和运行时状态分组；插件加载、卸载、热更新和 MCP 配置应有显式状态、权限边界和故障反馈。
- 新增证据：`Netor.Cartana` 的 PluginBus / WebSocket 重构说明插件通信、会话历史、memory supply、model capability 和 workflow history 可以统一进事件总线；插件协议只能提炼“统一通道 + 能力声明 + 诊断反馈”的架构模式。
- 适用场景：需要外部工具、MCP server、native/process 插件、模型供应商和用户可配置能力的 AI 桌面应用。
- 不可照搬风险：不要复制 `Netor.Cartana` 的插件协议、包名、Native AOT generator 约束或配置字段；插件协议必须按目标宿主的安全模型、版本兼容和审计要求重新设计。
- Avalonia 12 源码验证点：设置 UI 回到 `src/Avalonia.Controls/TabControl.cs`, `src/Avalonia.Controls/ListBox.cs`, `src/Avalonia.Controls/ContentControl.cs`；文件/外部启动回到 `src/Avalonia.Base/Platform/Storage/IStorageProvider.cs` 与 `src/Avalonia.Base/Platform/Storage/ILauncher.cs`。

## Desktop Entry and Tray

- 来源项目：`ClippyAI` 的 `App.axaml.cs`, `MainWindow.axaml`, `MainWindow.axaml.cs`；`Netor.Cartana` 的 `FloatWindow.axaml`, `BubbleWindow.axaml`。
- 经验：桌面入口可以分为托盘显隐、悬浮球、透明置顶小窗、字幕/状态气泡。入口层应只负责显示、隐藏、定位、激活和关闭，不应直接承载 AI 任务逻辑。
- 适用场景：常驻助手、剪贴板工具、屏幕边缘工具条、桌面浮层、快速唤起入口。
- 不可照搬风险：不要复制固定屏幕位置、固定尺寸、Topmost 默认策略、轮询剪贴板或无可访问性语义的浮窗；这些容易造成多屏、焦点、隐私和输入体验问题。
- Avalonia 12 源码验证点：`src/Avalonia.Controls/TrayIcon.cs`, `src/Avalonia.Controls/NativeMenu.cs`, `src/Avalonia.Controls/Screens.cs`, `src/Avalonia.Controls/TopLevel.cs`, `src/Avalonia.Controls/Window.cs`。

## Overlays and Notifications

- 来源项目：`mnemo` 的 `OverlayPopupHost.axaml`, `OverlayService.cs`, `ToastHost.axaml`, `ToastService.cs`；`ClippyAI` 的 `Libs/DesktopNotificationsNet8/DesktopNotifications.Avalonia/AppBuilderExtensions.cs` 与平台 notification manager。
- 经验：覆盖层应作为 window-level host 管理 z-order、backdrop、alignment、关闭级联和 dialog completion；toast 应区分 timed/sticky/history，并通过可预测的队列和容量限制避免抖动。系统通知应包装成平台服务，而不是散落在 ViewModel。
- 新增证据：`mnemo` 的 `PerfDiagnosticsOverlay.axaml` 把启动计时、指标、内存快照和 ring buffer 报告作为可打开的 overlay，不需要散落到普通页面。
- 适用场景：确认对话、命令面板、AI 工具执行进度、任务通知、跨平台系统通知。
- 不可照搬风险：不要复制 overlay host 的内部集合类型、z-index 常量、toast 文案、notification library 代码或平台实现；应只提炼 host/service 分层。
- Avalonia 12 源码验证点：`src/Avalonia.Controls/Primitives/Popup.cs`, `src/Avalonia.Controls/Flyouts/PopupFlyoutBase.cs`, `src/Avalonia.Controls/Notifications/WindowNotificationManager.cs`, `src/Avalonia.Controls/Primitives/PopupRoot.cs`。

## Theme Tokens and Design System

- 来源项目：`mnemo` 的 shell、sidebar、right sidebar、toast 和 overlay XAML 资源使用；`Netor.Cartana` 的 `DesignTokens.axaml`、`SharedStyles.axaml`、`ThemeResources.axaml`、`EmptyState.axaml`、主窗口/设置/浮窗视觉分组；`ClippyAI` 的小工具紧凑界面。
- 经验：AI 桌面产品需要把 shell surface、panel surface、assistant surface、overlay surface、status/toast、focus、danger、accent、spacing、density 和 typography 变成可复用 token，而不是在每个页面硬编码颜色、尺寸和边距。
- 新增证据：`Netor.Cartana` 最新增量先抽出 spacing/radius/font/shadow tokens、共享 link button styles 和 empty state 控件，适合提炼“先治理 token/空状态/共享状态样式，再逐步迁移局部样式”的设计系统演进方式。
- 适用场景：工作台、设置中心、工具面板、插件列表、聊天消息、通知与浮窗需要统一视觉语言的应用。
- 不可照搬风险：不要复制任何第三方 brush key、资源字典、动画、图标或 palette；应建立目标产品自己的 token 名称和覆盖层级。
- Avalonia 12 源码验证点：`src/Avalonia.Base/Styling/ThemeVariant.cs`, `src/Avalonia.Controls/ThemeVariantScope.cs`, `src/Avalonia.Base/Styling/Style.cs`, `src/Avalonia.Base/Styling/ResourceInclude.cs`。

## View and ViewModel Organization

- 来源项目：`mnemo` 的 `MainWindowViewModel.cs`、sidebar/right-sidebar ViewModel、`PerfDiagnosticsService.cs`；`Netor.Cartana` 的 partial code-behind 分区、`ViewModels/Workspace/*`、workflow executor；`ClippyAI` 的 `MainViewModel.cs` 与 `ConfigurationDialogViewModel.cs`。
- 经验：复杂 AI 桌面应把 shell VM、navigation service、assistant VM、workspace VM、overlay service、toast service、platform services 分开；局部工具可以用单一 VM 管理任务状态，但仍需把平台能力和 AI 执行服务隔离。
- 新增证据：多智能体工作流要把 task list、task detail、step item、approval VM、workflow executor、checkpoint store 分层；实时过程卡片只展示过程状态，不直接驱动 orchestration。
- 适用场景：模块化页面、ViewLocator、动态工作区、配置对话框、小窗工具流。
- 不可照搬风险：不要把 `Netor.Cartana` 的大量命名控件和 partial code-behind 当作默认建议；它能说明行为分区，但默认插件建议仍应优先 MVVM、typed templates 和 source-backed Avalonia patterns。
- Avalonia 12 源码验证点：`src/Avalonia.Controls/Templates/DataTemplates.cs`, `src/Avalonia.Controls/Templates/IDataTemplate.cs`, `src/Avalonia.Controls/ContentControl.cs`, `src/Avalonia.Base/Data/Core/ExpressionObserver.cs`。

## Platform Service Isolation

- 来源项目：`ClippyAI` 的托盘、剪贴板、通知和屏幕定位；`Netor.Cartana` 的插件/MCP 外部进程与文件工作区；`mnemo` 的 overlay/toast services。
- 经验：托盘、剪贴板、通知、文件选择、外部启动、多屏定位、插件进程和 MCP 连接都应通过应用服务边界进入 ViewModel。ViewModel 消费抽象能力，Avalonia API 使用点集中在窗口、TopLevel 或平台服务 adapter。
- 适用场景：跨平台桌面、macOS/Windows/Linux 差异、多窗口、多屏、常驻后台、插件化 AI 工具。
- 不可照搬风险：不要复制平台 notification manager 或直接在业务 VM 中轮询系统资源；应先定义权限、生命周期、取消、错误处理和测试替身。
- Avalonia 12 源码验证点：`src/Avalonia.Base/Input/Platform/IClipboard.cs`, `src/Avalonia.Base/Platform/Storage/IStorageProvider.cs`, `src/Avalonia.Base/Platform/Storage/ILauncher.cs`, `src/Avalonia.Controls/Screens.cs`, `src/Avalonia.Controls/TopLevel.cs`。

## Diagnostics and Performance

- 来源项目：`mnemo` 的 `PerfDiagnosticsService.cs`, `PerfDiagnosticsScope.cs`, `PerfDiagnosticsOverlay.axaml`, `ChatView.axaml`, `AiAssistantToolHost.cs`；`Netor.Cartana` 的 `RealtimeProcessCard.axaml`。
- 经验：AI 桌面应用需要把性能诊断、启动耗时、memory snapshot、实时过程输出和工具注册状态变成可观察能力。诊断采集服务、overlay 展示和业务 UI 应分层；聊天长列表应优先考虑虚拟化；AI 工具注册应按设置延迟加载。
- 适用场景：启动慢、聊天消息多、overlay 多、插件多、模型工具多、需要开发者诊断入口的 AI 桌面应用。
- 不可照搬风险：不要复制第三方 ring buffer 大小、日志格式、overlay 模板、工具注册流程或实时卡片样式；应定义目标应用自己的指标、采样、隐私和展示策略。
- Avalonia 12 源码验证点：`src/Avalonia.Controls/ItemsRepeater`, `src/Avalonia.Controls/Primitives/Popup.cs`, `src/Avalonia.Controls/Notifications/WindowNotificationManager.cs`, `src/Avalonia.Threading/DispatcherTimer.cs`。

## Transferable Anti-Patterns

- 来源项目：三个项目的可迁移风险观察。
- 经验：
  - 不要把 Avalonia 11.x 项目作为默认 API/XAML 样板。
  - 不要复制第三方项目的 XAML、模板、资源、图标、字符串、插件协议或平台实现。
  - 不要用固定尺寸、负边距、单屏假设或默认 Topmost 作为通用桌面模式。
  - 不要让 Window code-behind 直接拥有 AI 会话、插件生命周期、MCP 连接或系统通知逻辑。
  - 不要把剪贴板/文件/屏幕/通知这类平台能力隐藏在普通 ViewModel 内部。
  - 不要把 overlay、toast、dialog、notification 混成一个控件；它们的生命周期和可访问性语义不同。
- 适用场景：新建 AI 桌面应用、评审开源参考迁移、插件化能力设计、旧代码重构。
- Avalonia 12 源码验证点：使用对应功能前回查本文件各章节列出的 `frameworks/Avalonia/src` 路径。

## Avalonia 12 Source Verification Points

使用本经验库给出实现建议前，至少按功能回查以下源码入口：

| Need | Avalonia 12 source path |
| --- | --- |
| Shell content host / module view | `frameworks/Avalonia/src/Avalonia.Controls/ContentControl.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Templates/DataTemplates.cs` |
| Split panels and workbench layout | `frameworks/Avalonia/src/Avalonia.Controls/SplitView/SplitView.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Grid.cs` |
| Window, top-level services, screen placement | `frameworks/Avalonia/src/Avalonia.Controls/TopLevel.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Window.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Screens.cs` |
| Tray and native menu | `frameworks/Avalonia/src/Avalonia.Controls/TrayIcon.cs`, `frameworks/Avalonia/src/Avalonia.Controls/NativeMenu.cs` |
| Popup, flyout, overlay | `frameworks/Avalonia/src/Avalonia.Controls/Primitives/Popup.cs`, `frameworks/Avalonia/src/Avalonia.Controls/Flyouts/PopupFlyoutBase.cs` |
| Managed notification | `frameworks/Avalonia/src/Avalonia.Controls/Notifications/WindowNotificationManager.cs` |
| Clipboard and data transfer | `frameworks/Avalonia/src/Avalonia.Base/Input/Platform/IClipboard.cs` |
| Storage and launcher | `frameworks/Avalonia/src/Avalonia.Base/Platform/Storage/IStorageProvider.cs`, `frameworks/Avalonia/src/Avalonia.Base/Platform/Storage/ILauncher.cs` |
| Theme variant and resources | `frameworks/Avalonia/src/Avalonia.Controls/ThemeVariantScope.cs`, `frameworks/Avalonia/src/Avalonia.Base/Styling/Style.cs` |

## No-Copy Rules

- 可以复用：信息架构、层次划分、职责边界、风险清单、验证路径、测试思路。
- 不得复制：第三方 XAML、C#、资源键、brush、模板、动画、插件协议、图标、字符串、布局常量、命名体系。
- 如果任务需要实现类似能力，应先用本文件提炼需求，再用 Avalonia 12 源码和本插件的专题 references 重新设计实现。
- 如果回答引用 `mnemo`、`Netor.Cartana` 或 `ClippyAI`，必须说明其只是 Avalonia 12 project patterns，不是 Avalonia 12 source facts。
