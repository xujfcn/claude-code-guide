# 30｜Claude Code 接入 Crazyrouter 连载 30：用claude code 画系统功能模块图和系统架构图

> 本文是 Crazyrouter Claude Code 系列第 30 篇。本文会围绕「Claude Code 接入 Crazyrouter 连载 30：用claude code 画系统功能模块图和系统架构图」展开，重点覆盖 用claude code 画系统功能模块图和系统架构图、画系统功能模块图、三、系统架构设计图的生成。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code) 完成基础配置。

## 用claude code 画系统功能模块图和系统架构图

## 画系统功能模块图

### 1、使用/plan 模式

给claude code 一张参考图，让它提取模块图的风格、布局、配色和样式，这里我给的参照图是之前在Trae 里生成的功能模块图。

> claude code 截图粘贴快捷键是 Alt + v , 本文用的是Win11 的系统。

### 2、参照图风格、配色、布局提取完毕

### 3、这里用《功能模块文档.md》

### 4、分析文档内容，并创建计划，然后开始执行计划

### 5、生成的系统功能模块图对比

原来用Trae画的功能图：

用claude code的复刻的功能图：

claude code + GLM-5 是可靠的，和原图基本是一致的，而且一次对话即可完成，无需修正。

> 这里你也可以上传你自己的旧的参照图，根据你自己的风格、配色、布局进行模块图的生成。

配置文本：

```json

{
  "args": [
    "-y",
    "@z_ai/mcp-server"
  ],
  "command": "npx",
  "env": {
    "Z_AI_MODE": "VISION"
  },
  "type": "stdio"
}
```

## 三、系统架构设计图的生成

1. 这里我没再上传系统架构图的参照图让它学习，直接生成。

还帮我分析了功能图和系统架构图的区别：

2. 生成的系统架构图效果：

一次生成，看起来效果还行。

### 四、经验总结

1. 自从使用了claude code后，我已经不再使用Tare工具了，自从上次系统架构图生成实验后，大模型又发展了8个月了，很多东西已经发生了翻天覆地的变化了，现在让ai生成一个好看的系统架构图已经不是什么难事了；

2. claude code 除了cli 命令行方式让普通人觉得不友好外，其他的都是优点；

3. 如果想要画特定风格、配色、布局的功能图或系统架构设计图，你可以先上传一张参照图，先让大模型学习一下，再开始画图。

4. claude code 虽然是cli 的方式，但画图仍然也是扛扛的。

---

## 相关阅读

- 上一篇：[第 29 篇](./29-29-claude-code-接入-crazyrouter-连载-29-claude-code从需求到低保真线框图-再到高保真ui原型-全流程.md)
- 下一篇：[第 31 篇](./31-31-pencil-claude-code-快速原型图-crazyrouter-连载-31.md)
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
