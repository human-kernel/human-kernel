<div align="center">

# Human Kernel

**Everything about you, structured into a kernel that you own.**

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

> **Everything about you, structured into a kernel that you own.**
> **From it grows your alter ego — your other side, flowing with you through the digital world, sometimes one step ahead.**
> **Made of you. Owned by you. Moving with you.**

Human Kernel is an open-source protocol and local-first application for modeling one person — identity, values, relationships, knowledge, experience, preferences, capabilities, and permission boundaries — so that agents you authorize can understand you and act as your counterpart.

Agents are getting better at acting. They are not getting better at knowing **who they act for**. Today, the knowledge of you lives in scattered chat histories and closed memory features owned by platforms. Human Kernel takes the opposite position: the model of you should be a first-class artifact — structured, inspectable, correctable — and it should belong to you.

## The shape of it

| Layer | What it is | What you control |
| --- | --- | --- |
| **The kernel** | A structured, evidence-backed model of one person. Every belief in it can answer: *why do you think this, where did it come from, is it still valid, can I correct it?* | Stored locally. Owned outright. |
| **The alter ego** | The expression layer that grows from the kernel: it answers, reasons, reminds, prepares, and acts as you — not a generic assistant with your data bolted on. | Acts only within permissions you grant. |
| **The Human API** | The permissioned surface through which other people, products, and agents can query or invoke a slice of you. | You decide which slices exist, who can call them, and what requires confirmation. |

## Principles

- **Local-first.** Your kernel's authority of record lives on your device, not on anyone's servers.
- **Evidence over vibes.** Claims about you trace back to sources. Beliefs carry confidence, can expire, can be contested, and can be corrected — and corrections propagate.
- **You are the editor.** "That's wrong", "that's outdated", "that's true but never use it" are first-class operations.
- **Conservative action.** Silence is a valid action. The alter ego asks before acting beyond its permissions, and nothing leaves your machine without an audit trail.
- **No soul claims.** The kernel never claims to know your "true self". It holds evidence-backed, correctable hypotheses about what you care about and how you decide.
- **Open protocol.** The schema, the protocol, and this app are open source, because asking for this much trust with a closed black box is not a reasonable ask.

## What this is not

- ❌ Not a project-management or task tool. Execution systems can plug in as backends; they are not the product.
- ❌ Not a notes app, memory database, or "second brain" viewer.
- ❌ Not an AI companion, and not a personality test. It does not score you, type you, or diagnose you.
- ❌ Not a cloud service holding your life. There is no server-side master copy.

## Roadmap

- [ ] **Protocol spec v0.1** — the kernel's structure: evidence, beliefs, corrections, permissions
- [ ] **Reference app** — local-first application implementing the spec
- [ ] **Human API draft** — permissioned querying of kernel slices
- [ ] **Agent runtime integration** — hand off authorized actions to execution backends

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
