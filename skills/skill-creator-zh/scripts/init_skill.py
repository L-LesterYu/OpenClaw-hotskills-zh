#!/usr/bin/env python3
"""
技能初始化器 - 从模板创建新技能

用法:
    init_skill.py <技能名称> --path <路径> [--resources scripts,references,assets] [--examples]

示例:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-new-skill --path skills/public --resources scripts,references
    init_skill.py my-api-helper --path skills/private --resources scripts --examples
    init_skill.py custom-skill --path /custom/location
"""

import argparse
import re
import sys
from pathlib import Path

MAX_SKILL_NAME_LENGTH = 64
ALLOWED_RESOURCES = {"scripts", "references", "assets"}

SKILL_TEMPLATE = """---
name: {skill_name}
description: "TODO: 完成关于技能功能和何时使用的完整说明。包括何时使用此技能 - 触发它的特定场景、文件类型或任务。"
---

# {skill_title}

## 概述

[TODO: 1-2 句话说明此技能启用什么功能]

## 构建此技能

[TODO: 选择最适合此技能目的的结构。常见模式：

**1. 基于工作流程**（最适合顺序流程）
- 当有清晰的分步过程时效果很好
- 示例：DOCX 技能包含"工作流程决策树" -> "读取" -> "创建" -> "编辑"
- 结构：## 概述 -> ## 工作流程决策树 -> ## 步骤 1 -> ## 步骤 2...

**2. 基于任务**（最适合工具集合）
- 当技能提供不同操作/能力时效果很好
- 示例：PDF 技能包含"快速入门" -> "合并 PDF" -> "拆分 PDF" -> "提取文本"
- 结构：## 概述 -> ## 快速入门 -> ## 任务类别 1 -> ## 任务类别 2...

**3. 参考/指南**（最适合标准或规范）
- 对于品牌指南、编码标准或需求效果很好
- 示例：品牌样式包含"品牌指南" -> "颜色" -> "排版" -> "功能"
- 结构：## 概述 -> ## 指南 -> ## 规范 -> ## 用法...

**4. 基于能力**（最适合集成系统）
- 当技能提供多个相互关联的功能时效果很好
- 示例：产品管理包含"核心能力" -> 编号的能力列表
- 结构：## 概述 -> ## 核心能力 -> ### 1. 功能 -> ### 2. 功能...

模式可以根据需要混合使用。大多数技能会组合模式（例如，以基于任务开始，为复杂操作添加工作流程）。

完成后删除整个"构建此技能"部分 - 这只是指导。]

## [TODO: 根据选择的结构替换为第一个主要部分]

[TODO: 在此添加内容。参见现有技能中的示例：
- 技术技能的代码示例
- 复杂工作流程的决策树
- 带有实际用户请求的具体示例
- 根据需要引用脚本/模板/参考资料]

## 资源（可选）

仅创建此技能实际需要的资源目录。如果不需要资源，删除此部分。

### scripts/
可以直接运行以执行特定操作的可执行代码（Python/Bash 等）。

**其他技能的示例：**
- PDF 技能：`fill_fillable_fields.py`、`extract_form_field_info.py` - PDF 操作工具
- DOCX 技能：`document.py`、`utilities.py` - 文档处理 Python 模块

**适用于：** Python 脚本、Shell 脚本或任何执行自动化、数据处理或特定操作的可执行代码。

**注意：** 脚本可以在不加载到上下文的情况下执行，但仍可以被 Codex 读取以进行修补或环境调整。

### references/
预期加载到上下文中以指导 Codex 流程和思考的文档和参考材料。

**其他技能的示例：**
- 产品管理：`communication.md`、`context_building.md` - 详细的工作流程指南
- BigQuery：API 参考文档和查询示例
- 财务：模式文档、公司政策

**适用于：** 深入的文档、API 参考、数据库模式、综合指南或 Codex 在工作时应该参考的任何详细信息。

### assets/
不打算加载到上下文中，而是在 Codex 产生的输出中使用的文件。

**其他技能的示例：**
- 品牌样式：PowerPoint 模板文件 (.pptx)、Logo 文件
- 前端构建器：HTML/React 样板项目目录
- 排版：字体文件 (.ttf, .woff2)

**适用于：** 模板、样板代码、文档模板、图像、图标、字体或任何预期在最终输出中复制或使用的文件。

---

**并非每个技能都需要所有三种类型的资源。**
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
{skill_name} 的示例辅助脚本

这是一个可以直接执行的占位符脚本。
替换为实际实现或如果不需要则删除。

其他技能的真实脚本示例：
- pdf/scripts/fill_fillable_fields.py - 填充 PDF 表单字段
- pdf/scripts/convert_pdf_to_images.py - 将 PDF 页面转换为图像
"""

