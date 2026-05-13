⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.8.3-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.8.3.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个版本对 Subagent 面板做了一轮视觉打磨。之前面板的滚动条会出现在对话历史框的右侧，看起来像是属于整个对话区域，实际上它只属于 Subagent 面板自己。这版修正了这个问题，滚动条现在正确地显示在面板容器内部。

同时调整了面板卡片的整体观感：圆角更大、展开箭头居中对齐并改为主题绿色、关闭按钮独立在右侧、胶囊底色和间距也做了优化，整体更清晰。

---

### 更新内容 / What's New

🔧 **Subagent 面板滚动条位置修正** — 滚动条不再出现在对话历史框右侧，现在正确显示在 Subagent 面板容器内部。

🎨 **Subagent 面板视觉优化** — 卡片圆角加大、展开箭头居中并改为主题绿色、关闭按钮独立布局、胶囊底色和间距调整，整体更清晰易读。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
