# 04｜Claude Code 接入 Crazyrouter 连载 04：第一章：快速上手

> 本文是 Crazyrouter Claude Code 系列第 04 篇。本文会围绕「Claude Code 接入 Crazyrouter 连载 04：第一章：快速上手」展开，重点覆盖 第一章：快速上手、1.1 什么是 Claude Code、为什么非程序员也能轻松使用。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code) 完成基础配置。

## 第一章：快速上手

Claude Code安装全流程

链接：

【win安装claude code必备】

链接：

Claude Code安装视频教程和实战

链接：

## 1.1 什么是 Claude Code

Claude Code 是一个强大的 AI 助手工具，它可以帮助你在电脑上完成各种工作。简单来说，它就像一个随时待命的智能同事，你可以用日常语言和它对话，让它帮你处理文字、分析数据、整理文件等各种任务。

## 为什么非程序员也能轻松使用

Claude Code 的设计非常友好，你不需要懂任何编程知识就能使用它：

- 自然语言交互：用中文直接和它对话，就像和朋友聊天一样简单
- 支持界面操作：虽然Claude Code本身是命令行工具，但我们也可以在图形界面中使用
- 智能理解能力：它能理解你的意图，即使表达不够精确也能给出有用的帮助
- 所见即所得：你可以直接看到它处理的结果，不需要学习复杂的命令

## 1.2 安装 Trae 国内版与 Claude Code 插件

### 步骤 1：访问 Trae 官网

打开浏览器，访问

### 步骤 2：下载安装包

- 根据你的操作系统选择对应的版本：

  - Windows 版（支持 Windows 10/11）
  - macOS Intel 芯片版
  - macOS M 系列芯片版
- 点击下载按钮，等待安装包下载完成（约 613MB）

### 步骤 3：安装 Trae

- Windows：双击下载的安装包，按照安装向导完成安装
- macOS：打开下载的 .dmg 文件，将 Trae 拖到应用程序文件夹
- 安装时建议选择 SSD 存储路径，并预留 1GB 以上空间

### 步骤 4：启动 Trae

安装完成后，打开 Trae，你会看到一个与 VS Code 非常相似的编辑器界面。

## 在 Trae 中安装 Claude Code 插件

Trae 完全兼容 VS Code 的插件市场，安装 Claude Code 插件的步骤与在 VS Code 中完全相同。

### 步骤 1：打开插件市场

在 Trae 左侧边栏，点击插件图标（四个方块组成的图标），或者使用快捷键 `Ctrl+Shift+X` （Windows/Linux）或 `Cmd+Shift+X` （macOS）。

### 步骤 2：搜索 Claude Code

在搜索框中输入 "Claude Code"，在搜索结果中找到官方插件。

### 步骤 3：安装插件

点击插件右侧的"安装"按钮，等待安装完成。

## 首次启动 Claude Code

### 步骤 1：打开 Claude Code

安装完成后，不需要离开安装界面，在 Trae 顶部会出现 Claude Code 的图标（一个对话气泡图标），点击它。

此时，你的代码区域就会出现 Claude Code 的聊天窗口。

### 步骤 2：登录账户

首次使用需要登录 Anthropic 账户：

- 点击登录按钮
- 在浏览器中完成登录或注册
- 在弹出的对话框中点击确认
- 等待完成登录验证

由于国内用户被Claude官方屏蔽，推荐你使用下一张“接入国内大模型”的办法来使用Claude Code。

### 步骤 3：开始使用

登录成功后，你就可以开始使用 Claude Code 了！在聊天框中输入你的问题或需求，Claude Code 会给出回应。

## Trae 相比 VS Code 的优势

作为 VS Code 的替代品，Trae 国内版具有以下优势：

1. 完全兼容 VS Code：界面、快捷键、插件生态与 VS Code 完全一致
2. 国内网络优化：插件下载速度更快，访问更稳定
3. 内置 AI 功能：除了 Claude Code 插件，还提供额外的 AI 辅助功能
4. 更好的中文支持：针对中文用户进行了优化
5. 免费使用：完全免费，可以永久使用

## 常见问题

Q：Trae 是免费的吗？

A：是的，Trae 国内版完全免费，可以永久使用。

Q：Trae 和 VS Code 有什么区别？

A：Trae 是基于 VS Code 开发的，界面和操作方式几乎完全相同。主要区别是 Trae 针对国内用户进行了优化，网络访问更快，并且内置了一些额外的 AI 功能。

Q：Trae 支持 VS Code 的所有插件吗？

A：是的，Trae 完全兼容 VS Code 的插件生态，可以安装和使用所有 VS Code 插件。

