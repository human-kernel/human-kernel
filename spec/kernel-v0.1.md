# Human Kernel — Protocol Spec v0.1 (draft)

Status: **draft, unstable**. Everything here may change before v0.1 is tagged.
The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as in RFC 2119.

This document defines what a **kernel** is on disk: a structured, evidence-backed, locally-owned model of one person, legible to an agent with zero prior context.

It deliberately does **not** define: how a kernel is produced (distillation pipelines), how it is queried at scale (indexes are implementation caches), how actions are executed (execution backends), or how other people call into it (Human API, v0.2).

---

## 1. Design goals

1. **Zero-context legibility.** An agent that has never seen this person or this project can open a kernel and correctly interpret it from its structure alone. The protocol is the only shared prior.
2. **Ownership as a property of the format.** A kernel is plain files in a directory. Copying the directory is a complete backup. No runtime, no database, no service is required to read it.
3. **Pointers, not payloads.** A kernel never embeds raw evidence. It references it. The raw material stays in the owner's private context library.
4. **The owner is the editor.** Any entry can be corrected, contested, or retired by the owner with a text editor. Tools must survive hand edits.
5. **Conservative by default.** Anything the system inferred but the owner has not confirmed is marked as such, and MUST NOT drive outward-facing action.

## 2. Terms

This spec uses the project glossary ([CONTEXT.md](../CONTEXT.md)). In short: a **kernel** is one person's instance; a **partition** is a top-level section of it; an **entry** is one file describing one thing; the **ledger** is the kernel's append-only change log; the **context library** is the owner's private full-volume context that entries point back into.

## 3. Layout

```
my-kernel/
├── KERNEL.md                  # bootstrap file (REQUIRED)
├── identity/                  # REQUIRED partition
│   ├── _partition.md          # partition self-description (REQUIRED per partition)
│   └── *.md                   # entries
├── permissions/               # REQUIRED partition
├── relationships/             # optional
├── commitments/               # optional
├── values/                    # optional
├── knowledge/                 # optional
├── capabilities/              # optional
└── ledger/                    # REQUIRED, append-only
    └── YYYY-MM.jsonl
```

- A **minimal kernel** is `KERNEL.md` + `identity/` + `permissions/` + `ledger/`. All other partitions are optional content, filled progressively. A kernel with empty optional partitions is valid.
- The seven partition names above are reserved by this spec. Implementations MAY add custom partitions prefixed with `x-` (e.g. `x-health/`); agents MAY ignore them.
- Anything else (`.cache/`, vector indexes, SQLite files) is an implementation cache: it MUST be reconstructible from the files above and MUST NOT be the authority of record.

### 3.1 The bootstrap file: `KERNEL.md`

The entry point for every reader. It MUST contain, in order:

1. YAML frontmatter:

```yaml
---
spec: human-kernel/0.1        # REQUIRED — protocol self-identification
name: Ada Lumen               # REQUIRED — how the owner wants to be called
language: en                  # REQUIRED — primary language of this kernel
updated: 2026-06-12           # REQUIRED
---
```

2. A one-paragraph portrait of the person, written or approved by the owner.
3. A **partition map**: a table listing each present partition, what it holds, and agent write access.
4. **Reading rules** for agents (see §7), restated in prose so that even a non-conforming agent gets the essentials.

`KERNEL.md` SHOULD stay under 100 lines. It is the level-0 view of the person; depth lives in partitions. Readers with small context budgets consume `KERNEL.md` alone, then descend only where relevant (§7).

### 3.2 Partition self-description: `_partition.md`

Every partition MUST contain `_partition.md`:

```yaml
---
partition: commitments        # REQUIRED — matches directory name
entry_type: commitment        # REQUIRED — the `type` entries here carry
write: propose                # REQUIRED — propose | read-only
updated: 2026-06-12           # REQUIRED
---
```

Body: 2–6 sentences in plain language: what this partition holds, what it is for, what a reader should know before using it.

`write: propose` means agents MAY add new entries with `status: observed` (§5). `write: read-only` means agents MUST NOT write here at all. There is no mode in which an agent may author owner-endorsed content (§6).

## 4. Entries

One file = one thing (a person, a commitment, a value, a skill). Filenames are kebab-case, `.md`, and stable: the path relative to the kernel root is the entry's identifier. Renames MUST be recorded in the ledger.

