# Notion 技能

此技能通过官方 Notion API 操作 Notion 页面和数据库。

## 快速开始

1. 在 https://www.notion.so/my-integrations 创建 Notion 集成
2. 复制内部集成令牌
3. 导出为环境变量：`export NOTION_API_KEY=secret_xxx`
4. 将集成与您想访问的页面/数据库共享

## 功能特性

- 读取和创建页面
- 向页面追加内容块
- 查询数据库
- 创建和更新数据库行
- 架构检查和变更（含安全检查）

## 系统要求

- `NOTION_API_KEY` 环境变量
- `notion-cli` (Node.js) 或 `notion-cli-py` (Python) - 详见 SKILL.md 中的安装说明

## 版本

当前版本：0.1.0

这是一个声明式技能，记录了安全、推荐的操作。实际的 API 调用由本地 CLI 工具执行。
