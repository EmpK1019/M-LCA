### 下载 / Download

点击对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。Click your system's link to download. Other files on this page are auto-generated source archives; ignore them.

| 系统 System | 下载 Download |
|---|---|
| macOS (Apple Silicon) | M-LCA-Installer-0.13.1-arm64.dmg ↓ |
| Windows (x64) | M-LCA-Setup-0.13.1.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？“更多信息 → 仍要运行”。SmartScreen blocking? "More info → Run anyway."

---

这一版是 0.13.0 的资源补发版。0.13.0 已经把 Cowork 编程能力、IDE runtime、MCP/Plugin/Skill 链路发出去，但安装包没有完整带上默认数据资源：标准化模型库、全局物料清单，以及 `engine_data/skills` 里的内置上下文 skills。

0.13.1 修复的是“安装后能力不完整”的问题。新安装或缺少默认资源的环境会在启动时自动补齐模型库、物料库和内置 skills；已有用户自己的数据不会被覆盖。

---

### 更新内容 / What's New

📦 **补齐默认数据资源** — 安装包现在随包携带 `model_library_global.json` 和 `material_list_global.json`，新环境可直接使用标准化模型库和物料管理能力。

🧠 **补齐内置上下文 Skills** — 随包发布 `skill-creator`、`docx`、`xlsx`、`pptx`、`pdf`、`canvas-design` 等 `engine_data/skills` 内置 skills，并保留默认启用状态。

🛡️ **启动时安全种子同步** — packaged 启动前会把缺失的默认数据复制到用户 `engine_data`，只补缺失项，不覆盖用户已有模型库、物料库或自定义 skills。

---

### 验证 / Verification

- `npm run build:main`
- `node --check scripts/build-engine.mjs`

---

### 平台 / Platforms

- **macOS** - arm64 (Apple Silicon)，暂未完成 Apple 公证
- **Windows** - x64，暂未代码签名
