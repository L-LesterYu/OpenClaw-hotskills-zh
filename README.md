# Ontology 中文版 (Ontology-zh)

一个类型化知识图谱技能，用于结构化智能体记忆和可组合技能。

## 简介

Ontology-zh 是 [Ontology](https://clawhub.ai/kn72dv4fm7ss7swbq47nnpad9x7zy2jh/ontology) 技能的中文翻译版本，专为 OpenClaw 智能体设计。它提供了一个类型化词汇表和约束系统，用于将知识表示为可验证的图谱。

## 核心特性

- **类型化实体系统**: 支持人员、项目、任务、事件、文档等多种实体类型
- **关系管理**: 在实体之间建立和管理关系
- **约束验证**: 自动验证实体属性和关系约束
- **图谱查询**: 强大的查询和遍历功能
- **跨技能通信**: 支持不同技能之间的数据共享

## 安装

将此技能目录复制到您的 OpenClaw skills 目录：

```bash
cp -r ontology-zh ~/.openclaw/skills/
```

## 快速开始

### 初始化存储

```bash
mkdir -p memory/ontology
touch memory/ontology/graph.jsonl
```

### 创建实体

```bash
# 创建人员
python3 scripts/ontology.py create --type Person --props '{"name":"张三","email":"zhangsan@example.com"}'

# 创建项目
python3 scripts/ontology.py create --type Project --props '{"name":"网站重新设计","status":"active"}'

# 创建任务
python3 scripts/ontology.py create --type Task --props '{"title":"设计首页","status":"open","priority":"high"}'
```

### 查询实体

```bash
# 列出所有人员
python3 scripts/ontology.py list --type Person

# 查询开放任务
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'
```

### 建立关系

```bash
# 将任务关联到项目
python3 scripts/ontology.py relate --from proj_001 --rel has_task --to task_001
```

## 核心类型

### 智能体与人员
- **Person**: 人员信息
- **Organization**: 组织信息

### 工作管理
- **Project**: 项目
- **Task**: 任务
- **Goal**: 目标

### 时间与地点
- **Event**: 事件
- **Location**: 地点

### 信息
- **Document**: 文档
- **Message**: 消息
- **Thread**: 线程
- **Note**: 笔记

### 资源
- **Account**: 账户
- **Device**: 设备
- **Credential**: 凭证

## 文档

- [SKILL.md](SKILL.md) - 完整的技能说明文档
- [references/schema.md](references/schema.md) - 类型定义和约束模式
- [references/queries.md](references/queries.md) - 查询语言和遍历示例

## 使用场景

| 触发词 | 动作 |
|--------|------|
| "记住..." | 创建/更新实体 |
| "我知道什么关于X？" | 查询图谱 |
| "链接X到Y" | 创建关系 |
| "显示项目Z的所有任务" | 图遍历 |
| "什么依赖于X？" | 依赖查询 |

## 与原版的区别

这是 Ontology 技能的完整中文翻译版本，主要改动包括：

1. 所有文档翻译为中文
2. 示例使用中文数据
3. 保留了原始 Python 脚本的完整功能
4. 适用于中文环境下的 OpenClaw 使用

## 许可证

继承自原 Ontology 项目的许可证。

## 致谢

- 原始项目: [Ontology by @oswalpalash](https://clawhub.ai/kn72dv4fm7ss7swbq47nnpad9x7zy2jh/ontology)
- 翻译维护: OpenClaw 中文社区

## 贡献

欢迎提交问题和改进建议！
