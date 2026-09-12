# slipbox

A running library of what I read, and what I actually think about it.

Most reading doesn't survive contact with real life. A good idea lands, feels important for about a week, and quietly disappears back into the noise. This repository is the mechanism built to stop that: every book moves from raw capture through to atomic, linked notes, and nothing gets filed away until it's actually *mine* — connected to something I've lived, argued with, or changed my mind about.

It borrows its shape from two older habits of mind: Niklas Luhmann's *Zettelkasten*, and Ryan Holiday's practice of never carding an idea until it's survived a few weeks past the first reading. Neither one trusted a first impression. Neither do I.

## How it's organized

```
inbox/     raw, unprocessed captures
sources/   one file per book — literature notes, organized by idea, not chronology
notes/     the permanent record — atomic, linked, reviewed before anything gets written
index.md   clusters that emerge bottom-up from the link graph, never planned in advance
```

Full operating rules live in [`CLAUDE.md`](./CLAUDE.md).

## The distinction that matters most

Every permanent note is one of two things:

- a **reflection** — my own reaction, judgment, or a genuine connection to something I've actually done, not a paraphrase of the author's point
- a **concept** — an idea worth keeping as a building block in the graph, atomized and correctly linked, even before it's earned a personal take

The line between them exists on purpose. Generating a competent summary of any book is trivial now. What isn't trivial — what this system is actually built to produce — is the second layer: whether an idea survives contact with a specific life, a specific set of decisions, a specific set of mistakes.

## Backlinks, automatically

A small script (pure Python, no dependencies) parses the link graph on every push and rebuilds a "Linked from" section on every note that's a link target. The graph, not a folder hierarchy, is what actually organizes this project.

---

What tends to show up here: product and organizational strategy, go-to-market thinking, how incentive systems actually shape behavior, decision-making under uncertainty — and, less predictably, whatever a given season of life happens to be asking of me.

This is intentionally a working system, not a finished one. It's imperfect in the way anything still in use actually is.
