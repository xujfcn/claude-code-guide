# 12｜Claude Code 接入 Crazyrouter 连载 12：第九章：常用快捷键

> 本文是 Crazyrouter Claude Code 系列第 12 篇。本文会围绕「Claude Code 接入 Crazyrouter 连载 12：第九章：常用快捷键」展开，重点覆盖 第九章：常用快捷键、9.1 快捷键与快捷操作、常用快捷键。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 完成基础配置。

## 第九章：常用快捷键

## 9.1 快捷键与快捷操作

掌握快捷键和快捷操作可以大大提高使用 Claude Code 的效率，让你更快地完成各种任务。

## 常用快捷键

### 基础快捷键

发送消息

- Windows/Linux： `Ctrl + Enter`
- macOS： `Cmd + Enter`

新建对话

- Windows/Linux： `Ctrl + Shift + N`
- macOS： `Cmd + Shift + N`

打开设置

- Windows/Linux： `Ctrl + ,`
- macOS： `Cmd + ,`

打开帮助

- Windows/Linux： `Ctrl + /`
- macOS： `Cmd + /`

### 编辑快捷键

复制消息

- Windows/Linux： `Ctrl + C`
- macOS： `Cmd + C`

粘贴内容

- Windows/Linux： `Ctrl + V`
- macOS： `Cmd + V`

剪切内容

- Windows/Linux： `Ctrl + X`
- macOS： `Cmd + X`

全选

- Windows/Linux： `Ctrl + A`
- macOS： `Cmd + A`

撤销

- Windows/Linux： `Ctrl + Z`
- macOS： `Cmd + Z`

重做

- Windows/Linux： `Ctrl + Y` 或 `Ctrl + Shift + Z`
- macOS： `Cmd + Y` 或 `Cmd + Shift + Z`

### 导航快捷键 #

向上滚动

- `Page Up` 或 `Shift + Space`

向下滚动

- `Page Down` 或 `Space`

滚动到顶部

- `Home`

滚动到底部

- `End`

切换到上一个标签页

- Windows/Linux： `Ctrl + Tab`
- macOS： `Cmd + Tab`

切换到下一个标签页

- Windows/Linux： `Ctrl + Shift + Tab`
- macOS： `Cmd + Shift + Tab`

### 搜索快捷键 #

搜索对话历史

- Windows/Linux： `Ctrl + F`
- macOS： `Cmd + F`

搜索文件

- Windows/Linux： `Ctrl + P`
- macOS： `Cmd + P`

全局搜索

- Windows/Linux： `Ctrl + Shift + F`
- macOS： `Cmd + Shift + F`

## 快速操作按钮 #

### 聊天窗口操作 #

发送按钮

- 位置：输入框右侧
- 功能：发送消息
- 快捷键： `Ctrl/Cmd + Enter`

上传文件按钮

- 位置：输入框上方
- 功能：上传本地文件
- 使用：点击按钮，选择文件

插入代码按钮

- 位置：输入框上方
- 功能：插入代码块
- 使用：点击按钮，输入代码

格式化文本按钮

- 位置：输入框上方
- 功能：调整文本格式
- 使用：点击按钮，选择格式

### 消息操作 #

复制按钮

- 位置：每条消息右侧
- 功能：复制消息内容
- 使用：点击按钮，内容复制到剪贴板

重新生成按钮

- 位置：每条消息右侧
- 功能：让 AI 重新生成这条回复
- 使用：点击按钮，AI 重新生成

点赞按钮

- 位置：每条消息右侧
- 功能：给回复点赞
- 使用：点击按钮，反馈质量

点踩按钮

- 位置：每条消息右侧
- 功能：给回复点踩
- 使用：点击按钮，反馈质量

### 工具栏操作 #

新建对话按钮

- 位置：工具栏
- 功能：开始新的对话
- 快捷键： `Ctrl/Cmd + Shift + N`

历史记录按钮

- 位置：工具栏
- 功能：查看和管理历史对话
- 使用：点击按钮，打开历史记录面板

设置按钮

- 位置：工具栏
- 功能：打开设置界面
- 快捷键： `Ctrl/Cmd + ,`

帮助按钮

- 位置：工具栏
- 功能：查看使用帮助
- 快捷键： `Ctrl/Cmd + /`

## 批量处理技巧 #

### 批量上传文件 #

方法 1：多选上传

1. 点击上传文件按钮
2. 在文件选择对话框中，按住 `Ctrl` （Windows/Linux）或 `Cmd` （macOS）
3. 点击多个文件
4. 点击"打开"

方法 2：拖拽上传

1. 在文件管理器中选择多个文件
2. 拖拽到 Claude Code 的文件浏览区
3. 松开鼠标

### 批量处理消息 #

批量复制

1. 在对话历史中选择多条消息
2. 按 `Ctrl/Cmd + C` 复制
3. 粘贴到其他地方

批量删除

