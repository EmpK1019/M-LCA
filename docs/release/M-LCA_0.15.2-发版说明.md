⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用自动更新所需文件；GitHub 另行显示的 Source code (zip/tar.gz) 才是源码归档。
Click your system's link to download. The `.yml`, `.zip`, and `.blockmap` files support in-app updates; GitHub's separately listed Source code (zip/tar.gz) entries are source archives.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.15.2-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.15.2.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

0.15.2 修复了两个会直接影响桌面端可信度的问题。首先，发布流程现在会明确把新版本设为 GitHub Latest，并在结束前反向校验 Latest 指针。这样旧客户端读取自动更新入口时，不会再因为 Release 已上传但 Latest 仍指向旧版本而误判“已是最新”。

其次，Windows 与 macOS 不再共用一套看起来完全相同的窗口控件。品牌保持在标题栏正中；macOS 使用左侧原生红黄绿按钮并把主题、语言切换放到右侧，Windows 则把主题、语言切换放到左侧并保留右侧窗口按钮。模式切换移到侧栏，主页保持为独立图标按钮，减少顶部拥挤，同时保留原来的操作边界。

---

### 发版级别判断

- 上一正式发版为 `0.15.1`。
- 本轮是自动更新发布指针修复，以及双平台窗口栏和侧栏入口的小范围交互调整。
- 不改变建模数据、IPC 协议、持久化格式或自动更新协议，因此按规则定为 `patch`，版本号为 `0.15.2`。

---

### 更新内容 / What's New

🔄 **自动更新 Latest 防回归** — 正式发布时显式设置并校验 GitHub Latest，解决安装包已经发布、旧客户端却仍读取旧版更新清单的问题。

🍎 **macOS 原生窗口按钮** — macOS 使用系统原生红黄绿按钮，不再重复显示 Windows 风格的最小化、最大化和关闭控件。

🪟 **双平台标题栏对称布局** — M-LCA 品牌固定在几何中心；macOS 的主题/语言在右侧，Windows 的主题/语言在左侧，两端保持一致边距。

🧭 **侧栏主入口精简** — Modeling/Cowork 胶囊移至侧栏顶部，主页改为旁边的独立图标按钮，并与会话卡片和底部功能按钮右侧对齐。

⚡ **首帧平台稳定** — preload 同步提供平台信息，首帧即可渲染正确的窗口控件，避免跨平台控件闪现或重复。

---

### 验证 / Verification

- Renderer 完整回归：24 个测试文件、133 项测试全部通过。
- Renderer 类型检查与生产构建通过；Electron main、preload 编译通过。
- Windows 实际 `npm run dev` 窗口完成视觉核验；独立 macOS CI 将完成平台编译、打包和产物验证，原生窗口按钮的最终视觉仍以 macOS 实机为准。
- 发布工作流将从不可变 `v0.15.2` 标签构建 Windows 与 macOS 安装包，并严格核对完整自动更新资产集和 GitHub Latest。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
