#!/usr/bin/env python3
"""Regenerate 'Linked from' backlink sections across notes/*.md.

Parses the `links:` frontmatter list on every note (see CLAUDE.md Rule 5)
and writes a '## Linked from' section at the bottom of every note that is
a link target. Pure stdlib on purpose: the frontmatter schema is small and
fixed, so a full YAML parser is unneeded weight.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

NOTES_DIR = Path(__file__).resolve().parent.parent / "notes"
LINKED_FROM_RE = re.compile(r"\n*## Linked from\n.*?(?=\n## |\Z)", re.DOTALL)


def parse_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1], parts[2]


def parse_frontmatter(fm_text: str) -> dict:
    data: dict = {"id": None, "title": None, "links": []}
    in_links = False
    current: dict | None = None

    def flush() -> None:
        nonlocal current
        if current is not None:
            data["links"].append(current)
            current = None

    for line in fm_text.splitlines():
        if re.match(r"^id:\s*", line):
            flush()
            in_links = False
            data["id"] = parse_scalar(line.split(":", 1)[1])
        elif re.match(r"^title:\s*", line):
            flush()
            in_links = False
            data["title"] = parse_scalar(line.split(":", 1)[1])
        elif re.match(r"^links:\s*$", line):
            flush()
            in_links = True
        elif in_links and re.match(r"^\s*-\s*id:\s*", line):
            flush()
            current = {"id": parse_scalar(re.sub(r"^\s*-\s*id:\s*", "", line))}
        elif in_links and re.match(r"^\s+relation:\s*", line) and current is not None:
            current["relation"] = parse_scalar(line.split(":", 1)[1])
        elif in_links and re.match(r"^\S", line):
            # dedented to a new top-level key: links block is over
            flush()
            in_links = False
    flush()
    return data


def load_notes() -> dict[str, dict]:
    notes = {}
    if not NOTES_DIR.exists():
        return notes
    for path in sorted(NOTES_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        split = split_frontmatter(text)
        if split is None:
            print(f"warning: {path.name} has no frontmatter, skipping", file=sys.stderr)
            continue
        fm_text, body = split
        fm = parse_frontmatter(fm_text)
        if not fm["id"]:
            print(f"warning: {path.name} has no id, skipping", file=sys.stderr)
            continue
        notes[fm["id"]] = {
            "path": path,
            "text": text,
            "fm_text": fm_text,
            "body": body,
            "title": fm["title"] or path.stem,
            "links": fm["links"],
        }
    return notes


def build_backlinks(notes: dict[str, dict]) -> dict[str, list[dict]]:
    backlinks: dict[str, list[dict]] = {}
    for note_id, note in notes.items():
        for link in note["links"]:
            target = link.get("id")
            if not target:
                continue
            backlinks.setdefault(target, []).append(
                {
                    "id": note_id,
                    "title": note["title"],
                    "path": note["path"],
                    "relation": link.get("relation", "related"),
                }
            )
    return backlinks


def render_body(body: str, incoming: list[dict]) -> str:
    body = LINKED_FROM_RE.sub("", body).rstrip("\n")
    if not incoming:
        return body + "\n"
    lines = ["## Linked from", ""]
    for entry in sorted(incoming, key=lambda e: e["id"]):
        rel_path = entry["path"].name
        lines.append(f"- [{entry['title']}](./{rel_path}) — {entry['relation']}")
    return body + "\n\n" + "\n".join(lines) + "\n"


def main() -> int:
    notes = load_notes()
    if not notes:
        print("no notes found, nothing to do")
        return 0

    backlinks = build_backlinks(notes)
    changed = []
    for note_id, note in notes.items():
        new_body = render_body(note["body"], backlinks.get(note_id, []))
        new_text = "---" + note["fm_text"] + "---" + new_body
        if new_text != note["text"]:
            note["path"].write_text(new_text, encoding="utf-8")
            changed.append(note["path"].name)

    if changed:
        print("updated backlinks in: " + ", ".join(changed))
    else:
        print("backlinks already up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
