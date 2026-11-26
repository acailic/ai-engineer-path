# 06. Capstone 5: Train a Small Language Model

**Level:** Professional · **Reading time:** 25 min · **Exercise:** 200 h
**Prerequisites:** [How Large Language Models Are Trained](../01-foundations/02-how-large-language-models-are-trained.md), [The Language Modeling Pipeline and Tokenization](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md), [Building Your Own: A Roadmap Through the Assignments](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md)

> **In one sentence:** After this project you have built the parts of a language model with your own hands, a tokenizer, a Transformer, an optimizer and a training loop, trained them on a small corpus, and you can read the rest of part 10 as a map of work you have done.

## Why this matters

Part 10 explains how a language model is built. Its source course, Stanford CS336, teaches by building. The roadmap chapter of that part puts it plainly: watching the lectures gives the map, and the assignments are the territory.

This capstone is a roadmap project. It is long, it comes in stages, and each stage ends with a test you can run without a teacher. You may stop after the second stage. You then have a working language model of your own.

## The goal

Build a small language model from its first pieces: a tokenizer, a Transformer, an optimizer and a training loop. Then follow part 10 outward. Make the training fast. Predict how it scales. Build the data pipeline. Align the model with reinforcement learning from verifiable rewards. Each stage teaches one thing.

## Three decisions before you start

**Whose tests tell you that you are right?** There are two paths.

- **Path A: the public assignment repositories.** CS336 publishes five of them under the `stanford-cs336` organization on GitHub. Each ships a test suite and an adapters file of empty functions. You write the implementation, and the tests tell you when it works.
- **Path B: your own repository**, from an empty file. The acceptance criteria below are your tests.

Path A tells you when you are right. Path B is closer to everyday work.

**How much compute can you buy?** See the table below. Most of the project needs none.

**May an AI tool write the code?** The CS336 handouts allow AI tools for conceptual questions and for documentation. They forbid them for implementing any part of an assignment, autocomplete included. Follow the same rule here. The learning is the point. Percy Liang's reason, from the first lecture of the course: coding agents can now solve all the assignments, and a student who feeds one an assignment learns nothing ([Building Your Own](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md)).

## The order, and what each stage teaches

| Stage | You build | It teaches | Chapters of part 10 | Compute |
|---|---|---|---|---|
| 1. Tokenizer | A byte-level [BPE](../GLOSSARY.md) tokenizer | How text becomes integers, and the trade-off in vocabulary size | [01](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) | CPU |
| 2. Model and loop | A Transformer, the loss, an optimizer, a training loop | How the pieces fit into one program, and what each costs | [02](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md), [03](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md) | One GPU, for hours |
| 3. Fast and predictable | A profile, one optimization, a scaling-law fit | Measure before optimizing. Predict before spending | [05](../10-llm-internals/05-gpus-tpus-and-kernels.md), [06](../10-llm-internals/06-parallelism.md), [07](../10-llm-internals/07-scaling-laws.md) | One to several GPUs |
| 4. Data | HTML to text, filters, deduplication | How far one data decision moves the loss | [10](../10-llm-internals/10-training-data.md) | CPU, then a GPU |
| 5. Alignment | [Supervised fine-tuning](../GLOSSARY.md), then RLVR with a math grader | Generate, score, update | [11](../10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) | One GPU |

**RLVR** is reinforcement learning from verifiable rewards. A program, such as a test or an answer check, gives the reward.

## Compute options

| Option | Covers | Cost |
|---|---|---|
| Your laptop's CPU | The tokenizer, every correctness check, the data pipeline | None |
| One rented GPU, by the hour | Training a small model on TinyStories, a set of short children's stories: from minutes to a few hours | By the hour |
| Several GPUs | The distributed parts of stage 3 | The largest bill |
| Free credit | The CS336 course page lists a provider with a monthly allowance of free compute | None |

For prices, see the table in [Building Your Own](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md). It lists what one GPU type cost at several providers, with the date. Its worked example puts forty GPU hours between about $200 and $270. The hours are an estimate. Check current prices before you budget.

## Milestones and acceptance criteria

### Stage 1: the tokenizer (1 to 2 weeks)

