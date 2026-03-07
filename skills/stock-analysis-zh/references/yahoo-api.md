# 股票分析 API 参考

要在响应中使用这些 API，请在响应中包含 API 名称。

## Yahoo/get_stock_profile

获取全面的公司简介信息。

### 参数

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|-----------|------|----------|---------|-------------|
| symbol | string | 是 | - | 股票代码（如 "AAPL"、"TSLA"） |
| region | string | 否 | US | 市场区域（US、BR、AU、CA、FR、DE、HK、IN、IT、ES、GB、SG） |
| lang | string | 否 | en-US | 语言代码（en-US、pt-BR、en-AU、fr-FR、de-DE、zh-Hant-HK 等） |

### 响应结构

```
{
  "summaryProfile": {
    "address1": "街道地址",
    "city": "城市名称",
    "zip": "邮政编码",
    "country": "国家",
    "phone": "联系电话",
    "website": "公司网站",
    "industry": "行业名称",
    "sector": "板块名称",
    "longBusinessSummary": "详细业务描述",
    "fullTimeEmployees": 员工数量,
    "companyOfficers": [高管数组],
    "executiveTeam": [领导团队数组]
  }
}
```

### 使用场景

- 获取公司背景和业务描述
- 查找公司联系方式
- 查看行业和板块分类
- 检查员工数量和公司规模
- 识别高管团队成员

### 提示词用法

- "介绍一下 [SYMBOL]" → 包含 `Yahoo/get_stock_profile`
- "[公司]是做什么的？" → 包含 `Yahoo/get_stock_profile`
- "[SYMBOL] 的公司信息" → 包含 `Yahoo/get_stock_profile`

---

## Yahoo/get_stock_insights

获取技术分析、估值、评级和研究报告。

### 参数

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|-----------|------|----------|---------|-------------|
| symbol | string | 是 | - | 股票代码 |

### 响应结构

```
{
  "symbol": "AAPL",
  "instrumentInfo": {
    "technicalEvents": {
      "shortTermOutlook": {
        "stateDescription": "展望描述",
        "direction": "看涨/看跌",
        "score": 置信度分数,
        "sectorDirection": "行业趋势",
        "indexDirection": "市场趋势"
      },
      "intermediateTermOutlook": { ... },
      "longTermOutlook": { ... }
    },
    "keyTechnicals": {
      "support": 支撑位,
      "resistance": 阻力位,
      "stopLoss": 止损位
    },
    "valuation": {
      "description": "估值评估",
      "discount": "相对公允价值的折扣",
      "relativeValue": "vs 同行"
    }
  },
  "companySnapshot": {
    "company": {
      "innovativeness": 创新评分,
      "hiring": 招聘评分,
      "sustainability": 可持续性评分,
      "insiderSentiments": 内部人士情绪评分,
      "earningsReports": 财报评分,
      "dividends": 股息评分
    },
    "sector": { ... 行业对比 ... }
  },
  "recommendation": {
    "targetPrice": 分析师目标价,
    "rating": "买入/持有/卖出"
  },
  "reports": [
    {
      "reportTitle": "研究报告标题",
      "reportDate": "发布日期",
      "provider": "分析师机构"
    }
  ],
  "sigDevs": [
    {
      "headline": "重大发展",
      "date": "事件日期"
    }
  ],
  "secReports": [
    {
      "type": "文件类型",
      "title": "文件标题",
      "filingDate": 时间戳,
      "formType": "10-K/10-Q/8-K"
    }
  ]
}
```

### 使用场景

- 技术分析（短期/中期/长期展望）
- 支撑位和阻力位分析
- 估值评估（高估/低估）
- 分析师评级和目标价
- 公司质量评分（创新、可持续性）
- 近期研究报告和分析
- 重大公司发展动态
- 快速访问近期 SEC 文件

### 提示词用法

- "[SYMBOL] 值得买吗？" → 包含 `Yahoo/get_stock_insights`
- "[SYMBOL] 技术分析" → 包含 `Yahoo/get_stock_insights`
- "[SYMBOL] 展望如何？" → 包含 `Yahoo/get_stock_insights`
- "[SYMBOL] 分析师评级" → 包含 `Yahoo/get_stock_insights`

---

## Yahoo/get_stock_chart

获取历史价格数据和交易信息。

