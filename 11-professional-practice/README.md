# Part 11 — Professional Practice: Capstones and Checklists

You have read how LLMs work, how to build agents, how to evaluate them, how to secure them, how to test them and how to run them. This part puts it together.

After it you can ship one LLM feature end to end. You have finished at least one capstone project whose acceptance criteria you can test without a teacher. You carry five checklists. And you know what to follow when the course is over.

## The chapters

| # | Chapter | Level | Read | After it you can |
|---|---|---|---|---|
| 01 | [How to Ship an LLM Feature End to End](01-how-to-ship-an-llm-feature-end-to-end.md) | Practitioner | 30 min | Take one feature from a one-line idea to a monitored service, as nine decisions |
| 02 | [Capstone 1: A Task Agent with Evals](02-capstone-task-agent-with-evals.md) | Practitioner | 25 min | Build a task agent and the evaluator that proves what it can do |
| 03 | [Capstone 2: A Monitoring Agent for Prompt Injection](03-capstone-monitoring-agent-for-prompt-injection.md) | Practitioner | 25 min | Build and measure a monitor that flags instructions planted in data |
| 04 | [Capstone 3: From Model to Product](04-capstone-model-to-product.md) | Practitioner | 20 min | Take a classical ML feature through goals, mistakes, pipeline, deployment and operations |
| 05 | [Capstone 4: Efficient Inference](05-capstone-efficient-inference.md) | Practitioner | 20 min | Measure a small open model, quantize it, and report the trade-off |
| 06 | [Capstone 5: Train a Small Language Model](06-capstone-train-a-small-language-model.md) | Professional | 25 min | Build a tokenizer, a Transformer, an optimizer and a training loop, in stages |
| 07 | [Checklists for Shipping AI Systems](07-checklists.md) | Practitioner | 20 min | Copy five checklists into a project, one per stage |
| 08 | [Staying Current](08-staying-current.md) | Foundation | 20 min | Follow four sources and read a paper or a release critically |

## How to read this part

Read chapter 01 first and chapter 07 second. They take 50 minutes together, and they are the whole course in short form.

Then choose by what you need:

- **An agent soon.** Do [Capstone 1](02-capstone-task-agent-with-evals.md). It takes 30 to 40 hours.
- **Something to ship at work.** Do [Capstone 3](04-capstone-model-to-product.md), even if your feature uses an LLM. Its documents transfer unchanged. It takes 35 to 45 hours.
- **A safer agent.** Do [Capstone 2](03-capstone-monitoring-agent-for-prompt-injection.md) after Capstone 1. It uses that agent. It takes 30 to 40 hours.
- **A cheaper or a smaller model.** Do [Capstone 4](05-capstone-efficient-inference.md). It takes from 8 hours on a laptop.
- **To know how a language model is built.** Start [Capstone 5](06-capstone-train-a-small-language-model.md). It is a roadmap project of about twenty weeks, and its first two stages are a complete project on their own.
- **Before you move on.** Read [Staying Current](08-staying-current.md).

The capstones are independent of each other, except that Capstone 2 watches the agent of Capstone 1.

## What the capstones have in common

Each is a project brief with the same parts: the goal in one paragraph, the chapters to read first, a list of deliverables, three to five milestones with acceptance criteria, the hours and the cost, stretch goals, and the pitfalls specific to that project.

Every acceptance criterion is a box you can tick without a teacher. It asks for an artifact: a test that passes, a number in a report, a page in a folder.

## Where it leads

- [The roadmap](../ROADMAP.md) places this part in five learning paths, with the hours for each.
- [The glossary](../GLOSSARY.md) defines every term the course uses.

## Sources

This part adds no new source. It draws on parts 01 to 10, and every step links to the chapter that teaches it. [Staying Current](08-staying-current.md) names the four sources again and dates what it checked.

Capstone 2 is this repository's own project. It combines an idea from Berkeley's Fall 2025 course project with the threat model of part 04, and its chapter says so.
