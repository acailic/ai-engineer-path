# Lecture guide: Post-Training Verifiable Agents

**Lecturer:** Jiantao Jiao (NVIDIA) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 3 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=3l0Zxus34es) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/AgenticAI_Jiantao Jiao.pdf)
**Chapters that cite this lecture:** [03. From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) · [08. Training Models for Agentic Tasks](../02-building-agents/08-training-models-for-agentic-tasks.md)

> **In one sentence:** Jiantao Jiao lays out what it takes to post-train an agent whose answers can be checked: good data, honest evaluation, and a training loop that keeps exploring.

## Before you watch

Read [From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) first: the lecture assumes SFT, reward models and reinforcement learning. [Training Models for Agentic Tasks](../02-building-agents/08-training-models-for-agentic-tasks.md) is the chapter built around this lecture.

## The lecture, part by part

### [0:00–4:04](https://www.youtube.com/watch?v=3l0Zxus34es&t=0) From chatbots to verifiable agents

Chatbots were trained by RLHF to match human preference. An agentic model must also align with feedback from an environment and maximize verifiable rewards. The chatbot recipe he recaps: rank responses, train a reward model, then optimize it with SFT, PPO or GRPO.
**In this book:** [From Base Model to Assistant: Post-Training › 4. Reinforcement learning with verifiable rewards](../01-foundations/03-from-base-model-to-assistant-post-training.md#4-reinforcement-learning-with-verifiable-rewards) · [Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

### [4:04–6:53](https://www.youtube.com/watch?v=3l0Zxus34es&t=244) What an agentic model must do

Conversation has no single correct answer. Enterprise tasks involve people, code repositories, software systems and tools: the model must read the environment's full state, act, and give an answer a clear verifier accepts, since a wrong one can crash the system. Engineering cannot rescue a weak model.
**In this book:** [Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

### [6:53–11:30](https://www.youtube.com/watch?v=3l0Zxus34es&t=413) Three hard steps: data, evaluation, training

Data must be verifiable and good. Evaluation must escape the illusion that testing only what the data covers shows progress. Training must turn human feedback into an algorithm: after a mistake, the next attempt has to improve. He compares it to onboarding an engineer.
**In this book:** [Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

### [11:30–16:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=690) Three components of training data

An environment holds the state, such as a code repository with its system prompts. Tools are APIs the model calls to fetch information or to change that state. Verifiers check the result, and work better as a vector than one number: unit tests, proof checkers, browser checks, cost in steps and tokens.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step).

### [16:00–21:43](https://www.youtube.com/watch?v=3l0Zxus34es&t=960) Coverage and verifier quality

A system that works in a few environments breaks outside them, so data must cover many combinations of environments, tools and verifiers. Verifiers are the weak point: for change from a dollar after a 50-cent drink, 1/2 and 2/4 both count; asked for the simplest form, only 1/2 does. Minimize false positives and false negatives alike.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step).

### [21:43–26:15](https://www.youtube.com/watch?v=3l0Zxus34es&t=1303) Five things an agent is expected to do

Evaluation must test for generalization, since no data set covers every environment. He names five targets: work with many tools and many use cases, so a modified tool does not break the agent; cope with vaguely specified instructions, drawing out the user's intent in conversation while still emitting exactly formatted calls; work across software systems, not only the one it was built for; and stay robust, debugging problems like a good engineer. Each target maps to a family of benchmarks.
**In this book:** nothing beyond this guide; nearest: [Evaluating Agents: Trajectories and Environments › Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [26:15–31:42](https://www.youtube.com/watch?v=3l0Zxus34es&t=1575) The benchmarks that exist

SWE-bench asks for real GitHub issues to be fixed, under several harnesses, each offering a different set of tools. Other sets cover many tools and scenarios: τ-bench, BFCL, ComplexFuncBench. Unit tests check structured output such as JSON, which rules cannot repair later.
**In this book:** [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated).

### [31:42–38:27](https://www.youtube.com/watch?v=3l0Zxus34es&t=1902) Holistic evaluation and benchmark quality

Evaluation should stay holistic: many tasks and verifiers, harnesses swapped to reveal drops, capability sets such as HLE, AIME and SWE-bench. A benchmark needs watching for hardness (a set everyone scores high on proves nothing), separability (strong models above weak ones) and diversity. Many public benchmarks beat a few private ones.
**In this book:** [Evaluating Agents: Trajectories and Environments › Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [38:27–42:29](https://www.youtube.com/watch?v=3l0Zxus34es&t=2307) The principle of training

The agent attempts a task several times in its environment; a verifier marks each attempt correct or not and records its cost, and good attempts are reinforced. Attempts should differ, because one wrong answer teaches little. Each attempt costs compute, so tasks always or never solved both waste the run.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step).

### [42:29–49:06](https://www.youtube.com/watch?v=3l0Zxus34es&t=2549) Two stages: imitate, then explore

SFT is imitation: it raises the likelihood of demonstration trajectories so the model stops making meaningless attempts. It must be light and its demonstrations diverse, or the model cannot find its own answers. RL then lets the model explore, reinforcing correct trajectories and discouraging wrong ones.
**In this book:** [From Base Model to Assistant: Post-Training › 5. Jiao's recipe: imitate, then explore](../01-foundations/03-from-base-model-to-assistant-post-training.md#5-jiaos-recipe-imitate-then-explore).

### [49:06–56:56](https://www.youtube.com/watch?v=3l0Zxus34es&t=2946) No settled algorithm; three pillars

Current recipes do not follow from machine-learning theory, and he expects them to be replaced. Three pillars for RL: train longer, without saturating on one answer; train on harder tasks, though not impossible ones; see many different responses with high-quality reward feedback.
**In this book:** [From Base Model to Assistant: Post-Training › 5. Jiao's recipe: imitate, then explore](../01-foundations/03-from-base-model-to-assistant-post-training.md#5-jiaos-recipe-imitate-then-explore).

### [56:56–1:05:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=3416) Train longer: entropy collapse and three remedies

Entropy is the uncertainty of the model's next-token choice. Left alone, RL raises reward and lowers entropy until one answer gets 99% and exploration stops. Remedies: score only the model's own attempts (on-policy), which does better on MATH-500 and AIME; raise the upper clipping threshold (DAPO); add a loss that rewards entropy (Skywork-Open-Reasoner-1).
**In this book:** [From Base Model to Assistant: Post-Training › 5. Jiao's recipe: imitate, then explore](../01-foundations/03-from-base-model-to-assistant-post-training.md#5-jiaos-recipe-imitate-then-explore).

### [1:05:00–1:12:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=3900) Train harder: which prompts teach

A useful measure is the covariance between a sequence's log-probability and its advantage: the model should be confident on right answers. Training only on easy prompts gives low validation accuracy; only on hard ones does worse than a mixture. Dr. GRPO weights rewards by difficulty and penalizes overlong answers to easy questions.
**In this book:** [From Base Model to Assistant: Post-Training › 5. Jiao's recipe: imitate, then explore](../01-foundations/03-from-base-model-to-assistant-post-training.md#5-jiaos-recipe-imitate-then-explore).

### [1:12:00–1:15:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=4320) Sample better: select, then vote with confidence

Sample 32 answers and let the model pick one, and accuracy rises. DeepConf improves majority voting by tracking each trajectory's generation confidence and giving low-confidence ones little or no weight; on one open-weight model it beats plain voting.
**In this book:** [Reasoning in LLMs: From Chain-of-Thought to Search › 1. Self-consistency: sample, then vote](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#1-self-consistency-sample-then-vote).

### [1:15:00–1:18:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=4500) Summary and outlook

Good demonstrations for SFT; for RL, train longer, sample better, train harder. The field is immature; the aim is to close the gap between how people and models learn.
**In this book:** not needed (course introduction).

## What to take away

- A verifier is not one number: tests, proof and browser checks, and cost.
- Narrow coverage and weak verifiers, more than weak models, are what break in use.
- Keep SFT light and diverse; in RL, watch for entropy collapse.
- Judge a benchmark by hardness, separability and diversity, not by score alone.

## Sources

- Jiantao Jiao, "Post-Training Verifiable Agents", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=3l0Zxus34es).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