1. 在历史记录中选择多条对话
2. 点击删除按钮
3. 确认删除

### 批量执行命令 #

批量发送消息

1. 准备多个提示词
2. 依次发送给 Claude Code
3. 收集所有回复

批量生成内容

1. 使用模板生成多个版本
2. 选择最好的版本
3. 保存结果

## 效率提升技巧 #

### 快速切换模型 #

方法 1：通过工具栏

1. 点击工具栏的模型选择下拉菜单
2. 选择想要的模型
3. 开始使用

方法 2：通过命令

1. 在输入框中输入： `/model [模型名]`
2. 按 Enter 发送
3. 系统切换到指定模型

示例：

```bash
/model claude
/model wenxin
/model qwen
```

### 快速访问历史 #

方法 1：通过历史记录面板

1. 点击工具栏的"历史记录"按钮
2. 浏览历史对话
3. 点击想要查看的对话

方法 2：通过搜索

1. 按 `Ctrl/Cmd + F` 打开搜索
2. 输入关键词
3. 查看搜索结果

### 快速切换视图 #

切换聊天窗口

- 点击聊天窗口标签
- 或使用快捷键 `Ctrl/Cmd + Tab`

切换文件浏览区

- 点击文件浏览区标签
- 或使用快捷键 `Ctrl/Cmd + Shift + Tab`

切换全屏模式

- 按 `F11` 进入/退出全屏
- 或点击工具栏的全屏按钮

## 案例示例 #

### 案例：快速处理多个文件 #

场景：需要快速处理 10 个 Excel 文件，提取关键信息。

步骤：

1. 批量上传文件

   - 在文件管理器中选择 10 个 Excel 文件
   - 拖拽到 Claude Code 的文件浏览区
2. 批量处理

```bash
请帮我处理这 10 个文件：
1. 提取每个文件的总销售额
2. 计算每个文件的平均销售额
3. 找出每个文件中销售额最高的产品
4. 生成汇总表格
```

1. 保存结果

   - 复制生成的汇总表格
   - 粘贴到 Excel 中保存

时间节省：

- 原耗时：2-3 小时
- 现耗时：10-15 分钟
- 节省时间：90%

### 案例：快速生成多个文案 #

场景：需要为 5 个产品生成文案。

步骤：

1. 准备模板

```bash
请帮我写一个产品文案，产品是[产品名称]，主要特点包括[特点1]、[特点2]、[特点3]，目标用户是[目标用户]，字数在 200 字左右。
```

1. 批量生成

   - 产品 1：使用模板，填写产品信息
   - 产品 2：使用模板，填写产品信息
   - 产品 3：使用模板，填写产品信息
   - 产品 4：使用模板，填写产品信息
   - 产品 5：使用模板，填写产品信息
2. 选择最佳版本

   - 查看所有生成的文案
   - 选择最好的版本
   - 保存结果

时间节省：

- 原耗时：1-2 小时
- 现耗时：10-15 分钟
- 节省时间：85%

## 小技巧 #

1. 记住常用快捷键：记住常用的快捷键，可以大大提高效率
2. 自定义快捷键：在设置中可以自定义快捷键
3. 使用快捷操作：多使用快捷操作按钮，减少鼠标点击
4. 批量处理：尽量批量处理文件和任务
5. 快速切换：熟练使用快速切换功能
6. 定期清理：定期清理历史记录和临时文件

现在，试着使用这些快捷键和快捷操作，提高你的工作效率吧！

## 9.2 工作习惯培养

养成良好的工作习惯，可以让你更高效地使用 Claude Code，让 AI 成为你的得力助手。

## 合理使用 AI 助手 #

### 明确 AI 的定位 #

AI 是助手，不是替代

- AI 可以帮助你完成很多任务，但不能完全替代你的思考
- AI 的建议需要你进行判断和决策
- AI 的输出需要你进行审核和调整

AI 是工具，不是万能

- AI 有自己的局限性，不能解决所有问题
- AI 的知识有截止时间，可能不知道最新的信息
- AI 的理解能力有限，需要你提供清晰的需求

### 何时使用 AI #

适合使用 AI 的场景

1. 重复性任务：如撰写报告、整理数据、生成文案
2. 需要创意的任务：如头脑风暴、创意点子、故事生成
3. 需要分析的任务：如数据分析、趋势分析、洞察发现
4. 需要优化的任务：如文本优化、格式调整、内容改写

不适合使用 AI 的场景

1. 需要高度保密的任务：如处理敏感数据、机密信息
2. 需要专业判断的任务：如法律咨询、医疗诊断
3. 需要情感交流的任务：如安抚客户、处理纠纷
4. 需要实时信息的任务：如股票行情、新闻资讯

### 如何与 AI 协作 #

1. 明确需求

- 清晰表达你的需求
- 提供足够的背景信息
- 说明期望的输出格式

1. 迭代优化

- 不要期望一次就得到完美结果
- 根据反馈不断优化
- 耐心调整提示词

