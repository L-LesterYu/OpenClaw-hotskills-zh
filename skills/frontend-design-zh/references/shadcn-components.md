# shadcn/ui 组件参考

40+预装shadcn/ui组件的快速参考。

文档: https://ui.shadcn.com/docs/components

## 落地页最常用

| 组件 | 用途 | 示例 |
|-----------|----------|---------|
| `Button` | CTA、操作 | Hero按钮、表单提交 |
| `Badge` | 标签、状态 | "新"、"热门"、"测试中" |
| `Card` | 内容容器 | 功能卡片、价格层级 |
| `Accordion` | 可折叠内容 | FAQ部分 |
| `Dialog` | 模态框 | 视频播放器、注册表单 |
| `NavigationMenu` | 头部导航 | 带下拉的主导航 |
| `Tabs` | 标签页内容 | 功能展示 |
| `Carousel` | 滑动内容 | 推荐/评价、画廊 |

## 完整组件列表

### 布局与导航
- `Accordion` — 可折叠区块
- `Breadcrumb` — 导航路径
- `Carousel` — 滑动内容
- `Collapsible` — 展开/折叠
- `NavigationMenu` — 带下拉的头部导航
- `Pagination` — 分页导航
- `Resizable` — 可调整大小的面板
- `Scroll-Area` — 自定义滚动条
- `Separator` — 视觉分隔线
- `Sheet` — 滑出面板
- `Sidebar` — 应用侧边栏
- `Tabs` — 标签页内容

### 数据展示
- `Avatar` — 用户头像
- `Badge` — 标签和状态
- `Card` — 内容容器
- `HoverCard` — 悬停弹出
- `Table` — 数据表格

### 表单
- `Button` — 操作按钮
- `Checkbox` — 多选
- `Combobox` — 可搜索选择
- `DatePicker` — 日期选择
- `Form` — 带验证的表单包装器
- `Input` — 文本输入
- `InputOTP` — 一次性密码
- `Label` — 表单标签
- `RadioGroup` — 单选
- `Select` — 下拉选择
- `Slider` — 范围选择
- `Switch` — 开关
- `Textarea` — 多行输入
- `Toggle` — 切换按钮
- `ToggleGroup` — 按钮组

### 反馈
- `Alert` — 信息消息
- `AlertDialog` — 确认对话框
- `Dialog` — 模态窗口
- `Drawer` — 底部抽屉
- `Popover` — 弹出内容
- `Progress` — 加载进度条
- `Skeleton` — 加载占位符
- `Sonner` — Toast通知
- `Toast` — 通知提示
- `Tooltip` — 悬停提示

### 工具
- `AspectRatio` — 保持宽高比
- `Calendar` — 日期显示
- `Chart` — 数据可视化
- `Command` — 命令面板
- `ContextMenu` — 右键菜单
- `DropdownMenu` — 下拉菜单
- `Menubar` — 应用菜单栏

---

## 代码示例

### 带Badge和Button的Hero

```tsx
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"

function Hero() {
  return (
    <section className="py-24 text-center">
      <Badge variant="secondary" className="mb-4">
        现在测试中
      </Badge>
      
      <h1 className="text-5xl font-bold mb-6">
        在这里放你的标题
      </h1>
      
      <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
        副标题，更多产品详情。
      </p>
      
      <div className="flex gap-4 justify-center">
        <Button size="lg">开始使用</Button>
        <Button size="lg" variant="outline">了解更多</Button>
      </div>
    </section>
  )
}
```

### 功能卡片

```tsx
import { Card, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Zap, Shield, Globe } from "lucide-react"

const features = [
  { icon: Zap, title: "快速", description: "闪电般的性能" },
  { icon: Shield, title: "安全", description: "企业级安全" },
  { icon: Globe, title: "全球", description: "200+地点的CDN" },
]

function Features() {
  return (
    <section className="py-24">
      <div className="grid md:grid-cols-3 gap-8">
        {features.map((f) => (
          <Card key={f.title}>
            <CardHeader>
              <f.icon className="h-10 w-10 mb-4 text-primary" />
              <CardTitle>{f.title}</CardTitle>
              <CardDescription>{f.description}</CardDescription>
            </CardHeader>
          </Card>
        ))}
      </div>
    </section>
  )
}
```

