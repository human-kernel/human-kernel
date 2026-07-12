# Human Kernel

Shared language for the Human Kernel project — an open-source protocol and local-first app that models one person so authorized agents can understand and act as that person.

## Language

**Human Kernel**:
The structured, auditable, locally-owned model of one person — everything an agent needs to understand and act with that person's intent. The project, the protocol, and the product share this one name.
_Avoid_: Human OS, memory app, second brain, understanding engine

**kernel** (lowercase):
One person's instance of the model ("your kernel") and the center of the concentric structure. It belongs to the person, not to any agent framework that expresses it. Self-describing: readable by an agent that has never seen this person or this system before. Capitalized Human Kernel refers to the project and protocol.

**zero-context legibility**:
The kernel's defining property: an agent with no prior knowledge can orient and correctly interpret a kernel from its structure alone. The protocol is the only shared prior.

**context library**:
A person's private, human-first collection of raw and curated context — notes, logs, transcripts, files — that encloses the kernel as its raw context and evidence layer. Messy by design; it is never required to be agent-legible.
_Avoid_: second brain, memory database

**Brain**:
The founder's context library instance (ZeYu-AI-Brain). Also the root of the earlier Brain OS effort, whose mission Human Kernel succeeds.

**distillation**:
Turning context-library material into kernel entries, with provenance pointing back to the sources. The kernel never embeds evidence — it only points to it.

**partition**:
A top-level section of a kernel (identity, relationships, commitments, values, knowledge, capabilities, permissions), each carrying its own self-description so agents know what it is and whether they may write to it.

**entry**:
One file in a partition describing one thing (a person, a commitment, a value). The unit of reading, correction, and consent.

**minimal kernel**:
The smallest valid kernel: the bootstrap file plus identity and permissions. All other partitions are optional content, filled progressively.

**ledger**:
A kernel's append-only change log. Corrections invalidate; nothing is silently overwritten.

**interception layer**:
The policy point every kernel read and write passes through: sensitivity inheritance, consent enforcement, and audit. Planned for v0.2.

**alter ego**:
One of potentially multiple expression/persona layers generalized outward from a kernel and its enclosing context: a counterpart that answers, reasons, reminds, and acts as the person within granted permissions through a replaceable agent framework. Always lowercase — a role, not a brand, not a runtime.
_Avoid_: digital twin, 数字分身, AI companion, chatbot, assistant, personal OS

**Human API**:
The outer permissioned interface through which another person, product, or agent queries or invokes a selected slice of someone's kernel.
_Avoid_: agent marketplace, plugin API

**execution backend**:
An external system that carries out actions handed off by an alter ego after user-confirmed permission. Optional and replaceable; never part of the kernel.
