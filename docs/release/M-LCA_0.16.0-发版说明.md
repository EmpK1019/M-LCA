⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用更新所需文件；GitHub 另行显示的 Source code (zip/tar.gz) 才是源码归档。
Click your system's link to download. The `.yml`, `.zip`, and `.blockmap` files support application updates; GitHub's separately listed Source code (zip/tar.gz) entries are source archives.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.16.0-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.16.0.exe ↓ |

macOS：当前安装包尚无稳定签名，旧版无法通过应用内自动安装升级到 0.16.0；请下载 DMG 手动覆盖。安装后、首次打开前，请在终端运行 `xattr -cr /Applications/M-LCA.app`，然后再双击打开。

macOS: This build does not yet have a stable signing identity. Existing builds cannot install 0.16.0 automatically; download the DMG, replace the app, then run `xattr -cr /Applications/M-LCA.app` in Terminal before opening it for the first time.

Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

0.16.0 最大的变化是对话不再只能单向地等着。以前任务跑到一半想插一句、换个方向，都得先把它停下来；现在你直接在输入框发新消息，引擎会在下一个安全边界让当前 run 让位，把你的新消息并入同一个上下文继续跑，原来的进度和产出都保留，是续做还是变向由 agent 自己判断。停止也不再是一刀切打断，而是协作式的软取消：前端点了立即恢复，后台把当前那一步跑完再收尾，全程不再冒出「已停止 / 已取消」这类打断的噪音。

这一版同时把子代理面板、历史区/输入框布局、工具卡片这些高频接触的界面收了一遍：子代理面板去掉了直接对话、打开时盖住右侧面板；历史与输入框两侧对称留白、消息能撑满整行；连续三个工具卡片就自动折叠，长任务里工具卡片右上角的序号也去掉了。都是在减少长对话、多任务时眼睛和鼠标的负担。

---

### 发版级别判断

- 上一正式发版为 `0.15.5`。
- 本轮新增「运行中发新消息 = 补充续跑」这一新的交互流程，并对子代理面板、历史区/输入框布局、StepCard 与停止/中断做了一整批明显的能力与 UI/交互变化。
- 不改变建模数据模型、IPC 命令契约或平台架构，因此按规则定为 `minor`，版本号为 `0.16.0`。

---

### 更新内容 / What's New

💬 **运行中发新消息 = 补充续跑** — 任务执行中途直接发新消息，引擎在下一个工具边界软中断当前 run、保留已完成的步骤与产出，把新消息并入会话并从已有上下文继续，agent 自行续做或变向，不再拒绝或新开任务。

⏹ **停止不再生硬** — 停止/终止改为协作式软取消，不再冒出「已按请求停止 / cancelled」等打断文案；点下即前端立即复原，引擎在后台跑完当前工具调用再收尾，期间发新消息仍按补充入队。

🧩 **子代理面板收敛** — 子代理面板移除直接对话，只展示主 agent 派发后的进度、工具、思考与结果；打开时盖住右侧面板，仅与历史区双向拖拽调宽。

📐 **历史区与输入框布局** — 历史消息与输入框两侧统一 100px 对称留白，消息块可撑满整行；发送按钮去掉框与底色、仅保留飞机图标并跟随主题色；书签栏当前位置高亮与悬停放大更明显。

🧮 **StepCard 细节** — 连续 3 个及以上工具卡片自动折叠（原为 4），并取消卡片右上角序号，界面更清爽。

⚙️ **工具执行指示器** — 长工具执行期间顶部「正在思考」小状态也会点亮，避免看起来没有响应。

🔎 **子代理识别与超时** — 派发描述补充中文别名；wait_subagent 单次轮询上限说明为 60 秒，任务未完成可反复轮询，无固定总轮询次数上限。

---

### 验证 / Verification

- Renderer 完整回归通过（含 store/cowork、tool-group 等新增用例）。
- Renderer / Main / Preload 类型检查通过；Engine 相关回归（cowork+cancellation、子代理隔离、agent_runtime）通过。
- 引擎白名单仅 `material_list_global.json`、`model_library_global.json` 进入引擎与安装包。
- 发布工作流将从不可变的 `v0.16.0` 标签构建双平台安装包，并在上传前校验安装包资源边界。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 签名与公证；本版本需要通过 DMG 手动覆盖，并在首次打开前执行上方 `xattr` 命令。
- **Windows** — x64，暂未代码签名；现有应用内自动更新链保持可用。