# Human Kernel

> **Everything about you, structured into a kernel that you own.**
> **From it grows your alter ego — your other side, flowing with you through the digital world, sometimes one step ahead.**
> **Made of you. Owned by you. Moving with you.**

[中文 README](./README.zh-CN.md)

Human Kernel is an open-source protocol and local-first application for modeling one person — identity, values, relationships, knowledge, experience, preferences, capabilities, and permission boundaries — so that agents you authorize can understand you and act as your counterpart.

Agents are getting better at acting. They are not getting better at knowing **who they act for**. Today, the knowledge of you lives in scattered chat histories and closed memory features owned by platforms. Human Kernel takes the opposite position: the model of you should be a first-class artifact — structured, inspectable, correctable — and it should belong to you.

## The shape of it

1. **The kernel** — a structured, evidence-backed model of one person. Every belief in it can answer: *why do you think this, where did it come from, is it still valid, can I correct it?* Stored locally. Owned outright.
2. **The alter ego** — the expression layer that grows from the kernel: it answers, reasons, reminds, prepares, and acts as you, within permissions you grant. Not a generic assistant with your data bolted on — a counterpart grounded in your kernel.
3. **The Human API** — the permissioned surface through which other people, products, and agents can query or invoke a slice of you. You decide which slices exist, who can call them, and what requires confirmation.

## Principles

- **Local-first.** Your kernel's authority of record lives on your device, not on anyone's servers.
- **Evidence over vibes.** Claims about you trace back to sources. Beliefs carry confidence, can expire, can be contested, and can be corrected — and corrections propagate.
- **You are the editor.** "That's wrong", "that's outdated", "that's true but never use it" are first-class operations.
- **Conservative action.** Silence is a valid action. The alter ego asks before acting beyond its permissions, and nothing leaves your machine without an audit trail.
- **No soul claims.** The kernel never claims to know your "true self". It holds evidence-backed, correctable hypotheses about what you care about and how you decide.
- **Open protocol.** The schema, the protocol, and this app are open source, because asking for this much trust with a closed black box is not a reasonable ask.

## What this is not

- Not a project-management or task tool. Execution systems can plug in as backends; they are not the product.
- Not a notes app, memory database, or "second brain" viewer.
- Not an AI companion, and not a personality test. It does not score you, type you, or diagnose you.
- Not a cloud service holding your life. There is no server-side master copy.

## Status

Early and unstable, developed in the open. The protocol spec (v0.1) and the reference app are being built in parallel in this repository. Expect breaking changes; do not build on this yet.

## The manifesto in your language

The kernel is for everyone, so the manifesto should exist in every language.

- **English** — above
- **中文** — [README.zh-CN.md](./README.zh-CN.md)

If yours is missing: translating the three-line manifesto into your mother tongue is this project's smallest and most welcome first contribution. Open a PR.

## License

[AGPL-3.0](./LICENSE). Your kernel is yours; the code that handles it stays open — including when someone runs it as a service.