Q：安装需要多长时间？

A：通常只需要几分钟，具体时间取决于你的网络速度。

Q：可以在多台电脑上使用吗？

A：可以，你可以在任何电脑上安装 Trae 和 Claude Code 插件，使用同一个账户登录。

Q：Trae 的快捷键和 VS Code 一样吗？

A：是的，Trae 的快捷键与 VS Code 完全相同，你可以无缝切换使用。

## 1.3 认识 Claude Code 界面

用 Trae 随便打开一个文件，在上方右上角处就可以看到 Claude Code 图标。点击它可以打开 Claude Code 界面。

打开 Claude Code 后，你会看到一个友好的界面。让我们来认识一下各个部分的功能。

## 聊天窗口

聊天窗口是 Claude Code 的核心区域，位于界面左侧。

### 输入框

在聊天窗口底部，你会看到一个输入框，这里是你的主要工作区域：

- 在这里输入你的问题或需求
- 支持多行输入
- 可以粘贴文本内容
- 按 Enter 键发送消息

### 对话历史

输入框上方是对话历史区域：

- 显示你和 Claude Code 的所有对话
- 可以向上滚动查看历史记录
- 每条消息都有时间戳
- 可以复制任何一条消息的内容

### 消息类型

- 你的消息：通常显示在右侧，带有你的头像
- Claude 的回复：通常显示在左侧，带有 AI 图标
- 系统消息：显示操作提示或错误信息

## 核心操作

### 与 Claude Code 对话

- 发送消息：在输入框中输入内容后，按 Enter 键发送
- 中断生成：如果生成过程中需要中断，点击输入框旁边的“停止”按钮

### 快捷操作

点击输入框旁边的“/”按钮，展开快捷操作菜单。

菜单内容包括：

- 对话处理：新建、恢复、清空
- 文件操作：上传文件作为参考、指定文件路径
- 配置操作
- 斜杠命令

### 快捷命令

在聊天对话框中，输入 `/` 后，会弹出快捷菜单。输入 `@` 后，会弹出文件选择菜单。

### 思考模式开关

输入框旁边有一个“思考”开关按钮，用于切换思考模式。

### 执行模式

在输入框下方最左边有当前的执行模式，点击它可以切换为其他模式。模式包括：

- Plan mode：计划模式，用于生成代码计划
- Ask before edits：编辑前询问模式，用于确认是否对生成的代码进行修改
- Edit automatically：自动编辑模式，直接对生成的代码进行修改

现在你已经熟悉了 Claude Code 的界面，让我们开始第一次对话吧！

## 1.4 使用 Z Code 来使用 Claude Code

Z Code 是由Crazyrouter推出的一款轻量级 AI 协同开发工具，它为开发者提供了一个统一、友好的可视化桌面，让使用 Claude Code 等 AI 编程工具变得更加简单直观。

## 什么是 Z Code

Z Code 是一款处于 Alpha 测试阶段的轻量级代码编辑器，它的核心目标是解决命令行 AI 编程工具（如 Claude Code、Codex、Gemini 等）操作门槛高的问题。通过提供一个统一的可视化界面，Z Code 让强大的 AI 编程助手从只有高手才能驾驭的命令行，走进更多普通开发者的桌面。

### Z Code 的核心特性

1. 统一可视化界面：将多个 AI 编程工具集成到一个友好的图形界面中
2. 一键调用 Claude Code：无需复杂的命令行操作，直接在界面中使用 Claude Code
3. 低门槛使用：开发者仅需一个 API Key 就能开始使用
4. 轻量级设计：启动快速，占用资源少
5. 多 AI 工具集成：除了 Claude Code，还支持 Codex、Gemini 等多种 AI 编程工具

## 为什么可以借 Z Code 来使用 Claude Code

相比直接使用命令行版本的 Claude Code，Z Code 具有以下显著优势：

### 降低使用门槛

- 无需记忆复杂的命令行参数
- 可视化操作，直观易懂
- 适合初学者和经验不足的开发者

### 提升开发效率

- 统一的界面管理多个 AI 工具
- 快速切换不同的 AI 模型
- 减少上下文切换的时间成本

### 更好的用户体验

- 友好的图形界面
- 实时反馈和状态显示
- 支持编辑 AI 的思考过程

### 集成化工作流

- 将 AI 编程工具无缝集成到开发环境
- 支持代码编辑、调试、AI 辅助一体化
- 减少工具间的切换

## 如何获取 Z Code

### 访问官网

打开浏览器，访问 Z Code 官网：

### 下载安装

