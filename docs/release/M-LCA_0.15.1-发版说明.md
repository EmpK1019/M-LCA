### 下载 / Download

点击对应系统的链接下载安装。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用自动更新所需文件；GitHub 另行显示的 Source code (zip/tar.gz) 才是源码归档。
Click your system's link to download. The `.yml`, `.zip`, and `.blockmap` files support in-app updates; GitHub's separately listed Source code (zip/tar.gz) entries are source archives.

| 系统 System | 下载 Download |
|---|---|
| macOS (Apple Silicon) | M-LCA-Installer-0.15.1-arm64.dmg ↓ |
| Windows (x64) | M-LCA-Setup-0.15.1.exe ↓ |

macOS: 如果提示无法打开，在终端运行 `xattr -cr /Applications/M-LCA.app` 后再双击。
Windows: 如果 SmartScreen 拦截，点击“更多信息”，再选择“仍要运行”。

---

### 发版级别判断

- 上一正式发版为 `0.15.0`。
- 本轮聚焦 Cowork 已完成准备阶段的紧凑呈现与可访问性补强，不改变任务协议、工具能力、数据格式或安装包更新协议。
- 这是修复与小范围体验改进，按规则定为 `patch`，版本号为 `0.15.1`。

---

### 本版重点 / Highlights

0.15.1 收敛了 Cowork 最容易显得“仪式感过重”的一段界面：简短任务中，计划、计划就绪和准备环境往往在极短时间内连续出现，但之前会各自占据一整行。现在这些已经完成的准备记录默认折叠成一条紧凑摘要，界面把注意力留给真正正在执行的工作、工具证据和答复。

这不是隐藏任务过程。准备记录仍完整保存在时间线、恢复状态和审计数据中；需要查看时可直接点击或用键盘展开。文字答复、工具调用、生成文件和仍在执行的阶段不会被折叠，也不会跨越原有的事件顺序。

---

### 更新内容 / What's New

🧩 **准备阶段默认折叠** — 连续完成的 `planning`、`plan_ready`、`preparing` 合并为一条简洁摘要，避免短任务一开始就出现大块重复进度。

👁️ **真实执行仍然可见** — `executing`、工具卡、文字答复、生成文件及任何被工具或文字打断的阶段维持原有顺序和可见性。

⌨️ **按需展开且可访问** — 使用原生折叠控件，鼠标点击与键盘操作都能查看全部准备记录；默认关闭不依赖人为延迟或动画。

🛡️ **恢复与审计不受影响** — 只改变 Renderer 显示投影，Engine、持久化时间线、任务计划、取消与恢复逻辑保留完整原始数据。

🧰 **发布收口加固** — 草稿 Release 的最终绑定与发布改为按 Release ID 校验和执行，降低双平台产物已上传但最后一步无法发布的风险。

---

### 验证 / Verification

- Renderer 测试：22 个测试文件、130 项通过，覆盖准备阶段分组、工具/答复边界和默认折叠渲染。
- `npm run typecheck:renderer`、`npm run build:renderer` 均通过。
- 候选源码范围的 `git diff --check` 通过；运行时天气文件与定时任务数据不纳入发行内容。
- 发布工作流将从不可变 `v0.15.1` 产品标签构建 Windows 与 macOS 安装包，并对完整自动更新资产集做严格验证。

---

### 平台 / Platforms

- macOS arm64（Apple Silicon），暂未完成 Apple 公证。
- Windows x64，暂未代码签名。
