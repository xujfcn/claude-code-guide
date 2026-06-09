# 23｜Claude Code 接入 Crazyrouter 连载 23：完整项目实战

> 本文是 Crazyrouter Claude Code 系列第 23 篇。本文会围绕「Claude Code 接入 Crazyrouter 连载 23：完整项目实战」展开，重点覆盖 完整项目实战、拒绝 "Happy Path"：完善核心链路、注入灵魂：模拟真实数据 (Mock Data)。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code) 完成基础配置。

## 完整项目实战

## 拒绝 "Happy Path"：完善核心链路

很多初学者做原型，往往只做“Happy Path”（最理想的路径）：用户点击 -> API 响应成功 -> 显示结果。 但在真实世界里，事情往往没那么顺利。为了让你的原型看起来像个真正的产品，你需要考虑以下几个“隐形”的环节。

### 1.1 增加“等待”与“反馈”

当用户点击“生成文案”时，AI 往往需要几秒钟才能响应。如果界面毫无反应，用户会以为程序坏了。 你需要让 AI IDE 帮你加上 Loading 状态：

### 可复制项目：提示词示例

```text
当我点击生成按钮时，请把按钮变成‘生成中...’并不可点击，同时在右侧区域显示一个加载动画。直到 API 返回结果后，再恢复正常。
```

### 1.2 处理“失败”与“异常”

API Key 可能会过期，网络可能会断开。 你需要让 AI IDE 帮你处理报错：

### 可复制项目：提示词示例

```text
如果 API 请求失败了，不要直接在控制台报错，请在页面顶部弹出一个红色的提示框（Toast），告诉用户‘生成失败，请稍后重试’，并允许用户重新点击生成。
```

### 1.3 对话历史持久化

存储方案选择：

| 方案 | 适用场景 | 特点 |
|-|-|-|
| LocalStorage | 纯前端项目，用户数据保存在浏览器 | 实现简单，刷新不丢失，无法跨设备同步 |
| JSON 文件 | 本地原型，数据以文件形式存储 | 结构清晰，便于调试，可手动编辑 |
| TXT 文件 | 最简方案，快速记录文本内容 | 格式自由，兼容性好 |

对话内容示例： 保存的对话历史通常包含以下内容：

```json
[
  {
    "role": "user",
    "content": "帮我生成一款蓝牙耳机的抖音带货文案",
    "timestamp": "2026-01-20 10:30:00"
  },
  {
    "role": "assistant",
    "content": "【蓝牙耳机种草文案】\n\n🎧 告别延迟，沉浸式听歌体验\n\n姐妹们！这款蓝牙耳机真的太绝了👇\n\n✅ 40dB主动降噪，瞬间进入音乐世界\n✅ 30小时超长续航，一周通勤不用充电\n✅ 通话清晰如面对面，地铁嘈杂也能聊\n✅ 半入耳设计，久戴不痛不闷耳\n\n💰 限时优惠，点击下方链接入手！",
    "timestamp": "2026-01-20 10:30:05"
  }
]
```

### 可复制项目：实现提示词

```text
请帮我实现对话历史的保存功能。支持将用户和 AI 的对话记录保存为 JSON 文件（或使用 LocalStorage）。每次进入页面时自动加载历史对话，支持查看和删除单条对话记录。
```

## 注入灵魂：模拟真实数据 (Mock Data)

一个空荡荡的页面是无法打动人的。 为了让演示效果最佳，我们需要“伪造”一些逼真的数据，让你的原型看起来像一个已经运营了半年的真实产品。

### 2.1 让 AI 帮你设计数据结构

只需要告诉 AI 你的业务场景：

### 可复制项目：提示词示例

```text
我正在做一个电商素材工作台的原型。 请帮我设计一个 JSON 数据结构，用来描述一个‘商品任务’。 这个任务应该包含：商品的基本信息（名字、类目）、输入的素材（图片链接）、以及 AI 生成的结果（标题、文案、海报图）。 请直接给我一个 JSON 示例。
```

AI 会根据你的描述，自动帮你构思出类似 `productName` , `generatedContent` 这样的字段。

### 2.2 让 AI 批量生产“逼真”数据

有了数据结构后，下一步就是让 AI 帮你“填空”，生成一批看起来真实的数据。

提示词技巧： 你不能只告诉 AI “帮我生成数据”，你需要像给实习生布置任务一样，告诉它业务背景和内容要求：