- 根据你的操作系统选择对应的版本
- 目前支持 Windows 和 macOS 系统
- 下载安装包后按照提示完成安装

注意：Z Code 目前处于 Alpha 测试阶段，可能会有一些功能不完善或存在 bug。建议在使用前备份重要代码。

## 在 Z Code 中使用 Claude Code

### 配置 Claude Code

1. 启动 Z Code：打开已安装的 Z Code 编辑器
2. 打开设置：在菜单栏中找到设置选项
3. 添加 Claude Code：在 AI 工具配置中选择 Claude Code
4. 输入 API Key：输入你的 Anthropic API Key
5. 完成配置：保存配置并测试连接

### 使用 Claude Code

配置完成后，你就可以在 Z Code 中使用 Claude Code 了：

1. 打开聊天窗口：点击界面上的 Claude Code 图标
2. 输入需求：在聊天框中输入你的问题或代码需求
3. 获取响应：Claude Code 会给出相应的代码或建议
4. 应用代码：可以直接将生成的代码应用到你的项目中

### 缺点

- 目前 Z Code 仅支持 Windows 和 macOS 系统
- 功能相对来说更轻量级，无法直接编辑代码
- 不支持直接调试代码，需要通过其他IDE进行调试

## Z Code 与 Trae 的对比

| 特性 | Z Code | Trae |
|-|-|-|
| 开发公司 | Crazyrouter | Trae 团队 |
| 主要定位 | AI 协同开发工具 | AI 原生 IDE |
| Claude Code 集成 | 原生集成 | 通过插件 |
| 界面风格 | 轻量级编辑器 | 类似 VS Code |
| 多 AI 工具支持 | 支持 Claude Code、Codex、Gemini 等 | 主要支持 Claude Code |
| 适用场景 | 快速使用多种 AI 工具 | 完整的 IDE 开发环境 |

## 适用人群

### 适合使用 Z Code 的开发者

1. 初学者：对命令行不熟悉的开发者
2. 快速原型开发者：需要快速生成和测试代码的开发者
3. 多 AI 工具用户：需要使用多种 AI 编程工具的开发者
4. 轻量级需求：不需要完整 IDE 功能的开发者

### 适合使用 Trae 的开发者

1. VS Code 用户：习惯使用 VS Code 的开发者
2. 完整 IDE 需求：需要完整开发环境的开发者
3. 深度集成需求：需要与现有 VS Code 插件生态集成的开发者
4. 长期项目开发：需要稳定、成熟的开发环境的开发者

## 常见问题

Q：Z Code 是免费的吗？

A：目前 Z Code 处于 Alpha 测试阶段，可以免费使用。未来可能会有付费版本。

Q：Z Code 需要付费使用 Claude Code 吗？

A：Z Code 本身不收费，但使用 Claude Code 需要你有 Anthropic 的 API Key，这需要向 Anthropic 购买。

Q：Z Code 支持哪些编程语言？

A：Z Code 本身是一个编辑器，支持多种编程语言。Claude Code 可以处理几乎所有主流编程语言的代码。

Q：可以在 Z Code 中同时使用多个 AI 工具吗？

A：是的，Z Code 支持同时配置和使用多个 AI 工具，你可以在它们之间快速切换。

Q：Z Code 的稳定性如何？

A：由于 Z Code 目前处于 Alpha 测试阶段，可能会有一些不稳定的情况。建议在使用时定期保存代码。

Q：Z Code 可以替代 Trae 吗？

A：这取决于你的需求。如果你只需要使用 AI 编程工具，Z Code 是一个不错的选择。如果你需要一个完整的 IDE 环境，Trae 可能更适合。

## 总结

Z Code 是一个新兴的 AI 协同开发工具，它通过可视化界面大大降低了使用 Claude Code 等 AI 编程工具的门槛。对于初学者或需要快速使用多种 AI 工具的开发者来说，Z Code 是一个值得尝试的选择。

选择使用 Z Code 还是 Trae，主要取决于你的个人需求和开发习惯。如果你习惯使用命令行或需要完整的 IDE 环境，Trae 可能更适合；如果你想要一个简单直观的界面来使用 AI 编程工具，Z Code 是一个很好的选择。

在下一章中，我们将深入学习如何与 Claude Code 进行有效的对话，让 AI 更好地帮助你完成编程任务。

---

## 相关阅读

- 上一篇：[第 03 篇](./03-03-claude-code-接入-crazyrouter-的企业级应用实战.md)
- 下一篇：[第 05 篇](./05-05-通过-crazyrouter-在-claude-code-中统一接入国内模型.md)
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
