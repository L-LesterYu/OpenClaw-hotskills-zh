#!/bin/bash
# 主动式 Agent 安全审计
# 定期运行以检查安全问题

# 不要在错误时退出 - 我们想完成所有检查
set +e

echo "🔒 主动式 Agent 安全审计"
echo "=================================="
echo ""

ISSUES=0
WARNINGS=0

# 颜色
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # 无颜色

warn() {
    echo -e "${YELLOW}⚠️  警告: $1${NC}"
    ((WARNINGS++))
}

fail() {
    echo -e "${RED}❌ 问题: $1${NC}"
    ((ISSUES++))
}

pass() {
    echo -e "${GREEN}✅ $1${NC}"
}

# 1. 检查凭据文件权限
echo "📁 检查凭据文件..."
if [ -d ".credentials" ]; then
    for f in .credentials/*; do
        if [ -f "$f" ]; then
            perms=$(stat -f "%Lp" "$f" 2>/dev/null || stat -c "%a" "$f" 2>/dev/null)
            if [ "$perms" != "600" ]; then
                fail "$f 权限为 $perms (应为 600)"
            else
                pass "$f 权限正常 (600)"
            fi
        fi
    done
else
    echo "   未找到 .credentials 目录"
fi
echo ""

# 2. 检查常见文件中暴露的秘密
echo "🔍 扫描暴露的秘密..."
SECRET_PATTERNS="(api[_-]?key|apikey|secret|password|token|auth).*[=:].{10,}"
for f in $(ls *.md *.json *.yaml *.yml .env* 2>/dev/null || true); do
    if [ -f "$f" ]; then
        matches=$(grep -iE "$SECRET_PATTERNS" "$f" 2>/dev/null | grep -v "example\|template\|placeholder\|your-\|<\|TODO" || true)
        if [ -n "$matches" ]; then
            warn "$f 中可能有秘密 - 手动审查"
        fi
    fi
done
pass "秘密扫描完成"
echo ""

# 3. 检查网关安全（如果存在 clawdbot 配置）
echo "🌐 检查网关配置..."
CONFIG_FILE="$HOME/.clawdbot/clawdbot.json"
if [ -f "$CONFIG_FILE" ]; then
    # 检查网关是否绑定到回环地址
    if grep -q '"bind".*"loopback"' "$CONFIG_FILE"; then
        pass "网关绑定到回环地址（未暴露）"
    else
        warn "网关可能未绑定到回环地址 - 检查配置"
    fi
    
    # 检查 Telegram 是否使用配对
    if grep -q '"dmPolicy".*"pairing"' "$CONFIG_FILE"; then
        pass "Telegram DM 策略使用配对"
    fi
else
    echo "   未找到 clawdbot 配置"
fi
echo ""

# 4. 检查 AGENTS.md 中的安全规则
echo "📋 检查 AGENTS.md 中的安全规则..."
if [ -f "AGENTS.md" ]; then
    if grep -qi "injection\|external content\|never execute\|注入\|外部内容\|从不执行" "AGENTS.md"; then
        pass "AGENTS.md 包含注入防御规则"
    else
        warn "AGENTS.md 可能缺少提示注入防御"
    fi
    
    if grep -qi "deletion\|confirm.*delet\|trash\|删除\|确认.*删" "AGENTS.md"; then
        pass "AGENTS.md 包含删除确认规则"
    else
        warn "AGENTS.md 可能缺少删除确认规则"
    fi
else
    warn "未找到 AGENTS.md"
fi
echo ""

# 5. 检查来自不可信来源的技能
echo "📦 检查已安装的技能..."
SKILL_DIR="skills"
if [ -d "$SKILL_DIR" ]; then
    skill_count=$(find "$SKILL_DIR" -maxdepth 1 -type d | wc -l)
    echo "   找到 $((skill_count - 1)) 个已安装技能"
    pass "手动审查技能的可信度"
else
    echo "   未找到技能目录"
fi
echo ""

# 6. 检查 .gitignore
echo "📄 检查 .gitignore..."
if [ -f ".gitignore" ]; then
    if grep -q "\.credentials" ".gitignore"; then
        pass ".credentials 已被 gitignore"
    else
        fail ".credentials 不在 .gitignore 中"
    fi
    
    if grep -q "\.env" ".gitignore"; then
        pass ".env 文件已被 gitignore"
    else
        warn ".env 文件可能未被 gitignore"
    fi
else
    warn "未找到 .gitignore"
fi
echo ""

# 摘要
echo "=================================="
echo "📊 摘要"
echo "=================================="
if [ $ISSUES -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}所有检查通过！${NC}"
elif [ $ISSUES -eq 0 ]; then
    echo -e "${YELLOW}$WARNINGS 个警告，0 个问题${NC}"
else
    echo -e "${RED}$ISSUES 个问题，$WARNINGS 个警告${NC}"
fi
echo ""
echo "定期运行此审计以维护安全。"
