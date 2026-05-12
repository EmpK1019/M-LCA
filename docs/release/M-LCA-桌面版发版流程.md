# M-LCA 桌面版发版流程

## 目的

固化 M-LCA 桌面版的发版流程，后续按此文件执行。

---

## 版本号确定规则

以上一版已发版目录为基准，按本轮开发相对上一版的变化程度决定下一发版号：

- `patch`：以修复、规则调整、小范围功能补强为主，例如 `0.8.0 -> 0.8.1`
- `minor`：有一整批明显的新能力、新流程或较大范围 UI / 交互变化，例如 `0.8.x -> 0.9.0`
- `major`：存在不兼容变更、产品边界明显变化时再考虑

默认优先使用 `patch`。

**强制判断规则：**

- 先判断本轮改动级别，再决定发版号；不能先看当前 `package.json` 的 `-dev` 版本号再机械顺推。
- `desktop/package.json` 里的当前开发版本只表示工作区所处的开发态，不代表这次必须发布为对应的补丁号。
- 每次发版前，必须先对照上一已发版目录，按"修复补丁 / 明显新能力 / 架构级变化"三类判断本轮属于 `patch / minor / major`。
- 判断结论至少要能用 1 到 3 条具体理由说明，不能只写"按当前版本顺推"。

---

## 当前项目路径

- 项目根目录：`D:\1.AI-agent-file\2.LCA_modeler_Project\M-LCA\M-LCA_dev`
- 桌面端目录：`D:\1.AI-agent-file\2.LCA_modeler_Project\M-LCA\M-LCA_dev\desktop`
- 发版说明目录：`D:\1.AI-agent-file\2.LCA_modeler_Project\M-LCA\M-LCA_dev\docs\release`

---

## 版本文件

桌面端版本来源：

- `desktop/package.json`
- `desktop/package-lock.json`

开发态统一带 `-dev` 后缀，例如 `0.8.2-dev`。正式发版前切成不带 `-dev` 的正式版本，发版完成后再改回下一补丁版本的开发态。

---

## 标准发版步骤

### 1. 确定发版号

1. 查看上一版发版目录（例如 `M-LCA_0.8.0`）。
2. 列出本轮相对上一版的主要变化，至少写 1 到 3 条。
3. 判断属于 `patch / minor / major` 哪一类。
4. 判断完成后才确定具体版本号；禁止仅根据当前 `-dev` 版本号直接顺推。

### 2. 切到正式发版号

在 `desktop/` 目录下执行：

```bash
npm run version:release
```

### 3. 写发版说明

在 `docs/release/` 下新建 `M-LCA_<版本号>-发版说明.md`。

**这个文件会被 CI 直接读取作为 GitHub Release 的页面正文，也是 README 版本历史的来源，写好它等于同时更新了两个地方。**

#### 固定结构

```markdown
⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-<版本号>-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-<版本号>.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

[叙事段落：用第一人称或"我们"，讲这个版本解决了什么问题、为什么这么做。
语气直接，不用堆砌功能列表。1-3 段，每段聚焦一件事。]

---

### 更新内容 / What's New

[emoji] **[功能名]** — [一句话说清楚做了什么、解决了什么问题]

---

### 平台 / Platforms

- **macOS** — arm64（Apple Silicon），暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
```

#### 写作要求

- **下载表只列实际存在的安装包**：CI 用 `macos-14` runner，只出 arm64 DMG，不要写 Intel 行
- **叙事段落是核心**：不是功能列表的堆砌，而是讲清楚"这个版本发生了什么、为什么值得发"
- **语气直接**：不用"我们很高兴地宣布"，直接说问题和解法
- **更新内容列表**：每条用 emoji 开头，格式为 `emoji **名称** — 说明`，说明里要包含"解决了什么"而不只是"做了什么"

### 4. Commit 并推送到 GitHub

```bash
git add desktop/package.json desktop/package-lock.json docs/release/M-LCA_<版本号>-发版说明.md <其他改动文件>
git commit -m "release: v<版本号>"
git push origin main
```

### 5. 触发 GitHub Actions CI 打包

推送完成后，通过 GitHub API 触发 `desktop-release` workflow：

```bash
TOKEN="<github_token>"
curl -s -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $TOKEN" \
  "https://api.github.com/repos/EmpK1019/M-LCA_dev/actions/workflows/desktop-release.yml/dispatches" \
  -d "{\"ref\":\"main\",\"inputs\":{\"version\":\"<版本号>\"}}"
```

也可以直接在 GitHub 网页端：Actions → `desktop-release` → Run workflow → 填入版本号。

### 6. 等待 CI 完成，确认 Release 创建

CI 完成后会自动：

- 创建 GitHub Release（tag: `v<版本号>`）
- 上传 Windows 安装包（`M-LCA-Setup-<版本号>.exe`）
- 上传 macOS DMG（`M-LCA-Installer-<版本号>-<arch>.dmg`）

可通过 API 轮询确认：

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://api.github.com/repos/EmpK1019/M-LCA_dev/actions/runs/<run_id>" \
  | grep -E '"status"|"conclusion"'
```

### 7. 切回下一开发版本

发版完成后，将工作区版本改为下一补丁版本的开发态（例如 `0.8.1 -> 0.8.2-dev`）：

```bash
# 手动修改 desktop/package.json 和 desktop/package-lock.json 中的版本号
git add desktop/package.json desktop/package-lock.json
git commit -m "chore: bump to <下一版本>-dev"
git push origin main
```

### 8. 本地备份

用 robocopy 将当前开发目录备份为 `M-LCA_dev_<版本号>`：

```powershell
robocopy "D:\1.AI-agent-file\2.LCA_modeler_Project\M-LCA\M-LCA_dev" `
         "D:\1.AI-agent-file\2.LCA_modeler_Project\M-LCA\M-LCA_dev_<版本号>" `
         /E /XD "venv" "__pycache__" "node_modules" /XF "*.pyc" /NP /NFL /NDL /R:1 /W:1
```

> 注意：robocopy 退出码 1 表示"有文件被复制"，是正常成功状态，不是错误。

---

## 默认执行顺序

1. 查看上一版发版目录，列出本轮关键变化，判断 `patch / minor / major`
2. `npm run version:release`
3. 写发版说明（`docs/release/M-LCA_<版本号>-发版说明.md`）
4. `git commit` + `git push origin main`
5. 触发 GitHub Actions `desktop-release` workflow（传入版本号）
6. 等待 CI 完成，确认 GitHub Release 已创建并包含安装包
7. 手动修改版本号为下一 `-dev`，`git commit` + `git push`
8. robocopy 备份 `M-LCA_dev` 为 `M-LCA_dev_<版本号>`
