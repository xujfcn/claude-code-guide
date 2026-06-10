## 08｜iT邦幫忙繁中实操版

### 標題

一條指令設定 Claude Code：用 Crazyrouter 統一接入 Claude、GPT 和國內模型

### 正文

Claude Code 很適合拿來做 AI Coding，但新手最容易卡在 API 設定。

尤其是 Base URL：到底要不要加 `/v1`？

如果你用的是 Claude Code / Anthropic 原生模式，設定根網址：

```bash
export ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
export ANTHROPIC_API_KEY=YOUR_CRAZYROUTER_API_KEY
claude
```

如果你用的是 OpenAI-compatible SDK，才使用：

```text
https://cn.crazyrouter.com/v1
```

差別很小，但配錯就會出現 `/v1/v1/messages` 這種錯誤。

我整理了一套 Claude Code 中文實戰教學，共 36+ 篇：

https://github.com/xujfcn/claude-code-guide?utm_source=ithome&utm_medium=article&utm_campaign=claude_code_guide

內容包含：

- Claude Code 安裝與快速上手
- Crazyrouter 接入設定
- Base URL 排錯
- PRD 到程式碼生成
- Figma 原型流程
- Mermaid 架構圖與流程圖
- AI Coding 實戰案例

如果你想把 Claude Code 變成實際工作流，而不是只拿來聊天，這套教學可以從第一篇照著做。

---
