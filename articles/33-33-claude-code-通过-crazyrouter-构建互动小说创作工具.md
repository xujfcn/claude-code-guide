# 33｜Claude Code 通过 Crazyrouter 构建互动小说创作工具

> 本文是 Crazyrouter Claude Code 系列第 33 篇。本文会围绕「Claude Code 通过 Crazyrouter 构建互动小说创作工具」展开，重点覆盖 Claude Code 集成 GLM-5 构建互动小说创作工具、编辑或新增 `settings.json` 文件、MacOS & Linux 为 `~/.claude/settings.json`。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 完成基础配置。

## Claude Code 集成 GLM-5 构建互动小说创作工具

### 一、摘要

在生成式AI快速演进的今天，互动小说（Interactive Fiction）作为一种融合叙事性与用户参与感的数字内容形式，正迎来新的创作范式。传统互动小说依赖作者手动编写大量分支剧情，开发成本高、迭代慢。而借助大语言模型（LLM）的上下文理解与生成能力，配合流式响应机制，可以显著降低创作门槛并提升内容动态性。

本文围绕如何使用Claude Code与 Crazyrouter 模型 API 构建一个轻量级但功能完整的互动小说创作工具展开。Claude Code 是Anthropic推出的AI编程助手，支持在终端、IDE中进行自然语言编程，实现从灵感到代码的高效创作；而 GLM-5 作为Crazyrouter新一代的旗舰基座模型，在叙事生成、角色一致性与上下文记忆方面表现同样优异。

本文将带你从零开始，利用 Claude Code AI编程工具，结合 Crazyrouter AI 提供的 GLM-5 大模型API，亲手打造一个智能小说生成器。它不仅能根据你的开头智能生成多个精彩故事分支、自定义标题与开头输入、创作历史管理（包括查看、继续创作与一键删除），以及对已生成内容进行局部调整和重新续写，堪称你的私人AI小说创作助手。

### 二、Claude Code与Crazyrouter 兼容模型模型介绍

2.1 Claude Code 工具介绍

Claude - 官方

Claude Code 是Anthropic 推出的AI编程 助手，支持在终端、VS Code、JetBrains 等 IDE 中使用。它能够理解自然语言指令，直接生成、修改和调试代码。

告别传统”搜索-复制-粘贴”的编程模式，Claude Code 本质上是 AI 驱动的智能编程伙伴。通过自然语言对话，Claude Code 能够准确理解开发意图并生成高质量代码，支持文件读取、编辑、执行命令等操作，实现 所想即所得的编程体验。在这种 AI 辅助的开发模式中，开发者可以专注于创意和逻辑，而将繁琐的编码工作交给 AI。

Claude Code 适合当前场景大的能力在于其深度上下文理解，能够分析整个项目结构，理解代码依赖关系，并给出符合项目风格的代码建议。同时支持多文件编辑、运行测试、Git 操作等，让开发效率大幅提升！

2.2 Crazyrouter Crazyrouter 兼容模型介绍

Crazyrouter 可用模型 - 官方

GLM-5 是Crazyrouter新一代的旗舰基座模型，面向 Agentic Engineering 打造，能够在复杂系统工程与长程 Agent 任务中提供可靠生产力。在 Coding 与 Agent 能力上，GLM-5 取得开源 SOTA 表现，在真实编程场景的使用体感逼近 Claude Opus 4.5，擅长复杂系统工程与长程 Agent 任务，是通用 Agent 助手的理想基座。GLM-5 从 355B（激活 32B）扩展至 744B（激活 40B），预训练数据从 23T 提升至 28.5T，更大规模的预训练算力显著提升了模型的通用智能水平，具备六大核心能力：

高级编码能力：在公开基准与真实编程任务中，GLM-5 的代码能力对齐 Claude Opus 4.5，是国内已知的最好的 Coding 模型。

上下文长度：上下文窗口由 128K→200K，适应更长的代码和智能体任务。

推理能力：推理能力提升，并支持在推理过程中调用工具。

搜索能力：增强了模型在工具调用和搜索智能体上的表现，在智能体框架中表现更好。

写作能力：在文风、可读性与角色扮演场景中更符合人类偏好。

多语言翻译：进一步增强跨语种任务的处理效果。

