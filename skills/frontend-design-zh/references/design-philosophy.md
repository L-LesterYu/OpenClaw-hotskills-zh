# 设计哲学 —— 反AI套路宣言

本参考资料扩展核心 SKILL.md，提供创建独特设计的更深层指导。

## 问题：AI套路

通用AI生成的设计有这些明显特征：

### 排版罪过
- 到处是 Inter, Roboto, Arial
- 胆小的字重范围（仅400-600）
- 最小的字号递进（1.25x-1.5x）
- 无独特搭配策略

### 颜色罪行
- 白色上的紫色/蓝色渐变（头号大罪）
- 5种以上均匀分布的颜色，无层次
- 柔和、"安全"的调色板，不冒犯任何人，也不取悦任何人
- 灰色背景表示"我放弃了"

### 布局懒惰
- 所有东西居中
- 完美对称
- 可预测的卡片网格
- 无视觉张力或趣味

### 动效平庸
- 完全没有动画，或
- 每个元素上通用淡入
- 无协调或时机考虑

### 背景无聊
- 纯白色
- 纯浅灰色
- 如果感觉"大胆"，也许加个微妙渐变

---

## 解决方案：有意图的设计

### 投入一个极端

中间地带是设计死亡的地方。选择一个方向并推进：

**正确做法的繁复主义**:
- 密集、分层的构图
- 有清晰层次的重叠元素
- 丰富的纹理和图案
- 协调的多个动画
- 每个像素都在工作

**正确做法的极简主义**:
- 极度克制（最多3种颜色）
- 排版作为主角
- 负空间作为有意元素
- 单一、完美的动画
- 无多余之物

两者都需要勇气。两者都创造难忘的设计。

### 排版即身份

排版不是装饰——它是设计的声音。

**构建字体层次**:
```css
/* 展示：表明态度 */
.display {
  font-family: 'Clash Display', sans-serif;
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1;
}

/* 标题：支持展示 */
.heading {
  font-family: 'Satoshi', sans-serif;
  font-size: clamp(1.5rem, 3vw, 2.5rem);
  font-weight: 500;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

/* 正文：轻松阅读 */
.body {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.6;
}

/* 等宽：技术可信度 */
.mono {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.875rem;
  letter-spacing: 0;
}
```

**字体搭配策略**:

| 策略 | 展示 | 正文 | 效果 |
|----------|---------|------|------|
| 对比 | 衬线（Playfair） | 无衬线（Plus Jakarta） | 编辑优雅 |
| 和谐 | 几何（Satoshi） | 几何（General Sans） | 现代一致 |
| 张力 | 野兽派（Clash） | 人文（Source Sans） | 前卫但可读 |
| 技术 | 等宽（JetBrains） | 无衬线（IBM Plex Sans） | 开发者导向 |

### 颜色即情感

颜色不是关于"什么好看"——而是关于设计**感觉**如何。

**构建调色板**:

```css
/* 深色、自信、高端 */
:root {
  --bg-primary: #0a0a0a;
  --bg-secondary: #171717;
  --bg-tertiary: #262626;
  --text-primary: #fafafa;
  --text-secondary: #a3a3a3;
  --accent: #22c55e;  /* 自信绿 */
  --accent-subtle: rgba(34, 197, 94, 0.1);
}

/* 浅色、温暖、亲切 */
:root {
  --bg-primary: #fffbf5;
  --bg-secondary: #fff7ed;
  --bg-tertiary: #ffedd5;
  --text-primary: #1c1917;
  --text-secondary: #78716c;
  --accent: #ea580c;  /* 暖橙色 */
  --accent-subtle: rgba(234, 88, 12, 0.1);
}

/* 高对比、编辑 */
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f5f5f5;
  --text-primary: #000000;
  --text-secondary: #525252;
  --accent: #dc2626;  /* 大胆红 */
  --accent-subtle: rgba(220, 38, 38, 0.05);
}
```

**60-30-10法则**:
- 60% 主色（背景）
- 30% 次色（卡片、区块）
- 10% 强调色（CTA、高亮）

### 动效即叙事

动画讲述故事。你的故事是什么？

**页面加载协调**:
```css
/* Hero元素依次入场 */
.hero-badge {
  animation: fadeSlideUp 0.6s ease-out 0.1s both;
}
.hero-title {
  animation: fadeSlideUp 0.6s ease-out 0.2s both;
}
.hero-subtitle {
  animation: fadeSlideUp 0.6s ease-out 0.3s both;
}
.hero-cta {
  animation: fadeSlideUp 0.6s ease-out 0.4s both;
}

@keyframes fadeSlideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**滚动触发揭示**:
```javascript
// 滚动动画的交叉观察器
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate-in');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

**令人惊喜的悬停状态**:
```css
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.05);
}

/* 或更戏剧性 */
.card:hover {
  transform: scale(1.02) rotate(-0.5deg);
}
```

### 背景即氛围

背景在任何内容被阅读之前就设定了情绪。

**渐变网格**:
```css
.gradient-mesh {
  background: 
    radial-gradient(at 40% 20%, hsla(28, 100%, 74%, 0.3) 0px, transparent 50%),
    radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.2) 0px, transparent 50%),
    radial-gradient(at 0% 50%, hsla(355, 100%, 93%, 0.3) 0px, transparent 50%),
    radial-gradient(at 80% 50%, hsla(340, 100%, 76%, 0.2) 0px, transparent 50%),
    radial-gradient(at 0% 100%, hsla(269, 100%, 77%, 0.3) 0px, transparent 50%);
}
```

**噪点纹理**:
```css
.noise::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  opacity: 0.03;
  pointer-events: none;
  z-index: 1000;
}
```

**点阵图案**:
```css
.dots {
  background-image: radial-gradient(circle, #333 1px, transparent 1px);
  background-size: 20px 20px;
}
```

**玻璃态**:
```css
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
```

---

## 设计决策框架

当卡住时，问这些问题：

1. **一件事是什么？** — 如果用户记住一个元素，是什么？
2. **我会截屏吗？** — 有值得分享的时刻吗？
3. **感觉像是设计过的吗？** — 还是感觉像是生成的？
4. **情感是什么？** — 自信？俏皮？严肃？奢华？
5. **够勇敢吗？** — 我是在安全行事还是投入一个方向？

---

## 反模式检测

发布前，扫描这些：

| 反模式 | 修复 |
|--------------|-----|
| Inter字体 | 替换为独特替代品 |
| 紫色渐变 | 选择符合语境的调色板 |
| 全部居中 | 添加不对称或左对齐 |
| 无动画 | 添加协调的页面加载 |
| 纯色背景 | 添加纹理、渐变或图案 |
| 均匀分布的颜色 | 应用60-30-10法则 |
| 通用卡片 | 添加独特样式处理 |
| 默认阴影 | 使用分层、有氛围的阴影 |

---

*记住：Claude能够做出非凡的创意工作。不要犹豫。*
