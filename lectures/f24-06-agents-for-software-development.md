# Lecture guide: Agents for Software Development

**Lecturer:** Graham Neubig (CMU) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 6 · **Length:** 1:02:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=f9L9Fkq-8K4) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/neubig24softwareagents.pdf)
**Chapters that cite this lecture:** [01. The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) · [02. Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md) · [03. Planning, Search and Decision-Making](../02-building-agents/03-planning-search-and-decision-making.md) · [07. Coding Agents](../02-building-agents/07-coding-agents.md) · [08. Training Models for Agentic Tasks](../02-building-agents/08-training-models-for-agentic-tasks.md)

> **In one sentence:** Graham Neubig shows what a coding agent must do beyond writing code (find the right files, plan, recover from errors, stay safe) and how benchmarks measure it.

## Before you watch

Read [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) first; it teaches the agent loop the lecture assumes. Read [Coding Agents](../02-building-agents/07-coding-agents.md) afterwards: it follows the lecture closely.

## The lecture, part by part

### [0:00–3:46](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=0) Why software, and a developer's time

Graham Neubig, a professor at CMU and chief scientist at All Hands AI, maintains the open-source coding agent OpenHands. His motivation is a question: if everyone could write software quickly, what would they do? He cites Marc Andreessen's 2011 essay on software spreading through every industry and notes that two of that year's Nobel Prizes went to people who wrote software. A 2019 Microsoft study sets the scope: developers spend 15% of their day coding and 36% communicating.
**In this book:** nothing beyond this guide; nearest: [Coding Agents › Why this matters](../02-building-agents/07-coding-agents.md#why-this-matters).

### [3:46–9:32](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=226) From completion to agents

He grades automation like self-driving cars, from hand-written code up to a system that solves a whole development task. In a demo, OpenHands adds unit tests on request, pushes a branch and leaves review to a person; a GitHub study of 95 developers found Copilot users finishing 56% faster.
**In this book:** [Coding Agents › Why this matters](../02-building-agents/07-coding-agents.md#why-this-matters) · [Coding Agents › OpenHands](../02-building-agents/07-coding-agents.md#openhands).

### [9:32–12:33](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=572) Challenges and environments

Six challenges organize the talk: the environment, the observation and action space, code generation, file localization, planning with error recovery, and safety. Developers also work in task boards, documents and chat tools, yet test environments cover almost only coding.
**In this book:** [Coding Agents › How it works, step by step](../02-building-agents/07-coding-agents.md#how-it-works-step-by-step) · [Coding Agents › 1. Environment](../02-building-agents/07-coding-agents.md#1-environment).

### [12:33–17:45](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=753) Coding benchmarks

HumanEval and MBPP ask for a small function from a docstring, like an interview puzzle: necessary, not sufficient. CoNaLa and ODEX use Stack Overflow answers, ARCADE notebooks. SWE-bench gives a real GitHub issue and repository, scored by the tests added with the fix; it keeps only projects whose fixes added tests, so it leans toward bug fixes.
**In this book:** [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated).

### [17:45–21:19](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1065) Metrics and dataset leakage

The common metric is pass@k: the chance that at least one of k samples passes the tests. Public code leaks into training data: new ARCADE notebooks score far lower than published ones, and some models score high on HumanEval but low on the newer LiveCodeBench.
**In this book:** [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated) · [Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [21:19–22:32](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1279) Multimodal coding models

Design2Code, a data set from Stanford, shows a model an image of a web page and asks for the code that renders it; a multimodal version of SWE-bench had appeared only days before the lecture. Scoring compares screenshots, not text: a high-level score uses visual embeddings of the whole page, and a low-level score counts how many individual elements were reproduced. A coding model can therefore start from what it sees, not only from a written specification.
**In this book:** nothing beyond this guide; nearest: [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated).

### [22:32–30:18](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1352) Code as the action space

CodeAct replaces one tool call per step with programs: to compare phone prices in four countries, the model writes one loop instead of some fifteen calls. SWE-Agent adds commands to view a window of lines and to edit a range; OpenHands combines the two, so every action is code that can call those commands.
**In this book:** [Coding Agents › 2. Action space](../02-building-agents/07-coding-agents.md#2-action-space) · [Coding Agents › The agent-computer interface](../02-building-agents/07-coding-agents.md#the-agent-computer-interface).

### [30:18–37:08](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1818) Training code models

Nearly all serious language models now train on code, partly because code also improves general reasoning; The Stack 2 is an open pre-training data set with per-file license checks, dominated by a few popular languages. Infilling suits editing: a coherent span is masked and moved to the end of a document, and the model generates it. Because code is long, models also need context extension: pre-trained on roughly 4,000-token chunks, they generalize badly beyond that, since the angles of RoPE, the usual positional encoding, exceed the trained range. Scaling the angles back, uniformly or only at low frequencies, restores long inputs.
**In this book:** nothing beyond this guide; nearest: [Pre-training data](../01-foundations/02-how-large-language-models-are-trained.md#pre-training-data).

### [37:08–44:53](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2228) Context and file localization

A published account of Copilot's prompt shows how much context a completion model packs in: text around the cursor and the 20 most recently used files. Localization, finding the files a request is about, may be the largest open problem; four strategies are letting the user name the files, giving the agent a search tool, mapping the repository in advance (Aider) and searching in stages (Agentless).
**In this book:** [Coding Agents › 3. Context](../02-building-agents/07-coding-agents.md#3-context) · [Coding Agents › What the practitioners say](../02-building-agents/07-coding-agents.md#what-the-practitioners-say).

### [44:53–46:03](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2693) Retrieval-augmented code generation

The last strategy retrieves similar code with an embedding model and generates from what it found. Documentation can be retrieved as well and sometimes serves better than code, because a request in English and its solution in Python may look unrelated to a retriever. No agent system uses retrieval well yet, in his view: deciding when to retrieve during a task remains an unsolved problem.
**In this book:** nothing beyond this guide; nearest: [C. Retrieval: the standard pipeline](../02-building-agents/04-memory-and-knowledge-for-agents.md#c-retrieval-the-standard-pipeline).

### [46:03–51:51](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2763) Planning and error recovery

Many top leaderboard systems hard-code their process: Agentless localizes, generates several patches, validates them and keeps one that passes, which is cheap but inflexible. Plans often rest on wrong assumptions, so an executor must be able to send a failed plan back, as CoAct does, and one leading model retries the same failed fix until it runs out of turns.
**In this book:** [Coding Agents › What the practitioners say](../02-building-agents/07-coding-agents.md#what-the-practitioners-say) · [Planning, Search and Decision-Making › How it works: six patterns](../02-building-agents/03-planning-search-and-decision-making.md#how-it-works-six-patterns).

### [51:51–58:05](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=3111) Safety

Harm comes first by accident: an agent asked to commit pushed to the main branch, and one told to make tests pass deleted them. Three mitigations come from software security: OpenHands runs every action in a Docker container; fine-grained GitHub tokens give only the permissions needed (least privilege); and each action is audited before it runs and blocked if harmful.
**In this book:** [Coding Agents › 6. Safety](../02-building-agents/07-coding-agents.md#6-safety) · [6. Enforce least privilege on every action](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md#6-enforce-least-privilege-on-every-action).

### [58:05–1:02:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=3485) Conclusion and future directions

Copilots already pay off, and in some of his repositories an agent drafted half of the commits. Three directions remain: agentic training (following formats, planning, recovering from errors), evaluation of human-in-the-loop work, and tasks beyond coding, where almost no benchmarks exist.
**In this book:** [Coding Agents › What the practitioners say](../02-building-agents/07-coding-agents.md#what-the-practitioners-say) · [Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

## What to take away

- Coding is 15% of a developer's day; the prize is an agent that finishes a whole task.
- Finding the right files is the hardest open step; maps, staged search and retrieval each solve part of it.
- Benchmarks built from public code lean toward bug fixes and are contaminated by training data.
- Sandbox, least-privilege credentials and auditing each action before it runs are the three safety measures.

## Sources

- Graham Neubig, "Agents for Software Development", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=f9L9Fkq-8K4).
- Slides: [Agents for Software Development](https://rdi.berkeley.edu/llm-agents-mooc/slides/neubig24softwareagents.pdf).
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
