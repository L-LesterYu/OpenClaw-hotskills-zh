# 移动优先模式

从实际实现失败中学到的全面响应式CSS模式。

## Hero区块

### 问题
当一列在移动端隐藏时，2列网格布局会留下空白空间。

### 解决方案
在移动端从 `display: grid` 切换为 `display: flex`。

```css
/* 桌面：2列网格 */
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
  padding: 80px 0;
}

/* 移动端：居中flex */
@media (max-width: 768px) {
  .hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 40px 20px;
    gap: 24px;
  }

  .hero-content {
    align-items: center;
  }

  .hero-badge {
    align-self: center;
  }

  .hero-title {
    font-size: 32px;
    text-align: center;
  }

  .hero-subtitle {
    font-size: 14px;
    text-align: center;
  }

  .hero-cta {
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .hero-cta .btn {
    width: 100%;
    max-width: 280px;
  }

  .hero-visual {
    display: none;
  }
}
```

**关键规则**: Grid为隐藏列保留空间。Flex不会。

---

## 大型选择列表

### 问题
在移动端为20+项目使用水平滚动不可用——文字会被截断。

### 解决方案
带分类标题的可折叠手风琴。

```tsx
function MobileSelector({ categories }) {
  const [expanded, setExpanded] = useState<string | null>(null);

  return (
    <div className="selector">
      {categories.map(cat => (
        <div 
          key={cat.name} 
          className={cn("category", expanded === cat.name && "expanded")}
        >
          <button
            className="category-header"
            onClick={() => setExpanded(
              expanded === cat.name ? null : cat.name
            )}
          >
            <span>{cat.name}</span>
            <ChevronDown className={cn(
              "transition-transform",
              expanded === cat.name && "rotate-180"
            )} />
          </button>
          
          <div className="category-items">
            {cat.items.map(item => (
              <button key={item.id} className="item">
                {item.name}
              </button>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
```

```css
.category-items {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

@media (max-width: 768px) {
  .category-items {
    display: none;
  }

  .category.expanded .category-items {
    display: flex;
    flex-direction: column;
    padding: 12px;
    background: var(--bg-secondary);
    border-radius: 8px;
  }
}
```

---

## 表单布局

### 问题
多列表单布局在移动端会被截断。

### 解决方案
全宽垂直堆叠。

```css
.form-row {
  display: flex;
  gap: 16px;
}

.form-group {
  flex: 1;
}

@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
  }

  .form-group {
    width: 100%;
  }
  
  .form-row.half-width {
    /* 即使是"半宽"字段在移动端也全宽 */
    flex-direction: column;
  }
}
```

---

## 状态/警告卡片

### 问题
垂直堆叠水平元素时文字对齐不一致。

### 解决方案
同时使用 `align-items: center` 和 `text-align: center`。

```css
.alert {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 16px;
  border-radius: 8px;
}

.alert-icon {
  flex-shrink: 0;
}

.alert-content {
  flex: 1;
}

@media (max-width: 768px) {
  .alert {
    flex-direction: column;
    align-items: center;  /* 居中flex项目 */
    text-align: center;   /* 居中项目内文字 */
    gap: 8px;
  }

  .alert-content {
    text-align: center;  /* 为嵌套元素明确设置 */
  }

  .alert strong {
    text-align: center;  /* 块元素需要明确设置 */
  }
}
```

**关键规则**: 堆叠的flex项目需要同时设置 `align-items: center` 和 `text-align: center`。

---

## 网格布局

### 通用移动端折叠

```css
.pricing-grid,
.feature-grid,
.team-grid,
.stats-grid,
.testimonial-grid {
  display: grid;
  gap: 24px;
}

/* 桌面配置 */
.pricing-grid { grid-template-columns: repeat(3, 1fr); }
.feature-grid { grid-template-columns: repeat(3, 1fr); }
.team-grid { grid-template-columns: repeat(4, 1fr); }
.stats-grid { grid-template-columns: repeat(4, 1fr); }
.testimonial-grid { grid-template-columns: repeat(2, 1fr); }

/* 平板 */
@media (max-width: 1024px) {
  .team-grid { grid-template-columns: repeat(2, 1fr); }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}

/* 移动端：所有都是单列 */
@media (max-width: 768px) {
  .pricing-grid,
  .feature-grid,
  .team-grid,
  .stats-grid,
  .testimonial-grid {
    grid-template-columns: 1fr;
  }
}
```

---

## 导航

### 移动端菜单模式

