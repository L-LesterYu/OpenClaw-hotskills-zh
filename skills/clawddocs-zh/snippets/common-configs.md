# Clawdbot 常用配置片段

## 提供商设置

### Discord
```json
{
  "discord": {
    "token": "${DISCORD_TOKEN}",
    "guilds": {
      "*": {
        "requireMention": false
      }
    }
  }
}
```

### Telegram
```json
{
  "telegram": {
    "token": "${TELEGRAM_TOKEN}"
  }
}
```

### WhatsApp
```json
{
  "whatsapp": {
    "sessionPath": "./whatsapp-sessions"
  }
}
```

## 网关配置
```json
{
  "gateway": {
    "host": "0.0.0.0",
    "port": 8080
  }
}
```

## 智能体默认值
```json
{
  "agents": {
    "defaults": {
      "model": "anthropic/claude-sonnet-4-5"
    }
  }
}
```

## 定时任务
```json
{
  "cron": [
    {
      "id": "daily-summary",
      "schedule": "0 9 * * *",
      "task": "summary"
    }
  ]
}
```
