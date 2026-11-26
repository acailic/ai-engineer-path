# 08. Staying Current

**Level:** Foundation · **Reading time:** 20 min · **Exercise:** 30 min
**Prerequisites:** None.

> **In one sentence:** After this chapter you have a short list of primary sources to follow, five questions to ask of any paper or model release, and a test for telling an idea that will last from one that will not.

## Why this matters

Everything in this repository is a study guide to recorded material. The lectures were recorded between September 2024 and June 2026 ([SOURCES](../SOURCES.md)). Model names, scores, prices and products in the chapters were true on the date of their lecture. They will not stay true.

The ideas decay far more slowly. Nobody can follow everything. The skill is to spend attention where it keeps its value.

## The core idea

Sort what you read into three layers. Budget attention by how fast a layer changes.

| Layer | Examples from this course | What to do with it |
|---|---|---|
| Durable ideas | Build the evaluator before the features. No single defense holds. Model size is parameters times bits. Profile before optimizing. | Learn it once. These are the chapters |
| Methods | Post-training recipes. Quantization recipes. Schemes for parallel training | Learn the current one when you need it, and re-check the chapter |
| Facts | Which model scores best. Prices. The status of a framework. Benchmark records | Never memorize. Look it up, and note the date |

The examples are illustrative, not measurements. The boundaries between the layers are this chapter's rule of thumb.

Two facts from the chapters show why dates matter. [Building Your Own](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) lists what one GPU cost at several providers, with the date of the price. [AutoGen: Conversation Programming](../05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) records AutoGen as archived as of November 2026. Both were worth knowing on their date. Neither will be worth knowing for long.

## How it works, step by step

### 1. Follow four primary sources, not feeds

| Source | What it is | Editions this course uses |
|---|---|---|
| UC Berkeley MOOCs on LLM agents and agentic AI, taught by Dawn Song with guest lecturers | Lectures on agents, evaluation, safety, multi-agent systems and applications | Fall 2024, Spring 2025, Fall 2025 |
| *Machine Learning in Production: From Models to Products*, Christian Kästner (CMU, MIT Press, 2025) | A book and a course on ML inside products | The 2025 edition. Course 17-645 / 11-695 |
| MIT 6.5940, TinyML and Efficient Deep Learning Computing, Song Han | Lectures on pruning, quantization, distillation, TinyML and efficient inference | Fall 2024 |
| Stanford CS336, Language Modeling from Scratch, Percy Liang and Tatsunori Hashimoto | Lectures and five assignments on building a language model | The offering whose schedule runs from March 30 to June 3 |

The addresses are in [SOURCES](../SOURCES.md). Three notes. Where a page was opened, the date is given.

- **Later editions.** Berkeley's center ran three editions in two years, the three this course uses. That is a pattern, not a promise. Look for the next one on its site.
- **CS336.** The course page ([cs336.stanford.edu](https://cs336.stanford.edu/), opened 2026-11-24) names the two instructors, lists lectures from March 30 to June 3 and five assignments, and announces no later offering.
- **An address that fails once.** The Fall 2025 Berkeley course page address listed in SOURCES returned an HTTP 404 error on 2026-11-24 and loaded the next day. When a link fails, try again later, then search for the course title.

### 2. Follow the lecturers and their labs

[SOURCES](../SOURCES.md) lists every lecturer with the affiliation shown on the course page. For each person whose work a chapter returns to, find their laboratory page or publication list once, and save it. Five that this course cites again and again are Dawn Song (UC Berkeley), Song Han (MIT), Percy Liang (Stanford), Christian Kästner (CMU) and Graham Neubig (CMU).

This chapter gives no personal addresses. None was opened while it was written. Start from the course pages, which name each speaker.

### 3. Keep a short list of benchmarks and standards

A benchmark is worth following only if you know what its score means. Each of these has a chapter that explains it:

- **SWE-bench**, real GitHub issues scored by the tests added with each fix ([Coding Agents](../02-building-agents/07-coding-agents.md)). The green agent case study shows how much a quality review can change its picture ([the case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)).
- **WebArena, Mind2Web and OSWorld**, for web and computer use ([Multimodal Agents: Web and Computer Use](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md)).
- **τ-bench**, for tool-using agents that talk to customers ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md)).
- **AgentBeats**, the platform that hosts assessments between agents ([the case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)).

When a benchmark number appears, ask three things. Is the benchmark saturated, so that it no longer separates systems? Is its test data contaminated, present in the training data of the model? Does the score reflect real use? [Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md) and [Evaluating Language Models](../10-llm-internals/09-evaluating-language-models.md) explain each.

Standards and lists worth knowing about, with the chapter that places them:

- The OWASP Top 10 for LLM Applications (2025) and the OWASP list for agentic applications (2026) ([Threat Modeling LLM Applications and Agents](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md)).
- The Model Context Protocol, a standard for connecting models to tools and data ([Agent Infrastructure: Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md)).
- The Agent2Agent protocol, for agents that exchange tasks ([the case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)).
- Laws and standards for AI, on a dated map ([Policy, Governance and Standards](../04-safety-and-security/09-policy-governance-and-standards.md)). Its table lists what could be verified as of November 2026. Check the current text before you rely on an entry.

