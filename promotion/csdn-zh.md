## 07｜CSDN / 中文社区帖

### 标题

Claude Code 中文教程：接入 Crazyrouter 后，一个入口使用 Claude、GPT 和国内模型

### 正文

Claude Code 很好用，但真正上手时，很多人会卡在配置上。

最常见的问题是：Base URL 到底要不要带 `/v1`？

答案是：看客户端类型。

如果是 Claude Code / Anthropic 原生客户端，使用根域名：

```bash
export ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
export ANTHROPIC_API_KEY=YOUR_CRAZYROUTER_API_KEY
claude
```

如果是 OpenAI 兼容 SDK 或 HTTP API，使用 `/v1`：

```text
https://cn.crazyrouter.com/v1
```

这个区别很重要。如果写错，就可能出现 `/v1/v1/messages` 这类路径重复问题。

我整理了一套 Claude Code 中文实战教程：

https://github.com/xujfcn/claude-code-guide?utm_source=csdn&utm_medium=article&utm_campaign=claude_code_guide

目前包含 36+ 篇文章，覆盖：

- Claude Code 安装与基础操作
- Crazyrouter 接入配置
- Base URL 常见错误排查
- 提示词技巧
- 从 PRD 到代码生成
- Figma 原型设计
- Mermaid 架构图、流程图、时序图
- AI Coding 项目实战

如果你正在找 Claude Code 使用教程，或者想把 Claude Code 统一接入到一个 AI API 入口，这个仓库可以直接作为学习路径。

---
