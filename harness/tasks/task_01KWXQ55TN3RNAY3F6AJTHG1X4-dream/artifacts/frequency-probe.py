#!/usr/bin/env python3
"""Create the frequency-driven baseline for the metabolism probe.

This is intentionally simple: it scores each memory fragment by TF-IDF overlap
with existing kernel entry titles, then writes the top candidates into the same
comparison Markdown file used by metabolism-probe.py.
"""

from __future__ import annotations

import argparse
import hashlib
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


DEFAULT_MEMORY_DIR = Path("/Users/lizeyu/.openclaw/workspace/memory")
ARTIFACT_DIR = Path(__file__).resolve().parent
REPO_ROOT = ARTIFACT_DIR.parents[3]
DEFAULT_KERNEL_DIR = REPO_ROOT / "examples" / "zeyu-kernel"
DEFAULT_OUTPUT = ARTIFACT_DIR / "metabolism-probe-output.md"
DATE_FILE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
START = "<!-- frequency-baseline:start -->"
END = "<!-- frequency-baseline:end -->"


@dataclass(frozen=True)
class Entry:
    entry_id: str
    title: str
    tokens: frozenset[str]


@dataclass(frozen=True)
class Fragment:
    source: str
    index: int
    text: str

    @property
    def digest(self) -> str:
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()[:12]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data, text[end + 5 :]


def first_heading(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    for word in re.findall(r"[A-Za-z0-9_]{2,}", text.lower()):
        tokens.append(word)
    for run in re.findall(r"[\u4e00-\u9fff]+", text):
        if len(run) >= 2:
            tokens.extend(run[i : i + 2] for i in range(len(run) - 1))
        if len(run) >= 3:
            tokens.extend(run[i : i + 3] for i in range(len(run) - 2))
    return tokens


def load_entries(kernel_dir: Path) -> list[Entry]:
    entries: list[Entry] = []
    for path in sorted(kernel_dir.glob("*/*.md")):
        if path.name == "_partition.md" or path.parts[-2] == "ledger":
            continue
        frontmatter, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if "type" not in frontmatter:
            continue
        title = first_heading(body, path.stem.replace("-", " "))
        entries.append(
            Entry(
                entry_id=path.relative_to(kernel_dir).as_posix(),
                title=title,
                tokens=frozenset(tokenize(title)),
            )
        )
    return entries


def latest_memory_files(memory_dir: Path, limit: int, max_bytes: int) -> list[Path]:
    candidates = [p for p in memory_dir.glob("*.md") if DATE_FILE_RE.match(p.name)]
    candidates = [p for p in candidates if p.stat().st_size <= max_bytes]
    return sorted(candidates, key=lambda p: p.name)[-limit:]


def split_fragments(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    parts = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    return [part for part in parts if len(part) >= 20]


def load_fragments(memory_dir: Path, days: int, max_bytes: int) -> list[Fragment]:
    fragments: list[Fragment] = []
    for path in latest_memory_files(memory_dir, days, max_bytes):
        for index, text in enumerate(split_fragments(path), start=1):
            fragments.append(Fragment(path.name, index, text))
    return fragments


def score_fragments(entries: list[Entry], fragments: list[Fragment]) -> list[tuple[float, Fragment, list[str]]]:
    docs = [tokenize(fragment.text) for fragment in fragments]
    document_frequency: defaultdict[str, int] = defaultdict(int)
    for doc in docs:
        for token in set(doc):
            document_frequency[token] += 1

    total_docs = max(1, len(docs))
    results: list[tuple[float, Fragment, list[str]]] = []
    for fragment, tokens in zip(fragments, docs):
        tf = Counter(tokens)
        score = 0.0
        matched: list[str] = []
        for entry in entries:
            overlap = entry.tokens.intersection(tf)
            if not overlap:
                continue
            matched.append(f"{entry.entry_id} ({entry.title})")
            for token in overlap:
                idf = math.log((1 + total_docs) / (1 + document_frequency[token])) + 1
                score += tf[token] * idf / max(1, len(entry.tokens))
        if score > 0:
            results.append((score, fragment, matched))
    return sorted(results, key=lambda item: item[0], reverse=True)


def render_baseline(
    entries: list[Entry],
    fragments: list[Fragment],
    scored: list[tuple[float, Fragment, list[str]]],
    include_private_text: bool,
    top: int,
) -> str:
    lines = [
        START,
        "## Frequency Baseline",
        "",
        "Pure-statistical baseline: TF-IDF overlap between memory fragments and existing kernel entry titles.",
        "",
        f"- Kernel title entries: {len(entries)}",
        f"- Memory fragments scored: {len(fragments)}",
        f"- Candidates shown: {min(top, len(scored))}",
        f"- Private text embedded: `{str(include_private_text).lower()}`",
        "",
        "| Rank | Score | Source | Fragment hash | Matched kernel titles | Fragment |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for rank, (score, fragment, matched) in enumerate(scored[:top], start=1):
        if include_private_text:
            preview = re.sub(r"\s+", " ", fragment.text).strip()[:240]
        else:
            preview = "private text omitted; rerun with --include-private-text locally"
        lines.append(
            f"| {rank} | {score:.3f} | `{fragment.source}#{fragment.index}` | "
            f"`{fragment.digest}` | {'<br>'.join(matched)} | {preview} |"
        )
    lines.extend(["", END, ""])
    return "\n".join(lines)


def replace_frequency_section(path: Path, section: str) -> None:
    if path.exists():
        text = path.read_text(encoding="utf-8")
    else:
        text = "# Metabolism Probe Output\n\n"

    start = text.find(START)
    end = text.find(END)
    if start != -1 and end != -1 and end > start:
        end += len(END)
        text = text[:start] + section.rstrip() + text[end:]
    else:
        text = text.rstrip() + "\n\n" + section
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel-dir", type=Path, default=DEFAULT_KERNEL_DIR)
    parser.add_argument("--memory-dir", type=Path, default=DEFAULT_MEMORY_DIR)
    parser.add_argument("--days", type=int, default=14)
    parser.add_argument("--max-bytes", type=int, default=200_000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--include-private-text", action="store_true")
    args = parser.parse_args()

    entries = load_entries(args.kernel_dir)
    fragments = load_fragments(args.memory_dir, args.days, args.max_bytes)
    scored = score_fragments(entries, fragments)
    section = render_baseline(entries, fragments, scored, args.include_private_text, args.top)
    replace_frequency_section(args.output, section)
    print(f"Wrote frequency baseline to {args.output} with {min(args.top, len(scored))} candidates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
