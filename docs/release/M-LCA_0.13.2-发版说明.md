### 下载 / Download

点击对应系统的链接下载安装。页面上的其它文件是 GitHub 自动生成的源码包，可以忽略。
Click your system's link to download. Other files on this page are auto-generated source archives; you can ignore them.

| 系统 System | 下载 Download |
|---|---|
| macOS (Apple Silicon) | M-LCA-Installer-0.13.2-arm64.dmg |
| Windows (x64) | M-LCA-Setup-0.13.2.exe |

macOS: 如果提示无法打开，在终端运行 `xattr -cr /Applications/M-LCA.app` 后再双击。
Windows: 如果 SmartScreen 拦截，点击“更多信息”，再选择“仍要运行”。

---

### 本版重点 / Highlights

0.13.2 是 0.13.x 的 Skill 市场发版。安装包继续包含标准化模型库、全局物料清单等默认资源，同时新增 GitHub Skill 市场能力，让正式版用户不需要云服务也可以从固定公开仓库安装技能。

- 新增 Skill 市场页面，来源固定为 `EmpK1019/MLCA-skills`，支持实时拉取市场列表、查询市场版本、本地版本和更新状态。
- 本次安装包不随包预装市场 skill；市场 skill 均通过在线市场按需安装。
- 市场技能安装只下载被点击的 `skills/<id>` 目录，不再允许任意仓库作为市场来源。
- 本地 Skill 列表统一来源显示：市场管理的技能显示为“市场”，自建导入或手动 GitHub 安装显示为“自建”。
- 已安装的市场技能支持卸载；自建技能保持删除语义。
- 市场和本地技能发布者统一显示为 `MLCA`，避免继续显示旧的第三方来源或“非官方”。
- 发布工作流会同步专用技能源仓库到公开市场仓库 `EmpK1019/MLCA-skills`，正式用户无需配置私有 token。

---

### 验证 / Verification

- `python -m unittest engine.tests.test_skill_service engine.tests.test_skill_marketplace_service engine.tests.test_ipc_schema`
- `python -m py_compile engine\application\skill_service.py engine\application\skill_marketplace_service.py engine\application\builtin_skill_bundle.py`
- `npm run typecheck:renderer`
- `npm run build:main`
- `node --check scripts/build-engine.mjs`

---

### 平台 / Platforms

- macOS arm64 (Apple Silicon)，暂未完成 Apple 公证
- Windows x64，暂未代码签名
