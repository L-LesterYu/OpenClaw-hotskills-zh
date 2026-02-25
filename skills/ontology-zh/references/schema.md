# Ontology 模式参考

本体图谱的完整类型定义和约束模式。

## 核心类型

### 智能体与人员

```yaml
Person:
  required: [name]
  properties:
    name: string
    email: string?
    phone: string?
    organization: ref(Organization)?
    notes: string?
    tags: string[]?

Organization:
  required: [name]
  properties:
    name: string
    type: enum(company, team, community, government, other)?
    website: url?
    members: ref(Person)[]?
```

### 工作管理

```yaml
Project:
  required: [name]
  properties:
    name: string
    description: string?
    status: enum(planning, active, paused, completed, archived)
    owner: ref(Person)?
    team: ref(Person)[]?
    goals: ref(Goal)[]?
    start_date: date?
    end_date: date?
    tags: string[]?

Task:
  required: [title, status]
  properties:
    title: string
    description: string?
    status: enum(open, in_progress, blocked, done, cancelled)
    priority: enum(low, medium, high, urgent)?
    assignee: ref(Person)?
    project: ref(Project)?
    due: datetime?
    estimate_hours: number?
    blockers: ref(Task)[]?
    tags: string[]?

Goal:
  required: [description]
  properties:
    description: string
    target_date: date?
    status: enum(active, achieved, abandoned)?
    metrics: object[]?
    key_results: string[]?
```

### 时间与地点

```yaml
Event:
  required: [title, start]
  properties:
    title: string
    description: string?
    start: datetime
    end: datetime?
    location: ref(Location)?
    attendees: ref(Person)[]?
    recurrence: object?  # iCal RRULE 格式
    status: enum(confirmed, tentative, cancelled)?
    reminders: object[]?

Location:
  required: [name]
  properties:
    name: string
    address: string?
    city: string?
    country: string?
    coordinates: object?  # {lat, lng}
    timezone: string?
```

### 信息

```yaml
Document:
  required: [title]
  properties:
    title: string
    path: string?  # 本地文件路径
    url: url?      # 远程URL
    mime_type: string?
    summary: string?
    content_hash: string?
    tags: string[]?

Message:
  required: [content, sender]
  properties:
    content: string
    sender: ref(Person)
    recipients: ref(Person)[]
    thread: ref(Thread)?
    timestamp: datetime
    platform: string?  # email, slack, whatsapp, etc.
    external_id: string?

Thread:
  required: [subject]
  properties:
    subject: string
    participants: ref(Person)[]
    messages: ref(Message)[]
    status: enum(active, archived)?
    last_activity: datetime?

Note:
  required: [content]
  properties:
    content: string
    title: string?
    tags: string[]?
    refs: ref(Entity)[]?  # 链接到任何实体
    created: datetime
```

### 资源

```yaml
Account:
  required: [service, username]
  properties:
    service: string  # github, gmail, aws, etc.
    username: string
    url: url?
    credential_ref: ref(Credential)?

Device:
  required: [name, type]
  properties:
    name: string
    type: enum(computer, phone, tablet, server, iot, other)
    os: string?
    identifiers: object?  # {mac, serial, etc.}
    owner: ref(Person)?

Credential:
  required: [service, secret_ref]
  forbidden_properties: [password, secret, token, key, api_key]
  properties:
    service: string
    secret_ref: string  # 引用机密存储（例如 "keychain:github-token"）
    expires: datetime?
    scope: string[]?
```

### 元数据

```yaml
Action:
  required: [type, target, timestamp]
  properties:
    type: string  # create, update, delete, send, etc.
    target: ref(Entity)
    timestamp: datetime
    actor: ref(Person|Agent)?
    outcome: enum(success, failure, pending)?
    details: object?

Policy:
  required: [scope, rule]
  properties:
    scope: string  # 此策略适用的范围
    rule: string   # 自然语言或代码形式的约束
    enforcement: enum(block, warn, log)
    enabled: boolean
```

## 关系类型

### 所有权与分配

```yaml
owns:
  from_types: [Person, Organization]
  to_types: [Account, Device, Document, Project]
  cardinality: one_to_many

has_owner:
  from_types: [Project, Task, Document]
  to_types: [Person]
  cardinality: many_to_one

assigned_to:
  from_types: [Task]
  to_types: [Person]
  cardinality: many_to_one
```

### 层级与包含

```yaml
has_task:
  from_types: [Project]
  to_types: [Task]
  cardinality: one_to_many

has_goal:
  from_types: [Project]
  to_types: [Goal]
  cardinality: one_to_many

member_of:
  from_types: [Person]
  to_types: [Organization]
  cardinality: many_to_many

part_of:
  from_types: [Task, Document, Event]
  to_types: [Project]
  cardinality: many_to_one
```

### 依赖关系

```yaml
blocks:
  from_types: [Task]
  to_types: [Task]
  acyclic: true  # 防止循环依赖
  cardinality: many_to_many

depends_on:
  from_types: [Task, Project]
  to_types: [Task, Project, Event]
  acyclic: true
  cardinality: many_to_many

requires:
  from_types: [Action]
  to_types: [Credential, Policy]
  cardinality: many_to_many
```

### 引用

```yaml
mentions:
  from_types: [Document, Message, Note]
  to_types: [Person, Project, Task, Event]
  cardinality: many_to_many

references:
  from_types: [Document, Note]
  to_types: [Document, Note]
  cardinality: many_to_many

follows_up:
  from_types: [Task, Event]
  to_types: [Event, Message]
  cardinality: many_to_one
```

### 事件

```yaml
attendee_of:
  from_types: [Person]
  to_types: [Event]
  cardinality: many_to_many
  properties:
    status: enum(accepted, declined, tentative, pending)

located_at:
  from_types: [Event, Person, Device]
  to_types: [Location]
  cardinality: many_to_one
```

## 全局约束

```yaml
constraints:
  # 凭证绝不能直接存储机密
  - type: Credential
    rule: "forbidden_properties: [password, secret, token]"
    message: "凭证必须使用 secret_ref 引用外部机密存储"

  # 任务必须有有效的状态转换
  - type: Task
    rule: "status transitions: open -> in_progress -> (done|blocked) -> done"
    enforcement: warn

  # 事件必须有 end >= start
  - type: Event
    rule: "if end exists: end >= start"
    message: "事件结束时间必须在开始时间之后"

  # 无孤立任务（应属于项目或有明确的所有者）
  - type: Task
    rule: "has_relation(part_of, Project) OR has_property(owner)"
    enforcement: warn
    message: "任务应属于项目或有明确的所有者"

  # 循环依赖预防
  - relation: blocks
    rule: "acyclic"
    message: "不允许循环任务依赖"
```
