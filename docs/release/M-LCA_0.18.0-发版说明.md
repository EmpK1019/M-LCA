⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用自动更新所需文件；GitHub 的 Source code 归档才是源码。
Choose the installer for your system. Other assets support in-app updates.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | [M-LCA-Installer-0.18.0-arm64.dmg ↓](https://github.com/EmpK1019/M-LCA/releases/download/v0.18.0/M-LCA-Installer-0.18.0-arm64.dmg) |
| 🪟 Windows (x64) | [M-LCA-Setup-0.18.0.exe ↓](https://github.com/EmpK1019/M-LCA/releases/download/v0.18.0/M-LCA-Setup-0.18.0.exe) |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这次我们集中完善了 Cowork 的执行中交互。追加要求先进入队列，需要立即调整当前任务时再选择“调整方向”；持续目标、队列和输入区各自保留明确的状态，避免补充一句要求就打断整个目标。

当任务缺少必要信息时，助手可以直接发起问答。你可以选择选项、补充文字或跳过，回答会返回正在等待的工具调用，而不是另开一个聊天任务。界面继续沿用 M-LCA 的全局深浅主题，不改变 Modeling 的建模优先流程。

---

### 更新内容 / What's New

💬 **用户问答** — 支持单选、多选、自由回答与跳过，关闭时明确取消等待；回答持久化后才继续，过期运行的问题不能误投到新任务。

📥 **执行中指令队列** — 默认排队，支持编辑、删除和调整方向；多行编辑保留附件，提供文件卡片、受限本地图片缩略图和附件预览入口。

🎯 **Cowork Goal** — 支持查看轮次与步骤、向上展开编辑及明确的完成状态；改善后台刷新、切换会话与补充指令期间的状态处理。Modeling 模式不引入 Goal。

⌨️ **会话命令** — 指令与 Skills 分组显示，支持目标、模型、权限、日志导出与手动上下文压缩；未知命令不会静默发送为普通消息。

🗂️ **会话维护** — 日志 ZIP 导出不包含附件正文或私密推理；手动压缩保留原会话记录，提供运行、取消及结果未确认状态。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