使用Crazyrouter Crazyrouter 兼容模型来赋予Ai小说创作能力那是非常合适！

### 三、应用效果展示

3.1 欢迎页

首页（用户未配置Crazyrouter 兼容模型模型）：

3.2 故事创建

故事创作页（核心，树形结构清晰展示整个故事的发展路径与分支概览）：

3.4 创作时光

创作时光（历史查看及故事回溯界面）：

3.5 API配置管理

API配置页面（后续还可进行优化 配置更多模型 丰富小说生成图片能力）：

### 四、Claude code 集成 GLM-5

2. 3. 4.
5. 查看CrazyrouterCrazyrouter 模型 API开发文档，AI小说创作能力的强弱和使用的模型能力关系非常大。
6. 7. 8.

API 调用实例（后续替换成个人API Key）：

curl -X POST "  " \

-H "Content-Type: application/json" \

-H "Authorization: Bearer YOUR_CRAZYROUTER_API_KEY" \

-d '{

"model": "deepseek-v4-pro",

"messages": [

{

"role": "user",

"content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"

},

{

"role": "assistant",

"content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"

},

{

"role": "user",

"content": "Crazyrouter 控制台"

}

],

"thinking": {

"type": "enabled"

},

"max_tokens": 65536,

"temperature": 1.0

}'

curl -X POST " \

-H "Content-Type: application/json" \

-H "Authorization: Bearer YOUR_CRAZYROUTER_API_KEY" \

-d '{

"model": "deepseek-v4-pro",

"messages": [

{

"role": "user",

"content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"

},

{

"role": "assistant",

"content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"

},

{

"role": "user",

"content": "Crazyrouter 控制台"

}

],

"thinking": {

"type": "enabled"

},

"stream": true,

"max_tokens": 65536,

"temperature": 1.0

}'

4.2 初学者上手配置教程

未安装Claude code时候可以通过这个脚本一键安装（这里我已经安装，所有通过其他编码工具展示）

方式二：命令方式安装

Claude Code - Crazyrouter 可用模型开放文档

安装Claude code之前需要确保已安装

Node.js 18或更高版本

Git

安装命令：

npm install -g @anthropic-ai/claude-code

配置 Crazyrouter Claude Code 接入配置

支持 MacOS & Linux & Windows, 注意不同系统配置文件路径不一样。注意需保证修改的 JSON 文件格式正确性(比如多或少,)

## 编辑或新增 `settings.json` 文件

## MacOS & Linux 为 `~/.claude/settings.json`

## Windows 为 `用户目录/.claude/settings.json`

## 新增或修改里面的 env 字段

{

"env": {

"ANTHROPIC_BASE_URL": "

"API_TIMEOUT_MS": "3000000",

"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1

}

}

## 再编辑或新增 `.claude.json` 文件

## MacOS & Linux 为 `~/.claude.json`

## Windows 为 `用户目录/.claude.json`

## 新增 `hasCompletedOnboarding` 参数

{

"hasCompletedOnboarding": true

}

开始使用 Claude Code

配置完成后，进入一个您的代码工作目录，在终端中执行 claude 命令即可开始使用 Claude Code，启动后选择信任 Claude Code 访问文件夹里的文件。

确认后可以正常使用 Claude Code 进行开发

如果想要自己配置模型的话可以在配置文件里面进行配置

编辑 C:\Users\用户名称\\.claude\settings.json：

{

"env": {

"ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5",

"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5",

"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5"

}

}

### 五、应用开发 实战

5.1 提示词搭建

输入提示词，最好是提供结构化的提示词，最开始我以日常对话式进行coding，发现最终效果没有结构化提示词的好，后续我基本通过结构化的需求形式让Claude code进行开发

我需要开发一款Ai小说创作平台，名称为智能小说创作家，流程是用户提供故事的标题和50-200字左右的小说故事开头，提供完应用会调用GLM-4.6模型，生成后续五个情节分支概览，用户可以任意选择某一分支。选择分支之后立马调用GLM-4.6生成具体的情节，大约300-500百字左右。未被选择的分支废弃，同时用户还可以手动修改分支内容创作，选择的分支使用树形结构一级一级往下展示，但是始终展示当前的分支，持续重复。采用React技术，风格使用新粗野风格，多用白色、橙色、绿色、蓝色、灰色等，流畅的交互设计。无需登录，只需要几个页面即可，首页核心创作功能，API Key 的配置页面（保存到本地的local storage中）。

