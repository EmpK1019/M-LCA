⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.8.4-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.8.4.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个版本集中解决了 Subagent 系统的稳定性问题。之前 researcher 在执行大量搜索时会超时，根因是工具结果无限堆积导致每次 LLM 调用的输入 token 线性增长。更严重的是，subagent 拿到了 `invoke_subagent` 工具后会递归嵌套自己，直接死锁。这两个问题现在都修了。

另外修复了 subagent 内工具调用报"没有活动会话"、生成文件不出现在聊天中、步骤串入主 agent 列表等一系列问题。Subagent 面板的交互也做了打磨——header 固定、自动滚动到底、滚动条样式统一。

---

### 更新内容 / What's New

🐛 **修复 subagent 递归死锁** — subagent 不再能调用 `invoke_subagent`，消除了递归嵌套导致的无限等待

🐛 **修复 subagent 工具调用崩溃** — subagent 内的 `run_generated_script` / `render_pptx` 不再报"当前没有活动会话"

🐛 **修复 subagent 生成文件不显示** — subagent 产出的文件现在正确出现在聊天中

🐛 **修复 subagent 步骤串入主列表** — subagent 的搜索步骤不再混入主 agent 的思考面板

🐛 **修复 skill 创建时崩溃** — 指令文本中包含 None 元素时不再抛异常

⚡ **Memory microcompaction** — 冷区大体积工具结果自动压缩为占位符，防止 token 数线性增长导致超时

🎨 **Subagent 面板交互优化** — header 固定不滚动、新步骤自动滚到底、滚动条样式统一、入场动画禁用

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