### 4. Read a paper or a model release with five questions

1. **What is claimed, and is it demonstrated or expected?** [What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md) marks each frontier claim one way or the other. Do the same.
2. **Against what baseline?** An accuracy means little alone. Ask for the baseline and the reduction in error ([Measuring Model Quality](../08-quality-assurance/02-measuring-model-quality.md)).
3. **How many runs, and what are the error bars?** Answers are sampled, so a difference without a standard error is not evidence ([Why LLM Outputs Are Noisy](../01-foundations/07-why-llm-outputs-are-noisy.md), [Statistics for Evals](../03-evaluation/05-statistics-for-evals.md)).
4. **Is the evaluation valid?** Held-out data, no contamination, a benchmark that is not saturated, tasks like real use ([Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md)).
5. **Who is speaking, and what can they show?** A vendor reports on its own product. [Agents in the Enterprise](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) builds on lectures by speakers from Google and ServiceNow. Access bounds evaluation: API access, open weights and open source allow different questions ([Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md)).

For a model release, add three. What does the model card state, and what does it leave out ([Deploying a Model](../07-ml-in-production/07-deploying-a-model.md))? What is the license? What is withheld: the data, the recipe, or both?

Then do the one thing that beats reading. Run your own evaluation set on the new model, and let the regression gate speak before the announcement does ([Evals in Production](../03-evaluation/07-evals-in-production.md)).

### 5. Tell a durable idea from a fashion item

An idea is likely to last when it passes these five tests.

1. **It survives a change of model.** Evaluate on held-out data. That held for classical models and holds for LLMs ([Measuring Model Quality](../08-quality-assurance/02-measuring-model-quality.md)). A prompt trick that stops working with the next model does not pass.
2. **You can say why it works.** Quantization saves memory because model size is parameters times bits ([Quantization](../09-efficient-deep-learning/04-quantization.md)).
3. **More than one source states it.** "There is no one silver bullet" is Dawn Song's caution in every term she taught the material ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md)). Kästner reaches the same place from the other side: build the rest of the system so that a wrong prediction causes little harm ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md)).
4. **It has a number that can go down.** The attack success rate, pass^k, the cost per attempt. A claim with no metric cannot be tracked, so it cannot be corrected.
5. **It is an old engineering principle in new clothes.** Least privilege goes back to Saltzer and Schroeder in 1975, as the defenses chapter notes. FMEA and fault trees come from safety engineering. The rehearsed rollback is ordinary operations.

A fashion item fails most of the tests: the name of a framework, a leaderboard record, a single demo, a technique named before anyone measured it. A fashion can become durable. Give it the five tests again, a year later.

### 6. Keep a routine

- **Weekly, 30 minutes.** One primary source: a lecture, a paper or a release note, read with the five questions.
- **Monthly.** Run your evaluation set on the model you use. Write down the date and the numbers.
- **On every release of a model you depend on.** Run the regression gate before you read the post about it.
- **One notes file.** Every line has a date and an address.
- **Once a quarter.** Delete the notes about facts. Keep the notes about ideas.

## Worked example

Three readings from this repository's own record. Each is a habit.

1. **Read the definition, not the label.** A Berkeley slide prints its all-runs reliability metric as "pass@k" while defining pass^k. This course keeps the two apart ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md)).
2. **Check the source passage.** [AI for Cyber Defense and Vulnerability Detection](../04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) marks its Project Zero links as taken from the lecture slides and not opened for the chapter. Such a link is a lead, not a fact.
3. **Date the status.** Part 05 records AutoGen as archived as of November 2026 ([AutoGen: Conversation Programming](../05-frameworks-and-multi-agent/02-autogen-conversation-programming.md)). Before you build on any framework, check its repository on the day you decide.

Where a source was not opened, a chapter says so in its Sources list. Read that list before you rely on a number in it.

## What the practitioners say

- **Rules should rest on measured risk.** Dawn Song's case for evidence-based AI policy is that measuring the risk is itself a research job ([Policy, Governance and Standards](../04-safety-and-security/09-policy-governance-and-standards.md)). Read an announcement the same way. Ask for the measurement.
- **Access decides what an evaluation can show.** Percy Liang separates API access, open weights and open source by the questions each allows ([Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md)).
- **Each part keeps its own outlook.** [Course Summary and Outlook](../09-efficient-deep-learning/17-course-summary-and-outlook.md) places every efficiency technique on one map, adds a six-step procedure, and offers a routine for keeping up with a fast-moving field. The routine is that chapter's own, and it says so.
- **Building is what lasts.** The CS336 handouts allow AI tools for explanations and forbid them for implementation, because a tool can do the assignment and leave no learning behind ([Building Your Own](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md)). New tools do not change that.

## Pitfalls