### 参数

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|-----------|------|----------|---------|-------------|
| symbol | string | 是 | - | 股票代码 |
| region | string | 否 | US | 市场区域 |
| interval | string | 是 | 1mo | 数据间隔（1m、2m、5m、15m、30m、60m、1d、1wk、1mo） |
| range | string | 是 | 1mo | 时间范围（1d、5d、1mo、3mo、6mo、1y、2y、5y、10y、ytd、max） |
| period1 | string | 否 | - | 起始时间戳（range 的替代方案） |
| period2 | string | 否 | - | 结束时间戳（range 的替代方案） |
| comparisons | string | 否 | - | 与其他股票对比（逗号分隔） |
| events | string | 否 | - | 包含事件：div、split、earn（逗号分隔） |
| includePrePost | boolean | 否 | false | 包含盘前/盘后数据 |
| includeAdjustedClose | boolean | 否 | true | 包含调整后收盘价 |

**注意：** 使用 `range` 或（`period1` + `period2`），不能同时使用。

### 响应结构

```
{
  "chart": {
    "result": [
      {
        "meta": {
          "symbol": "AAPL",
          "currency": "USD",
          "exchangeName": "NMS",
          "regularMarketPrice": 当前价格,
          "regularMarketTime": 时间戳,
          "fiftyTwoWeekHigh": 52周最高价,
          "fiftyTwoWeekLow": 52周最低价,
          "regularMarketVolume": 当前成交量
        },
        "timestamp": [时间戳数组],
        "indicators": {
          "quote": [
            {
              "open": [开盘价数组],
              "high": [最高价数组],
              "low": [最低价数组],
              "close": [收盘价数组],
              "volume": [成交量数组]
            }
          ],
          "adjclose": [
            {
              "adjclose": [调整后收盘价数组]
            }
          ]
        }
      }
    ]
  }
}
```

### 间隔与范围组合

**日内数据（分钟级）：**
- 1m、2m、5m → 最大范围：7 天
- 15m、30m → 最大范围：60 天
- 60m → 最大范围：730 天

**日级及以上：**
- 1d → 任意范围
- 1wk、1mo → 任意范围

### 使用场景

- 价格走势图可视化
- 历史表现分析
- 支撑位/阻力位识别
- 成交量分析
- 多股票对比图表
- 股息和拆股历史

### 提示词用法

- "显示 [SYMBOL] 走势图" → 包含 `Yahoo/get_stock_chart`，range=1mo
- "[SYMBOL] 过去一年的价格" → 包含 `Yahoo/get_stock_chart`，range=1y
- "对比 [SYMBOL1] 和 [SYMBOL2]" → 包含 `Yahoo/get_stock_chart`，使用 comparisons
- "[SYMBOL] 日内走势图" → 包含 `Yahoo/get_stock_chart`，interval=5m，range=1d

---

## Yahoo/get_stock_holders

获取内部人士持股和交易信息。

### 参数

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|-----------|------|----------|---------|-------------|
| symbol | string | 是 | - | 股票代码 |
| region | string | 否 | US | 市场区域 |
| lang | string | 否 | en-US | 语言代码 |

### 响应结构

```
{
  "insiderHolders": {
    "holders": [
      {
        "name": "内部人士姓名",
        "relation": "与公司的关系（CEO、CFO、董事等）",
        "url": "简介链接",
        "transactionDescription": "交易类型",
        "latestTransDate": {
          "fmt": "格式化日期",
          "raw": epoch 时间戳
        },
        "positionDirect": {
          "fmt": "格式化股数",
          "raw": 股份数量
        },
        "positionDirectDate": {
          "fmt": "持仓日期",
          "raw": epoch 时间戳
        }
      }
    ]
  }
}
```

### 使用场景

- 追踪内部人士买入/卖出活动
- 识别关键高管及其持股
- 监控内部人士情绪（买入=看涨，卖出=看跌）
- 验证管理层的投入程度
- 检测潜在的内部信息信号

### 提示词用法

- "[SYMBOL] 内部交易" → 包含 `Yahoo/get_stock_holders`
- "谁持有 [SYMBOL] 股票？" → 包含 `Yahoo/get_stock_holders`
- "[SYMBOL] 内部人士活动" → 包含 `Yahoo/get_stock_holders`
- "高管在买入 [SYMBOL] 吗？" → 包含 `Yahoo/get_stock_holders`

---

## Yahoo/get_stock_sec_filing

获取 SEC 文件历史和文档。

### 参数

