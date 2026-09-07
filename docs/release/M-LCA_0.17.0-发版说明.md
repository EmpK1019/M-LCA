⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用自动更新所需文件；GitHub 另行显示的 Source code (zip/tar.gz) 才是源码归档。
Click your system's link to download. The `.yml`, `.zip`, and `.blockmap` files support in-app updates; GitHub's separately listed Source code (zip/tar.gz) entries are source archives.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.17.0-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.17.0.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个版本把 Cowork 从“能调用工具”推进到更可靠的长任务执行。任务、交互、附件、上下文、子任务与运行记录现在都有更明确的持久化和恢复边界；中断、重试或切换会话后，应用更少丢失状态，也不会把旧请求的结果写进新页面。

Coding 完成条件也被收紧了。修改源码后必须有与改动相关、且发生在最后一次修改之后的成功测试、类型检查、构建或语法校验；无关的成功命令、先成功后失败、恢复后不验证都不能再冒充完成。确定性回放已扩展到 11 个案例，覆盖失败、修复、续跑与失败关闭。

桌面交互同步完成了一轮可用性修整：任务进度与审批卡片采用悬浮布局，审批操作更紧凑，流式输出允许用户停在上方阅读；同时修复图标裁切、Modeling 右侧面板文字颜色和底部内容遮挡等问题。

---

### 更新内容 / What's New

🧪 **Coding 完成证据门禁** — 源码修改后必须完成相关验证，拒绝无关命令、过期成功结果和恢复绕过，减少“代码写了但任务并未真正完成”。

🧭 **可恢复 Cowork 运行时** — 任务计划、目标、交互请求、子任务、附件和上下文形成可恢复链路，降低长任务中断、重试和跨会话执行时的状态丢失。

🖥️ **更稳的桌面状态归属** — 为建模、资料库、附件、项目、会话和工具输出补齐请求关联与所有权隔离，避免后台结果覆盖当前界面或草稿。

📖 **任务与审批交互优化** — 任务进度和审批卡片悬浮展示，审批按钮右置并压缩内容高度；用户上滑阅读流式输出时不再被持续强制拉到底部。

🔌 **自动化与外部接入基础** — 增加 Python SDK、一次性 CLI、Headless Host、持久 Webhook、外部 Provider 接入边界和原生能力预检，为受控自动化提供统一入口。

🔐 **安全与可审计性** — 强化凭据隔离、结构化脱敏、工具结果规范、持久终端、运行日志与可选元数据遥测，使失败原因和执行证据更容易追踪。

📎 **附件与长输出可靠性** — 使用内容寻址附件、校验读取、派生缓存与可恢复长输出，减少重复存储、截断和损坏数据被继续使用的风险。

🌱 **建模优先保持不变** — Excel、材料库、版本管理和 LCA 建模流程继续复用原有能力；通用 Agent 增强没有替代 Python Engine 的建模与策略权威。

---

### 发版级别判断 / Release Level

本次从 `0.16.0` 升级到 `0.17.0`，属于 minor：一是新增可恢复运行时、SDK/Headless/Webhook 与外部 Provider 等整批能力；二是 Coding 完成机制从提示约束升级为运行时证据门禁；三是桌面请求归属与任务/审批交互有较大范围调整。上述变化明显超过单一补丁，但没有引入需要 major 版本表达的不兼容产品边界。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
