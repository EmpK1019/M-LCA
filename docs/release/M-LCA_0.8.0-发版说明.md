# M-LCA 0.8.0 发版说明

## 发版级别判断

- 上一已发版目录为 `M-LCA_0.7.0`
- 本轮包含：思考过程显示系统全面重构、PPTX 视觉审计流程强制化、工具执行步骤富信息展示、截图导出与结构化审计双轨机制
- 按发版规则属于 `minor` 级别，版本号定为 `0.8.0`
- 理由：(1) 思考过程显示从临时状态条重构为可折叠持久面板，属于交互模式明显变化；(2) PPTX 审计流程从口头自检升级为强制工具调用循环，属于流程级改造；(3) 工具步骤卡片引入 Lucide Icons、耗时显示、进度徽章等一批新 UI 能力

## 本版重点

### 思考过程显示重构

- **ThinkingPanel 可折叠面板**：替代原来一闪而过的 ThinkingStatusBar，所有 LLM 思考内容累积保存，默认折叠、支持展开查看全部历史
- **"思考过程"→"执行步骤"**：原 ThinkingBubble 区域更名为"执行步骤"，更准确反映其展示工具调用步骤的实际功能
- **thinkingHistory 累积机制**：store.ts 新增 `thinkingHistory: string[]`，每次 `task.thinking_status` 事件追加到历史，思考结束不清空

### PPTX 视觉审计强制化

- **审计数据默认生成**：render_deck.js 不再依赖 spec 中的 `_auditOutput` 字段，每次渲染后自动在 workdir 生成 `*_audit.json`
- **强制审计流程**：deck_workflow.md、mode_native_pptx.md、audit_workflow.md 三份文件统一写入"不得用口头自检代替实际工具调用"的强制语言
- **截图导出不暴露给用户**：`run_generated_script` 新增 `collect_all_outputs` 参数，截图步骤设为 `false`，防止 PNG 作为附件返回给用户
- **结构化审计脚本**：audit_deck_structural.js 规则引擎（填充率、字号一致性、文本溢出、元素重叠等 9 条规则）
- **截图导出脚本**：export_slides.js 支持 PowerPoint COM (Windows) → AppleScript (macOS) → LibreOffice headless 三级 fallback

### 工具执行步骤富信息展示

- **Lucide Icons 工具图标映射**：15 种工具专属图标（BrainCircuit、Globe、Presentation 等）
- **耗时显示**：工具完成后右上角等宽字体显示耗时（如 `2.4s`）
- **进度徽章**：sequential-thinking 显示 `[3/5]` 进度
- **详细 thought**：`_build_detailed_thought()` 为每种工具提供丰富上下文描述（搜索关键词、PPTX 标题页数、技能资源名等）
- **下一步预告**：完成步骤底部显示 Fuchsia 色预告 + ArrowDownRight 图标

### 动效系统

- **slideDownFade**：卡片入场丝滑展开淡入
- **gentle-breathe**：思考图标呼吸灯带光晕
- **text-update-flash**：Token 流更新微动效
- **pop-done**：完成时图标弹跳动效

## 影响范围

- 思考过程显示（ThinkingBubble → ThinkingPanel + StepCard）
- PPTX 生成审计流程（render_deck.js、skill 文档）
- 工具执行步骤展示（AgentStepCallback、thinking-bubble.tsx）
- `run_generated_script` 工具（新增 collect_all_outputs 参数）
- CSS 动画系统（styles.css）

## 文件变更清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `desktop/package.json` | 修改 | 版本 0.7.1-dev → 0.8.0 |
| `desktop/renderer/src/components/thinking-bubble.tsx` | 重构 | ThinkingPanel + StepCard + Lucide Icons |
| `desktop/renderer/src/store.ts` | 修改 | 新增 thinkingHistory、thinkingStatus 累积逻辑 |
| `desktop/renderer/src/workspace-types.ts` | 修改 | AgentStep 新增 elapsed_ms、progress |
| `desktop/renderer/src/styles.css` | 修改 | ThinkingPanel 样式 + 4 组 keyframes |
| `desktop/renderer/src/i18n.ts` | 修改 | roleThinking: 思考过程→执行步骤 |
| `engine/application/agent_runtime.py` | 重构 | AgentStepCallback 全面重写 |
| `engine/application/agent_tools.py` | 修改 | run_generated_script 新增 collect_all_outputs |
| `engine/application/generated_artifact_service.py` | 修改 | _collect_generated_files 新增 only_expected 参数 |
| `engine/main.py` | 修改 | 新增 _emit_thinking_status |
| `engine_data/skills/pptx/scripts/render_deck.js` | 修改 | 审计数据默认生成 |
| `engine_data/skills/pptx/scripts/export_slides.js` | 新增 | 截图导出脚本（三级 fallback） |
| `engine_data/skills/pptx/scripts/export_slides_to_images.ps1` | 新增 | PowerShell COM 导出脚本 |
| `engine_data/skills/pptx/scripts/audit_deck_structural.js` | 新增 | 结构化审计规则引擎 |
| `engine_data/skills/pptx/mode_native_pptx.md` | 重写 | TRACK 阶段强制审计步骤 |
| `engine_data/skills/pptx/deck_workflow.md` | 修改 | 审计强制化语言 |
| `engine_data/skills/pptx/audit_workflow.md` | 重写 | 完整审计流程文档 |

## 备注

- macOS 产物仍需在 macOS 主机或 CI 环境执行 `npm run pack:mac`
- LibreOffice Portable（D:\tmp\LibreOfficePortable）作为截图导出 fallback，未打包进发行物
