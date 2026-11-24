# Part 07: ML in Production: From Idea to Deployed System

Take an ML idea through requirements, architecture, deployment and operations with a software engineer's discipline, and apply the same thinking to LLM and agent systems.

This part is written for a software engineer who has never worked with ML. You do not need to train a model to read it. You need the habit of asking what a component assumes, what happens when it fails, and how you would know.

## What you can do after this part

- Say no to ML when a rule would do, with a baseline and a cost table as evidence.
- Write goals, measures and requirements for a feature that contains a model.
- Run a mistake analysis and design the system so that a wrong prediction does not become an incident.
- Draw the architecture and put numbers on latency, cost and accuracy before choosing a model.
- Deploy, update, monitor and switch off a model without a hero effort.

## Chapters

Read in order the first time. Each chapter builds on the one before.

| # | Chapter | Level | Reading | What you can do afterward |
|---|---|---|---|---|
| 01 | [From Models to Systems and Products](01-from-models-to-systems-and-products.md) | Foundation | 25 min | Map the system around a model: goal, components, interfaces, consequences |
| 02 | [When to Use ML, and When Not To](02-when-to-use-ml-and-when-not-to.md) | Foundation | 20 min | Decide with a measured baseline and a full cost table |
| 03 | [Goals and Requirements](03-goals-and-requirements.md) | Practitioner | 25 min | Write layered goals, one precise measure each, and requirements that separate world from software |
| 04 | [Planning for Mistakes](04-planning-for-mistakes.md) | Practitioner | 30 min | Run a mistake analysis with FMEA, fault trees and two checklists |
| 05 | [Architecture for ML Systems](05-architecture-for-ml-systems.md) | Practitioner | 20 min | Draw components, interfaces and decision records |
| 06 | [Quality Attributes of ML Components](06-quality-attributes-of-ml-components.md) | Practitioner | 25 min | Trade latency, cost and accuracy on evidence, not opinion |
| 07 | [Deploying a Model](07-deploying-a-model.md) | Practitioner | 30 min | Choose how a model is served, where it runs and how it is updated |
| 08 | [Automating the Pipeline](08-automating-the-pipeline.md) | Practitioner | 25 min | Turn a notebook into a pipeline of tested stages |
| 09 | [Scaling the System](09-scaling-the-system.md) | Practitioner | 15 min | Do the capacity arithmetic before buying anything |
| 10 | [Planning for Operations](10-planning-for-operations.md) | Practitioner | 30 min | Pass a launch review with objectives, monitors, rollback and an incident plan |

Three shorter routes:

- **Before a launch.** Read [04](04-planning-for-mistakes.md) and [10](10-planning-for-operations.md), with [03](03-goals-and-requirements.md) for the measures. These two chapters are the ones you will reuse most.
- **Building on an LLM API.** Read [01](01-from-models-to-systems-and-products.md), [02](02-when-to-use-ml-and-when-not-to.md), [05](05-architecture-for-ml-systems.md), [04](04-planning-for-mistakes.md) and [10](10-planning-for-operations.md).
- **Deciding whether to build at all.** Read [02](02-when-to-use-ml-and-when-not-to.md) and [06](06-quality-attributes-of-ml-components.md).

## How the chapters are built

Every chapter uses the same small product: a feature that routes support tickets to the team that can solve them. The model changes from a keyword rule to a classifier to an LLM as the chapters need it.

- **Worked examples** are short Python programs. They need Python 3.10 or newer and the standard library only.
- **No example calls a paid API.** Two stretch goals suggest calling one and say what it costs.
- **Each chapter has a section called "What changes for LLM and agent systems".** It translates the chapter's idea to products built on large language models and to agents, programs that let a model call tools.
- **Each chapter ends with an exercise** that has a clear deliverable and a condition for being done, plus recall questions with answers.

## Background you may want

If the words *model*, *training* and *prediction* are new, chapter 01 defines them. For more, read [Machine Learning in a Nutshell](../01-foundations/01-machine-learning-in-a-nutshell.md). This part does not cover how models learn. Parts 01 and 10 do.

## Source

The part is synthesized from Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapters 1, 2 and 4 to 13: [free online edition](https://mlip-cmu.github.io/book/). The book is licensed CC BY-NC-ND 4.0. Every chapter paraphrases and links to the chapters of the book it draws on, and was checked against their full text.

Kästner's own running examples are a transcription service, a fraud detector and smart glasses. This part retells three of them where they are the clearest illustration: the toaster, the legal chatbot and the smart glasses. Everything else uses the support-ticket feature.

## Related parts

- [Evaluation](../03-evaluation/01-evaluation-is-the-product.md): the evaluation set that stands in for a specification.
- [Safety and Security](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md): threat modeling and prompt injection.
- [Quality Assurance](../08-quality-assurance/09-testing-and-experimenting-in-production.md): testing in production and canary experiments.
- [Efficient Deep Learning](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md): serving LLMs efficiently.
- [Professional Practice](../11-professional-practice/07-checklists.md): how to keep checklists usable.
