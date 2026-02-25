# 查询参考

查询模式和图遍历示例。

## 基本查询

### 通过ID获取

```bash
python3 scripts/ontology.py get --id task_001
```

### 按类型列出

```bash
# 所有任务
python3 scripts/ontology.py list --type Task

# 所有人员
python3 scripts/ontology.py list --type Person
```

### 按属性过滤

```bash
# 开放任务
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'

# 高优先级任务
python3 scripts/ontology.py query --type Task --where '{"priority":"high"}'

# 分配给特定人员的任务（按属性）
python3 scripts/ontology.py query --type Task --where '{"assignee":"p_001"}'
```

## 关系查询

### 获取相关实体

```bash
# 属于项目的任务（出向）
python3 scripts/ontology.py related --id proj_001 --rel has_task

# 此任务属于什么项目（入向）
python3 scripts/ontology.py related --id task_001 --rel part_of --dir incoming

# 实体的所有关系（双向）
python3 scripts/ontology.py related --id p_001 --dir both
```

### 常见模式

```bash
# 谁拥有这个项目？
python3 scripts/ontology.py related --id proj_001 --rel has_owner

# 这个人参加什么活动？
python3 scripts/ontology.py related --id p_001 --rel attendee_of --dir outgoing

# 什么在阻塞这个任务？
python3 scripts/ontology.py related --id task_001 --rel blocked_by --dir incoming
```

## 编程式查询

### Python API

```python
from scripts.ontology import load_graph, query_entities, get_related

# 加载图谱
entities, relations = load_graph("memory/ontology/graph.jsonl")

# 查询实体
open_tasks = query_entities("Task", {"status": "open"}, "memory/ontology/graph.jsonl")

# 获取相关实体
project_tasks = get_related("proj_001", "has_task", "memory/ontology/graph.jsonl")
```

### 复杂查询

```python
# 查找所有被未完成依赖项阻塞的任务
def find_blocked_tasks(graph_path):
    entities, relations = load_graph(graph_path)
    blocked = []
    
    for entity in entities.values():
        if entity["type"] != "Task":
            continue
        if entity["properties"].get("status") == "blocked":
            # 查找什么在阻塞它
            blockers = get_related(entity["id"], "blocked_by", graph_path, "incoming")
            incomplete_blockers = [
                b for b in blockers 
                if b["entity"]["properties"].get("status") != "done"
            ]
            if incomplete_blockers:
                blocked.append({
                    "task": entity,
                    "blockers": incomplete_blockers
                })
    
    return blocked
```

### 路径查询

```python
# 查找两个实体之间的路径
def find_path(from_id, to_id, graph_path, max_depth=5):
    entities, relations = load_graph(graph_path)
    
    visited = set()
    queue = [(from_id, [])]
    
    while queue:
        current, path = queue.pop(0)
        
        if current == to_id:
            return path
        
        if current in visited or len(path) >= max_depth:
            continue
        
        visited.add(current)
        
        for rel in relations:
            if rel["from"] == current and rel["to"] not in visited:
                queue.append((rel["to"], path + [rel]))
            if rel["to"] == current and rel["from"] not in visited:
                queue.append((rel["from"], path + [{**rel, "direction": "incoming"}]))
    
    return None  # 未找到路径
```

## 按用例分类的查询模式

### 任务管理

```bash
# 我的所有开放任务
python3 scripts/ontology.py query --type Task --where '{"status":"open","assignee":"p_me"}'

# 逾期任务（需要自定义脚本进行日期比较）
# 有关日期处理，请参阅 references/schema.md

# 无阻塞的任务
python3 scripts/ontology.py query --type Task --where '{"status":"open"}'
# 然后在代码中过滤没有入向 "blocks" 关系的任务
```

### 项目概览

```bash
# 项目中的所有任务
python3 scripts/ontology.py related --id proj_001 --rel has_task

# 项目团队成员
python3 scripts/ontology.py related --id proj_001 --rel has_member

# 项目目标
python3 scripts/ontology.py related --id proj_001 --rel has_goal
```

### 人员与联系人

```bash
# 所有人员
python3 scripts/ontology.py list --type Person

# 组织中的人员
python3 scripts/ontology.py related --id org_001 --rel has_member

# 分配给此人的内容
python3 scripts/ontology.py related --id p_001 --rel assigned_to --dir incoming
```

### 事件与日历

```bash
# 所有事件
python3 scripts/ontology.py list --type Event

# 某地点的事件
python3 scripts/ontology.py related --id loc_001 --rel located_at --dir incoming

# 事件参与者
python3 scripts/ontology.py related --id event_001 --rel attendee_of --dir incoming
```

## 聚合

对于复杂聚合，使用Python:

```python
from collections import Counter

def task_status_summary(project_id, graph_path):
    """按状态统计项目任务"""
    tasks = get_related(project_id, "has_task", graph_path)
    statuses = Counter(t["entity"]["properties"].get("status", "unknown") for t in tasks)
    return dict(statuses)

def workload_by_person(graph_path):
    """统计每人的开放任务数"""
    open_tasks = query_entities("Task", {"status": "open"}, graph_path)
    workload = Counter(t["properties"].get("assignee") for t in open_tasks)
    return dict(workload)
```