### 价格表

```tsx
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Check } from "lucide-react"

const plans = [
  { name: "免费", price: 0, features: ["5个项目", "基础支持"] },
  { name: "专业", price: 19, features: ["无限项目", "优先支持", "API访问"], popular: true },
  { name: "团队", price: 49, features: ["专业版所有功能", "团队功能", "SSO"] },
]

function Pricing() {
  return (
    <section className="py-24">
      <div className="grid md:grid-cols-3 gap-8">
        {plans.map((plan) => (
          <Card key={plan.name} className={plan.popular ? "border-primary" : ""}>
            <CardHeader>
              {plan.popular && <Badge className="w-fit mb-2">最受欢迎</Badge>}
              <CardTitle>{plan.name}</CardTitle>
              <CardDescription>
                <span className="text-4xl font-bold">¥{plan.price}</span>
                <span className="text-muted-foreground">/月</span>
              </CardDescription>
            </CardHeader>
            <CardContent>
              <ul className="space-y-2">
                {plan.features.map((f) => (
                  <li key={f} className="flex items-center gap-2">
                    <Check className="h-4 w-4 text-primary" />
                    {f}
                  </li>
                ))}
              </ul>
            </CardContent>
            <CardFooter>
              <Button className="w-full" variant={plan.popular ? "default" : "outline"}>
                开始使用
              </Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </section>
  )
}
```

### FAQ手风琴

```tsx
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

const faqs = [
  { q: "如何运作？", a: "我们的平台使用AI来..." },
  { q: "有免费试用吗？", a: "是的，你有14天免费..." },
  { q: "可以随时取消吗？", a: "当然，无需问任何问题..." },
]

function FAQ() {
  return (
    <section className="py-24 max-w-3xl mx-auto">
      <h2 className="text-3xl font-bold text-center mb-12">
        常见问题
      </h2>
      
      <Accordion type="single" collapsible>
        {faqs.map((faq, i) => (
          <AccordionItem key={i} value={`item-${i}`}>
            <AccordionTrigger>{faq.q}</AccordionTrigger>
            <AccordionContent>{faq.a}</AccordionContent>
          </AccordionItem>
        ))}
      </Accordion>
    </section>
  )
}
```

### 带Sheet的移动端导航

```tsx
import { Button } from "@/components/ui/button"
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet"
import { Menu } from "lucide-react"

function MobileNav() {
  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button variant="ghost" size="icon" className="md:hidden">
          <Menu className="h-6 w-6" />
        </Button>
      </SheetTrigger>
      <SheetContent side="right">
        <nav className="flex flex-col gap-4 mt-8">
          <a href="#features">功能</a>
          <a href="#pricing">价格</a>
          <a href="#faq">FAQ</a>
          <Button className="mt-4">开始使用</Button>
        </nav>
      </SheetContent>
    </Sheet>
  )
}
```

### 带Dialog的视频模态框

```tsx
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import { Play } from "lucide-react"

function VideoModal() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline" size="lg">
          <Play className="mr-2 h-4 w-4" />
          观看演示
        </Button>
      </DialogTrigger>
      <DialogContent className="max-w-4xl p-0">
        <div className="aspect-video">
          <iframe
            src="https://www.youtube.com/embed/..."
            className="w-full h-full"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      </DialogContent>
    </Dialog>
  )
}
```

---

## 样式技巧

### 自定义颜色

shadcn使用CSS变量。在你的globals.css中覆盖：

```css
:root {
  --primary: 220 90% 56%;
  --primary-foreground: 0 0% 100%;
  --accent: 25 95% 53%;
}

.dark {
  --primary: 220 90% 66%;
}
```

### 扩展变体

```tsx
// components/ui/button.tsx
const buttonVariants = cva(
  "...",
  {
    variants: {
      variant: {
        default: "...",
        // 添加自定义变体
        gradient: "bg-gradient-to-r from-primary to-accent text-white hover:opacity-90",
      },
    },
  }
)
```

### 与Tailwind配合使用

所有组件接受 `className` 用于额外样式：

```tsx
<Button className="rounded-full px-8">
  药丸按钮
</Button>

<Card className="bg-gradient-to-br from-primary/10 to-accent/10">
  渐变卡片
</Card>
```
