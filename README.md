<div align="center">

# Human Kernel

**Your identity in the world of agents.**

<p>
  <a href="https://humankernel.org">Website</a> ·
  <a href="#the-shape-of-it">How it works</a> ·
  <a href="https://github.com/human-kernel/human-kernel/discussions">Discussions</a> ·
  <a href="#contributing">Contributing</a>
</p>

<p>
  <a href="./LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/github/license/human-kernel/human-kernel?color=blue"></a>
  <a href="https://github.com/human-kernel/human-kernel/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/human-kernel/human-kernel?style=flat&logo=github&color=yellow"></a>
  <a href="https://github.com/human-kernel/human-kernel/commits/main"><img alt="Commit activity" src="https://img.shields.io/github/commit-activity/m/human-kernel/human-kernel?color=green"></a>
  <a href="https://github.com/human-kernel/human-kernel/issues"><img alt="Issues" src="https://img.shields.io/github/issues/human-kernel/human-kernel"></a>
  <a href="https://github.com/human-kernel/human-kernel/discussions"><img alt="Discussions" src="https://img.shields.io/github/discussions/human-kernel/human-kernel?color=purple"></a>
  <img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen">
  <img alt="Status: early" src="https://img.shields.io/badge/status-early%20%26%20unstable-orange">
</p>

<p>
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README.zh-CN.md"><img alt="简体中文版 README" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
  <img alt="Your language" src="https://img.shields.io/badge/your%20language%20%E2%86%92%20PR-ffd9d9">
</p>

</div>

---

> **In the real world, an ID lets society recognize you.**
> **In the agent world, nothing does — until now.**
> **Human Kernel is your identity layer: structured, owned by you, readable by any agent you authorize.**

Agents are getting better at acting. They are not getting better at knowing **who they act for**. Today, the understanding of you lives in scattered chat histories and closed memory features owned by platforms — fragmented, non-portable, and opaque.

Human Kernel takes the opposite position: a structured, evidence-backed model of one person — identity, values, relationships, knowledge, experience, preferences, capabilities, and permission boundaries — owned outright by that person and readable by any authorized agent with zero prior context.

Think of it this way:
- **Without Human Kernel:** every agent starts from zero, guessing who you are.
- **With Human Kernel:** any agent understands you from the first second.

An ID card proves *that* you are someone. Human Kernel tells agents *what kind of person* you are, how you decide, and what you care about. It is the first human representation layer for the agent era.

## The shape of it

Human Kernel is centered on your kernel: the durable structure that remains readable, correctable, and owned by you. Its context library surrounds it; one or more alter egos express it outward through replaceable agent frameworks; and at the edge, the Human API exposes only the slices you authorize. The kernel is yours; the bodies it inhabits are rented.

Four concentric layers (read from most private to most public):

| Layer | What it is | What you control |
| --- | --- | --- |
| **The context library** | The kernel's enclosing private context — notes, logs, transcripts, files, years of it. Messy by design; it is never required to be agent-legible. | It never leaves home. The kernel only points into it. |
| **The kernel** | The center: a structured, evidence-backed model of one person. Your identity in the agent world: who you are, what you value, how you decide, who you know, what you can do. Every belief can answer: *why do you think this, where did it come from, is it still valid, can I correct it?* | Stored locally. Owned outright. Portable across any agent or platform. |
| **The alter ego** | An expression layer generalized outward from the kernel and its context: each alter ego can answer, reason, remind, prepare, and act as you through a replaceable agent framework — not as a generic assistant with your data bolted on. | Acts only within permissions you grant. One kernel can have more than one. |
| **The Human API** | The outer permissioned surface through which other people, products, and agents can query or invoke a slice of you. | You decide which slices exist, who can call them, and what requires confirmation. |

## Principles

- **Local-first.** Your kernel's authority of record lives on your device, not on anyone's servers.
- **Evidence over vibes.** Claims about you trace back to sources. Beliefs carry confidence, can expire, can be contested, and can be corrected — and corrections propagate.
- **Pointers, not payloads.** The kernel never embeds raw evidence — it references it. What travels is the distilled model; the material it came from stays in your context library.
- **You are the editor.** "That's wrong", "that's outdated", "that's true but never use it" are first-class operations.
- **Conservative action.** Silence is a valid action. The alter ego asks before acting beyond its permissions, and nothing leaves your machine without an audit trail.
- **No soul claims.** The kernel never claims to know your "true self". It holds evidence-backed, correctable hypotheses about what you care about and how you decide.
- **Portable and platform-agnostic.** Your kernel works with any agent, any runtime, any platform. It is not locked into one AI vendor’s ecosystem.
- **Open protocol.** The schema, the protocol, and this app are open source, because asking for this much trust with a closed black box is not a reasonable ask.

## What this is not

- ❌ Not a project-management or task tool. Execution systems can plug in as backends; they are not the product.
- ❌ Not a notes app, memory database, or "second brain" viewer.
- ❌ Not an AI companion, and not a personality test. It does not score you, type you, or diagnose you.
- ❌ Not a cloud service holding your life. There is no server-side master copy.
- ❌ Not another "AI memory" feature. Memory features are owned by platforms and locked in their ecosystems. Human Kernel is owned by you and works everywhere.

## Roadmap

**v0.1 — the kernel takes shape**

- [ ] **Protocol spec** — partitions, required fields, the bootstrap file, privacy tiers, the ledger → [draft](./spec/kernel-v0.1.md) · [example kernel](./examples/ada-lumen/KERNEL.md)
- [ ] **Validator** — structural checks and pointer integrity
- [ ] **Kernel inspector** — view, edit, and correct your kernel locally
- [ ] **MCP server** — any agent can read a kernel, zero context required

**v0.2 — the kernel meets others**

- [ ] **Human API draft** — per-recipient, per-purpose consent; query and invoke kernel slices
- [ ] **Interception layer** — every read and write passes through policy: sensitivity inheritance, consent enforcement, audit
- [ ] **Import adapters** — bring your memory from ChatGPT, Claude, Mem0, Obsidian, and others

**Later**

- [ ] **Execution handoff** — authorized actions delegated to agent runtimes
- [ ] **Portable packaging** — your whole kernel as a single file you can move anywhere

Followed and discussed in [Discussions](https://github.com/human-kernel/human-kernel/discussions). Early and unstable, developed in the open. Expect breaking changes; do not build on this yet.

## The manifesto in your language

The kernel is for everyone, so the manifesto should exist in every language.

| Language | Manifesto |
| --- | --- |
| English | above |
| 中文 | [README.zh-CN.md](./README.zh-CN.md) |
| *yours?* | *translating the three-line manifesto into your mother tongue is this project's smallest and most welcome first contribution — open a PR* |

## Contributing

The project is at the stage where the most valuable contributions are **sharp questions** and **manifesto translations**.

1. **Disagree with us** — open a [Discussion](https://github.com/human-kernel/human-kernel/discussions) about the protocol's direction
2. **Translate the manifesto** — add your language to the table above
3. **Watch the repo** — spec v0.1 will land here first

## Star History

<a href="https://star-history.com/#human-kernel/human-kernel&Date">
  <img src="https://api.star-history.com/svg?repos=human-kernel/human-kernel&type=Date" alt="Star History Chart" width="600">
</a>

## License

[AGPL-3.0](./LICENSE). Your kernel is yours; the code that handles it stays open — including when someone runs it as a service.
