# Human Kernel Overview

## Thesis

Human Kernel is an open-source protocol and local-first application for modeling one person so authorized agents can understand and act with that person's intent. The model should be structured, inspectable, correctable, and owned by the person, not trapped in platform-owned chat memory.

The short public promise is:

> Everything about you, structured into a kernel that you own.

## Four-Layer Model

The product is anchored on the kernel. Its enclosing context library stays private and evidence-rich; the inner model is expressed outward as an alter ego; the outer Human API exposes only authorized slices.

| Layer | Role | Boundary |
| --- | --- | --- |
| Context library | Private full-volume raw and curated context surrounding the kernel: notes, logs, transcripts, files. | Human-first and messy by design; it should not need to be agent-legible. |
| Kernel | Center of the model: structured, evidence-backed representation of one person. | Local authority of record; entries point back to evidence instead of embedding it. |
| Alter ego | Expression layer generalized outward from the kernel and its context: answers, reasons, reminds, prepares, and acts within grants. | Acts only inside explicit permissions. |
| Human API | Outer permissioned interface for other people, products, and agents to query or invoke a selected slice. | Per-slice, per-recipient, and per-purpose consent belongs to the owner. |

Read linearly, these layers still move from most private to most public; that ordering is a privacy view, not the product's primary shape.

## Principles

- Local-first: the authority of record lives on the owner's device.
- Evidence over vibes: claims trace to sources, carry status, and can be corrected.
- Pointers, not payloads: raw material stays in the context library; the kernel references it.
- Owner as editor: correction, invalidation, and "true but never use" are first-class operations.
- Conservative action: silence is valid; outward action requires permission and audit.
- No soul claims: the kernel holds evidence-backed hypotheses, not claims about a true self.
- Open protocol: schemas, protocol, and handling code stay open.

## Non-Goals

- Not a project-management or task tool; execution systems are optional backends.
- Not a notes app, memory database, or second-brain viewer.
- Not an AI companion, chatbot, personality test, or diagnostic tool.
- Not a cloud service holding a server-side master copy of someone's life.

## Source Pointers

- Public English manifesto and roadmap: `README.md`
- Public Chinese manifesto and roadmap: `README.zh-CN.md`
- Canonical terminology: `CONTEXT.md`
