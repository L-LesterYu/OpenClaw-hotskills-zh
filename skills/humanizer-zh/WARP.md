# WARP.md

此文件为 WARP（warp.dev）提供关于如何使用此仓库中代码的指导。

## 这个仓库是什么
此仓库是一个完全用 Markdown 实现的 **OpenClaw 技能**。

"运行时"产物是 `SKILL.md`：OpenClaw 读取 YAML 前置元数据（元数据 + 允许的工具）以及随后的提示/指令。

`README.md` 是为人类准备的：安装、使用和模式的紧凑概述。

## 关键文件（及其关系）
- `SKILL.md`
  - 实际的技能定义。
  - 以 YAML 前置元数据（`---` ... `---`）开头，包含 `name`、`version`、`description` 和 `allowed-tools`。
  - 前置元数据之后是编辑器提示：包含示例的权威、详细模式列表。
- `README.md`
  - 安装和使用说明。
  - 包含简化的"24 种模式"表格和简短版本历史。

在更改行为/内容时，将 `SKILL.md` 视为真实来源，并更新 `README.md` 以保持一致。

## 常用命令
### 将技能安装到 OpenClaw
推荐（直接克隆到 OpenClaw 技能目录）：
```bash
mkdir -p ~/.openclaw/skills
git clone https://github.com/blader/humanizer.git ~/.openclaw/skills/humanizer-zh
```

手动安装/更新（仅技能文件）：
```bash
mkdir -p ~/.openclaw/skills/humanizer-zh
cp SKILL.md ~/.openclaw/skills/humanizer-zh/
```

## 如何"运行"它（OpenClaw）
调用技能：
- 直接要求人性化文本

## 安全地进行更改
### 版本控制（保持同步）
- `SKILL.md` 在其 YAML 前置元数据中有一个 `version:` 字段。
- `README.md` 有一个"版本历史"部分。

如果你更新版本，请同时更新两者。

### 编辑 `SKILL.md`
- 保持有效的 YAML 前置元数据格式和缩进。
- 保持模式编号稳定，除非你故意重新编号（因为 README 表格和示例引用相同的编号）。

### 记录非显而易见的修复
如果你更改提示以处理棘手的失败模式（例如，重复的错误编辑或意外的语调变化），请在 `README.md` 的版本历史中添加简短说明，描述修复了什么以及为什么。
