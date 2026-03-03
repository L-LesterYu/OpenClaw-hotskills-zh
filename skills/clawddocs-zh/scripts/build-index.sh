#!/bin/bash
# 全文索引管理（需要 qmd）
case "$1" in
  fetch)
    echo "正在下载所有文档..."
    ;;
  build)
    echo "正在构建搜索索引..."
    ;;
  search)
    shift
    echo "语义搜索：$*"
    ;;
  *)
    echo "用法：build-index.sh {fetch|build|search <查询>}"
    ;;
esac
