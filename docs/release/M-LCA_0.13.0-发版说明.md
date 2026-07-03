### 下载 / Download

点击对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。Click your system's link to download. Other files on this page are auto-generated source archives; ignore them.

| 系统 System | 下载 Download |
|---|---|
| macOS (Apple Silicon) | M-LCA-Installer-0.13.0-arm64.dmg ↓ |
| Windows (x64) | M-LCA-Setup-0.13.0.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？“更多信息 → 仍要运行”。SmartScreen blocking? "More info → Run anyway."

---

这一版重点补齐 Cowork 的编程执行能力和运行时稳定性：Agent 现在能更像 IDE 一样先理解工作区、读取和搜索代码、应用补丁、运行命令与测试，并能检查 Python、Node、Java/JDK、Git 等核心运行环境。针对之前“任务超时、脚本卡住、涉及 py/js/java 不稳”的问题，这一版加入了更完整的诊断、自检和进程清理链路。

同时，MCP、Plugin、Skill 的安装、审计和配置链路继续增强。模型可以查看已安装 MCP/Plugin 能力、按审批策略配置 MCP，安装 GitHub Plugin，并兼容更多 Codex/Claude 风格的插件、技能、hooks 和 MCP 配置格式。界面侧也修复了 Cowork 分组、归档、停止按钮、侧栏操作和设置页的一批细节。

---

### 更新内容 / What's New

🔧 **Cowork 编程能力增强** — 新增和完善工作区上下文、文件读取、目录树、代码搜索、Git 状态、补丁应用、受控 Shell 命令、项目资料解析等工具。Agent 可以先读项目结构，再修改代码，最后运行测试和查看 diff/status，减少静态界面、半截文件和无验证交付。

🧪 **IDE Runtime 诊断与冒烟测试** — 新增 IDE 能力诊断和真实冒烟测试，覆盖 Python、Node/JavaScript、Java/JDK、Git、补丁应用、测试运行和 diff 校验。Java/JDK 支持用户级 Temurin OpenJDK 21 自动发现，并会注入到软件子进程环境中。

⏱️ **超时与停止链路更稳** — Shell 执行、脚本验证、任务停止、审批等待和子进程清理进一步收敛。长任务失败时会返回更明确的 stdout/stderr、退出码、超时标记和失败步骤，减少“看起来一直在思考但不知道卡在哪”的情况。

🧩 **MCP / Plugin / Skill 兼容性增强** — 支持审计已安装 MCP、配置 MCP、从 inline `mcpServers` 导入配置、安装 GitHub Plugin、同步插件内置 Skill/MCP、解析 plugin app 映射、加载 hooks，并兼容 `.codex-plugin`、`.claude/skills`、`.codex/skills` 等常见仓库布局。

🔒 **MCP 安全与并发修复** — MCP 工具审批模式按配置生效，命令行参数摘要脱敏；同一 MCP server 的并发调用会串行化，减少 session 复用导致的协议交错、卡顿和上下文污染。

🗂️ **Cowork 项目与会话体验** — Cowork 首页支持选择项目归属，本地项目可从列表移除但不删除磁盘文件；项目聊天分组、待处理会话分组、归档会话筛选和历史恢复更清晰。

🎛️ **界面细节修复** — 侧栏图标、滚动条、设置页、定时任务控件、输入框发送/停止按钮等视觉和交互细节做了统一。停止按钮恢复为醒目的红色状态，运行时更容易识别。

---

### 验证 / Verification

- Focused IDE/runtime suite: 125 tests passed across agent runtime, agent tools, registry, generated artifact service, and IPC schema.
- Generated artifact / IPC checks: 46 tests passed.
- Real IDE smoke check passed: Python unittest, Node test, Java compile/run, Git diff/status, and cleanup.
- Dependency check passed after installing required agent packages.

---

### 平台 / Platforms

- **macOS** - arm64 (Apple Silicon)，暂未完成 Apple 公证
- **Windows** - x64，暂未代码签名
