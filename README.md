# slipbox

Raul's personal reading/notes system — a slipbox (Zettelkasten-style) for retaining what he reads and building a library of his own applied thinking, not book summaries.

Full operating rules for how this repo is used (filing, the summary gate, note format, linking, backlinks) live in [`CLAUDE.md`](./CLAUDE.md) — read that before working in here.

## Structure

```
inbox/     raw, unprocessed captures — short-lived, messy is fine
sources/   one file per book/article — metadata + literature notes
notes/     permanent, atomic, linked notes — the real asset
index.md   curated groupings of notes by theme — built bottom-up
```

## Backlinks

`.github/workflows/backlinks.yml` runs `scripts/generate_backlinks.py` on every push to `main`, parsing the `links:` frontmatter across `notes/*.md` and regenerating a "Linked from" section at the bottom of every note that's a link target. Fully automatic, no dependencies beyond the Python standard library.
