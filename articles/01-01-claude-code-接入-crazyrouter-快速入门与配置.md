# 01｜Claude Code 接入 Crazyrouter 快速入门与配置

> 本文是 Crazyrouter Claude Code 系列第 01 篇。本文会围绕「Claude Code 接入 Crazyrouter 快速入门与配置」展开，重点覆盖 Claude Code快速入门与配置。
>
> 统一接入口径：Claude Code / Anthropic 原生客户端使用 `ANTHROPIC_BASE_URL=https://cn.crazyrouter.com`；OpenAI 兼容 SDK、HTTP 请求和前后端应用使用 `base_url=https://cn.crazyrouter.com/v1`。

## 本篇导读

- 适合人群：正在用 Claude Code、准备接入国产模型，或希望把团队调用统一到 Crazyrouter 的开发者。
- 你会学到：如何按 Crazyrouter 文档配置环境变量、组织工作流，并避免 Base URL 写错导致的 `/v1/v1/...` 问题。
- 推荐准备：先在 [Crazyrouter 控制台](https://crazyrouter.com/console?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 创建一个单独的 API Token，再参考 [Claude Code 接入文档](https://docs.crazyrouter.com/integrations/claude-code?utm_source=github&utm_medium=tutorial&utm_campaign=claude_code_guide) 完成基础配置。

## Claude Code快速入门与配置

### **安装 Claude Code**

**系统需要满足以下最低要求：**

**操作系统：** Linux(Ubuntu 18.04+, CentOS 7+) macOS 10.15+, Windows 10+

网络连接：稳定的互联网连接

存储空间：至少 500MB 可用磁盘空间

#### 安装 Node.js

在开始安装前，请先检查 Node.js 和 npm 版本：

```bash
node --version
npm --version
```

如果本机还没有 Node.js，建议安装 Node.js 18 LTS 或更高版本：

- 下载地址：[Node.js 官网](https://nodejs.org/zh-cn/download)
- 安装文档：[Node.js 官方文档](https://nodejs.org/zh-cn/learn/getting-started/how-to-install-nodejs)

#### 安装 Git

在开始安装前，请先检查 Git 版本：

```bash
git --version
```

如果本机还没有 Git，可以按系统选择安装方式：

- 下载地址：[Git 官网](https://git-scm.com/downloads)
- 安装文档：[Git 官方文档](https://git-scm.com/book/zh/v2/起步-安装-Git)

#### **Linux /macOS 安装**

```text
# 全局安装 Claude Code
sudo npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version
```

#### **Windows 安装**

```text
#以管理员身份打开 Powershell 或命令提示符

# 全局安装
npm install -g @anthropic-ai/claude-code

# 验证安装
claude --version
```

#### 配置 Crazyrouter API Key

Claude Code 接入 Crazyrouter 时，优先配置 `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_API_KEY`。一般不需要在文章里填写空的代理地址。

Windows PowerShell：

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://cn.crazyrouter.com", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "YOUR_CRAZYROUTER_API_KEY", "User")
```

macOS / Linux：

```bash
export ANTHROPIC_BASE_URL=https://cn.crazyrouter.com
export ANTHROPIC_API_KEY=YOUR_CRAZYROUTER_API_KEY
```

如果希望脚本自动检查 Git、Node.js 和 Claude Code，可以直接使用 [Crazyrouter Claude Code 一键配置脚本](https://github.com/xujfcn/crazyrouter-claude-code)。

#### **控制台启动claude code**

终端输入：claude，之后需要登录claude使用 Crazyrouter Token 完成认证

### 一、基础操作：命令与配置是起点

#### **吃透帮助命令，解锁所有可能**

想快速上手？从 `claude --help` 开始。这个命令会列出所有可用参数和命令，比如 `-p` 用于非交互式输出、 `-c` 继续最近的对话、 `--model` 指定模型等。记住常用参数能让操作效率翻倍，比如用 `claude -r` 恢复历史会话，或 `--output-format json` 导出结构化结果。

| 命令 | 解释 | 使用场景 |
|-|-|-|
| /clear | 清空上下文 | 如果需要重新开始，或者是感觉 AI 已经无法解决问题 |
| /compact | 压缩对话 | 重开对话，但是不希望丢掉之前的记忆 |
| /cost | 花费 | 可用于查看当前会话消耗，建议结合 Crazyrouter 控制台日志核对 |
| /logout /login | 登录登出 | 切换账号等操作 |
| /model | 切换模型 | 可按 Token 权限和模型白名单切换可用模型 |
| /status | 状态 | 查看当前 CC 的状态 |
| /doctor | 检测 | 检测 CC 的安装状态 |

#### **与 IDE 无缝衔接，编码不切换窗口**

#### 在 VS Code、Cursor等 IDE 中使用 Claude Code，只需两步：

- **安装插件** ：搜索 “Claude Code”，认准 Anthropic 官方版本，点击安装即可。

- **快速启动** ：用快捷键 `Cmd+Escape` （可自定义）唤醒，或点击 IDE 界面中的 Claude Code 图标，右侧会直接显示工作区，支持选中代码自动传入上下文、diff 对比代码修改，甚至用 `Alt+Cmd+K` 一键推送选中内容到提示框。

### 二、核心模式：按场景切换，效率拉满

#### **自动编辑模式：免确认批量操作**

适合无需逐次确认的文件创建、修改场景。按下 `Shift+Tab` 一次即可开启，此时 Claude 会自动执行编辑操作，无需手动确认。比如提示 “创建一个酷炫的 todolist 应用”，它会直接生成文件并修改，省去反复确认的时间。

#### **Plan 模式：前期规划神器**

面对项目搭建或复杂问题时，用 `Shift+Tab` 两次开启 Plan 模式。它会先梳理方案框架，比如要做 “像素风格的移动端 todolist”，会自动规划技术栈、页面结构、适配方案等，确认后再动手。若不满意可直接说 “重新规划”，直到符合预期。

#### **Yolo 模式：全权限放手干**

重构代码、启动新项目或修复复杂 bug 时，用 `claude --dangerously-skip-permissions` 进入 Yolo 模式。此时 Claude 拥有更高权限，可直接执行更多操作（需注意安全，建议在沙箱环境使用）。进入后仍能用 `Shift+Tab` 调整模式，灵活切换权限粒度。

```text
claude --dangerously-skip-permissions
```

### 三、CLAUDE.md：全局记忆的核心

和聊天机器人交流时，我们知道 “系统提示词” 很重要，会持续影响 AI 的行为。那么 CC 中， CLAUDE.md 也是类似的地位。一个典型的工作流是：

> 建初始 CLAUDE.md → 对话直到长度接近溢出，运行 /compact 续命 → 达到里程碑时要求 CC 根据进度更新CLAUDE.md → 循环直到结束

可以看到 CLAUDE.md 就是一个持续发挥作用的全局变量。而且 CC 往里写入时一般做了充分的缩略，所以可读性很好。

**CLAUDE.md 注意事项**

- 文件不要太长，毕竟 CC 会默认读入这个文件
- 会话时为了省事，说 claude.md 时 CC 也可以懂
- 文件里适合放提醒事项，比如 “要求 CC 每次宣布成功时都要带上证据文件链接”，以及 “代理服务端口是 9890” 。然后会话时，可以要求 CC “查询 claude.md 相关部分”。
- 官方的 "#" 进文档据 GPT 说有个 bug 不稳定。

### 四、会话管理：避免失控，高效推进

#### **随时暂停与回滚**

- 工作中按 `Esc` 可暂停当前操作，比如发现 Claude 安装依赖超时、思路跑偏时，及时中断能减少无效操作。
- 按 `Esc` 两次可回退到历史对话节点（注意无 redo 功能，回退前确认）。
- 代码不满意？直接说 “回滚到上次的代码”，Claude 会自动恢复之前版本。

#### **应对历史溢出**

#### 当会话提示 “Context left until auto-compact: 3%”，说明历史记录快满了。此时会自动触发压缩（约 150 秒），也可手动用 `/compact` 命令续命，避免对话中断。

#### **恢复与查看历史**

- 用 `claude -c` 直接进入上次对话；
- 用 `claude -r` 选择历史会话恢复，适合中途退出后继续工作。

### 五、资源监控与批量任务：把控节奏不浪费

#### **实时监控 token 用量**

想知道每天 / 每小时消耗多少资源？运行 `npx ccusage@latest` 查看按天用量，或 `npx ccusage blocks --live` 实时监控消耗速度。若速度过快，可手动处理 git commit 等费 token 的操作，避免超额。

```text
npx ccusage@latest
```

#### **批量任务高效处理**

需要执行几十个重复任务（比如批量生成文档章节）用脚本式用法：

1. 把任务按行写入 `TASK.md` （一行一个任务）；
2. 运行命令：

```text
cat TASK.md | while IFS= read -r line; do echo $line; claude -p "$line" --debug; done
```

可加 `timeout` 防止单个任务卡死，同时用 `--allowedTools "Edit"` 限制权限，避免意外操作。注意不要并发执行，否则可能触发限额封禁。

### 六、避坑与进阶：让 Claude 更 “听话”

#### **给足自由，也要做好防护**

- 开启 auto-accept edits （ Shift+Tab 切换）让 Claude 自动编辑文件，配合 git 版本控制，不怕误操作。
- 执行 Bash 命令时，用 Docker 隔离环境，或用 btrfs 文件系统做快照，既能放开权限，又能快速回滚。
- 避免在会话目录存放 ssh key 等敏感信息，防止跨机操作风险。

#### **严防 “虚假成果”**

Claude 偶尔会 “吹牛”，比如未完成测试就宣称成功。可在 CLAUDE.md 中加入规则：“每次宣称成功必须附证据文件链接”，并定期反问：“真的完成了？有证据吗？” 发现问题及时让其修正。

掌握这些技巧，能让 Claude Code 从 “工具” 变成“高效搭档”，无论是日常编码、项目管理还是批量处理，都能大幅提升效率。记住：核心是按需切换模式、用好全局记忆，再加上适当的监控和防护，就能发挥它的最大价值。

---

## 相关阅读

- 下一篇：[第 02 篇](./02-02-claude-code-接入-crazyrouter-的工程实践.md)
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
