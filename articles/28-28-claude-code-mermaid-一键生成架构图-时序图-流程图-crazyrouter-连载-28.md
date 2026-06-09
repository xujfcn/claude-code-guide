# 28｜Claude Code + Mermaid 一键生成架构图、时序图、流程图：Crazyrouter 连载 28

> 本文是 Crazyrouter Claude Code 系列第 28 篇。本文会围绕「Claude Code + Mermaid 一键生成架构图、时序图、流程图：Crazyrouter 连载 28」展开，重点覆盖 Claude Code + Mermaid 一键生成架构图、时序图、流程图、**用Claude Code生成Mermaid代码**、**生成时序图、流程图**。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code) 完成基础配置。

## Claude Code + Mermaid 一键生成架构图、时序图、流程图

本文将手把手教你如何用 **Claude Code生成Mermaid代码** ，并在Mermaid、draw.io、ProcessOn等工具中渲染成精美图表。

## **用Claude Code生成Mermaid代码**

使用的工具是 Cursor + Claude Code，在Claude Code中输入结构化提示词，让它生成总体架构图，输出Mermaid代码。

## **生成时序图、流程图**

有了Mermaid代码，那么生成时序图、流程图等图表也是同样的简单

## **使用Mermaid工具渲染图表（最快捷）**

打开Mermaid官网，在Dashboard页面，选择新建图表

将Mermaid代码复制到左侧的CODE位置，右侧自动会生成架构图表，可以使用工具进行架构图风格的调整

## **使用draw.io工具渲染图表**

打开draw.io网站，点击“+”--->Mermaid...，将Mermaid代码粘贴到弹框中，点击“插入”即可生成架构图，可以使用工具进行架构图风格的调整

## **使用ProcessOn工具渲染图表（国内用户首选）**

打开rocessOn网站，点击“新建”--->Mermaid，将Mermaid代码粘贴到页面左侧，则自动生成Mermaid图表，有条件的可以进行“图形化编辑”

## **生成时序图、流程图**

有了Mermaid代码，那么生成时序图、流程图等图表也是同样的简单

## **总 结**

通过Claude + Mermaid的组合，我们实现了：

- **效率提升：** 从小时级到分钟级的图表生成速度
- **质量提升：** 专业统一的图表风格
- **维护便捷：** 文本格式方便迭代和版本管理

现在就开始你的AI绘图之旅吧！生成架构图、时序图、流程图、甘特图、状态图，你必须记住这个高效工作流：

**描述需求 → 生成Mermaid代码 → 粘贴到渲染工具 → 精细化调整**

---

## 相关阅读

- 上一篇：[第 27 篇](./27-27-claude-code-打通-figma-2-分钟搞定产品ui界面-附保姆级安装教程-crazyrouter-连载-27.md)
- 下一篇：[第 29 篇](./29-29-claude-code-接入-crazyrouter-连载-29-claude-code从需求到低保真线框图-再到高保真ui原型-全流程.md)
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