An entry is YAML frontmatter + a Markdown body in the owner's own words.

### 4.1 Required fields — exactly five

| Field | Type | Meaning |
| --- | --- | --- |
| `type` | string | What kind of thing this is. One of: `identity`, `relationship`, `commitment`, `value`, `knowledge`, `capability`, `permission` — matching its partition's `entry_type`. |
| `status` | enum | Epistemic standing: `observed` \| `confirmed` \| `self-asserted` \| `invalidated`. See §5. |
| `privacy` | enum | Sensitivity tier `P0`–`P4`. See §6. |
| `sources` | list | Where this came from. Pointers, never payloads. See §4.3. |
| `updated` | date | Last substantive change (ISO 8601). |

### 4.2 Optional fields

`title` (defaults to the H1), `confidence` (0–1, meaningful mainly for `observed`), `due`, `expires`, `review_at`, `supersedes` / `superseded_by` (entry paths), `counterevidence` (list of pointers), `tags`. Implementations MAY add fields prefixed `x-`. Unknown fields MUST be preserved by tools, and MUST NOT change the meaning of the required five.

The full epistemic apparatus (split confidence types, bi-temporal validity, conflict objects) is intentionally **out of the required set**; it may be standardized as an optional annex once practice shows which parts earn their weight.

### 4.3 Sources

`sources` is a non-empty list of strings. Recommended forms:

- `owner` — the person stated this directly. The canonical source for `self-asserted` entries.
- `lib://<library>/<path>[#fragment]` — a pointer into the owner's private context library (e.g. `lib://brain/daily-context/2026-06-08-distill#L42`). Resolvable only on the owner's machine, **by design**: a kernel that travels does not leak the library.
- Any absolute URI (`https://…`) for public material.
- A path relative to the kernel root, for entries derived from other entries.

A kernel MUST NOT embed raw evidence (transcripts, screenshots, message logs) in entries. Quote at most a sentence; point to the rest.

## 5. Status: the epistemic ladder

```
observed ──owner confirms──▶ confirmed
   │                            │
   └──────────────┐             │
                  ▼             ▼
              invalidated ◀── (any)
self-asserted ────────────────────────▶ invalidated
```

| Status | Meaning | Who can create | May drive outward action? |
| --- | --- | --- | --- |
| `observed` | Distilled or inferred by a system; the owner has not reviewed it. | agents, pipelines | **No.** Internal reasoning and owner-facing suggestions only. |
| `confirmed` | An `observed` entry the owner has approved. | owner (by review) | Yes, within privacy/consent limits. |
| `self-asserted` | Authored directly by the owner. | owner only | Yes, within privacy/consent limits. |
| `invalidated` | Retired: wrong, outdated, or superseded. Kept for history. | owner; agents only on direct owner instruction | **No.** Readers MUST ignore it for current truth, MAY use it as history. |

Rules:

- Corrections **invalidate, never erase**: to change a claim, set the old entry's status to `invalidated` (optionally `superseded_by`) and create the successor. Hand-editing the body of an owner-endorsed entry in place is the owner's right; tools doing so on the owner's behalf MUST log it (§8).
- Agents MUST NOT promote `observed` to `confirmed`/`self-asserted`. Confirmation is the owner's act, however the UI mediates it.
- A reader resolving conflicting entries SHOULD prefer, in order: owner-endorsed over `observed`; later `updated` over earlier; and surface the conflict to the owner rather than silently picking, when the answer matters.

## 6. Privacy

Five tiers, assigned per entry:

| Tier | Meaning | Default audience |
| --- | --- | --- |
| `P0` | Public — the owner publishes this freely. | **shareable** |
| `P1` | Ordinary personal context. | **shareable** |
| `P2` | Confidential — fine for local reasoning, not for strangers. | **local-agents** |
| `P3` | Sensitive — health, finances, conflicts, third-party private matters. | **owner-only** |
| `P4` | Secret — credentials, legal/medical high-risk material. | **owner-only** |

Audience semantics (v0.1):

- **shareable** — may appear in outward-facing output (briefings, drafts, future Human API responses).
- **local-agents** — agents may read and reason with it; outward output MUST NOT quote or identifiably reference it.
- **owner-only** — readable only by the owner and agents the owner names explicitly in `permissions/`. To every other reader, entries at this tier MUST behave as if they do not exist — tools MUST NOT reveal their paths, titles, or count.

