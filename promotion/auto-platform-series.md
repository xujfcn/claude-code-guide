# Claude Code Guide 自动运营推广系列

> 推广对象：https://github.com/xujfcn/claude-code-guide  
> 核心关键词：Claude Code 使用教程、Claude Code 接入第三方 API、Claude Code 中转站、Claude Code 国内模型、Claude Code Crazyrouter  
> 主链接：https://github.com/xujfcn/claude-code-guide?utm_source={platform}&utm_medium={medium}&utm_campaign=claude_code_guide

## 统一定位

这不是单篇博客，而是一套 Claude Code 中文实战教程资产：36+ 篇文章，覆盖安装配置、Crazyrouter 接入、Base URL 排错、提示词、项目实战、Figma 原型、Mermaid 架构图和 AI Coding 工作流。

最适合拿来做：

- GitHub SEO 入口；
- 中文开发者社区教程；
- LinkedIn / Mastodon / Bluesky 社交推广；
- Dev.to / Hashnode 英文分发；
- Zenn 日文教程改写；
- Blogger / WordPress / Tumblr 镜像分发；
- SourceForge / GitLab / Codeberg 项目页镜像。

---

## 01｜主推长文：英文 Dev.to / Hashnode / Blogger / WordPress

### Title

Claude Code Guide: A Practical Chinese Tutorial Repo for Setup, API Routing, and AI Coding Workflows

### Tags

ai, claude, coding, api

### Body

Claude Code is becoming one of the most useful AI coding tools for developers, but onboarding is still messy.

Some users need the basic install command. Some need to configure a third-party API endpoint. Some run into the classic Base URL problem: should the endpoint include `/v1`, or should the client append it automatically? Others want workflow examples: PRD to code, Figma to prototype, Mermaid diagrams, project planning, and reusable prompts.

That is why we created **Claude Code Guide**:

https://github.com/xujfcn/claude-code-guide?utm_source=devto&utm_medium=article&utm_campaign=claude_code_guide

It is a 36+ article Chinese tutorial repository for Claude Code users, with a practical focus on setup, API routing, and real AI coding workflows.

### What the guide covers

- Claude Code installation and basic usage
- Correct Crazyrouter integration for Claude Code
- The difference between Anthropic-style root endpoints and OpenAI-compatible `/v1` endpoints
- Common Base URL mistakes, including `/v1/v1/messages`
- Prompting and workflow patterns
- Project implementation from PRD to code
- Figma and prototype workflows
- Mermaid architecture diagrams
- Product manager and developer collaboration workflows

### The most important setup rule

For Claude Code and Anthropic-native clients, use the root endpoint:

```bash
export ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
export ANTHROPIC_API_KEY=YOUR_CRAZYROUTER_API_KEY
claude
```

For OpenAI-compatible SDKs, use the `/v1` endpoint:

```text
https://cn.crazyrouter.com/v1
```

This distinction matters because different clients append paths differently. A wrong Base URL can create duplicated paths such as `/v1/v1/messages`.

### Why this repo is useful

Most AI tool documentation explains one feature at a time. This guide is organized as a learning path:

1. Quick setup
2. API and endpoint configuration
3. Basic Claude Code operations
4. Engineering workflows
5. Product and design workflows
6. Real project examples

The goal is not only to explain Claude Code, but to reduce integration friction for developers who want one practical reference.

### Repository

GitHub:

https://github.com/xujfcn/claude-code-guide?utm_source=devto&utm_medium=article&utm_campaign=claude_code_guide

If you are using Claude Code with custom API routing, model gateways, or multi-model AI coding workflows, this guide is meant to be a starting point.

---

## 02｜LinkedIn 推广帖

Developer onboarding for AI coding tools is still too fragile.

Claude Code users often get stuck on basic questions:

- Which Base URL should I use?
- Should the endpoint include `/v1`?
- How do I route Claude Code through a gateway?
- How do I move from prompt experiments to real project workflows?

We put together a 36+ article Chinese Claude Code guide covering setup, Crazyrouter integration, Base URL troubleshooting, PRD-to-code workflows, Figma prototypes, Mermaid diagrams, and AI coding patterns.

GitHub repo:
https://github.com/xujfcn/claude-code-guide?utm_source=linkedin&utm_medium=social&utm_campaign=claude_code_guide

The key rule:

Claude Code / Anthropic-native clients use:
`https://cn.crazyrouter.com`

OpenAI-compatible SDKs use:
`https://cn.crazyrouter.com/v1`

Small config details like this can save hours of support and debugging.

#ClaudeCode #AICoding #DeveloperTools #AIInfrastructure

---

## 03｜Mastodon 推广帖

Claude Code onboarding is full of small config traps.

