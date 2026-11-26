# Verification

What was checked in this repository, how, and what was left out. The checks ran on 2026-11-24 and 2026-11-25. Each part's main limitations are under "Status and gaps" in the [README](README.md#status-and-gaps).

## Automated checks

These checks ran on 2026-11-25, after the second review.

- **Internal links.** 2,636 checked, none broken; 4,962 with the lecture guides on 2026-11-26, none broken.
- **External links.** 181 links other than YouTube. Three refuse automated requests: two DOI links into the ACM Digital Library and one Medium post. They open in a browser.
- **arXiv citations.** 119 citations to 103 distinct papers. Every title and year matches the arXiv record.
- **Lecture citations.** 1,459 links point to a moment in a lecture video. Each was checked against the two-minute block of the machine transcript at that moment.
- **Overlap with the sources.** About 2.5 million words of sources were compared with the chapters. The longest passage a chapter shares with a source is 23 words: a quotation with an attribution, an author list or a paper title.
- **Diagrams.** 81 diagrams in 80 chapters. Each passes Mermaid's own parser, and each has a caption before it and a plain sentence after it.
- **Code.** 66 Python listings run on their own, and 17 tests pass in four pytest suites. Two more suites fail on purpose, as their chapters describe, to show tests catching planted errors. A third needs a paid model and is labelled as pseudocode that does not run as pasted. The remaining listings that do not run alone are labelled in their chapters: they need a package such as numpy or PyTorch, or a file the reader creates. The four programs in `examples/` are identical to their chapter listings and run.
- **Chapter shape.** Every chapter has the same required sections, a level tag, a self-check with answers and a sources list. The longest chapter is 4,184 words including code, diagrams and link addresses.

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

## Second review

The verification pass left two things undone. It rewrote many passages, and nobody had checked those since. And nobody had read the chapters as the reader they are written for. On 2026-11-25 a second review did both, one reviewer per part, who also added a diagram where a picture explains more than prose.

| Part | Attributed statements re-checked | Corrected | Diagrams added |
|---|---|---|---|
| [01 Foundations](01-foundations/README.md) | 198 | 22 | 9 |
| [02 Building agents](02-building-agents/README.md) | about 150 claims on 149 links, plus 18 quotations | corrections in 7 of 8 chapters | 8 |
| [03 Evaluation](03-evaluation/README.md) | 98 lecture links and 13 book claims | 19, plus one bug in a code listing | 7 |
| [04 Safety and security](04-safety-and-security/README.md) | 172 links against 130 transcript blocks, plus slides and two papers | 19 | 8 |
| [05 Frameworks and multi-agent](05-frameworks-and-multi-agent/README.md) | 139 statements and 19 slide figures | at least 7 | 6 |
| [06 Frontier applications](06-frontier-applications/README.md) | about 198 links | several, in chapters 01 to 05 | 3 |
| [07 ML in production](07-ml-in-production/README.md) | about 315 statements against the book | 11 | 8 |
| [08 Quality assurance](08-quality-assurance/README.md) | about 344 statements against the book | 4 wrong, several others narrowed to what the book says | 11 |
| [09 Efficient deep learning](09-efficient-deep-learning/README.md) | about 228 statements and figures | several, including two listings whose real output contradicted the text | 9 |
| [10 LLM internals](10-llm-internals/README.md) | 268 links and about 20 other claims | 10 attributed statements, plus wrong answers and exercises | 12 |

In total: about 2,100 attributed statements re-checked and more than 130 corrected, 81 diagrams added.

The second review also found defects that no check for sources can catch:

- **Self-check answers.** In many chapters the correct option was the first or the second for most questions, so length or position gave the answer away. Options are now reordered and every answer was re-derived. A few answers were wrong.
- **Exercises.** Some could not be done with what the chapter gives: a step was missing, or no configuration fits the stated hardware. They now say what to do, or give a configuration that works.
- **Terms.** More than 150 terms were used before they were defined. Each is now defined at first use.
- **Listings.** Running the code showed that in a few chapters the text described an output the code does not produce. The text now reports the real output.

## Lecture guides

The chapters cite a lecture where they make a claim taken from it. They do not read a lecture from end to end, and a count on 2026-11-25 found that they cited only about a third of the lectures' two-minute blocks. From that day on, one guide was written for each of the 77 lectures, in [`lectures/`](lectures/README.md). A guide maps the whole lecture in parts of a few minutes and says for each part where this book teaches the same thing.

