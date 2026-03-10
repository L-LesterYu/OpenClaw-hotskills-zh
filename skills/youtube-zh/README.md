# YouTube 📹

[Clawdbot](https://clawdbot.com) 的 YouTube 研究和转录技能。

## 功能特性

- 📹 **视频详情** - 获取标题、描述、统计数据、发布日期
- 📝 **字幕** - 提取带时间戳的字幕
- 📺 **频道信息** - 获取频道详情和最近视频
- 🔍 **搜索** - 按关键词查找视频
- 🎬 **播放列表信息** - 获取播放列表详情

## 安装

```bash
clawdhub install youtube-zh
```

## 配置

从 [Google Cloud Console](https://console.cloud.google.com) 获取 YouTube API 密钥：
1. 创建项目
2. 启用 YouTube Data API v3
3. 创建凭证 → API 密钥

```bash
export YOUTUBE_API_KEY="your-api-key"
```

或添加到 `~/.clawdbot/clawdbot.json`：
```json
{
  "skills": {
    "entries": {
      "youtube": {
        "apiKey": "AIzaSy..."
      }
    }
  }
}
```

## 使用示例

```
"查找最新的 Lex Fridman 播客剧集"
"获取此视频的字幕：https://youtube.com/watch?v=Z-FRe5AKmCU"
"在 YouTube 上搜索 Laravel 教程"
"显示频道 UCSHZKyawb77ixDdsGog4iWA 的最近视频"
"获取视频 Z-FRe5AKmCU 的详情"
```

## 致谢

此技能使用 Zubeid Hendricks 的 [youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) 进行 YouTube Data API 集成。

## 许可证

MIT
