### 下载 / Download

点击对应系统的链接下载安装。页面上的其它文件是 GitHub 自动生成的源码包，可以忽略。
Click your system's link to download. Other files on this page are auto-generated source archives; you can ignore them.

| 系统 System | 下载 Download |
|---|---|
| macOS (Apple Silicon) | M-LCA-Installer-0.14.0-arm64.dmg |
| Windows (x64) | M-LCA-Setup-0.14.0.exe |

macOS: 如果提示无法打开，在终端运行 `xattr -cr /Applications/M-LCA.app` 后再双击。
Windows: 如果 SmartScreen 拦截，点击“更多信息”，再选择“仍要运行”。

---

### 发版级别判断

- 上一正式发版为 `0.13.2`。
- 本轮不只是修复问题，还把 Cowork 子智能体升级为可并列打开、可独立继续对话、可查看指令/工具/进度/背景信息的完整工作面板。
- 同时包含较大范围 UI 调整、IPC 能力扩展、权限与模型选择继承、思考过程时间线持久化，因此按规则属于 `minor`，版本号定为 `0.14.0`。

---

### 本版重点 / Highlights

0.14.0 主要解决 Cowork 子智能体“看不见、等不稳、接不上”的问题。之前主会话派发子智能体后，用户只能看到零散工具调用，很多时候不知道它到底有没有启动、在想什么、卡在哪里；现在子智能体会出现在右侧列表里，点开就是独立面板，可以看到主 agent 指令、公开进度、工具记录和最终结果。

这版也把子智能体补成真正能继续协作的会话。它有自己的输入框、附件、模型选择、权限控制和背景信息窗口，默认跟随主会话设置，但上下文和历史独立保存。也就是说，子智能体不再只是后台跑完即结束的任务，而是可以被打开、追问、检查和恢复的工作线程。

稳定性也做了收口：默认隔离模式切回线程，进程模式保留为显式选项；等待窗口恢复到至少 300 秒；权限请求可以正确回到子面板处理；显式“派发多个智能体”的请求不会再被外层 planner 二次拆分，避免任务完成后又重复跑一轮。

---

### 更新内容 / What's New

🧠 **子智能体并列面板** — Cowork 右侧新增子智能体列表，支持打开独立面板查看角色、状态、主 agent 指令、工具步骤和结果。

🧵 **子智能体独立对话** — 新增 `subagent.message` 通道，子智能体支持继续提问、附件、模型选择、权限控制和独立背景信息。

👀 **思考过程实时化** — 思考进度和工具卡片按时间线穿插展示，并随会话持久化，刷新后不再退化成一条汇总文本。

🛠 **长任务稳定性修复** — `wait_subagent` 单次等待至少 300 秒，subagent 默认使用线程隔离，避免进程启动无响应、假超时和长研究任务被误杀。

🔐 **权限与模型继承** — subagent 继承主会话模型/路由/权限策略，审批请求可在子面板正确处理，不再错误超时或回错会话。

🧩 **避免重复派发** — 当用户明确要求“派发/调用多个智能体”时，Cowork 跳过外层任务拆分，防止首轮已完成后又执行第二轮。

🎛 **Cowork UI 统一** — 主会话和子智能体输入框、发送按钮、复制按钮、右侧模块标题和布局间距统一，子智能体面板支持拖拽调整宽度。

🧹 **Skill 分发整理** — 市场 skill 继续保持在线市场分发，本次安装包不预装 `marketplace/skills` 下的市场技能；运行时技能索引同步清理旧来源。

---

### 验证 / Verification

- `python -m unittest engine.tests.test_cowork_service`
- `python -m unittest engine.tests.test_subagent_isolation`
- `python -m unittest engine.tests.test_approval_service`
- `python -m unittest engine.tests.test_agent_tools_search`
- `python -m unittest engine.tests.test_agent_tools_safety`
- `python -m unittest engine.tests.test_agent_runtime`
- `python -m py_compile engine\application\subagent_worker.py engine\application\subagent_service.py engine\application\subagent_registry.py engine\application\agent_tools.py engine\application\approval_service.py engine\application\cowork_service.py`
- `npm run sync:ipc-schema`
- `npm run build:main`
- `npm run build:preload`
- `npm run typecheck:renderer`
- `npm run build:renderer`
- `npm run test:renderer -- store-session-repair.test.ts store-session-ordering.test.ts`

---

### 平台 / Platforms

- macOS arm64 (Apple Silicon)，暂未完成 Apple 公证
- Windows x64，暂未代码签名