| Course | Guides | Parts | Parts no chapter teaches |
|---|---|---|---|
| [UC Berkeley LLM Agents MOOC, Fall 2024](lectures/README.md#uc-berkeley-llm-agents-mooc-fall-2024) | 12 | 173 | 15 |
| [UC Berkeley Advanced LLM Agents MOOC, Spring 2025](lectures/README.md#uc-berkeley-advanced-llm-agents-mooc-spring-2025) | 12 | 175 | 14 |
| [UC Berkeley Agentic AI MOOC, Fall 2025](lectures/README.md#uc-berkeley-agentic-ai-mooc-fall-2025) | 12 | 162 | 15 |
| [MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024](lectures/README.md#mit-65940-tinyml-and-efficient-deep-learning-computing-fall-2024) | 23 | 410 | 21 |
| [Stanford CS336 Language Modeling from Scratch, Spring 2026](lectures/README.md#stanford-cs336-language-modeling-from-scratch-spring-2026) | 18 | 287 | 4 |
| Total | 77 | 1,207 | 69 |

In 69 of the 1,207 parts, 6%, the guide's writer found no chapter section that teaches the same thing, and the guide explains the part itself. That is the measure of how much of the lectures the chapters do not cover. It is largest for the MIT course, where 21 of 410 parts are explained only in the guide, and smallest for CS336, with 4 of 287. The count rests on each writer's judgement of what counts as the same thing, so read it as an estimate.

An automatic check runs on every guide before it is published. For each guide it confirms that:

- the parts start at the first minute and end at the lecture's last minute, with no gap or overlap between them;
- every part heading links to the second of the video that the heading names;
- every link to a chapter section points to a section that exists;
- a part that no chapter teaches has at least 60 words;
- no run of eight or more words is copied from the lecture, outside quotation marks.

The check caught wrong seconds, links to sections that do not exist, copied phrases and parts that were too short, guide after guide. They were corrected before publication.

What the check cannot see is whether a guide understood the lecture correctly. Each guide was written by an AI writer who read the lecture once, through the machine transcript. On 2026-11-26 a second reading took place, again by AI and not by a person:

- **Numbers and names, all 77 guides.** Every number and every capitalized name in each guide was compared mechanically with the lecture's text and slides. Of the numbers, 57 were not found in that form; read one by one, 53 were forms the machine made (a number spoken in words, a value derived from two others) and 4 were wrong and were corrected. Every name was found.
- **Second reading, all 77 guides from beginning to end.** An AI reviewer read the guide and then the whole lecture and corrected every statement the lecture does not support. Each needed between 2 and 20 corrections: numbers the lecturer gave differently, claims never made, a conclusion of the guide presented as the lecturer's statement, content filed under the wrong part, and part boundaries that cut a thought in two. A sample of 29 corrections was re-read against the lecture by hand and all held. The reviewer sometimes replaced a well-known name that the machine garbles (Hugging Face, FLAML, ICLR) by a vague description; these were restored by hand.
- **The chapters checked against the corrected claims.** A claim that one reader of a lecture got wrong, another reader of the same lecture may have got wrong too. For every claim corrected in a guide, the chapters were searched for the same claim and the passage was re-read against the lecture: for the guides of all four courses, 387 changed claims were checked and 45 sentences in 26 chapters corrected.
Names are the weakest point: the machine transcript can garble a name, so a guide prefers the names as the lecture's slides spell them and otherwise says "the lecturer". If a guide and the lecture disagree, the lecture wins.

**Moved into the chapters, 2026-11-26.** By the evening of 2026-11-26 forty-two chapters, in every part that was written from lectures, had been enlarged this way, and the parts that only a guide teaches had fallen from 231 to 69 of 1,207. The added text has not had the reading that the rest of the book has had. In the first nine enlarged chapters that were read a second time against the lectures, passages were corrected in six of them and none were needed in three: numbers the lecturer gave differently, a claim he had not made, a passage copied in eight or more words, and once a chapter that had grown past its word limit. Those nine are corrected; the other thirty-three enlarged chapters are being read the same way, and until that is done their added passages count as unchecked.

## Glossary

Each of the 1,091 rows of [GLOSSARY.md](GLOSSARY.md) was read against the chapter it links to on 2026-11-25. 12 definitions were corrected, 7 links moved to the chapter that defines the term better, 13 duplicate rows merged, 16 rows removed and 24 rows added. The glossary now has 1,086 terms.

## Reading site

The same files are published as a website, <https://acailic.github.io/ai-engineer-path/>, rebuilt on every push by [`tools/site/build.py`](tools/site/build.py). The build stops if an internal link or a link to a section is broken. Every page has a read-aloud button that uses the speech synthesis built into the browser; no account, key or network service is involved. On 2026-11-25 the site was checked in one desktop browser at full width and at phone width. The voices offered differ between browsers and devices, and only one browser was tried.

## What is not verified

- **The capstones.** The five capstones in part 11 were specified, not carried out. Their hours and costs, and those of the roadmap, are estimates.
- **Engineering judgment.** It is marked in the chapters as this repository's own and was not checked against a source.
- **General knowledge.** Topics that no transcript covers are explained from general knowledge.
- **Fast-moving facts.** Model names, prices, APIs, products and regulation are true as of the date each chapter gives, usually the lecture date or 2026-11-24.
- **External links.** Links other than those named above were not all reopened, and YouTube links were not checked. The Fall 2025 Berkeley course page address in [SOURCES.md](SOURCES.md) returned an HTTP 404 error on 2026-11-24.
- **The transcripts.** They are machine-made and can garble names. The lectures are the authority: a chapter that disagrees with its source is wrong.
- **The lecture guides.** they were read a second time only by AI, never by a person.
- **Coverage of the book.** The chapters of parts 07 and 08 were checked statement by statement against the book *Machine Learning in Production*, and their coverage was reviewed from 2026-11-26. A word-overlap count had flagged 82 of its 399 sections as possibly reflected only in part; these sections were read against the chapters, in 10 groups. All ten groups are finished, and the sections a reader needs were added to the chapters; two short proposed texts for the chapters on models-to-systems and on goals did not fit under the 3,500-word limit and are not in the course. The review also found 35 sentences in 19 chapters that repeated the book's wording without quotation marks; all were rephrased, and the longest passage a chapter now shares with the book outside quotation marks is a paper title.

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
