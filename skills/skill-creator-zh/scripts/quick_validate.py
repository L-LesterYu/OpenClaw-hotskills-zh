#!/usr/bin/env python3
"""
技能快速验证脚本 - 最小版本
"""

import re
import sys
from pathlib import Path
from typing import Optional

try:
    import yaml
except ModuleNotFoundError:
    yaml = None

MAX_SKILL_NAME_LENGTH = 64


def _extract_frontmatter(content: str) -> Optional[str]:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def _parse_simple_frontmatter(frontmatter_text: str) -> Optional[dict[str, str]]:
    """
    当 PyYAML 不可用时的最小后备解析器。
    支持 SKILL.md frontmatter 使用的简单 `key: value` 映射。
    """
    parsed: dict[str, str] = {}
    current_key: Optional[str] = None
    for raw_line in frontmatter_text.splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        is_indented = raw_line[:1].isspace()
        if is_indented:
            if current_key is None:
                return None
            current_value = parsed[current_key]
            parsed[current_key] = (
                f"{current_value}\n{stripped}" if current_value else stripped
            )
            continue

        if ":" not in stripped:
            return None
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            return None
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        parsed[key] = value
        current_key = key
    return parsed


def validate_skill(skill_path):
    """技能的基本验证"""
    skill_path = Path(skill_path)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "未找到 SKILL.md"

    try:
        content = skill_md.read_text(encoding="utf-8")
    except OSError as e:
        return False, f"无法读取 SKILL.md: {e}"

    frontmatter_text = _extract_frontmatter(content)
    if frontmatter_text is None:
        return False, "无效的 frontmatter 格式"
    if yaml is not None:
        try:
            frontmatter = yaml.safe_load(frontmatter_text)
            if not isinstance(frontmatter, dict):
                return False, "Frontmatter 必须是 YAML 字典"
        except yaml.YAMLError as e:
            return False, f"Frontmatter 中的 YAML 无效: {e}"
    else:
        frontmatter = _parse_simple_frontmatter(frontmatter_text)
        if frontmatter is None:
            return (
                False,
                "Frontmatter 中的 YAML 无效: 未安装 PyYAML 时不支持的语法",
            )

    allowed_properties = {"name", "description", "license", "allowed-tools", "metadata"}

    unexpected_keys = set(frontmatter.keys()) - allowed_properties
    if unexpected_keys:
        allowed = ", ".join(sorted(allowed_properties))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"SKILL.md frontmatter 中有意外的键: {unexpected}。允许的属性有: {allowed}",
        )

    if "name" not in frontmatter:
        return False, "Frontmatter 中缺少 'name'"
    if "description" not in frontmatter:
        return False, "Frontmatter 中缺少 'description'"

    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"名称必须是字符串，得到 {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"名称 '{name}' 应为连字符形式（仅小写字母、数字和连字符）",
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"名称 '{name}' 不能以连字符开头/结尾或包含连续连字符",
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"名称太长（{len(name)} 个字符）。"
                f"最大为 {MAX_SKILL_NAME_LENGTH} 个字符。",
            )

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"描述必须是字符串，得到 {type(description).__name__}"
    description = description.strip()
    if description:
        if "<" in description or ">" in description:
            return False, "描述不能包含尖括号（< 或 >）"
        if len(description) > 1024:
            return (
                False,
                f"描述太长（{len(description)} 个字符）。最大为 1024 个字符。",
            )

    return True, "技能有效！"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python quick_validate.py <技能目录>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
