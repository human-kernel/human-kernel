---
type: permission
status: self-asserted
privacy: P1
sources:
  - owner
expires: 2026-12-31
updated: 2026-06-12
---

# Grant: scheduling-agent

Ada's scheduling agent may read `identity/` and `commitments/` up to P2, propose entries in `commitments/`, and draft (never send) replies that touch scheduling. It may not read `relationships/` or anything P3+.
