⬇ 下载 / Download

点对应系统的链接下载。页面上其它文件是 GitHub 自动生成的源码包，不用管。
Click your system's link to download. Other files on this page are auto-generated source archives — ignore them.

| 系统 System | 下载 Download |
|---|---|
| 🍎 macOS (Apple Silicon) | M-LCA-Installer-0.8.1-arm64.dmg ↓ |
| 🪟 Windows (x64) | M-LCA-Setup-0.8.1.exe ↓ |

macOS：打不开？终端运行 `xattr -cr /Applications/M-LCA.app` 再双击。/ Can't open? Run `xattr -cr /Applications/M-LCA.app` in Terminal, then double-click.
Windows：SmartScreen 拦了？「更多信息 → 仍要运行」。/ SmartScreen blocking? "More info → Run anyway."

* * *

这个版本只做了一件事，但这件事之前一直在悄悄出错。

`query_model_library` 是建模流程里最常用的工具之一。你让 AI 查一个模型，它搜出来，然后在下一轮对话里引用——问题就出在这里。跨轮之后，AI 有时候不是用搜索结果里的 UUID，而是"凭印象"拼出一个它觉得对的 UUID，然后用这个猜出来的 ID 去查详情。查到的数据是错的，但它不知道，继续往下建模。

这个问题不容易被发现，因为输出看起来是正常的，只是数据不对。

修法很直接：搜索结果唯一时，工具直接把完整数据一起返回，不需要再发起第二次请求，也就不存在跨轮丢失 UUID 的机会。搜索结果有多条时，每条附带明确的 UUID，并在返回里写死"必须用这个，不能自己推断"。

顺带修了另一个场景：用户说"帮我看一下模型库里这个模型的数据"，AI 之前会误以为这是在建模，触发清单校验流程，输出一堆不该出现的校验提示。现在这个场景单独处理，直接展示库里的数据，不校验，不推理。

还有一条：流程图从这版开始强制用 Mermaid，不再出现 ASCII 图。

---

### 更新内容 / What's New

🔍 **模型库查询修复** — 唯一命中直接返回完整数据；多命中附带 UUID 并禁止 AI 自行推断。解决跨轮对话中 AI 猜 UUID 导致引用错误数据的问题。

📋 **模型库展示模式** — 查看模型详情时直接展示库中数据，不触发清单校验流程。

📐 **流程图强制 Mermaid** — 所有流程图统一 Mermaid 格式输出。

---

### 平台 / Platforms

- **macOS** — arm64 / x64，暂未完成 Apple 公证
- **Windows** — x64，暂未代码签名
