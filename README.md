# Claude Code 中文实战指南：通过 Crazyrouter 统一接入 Claude、GPT 与国内模型

> 36+ 篇 Claude Code 中文教程，覆盖安装配置、Crazyrouter 接入、提示词模板、项目实战、产品原型、Figma、Mermaid 架构图和 AI Coding 工作流。

如果你正在搜索 **Claude Code 使用教程**、**Claude Code 接入第三方 API**、**Claude Code 中转站**、**Claude Code 国内模型**，这个仓库可以按从入门到实战的顺序阅读。

## 最快 3 步接入 Crazyrouter

Claude Code / Anthropic 原生客户端使用 Crazyrouter **根域名**，不要在这里加 `/v1`：

```bash
export ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
export ANTHROPIC_API_KEY=YOUR_CRAZYROUTER_API_KEY
claude
```

Windows PowerShell：

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://cn.crazyrouter.com", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "YOUR_CRAZYROUTER_API_KEY", "User")
```

OpenAI 兼容 SDK、HTTP 请求和前后端应用才使用 `/v1` 地址：

```text
https://cn.crazyrouter.com/v1
```

## 一键配置脚本

如果你希望自动检查 Git、Node.js、Claude Code，并写入环境变量，可以使用：

```bash
curl -fsSL https://raw.githubusercontent.com/xujfcn/crazyrouter-claude-code/main/setup.sh | bash
```

脚本仓库：

- [Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)

## 为什么 Claude Code 适合接入 Crazyrouter

- 一个 API Token 统一管理 Claude、GPT、Gemini、DeepSeek 等模型。
- Claude Code 使用根域名：`https://cn.crazyrouter.com`，避免 `/v1/v1/messages` 配置错误。
- 控制台统一查看调用日志、余额、失败原因和模型权限。
- 可以给 Claude Code 单独创建 Token，设置预算和模型白名单。
- 适合团队把 AI Coding 工具、后端服务和内部 Agent 统一到一个入口。

## 推荐阅读路径

### 入门配置

1. [01｜Claude Code 接入 Crazyrouter 快速入门与配置](articles/01-01-claude-code-接入-crazyrouter-快速入门与配置.md)
2. [05｜通过 Crazyrouter 在 Claude Code 中统一接入国内模型](articles/05-05-通过-crazyrouter-在-claude-code-中统一接入国内模型.md)
3. [06｜Claude Code 入门基础操作](articles/06-06-claude-code-接入-crazyrouter-连载-06-第三章-入门基础操作.md)

### 工程实践

1. [02｜Claude Code 接入 Crazyrouter 的工程实践](articles/02-02-claude-code-接入-crazyrouter-的工程实践.md)
2. [03｜Claude Code 接入 Crazyrouter 的企业级应用实战](articles/03-03-claude-code-接入-crazyrouter-的企业级应用实战.md)
3. [24｜AI Coding 实战：从 PRD 到代码生成](articles/24-24-claude-code-接入-crazyrouter-连载-24-aicoding实战-从prd到代码生成.md)

### 产品与设计工作流

1. [25｜Claude Code + Figma：从 PRD 到设计稿](articles/25-25-claude-code-figma-ai-画原型完整教程-从-prd-到设计稿只要-5-分钟-crazyrouter-连载-25.md)
2. [28｜Claude Code + Mermaid 一键生成架构图、时序图、流程图](articles/28-28-claude-code-mermaid-一键生成架构图-时序图-流程图-crazyrouter-连载-28.md)
3. [36｜用设计和编程 Agent 设计网站](articles/36-36-claude-code-接入-crazyrouter-连载-36-用设计和编程-agent-设计网站.md)

## 常见错误

### 1. Claude Code 的 Base URL 写成了 `/v1`

错误：

```text
ANTHROPIC_BASE_URL=https://cn.crazyrouter.com/v1
```

正确：

```text
ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
```

Claude Code 会自己拼接 `/v1/messages`。如果你手动加 `/v1`，日志里可能出现 `/v1/v1/messages`。

### 2. 把 OpenAI compatible 地址用于 Claude Code

OpenAI SDK / HTTP 请求用：

```text
https://cn.crazyrouter.com/v1
```

Claude Code 用：

```text
https://cn.crazyrouter.com
```

### 3. Token 没有模型权限

