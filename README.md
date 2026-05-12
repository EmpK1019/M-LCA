# M-LCA

**AI 驱动的 LCA 建模桌面工具**

用自然语言完成生命周期评价建模 · 标准化模型库查询与复用 · 本地运行，数据不出机器

---

## 这是什么

M-LCA 是一款面向 LCA 从业者的桌面建模助手。通过对话驱动建模流程，支持 ISO 14067 / GB/T 24067 等主流标准，内置标准化模型库、物料名称标准化、清单结构校验与 Excel 模板导出。

核心设计原则：建模逻辑在本地 Python 引擎中运行，会话数据、产品数据、物料清单均不上传。

---

## 下载

| 平台 | 文件 |
|------|------|
| Windows (x64) | `M-LCA-Setup-<版本号>.exe` |
| macOS (Apple Silicon) | `M-LCA-Installer-<版本号>-<arch>.dmg` |

前往 [Releases](https://github.com/EmpK1019/M-LCA_dev/releases) 下载最新版本。

> macOS：右键 → 打开（首次运行需绕过 Gatekeeper）  
> Windows：SmartScreen 提示时选择"仍要运行"

---

## 快速开始

1. 下载并安装对应平台的安装包
2. 在根目录创建 `api_config.py`，填入 API Key（见下方配置说明）
3. 启动应用，开始对话建模

---

## 主要能力

### 对话建模

用自然语言描述产品系统，AI 引导完成功能单位定义、系统边界划定、清单数据填写与结果输出。支持多轮对话修改，建模过程可随时中断和恢复。

### 标准化模型库

内置标准化模型库，支持按关键词搜索或按 UUID 查看完整数据清单。命中后直接复用库中数据，无需重新推理，保证数据一致性。

### Skill 系统

两阶段加载机制：列表阶段只展示名称与描述，执行阶段按需加载并自动注入权限。内置 `lca-base`（建模规则）、`pptx`（演示文稿生成）等 Skill，支持从 GitHub 安装自定义 Skill。

### 工具执行步骤

每个工具调用以可折叠步骤卡片展示，含工具图标、耗时、进度。LLM 思考内容累积保存到思考面板，默认折叠，支持展开查看完整历史。

### PPTX 生成

结构化 deck spec → 原生可编辑 PPTX。强制审计流程：渲染后自动生成审计报告，9 条结构规则（填充率、字号一致性、文本溢出、元素重叠等）自动检查。

### 权限与钩子

工具调用权限管线（deny > hooks > allow > ask > default），通过 `.lca-agent/hooks.yaml` 配置六类事件钩子。

---

## 使用场景

- **LCA 工程师**：对话式完成建模，查询标准化模型库，导出 Excel 清单
- **碳核查团队**：批量匹配物料，生成符合 ISO 14067 / GB/T 24067 的核查报告
- **研究人员**：本地运行，敏感数据不出机器，支持自定义 Skill 扩展建模规则

---

## 配置

根目录创建 `api_config.py`：

```python
OPENAI_API_KEY = "..."
OPENAI_API_BASE = "..."
FALLBACK_API_KEY = "..."      # 可选，备用模型
FALLBACK_API_BASE = "..."
FALLBACK_MODEL = "..."
TAVILY_API_KEY = "..."        # 可选，网页搜索
```

---

## 项目结构

```
M-LCA_dev/
├── desktop/          # Electron + React 桌面端
├── engine/           # Python 建模引擎
│   └── application/  # 应用服务层（建模流程、Skill、物料、Excel）
├── shared/           # 前后端共享协议
├── skills/           # 内置 Skill 包
├── engine_data/      # 运行时数据（会话、输出、物料库）
└── docs/             # 发版说明与操作文档
```

运行时数据写入 `engine_data/`，打包态写入系统可写目录，不写入安装目录。

---

## 开发环境

```bash
# 在 desktop/ 目录下
node scripts/dev.mjs
```

同时启动 Electron 前端与 Python 引擎，改动即时生效。

---

## 版本历史

| 版本 | 类型 | 重点 |
|------|------|------|
| **0.8.1** | patch | 模型库查询优化：唯一命中直接返回完整数据，禁止猜测 UUID；lca-base 新增模型库展示交互模式；流程图强制 Mermaid 格式 |
| **0.8.0** | minor | 思考过程显示重构（ThinkingPanel）；PPTX 视觉审计强制化；工具步骤富信息展示（图标、耗时、进度徽章）；动效系统 |
| **0.7.0** | minor | 权限管线系统；Hook 服务；Skill 两阶段加载；MCP 桥接；Token 流式推送 |
| **0.6.0** | minor | 双平台发版架构；聊天附件持久化；PPTX deck spec 宽松解析 |

完整发版说明见 [Releases](https://github.com/EmpK1019/M-LCA_dev/releases)。

---

## 发版

发版流程见 [`docs/release/M-LCA-桌面版发版流程.md`](docs/release/M-LCA-桌面版发版流程.md)。

CI 打包通过 GitHub Actions `desktop-release` workflow 触发（`workflow_dispatch`，手动传入版本号），产出 Windows 安装包与 macOS DMG。

---

Copyright © 2026 EC. All rights reserved.
