# skill-agent-browser-zh

[agent-browser](https://github.com/vercel-labs/agent-browser) 的 OpenClaw 技能 — 最适合 AI 智能体的浏览器自动化 CLI。

## 为什么这更好

### 确定性引用（AI 的游戏规则改变者）

传统的浏览器自动化使用经常失效的 **CSS 选择器**或**坐标**。agent-browser 使用来自无障碍树的**确定性引用**：

```bash
# 获取快照 — 每个元素获得稳定的引用
agent-browser snapshot -i --json
# 输出: - button "Submit" [ref=e2]

# 使用该引用 — 它对该元素永不改变
agent-browser click @e2
```

**为什么这很重要：**
- CSS 选择器在网站更新时失效
- 坐标在响应式布局上失败
- 基于视觉的自动化慢且昂贵
- **引用就是好用** — 指向快照中的确切元素

### 为 AI 智体构建（而非开发者）

| | 传统工具 | agent-browser |
|---|---|---|
| **元素定位** | 脆弱的选择器 | 确定性引用 |
| **页面理解** | 原始 HTML 混合体 | 语义无障碍树 |
| **输出** | 文本日志 | 结构化 JSON |
| **速度** | 每个命令慢 | 快速守护进程架构 |
| **设计对象** | 人类开发者 | AI 智能体 |

### 快速架构

- **Rust CLI** — 用于即时命令解析的原生二进制文件
- **Node.js 守护进程** — 浏览器在命令之间保持活跃
- **首次启动：** ~2 秒
- **后续命令：** ~100 毫秒

## 安装

### 前置条件

```bash
npm install -g agent-browser
agent-browser install  # 下载 Chromium（约 30 秒）
```

### 安装技能

```bash
cd ~/.openclaw/skills  # 或 ~/clawd/skills
git clone https://github.com/clawdbrunner/skill-agent-browser.git agent-browser
```

## AI 工作流

让 agent-browser 发挥作用的模式：

```bash
# 1. 导航
agent-browser open example.com

# 2. 获取结构化快照（AI "看到" 页面）
agent-browser snapshot -i --json

# 3. AI 选择引用，执行操作
agent-browser click @e1
agent-browser fill @e2 "user@example.com"

# 4. 验证状态已更改
agent-browser snapshot -i --json

# 5. 完成
agent-browser close
```

## 快速参考

### 基本命令

```bash
# 导航
agent-browser open <url> [--json] [--headed]

# 快照（杀手级功能）
agent-browser snapshot [-i] [-c] [--json]              # 交互、紧凑、JSON

# 使用引用交互
agent-browser click @e1
agent-browser fill @e2 "text"
agent-browser type @e2 "text"                          # 不清空
agent-browser press Enter

# 状态检查
agent-browser get text @e1
agent-browser get url
agent-browser is visible @e2

# 会话管理
agent-browser --session <name> open <url>            # 隔离会话
agent-browser --profile <path> open <url>            # 持久化 cookies
agent-browser close
```

### 快照选项（控制 AI 看到的内容）

| 标志 | 用途 |
|------|---------|
| `-i` | 仅交互元素 — **推荐** |
| `-c` | 紧凑（移除空元素） |
| `-d <n>` | 限制树深度 |
| `-s <sel>` | 范围限制到 CSS 选择器 |
| `--json` | 机器可读的 JSON — **AI 必需** |

**AI 最佳：** `agent-browser snapshot -i -c --json`

### 选择器策略（排名）

1. **引用**（最佳）：`agent-browser click @e2`
2. **语义**：`agent-browser find role button click --name "Submit"`
3. **CSS**：`agent-browser click "#submit"`
4. **文本/XPath**（最后手段）：`agent-browser click "text=Submit"`

## 示例：复杂表单自动化

```bash
# 打开计费门户
agent-browser open https://portal.aeronetpr.com

# 使用快照中的引用进行登录流程
agent-browser fill @e1 "username"
agent-browser fill @e2 "password"
agent-browser click @e3

# 等待导航，获取新状态
sleep 2
agent-browser snapshot -i --json

# 添加信用卡
agent-browser click @e24                                    # "添加新信用卡"
agent-browser fill @e10 "John Smith"                       # 卡上姓名
agent-browser fill @e11 "4111111111111111"                 # 卡号（测试）
agent-browser fill @e12 "12/2030"                          # 有效期
agent-browser fill @e13 "123"                              # CVV
agent-browser fill @e14 "123 Main Street"                  # 地址
agent-browser fill @e260 "San Juan"                        # 城市
agent-browser fill @e322 "00907"                           # 邮编
agent-browser click @e324                                  # 提交

# 验证
agent-browser snapshot -i --json

# 清理
agent-browser close
```

## 文档

完整文档请参见 [SKILL.md](SKILL.md)，包括：
- 与其他工具的详细比较
- 所有命令和选项
- AI 智能体技巧
- 何时使用此工具与内置浏览器工具

## 与替代方案比较

| 工具 | agent-browser 优势 |
|------|------------------------|
| **Puppeteer/Playwright** | 专为 AI 构建，确定性引用 vs 脆弱选择器 |
| **Selenium** | 快 10 倍，现代架构 |
| **browser-use** | 更好的引用系统，更快的 CLI |
| **基于视觉** | 便宜 100 倍，快 10 倍，无 API 调用 |
| **OpenClaw browser** | 更适合复杂的多步骤流程 |

## 何时使用

**在以下情况使用 agent-browser：**
- 多步骤 Web 工作流
- 复杂表单填写
- 可靠、可重复的自动化
- 动态/现代 Web 应用
- 成本敏感操作（无视觉 API）

**在以下情况使用 OpenClaw 内置浏览器工具：**
- 简单的单页检查
- 快速截图
- 已经过身份验证的 Chrome 会话

## 链接

- **上游项目：** https://github.com/vercel-labs/agent-browser
- **此技能：** https://github.com/clawdbrunner/skill-agent-browser
- **发布：** https://github.com/clawdbrunner/skill-agent-browser/releases

## 许可证

MIT
