#!/bin/bash
# 站点地图生成器 - 按类别显示所有文档
echo "正在获取 Clawdbot 文档站点地图..."

# 基于 docs.clawd.bot 的类别结构
CATEGORIES=(
  "start"
  "gateway"
  "providers"
  "concepts"
  "tools"
  "automation"
  "cli"
  "platforms"
  "nodes"
  "web"
  "install"
  "reference"
)

for cat in "${CATEGORIES[@]}"; do
  echo "📁 /$cat/"
done
