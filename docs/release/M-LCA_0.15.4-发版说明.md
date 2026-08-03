⬇ 下载 / Download

点对应系统的链接下载。页面上的 `.yml`、`.zip` 与 `.blockmap` 是应用更新所需文件；GitHub 另行显示的 Source code (zip/tar.gz) 才是源码归档。
Click your system's link to download. The `.yml`, `.zip`, and `.blockmap` files support application updates; GitHub's separately listed Source code (zip/tar.gz) entries are source archives.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.15.4-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.15.4.exe ↓ |

macOS：当前安装包尚无稳定签名，旧版无法通过应用内自动安装升级到 0.15.4；请下载 DMG 手动覆盖。安装后、首次打开前，请在终端运行 `xattr -cr /Applications/M-LCA.app`，然后再双击打开。

macOS: This build does not yet have a stable signing identity. Existing builds cannot install 0.15.4 automatically; download the DMG, replace the app, then run `xattr -cr /Applications/M-LCA.app` in Terminal before opening it for the first time.

Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

0.15.4 修正了 Cowork 长任务的交付方式。过程中已经按时间出现的文字不再在任务结束时整段重复；计划、准备、执行与收尾等内部状态统一收进默认折叠的“准备阶段”；右侧任务进度会在同一会话中持续累计；四张及以上连续工具卡片会自动折叠，但助手反馈仍会准确切开分组。

本版本也修复了模型与联网配置的安装边界。配置现在只属于当前用户目录，升级不会覆盖已有设置；旧安装位置中的配置只会在用户配置不存在时单向迁移。构建与发布流程新增多层失败保护，禁止真实配置、示例配置或环境文件进入引擎二进制、安装包、公开 Release 仓库与源码归档。

---

### 发版级别判断

- 上一正式发版为 `0.15.3`。
- 本轮以 Cowork 输出/展示正确性、任务进度补强和配置隔离修复为主。
- 不改变建模数据、IPC 命令、更新协议或平台架构，因此按规则定为 `patch`，版本号为 `0.15.4`。

---

### 更新内容 / What's New

🧹 **最终答复去重** — 终态不再重新拼接已经展示过的步骤结果，保留真实时间顺序和文件归属。

📦 **准备阶段统一折叠** — 计划、准备、执行、检查点与收尾生命周期收进一个默认折叠入口。

📋 **任务进度持续累计** — 同一会话的新任务追加到右侧进度列表，紧凑历史可在重启后恢复。

🛠️ **连续工具调用合并** — 连续四张及以上工具卡片自动折叠，助手反馈会自然切分工具组。

🔐 **用户配置永久独立** — 模型与联网设置统一保存在 `~/.mlca/api_config.local.py`，安装与升级不覆盖既有配置。

🧱 **发布配置零携带** — PyInstaller、双平台 Resources、发布组合目录和公开仓库均增加配置文件阻断检查。

🍎 **macOS 首次打开说明固定** — 发版说明恢复 `xattr -cr /Applications/M-LCA.app`，工作流缺少该命令时直接拒绝发版。

---

### 验证 / Verification

- Renderer 完整回归：28 个测试文件、144 项测试全部通过。
- Engine 完整回归：489 项测试通过、2 项按环境条件跳过。
- 发版/配置隔离策略：3 项全部通过。
- Renderer 类型检查以及 Renderer/Main/Preload 生产构建通过。
- 依赖锁、package JSON 和 GitHub Actions workflow YAML 校验通过。
- Windows 真实 `npm run dev` 验证：现有用户配置在启动前、运行中和退出后的 SHA-256 完全一致。
- 发布工作流将使用 Python 3.11 从不可变 `v0.15.4` 标签构建双平台安装包，并在上传前验证隔离配置桩来源和安装包资源边界。

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 签名与公证；本版本需要通过 DMG 手动覆盖，并在首次打开前执行上方 `xattr` 命令
- **Windows** — x64，暂未代码签名；现有应用内自动更新链保持可用
