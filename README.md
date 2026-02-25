# OpenClaw-hotskills-zh 🇨🇳

> 致力于将 clawhub.ai 平台的优质安全项目转化为中文版 Skills。降低阅读理解门槛，提供更符合中文开发者习惯的开源技能库。

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/L-LesterYu/OpenClaw-hotskills-zh.svg?style=social)](https://github.com/L-LesterYu/OpenClaw-hotskills-zh/stargazers)

## 📖 项目简介

本项目旨在为中文开发者提供 ClawHub 平台上优质技能（Skills）的中文版本，让使用 OpenClaw 的开发者能够更轻松地理解和使用各种技能。

### 🎯 项目目标

- 🌏 **降低阅读门槛**：将英文 Skills 翻译为清晰的中文文档
- 🔧 **保持技术准确**：保留代码示例和技术术语的原汁原味
- 📚 **提供详细说明**：增加使用示例和最佳实践
- 🚀 **便于安装使用**：提供完整的安装和使用指南

## 📦 已发布的 Skills

### 1. ontology-zh - 类型化知识图谱

**版本**: v0.1.2
**状态**: ✅ 已发布
**来源**: [ClawHub - Ontology](https://clawhub.ai/kn72dv4fm7ss7swbq47nnpad9x7zy2jh/ontology)

**功能**：
- 🗂️ **类型化实体系统**：支持人员、项目、任务、事件、文档等多种实体类型
- 🔗 **关系管理**：在实体之间建立和管理关系
- ✅ **约束验证**：自动验证实体属性和关系约束
- 🔍 **图谱查询**：强大的查询和遍历功能
- 🔄 **跨技能通信**：支持不同技能之间的数据共享

**核心类型**：
- **智能体与人员**: Person, Organization
- **工作管理**: Project, Task, Goal
- **时间与地点**: Event, Location
- **信息**: Document, Message, Thread, Note
- **资源**: Account, Device, Credential

**安装**：
```bash
cd ~/.openclaw/skills/
git clone https://github.com/L-LesterYu/OpenClaw-hotskills-zh.git temp-repo
cp -r temp-repo/skills/ontology-zh ./
rm -rf temp-repo
```

**快速开始**：
```bash
# 初始化存储
mkdir -p memory/ontology
touch memory/ontology/graph.jsonl

# 创建实体
python3 scripts/ontology.py create --type Person --props '{"name":"张三","email":"zhangsan@example.com"}'
python3 scripts/ontology.py create --type Project --props '{"name":"网站重新设计","status":"active"}'

# 查询实体
python3 scripts/ontology.py list --type Person
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'

# 建立关系
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_001
```

**使用场景**：
- "记住..." → 创建/更新实体
- "我知道什么关于X？" → 查询图谱
- "链接X到Y" → 创建关系
- "显示项目Z的所有任务" → 图遍历

[查看详细文档](./skills/ontology-zh/SKILL.md) | [查询参考](./skills/ontology-zh/references/queries.md) | [模式定义](./skills/ontology-zh/references/schema.md)

---

### 2. gog-zh - Google Workspace 命令行工具

**版本**: v1.0.0
**状态**: ✅ 已发布
**来源**: [ClawHub - Gog](https://clawhub.ai/kn70pywhg0fyz996kpa8xj89s57yhv26/gog)

**功能**：
- 📧 **Gmail 管理**：搜索、发送邮件
- 📅 **日历操作**：查询和管理日历事件
- 💾 **云盘搜索**：搜索 Google Drive 文件
- 👥 **联系人管理**：列出和管理联系人
- 📊 **表格操作**：读取、更新、追加、清除表格数据
- 📄 **文档处理**：导出和查看 Google Docs

**安装**：
```bash
# 1. 安装 gog CLI 工具
brew install steipete/tap/gogcli

# 2. 安装 Skill
cd ~/.openclaw/skills/
git clone https://github.com/L-LesterYu/OpenClaw-hotskills-zh.git temp-repo
cp -r temp-repo/skills/gog-zh ./
rm -rf temp-repo
```

**使用**：
```bash
# 设置 OAuth 凭证
gog auth credentials /path/to/client_secret.json
gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs

# 常用命令示例
gog gmail search 'newer_than:7d' --max 10
gog calendar events <calendarId> --from <iso> --to <iso>
gog sheets get <sheetId> "工作表!A1:D10" --json
```

[查看详细文档](./skills/gog-zh/SKILL.md)

---

### 3. Agent-Browser-zh - AI 浏览器自动化工具

**版本**: v1.0.0
**状态**: ✅ 已发布
**来源**: [ClawHub - Agent Browser](https://clawhub.ai)

**功能**：
- 🌐 **浏览器自动化**：专为 AI 智能体设计的浏览器自动化 CLI
- 🎯 **确定性引用**：使用无障碍树的稳定引用，避免脆弱的 CSS 选择器
- 🔄 **快速架构**：Rust CLI + Node.js 守护进程，首次 ~2秒，后续 ~100毫秒
- 📊 **结构化输出**：JSON 格式输出，完美适配 LLM 解析
- 🚀 **AI 优化工作流**：快照-操作-验证的完整工作流

**核心优势**：
- **确定性引用** - `@e2` 始终指向快照中的同一元素
- **无障碍树** - 语义化页面理解，比 HTML 和截图更适合 AI
- **快速执行** - 浏览器持久化，命令间无需重启
- **复杂流程** - 完美处理多步骤表单和工作流

**安装**：
```bash
# 1. 安装 agent-browser CLI
npm install -g agent-browser
agent-browser install  # 下载 Chromium（约30秒）

# 2. 安装 Skill
cd ~/.openclaw/skills/
git clone https://github.com/L-LesterYu/OpenClaw-hotskills-zh.git temp-repo
cp -r temp-repo/skills/Agent-Browser-zh ./
rm -rf temp-repo
```

**快速开始**：
```bash
# 导航到网站
agent-browser open https://example.com

# 获取页面结构（AI "看到" 页面）
agent-browser snapshot -i --json

# 执行操作（使用确定性引用）
agent-browser click @e2
agent-browser fill @e3 "test@example.com"

# 验证状态
agent-browser snapshot -i --json

# 完成
agent-browser close
```

**使用场景**：
- 自动化多步骤 Web 工作流
- 填写复杂表单
- 可靠、可重复的浏览器自动化
- 处理动态/现代 Web 应用
- 成本敏感操作（无需视觉 API）

[查看详细文档](./skills/Agent-Browser-zh/SKILL.md) | [快速参考](./skills/Agent-Browser-zh/README.md)

---

### 4. self-improvement-zh - 自我改进技能

**版本**: v1.0.0
**状态**: ✅ 已发布

**功能**：
- 📝 记录学习内容、错误和功能请求
- 🔄 实现持续改进和知识积累
- 📊 结构化的日志管理
- 🔍 支持模式检测和优先级管理

**安装**：
```bash
cd ~/.openclaw/skills/
git clone https://github.com/L-LesterYu/OpenClaw-hotskills-zh.git temp-repo
cp -r temp-repo/skills/self-improvement-zh ./
rm -rf temp-repo
```

[查看详细文档](./skills/self-improvement-zh/README.md)

## 🚀 快速开始

### 前置要求

- OpenClaw 已安装并配置
- 基本的命令行操作能力

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/L-LesterYu/OpenClaw-hotskills-zh.git
```

2. **选择并安装 Skill**
```bash
cd OpenClaw-hotskills-zh/
cp -r <skill-name> ~/.openclaw/skills/
```

3. **验证安装**
```bash
ls ~/.openclaw/skills/<skill-name>/
```

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. **Fork 本仓库**
2. **创建特性分支** (`git checkout -b feature/AmazingSkill`)
3. **提交更改** (`git commit -m '添加某个中文版 Skill'`)
4. **推送到分支** (`git push origin feature/AmazingSkill`)
5. **创建 Pull Request`

### 贡献规范

- ✅ 确保翻译准确、流畅
- ✅ 保持代码示例和技术术语不变
- ✅ 添加详细的使用说明和示例
- ✅ 遵循现有的文件结构
- ✅ 更新相关的 README 文档

## 📝 待办事项

- [ ] 添加更多 ClawHub 优质 Skills 的中文版本
- [ ] 创建自动化测试脚本
- [ ] 建立持续集成/持续部署流程
- [ ] 编写更详细的贡献指南
- [ ] 创建 Skill 质量检查工具

## 🔗 相关链接

- [OpenClaw 官网](https://openclaw.ai)
- [ClawHub Skills 市场](https://clawhub.ai)
- [OpenClaw 文档](https://docs.openclaw.ai)
- [Agent Skills 规范](https://agentskills.io/specification)

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

感谢以下项目和个人的支持：

- [OpenClaw](https://github.com/openclaw/openclaw) - 强大的 AI 代理框架
- [ClawHub](https://clawhub.ai) - Skills 分享平台
- 所有原始 Skills 的作者们
- 为本项目贡献的所有开发者

## 📮 联系方式

- **项目地址**: https://github.com/L-LesterYu/OpenClaw-hotskills-zh
- **问题反馈**: [GitHub Issues](https://github.com/L-LesterYu/OpenClaw-hotskills-zh/issues)

---

**如果这个项目对您有帮助，请给一个 ⭐️ Star 支持一下！**

Made with ❤️ by [L-LesterYu](https://github.com/L-LesterYu)
