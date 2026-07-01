# 40 · Task Packets(可派工层)读法

> 本目录把设计转成**可派工的单元**。一个 packet 一个文件,锁死边界,worker 拿走即可开工、碰边界即知停。
> 完整模板见 skill 的 `references/task-packet-template.md`。

## 命名

`TP-<里程碑>-<序号>.md`,例:`TP-M1-01.md`。

## 一个 packet 必含(缺一不可派工)

| 字段 | 装什么 |
|---|---|
| `goal_alignment` | 本包如何推进里程碑目标,对应哪条验收标准 |
| `inputs` | 前置产物路径 |
| `reading_list` | worker 开工前必读的**具体文件**(不能只写目录或 README) |
| `outputs` | 交付物路径 + 格式 |
| `forbidden` | 本 worker 不得触碰的边界 |
| `gates` | entry(开工前条件)+ exit(完成判定,可检查) |
| `stop_condition` | 何时停下升级而非继续 |
| `review_route` | self / peer / arch review |

## 铁律

- **reading_list 必须具体到文件**;worker 发现不匹配,回 coordinator 补包,不自行考古扩大上下文。
- **worker 不可自行扩展 outputs**,超出要升级。
- **review_route 不可省略**,防自审自过。
- 依赖的决策未裁决(needs_decision),entry gate 不满足,packet 停 draft。
