#!/bin/bash
# 获取特定文档
if [ -z "$1" ]; then
  echo "用法：fetch-doc.sh <路径>"
  exit 1
fi
echo "正在获取：https://docs.clawd.bot/$1"
