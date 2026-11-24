# Verification

What was checked in this repository, how, and what was left out. The last checks ran on 2026-11-24 and 2026-11-25. Each part's main limitations are under "Status and gaps" in the [README](README.md#status-and-gaps). The rest are under [Limitations by part](#limitations-by-part).

## Automated checks

These checks ran on 2026-11-25, after the verification pass.

- **Internal links.** 2,520 checked, none broken.
- **External links.** 179 links other than YouTube. Three refuse automated requests: two DOI links into the ACM Digital Library and one Medium post. They open in a browser.
- **arXiv citations.** 119 citations to 103 distinct papers. Every title and year matches the arXiv record.
- **Lecture citations.** 1,412 links in the chapters point to a moment in a lecture video. Each was checked against the two-minute block of the machine transcript it points to.
- **Overlap with the sources.** The chapters were compared with about 2.5 million words of sources. The longest passage a chapter shares with a source is 23 words: short quotations with an attribution, or author lists and paper titles.
- **Code.** 66 Python listings run on their own, and 16 tests pass in four pytest suites. Three more suites fail on purpose, as their chapters describe, to show tests catching planted errors. The four programs in `examples/` are identical to their chapter listings and run.
- **Chapter structure.** Every chapter has the same required sections, a level tag, a self-check with answers and a sources list, and at most 3,700 words including code.

## The verification pass

An automated check shows that a citation points where it says. It does not show that the source says what the chapter claims. The verification pass, run on 2026-11-24, covered that, one part at a time. Every statement that a chapter attributes to a lecture or to the book was compared with the source at the cited place. Where the transcript held the lecturer's own content and the chapter had been written from general knowledge, the passage was replaced.

| Part | Attributed statements checked | Corrected | Chapters deepened |
|---|---|---|---|
| [01 Foundations](01-foundations/README.md) | 76 timestamped links, about 25 other attributions | 30 | 6 of 8 |
| [02 Building agents](02-building-agents/README.md) | 102 timestamped links | at least one in each of the 8 chapters | 7 of 8 |
| [03 Evaluation](03-evaluation/README.md) | 55 timestamped links, about 55 other attributions | 16 | 4 of 8 |
| [04 Safety and security](04-safety-and-security/README.md) | 109 links, about 99 attributed statements | 21 substantive, plus 8 typographical | 8 of 9 |
| [05 Frameworks and multi-agent](05-frameworks-and-multi-agent/README.md) | 96 links, 68 transcript blocks, the slides, 2 MCP specification pages | about 20 | 5 of 7 |
| [06 Frontier applications](06-frontier-applications/README.md) | 116 statements on 124 links | 30 | 5 of 5 |
| [07 ML in production](07-ml-in-production/README.md) | about 200 statements against the full book text | 9 | 7 of 10 |
| [08 Quality assurance](08-quality-assurance/README.md) | about 218 statements against the full book text | 12 | 8 of 14 |
| [09 Efficient deep learning](09-efficient-deep-learning/README.md) | 156 links, 138 transcript blocks and the slides | 21 | 9 of 11 |
| [10 LLM internals](10-llm-internals/README.md) | 95 links and about 180 unlinked statements (about 275) | 49 | 13 of 13 |

In total, about 1,500 attributed statements were checked and more than 210 corrected. Part 11 was written from the other parts and has no source of its own.

### Kinds of errors found

All were corrected.

- A citation that pointed at a moment where the statement is not made.
- Half of what a lecturer said: for example, "PPO beats DPO" without "but DPO is far cheaper to experiment with".
- Numbers and names written from memory: wrong arXiv identifiers, a model's name, a vulnerability type.
- A definition or a list attributed to the book that the book does not contain, replaced by what the book says.
- Two slide titles quoted that do not exist.
- Passages that put a framing into a lecturer's mouth.

## What is not verified

- **The capstones.** The five capstone projects in part 11 were specified, not carried out. The hours and costs in the capstones and in the roadmap are estimates.
- **Engineering judgment.** Statements of engineering judgment were not checked against a source. The chapters mark them as this repository's own.
- **General knowledge.** Where a transcript did not cover a topic, the chapter still explains it from general knowledge.
- **Fast-moving facts.** Model names, prices, APIs, products and regulation are true as of the date each chapter gives, usually the lecture date or 2026-11-24.
- **External links.** Links other than those named above were not all reopened. YouTube links were not checked.
- **The transcripts.** They are machine-made and can garble names. The lectures are the authority: if a chapter and its source disagree, the source wins.

## Limitations by part

The [README](README.md#status-and-gaps) lists, for each part, the limitations to know before reading. This list holds the rest: figures, names, code and procedures that could not be confirmed.

### Part 01 · Foundations

- **01.06** A drop of more than 30 points in a logic task is quoted from a slide that could not be re-read.

### Part 02 · Building agents

- **02.02, 02.07** The agent-computer interface, with its 12.5 percent figure, comes from the SWE-agent paper, which was not re-read.

### Part 03 · Evaluation

- **03.02** One lecture slide labels the all-runs metric "pass@k" while defining pass^k. This course writes pass^k for "all runs succeed".

### Part 04 · Safety and security

- **04.08** The figure of 35 zero-days rests on the transcript alone, and the C example was not run.

### Part 05 · Frameworks and multi-agent systems

- **05.04, 05.05** Theory of mind, debate and the other run-time collaboration patterns are not in the lectures; the pattern table is this repository's.

### Part 06 · Frontier applications

- **06.04** The Lean snippet was not executed.

### Part 07 · ML in production

- **07.02, 07.05, 07.06, 07.09** The ladder of alternatives, the cost table, the decision-record format, the feedback-loop framing and the cache invalidation rule are this repository's own.

### Part 08 · Quality assurance

- **08.05** The cost estimate assumes $0.50 per million tokens, and the model-call interface is pseudocode.

### Part 09 · Efficient deep learning

- **09.02, 09.04, 09.05, 09.07, 09.08** Some figures are garbled, cut off or unclear in the transcript. They are quoted with that caveat or left out. The LoRA memory rules of thumb (09.09) are unverified approximations.

### Part 10 · LLM internals

- **10.01, 10.05, 10.06** The slides are missing or are outlines only. Some figures, such as the 44% and 80% MLP FLOP shares, are taken from the transcript as spoken.
- **10.02, 10.05** The einops and Triton snippets are illustrative and were not run.

### Part 11 · Professional practice

- **11.04, 11.05** Capstones 4 and 5 name no dataset, model, library, engine or price, because none was verified.

## How to report an error

Open an issue on the repository. Name the chapter and, for a claim taken from a lecture, the timestamp.
