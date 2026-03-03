#!/bin/bash
# 跟踪文档变更
case "$1" in
  snapshot)
    echo "正在保存当前状态..."
    ;;
  list)
    echo "正在显示快照..."
    ;;
  since)
    echo "自 $2 以来的变更..."
    ;;
  *)
    echo "用法：track-changes.sh {snapshot|list|since <日期>}"
    ;;
esac