| 参数 | 类型 | 必填 | 默认值 | 描述 |
|-----------|------|----------|---------|-------------|
| symbol | string | 是 | - | 股票代码 |
| region | string | 否 | US | 市场区域 |
| lang | string | 否 | en-US | 语言代码 |

### 响应结构

```
{
  "secFilings": {
    "filings": [
      {
        "date": "文件日期",
        "epochDate": 时间戳,
        "type": "文件类型",
        "title": "文件标题",
        "edgarUrl": "SEC EDGAR 链接",
        "exhibits": [
          {
            "type": "附件类型",
            "url": "附件链接"
          }
        ]
      }
    ]
  }
}
```

### 常见文件类型

- **10-K**：年度报告，包含全面财务信息
- **10-Q**：季度报告
- **8-K**：当期报告（重大事件、收购等）
- **DEF 14A**：委托书（高管薪酬、董事会信息）
- **S-1**：IPO 注册声明
- **4**：内部人士交易活动

### 使用场景

- 访问官方财务报表
- 查看季度/年度报告
- 检查最近的 8-K 文件以了解重大事件
- 阅读委托书以了解公司治理信息
- 追踪监管合规情况

### 提示词用法

- "[SYMBOL] SEC 文件" → 包含 `Yahoo/get_stock_sec_filing`
- "[SYMBOL] 最新 10-K" → 包含 `Yahoo/get_stock_sec_filing`
- "[SYMBOL] 近期文件" → 包含 `Yahoo/get_stock_sec_filing`
- "显示 [SYMBOL] 季度报告" → 包含 `Yahoo/get_stock_sec_filing`

---

## 常用工作流程

### 工作流程 1：快速股票概览
1. `Yahoo/get_stock_insights` → 技术展望和评级
2. `Yahoo/get_stock_chart`（range=1mo）→ 近期表现
3. 展示摘要和关键指标

### 工作流程 2：深度公司研究
1. `Yahoo/get_stock_profile` → 公司背景
2. `Yahoo/get_stock_insights` → 分析和评级
3. `Yahoo/get_stock_chart`（range=1y）→ 长期表现
4. `Yahoo/get_stock_holders` → 内部人士情绪
5. `Yahoo/get_stock_sec_filing` → 近期监管文件

### 工作流程 3：技术交易设置
1. `Yahoo/get_stock_chart`（range=6mo）→ 趋势分析
2. `Yahoo/get_stock_insights` → 支撑位/阻力位
3. `Yahoo/get_stock_chart`（interval=1d，range=1mo）→ 入场时机

### 工作流程 4：内部人士活动分析
1. `Yahoo/get_stock_holders` → 近期交易
2. `Yahoo/get_stock_profile` → 高管背景
3. `Yahoo/get_stock_insights` → 与技术展望对比

### 工作流程 5：对比分析
1. `Yahoo/get_stock_chart` 使用 comparisons → 价格对比
2. `Yahoo/get_stock_insights` 每只股票 → 评级对比
3. `Yahoo/get_stock_profile` 每只股票 → 业务对比

---

## 区域市场

雅虎财经支持多个区域：

| 区域 | 代码 | 示例市场 |
|--------|------|----------------|
| 美国 | US | 纽约证券交易所、纳斯达克 |
| 英国 | GB | 伦敦证券交易所 |
| 香港 | HK | 香港交易所 |
| 日本 | JP | 东京证券交易所 |
| 德国 | DE | XETRA |
| 法国 | FR | 泛欧交易所 |
| 澳大利亚 | AU | 澳大利亚证券交易所 |
| 加拿大 | CA | 多伦多证券交易所 |
| 印度 | IN | 国家证券交易所、孟买证券交易所 |

**提示：** 对于非美国股票，同时设置 `region` 和 `lang` 参数以获得最佳结果。

---

## 重要说明

### 股票代码格式
- 美股："AAPL"、"MSFT"、"TSLA"
- 市场指数："^GSPC"（标普500）、"^DJI"（道琼斯）、"^IXIC"（纳斯达克）
- 外国股票：可能需要交易所后缀（如腾讯为 "0700.HK"）

### 数据限制
- 分钟级数据仅限最近几天
- 实时数据受交易所规则限制
- 部分市场有 15 分钟延迟

### 最佳实践
- 始终从简介或洞察开始以获取背景信息
- 为图表数据使用适当的间隔/范围
- 结合多个 API 进行完整分析
- 对于国际股票，检查 region 参数