def main():
    print("这是 {skill_name} 的示例脚本")
    # TODO: 在此添加实际脚本逻辑
    # 这可以是数据处理、文件转换、API 调用等

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# {skill_title} 的参考文档

这是详细参考文档的占位符。
替换为实际参考内容或如果不需要则删除。

其他技能的真实参考文档示例：
- product-management/references/communication.md - 状态更新综合指南
- product-management/references/context_building.md - 收集上下文的深入指南
- bigquery/references/ - API 参考和查询示例

## 参考文档何时有用

参考文档适用于：
- 全面的 API 文档
- 详细的工作流程指南
- 复杂的多步骤流程
- 对于主 SKILL.md 来说太长的信息
- 仅特定用例需要的内容

## 结构建议

### API 参考示例
- 概述
- 认证
- 带示例的端点
- 错误代码
- 速率限制

### 工作流程指南示例
- 前提条件
- 分步说明
- 常见模式
- 故障排除
- 最佳实践
"""

EXAMPLE_ASSET = """# 示例资产文件

此占位符代表资产文件的存储位置。
替换为实际资产文件（模板、图像、字体等）或如果不需要则删除。

资产文件不打算加载到上下文中，而是在 Codex 产生的输出中使用。

其他技能的示例资产文件：
- 品牌指南：logo.png、slides_template.pptx
- 前端构建器：包含 HTML/React 样板的 hello-world/ 目录
- 排版：custom-font.ttf、font-family.woff2
- 数据：sample_data.csv、test_dataset.json

## 常见资产类型

- 模板：.pptx、.docx、样板目录
- 图像：.png、.jpg、.svg、.gif
- 字体：.ttf、.otf、.woff、.woff2
- 样板代码：项目目录、起始文件
- 图标：.ico、.svg
- 数据文件：.csv、.json、.xml、.yaml

