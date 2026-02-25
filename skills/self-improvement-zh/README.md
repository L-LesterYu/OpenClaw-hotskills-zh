# Self-Improvement-zh - 自我改进技能（中文版）

> 捕获学习内容、错误和纠正以实现持续改进

[![版本](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/L-LesterYu/OpenClaw-hotskills-zh)
[![许可证](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)

## 📖 简介

这是 [self-improving-agent](https://clawhub.ai/pskoett/self-improving-agent) 技能的完整中文版本，专为中文 OpenClaw 用户设计。该技能帮助你记录学习内容、错误和功能请求，实现持续改进和知识积累。

### ✨ 主要特性

- 🌏 **完全中文化** - 所有说明和模板都使用中文
- 📝 **结构化记录** - 使用标准化的格式记录学习、错误和功能请求
- 🔄 **持续改进** - 支持知识积累和模式检测
- 📊 **优先级管理** - 支持 low、medium、high、critical 四个优先级
- 🔗 **交叉引用** - 通过 `See Also` 链接相关条目
- 📈 **提升机制** - 将重要的学习内容提升到项目记忆

## 🚀 快速开始

### 安装

#### 方法 1: 从本仓库安装（推荐）

```bash
# 克隆仓库
git clone https://github.com/L-LesterYu/OpenClaw-hotskills-zh.git

# 复制技能到 OpenClaw 目录
cp -r OpenClaw-hotskills-zh/skills/self-improvement-zh ~/.openclaw/skills/

# 创建学习文件目录
mkdir -p ~/.openclaw/workspace/.learnings

# 复制模板文件
cp OpenClaw-hotskills-zh/skills/self-improvement-zh/.learnings/*.md ~/.openclaw/workspace/.learnings/
```

#### 方法 2: 直接下载

```bash
cd ~/.openclaw/skills/
git clone https://github.com/L-LesterYu/OpenClaw-hotskills-zh.git temp-repo
cp -r temp-repo/skills/self-improvement-zh ./
rm -rf temp-repo
```

### 验证安装

```bash
# 检查技能目录
ls ~/.openclaw/skills/self-improvement-zh/

# 检查学习文件
ls ~/.openclaw/workspace/.learnings/
```

### 基本使用

#### 1. 记录学习内容

编辑 `~/.openclaw/workspace/.learnings/LEARNINGS.md`：

```markdown
## [LRN-20250224-001] best_practice

**Logged**: 2025-02-24T18:00:00+08:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
使用 git clone 安装 ClawHub 技能的替代方法

### Details
当 clawdhub CLI 不可用时，可以直接使用 git clone 将技能安装到 ~/.openclaw/skills/ 目录

### Suggested Action
将此方法添加到文档中

### Metadata
- Source: user_feedback
- Related Files: 
- Tags: installation, git, skills

---
```

#### 2. 记录错误

编辑 `~/.openclaw/workspace/.learnings/ERRORS.md`：

```markdown
## [ERR-20250224-001] command_not_found

**Logged**: 2025-02-24T18:05:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
clawdhub 命令未找到

### Error
```
clawdhub: command not found
```

### Context
- 尝试运行 `clawdhub install`
- 系统中未安装 clawdhub CLI

### Suggested Fix
使用 git clone 作为替代方案

### Metadata
- Reproducible: yes
- Related Files: 

### Resolution
- **Resolved**: 2025-02-24T18:06:00+08:00
- **Notes**: 使用 git clone 成功安装

---
```

#### 3. 记录功能请求

编辑 `~/.openclaw/workspace/.learnings/FEATURE_REQUESTS.md`：

```markdown
## [FEAT-20250224-001] auto_translation

**Logged**: 2025-02-24T18:10:00+08:00
**Priority**: medium
**Status**: pending
**Area**: backend

### Requested Capability
自动翻译技能功能

### User Context
希望能够自动将英文技能翻译成中文

### Complexity Estimate
complex

### Suggested Implementation
创建翻译工具，保持代码示例不变

### Metadata
- Frequency: first_time
- Related Features: localization

---
```

## 📋 快速参考

| 情况 | 操作 | 文件 |
|------|------|------|
| 命令/操作失败 | 记录错误 | `ERRORS.md` |
| 用户纠正你 | 记录学习 | `LEARNINGS.md` (correction) |
| 想要新功能 | 记录请求 | `FEATURE_REQUESTS.md` |
| 发现更好的方法 | 记录学习 | `LEARNINGS.md` (best_practice) |
| 知识过时 | 记录学习 | `LEARNINGS.md` (knowledge_gap) |

## 🎯 使用场景

### 什么时候记录？

1. **命令失败** - 返回非零退出码
2. **用户纠正** - "不对，应该是..."
3. **发现新知识** - 学到了新东西
4. **找到更好的方法** - 改进了原有方案
5. **功能请求** - "我希望..."

### 学习类别

- `correction` - 纠正错误
- `knowledge_gap` - 知识缺口
- `best_practice` - 最佳实践

### 优先级

| 优先级 | 使用场景 |
|--------|---------|
| `critical` | 阻止核心功能，数据丢失风险 |
| `high` | 影响重大，重复问题 |
| `medium` | 影响中等，存在解决方法 |
| `low` | 轻微不便，边缘情况 |

### 区域标签

- `frontend` - UI、组件
- `backend` - API、服务
- `infra` - CI/CD、部署
- `tests` - 测试
- `docs` - 文档
- `config` - 配置

## 📊 高级功能

### 1. 条目 ID 格式

```
TYPE-YYYYMMDD-XXX
```

- TYPE: `LRN` (学习), `ERR` (错误), `FEAT` (功能)
- YYYYMMDD: 日期
- XXX: 序号或随机字符

示例：`LRN-20250224-001`

### 2. 交叉引用

使用 `See Also` 链接相关条目：

```markdown
### Metadata
- See Also: LRN-20250224-001, ERR-20250224-002
```

### 3. 状态管理

- `pending` - 待处理
- `in_progress` - 处理中
- `resolved` - 已解决
- `wont_fix` - 不修复
- `promoted` - 已提升

### 4. 提升到项目记忆

将重要的学习内容提升到工作区文件：

| 学习类型 | 提升到 | 示例 |
|---------|--------|------|
| 行为模式 | `SOUL.md` | "简洁明了" |
| 工作流改进 | `AGENTS.md` | "生成子代理" |
| 工具陷阱 | `TOOLS.md` | "Git 需要认证" |

### 5. 定期审查

```bash
# 统计待处理项
grep -h "Status\*\*: pending" ~/.openclaw/workspace/.learnings/*.md | wc -l

# 列出高优先级项
grep -B5 "Priority\*\*: high" ~/.openclaw/workspace/.learnings/*.md

# 查找特定区域
grep -l "Area\*\*: backend" ~/.openclaw/workspace/.learnings/*.md
```

## 🔧 配置

### 可选：启用钩子

```bash
# 复制钩子
cp -r ~/.openclaw/skills/self-improvement-zh/hooks/openclaw ~/.openclaw/hooks/self-improvement-zh

# 启用钩子
openclaw hooks enable self-improvement-zh
```

### Gitignore 选项

**保持本地**（每个开发者）：
```gitignore
.learnings/
```

**团队共享**：
不添加到 .gitignore

## 📚 最佳实践

1. ✅ **立即记录** - 问题发生后立即记录
2. ✅ **要具体** - 提供详细的上下文
3. ✅ **包含步骤** - 特别是错误复现步骤
4. ✅ **链接文件** - 关联相关文件路径
5. ✅ **建议修复** - 提供具体的解决方案
6. ✅ **使用一致** - 统一类别和标签
7. ✅ **积极提升** - 重要内容提升到项目记忆
8. ✅ **定期审查** - 定期检查和更新条目

## 🔗 相关链接

- [原始技能 (英文)](https://clawhub.ai/pskoett/self-improving-agent)
- [OpenClaw 文档](https://docs.openclaw.ai)
- [Agent Skills 规范](https://agentskills.io/specification)

## 📄 许可证

本项目基于 MIT 许可证开源。原始技能由 [@pskoett](https://github.com/pskoett) 创建。

## 🙏 致谢

- 感谢 [@pskoett](https://github.com/pskoett) 创建原始的 self-improving-agent 技能
- 感谢 OpenClaw 团队提供优秀的 AI 代理框架
- 感谢所有为本项目贡献的开发者

---

**如果这个技能对您有帮助，请给项目一个 ⭐️ Star！**

Made with ❤️ by [L-LesterYu](https://github.com/L-LesterYu)
