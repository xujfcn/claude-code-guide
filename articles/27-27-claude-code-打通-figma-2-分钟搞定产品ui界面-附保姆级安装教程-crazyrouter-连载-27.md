# 27｜Claude Code 打通 Figma，2 分钟搞定产品UI界面（附保姆级安装教程）：Crazyrouter 连载 27

> 本文是 Crazyrouter Claude Code 系列第 27 篇。本文会围绕「Claude Code 打通 Figma，2 分钟搞定产品UI界面（附保姆级安装教程）：Crazyrouter 连载 27」展开，重点覆盖 Claude Code 打通 Figma，2 分钟搞定产品UI界面（附保姆级安装教程）、一、安装claude code、二、接入API。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 完成基础配置。

## Claude Code 打通 Figma，2 分钟搞定产品UI界面（附保姆级安装教程）

> 🔗

## 一、安装claude code

### **第 1 步：下载 Cursor**

安装claude code之前，要先安装Cursor、VScode等都可以。

直接让Cursor帮忙安装claude code

```bash
提示词：请直接在终端里帮我执行 npm install -g @anthropic-ai/claude-code 来安装 Claude Code CLI
```

然后如果遇到停顿，你就点击【RUN】就可以了。到下图的这一步，你就回复【用本地安装方案就行】

直到右图的显示，就说明安装成功了。

### **第 2 步：打开 Cursor 底部的“ 终端 (Terminal) ”**

如果你现在界面底部没有那个用来敲命令的黑框框，你可以按下键盘快捷键 **Cmd + J** （Mac 系统），终端就会弹出来。

### **第 3 步：输入启动命令并回车**

在弹出的终端里直接输入下面这三个单词，然后按下回车键：

```bash
npm run claude
```

如果遇到报错，直接截图发给Cursor问，根据他的步骤来解决。解决完报错问题，显示以下界面说明claude code安装成功了。

## 二、接入API

Claude Code 我们可以使用两种方式，第一种是官方版，第二种是使用国内模型如 GLM4.6 驱动 ClaudeCode。

如果你是新用户，点击【财务】-【资源包管理】-【我的资源包】里面会有一些免费的额度可以使用。

如果你不是新用户，选择点击【Crazyrouter Claude Code 接入配置】

想试试水的话，选择第一个【GLM Coding Lite】就行了。

复制下图的API key。

## 三、下载cc switch

然后让AI直接帮你下载cc switch，我是让codex帮我下载的。

codex下载mac地址： 

下载windows地址： 

```bash
帮我下载cc switch：
```

下载完后，打开CC Switch，点击右上角的添加【+】按钮。

选择Crazyrouter模型，再往下滑输入API。

粘贴刚刚复制的API key，点击【添加】就可以了。

再点击设置按钮。

这里有个设置一定要开，点击下面的【应用到claude code插件】开关。

## 四、启动claude code

点击删除按钮，删掉后，重新【command+j】打开终端。

输入命令claude回车，就可以愉快的聊天了！

## 五、连接figma mcp

**第 1 步：** 退回到最外层的电脑终端如果你现在还在 > 符号后面，请输入 /exit 然后回车。确保你回到了带有 % 符号的普通 Mac 终端界面。

**第 2 步：** 执行官方的“全局安装”命令在带有 % 的终端里，复制粘贴这行 Figma 官方专门给 Claude Code 准备的安装代码：

```bash
claude mcp add --scope user --transport http figma 
```

(注意：这里加了--scope user，意思是给你电脑上所有的代码项目都装上这个插件，以后换个文件夹敲代码也不用重复装了。复制完按下回车执行。)

**第 3 步：** 重新叫出claude code代码执行完毕后，再次输入启动口令，按回车：claude

**第 4 步：** 关键一步——去 Figma 官网领“通行证”在小机器人的 > 后面，输入 /mcp 并回车。看到>在figma中，继续回车。

请选择 **Authenticate(授权)** 并再次回车。电脑会自动弹出一个浏览器网页。在网页里登录你的 Figma 账号，并点击 **Allow Access (允许访问)** 。网页授权成功后，切回终端，你就会看到一句闪亮的 Authentication successful. Connected to figma.！

## 六、安装figma plugin

复制下面这条命令，粘贴到claude code，然后回车

```bash
/plugin install figma@claude-plugins-official
```

显示下面这个页面后，继续回车。

继续输入【/plugin】回车，会看到以下界面，键盘右键选择【installed】，再按回车。

这样插件就安装成功了！然后连按几下键盘左上角的 **Esc键** ，直到退回那个只有 > 的普通聊天状态。

## 七、报错解决

这里有一个报错卡了我很久，就是下图这个400。

原本Claude code v2.1.69的版本降到68就可以了。

继续让codex帮你的版本改成低一个版本提示词：帮我的claude code版本改成v2.1.68

## 八、Claude code to figma

我们到figma【复制链接】建一个空的文件。

回到Cursor中，输入提示词：需要在下面的提示词中粘贴你的figma链接。

```bash
直接在这个空的 Figma 文件里，为我设计一个现代风格的设计师个人网站首页，包含导航栏、个人简介、作品集展示区和页脚。设计完成后，再帮我生成对应的 HTML/CSS/JS 代码：
```

接着会一直做一些选项，一直选择yes回车就行。

最后会自动跳转到浏览器，然后可以直接点击【发送到figma】

就会自动发送到figma文件中。

看看它生成的效果，不愧是claude code，没话说，效果非常好！

## 九、修改完设计如何传回code里？

选择设计稿，右键复制【copy link to selection】。

回到claude code 中输入：

```bash
update changes:【这里是刚刚复制的链接】
```

claude就重新构建了对应的部分，就这么简单。

---

## 相关阅读

- 上一篇：[第 26 篇](./26-26-claude-cursor-figmamastergo四步生成高端的产品原型图-附提示词和步骤-crazyrouter-连载-26.md)
- 下一篇：[第 28 篇](./28-28-claude-code-mermaid-一键生成架构图-时序图-流程图-crazyrouter-连载-28.md)
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