- 业务背景：告诉 AI 我们是做“抖音电商”的，所以商品标题要吸睛（比如“显瘦神器”、“学生党必入”），文案要口语化。
- 图片要求：为了让原型好看，图片不能是黑白的占位符，最好是随机的彩色风景或实物图。

### 可复制项目：提示词示例

```text
请基于刚才设计的结构，帮我生成 10 条逼真的模拟数据。 （备注：不一定要 JSON 格式。如果你正在写前端，可以让它直接生成 JavaScript 数组；如果你用 Python，可以让它生成 List。）
```

> 业务场景要求：

1. 假设这是一家综合百货店，商品涵盖‘女装’、‘数码’、‘美妆’三个类目。
2. 生成的标题和文案要非常‘抖音风’：比如标题要包含 Emoji (🔥, ✨)，文案要用‘绝绝子’、‘亲测好用’这种语气。
3. 图片字段：请统一使用 ` 这个格式，确保每张图都不一样。”

生成的 Mock Data 示例：

```bash
export const mockProductTasks = [
  {
    id: 'task_001',
    name: '夏季法式复古碎花裙',
    status: 'completed',
    input: {
      category: '女装',
      features: ['收腰', '显瘦', '气质'],
      originalImage: '
    },
    output: {
      generatedTitle: '✨谁穿谁好看！这条法式碎花裙真的绝绝子🔥',
      generatedCopy:
        '姐妹们！这条裙子真的太显瘦了！收腰设计绝了，穿上立马有腰身。面料很透气，夏天穿完全不闷。约会逛街首选！👗',
      generatedPosterImage: '
    },
    createdAt: '2026-01-20T10:00:00Z'
  },
  {
    id: 'task_002',
    name: '超强降噪蓝牙耳机 Pro',
    status: 'completed',
    input: {
      category: '数码',
      features: ['降噪', '超长续航', '低延迟'],
      originalImage: '
    },
    output: {
      generatedTitle: '🎧 终于被我找到了！这款耳机降噪太强了吧！🔇',
      generatedCopy:
        '戴上它，世界瞬间安静了。音质绝佳，听歌就像在现场。续航也很给力，充一次电用一周！学生党必入！',
      generatedPosterImage: '
    },
    createdAt: '2026-01-21T14:30:00Z'
  }
  // ... 更多数据
]
```

### 2.3 (进阶) 使用 LocalStorage 实现“假增删改”

如果你希望刚才生成的“模拟数据”不仅能看，还能删、能改，甚至新生成的任务刷新页面后还在，你可以结合 `LocalStorage` 。

### 可复制项目：提示词示例

```text
请帮我实现一个数据存储功能。
```

1. 优先从 `localStorage` 读取数据。
2. 如果 `localStorage` 为空，则使用刚才生成的 Mock 数据初始化，并将它们存入 `localStorage` 。
3. 同时帮我写 `addProductTask` 和 `deleteProductTask` 函数，每次操作都要同步更新 `localStorage` 。”

通过这一步，你的原型就拥有了“记忆”，用户体验几乎和真产品无异。

## 收集反馈与快速迭代

闭门造车是做不出好产品的。现在你的原型已经具备了“核心功能”+“完整链路”+“演示数据”，是时候拿给别人看了。

### 3.1 找谁测？怎么测？

- 找朋友/同事：不需要他们懂技术，只需要让他们试着用一下。
- 观察而非引导：不要说“点这里”，而是看他们会点哪里。如果他们找不到按钮，说明设计有问题。
- “Wizard of Oz” (绿野仙踪法)：如果你的 AI 还没接好，你可以人工在后台（或数据库）手动修改数据来模拟 AI 的返回，先验证用户是否需要这个功能。

### 3.2 面对 Bug 和 吐槽

- 样式错乱：不同屏幕尺寸下可能会乱。

  - Action: 截图发给 AI IDE -> “在这个屏幕宽度下乱了，帮我修一下。”
- 操作别扭：“这个流程太繁琐了”。

  - Action: 把建议告诉 AI IDE -> “用户觉得先上传再生成太慢，能不能改成一键生成？”
- 需求新增：“如果有这个功能就好了”。

  - Action: 评估是否核心，如果是，让 AI 快速实现一个简化版。

记住：在这个阶段，AI 是你最好的修改助手。你只需要负责发现问题，代码修改交给它。

---

## 相关阅读

- 上一篇：[第 22 篇](./22-22-claude-code-接入-crazyrouter-连载-22-为原型注入-ai-能力.md)
- 下一篇：[第 24 篇](./24-24-claude-code-接入-crazyrouter-连载-24-aicoding实战-从prd到代码生成.md)
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
