# 22｜Claude Code 接入 Crazyrouter 连载 22：为原型注入 AI 能力

> 本文是 Crazyrouter Claude Code 系列第 22 篇。本文会围绕「Claude Code 接入 Crazyrouter 连载 22：为原型注入 AI 能力」展开，重点覆盖 为原型注入 AI 能力、API 基础概念、接入文本生成 API：DeepSeek。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code) 完成基础配置。

## 为原型注入 AI 能力

## API 基础概念

前面提到，我们的目标是「把 AI 能力接进来」，让原型不再是静态演示，而是能调用真实 AI 服务的工具。要实现这一点，关键就在于理解并使用 API（应用程序编程接口）。

API 是计算机领域的一个重要抽象概念，我们可以简单理解为：你按对方要求的格式"发一个问题"，对方就按同样的格式"回一个结果"。

- 你发出去的内容：通常包括"密钥（API Key）"和"你要生成什么"
- 对方回给你的内容：成功就给结果；失败会告诉你原因（比如"密钥不对""余额不足""参数写错"）

具体来说，你需要掌握以下核心要素：

1. API Key：你的"通行证"，也是"钱包钥匙"。别人拿到它，就可以替你调用接口并产生费用。
2. Endpoint（接口路径）：API 请求的具体路径，告诉服务器你要访问哪个功能。完整的请求地址通常由"基础 URL + Endpoint路径"构成。例如：

   - 文本生成：基础URL ( ` ) + Endpoint ( `/v1/chat/completions` ) = 完整URL `
   - 图像生成：基础URL ( ` ) + Endpoint ( `/v1/images/generations` ) = 完整URL `
3. 调用/请求：向 AI 服务发送任务并获取结果的过程
4. 请求内容：你发给AI的具体内容，比如你想让AI写的文章主题、生成的图片描述等。
5. 响应结果：AI处理完后返回给你的内容，比如生成的文章、图片等。
6. 错误处理：当出现问题时（如API Key错误、请求太频繁等），知道如何排查解决。

## 接入文本生成 API：DeepSeek

虽然 API 涉及这些技术概念，但在原型开发阶段，实际操作可以非常简单高效。核心思路就是：

> 找到官方示例、拿到 API Key、让 AI IDE 帮你接到按钮上。

掌握了这些概念后，你会发现无论是接入文字模型还是图像模型，其本质流程都是一样的：当用户点击按钮时，前端整理输入并发起请求；接口返回结果后，再把结果展示到页面上。接下来，我们就通过实际操作来验证这一点。

在 `1.2 动手做出原型` 里，你已经做出了一个可交互的原型。接下来我们要做的，是把原型里“看起来像 AI 的功能”变成真正可用的能力：当用户点击按钮时，原型会向Crazyrouter 模型服务发出请求，并把返回的文字展示出来。

跟着这 3 步走，就能实现大模型生成 API 的快速集成：

2. 在 Crazyrouter 文档中找到文本生成示例（通常有现成代码可直接复制）
3. 打开 AI IDE，把 API Key + 官方示例粘贴进去，告诉 AI 要实现什么功能：
4. 帮我接入这个大模型的 API ，支持这个应用的文案生成任务

使用提示词参考如下：

```json
参考这个调用方法，帮我支持文案生成功能，可以基于商品信息点击后生成对应抖音电商文案，多种风格。

以下参考资料：
api key：YOUR_CRAZYROUTER_API_KEY
api 请求参考：
curl https://cn.crazyrouter.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_CRAZYROUTER_API_KEY" \
  -d '{
        "model": "deepseek-v4-pro",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hello!"}
        ],
        "stream": false
      }'
```

经过一段时间的 AI 代码生成，我们很容易得到对应的文案生成按钮进行测试，如果你找不到入口，可以让 AI IDE 告诉你从什么页面可以点到该页面，如果实在找不到，可以让 AI IDE 直接基于你的想法重构改进，得到最后的文案生成结果。

当然，此处你可能想问，我怎么知道真正调用了大模型而不只是内置了固定的回复？你可以输入自定义的文案，让大模型根据你及时指定的自定义分析，生成对应的文案。

如果发现每次不一样并且合乎逻辑，你可以放心认为此时已经正常调用 API 生成。你也可以在 Crazyrouter 控制台日志查看是否成功调用（虽然可能需要等几分钟才能看到）。

## 接入图像转文字 API：Qwen3 VL

在前面的部分我们说明了如何接入文字生成 API， 但对于前面的应用场景我们会发现一个问题，我们上传的是一张图片，如果只用大语言模型，它没办法很好的理解图片中的内容，生成的结果很可能会有差别。

我们希望有一个模型能够帮助我们把一个图片变成文字描述，这就需要用到视觉语言模型（VLM）。在案例中，我们将会使用视觉语言模型生成商品的卖点描述，提升用户体验。

我们可以选择任意一个进行测试，这里以 `qwen3-vl-8b-instruct` 为例。

你可以直接使用下面的代码作为参考代码，和生成的 API Key 一起，发送给 AI IDE ，进行功能集成。

在这个场景中，我们直接尝试让 AI IDE 帮我们实现将上传的图片，自动生成电商卖点文本、关键词的功能，如下所示：

```bash
基于下面的图生文接口 API ，帮我们实现将上传的图片，自动生成电商卖点文本、关键词的功能

<此处省略代码，你需要自行粘贴密钥和参考代码>
```

## 接入图像生成 API：Seedream 即梦

在前面的部分我们主要和文本相关的任务打交道，接下来我们将尝试接入图片生成的功能，支持从文字描述生成图片，或者对图片进行修改。

由于我们之后使用的是参考图生成模式，我们先去的是多张图生成单张图的功能。参考代码复制如下：

```C++
curl -X POST https://cn.crazyrouter.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_CRAZYROUTER_API_KEY" \
  -d '{
    "model": "doubao-seedream-4-5",
    "prompt": "将图1的服装换为图2的服装",
    "image": [" "],
    "sequential_image_generation": "disabled",
    "response_format": "url",
    "size": "2K",
    "stream": false,
    "watermark": true
}'
```

有了图像参考代码后，我们让 AI IDE 支持电商中常用的图像任务功能：

```bash
请你基于下面 API，帮我实现这个工程中，电商业务的常见功能（例如海报生成、抖音电商首图生成等等）

<此处粘贴 API KEY以及图像编辑代码>
```

实现效果如下:

值得注意的是，由于生成图片可能会经常遇到一些奇怪的问题，建议你需要让 AI IDE 能够显示完整的报错信息，方便复制粘贴进行修改（否则可能会反复显示生成失败但是不知道为什么），例如你可以说：

```bash
不要只显示图片生成失败，每次都显示完整的失败原因，比如图片不匹配、请求错误、超时等等！
```

有时候修改后更新并不会应用到网页中，如果你发现修改后网页一直还在报错（反复多次），也可以试试直接对 AI IDE 说：请你重启这个项目。

在电商的业务中，我们可能会想让用户上传的衣服能够自动穿在人物身上，又或者是自动生成商品吸引人的售卖图、海报。这里我们尝试的提示词是让它生成一个电商海报：

你可以根据自己想象的业务场景，使用文生图或者图生图 API 实现不同的功能。

## 更多不同图像服务选型

下面给出其他选择。建议你先跑通 Qwen 生图的结果，再根据效果与成本使用下列服务做替换（根据实际使用感受选择）。

### Recraft 集成

如果你的原型更偏“设计生产”（例如生成品牌风格插画、营销海报、矢量风格素材），Recraft 往往会更顺手。接入方式与上一节完全一致：拿到 Key + 找到官方示例 + 让 AI IDE 把示例落到你的按钮/页面里。

### Qwen Image / Qwen Image Edit 集成

如果你希望使用更简单的方式接入图像生成服务，可以考虑 Qwen Image（通义万相）。思路同样不变：把它当成一个"图片生成 API"，接到你的原型按钮上即可。

如果你选择"Image"，你将只看到当前支持的所有文生图模型。在这种情况下，我们将使用 qwen-image-plus。

一切设置好后，我们需要参考相应的图像生成 API 文档。你可以在官方文档页面找到任何标记为"API Reference"的部分。点击它，然后导航到 图像生成的 API 部分并找到相关的请求示例。

你可以把下列请求示例和 API KEY 一起发给 AI IDE， 即可实现图像生成的功能。

```SQL
curl --request POST \
  --url https://cn.crazyrouter.com/v1/images/generations \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "model": "qwen-image-plus",
  "prompt": "an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea"
}
'
```

这里的模型可以使用 qwen-image-plus 或者 qwen-image-plus。

## 附录：如何找到“当前更强”的 AI 模型

文字模型（也常被叫作“大语言模型”）的发展速度非常快，我们总是需要确保我们用的是表现更好的模型之一。通过以下两个网站，你可以很方便地看到“现在大家常用、评价也更好的模型”。

一般来说，这类网站可以理解为 “模型竞技场”：它会把两个模型的输出放在一起，你投票选你更喜欢的那个。票数高的模型，通常意味着更多人觉得它“更好用”。

此外，你偶尔可能会在这些大模型竞技场中看到神秘的匿名模型（“Unknown Model”）。这通常意味着：有人把“内部测试模型”悄悄放进来做盲测，你可能有机会提前体验到更强的能力。

网站： 

一个简单的用法是：

1. 直接看排行榜（Leaderboard）
2. 先选一个你要做的方向（例如通用对话 / 编程 / 视觉）
3. 选 Top 3 里你能用的那个（能访问、价格能接受、延迟能接受）

网站： 

常用的用法是：

1. 找到你关心的模型类别（文本 / 生图等）
2. 看质量指标（Quality）+ 价格（Price）+ 延迟/吞吐（Latency/Throughput）
3. 选一个“综合性价比”最符合你产品的

✅ 建议

不要凭感觉争论“哪个更强”。更可靠的做法是：用同一组输入同时测试 2\~3 个模型，再结合榜单与价格做决定。

## 总结

在接入各类 AI 服务时，不必把 API 想象得太复杂。把握住以下几个核心概念，基本就能应对大多数场景：

API 的本质是通信桥梁。它做的事情很简单：把你的请求发送出去，再把模型的响应带回来。你不需要关心背后发生了什么，只需要正确地组织请求格式。

SDK 是对 API 的封装。如果说 API 是 raw 接口，SDK 就是一套现成的工具箱——它把请求签名、错误处理、参数校验这些繁琐的细节都替你做好了。日常开发中，优先选择 SDK 而不是直接调 API，能省去不少麻烦。

阅读文档时，盯住三样东西就够了：服务地址（endpoint）、身份凭证（API key）以及调用参数怎么填。把这三点弄清楚，调通只是时间问题。

剩下的工作，IDE 和现代化的开发工具会帮你完成。专注于你的业务逻辑，底层调用的事交给这些成熟的 SDK 和工具链。

---

## 相关阅读

- 上一篇：[第 21 篇](./21-21-claude-code-接入-crazyrouter-连载-21-动手做出原型.md)
- 下一篇：[第 23 篇](./23-23-claude-code-接入-crazyrouter-连载-23-完整项目实战.md)
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
