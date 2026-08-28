⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用更新所需文件；GitHub 另行显示的 Source code (zip/tar.gz) 才是源码归档。
Click your system's link to download. The `.yml`, `.zip`, and `.blockmap` files support application updates; GitHub's separately listed Source code (zip/tar.gz) entries are source archives.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.15.5-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.15.5.exe ↓ |

macOS：当前安装包尚无稳定签名，旧版无法通过应用内自动安装升级到 0.15.5；请下载 DMG 手动覆盖。安装后、首次打开前，请在终端运行 `xattr -cr /Applications/M-LCA.app`，然后再双击打开。

macOS: This build does not yet have a stable signing identity. Existing builds cannot install 0.15.5 automatically; download the DMG, replace the app, then run `xattr -cr /Applications/M-LCA.app` in Terminal before opening it for the first time.

Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

0.15.5 主要解决长对话越来越难回看的问题。对话历史左侧新增了一条缩略书签栏，每条用户消息对应一根小横线，光标悬停会显示那句消息的概要，点一下就能直接跳回那一段，不用在很长的聊天里反复滚动翻找。同一页里，工具调用卡片默认只保留标题行，思考过程、输入与输出等细节收进折叠态，中间过程的大模型回复也去掉了卡片底色——只有最后一条完整答复保留卡片效果，主次一眼能分清。

这一版还顺手修正了交互与统计上的两个细节：macOS 拼音输入时按回车不再会误把正在组词的内容发送出去；背景信息窗口里的用量统计把工具调用、思考流和子任务都算进去了，数字更接近真实。

---

### 发版级别判断

- 上一正式发版为 `0.15.4`。
- 本轮以对话历史导航、消息与回复呈现的细化打磨为主，外加输入法组合态与上下文统计口径修复。
- 不改变建模数据、IPC 命令、更新协议或平台架构，因此按规则定为 `patch`，版本号为 `0.15.5`。

---

### 更新内容 / What's New

🔖 **对话书签栏** — 长对话左侧新增缩略书签栏，悬停预览、点击直达任一条用户消息，回看不再反复翻页。

🧊 **工具卡片默认折叠** — 工具调用只保留标题行，思考、输入输出等细节默认收起，点击展开，长对话不再被步骤卡刷屏。

🗑️ **过程答复去卡片化** — 中间过程的大模型回复改为透明展示，仅最后一条完整答复保留卡片，正文主次更清晰。

⏱️ **用户消息时间戳与复制** — 已发送消息底部显示发送时间，复制按钮移至气泡外，悬浮时才显现，界面更干净。

🖱️ **输入法组合态修复** — macOS 拼音输入时按 Enter 只确认候选词，不再误发送正在组词的文字。

📊 **上下文统计口径补齐** — 背景信息窗口的用量统计纳入工具调用、思考流与子任务，估算更接近真实。

🧹 **内部阶段不再展示** — planning / preparing / executing 等内部生命周期从对话中完全隐藏，只呈现对用户有意义的结果。

---

### 验证 / Verification

- Renderer 完整回归：28 个测试文件、144 项测试全部通过。
- Renderer / Main 类型检查通过。
- Renderer / Main / Preload 生产构建通过。
- 发版/配置隔离策略：3 项全部通过（真实、示例与环境配置文件不会进入引擎二进制、安装包与公开仓库）。
- 发布工作流将从不可变的 `v0.15.5` 标签构建双平台安装包，并在上传前校验配置隔离与安装包资源边界。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 签名与公证；本版本需要通过 DMG 手动覆盖，并在首次打开前执行上方 `xattr` 命令。
- **Windows** — x64，暂未代码签名；现有应用内自动更新链保持可用。