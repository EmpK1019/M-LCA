⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.12.0-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.12.0.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这一版让 Cowork 真正成为一个"工作模式"。在此之前，Cowork 的 Agent 只能在受限的输出目录里折腾自己产出的文件，碰不到你电脑上真实的项目。0.12.0 引入了**项目工作空间**：选一个本地文件夹，Agent 就在里面干活——读现有文件、改它们、新建、删除（写操作都走审批确认），侧边有文件树看得见它动了哪些文件，还会自动读取项目根的 `CLAUDE.md` / `AGENTS.md` 当作项目规矩。一个项目下可以挂多个会话，会话按项目归类；也允许不绑定任何项目的会话存在。这套设计对齐了 Claude Code 的心智模型。

同时把 0.11.0 留下的"建好了但没接通"的能力补齐了：停止按钮过去是假的，点了停不下正在跑的任务——现在中断信号注入到了 Agent 执行循环的每一步，真能停；工具的完整输出、运行时指标抽屉也都接到了前端。

稳定性上做了一批硬修复：多会话并行时工具串台、切换会话丢失执行步骤的问题修好了；执行步骤现在作为永久消息留在对话里，切走再回来原样还在；建模导出的三张表模板从易丢的外部 xlsx 改为内置 JSON，彻底融进软件不会再丢；模型路由收敛为两个对等可切换的槽。

---

### 更新内容 / What's New

🗂️ **Cowork 项目工作空间** — 选本地文件夹作为工作目录，Agent 在其中读 / 改 / 建 / 删文件（写走审批），不再局限于沙箱输出目录

🌲 **文件树面板 + 会话按项目分类** — 侧栏展示项目文件树并高亮 Agent 改动；会话按所属项目归类，「无项目」会话也能独立存在

📋 **项目指令自动注入** — 项目根的 `CLAUDE.md` / `AGENTS.md` 自动作为上下文注入，Agent 上来就懂项目规矩

⏹️ **真·停止按钮** — 中断信号接入 Agent 执行循环的每一步，连续多轮工具调用 / 长回复都能在下一步边界即停，不再是摆设

🧵 **多会话并发修复** — 修复并行会话间工具串台、切换会话丢失已生成执行步骤的问题，多开会话互不干扰

💬 **执行步骤永存化** — 思考过程与执行步骤作为永久消息留在对话里，切走再回来、重启后原样还在，不再消失或串显

📑 **建模导出模板内置化** — 三张业务表结构固化为内置 JSON，不再依赖易丢的外部 xlsx 模板，列结构对齐真实填表文件

🔀 **路由模型简化** — 收敛为主 / 备用两个对等独立路由槽，各自可切 OpenAI / Anthropic，用户选哪个模型就只走对应路由

📊 **运行时指标抽屉** — 工具调用次数、Token 消耗、平均延迟、会话回放导出，P3.4 审计能力终于有了入口

🛡️ **脚本执行加固** — `run_generated_script` 默认超时收紧、注入网络超时、Windows 进程树终止，错误脚本不再让会话假死

🗓️ **对话记录「昨天」分组** — 时间分类新增「昨天」，会话列表更清晰

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