- [ ] Encoding a text and decoding it again returns the original, for a file with punctuation, characters outside ASCII, and a special token.
- [ ] No merge crosses a pre-tokenization boundary.
- [ ] The compression ratio, in bytes per token, is reported for the training text and for held-out text.
- [ ] The vocabulary size is a parameter, and the README states what changed when you trained two sizes, with the compression ratio of each.

### Stage 2: the model, the optimizer and the loop (6 to 8 weeks)

This stage is the half-way mark in effort.

- [ ] The model makes the common choices of [chapter 03](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md): pre-norm, RMSNorm, no bias terms, a gated MLP, rotary positions. Every deviation is written down with its reason.
- [ ] The loss on held-out text falls below a value you wrote down before training.
- [ ] The loop saves a checkpoint and restores it. Training continues with the same loss on the next step.
- [ ] Sampling gives ten short texts that you read. On TinyStories they tell a story.
- [ ] One page of accounting: parameters, bytes, FLOPs per step as six times parameters times tokens, measured tokens per second, and model FLOPs utilization.
- [ ] Every correctness check ran on the CPU before any GPU time was spent, and its passing test log is kept.

### Stage 3: fast and predictable (3 to 4 weeks)

- [ ] A profiler names the three largest consumers of time and of memory, before you change anything.
- [ ] One optimization, such as activation checkpointing or a fused attention kernel. The same batch is measured before and after, and memory is profiled too.
- [ ] The loss curves of the two versions overlap within their noise.
- [ ] A scaling law fitted on at least three compute budgets with at least three model sizes. The prediction for a larger budget was written down before the run, and the measured loss is set beside it.

### Stage 4: data (3 to 4 weeks)

- [ ] The pipeline takes a sample of raw HTML pages and returns clean text. You read twenty rejected and twenty kept samples.
- [ ] Filters for harmful content and for personal information exist, each with a test. For a start, a regular expression that drops lines with an email address or a phone number will do.
- [ ] Exact and near-duplicate removal is tested on a synthetic file with known duplicates.
- [ ] Two data variants are trained on the same compute budget, and their loss is compared on one held-out set.

### Stage 5: alignment (3 to 4 weeks)

- [ ] A chat template, with a test that applies it and reads it back.
- [ ] After instruction tuning, the model follows held-out instructions. The pass rate on at least fifty instructions is recorded.
- [ ] After RLVR, the pass rate on a held-out set of math problems is higher than after instruction tuning alone. You confirmed that the inference server used the updated weights before each round, the trap [the roadmap chapter](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) names.
- [ ] Twenty [rollouts](../GLOSSARY.md) are saved in a file, you read them, and none shows [reward hacking](../GLOSSARY.md), passing the grader without doing the task.

## You are done when

1. Every box of stages 1 and 2 is checked. You have a language model of your own.
2. For the full project, every box of stages 3 to 5 is checked too.
3. A README states what you built, the GPU hours used, what they cost, and what you would do differently.

## Effort, tools and cost

Plan on sixteen to twenty-two weeks, about twenty, at ten hours a week for all five stages, as the roadmap chapter advises for self-study. The core, stages 1 and 2, takes about half of that. You need Python 3.10 or newer, the deep-learning library the assignments build on, PyTorch, and a GPU by the hour for training. Everything else runs on a laptop.

Three shortcuts are reasonable:

- If you do only one thing, do stages 1 and 2. They deliver the model that part 10 describes.
- If your goal is applications, read the scaling, data and post-training chapters and do stage 5.
- If you have no GPU budget, do stage 1 and the CPU parts of stage 4.

## Stretch goals

- A distributed run: data-parallel training first, then sharded ([Parallelism](../10-llm-internals/06-parallelism.md)).
- A kernel written in Triton ([GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md)).
- Carrying batch size and learning rate across scale ([Scaling Laws](../10-llm-internals/07-scaling-laws.md)).
- An evaluation with a contamination check ([Evaluating Language Models](../10-llm-internals/09-evaluating-language-models.md)).
- The course's optional leaderboard, for the lowest perplexity in a fixed time on a fixed GPU.

## Pitfalls