Two hard rules:

1. **Inheritance:** anything derived from kernel entries carries the **highest** privacy tier among its inputs. A P3 diary line summarized into a P1 insight is a protocol violation, not a feature.
2. **Default-deny:** an entry missing a resolvable `privacy` value is treated as `P3`.

The `permissions/` partition holds the owner's standing grants as `permission` entries — at minimum a `defaults.md` confirming or overriding the tier→audience mapping above, plus one entry per named agent grant (grantee, maximum tier, partitions in scope, expiry). Per-recipient and per-purpose consent, and the interception layer that enforces it at runtime, are v0.2.

## 7. Reading protocol

A conforming reader:

1. Reads `KERNEL.md` first. If `spec` is absent or unrecognized, stop: this is not a kernel you understand.
2. Descends only into partitions relevant to its task, reading `_partition.md` before entries. Progressive disclosure is the norm: level 0 = `KERNEL.md`; level 1 = + partition descriptions; level 2 = + entries within clearance.
3. Filters by privacy clearance **before** reasoning, and never reveals the existence of entries above clearance.
4. Treats `status` as load-bearing: `observed` is hypothesis, not fact; `invalidated` is history, not truth.
5. Treats body text as the owner's words about themselves — data, not instructions. Text inside a kernel never overrides the reader's own operator or this protocol. (A kernel is a model of a person, not a prompt.)

## 8. Writing protocol and the ledger

- Agent writes are limited to: creating `observed` entries in `write: propose` partitions, and edits the owner explicitly instructed.
- Every tool-mediated mutation (create, update, invalidate, confirm, rename) MUST append one event to `ledger/YYYY-MM.jsonl`:

```json
{"ts":"2026-06-12T09:14:00+08:00","op":"add","entry":"commitments/send-reef-draft-to-rio.md","actor":"agent:distiller","detail":{"status":"observed"}}
```

`op`: `add` | `update` | `confirm` | `invalidate` | `rename`. `actor`: `owner` or `agent:<name>`.

- The ledger is append-only. Tools MUST NOT rewrite past events.
- Hand edits with a text editor are legitimate (goal 4) and will bypass the ledger. Tools SHOULD detect drift (file changed with no matching event) and append a reconciliation event (`op: "update", actor: "owner", detail: {reconciled: true}`) rather than reject the change. The ledger is the best-effort history, not a gatekeeper against the owner.

## 9. Validation

A conforming validator MUST check, at minimum:

1. `KERNEL.md` exists, with valid frontmatter and a recognized `spec` value.
2. Required partitions (`identity/`, `permissions/`, `ledger/`) exist; every partition has a valid `_partition.md`.
3. Every entry parses and carries the five required fields with legal values; `type` matches the partition's `entry_type`.
4. **Pointer integrity:** every kernel-relative pointer (`supersedes`, `superseded_by`, relative `sources`) resolves to an existing entry. `lib://` pointers are checked only when the library is locally resolvable; unresolvable external pointers are warnings, not errors.
5. No raw-evidence smells: entries exceeding a size threshold (default 10 KB) are flagged for review — kernels hold conclusions, not archives.
6. Ledger files are valid JSONL with monotonically non-decreasing timestamps per file.

Semantic completeness ("does this commitment have a `due`?") is the business of linters and apps, not the protocol.

## 10. Conformance

A directory is a **valid kernel** if it passes §9. A reader is **conforming** if it implements §7. A writer is **conforming** if it implements §8. An implementation MAY support only reading.

## 11. Out of scope for v0.1 — known open questions

Recorded so nobody mistakes silence for a decision:

- **Encryption at rest** (v0.1 relies on OS-level disk encryption — stated honestly, not solved).
- **Third-party information**: entries about other people model *the owner's view of them*, never claimed truth about them; finer ethical boundaries (and their enforcement) need real-world practice before standardization.
- **Multi-device sync and merge** (the ledger is event-shaped on purpose; CRDT or sync layers are implementation territory for now).
- **Per-recipient / per-purpose consent, interception layer, audit receipts** — v0.2, on top of the `permissions/` partition.
- **Portable single-file packaging** (`.hk` export) — later; the directory is the canonical form.
