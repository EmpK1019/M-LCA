⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用自动更新所需文件；GitHub 的 Source code 归档才是源码。
Choose the installer for your system. Other assets support in-app updates.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | [M-LCA-Installer-0.18.1-arm64.dmg ↓](https://github.com/EmpK1019/M-LCA/releases/download/v0.18.1/M-LCA-Installer-0.18.1-arm64.dmg) |
| 🪟 Windows (x64) | [M-LCA-Setup-0.18.1.exe ↓](https://github.com/EmpK1019/M-LCA/releases/download/v0.18.1/M-LCA-Setup-0.18.1.exe) |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个热修复解决 v0.18.0 正式安装版中执行中指令组件反复堆叠的问题。审批、指令队列与用户问答现在拥有稳定且互不冲突的界面身份，不会再因生产环境更新而残留大量重复的“正在提交”条目。

同时收紧了同一会话的提交与结算路径。连续按下 Enter 或在会话状态变化期间补充要求，只会产生一条排队指令；Engine 确认后组件会正确更新并清除。

---

### 更新内容 / What's New

🧩 **执行中组件稳定性** — 修复审批、指令队列和用户问答组件身份冲突造成的重复堆叠。

📥 **排队指令幂等提交** — 同一会话提交期间阻止重复发送，并按指令 ID 去重显示。

✅ **提交状态结算** — 会话范围变化时仍能正确完成或标记未确认的本地排队状态，避免长期停留在“正在提交”。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