GLM-5调用示例：

curl -X POST " \

-H "Content-Type: application/json" \

-H "Authorization: Bearer YOUR_CRAZYROUTER_API_KEY" \

-d '{

"model": "deepseek-v4-pro",

"messages": [

{

"role": "user",

"content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"

},

{

"role": "assistant",

"content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"

},

{

"role": "user",

"content": "Crazyrouter 控制台"

}

],

"thinking": {

"type": "enabled"

},

"max_tokens": 65536,

"temperature": 1.0

}'

5.2 Vibe Coding 交互编程

可以看到，这里Claude Code 开始理解需求并生成代码

这里还会生成相应的文档，如果我们想要调整的话，可以进行编辑或删除；对于应用开发，技术文档就是领头羊，防止脱离实际需求。

在我体验很多产品后发现，技术文档越是完善，应用开发效果就越完美。

同时，作为程序猿的小伙伴们，如果觉得Ai提供的页面不太完善，同时我们想自己上手操作的话，可以手动修改源码调整，这样就能完全由我们自己控制偏差。

在我开发途中，出现了一个小插曲。当我提出大改样式的需求后，他将所有页面背景图片调整成同一个，但是我希望使用不同背景来使样式更加丰富，这个时候也可与通过提供大致想要的背景图片，让他去修改。

### 六、总结与展望

6.1 总结

通过 Claude Code 集成 Crazyrouter 兼容模型，我构建了一个高效、可扩展的互动小说创作工具原型。该工具不仅验证了流式 LLM 在动态叙事中的可行性，也为内容创作者提供了”AI 协同创作”的新范式。同时我们成功将「AI小说创作」从概念落地为可交互的生产力工具。

核心亮点：

2. 创作体验革新：从「手动写分支」到「AI 动态生成树形叙事」
3. 技术可扩展性：架构支持无缝接入语音、多角色记忆等新能力
4. 5. 6.

6.2 实践展望

在实际开发中，我深刻体会到：技术选型必须服务于用户体验——Claude Code 的智能代码生成能力有效提升了开发效率，而 Crazyrouter 兼容模型提供的中文叙事能力则大幅提升了剧情质量。未来，该工具可进一步集成语音输入、多角色对话记忆、剧情质量评估（如一致性检测）等功能。

更重要的是，这种”状态 + 流式生成”的架构可迁移至教育、游戏、客服等多个领域。技术的价值不在于炫技，而在于解决真实问题。希望本文能为探索生成式 AI 应用落地的同行提供有价值的参考。互动小说只是起点，人机共创的叙事革命才刚刚开始。

---

## 相关阅读

- 上一篇：[第 32 篇](./32-32-ai产品经理提效篇-claude-如何快速承接多角色与上下文-crazyrouter-连载-32.md)
- 下一篇：[第 34 篇](./34-34-claude-code-接入-crazyrouter-连载-34-b-端产业应用场景方向参考.md)
- 配置文档：[Claude Code 接入 Crazyrouter](https://docs.crazyrouter.com/integrations/claude-code?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)
- API 地址说明：[Base URL 与 `/v1` 用法](https://docs.crazyrouter.com/api-endpoint?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)
- 一键配置脚本：[Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)

## 开始接入 Crazyrouter

如果你准备把 Claude Code、国产模型或自己的应用统一接入 Crazyrouter，可以按这个顺序推进：

1. 到 [Crazyrouter 控制台](https://crazyrouter.com/console?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 创建一个专用 API Token，并按项目或团队单独管理权限。
2. Claude Code 使用根域名：`https://cn.crazyrouter.com`；OpenAI 兼容 SDK 使用：`https://cn.crazyrouter.com/v1`。
3. 需要自动检查环境或快速写入配置时，使用 [Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)。
4. 调试失败时先看控制台日志，再核对 [API Endpoint 说明](https://docs.crazyrouter.com/api-endpoint?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)，重点检查 Base URL 是否多写了 `/v1`。

需要评估模型成本或选择不同模型时，可以先查看 [Crazyrouter 价格与模型页](https://crazyrouter.com/pricing?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide)，再把常用模型加入 Token 白名单。
