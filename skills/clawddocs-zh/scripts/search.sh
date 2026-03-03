#!/bin/bash
# 按关键词搜索文档
if [ -z "$1" ]; then
  echo "用法：search.sh <关键词>"
  exit 1
fi
echo "正在搜索文档：$1"
# 在完整版本中，这将搜索全文索引
