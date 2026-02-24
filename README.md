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

### 1. self-improvement-zh - 自我改进技能

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

**使用**：
- 编辑 `~/.openclaw/workspace/.learnings/LEARNINGS.md` 记录学习内容
- 编辑 `~/.openclaw/workspace/.learnings/ERRORS.md` 记录错误
- 编辑 `~/.openclaw/workspace/.learnings/FEATURE_REQUESTS.md` 记录功能请求

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
cd OpenClaw-hotskills-zh/skills/
cp -r <skill-name> ~/.openclaw/skills/
```

3. **验证安装**
```bash
ls ~/.openclaw/skills/<skill-name>/
```

## 📋 目录结构

```
OpenClaw-hotskills-zh/
├── README.md                   # 项目说明文档
├── LICENSE                     # MIT 许可证
├── skills/                     # Skills 目录
│   └── self-improvement-zh/   # 自我改进技能（中文版）
│       ├── SKILL.md           # 技能主文档
│       ├── README.md          # 详细使用说明
│       ├── assets/            # 资源文件
│       ├── scripts/           # 脚本工具
│       ├── hooks/             # OpenClaw 钩子
│       └── .learnings/        # 学习文件模板
│           ├── LEARNINGS.md
│           ├── ERRORS.md
│           └── FEATURE_REQUESTS.md
└── docs/                      # 其他文档
    └── contributing.md        # 贡献指南
```

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. **Fork 本仓库**
2. **创建特性分支** (`git checkout -b feature/AmazingSkill`)
3. **提交更改** (`git commit -m '添加某个中文版 Skill'`)
4. **推送到分支** (`git push origin feature/AmazingSkill`)
5. **创建 Pull Request**

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
