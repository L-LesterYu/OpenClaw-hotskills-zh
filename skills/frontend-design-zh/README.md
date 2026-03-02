# 前端设计终极版

🎨 使用 React、Tailwind CSS 和 shadcn/ui 创建独特、生产级的静态网站——无需设计稿。

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![ClawHub](https://img.shields.io/badge/ClawHub-frontend--design--ultimate-purple)](https://clawhub.ai/skills/frontend-design-ultimate)

## 这是什么？

一个 OpenClaw/Claude Code 技能，从纯文本需求生成大胆、令人难忘的网页设计。无需 Figma、无需线框图——只需描述你想要的。

**核心特性:**
- 🚫 **反AI套路** — 明确指导避免通用设计（无Inter、无紫色渐变、无居中布局）
- 📱 **移动优先模式** — 真正有效的响应式CSS
- ⚡ **两种工作流** — Vite（纯静态）或 Next.js（Vercel部署）
- 🧩 **shadcn/ui 组件** — 预装10个常用组件，通过CLI添加更多
- 📦 **单文件打包** — 将整个网站打包为一个HTML文件
- 🔗 **可组合护栏** — 与 `design-taste-frontend` 配对使用更严格的反套路强制，而本技能保持为工作流/生成器层

## 快速开始

### 安装技能

```bash
# OpenClaw
openclaw skill install frontend-design-ultimate

# Claude Code（复制到 .claude/skills/）
git clone https://github.com/kesslerio/frontend-design-ultimate-clawhub-skill.git ~/.claude/skills/frontend-design-ultimate
```

### 使用

只需描述你想要的：

```
为一个AI写作工具构建SaaS落地页。深色主题，
编辑排版风格，微妙纹理背景。页面包括：带动画演示的英雄区、
功能网格、价格表、FAQ手风琴、页脚。
```

技能会：
1. 确定一个大胆的美学方向
2. 选择独特的排版（无Inter！）
3. 使用 React + Tailwind + shadcn/ui 构建
4. 应用移动优先响应式模式
5. 输出生产就绪的代码

## 有什么不同？

### 对比通用AI设计
| 通用AI | 本技能 |
|------------|------------|
| 到处是Inter字体 | 独特的排版选择 |
| 紫色渐变 | 符合语境的调色板 |
| 居中布局 | 有意图的空间构成 |
| 无动画 | 协调的动效 |
| 纯色背景 | 有氛围的纹理 |

### 基于以下
- **Anthropic的frontend-design** — 设计哲学、反AI套路指南
- **Anthropic的web-artifacts-builder** — React+Tailwind+shadcn脚手架
- **社区frontend-design-v2** — 移动优先响应式模式

## 工作流

### 选项A: Vite（纯静态）
```bash
bash scripts/init-vite.sh my-site
cd my-site
npm run dev

# 构建
npm run build

# 打包为单个HTML
bash scripts/bundle-artifact.sh
```

### 选项B: Next.js（Vercel）
```bash
bash scripts/init-nextjs.sh my-site
cd my-site
npm run dev

# 部署
vercel
```

## 文档

- [SKILL.md](SKILL.md) — 主要技能说明
- [references/design-philosophy.md](references/design-philosophy.md) — 反AI套路宣言
- [references/mobile-patterns.md](references/mobile-patterns.md) — 响应式CSS模式
- [references/shadcn-components.md](references/shadcn-components.md) — 组件快速参考
- [templates/site-config.ts](templates/site-config.ts) — 可编辑内容配置示例

## 要求

- Node.js 18+
- npm

## 许可证

Apache 2.0 — 详见 [LICENSE](LICENSE)

## 致谢

站在以下巨人的肩膀上：
- [Anthropic's Claude Skills](https://github.com/anthropics/skills)
- [shadcn/ui](https://ui.shadcn.com)
- [Tailwind CSS](https://tailwindcss.com)
- [nhatmobile1's frontend-design-v2](https://github.com/nhatmobile1/claude-skills)

---

由 [Kessler.io](https://kessler.io) 用 🎨 制作
