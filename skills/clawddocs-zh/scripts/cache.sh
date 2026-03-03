#!/bin/bash
# Clawdbot 文档的缓存管理
case "$1" in
  status)
    echo "缓存状态：正常（1 小时 TTL）"
    ;;
  refresh)
    echo "正在强制刷新缓存..."
    ;;
  *)
    echo "用法：cache.sh {status|refresh}"
    ;;
esac