1. **Chasing every release.** Fix: one primary source a week.
2. **Summaries of summaries.** Fix: go to the paper, the lecture or the model card.
3. **A leaderboard difference without error bars.** Fix: the five questions.
4. **A vendor's benchmark taken as neutral.** Fix: ask who is speaking, and run your own set.
5. **Undated notes.** Fix: a date and an address on every line.
6. **A name mistaken for an idea.** Fix: read the definition.
7. **Letting a tool do the learning.** Fix: use AI to explain, never to implement.
8. **Treating this repository as the authority.** The courses and the book are. If a chapter and its source disagree, the source wins.

## Try it

Build your sources file in 30 minutes.

1. Four course pages, each with the date you checked it.
2. One page for each lecturer you cite.
3. Three benchmarks, each with the date of its latest results.
4. One dated entry: a paper or a release, read with the five questions.

**Deliverable:** the sources file.

**You are done when** every line has an address and a date, and the entry answers all five questions or says "not stated" for each.

**Stretch goal:** a quarter from now, re-read the entry and mark which answers changed.

## Key takeaways

- Sort what you read into durable ideas, methods and facts. Spend attention in that order.
- Follow four primary sources, their later editions, and the people behind them.
- A benchmark number means nothing until you know whether it is saturated, contaminated and realistic.
- Read any paper or release with five questions: the claim, the baseline, the error bars, the validity, the speaker.
- An idea lasts when it survives new models, has a mechanism, appears in several sources, has a metric, and reduces to an old principle.
- Date everything. This repository included.

## Self-check

1. What are the three layers, and which one should never be memorized?
2. What three questions should you ask about any benchmark number?
3. What are the five questions to ask of a paper or a model release?
4. What single action beats reading a model announcement, and why?
5. Name three of the five tests for a durable idea.
6. Why does this chapter give no personal addresses for the lecturers?

<details><summary>Show answers</summary>

1. Durable ideas, methods and facts. Facts should never be memorized: they are looked up, with the date.
2. Is the benchmark saturated? Is its data contaminated? Does it reflect real use?
3. What is claimed, and is it demonstrated or expected? Against what baseline? How many runs, and what error bars? Is the evaluation valid? Who is speaking, and what can they show?
4. Running your own evaluation set on the new model, with the regression gate. It measures the model on your tasks, which no announcement does.
5. Any three of: it survives a change of model; you can say why it works; more than one source states it; it has a number that can go down; it is an old engineering principle in new clothes.
6. A page is cited only if it was opened, with its date. None of the lecturers' pages was opened while the chapter was written, so the chapter sends the reader to the course pages instead.

</details>

## Sources

- [SOURCES](../SOURCES.md): every lecture, its speakers and its link. Course addresses as listed there: Berkeley [Fall 2024](https://rdi.berkeley.edu/llm-agents/f24), [Spring 2025](https://rdi.berkeley.edu/adv-llm-agents/sp25) and [Fall 2025](https://rdi.berkeley.edu/agentic-ai/f25); Kästner's [book](https://mlip-cmu.github.io/book/) and [course](https://mlip-cmu.github.io/); MIT [6.5940](https://hanlab.mit.edu/courses/2024-fall-65940); Stanford [CS336](https://cs336.stanford.edu/).
- Web pages opened for this chapter: [cs336.stanford.edu](https://cs336.stanford.edu/), read on 2026-11-24. The Berkeley Fall 2025 address above returned an HTTP 404 error on 2026-11-24 and loaded when opened again on 2026-11-25 and on 2026-11-26. The other addresses were not checked.
- [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md), [Statistics for Evals](../03-evaluation/05-statistics-for-evals.md), [Evals in Production](../03-evaluation/07-evals-in-production.md), [the green agent case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) (part 03)
- [Threat Modeling LLM Applications and Agents](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md), [Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md), [AI for Cyber Defense and Vulnerability Detection](../04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md), [Policy, Governance and Standards](../04-safety-and-security/09-policy-governance-and-standards.md) (part 04)
- [AutoGen: Conversation Programming](../05-frameworks-and-multi-agent/02-autogen-conversation-programming.md), [Agent Infrastructure: Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md), [Agents in the Enterprise](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) (part 05)
- [Multimodal Agents: Web and Computer Use](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md), [Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md), [What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md) (part 06)
- [Why LLM Outputs Are Noisy](../01-foundations/07-why-llm-outputs-are-noisy.md) (part 01), [Coding Agents](../02-building-agents/07-coding-agents.md) (part 02), [Measuring Model Quality](../08-quality-assurance/02-measuring-model-quality.md) (part 08)
- [Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md), [Deploying a Model](../07-ml-in-production/07-deploying-a-model.md) (part 07), [Quantization](../09-efficient-deep-learning/04-quantization.md), [Course Summary and Outlook](../09-efficient-deep-learning/17-course-summary-and-outlook.md) (part 09), [Evaluating Language Models](../10-llm-internals/09-evaluating-language-models.md), [Building Your Own: A Roadmap Through the Assignments](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) (part 10)

## Next

→ You have reached the last chapter. Return to the [roadmap](../ROADMAP.md) to choose what to do with it, or start with [How to Ship an LLM Feature End to End](01-how-to-ship-an-llm-feature-end-to-end.md).
