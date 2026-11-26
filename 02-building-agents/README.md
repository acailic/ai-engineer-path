# Part 02: Building Agents

Design and build a single-agent system: the agent loop, tools, planning, memory, pipelines, and an engineer's view of how agent system designs have evolved.

This part is for a software engineer who has finished [Part 01](../01-foundations/01-machine-learning-in-a-nutshell.md) and can write Python but has never built an agent. By the end you can sit down and build a small, well-structured single-agent system and explain every design decision in it.

## What you will be able to do

- Write a working agent loop in plain Python, without a framework, and test it without an API key.
- Design tools whose schemas, descriptions and error messages a model can use.
- Choose how much deliberation an agent needs before each action, and when to hand a sub-problem to a solver.
- Decide what an agent keeps in its context, what it stores outside, and how to compact a long run.
- Write a language-model pipeline as a short declarative program and tune it with a metric and an optimizer.
- Read a coding agent's design and carry its lessons to agents in other domains.
- Explain what changes when a model is trained for agent work.

## Chapters

| # | Chapter | Level | Reading | Exercise |
|---|---|---|---|---|
| 01 | [The Anatomy of an Agent](01-the-anatomy-of-an-agent.md) | Practitioner | 30 min | 60 min |
| 02 | [Tool Design and Function Calling](02-tool-design-and-function-calling.md) | Practitioner | 30 min | 60 min |
| 03 | [Planning, Search and Decision-Making](03-planning-search-and-decision-making.md) | Practitioner | 30 min | 60 min |
| 04 | [Memory and Knowledge for Agents](04-memory-and-knowledge-for-agents.md) | Practitioner | 30 min | 60 min |
| 05 | [Compound AI Systems and DSPy](05-compound-ai-systems-and-dspy.md) | Practitioner | 30 min | 60 min |
| 06 | [How Agent System Designs Evolve](06-how-agent-system-designs-evolve.md) | Practitioner | 15 min | 30 min |
| 07 | [Coding Agents](07-coding-agents.md) | Practitioner | 30 min | 90 min |
| 08 | [Training Models for Agentic Tasks](08-training-models-for-agentic-tasks.md) | Professional | 30 min | 60 min |

## How to read this part

- **In order:** 01 to 05 build one system piece by piece, then 06 zooms out and 07 and 08 go deep.
- **Short on time:** read 01, 02 and 04. They cover the loop, the tools and the context, which is where most first agents fail.
- **Survey first:** 06 is short and needs only 01. Read it early if you want the map before the details.
- **Hardest chapter:** 08 is the only chapter at Professional level. It assumes the post-training basics from [Part 01](../01-foundations/03-from-base-model-to-assistant-post-training.md).

A project to carry through the part: an agent over a folder of notes.

1. Build the loop with a scripted model ([01](01-the-anatomy-of-an-agent.md)).
2. Add three tools: list, search and read ([02](02-tool-design-and-function-calling.md)).
3. Compare a reactive policy with a plan-first one ([03](03-planning-search-and-decision-making.md)).
4. Add a notes file and compaction ([04](04-memory-and-knowledge-for-agents.md)).
5. Rewrite the question-answering step as a declarative program and optimize it ([05](05-compound-ai-systems-and-dspy.md)).

## What this part does not cover

- **Evaluation** of agents and LLM components: [Part 03](../03-evaluation/01-evaluation-is-the-product.md).
- **Security**, prompt injection and threat modeling: [Part 04](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md).
- **Frameworks, multi-agent systems, sandboxes and protocols:** [Part 05](../05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md).

## About the examples

All examples are plain Python and appear in full inside the chapters. Four run offline with no API key: the agent loop with a scripted model (01), the retrieval example (04), the agent-computer interface (07) and the corridor training loop (08). Where a chapter shows how to connect a real model, the adapter is illustrative and calls a paid API; the chapter says so and gives an estimated cost. Provider APIs change, so check the current documentation before you rely on a code shape.

## Sources

The part is synthesized from six lectures of the UC Berkeley LLM Agents and Agentic AI MOOCs:

- Graham Neubig, "Agents for Software Development" (Fall 2024)
- Omar Khattab, "Compound AI Systems and the DSPy Framework" (Fall 2024)
- Yuandong Tian, "Towards a Unified Framework of Neural and Symbolic Decision Making" (Fall 2024)
- Yu Su, "Reasoning, Memory and Planning of Language Agents" (Spring 2025)
- Yangqing Jia, "Evolution of System Designs from an AI Engineer Perspective" (Fall 2025)
- Weizhu Chen, "Training Agentic Models" (Fall 2025)

Each chapter cites the moments it uses.

## Lecture guides for this part

Each guide maps one lecture from its first minute to its last and says where this book teaches each piece. Where no chapter teaches a part of the lecture, the guide explains it itself; the table counts those parts.

| Lecture | Lecturer | Length | Parts no chapter teaches | Guide |
|---|---|---|---|---|
| Evolution of system designs from an AI engineer perspective | Yangqing Jia (NVIDIA) | 1:20:00 | 2 of 9 | [open guide](../lectures/f25-02-evolution-of-system-designs-from-an-ai-engineer.md) |
| Compound AI Systems & the DSPy Framework | Omar Khattab (Databricks) | 1:06:00 | 1 of 16 | [open guide](../lectures/f24-05-compound-ai-systems-and-the-dspy-framework.md) |
| Agents for Software Development | Graham Neubig (CMU) | 1:02:00 | 4 of 13 | [open guide](../lectures/f24-06-agents-for-software-development.md) |
| On Reasoning, Memory, and Planning of Language Agents | Yu Su (Ohio State University) | 1:34:00 | 2 of 11 | [open guide](../lectures/sp25-03-on-reasoning-memory-and-planning-of-language.md) |
| Some Challenges and Lessons from Training Agentic Models | Weizhu Chen (Microsoft) | 1:06:00 | 2 of 18 | [open guide](../lectures/f25-05-some-challenges-and-lessons-from-training.md) |
| Towards a unified framework of Neural and Symbolic Decision Making | Yuandong Tian (Meta AI, FAIR) | 1:10:00 | 0 of 16 | [open guide](../lectures/f24-08-towards-a-unified-framework-of-neural-and.md) |

## Where to go next

→ [Part 03: Evaluation](../03-evaluation/01-evaluation-is-the-product.md). An agent you cannot measure is an agent you cannot improve.