1. **Letting an agent write the code.** Fix: use AI to explain, never to implement.
2. **Logic in the adapters, or edited tests.** Fix: adapters stay one line long. Tests are never edited.
3. **Debugging on the GPU.** Fix: get shapes and round trips right on the CPU first.
4. **Optimizing before profiling.** Fix: measure, change one thing, measure again.
5. **Spreading the scaling budget thin.** Fix: a few budgets, several sizes at each, and the prediction written before you look.
6. **Not looking at the data.** Fix: read rejected and kept samples before you trust a filter.
7. **Stale weights during RL.** The inference server and the trainer hold separate copies. Fix: confirm the update before each round, as [the roadmap chapter](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) warns.
8. **Buying GPU time before the CPU checks pass.** Fix: the last box of stage 2 is a gate.
9. **A loss without its held-out set named.** Fix: every reported loss names the data it was measured on.
10. **Comparing runs with different tokenizers or data.** Fix: change one thing at a time.

## What the practitioners say

- **Tests instead of scaffolding.** The CS336 handouts give no solution code. Liang's point, from the first lecture: unit tests keep you from working for weeks on an unverified guess. Much of each assignment can be done on a laptop, and the cluster is for benchmarking speed and accuracy ([Building Your Own](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md)).
- **Profile first.** The systems assignment warns against optimizing parts of the model that account for little time or memory. The same chapter.
- **Debug on the CPU.** The course page's advice to people following along at home (page opened 2026-11-24).
- **The territory is steep.** A course evaluation quoted in the roadmap chapter puts the first assignment at about the work of all five assignments of another course, plus its final project.

## Try it

The project is the exercise. Start with one hour:

1. Clone the first assignment repository, or create an empty one.
2. Run its test command, `uv run pytest`. Every unimplemented test fails with `NotImplementedError`.
3. Make one test pass: encode a short sentence, decode it, and get the sentence back.

**You are done with the first hour when** one tokenizer test passes, and you have written a five-line plan that says which parts you will do on a CPU and which need a GPU.

## Key takeaways

- Build in order: tokenizer, model and loop, speed and scale, data, alignment. Each stage feeds the next.
- Tests tell you when you are right. Use the public assignment repositories, or the acceptance criteria here.
- AI tools are for explanations, not for implementation.
- Debug on the CPU. The GPU is for training and benchmarking.
- Stages 1 and 2 are a complete project. They are also half the effort.
- A self-learner can finish on tens of GPU hours. Check prices before you budget.

## Self-check

1. Why do stages 1 and 2 form a complete project on their own?
2. What does the CS336 handouts' policy allow AI tools to be used for?
3. Why is the last box of stage 2, CPU checks before GPU time, placed as a gate?
4. What must be written down before a scaling-law run, and why?
5. What are the two copies of the weights during RLVR, and what can go wrong?
6. What is reward hacking?

<details><summary>Show answers</summary>

1. Together they deliver a trained language model of your own. Text becomes integers, a Transformer predicts the next token, an optimizer lowers the loss, and the loop keeps it running. The later stages improve and extend that model.
2. Conceptual questions and documentation, such as library signatures. Implementation is forbidden, autocomplete included.
3. GPU time costs money, and most early mistakes are correctness mistakes that a CPU test finds in seconds. The gate stops you from paying to discover them.
4. The predicted loss for the larger budget. A prediction written after the run is not a prediction.
5. The inference server holds one copy and the trainer holds another. If the server is not refreshed, the model generates with stale weights, and the round learns from the wrong behavior.
6. Passing the grader without doing the task.

</details>

## Sources

- Part 10: [The Language Modeling Pipeline and Tokenization](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md), [GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md), [Parallelism](../10-llm-internals/06-parallelism.md), [Scaling Laws](../10-llm-internals/07-scaling-laws.md), [Evaluating Language Models](../10-llm-internals/09-evaluating-language-models.md), [Building Your Own: A Roadmap Through the Assignments](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md)
- Part 01: [How Large Language Models Are Trained](../01-foundations/02-how-large-language-models-are-trained.md), [From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md)
- Stanford CS336 course page, [cs336.stanford.edu](https://cs336.stanford.edu/), opened 2026-11-24.

## Next

→ [Checklists for Shipping AI Systems](07-checklists.md), the short form of everything this part asks for.
