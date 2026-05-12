⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.8.2-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.8.2.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个版本主要解决了两个一直存在的隐患：对话记忆的处理方式，和附件预览的可用性。

之前对话历史超出限制时，旧消息会被直接删掉。这意味着你在前面说过的内容、AI 给出的分析结论，可能在你不知情的情况下消失了。这版改成了真正的压缩：超过上限时，AI 会先把旧对话总结成一段摘要，用摘要替换原始消息，信息有损但不会完全丢失。同时上下文窗口从 32k 扩大到 256k，大多数情况下根本不会触发压缩。

附件预览之前有个问题：Word 和 Excel 文件打开后内容超出一屏就没法滚动，只能看到第一屏。这版修了这个问题，现在可以正常滚动浏览全部内容。图片附件也去掉了 8 MB 的大小限制。

---

### 更新内容 / What's New

🧠 **对话上下文扩容** — 从 32k 扩大到 256k tokens，长对话不再频繁触发历史裁剪。

📝 **真正的对话压缩** — 历史超限时改为 LLM 摘要压缩，替代原来的直接删除，关键信息不再无声消失。

📎 **附件预览可滚动** — 修复 Word、Excel、HTML 预览面板无法滚动的问题，现在可以浏览完整内容。

🖼 **图片附件无大小限制** — 移除 8 MB 上传限制，大图可以直接发送。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