1. 人工审核

- 重要任务必须人工审核
- 检查结果的准确性
- 调整不符合要求的内容

1. 持续学习

- 记录有效的提示词
- 总结使用经验
- 不断优化工作流程

## 平衡人工与 AI #

### 人工的优势 #

1. 创造力

- 人类有独特的创造力
- 可以产生原创性的想法
- 可以进行艺术创作

1. 情感理解

- 人类可以理解情感
- 可以进行情感交流
- 可以处理复杂的人际关系

1. 专业判断

- 人类有专业知识和经验
- 可以进行复杂的判断
- 可以处理模糊的情况

1. 责任担当

- 人类可以承担责任
- 可以做出道德判断
- 可以处理伦理问题

### AI 的优势 #

1. 处理速度

- AI 处理速度快
- 可以批量处理任务
- 可以 24 小时工作

1. 数据处理

- AI 可以处理大量数据
- 可以快速分析数据
- 可以发现数据中的规律

1. 知识储备

- AI 有丰富的知识储备
- 可以快速检索信息
- 可以整合多领域知识

1. 一致性

- AI 的输出一致性好
- 不会疲劳
- 不会受情绪影响

### 如何平衡 #

1. 分配任务

- 将重复性、标准化的任务交给 AI
- 将创造性、需要判断的任务保留给人工
- 根据任务特点合理分配

1. 协作流程

- 人工提出需求
- AI 生成初稿
- 人工审核和调整
- AI 根据反馈优化

1. 质量控制

- 人工设定质量标准
- AI 按照标准生成内容
- 人工审核质量
- AI 根据反馈改进

## 持续学习与探索 #

### 学习新功能 #

关注更新

- 定期查看 Claude Code 的更新日志
- 了解新功能和改进
- 尝试使用新功能

学习技巧

- 阅读官方文档
- 观看教程视频
- 参加培训课程

实践应用

- 在实际工作中应用新功能
- 总结使用经验
- 分享给同事

### 探索新用法 #

尝试新场景

- 尝试用 AI 处理新的任务
- 探索 AI 在不同领域的应用
- 发现 AI 的更多可能性

优化工作流程

- 不断优化使用 AI 的流程
- 提高工作效率
- 节省更多时间

创新应用

- 思考 AI 的创新应用
- 结合自己的工作特点
- 创造独特的使用方法

### 建立知识库 #

记录提示词

- 记录有效的提示词
- 分类整理提示词
- 建立提示词库

总结经验

- 总结使用 AI 的经验
- 记录成功案例
- 分析失败原因

分享交流

- 与同事分享经验
- 参与社区讨论
- 互相学习进步

## 案例示例 #

### 案例：建立高效的工作流程 #

场景：营销人员需要定期生成各种营销文案。

工作流程：

1. 建立提示词库

- 产品描述提示词
- 广告文案提示词
- 社交媒体内容提示词
- 邮件写作提示词

1. 创建模板

- 产品描述模板
- 广告文案模板
- 社交媒体内容模板
- 邮件写作模板

1. 批量生成

- 使用模板批量生成文案
- 选择最好的版本
- 保存结果

1. 人工审核

- 审核生成的文案
- 调整不符合要求的内容
- 确保质量

1. 持续优化

- 根据反馈优化提示词
- 改进模板
- 提高效率

效果：

- 原耗时：每周 8-10 小时
- 现耗时：每周 2-3 小时
- 节省时间：70-75%

### 案例：平衡人工与 AI #

场景：客服人员需要回复客户邮件。

工作流程：

1. AI 生成初稿

- 提供客户邮件内容
- AI 生成回复初稿
- AI 提供多个版本

1. 人工审核

- 审核初稿的准确性
- 检查语气是否合适
- 确认内容是否完整

1. 人工调整

- 调整不合适的内容
- 补充遗漏的信息
- 优化表达方式

1. 发送邮件

- 发送给客户
- 记录客户反馈
- 总结经验

效果：

- 原耗时：每封邮件 15-20 分钟
- 现耗时：每封邮件 5-8 分钟
- 节省时间：60-70%
- 客户满意度：保持不变或提高

## 小技巧 #

1. 从小任务开始：先从简单的任务开始使用 AI，积累经验
2. 逐步扩展：随着经验积累，逐步扩展 AI 的使用范围
3. 保持学习：持续学习新功能和新用法
4. 定期总结：定期总结使用经验，优化工作流程
5. 分享交流：与同事分享经验，互相学习
6. 保持平衡：合理使用 AI，不要过度依赖

现在，开始培养良好的工作习惯，让 AI 成为你的得力助手吧！

---

## 相关阅读

- 上一篇：[第 11 篇](./11-11-claude-code-接入-crazyrouter-连载-11-第八章-提示词优化技巧.md)
- 下一篇：[第 13 篇](./13-13-claude-code-接入-crazyrouter-连载-13-第十章-用编程的思维解决问题.md)
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