We created a 36+ article Chinese guide covering:

- Claude Code setup
- Crazyrouter integration
- Base URL rules
- `/v1/v1/messages` troubleshooting
- PRD → code workflows
- Figma and Mermaid examples

Repo:
https://github.com/xujfcn/claude-code-guide?utm_source=mastodon&utm_medium=social&utm_campaign=claude_code_guide

Claude Code root URL:
https://cn.crazyrouter.com

OpenAI-compatible URL:
https://cn.crazyrouter.com/v1

#ClaudeCode #AICoding #LLM #DevTools

---

## 04｜Bluesky 推广帖

Claude Code setup gets confusing fast: root endpoint or `/v1`?

We made a 36+ article Chinese guide for Claude Code + Crazyrouter: setup, Base URL rules, troubleshooting, PRD-to-code, Figma, Mermaid, and AI coding workflows.

https://github.com/xujfcn/claude-code-guide?utm_source=bluesky&utm_medium=social&utm_campaign=claude_code_guide

---

## 05｜Twitter/X 推广帖

Claude Code users keep hitting the same setup trap:

Claude Code / Anthropic-native clients:
https://cn.crazyrouter.com

OpenAI-compatible SDKs:
https://cn.crazyrouter.com/v1

So we built a 36+ article Chinese Claude Code guide: setup, Crazyrouter integration, Base URL debugging, PRD-to-code, Figma, Mermaid, workflows.

https://github.com/xujfcn/claude-code-guide?utm_source=twitter&utm_medium=social&utm_campaign=claude_code_guide

---

## 06｜Zenn 日文改写版

### タイトル

Claude Code 中文実践ガイド：Crazyrouter で Claude / GPT / 国内モデルを統合する

### 本文

Claude Code は強力な AI コーディングツールですが、実際の導入では設定ミスがよく起きます。

特に多いのが Base URL の違いです。

Claude Code / Anthropic 互換クライアントでは、ルート URL を使います。

```bash
export ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
export ANTHROPIC_API_KEY=YOUR_CRAZYROUTER_API_KEY
claude
```

一方、OpenAI 互換 SDK や HTTP API では `/v1` を含む URL を使います。

```text
https://cn.crazyrouter.com/v1
```

この違いを間違えると、`/v1/v1/messages` のようなパス重複エラーが発生することがあります。

この問題を整理するために、Claude Code の中国語実践ガイドを公開しました。

GitHub:
https://github.com/xujfcn/claude-code-guide?utm_source=zenn&utm_medium=article&utm_campaign=claude_code_guide

内容：

- Claude Code のインストールと基本操作
- Crazyrouter との連携
- Base URL の正しい使い分け
- プロンプト設計
- PRD からコード生成までの流れ
- Figma / Mermaid を使った設計ワークフロー
- AI Coding 実践例

Claude Code を使った開発ワークフローを体系的に学びたい人向けのリポジトリです。

---

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

## 09｜平台自动分发建议

| 平台 | 文件/内容 | 状态 | UTM |
|---|---|---|---|
| Dev.to | 01 英文长文 | 可自动 | `utm_source=devto&utm_medium=article` |
| Hashnode | 01 英文长文 | 可自动 | `utm_source=hashnode&utm_medium=article` |
| Blogger | 01 英文长文 | 可自动 | `utm_source=blogger&utm_medium=article` |
| WordPress.com | 01 英文长文 | 可自动 | `utm_source=wordpress&utm_medium=article` |
| Tumblr | 01 英文长文精简 | 可自动 | `utm_source=tumblr&utm_medium=article` |
| LinkedIn | 02 | 可自动 | `utm_source=linkedin&utm_medium=social` |
| Mastodon | 03 | 可自动 | `utm_source=mastodon&utm_medium=social` |
| Bluesky | 04 | 可自动 | `utm_source=bluesky&utm_medium=social` |
| Twitter/X | 05 | 通过 Jeff 私聊 session | `utm_source=twitter&utm_medium=social` |
| Zenn | 06 日文 | Git push 自动 | `utm_source=zenn&utm_medium=article` |
| CSDN | 07 中文 | Jeff 手动粘贴 | `utm_source=csdn&utm_medium=article` |
| iT邦 | 08 繁中 | Jeff 手动粘贴 | `utm_source=ithome&utm_medium=article` |

---

## 10｜短链/追踪规范

所有人看的链接加 UTM：

```text
https://github.com/xujfcn/claude-code-guide?utm_source={platform}&utm_medium={article|social}&utm_campaign=claude_code_guide
```

API endpoint 不加 UTM：

```text
https://cn.crazyrouter.com
https://cn.crazyrouter.com/v1
```