注意：这是文本占位符。实际资产可以是任何文件类型。
"""


def normalize_skill_name(skill_name):
    """将技能名称标准化为小写连字符形式。"""
    normalized = skill_name.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    normalized = normalized.strip("-")
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized


def title_case_skill_name(skill_name):
    """将连字符形式的技能名称转换为标题大小写用于显示。"""
    return " ".join(word.capitalize() for word in skill_name.split("-"))


def parse_resources(raw_resources):
    if not raw_resources:
        return []
    resources = [item.strip() for item in raw_resources.split(",") if item.strip()]
    invalid = sorted({item for item in resources if item not in ALLOWED_RESOURCES})
    if invalid:
        allowed = ", ".join(sorted(ALLOWED_RESOURCES))
        print(f"[错误] 未知的资源类型: {', '.join(invalid)}")
        print(f"   允许的: {allowed}")
        sys.exit(1)
    deduped = []
    seen = set()
    for resource in resources:
        if resource not in seen:
            deduped.append(resource)
            seen.add(resource)
    return deduped


def create_resource_dirs(skill_dir, skill_name, skill_title, resources, include_examples):
    for resource in resources:
        resource_dir = skill_dir / resource
        resource_dir.mkdir(exist_ok=True)
        if resource == "scripts":
            if include_examples:
                example_script = resource_dir / "example.py"
                example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
                example_script.chmod(0o755)
                print("[OK] 已创建 scripts/example.py")
            else:
                print("[OK] 已创建 scripts/")
        elif resource == "references":
            if include_examples:
                example_reference = resource_dir / "api_reference.md"
                example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
                print("[OK] 已创建 references/api_reference.md")
            else:
                print("[OK] 已创建 references/")
        elif resource == "assets":
            if include_examples:
                example_asset = resource_dir / "example_asset.txt"
                example_asset.write_text(EXAMPLE_ASSET)
                print("[OK] 已创建 assets/example_asset.txt")
            else:
                print("[OK] 已创建 assets/")


def init_skill(skill_name, path, resources, include_examples):
    """
    使用 SKILL.md 模板初始化新技能目录。

    参数:
        skill_name: 技能名称
        path: 应创建技能目录的路径
        resources: 要创建的资源目录
        include_examples: 是否在资源目录中创建示例文件

    返回:
        创建的技能目录路径，如果出错则返回 None
    """
    # 确定技能目录路径
    skill_dir = Path(path).resolve() / skill_name

    # 检查目录是否已存在
    if skill_dir.exists():
        print(f"[错误] 技能目录已存在: {skill_dir}")
        return None

    # 创建技能目录
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"[OK] 已创建技能目录: {skill_dir}")
    except Exception as e:
        print(f"[错误] 创建目录时出错: {e}")
        return None

    # 从模板创建 SKILL.md
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title)

    skill_md_path = skill_dir / "SKILL.md"
    try:
        skill_md_path.write_text(skill_content)
        print("[OK] 已创建 SKILL.md")
    except Exception as e:
        print(f"[错误] 创建 SKILL.md 时出错: {e}")
        return None

    # 如果请求，创建资源目录
    if resources:
        try:
            create_resource_dirs(skill_dir, skill_name, skill_title, resources, include_examples)
        except Exception as e:
            print(f"[错误] 创建资源目录时出错: {e}")
            return None

    # 打印后续步骤
    print(f"\n[OK] 技能 '{skill_name}' 已在 {skill_dir} 成功初始化")
    print("\n后续步骤:")
    print("1. 编辑 SKILL.md 以完成 TODO 项目并更新描述")
    if resources:
        if include_examples:
            print("2. 自定义或删除 scripts/、references/ 和 assets/ 中的示例文件")
        else:
            print("2. 根据需要向 scripts/、references/ 和 assets/ 添加资源")
    else:
        print("2. 仅在需要时创建资源目录（scripts/、references/、assets/）")
    print("3. 准备好后运行验证器检查技能结构")

    return skill_dir


def main():
    parser = argparse.ArgumentParser(
        description="使用 SKILL.md 模板创建新技能目录。",
    )
    parser.add_argument("skill_name", help="技能名称（标准化为连字符形式）")
    parser.add_argument("--path", required=True, help="技能的输出目录")
    parser.add_argument(
        "--resources",
        default="",
        help="逗号分隔的列表: scripts,references,assets",
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="在选定的资源目录中创建示例文件",
    )
    args = parser.parse_args()

    raw_skill_name = args.skill_name
    skill_name = normalize_skill_name(raw_skill_name)
    if not skill_name:
        print("[错误] 技能名称必须包含至少一个字母或数字。")
        sys.exit(1)
    if len(skill_name) > MAX_SKILL_NAME_LENGTH:
        print(
            f"[错误] 技能名称 '{skill_name}' 太长（{len(skill_name)} 个字符）。"
            f"最大为 {MAX_SKILL_NAME_LENGTH} 个字符。"
        )
        sys.exit(1)
    if skill_name != raw_skill_name:
        print(f"注意: 技能名称从 '{raw_skill_name}' 标准化为 '{skill_name}'。")

    resources = parse_resources(args.resources)
    if args.examples and not resources:
        print("[错误] --examples 需要设置 --resources。")
        sys.exit(1)

    path = args.path

    print(f"正在初始化技能: {skill_name}")
    print(f"   位置: {path}")
    if resources:
        print(f"   资源: {', '.join(resources)}")
        if args.examples:
            print("   示例: 已启用")
    else:
        print("   资源: 无（根据需要创建）")
    print()

    result = init_skill(skill_name, path, resources, args.examples)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
