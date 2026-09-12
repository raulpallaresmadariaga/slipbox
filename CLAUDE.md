# Slipbox — Operating Rules

This repo is Raul's personal slipbox: a structured reading/notes system built for two goals —
(1) retain and connect what he reads instead of forgetting it, and
(2) build a real library of his own applied thinking (not book summaries) for career use and an eventual MBA application.

**The whole point of this repo is that it is NOT the same as asking Claude cold.** Claude already knows the textbook content of most books Raul reads. The value here is everything Claude can't produce on its own: Raul's own reaction to an idea, and its connection to what he's actually lived and done (Worky, Nova, Cobre, GTM, comp design, etc). Every rule below exists to protect that distinction. When in doubt, favor rules that force Raul's own thinking onto the page over rules that make filing convenient. (Concept notes, introduced in Rule 4, are the one deliberate exception — they exist to give reflection notes correctly-categorized, linkable material to connect to, not to replace them.)

## Context — who this is for

Raul Pallares Madariaga, Head of Product at Worky (Mexican HR/payroll SaaS). Leads the Nova migration program and manages a PM team, reporting to Juanma. Career arc: Dell EMC → OYO Rooms → Cobre (employee #22, Product Lead / Revenue Analytics) → Worky. Deep experience in compensation system design (OTE/NDR logic) and solution-selling GTM frameworks.

Current professional focus: moving from tactical execution to operating at a true Head-of-Product level — product P&L ownership, cadence quality, executive presence, leading with framing rather than reporting. Actively working on confidence/assertiveness and influence-without-authority as core growth areas.

Preparing for an MBA starting August 2027, targeting Harvard, Booth, Wharton, MIT, and Columbia.

Recurring domains his reading is likely to touch, roughly in order of relevance: product strategy and leadership, GTM/RevOps, compensation design, executive presence and influence, venture capital and LATAM market strategy, data-driven decision-making.

Use this context actively, not just as background: when drafting a note's `applies_to` field, proposing an index cluster, or judging whether a draft clears the summary gate (Rule 4), reach for a real, specific connection to this context — "this is how Nova's governance problem actually works," not "this could apply to product management in general." If a connection is ambiguous, ask Raul rather than inventing one that sounds plausible but doesn't actually hold — a false `applies_to` is worse than none, because it corrupts the exact thing this system exists to protect. If Raul's role or focus changes, he'll tell you to update this section — don't infer changes to it on your own.

## Repo structure

```
inbox/     raw, unprocessed captures — short-lived, messy is fine
sources/   one file per book/article — metadata + literature notes
notes/     permanent, atomic, linked notes — the real asset
index.md   curated groupings of notes by theme — built bottom-up, never planned in advance
```
(A `review/` stage for spaced-repetition is planned but not built yet — see "Stage 2" at the bottom. Ignore it until told otherwise.)

## Rule 1 — Never file a capture without knowing its source

When Raul pastes raw notes, do not write anything until you know which source they belong to.

- If he names the book/article, check whether `sources/<slug>.md` exists. If not, create it (see Rule 2) before filing anything.
- If he does **not** name a source, ask. Never guess — not even if only one source currently has `status: reading`. He may be reading more than one thing at once, and a silently misattributed note corrupts the record.
- Once the source is confirmed, append the raw text to `inbox/<YYYY-MM-DD>.md` under a heading naming that source.
- When filing, correct spelling and grammar only. Leave Raul's phrasing, word choice, and structure untouched — this is a raw personal reaction, not prose to polish, and Rule 4's "Raul's voice" bar depends on it staying his.

## Rule 2 — Source files

`sources/<slug>.md` frontmatter:

```yaml
title:
author:
status: reading | finished | paused
started:
finished:
permanent_notes: []   # ids of permanent notes this source has produced
```

Body holds literature notes: raw captures organized by idea (not chronology) once processed out of inbox/. Literature notes are allowed to stay close to the source text — they are not held to the Rule 4 bar below, only permanent notes are.

**Date fields, always full `YYYY-MM-DD`:** if Raul gives only a month and year (e.g. "January 2026"), assume the 1st of that month unless he states an exact day. Never write a partial date like `2026-01` into any frontmatter field.

## Rule 3 — Processing run (weekly, manual or scheduled)

1. Read everything in `inbox/` not yet processed.
2. Group by source. For each source, fold captures into that source's literature notes (organize by idea).
3. From the literature notes, draft **candidate** permanent notes. Do not write to `notes/` yet — present candidates for Raul's review first, always.

## Rule 4 — The summary gate, and the concept-note alternative (the most important rule in this file)

Every candidate for `notes/` is one of two types, set via `type:` in its frontmatter (Rule 5). Which bar it has to clear depends on the type.

**`type: reflection`** — the summary gate applies. Before proposing any draft as a reflection note, check it against this bar. A draft may proceed **only if it has at least one of**:

- A personal reaction, judgment, disagreement, or open question, in Raul's voice
- An explicit connection to Raul's own work or experience
- An explicit relationship (agrees / contradicts / extends / is-an-example-of) to a note already in `notes/`

If a draft has **none** of these — it's just the book's idea restated — it doesn't qualify as a reflection note. Don't write it to `notes/` as one. Instead, ask Raul directly: what's your take on this, where have you seen this show up, does this support or clash with something you've already written. Nothing gets promoted as a reflection until there's something of his own attached — or, if the idea is worth keeping anyway, it can go in as a concept note instead (below).

**`type: concept`** — no personal-reaction requirement. A concept note captures an idea worth having as a standalone, linkable node in the graph — correctly themed and tagged, and rewritten in Raul's own words so it stands on its own (Rule 5) rather than pasted or lightly edited from the source. The bar here is lighter than the summary gate, but not zero: the idea still has to be understood well enough to restate cleanly and atomically. A `type: concept` note still needs Raul's review before it's written (Rule 9) — the relaxed bar is about content, not about skipping approval.

Not every capture deserves to become a permanent note of either type, and that's fine — weak material can just sit unpromoted in a source file rather than being force-processed into a mediocre note. It also doesn't have to happen the week it was captured: a short delay before finalizing a note is a feature, not a bug — the ideas that still feel important a few weeks later are usually the ones worth keeping (this is deliberately borrowed from Ryan Holiday's own notecard practice: he waits weeks after finishing a book before carding anything, precisely to separate what stuck from what merely stood out on first read).

## Rule 5 — Permanent note format

Filename: `notes/YYYYMMDDHHMM-slug.md` (timestamp keeps IDs stable and sortable even if the topic gets renamed later).

Frontmatter:

```yaml
id: YYYYMMDDHHMM
title:
type: reflection | concept   # reflection: subject to the Rule 4 summary gate. concept: atomic idea, no personal-reaction requirement.
theme:              # one primary filing category, e.g. "Strategy", "Leadership", "Compensation Design"
tags: []            # optional secondary tags
source: <sources-slug or page ref>, or "original" if it's Raul's own synthesis across sources
links:
  - id: <other-note-id>
    relation: supports | contradicts | extends | example-of
applies_to: >        # required for type: reflection — how this shows up in Raul's actual work or life. This is
                      # the field that makes reflections different from a search index over books he's read.
                      # Optional for type: concept.
```

Body: the idea rewritten so it stands on its own, without needing the source to make sense.

## Rule 6 — Linking

The `notes/` folder is small enough to read in full — don't build search infrastructure for this. When drafting a candidate, read the existing notes, flag topical overlap, and propose a link with a specific relation type (never a generic "related"). Raul approves or edits every link before it's written.

## Rule 7 — Index / clusters: proposed automatically, named by Raul

Don't wait for Raul to notice a cluster forming. On a monthly cadence (or whenever `notes/` grows enough to warrant it), scan the link graph for notes that reference each other densely (3+ mutual links is a reasonable trigger) and propose a name and one-paragraph description for a new `index.md` section. Raul approves or renames it; only then does it get written.

## Rule 8 — Backlinks: fully automatic, no review needed

A GitHub Action runs on every push to `main`: it parses `links:` across all notes and regenerates a "Linked from" section at the bottom of every note that is a link target. This is pure mechanical bookkeeping — no approval step, no judgment involved.

## Rule 9 — Hard "never"s

- Never write to `notes/` without Raul reviewing the draft first.
- Never guess which source an untagged capture belongs to.
- Never let a `type: reflection` note through that is purely the source's idea restated (Rule 4). A `type: concept` note restating the idea cleanly and atomically is fine — that's its job.
- Never invent a relationship link that doesn't clearly hold — ask if unsure.

## Stage 2 (not built yet — do not implement until Raul asks)

A spaced-repetition / resurfacing layer for retention, using this same repo as the deck: `last_reviewed` and `review_count` fields on permanent notes, plus a scheduled prompt that resurfaces older notes for active recall before showing their content. Parked deliberately until stage 1 (capture → literature notes → permanent notes → links) is running smoothly.