```tsx
function MobileNav() {
  const [open, setOpen] = useState(false);

  return (
    <>
      {/* 移动端菜单按钮 */}
      <button 
        className="md:hidden"
        onClick={() => setOpen(!open)}
      >
        {open ? <X /> : <Menu />}
      </button>

      {/* 移动端菜单遮罩 */}
      <div className={cn(
        "fixed inset-0 bg-black/50 md:hidden transition-opacity",
        open ? "opacity-100" : "opacity-0 pointer-events-none"
      )} onClick={() => setOpen(false)} />

      {/* 移动端菜单面板 */}
      <nav className={cn(
        "fixed top-0 right-0 h-full w-64 bg-background p-6",
        "transform transition-transform md:hidden",
        open ? "translate-x-0" : "translate-x-full"
      )}>
        {/* 导航项 */}
      </nav>
    </>
  );
}
```

---

## 表单元素一致性

### 始终作为一组样式

```css
/* 错误 - 只针对input */
.input {
  border: 2px solid var(--border);
  border-radius: 8px;
}

/* 正确 - 所有表单字段 */
.input,
.select,
.textarea {
  border: 2px solid var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  font-size: 16px; /* 防止iOS缩放 */
  background: var(--bg-secondary);
  color: var(--text-primary);
}
```

### Textarea边框圆角例外

药丸形输入框在textarea上看起来不对：

```css
.input,
.select {
  border-radius: 100px; /* 药丸形 */
}

.textarea {
  border-radius: 16px; /* 更柔和，但不是药丸形 */
}
```

### 下拉选项样式

`<option>` 元素无法继承backdrop-filter：

```css
.select {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  color: white;
}

/* 选项需要实心背景 */
.select option {
  background: #1a1a2e;
  color: white;
}
```

### 防止iOS聚焦缩放

iOS在font-size < 16px的输入框上会缩放：

```css
input, select, textarea {
  font-size: 16px; /* 防止缩放的最小值 */
}

/* 或使用transform技巧 */
@media (max-width: 768px) {
  input, select, textarea {
    font-size: 16px;
  }
}
```

---

## 颜色对比检查清单

### 徽章/药丸元素

```css
/* 错误 - 可能不可见 */
.badge {
  background: var(--accent);
  color: white; /* 可能无对比 */
}

/* 正确 - 确保对比 */
.badge {
  background: var(--accent);
  color: var(--accent-foreground); /* 定义为对比色 */
}
```

### 颜色色块

显示颜色的色块需要可见边框：

```css
.color-swatch {
  border: 2px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.3);
}
```

### 深色主题表单标签

```css
/* 错误 - 硬编码 */
.label {
  color: white;
}

/* 正确 - 语义变量 */
.label {
  color: var(--text-primary);
}
```

---

## 断点参考

```css
/* 大桌面 */
@media (min-width: 1440px) {
  .container { max-width: 1280px; }
}

/* 桌面 */
@media (max-width: 1200px) {
  /* 堆叠侧边栏，保持内容宽度 */
}

/* 平板 */
@media (max-width: 1024px) {
  /* 减少网格列 */
}

/* 移动端 */
@media (max-width: 768px) {
  /* 完全单列，居中内容 */
}

/* 小屏移动端 */
@media (max-width: 480px) {
  /* 紧凑间距，缩小字体 */
}
```

---

## 移动端字体缩放

```css
/* 基础（桌面） */
.display { font-size: 64px; }
.h1 { font-size: 48px; }
.h2 { font-size: 36px; }
.h3 { font-size: 24px; }
.body { font-size: 16px; }
.small { font-size: 14px; }

/* 移动端 */
@media (max-width: 768px) {
  .display { font-size: 40px; }
  .h1 { font-size: 32px; }
  .h2 { font-size: 24px; }
  .h3 { font-size: 20px; }
  .body { font-size: 16px; } /* 保持可读 */
  .small { font-size: 13px; }
}
```

---

## 触摸目标尺寸

触摸目标最小44x44px（Apple HIG）：

```css
.btn,
.nav-link,
.icon-btn {
  min-height: 44px;
  min-width: 44px;
}

@media (max-width: 768px) {
  .btn {
    padding: 14px 24px; /* 更大的触摸区域 */
  }
}
```

---

## 实施前检查清单

在最终确定任何移动端设计之前：

- [ ] Hero在移动端居中（非左对齐留空）
- [ ] 所有表单字段（input、select、textarea）样式一致
- [ ] Radio/checkbox可见（尤其是透明边框样式）
- [ ] 下拉选项有可读背景
- [ ] 标签使用语义颜色变量
- [ ] 状态/警告卡片正确居中
- [ ] 大型选择列表使用手风琴（非水平滚动）
- [ ] 网格布局折叠为单列
- [ ] 徽章/药丸文字与背景对比
- [ ] 颜色色块有可见边框
- [ ] 触摸目标最小44x44px
- [ ] 字体大小16px+以防止iOS缩放
- [ ] 导航有移动端菜单模式
