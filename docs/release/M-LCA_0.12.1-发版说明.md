⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.12.1-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.12.1.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

一个小而实在的体验修正：模型选择器的默认逻辑。

之前选择框在没手动选模型时，会显示一个写死的名字 `Default (claude-opus-4-6-max)`——它既不是引擎真正会调用的模型，版本也是旧的，让人对"现在到底在用哪个模型"产生误解。而且每次重启都回到这个含糊的默认，不记得你上次选了什么。

这一版对齐了 Cursor、Claude 这类多模型工具的通行做法：启动时如果你上次选过的模型还在，就恢复它；否则默认选中引擎实际配置的主模型，并按真实名字显示。你的选择会被记住，下次启动直接沿用。

---

### 更新内容 / What's New

🎯 **模型默认逻辑修正** — 默认按真实模型名显示（不再是写死的假名），启动时恢复上次选择，记不住改成记得住，所见即所用

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
