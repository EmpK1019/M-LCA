⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用自动更新所需文件；GitHub 的 Source code 归档才是源码。
Choose the installer for your system. Other assets support in-app updates.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | [M-LCA-Installer-0.18.2-arm64.dmg ↓](https://github.com/EmpK1019/M-LCA/releases/download/v0.18.2/M-LCA-Installer-0.18.2-arm64.dmg) |
| 🪟 Windows (x64) | [M-LCA-Setup-0.18.2.exe ↓](https://github.com/EmpK1019/M-LCA/releases/download/v0.18.2/M-LCA-Setup-0.18.2.exe) |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个版本修复了长任务持续工作却在十分钟后被强制停止的问题。Cowork 现在按“连续无进展”判断超时：模型输出、步骤变化和工具执行都会续期，不再设置整轮任务的绝对时长上限；真正停滞的任务仍会自动结束，手动停止和单项工具超时也保持有效。

同时补齐了生成文件的统一成果登记。只要工具确实在受控输出目录中生成了文件，即使走的是通用写入或命令工具，也会形成可点击的消息文件卡片并同步到右侧“输出成果”。重启恢复中的重复 prompt、错误时间，以及执行中指令条不自然的“等待接收”提示也一并修正。

---

### 更新内容 / What's New

⏱️ **持续进展续期** — 将固定十分钟整轮上限改为连续十分钟无进展超时，长研究和多工具任务不再被误杀。

📄 **成果文件统一登记** — 为所有 agent 工具增加安全的成果发现兜底，恢复聊天文件卡片和右侧可点击成果列表。

🔄 **会话恢复稳定性** — 统一 Engine 秒时间戳与前端毫秒时间戳，修复重启后 prompt 重复及错误时间显示。

📨 **执行中指令反馈** — 移除不协调的队列字符图标，并以“发送/已发送”呈现补充指令，内部仍在安全步骤边界消费。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
