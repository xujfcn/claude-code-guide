# 05｜通过 Crazyrouter 在 Claude Code 中统一接入国内模型

> 本文是 Crazyrouter Claude Code 系列第 05 篇。本文会围绕「通过 Crazyrouter 在 Claude Code 中统一接入国内模型」展开，重点覆盖 为什么统一走 Crazyrouter、Claude Code 的正确配置、OpenAI 兼容应用的正确配置。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code) 完成基础配置。

Claude Code 可以用 Claude 系列模型，也可以通过 Anthropic Messages 兼容协议使用部分国产模型。对站内读者来说，重点不是分别去各家平台注册、开通、复制 Key，而是把模型统一接入 Crazyrouter。

统一入口如下：

```text
ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
ANTHROPIC_API_KEY=YOUR_CRAZYROUTER_API_KEY
```

Claude Code 会自己拼接 `/v1/messages`，所以 `ANTHROPIC_BASE_URL` 必须填写根域名，不要写成 `https://cn.crazyrouter.com/v1`，也不要写完整的 `/v1/messages`。

## 为什么统一走 Crazyrouter

把 Claude Code 和国产模型统一放到 Crazyrouter 后面，有几个实际好处：

- 一个 Token 管理多类模型，不需要在多个平台之间复制密钥。
- 在控制台里统一查看日志、余额、失败原因和模型调用情况。
- 可以给 Claude Code 单独创建 Token，设置预算和模型白名单，避免和其他工具混用。
- 国内网络优先使用 `https://cn.crazyrouter.com`，减少跨境线路波动。
- 后续切换模型时，只需要调整模型名或控制台配置，不需要重写整套接入流程。

## Claude Code 的正确配置

macOS / Linux：

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

重新打开终端后执行：

```powershell
claude
```

如果你希望自动检查 Git、Node.js、Claude Code 并写入环境变量，可以使用 Crazyrouter 的一键配置仓库：[Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)。

## OpenAI 兼容应用的正确配置

如果你不是配置 Claude Code，而是在自己的应用、SDK、后端服务里调用 OpenAI 兼容接口，则使用 `/v1` 地址：

```text
base_url=https://cn.crazyrouter.com/v1
```

示例：

```bash
curl https://cn.crazyrouter.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_CRAZYROUTER_API_KEY" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [
      {"role": "user", "content": "用一句话说明 Crazyrouter 的作用"}
    ]
  }'
```

## 模型选择建议

不要把“国产模型接入”理解成跳转到某个厂商平台。站内文章默认采用 Crazyrouter 的模型列表和 Token 权限作为准入标准。

建议按任务选型：

- 代码阅读、重构、复杂工程任务：优先选择 Claude 系列或经过 Claude Code 兼容验证的 Coding 模型。
- 中文文档、总结、内容处理：选择中文能力强、成本适中的通用模型。
- 长文本项目分析：选择上下文更长、输出稳定的模型。
- 批量任务：优先选择成本更低、吞吐更稳的模型，并给 Token 设置预算。

可用模型以 Crazyrouter 控制台和 `GET https://cn.crazyrouter.com/v1/models` 的返回为准。

## 常见错误

### 1. Base URL 写错

Claude Code：

```text
ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
```

OpenAI 兼容 SDK：

```text
base_url=https://cn.crazyrouter.com/v1
```

如果日志里出现 `/v1/v1/messages`、`/v1/v1/models`，通常是把 `/v1` 重复写进了 Base URL。

### 2. Token 没有对应模型权限

如果返回 `model not allowed` 或 403，检查 Crazyrouter 控制台里的 Token 白名单。给 Claude Code 单独建一个 Token，通常更容易排查。

### 3. 把示例 Key 写进代码

文章和示例都使用 `YOUR_CRAZYROUTER_API_KEY` 占位。真实 Token 不要提交到 Git，也不要发给 AI 工具作为长期上下文。

## 推荐工作流

1. 在 Crazyrouter 控制台创建 Claude Code 专用 Token。
2. 配置 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`。
3. 启动 Claude Code，先用 `/status` 检查当前模型与状态。
4. 在 Crazyrouter 控制台确认日志能看到请求。
5. 再根据任务切换模型或调整 Token 白名单。

这套流程适合 Claude 系列模型，也适合通过 Crazyrouter 兼容接入的国产模型。读者不需要被引导到其他模型平台，所有密钥、计费、日志和排障都回到 Crazyrouter 内完成。

---

## 相关阅读

- 上一篇：[第 04 篇](./04-04-claude-code-接入-crazyrouter-连载-04-第一章-快速上手.md)
- 下一篇：[第 06 篇](./06-06-claude-code-接入-crazyrouter-连载-06-第三章-入门基础操作.md)
- 配置文档：[Claude Code 接入 Crazyrouter](https://docs.crazyrouter.com/integrations/claude-code)
- API 地址说明：[Base URL 与 `/v1` 用法](https://docs.crazyrouter.com/api-endpoint)
- 一键配置脚本：[Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)

## 开始接入 Crazyrouter

如果你准备把 Claude Code、国产模型或自己的应用统一接入 Crazyrouter，可以按这个顺序推进：

1. 到 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个专用 API Token，并按项目或团队单独管理权限。
2. Claude Code 使用根域名：`https://cn.crazyrouter.com`；OpenAI 兼容 SDK 使用：`https://cn.crazyrouter.com/v1`。
3. 需要自动检查环境或快速写入配置时，使用 [Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)。
4. 调试失败时先看控制台日志，再核对 [API Endpoint 说明](https://docs.crazyrouter.com/api-endpoint)，重点检查 Base URL 是否多写了 `/v1`。

需要评估模型成本或选择不同模型时，可以先查看 [Crazyrouter 价格与模型页](https://crazyrouter.com/pricing)，再把常用模型加入 Token 白名单。
