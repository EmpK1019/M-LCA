⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用更新所需文件；GitHub 另行显示的 Source code (zip/tar.gz) 才是源码归档。
Click your system's link to download. The `.yml`, `.zip`, and `.blockmap` files support application updates; GitHub's separately listed Source code (zip/tar.gz) entries are source archives.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.15.3-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.15.3.exe ↓ |

macOS：当前安装包尚无稳定签名，旧版无法通过应用内自动安装升级到 0.15.3；请下载 DMG 手动覆盖。首次打开如被拦截，可右键选择“打开”。

macOS: This build does not yet have a stable signing identity. Existing builds cannot install 0.15.3 automatically; download the DMG and replace the app manually.

Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

0.15.3 调整了明亮模式的工作区表面层级。顶部标题栏、左侧导航栏和右侧信息栏现在共同构成浅绿色外框，中间首页、对话和管理工作区改为白色主画布，让视觉重心回到内容区域。

这次变更只交换明亮模式下已有浅绿色与白色的使用位置。暗色模式、组件结构、窗口栏布局、交互、IPC、引擎和持久化数据均保持不变。

---

### 发版级别判断

- 上一正式发版为 `0.15.2`。
- 本轮只调整明亮模式的工作区背景层级并增加静态回归。
- 不改变建模数据、IPC 协议、持久化格式或更新协议，因此按规则定为 `patch`，版本号为 `0.15.3`。

---

### 更新内容 / What's New

🎨 **浅绿色应用外框** — 明亮模式下的标题栏、左侧栏和右侧栏统一使用既有浅绿色背景。

⬜ **白色中央工作区** — 首页、对话和管理视图共用的中央区域改为白色，内容层级更加清晰。

🌙 **暗色模式不变** — 颜色交换仅作用于明亮模式，暗色模式保持原有视觉。

🧩 **结构与交互稳定** — 不改变组件层级、按钮位置、窗口控件、IPC 或引擎行为。

---

### 验证 / Verification

- 明亮模式工作区表面定向测试：2 项全部通过。
- Renderer 完整回归：25 个测试文件、135 项测试全部通过。
- Renderer 类型检查与生产构建通过。
- Windows 真实 `npm run dev` Electron 窗口完成明亮模式视觉核验。
- 发布工作流将从不可变 `v0.15.3` 标签构建 Windows 与 macOS 安装包，并严格核对完整更新资产集和 GitHub Latest。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 签名与公证；本版本需要通过 DMG 手动覆盖安装
- **Windows** — x64，暂未代码签名；现有应用内自动更新链保持可用