如果返回 `model not allowed`、`403` 或模型不可用，先检查 Crazyrouter 控制台里的 Token 白名单和余额。

### 4. 把真实 API Key 写进仓库

示例里只使用 `YOUR_CRAZYROUTER_API_KEY`。真实 Token 不要提交到 Git，也不要长期放进公开对话上下文。

## 相关链接

- [Crazyrouter 控制台](https://crazyrouter.com/console?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)
- [Crazyrouter 价格与模型](https://crazyrouter.com/pricing?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)
- [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)
- [API Endpoint 说明](https://docs.crazyrouter.com/api-endpoint?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)
- [Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)

## 完整目录

| 序号 | 文章 |
|-|-|
| 01 | [01｜Claude Code 接入 Crazyrouter 快速入门与配置](articles/01-01-claude-code-接入-crazyrouter-快速入门与配置.md) |
| 02 | [02｜Claude Code 接入 Crazyrouter 的工程实践](articles/02-02-claude-code-接入-crazyrouter-的工程实践.md) |
| 03 | [03｜Claude Code 接入 Crazyrouter 的企业级应用实战](articles/03-03-claude-code-接入-crazyrouter-的企业级应用实战.md) |
| 04 | [04｜Claude Code 接入 Crazyrouter 连载 04：第一章：快速上手](articles/04-04-claude-code-接入-crazyrouter-连载-04-第一章-快速上手.md) |
| 05 | [05｜通过 Crazyrouter 在 Claude Code 中统一接入国内模型](articles/05-05-通过-crazyrouter-在-claude-code-中统一接入国内模型.md) |
| 06 | [06｜Claude Code 接入 Crazyrouter 连载 06：第三章：入门基础操作](articles/06-06-claude-code-接入-crazyrouter-连载-06-第三章-入门基础操作.md) |
| 07 | [07｜Claude Code 接入 Crazyrouter 连载 07：第四章：文本处理与创作](articles/07-07-claude-code-接入-crazyrouter-连载-07-第四章-文本处理与创作.md) |
| 08 | [08｜Claude Code 接入 Crazyrouter 连载 08：第五章：文档管理与处理](articles/08-08-claude-code-接入-crazyrouter-连载-08-第五章-文档管理与处理.md) |
| 09 | [09｜Claude Code 接入 Crazyrouter 连载 09：第六章：数据处理与分析](articles/09-09-claude-code-接入-crazyrouter-连载-09-第六章-数据处理与分析.md) |
| 10 | [10｜Claude Code 接入 Crazyrouter 连载 10：第七章：个性化工作流](articles/10-10-claude-code-接入-crazyrouter-连载-10-第七章-个性化工作流.md) |
| 11 | [11｜Claude Code 接入 Crazyrouter 连载 11：第八章：提示词优化技巧](articles/11-11-claude-code-接入-crazyrouter-连载-11-第八章-提示词优化技巧.md) |
| 12 | [12｜Claude Code 接入 Crazyrouter 连载 12：第九章：常用快捷键](articles/12-12-claude-code-接入-crazyrouter-连载-12-第九章-常用快捷键.md) |
| 13 | [13｜Claude Code 接入 Crazyrouter 连载 13：第十章：用编程的思维解决问题](articles/13-13-claude-code-接入-crazyrouter-连载-13-第十章-用编程的思维解决问题.md) |
| 14 | [14｜第十一章：Claude高级功能使用：Crazyrouter 连载 14](articles/14-14-第十一章-claude高级功能使用-crazyrouter-连载-14.md) |
| 15 | [15｜第十二章：让Claude自动解决问题：Crazyrouter 连载 15](articles/15-15-第十二章-让claude自动解决问题-crazyrouter-连载-15.md) |
| 16 | [16｜Claude Code 接入 Crazyrouter 连载 16：第十三章：复用文档解决同类问题](articles/16-16-claude-code-接入-crazyrouter-连载-16-第十三章-复用文档解决同类问题.md) |
| 17 | [17｜Claude Code 接入 Crazyrouter 连载 17：从创意到 AI 产品](articles/17-17-claude-code-接入-crazyrouter-连载-17-从创意到-ai-产品.md) |
| 18 | [18｜Claude Code 接入 Crazyrouter 连载 18：AI 时代，会说话就会编程](articles/18-18-claude-code-接入-crazyrouter-连载-18-ai-时代-会说话就会编程.md) |
| 19 | [19｜Claude Code 接入 Crazyrouter 连载 19：学会 AI 编程工具](articles/19-19-claude-code-接入-crazyrouter-连载-19-学会-ai-编程工具.md) |
| 20 | [20｜Claude Code 接入 Crazyrouter 连载 20：找到好点子](articles/20-20-claude-code-接入-crazyrouter-连载-20-找到好点子.md) |
| 21 | [21｜Claude Code 接入 Crazyrouter 连载 21：动手做出原型](articles/21-21-claude-code-接入-crazyrouter-连载-21-动手做出原型.md) |
| 22 | [22｜Claude Code 接入 Crazyrouter 连载 22：为原型注入 AI 能力](articles/22-22-claude-code-接入-crazyrouter-连载-22-为原型注入-ai-能力.md) |
| 23 | [23｜Claude Code 接入 Crazyrouter 连载 23：完整项目实战](articles/23-23-claude-code-接入-crazyrouter-连载-23-完整项目实战.md) |
| 24 | [24｜Claude Code 接入 Crazyrouter 连载 24：AICoding实战：从Prd到代码生成](articles/24-24-claude-code-接入-crazyrouter-连载-24-aicoding实战-从prd到代码生成.md) |
| 25 | [25｜Claude Code + Figma：AI 画原型完整教程，从 PRD 到设计稿只要 5 分钟：Crazyrouter 连载 25](articles/25-25-claude-code-figma-ai-画原型完整教程-从-prd-到设计稿只要-5-分钟-crazyrouter-连载-25.md) |
| 26 | [26｜Claude+Cursor+FigmaMasterGo四步生成高端的产品原型图（附提示词和步骤）：Crazyrouter 连载 26](articles/26-26-claude-cursor-figmamastergo四步生成高端的产品原型图-附提示词和步骤-crazyrouter-连载-26.md) |
| 27 | [27｜Claude Code 打通 Figma，2 分钟搞定产品UI界面（附保姆级安装教程）：Crazyrouter 连载 27](articles/27-27-claude-code-打通-figma-2-分钟搞定产品ui界面-附保姆级安装教程-crazyrouter-连载-27.md) |
| 28 | [28｜Claude Code + Mermaid 一键生成架构图、时序图、流程图：Crazyrouter 连载 28](articles/28-28-claude-code-mermaid-一键生成架构图-时序图-流程图-crazyrouter-连载-28.md) |
| 29 | [29｜Claude Code 接入 Crazyrouter 连载 29：claude code从需求到低保真线框图，再到高保真UI原型，全流程](articles/29-29-claude-code-接入-crazyrouter-连载-29-claude-code从需求到低保真线框图-再到高保真ui原型-全流程.md) |
| 30 | [30｜Claude Code 接入 Crazyrouter 连载 30：用claude code 画系统功能模块图和系统架构图](articles/30-30-claude-code-接入-crazyrouter-连载-30-用claude-code-画系统功能模块图和系统架构图.md) |
| 31 | [31｜Pencil + Claude Code：快速原型图：Crazyrouter 连载 31](articles/31-31-pencil-claude-code-快速原型图-crazyrouter-连载-31.md) |
| 32 | [32｜AI产品经理提效篇：Claude 如何快速承接多角色与上下文：Crazyrouter 连载 32](articles/32-32-ai产品经理提效篇-claude-如何快速承接多角色与上下文-crazyrouter-连载-32.md) |
| 33 | [33｜Claude Code 通过 Crazyrouter 构建互动小说创作工具](articles/33-33-claude-code-通过-crazyrouter-构建互动小说创作工具.md) |
| 34 | [34｜Claude Code 接入 Crazyrouter 连载 34：B 端产业应用场景方向参考](articles/34-34-claude-code-接入-crazyrouter-连载-34-b-端产业应用场景方向参考.md) |
| 35 | [35｜Claude Code 接入 Crazyrouter 连载 35：C 端消费场景灵感参考](articles/35-35-claude-code-接入-crazyrouter-连载-35-c-端消费场景灵感参考.md) |
| 36 | [36｜Claude Code 接入 Crazyrouter 连载 36：用设计和编程 Agent 设计网站](articles/36-36-claude-code-接入-crazyrouter-连载-36-用设计和编程-agent-设计网站.md) |

## License

MIT
