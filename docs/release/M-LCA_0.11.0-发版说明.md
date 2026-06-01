⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.11.0-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.11.0.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个版本完成了 Cowork 架构改造的全部三个阶段。上一版（0.10.1）引入了全局记忆系统，但 Agent 的实际工作能力还很有限——不能读写自己产出的文件，不能中断失控的任务，多轮对话时会忘记上一轮用了什么工具。这些问题在 0.11.0 里一次性解决了。

Phase 1 让 Agent 有了完整的文件操作能力（读、写、搜索、编辑）和跨轮次的工具调用记忆。Phase 2 让系统变得更聪明——简单问题不再浪费时间做规划，记忆按相关性筛选而非全量灌入，Cowork 模式接入了 Skill 体系。Phase 3 是底层架构升级：子 Agent 跑在独立进程里不会拖垮主进程，用户可以随时中断任务，新增了原生 Anthropic API 通道为后续接入 Claude 高级能力铺路，还加了完整的运行时审计和指标系统。

另外新建了 20 条自动化回归测试用例，确保后续迭代不会悄悄打破已有功能。

---

### 更新内容 / What's New

🔧 **文件系统四件套** — Agent 现在能读取、编辑、搜索、列出自己产出的文件，不再需要用户手动复制粘贴内容

🧠 **多轮工具记忆** — 跨轮对话时 Agent 能看到上一轮调用了哪些工具、结果是什么，不再重复搜索已有的信息

⚡ **Planning 自适应** — 简单问题直接回答，不再每次都走一遍 LLM 规划流程，响应速度提升 1-2 秒

🎯 **记忆相关性筛选** — 记忆不再全量注入 prompt，按用户消息关键词筛选相关条目，减少噪音

🔌 **Skill 体系接入** — Cowork 模式能感知并激活已安装的 contextual skill，自动注入专业领域指令

🏗️ **子 Agent 进程隔离** — 子 Agent 在独立进程中运行，崩溃或死循环不会拖垮主进程

⏹️ **任务中断与超时** — 用户可随时取消正在运行的任务，工具调用有超时保护，总任务有预算上限

🌐 **原生 Anthropic API** — 新增直连 Anthropic Messages API 的通道，零额外依赖，支持流式和 tool_use

📊 **运行时审计** — 结构化事件记录、聚合指标、会话回放导出，为后续可观测性打基础

🧪 **回归测试框架** — 20 条标准化用例 + 自动断言 + 版本基线对比，防止迭代回归

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
