# 31｜Pencil + Claude Code：快速原型图：Crazyrouter 连载 31

> 本文是 Crazyrouter Claude Code 系列第 31 篇。本文会围绕「Pencil + Claude Code：快速原型图：Crazyrouter 连载 31」展开，重点覆盖 Pencil + Claude Code：快速原型图、一、Pencil、二、下载安装与配置。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code) 完成基础配置。

## Pencil + Claude Code：快速原型图

> 🔗

## 一、Pencil

Pencil 是一个专门为 AI 时代设计的原型工具。

**说人话就是：它可以被 AI 编程工具直接操控。**

你在 Claude Code 里说一句"给我画一个登录页面"，Pencil 就能自动画出来。

## 二、下载安装与配置

官网下载桌面端，Windows 和 macOS 都支持。

（之前不支持windows我就没折腾，最近开始支持intel/AMDx64了）

### 关键配置

装好后， **Pencil 会自动配置好 MCP 服务。**

可以在claude窗口中输入 **/mcp** 验证一下

但要在 Claude 的配置文件里加个权限设置，不然每次使用时，一直弹窗确认：

配置路径：C:\Users\你的用户名\\.claude\settings.json

```bash
{ "permissions": { "allow": ["mcp__pencil"] } }
```

## 三、在 Pencil 中使用 AI 作图

### 手动作图

pencil和常用的原型工具类似，比如Axture和Figma，

都可以手动在画布上去拖动生成组件。

如果不想手动反复调整 UI，可以让 Claude Code 先生成结构，再用设计工具细化视觉。

**所以我们需要借助AI的力量。**

**用语言描述来生成UI原型图。**

### 桌面端AI配置（可不做）

**注意，这一步即使你不做，完全不影响我们后续的使用。**

**只是多了一种更直观的使用方式\~\~**

在pencil桌面端的右上角，有一个设置按钮。

2选1配置好后，就可以在左下角点开AI对话框。

**可以看到pencil天然支持claude模型**

当你配置完成后，就可以通过文字的能力来让AI生成完整设计图。

**这里依然不是我们的重点，**

**我们的目的是借助Claude Code来完全打通原型图和代码。**

## 四、MCP 打通的核心能力

上述我们提到了，

**pencil安装过程中，自动配置好了AI编码工具的MCP**

这是最重要的部分。

**我们需要了解MCP有哪些接口，才能理解他后续能做哪些事情。**

Pencil MCP 提供了 14 个 API，我把它们分成 5 类：

**查询类** → 了解当前状态

- get_editor_state **获取选中元素**
- get_screenshot *()* **截图验证效果**

**读取类** → 理解设计稿

- batch *()* \_get 批量搜索节点
- get_variables 获取设计变量

**修改类** → 改设计稿

- batch_design **核心！增删改节点**
- set_variables 设置设计变量

**批量操作类** → 全局修改

- replace_all_matching_properties 批量替换属性（比如全局换肤）

**辅助类** → 设计灵感

- get_guidelines 获取设计规范
- get_style_guide 获取风格指南

### 核心 API：batch_design

支持 6 种操作：

```bash
I(parent, {...})  → 插入节点
C(nodeId, ...)    → 复制节点
U(nodeId, {...})  → 更新属性
R(nodeId, {...})  → 替换节点
M(nodeId, ...)    → 移动节点
D(nodeId)         → 删除节点
```

### 核心 API：get_editor_state

获取选中元素,这意味着，你可以点选某个组件，然后用语言组织去修改。

### 核心 API：get_screenshot

截图验证效果,这意味着，你可以让Agent自己去判断生成的设计图是否符合要求。

比如可以组建一个Agent团队，其中职责为设计师的SubAgent自己去做这件事情。

**这些组合起来，就能完全控制设计稿。**

## 五、两个关键Skills

于是，我用 **find-skill，寻找到两个技能来串联流程** 。

```bash
用find-skill，寻找pencil相关技能。解决以下问题：
如何给出美观的设计图提示词，并且风格统一。
生成原型图后，如何优雅的转化为代码直接执行。
```

### pencil-design 技能

*作用：帮你生成设计提示词 + 调用 MCP 创建设计稿*

工作流程：

1. 你描述想要什么界面
2. 技能帮你理清需求（ **可结合 brainstorming 做头脑风暴** ）
3. 调用 MCP API 创建设计

这里会放大使用者的差距，如何描述需求是一门学问。

### ui-skills 技能

*作用：把设计稿导出成代码*

它会读取设计稿节点，按 Tailwind *()* + shadcn/ui 规范 **生成 React 代码** 。

生成的不是玩具代码，是可以直接跑的。

## 六、代码导出与运行

### 导出流程

1. 告诉 Claude 你要导出哪个界面
2. Claude 读取设计稿，分析结构
3. 自动生成项目代码

生成的代码结构：

```bash
src/
├── app/          # 页面
├── components/   # 组件
└── lib/          # 工具函数
```

### 运行

```bash
npm install && npm run dev
```

访问 localhost:3000 就能看到效果。

**像素级还原，不是吹的。**

而且 Claude 会自动加上页面跳转逻辑，不是静态页面。

## 七、修改组件的两种方式

### 方式一：在 Pencil 中直接改

1. 1.打开 Pencil 桌面端
2. 2.点选要修改的组件
3. 3.在右侧属性面板修改
4. 4.用 MCP 导出代码

适合：可视化调整、设计师习惯

### 方式二：在 Claude Code 中用自然语言改

直接告诉 Claude：

- "把所有卡牌背景色改成蓝色"
- "把界面上的英文都翻译成中文"

Claude 会自动找到目标节点并修改。

适合：批量修改、程序员习惯、快速迭代

两种方式改的是同一份 .pen 文件，可以混着用。

## 八、版本管理：可以用 Git

特别提一下：

**Pencil 的文件格式是 .pen，本质上是 JSON。**

这意味着：

- **可以放进 Git 仓库**
- 追踪每次设计变更
- 多人协作做版本控制
- **代码和设计稿放同一个仓库管理**

**传统的 Figma 文件是二进制格式，Git 很难追踪变更。**

**另外，Pencil是支持直接导入Figma文件的。**

Pencil 的 JSON 格式解决了这个问题。

设计稿也可以像代码一样做 Code Review 了。

## 九、完整工作流

把上面说的串起来：

**非常适合用来**

- 快速验证想法
- 一个人既做设计又做开发
- 需要频繁迭代的原型
- AI 辅助开发的工作流

可以把原型图的流程，作为spec开发的一环。

这样能够让AI自主去评审和迭代。

---

## 相关阅读

- 上一篇：[第 30 篇](./30-30-claude-code-接入-crazyrouter-连载-30-用claude-code-画系统功能模块图和系统架构图.md)
- 下一篇：[第 32 篇](./32-32-ai产品经理提效篇-claude-如何快速承接多角色与上下文-crazyrouter-连载-32.md)
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
