# Verification

What was checked in this repository, how, and what was left out. The last checks ran on 2026-11-24 and 2026-11-25. Each part's main limitations are under "Status and gaps" in the [README](README.md#status-and-gaps).

## Automated checks

- **Internal links.** 2,520 checked, none broken.
- **External links.** 179 links other than YouTube. Three refuse automated requests: two DOI links into the ACM Digital Library and one Medium post. They open in a browser.
- **arXiv citations.** 119 citations to 103 distinct papers. Every title and year matches the arXiv record.
- **Lecture citations.** 1,412 links point to a moment in a lecture video. Each was checked against the two-minute block of the machine transcript at that moment.
- **Overlap with the sources.** About 2.5 million words of sources were compared with the chapters. The longest passage a chapter shares with a source is 23 words: a quotation with an attribution, an author list or a paper title.
- **Code.** 66 Python listings run on their own, and 16 tests pass in four pytest suites. Two more suites fail on purpose, as their chapters describe, to show tests catching planted errors. A third needs a paid model and is labelled as pseudocode that does not run as pasted. The four programs in `examples/` match their chapters and run.

## The verification pass

An automated check shows that a citation points where it says, not that the source says what the chapter claims. On 2026-11-24, a verification pass compared every statement that a chapter attributes to a lecture or to the book with the source at the cited place. Where the transcript had the lecturer's own content, passages written from general knowledge were replaced with it.

| Part | Attributed statements checked | Corrected | Chapters deepened |
|---|---|---|---|
| [01 Foundations](01-foundations/README.md) | 76 links, about 25 other attributions | 30 | 6 of 8 |
| [02 Building agents](02-building-agents/README.md) | 102 links | at least one in each of the 8 chapters | 7 of 8 |
| [03 Evaluation](03-evaluation/README.md) | 55 links, about 55 other attributions | 16 | 4 of 8 |
| [04 Safety and security](04-safety-and-security/README.md) | 109 links, about 99 statements | 21 substantive, plus 8 typographical | 8 of 9 |
| [05 Frameworks and multi-agent](05-frameworks-and-multi-agent/README.md) | 96 links, 68 transcript blocks, slides, 2 MCP specification pages | about 20 | 5 of 7 |
| [06 Frontier applications](06-frontier-applications/README.md) | 116 statements on 124 links | 30 | 5 of 5 |
| [07 ML in production](07-ml-in-production/README.md) | about 200 statements, full book text | 9 | 7 of 10 |
| [08 Quality assurance](08-quality-assurance/README.md) | about 218 statements, full book text | 12 | 8 of 14 |
| [09 Efficient deep learning](09-efficient-deep-learning/README.md) | 156 links, 138 transcript blocks, slides | 21 | 9 of 11 |
| [10 LLM internals](10-llm-internals/README.md) | 95 links, about 180 unlinked statements | 49 | 13 of 13 |

In total, about 1,500 attributed statements were checked and more than 210 corrected. Part 11 is absent because it was written from the other parts.

### Kinds of errors found

All were corrected.

- A citation that pointed at a moment where the statement is not made.
- Half of what a lecturer said: for example, "PPO beats DPO" without "but DPO is far cheaper to experiment with".
- Numbers and names written from memory: wrong arXiv identifiers, a model's name, a vulnerability type.
- A definition or a list attributed to the book that the book does not contain, replaced by what the book says.
- Two slide titles quoted that do not exist.
- Passages that put a framing into a lecturer's mouth.

## What is not verified

- **The capstones.** The five capstones in part 11 were specified, not carried out. Their hours and costs, and those of the roadmap, are estimates.
- **Engineering judgment.** It is marked in the chapters as this repository's own and was not checked against a source.
- **General knowledge.** Topics that no transcript covers are explained from general knowledge.
- **Fast-moving facts.** Model names, prices, APIs, products and regulation are true as of the date each chapter gives, usually the lecture date or 2026-11-24.
- **External links.** Links other than those named above were not all reopened, and YouTube links were not checked. The Fall 2025 Berkeley course page address in [SOURCES.md](SOURCES.md) returned an HTTP 404 error on 2026-11-24.
- **The transcripts.** They are machine-made and can garble names. The lectures are the authority: a chapter that disagrees with its source is wrong.

## Further limitations by part

Further ones, not listed in the [README](README.md#status-and-gaps):

- **Part 01.** **01.06** A drop of more than 30 points is quoted from a slide that could not be re-read.
- **Part 02.** **02.02, 02.07** The agent-computer interface, with its 12.5 percent figure, comes from the SWE-agent paper, which was not re-read.
- **Part 04.** **04.08** The 35 zero-days figure rests on the transcript alone, and the C example was not run.
- **Part 08.** **08.05** The cost estimate assumes $0.50 per million tokens.
- **Part 10.** **10.02, 10.05** The einops and Triton snippets are illustrative and were not run.
- **Part 11.** **11.04, 11.05** Capstones 4 and 5 name no dataset, model, library, engine or price, because none was verified.

## How to report an error

Open an issue on the repository. Name the chapter and, for a claim taken from a lecture, the timestamp.
