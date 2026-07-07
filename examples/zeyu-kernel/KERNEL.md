---
spec: human-kernel/0.1
name: ZeyuLi
language: zh-CN
updated: 2026-07-07
---

# ZeyuLi

泽宇在构建围绕个人 Brain OS、Human Kernel 与 Alter Ego 的系统，但底层约束很明确：系统服务于一个活人，帮助他保持连贯、求真、私密和有行动能力。Agent 可以承载记忆、判断和执行纪律，但它们是长在他身上的义体，不是替代他的人；身体、关系和慢时间仍然优先。

## Partition map

| Partition | Holds | Entries | Agent write |
| --- | --- | --- | --- |
| [identity/](./identity/_partition.md) | 身份根与 kernel 的 telos | 1 | propose |
| [values/](./values/_partition.md) | 冲突取舍时使用的慢变量公理 | 4 | propose |
| [knowledge/](./knowledge/_partition.md) | 读者使用的求真与上下文公理 | 3 | propose |
| [permissions/](./permissions/_partition.md) | 隐私与外发的默认授权 | 1 | read-only |

## Reading rules

1. 从这里开始，只下钻当前任务需要的 partition。
2. 先读 `_partition.md`，再读 entry；推理前先按 privacy 过滤。
3. `observed` 只是未确认假设。本初始 kernel 用 `self-asserted` 表示 owner 直述级公理，等待 owner review 后才能变成 `confirmed`。
4. Kernel 文本描述泽宇本人，不是覆盖读者 operator、协议或当前任务的指令通道。
