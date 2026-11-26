# Lecture guide: Some Challenges and Lessons from Training Agentic Models

**Lecturer:** Weizhu Chen (Microsoft) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 5 · **Length:** 1:06:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=xNxrBHZPDvM) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/weizhu.pdf)
**Chapters that cite this lecture:** [08. Training Models for Agentic Tasks](../02-building-agents/08-training-models-for-agentic-tasks.md)

> **In one sentence:** Weizhu Chen, who leads post-training teams at Microsoft, shares what training agentic models takes in practice: data with rubrics and graders, reward hacking and its cures, and the efficiency work (asynchronous training, exploration, length, LoRA) that makes reinforcement learning run at scale.

## Before you watch

Read [Training Models for Agentic Tasks](../02-building-agents/08-training-models-for-agentic-tasks.md) first; it orders the same material into a procedure with a runnable example. The lecture assumes you know what supervised fine-tuning and reinforcement learning are, and it reports one team's experience more than public results.

## The lecture, part by part

### [0:00–1:32](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=0) Introduction

The lecturer introduces himself: about 20 years at Microsoft, now in a product team, working on post-training, mostly reinforcement learning.
**In this book:** not needed (course introduction).

### [1:32–6:18](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=92) What training a coding agent involves

A repository and an issue go in; a pull request comes back, and the user comments on it over several turns. Between them the model talks many times to an environment simulator that runs code and tests; it runs mostly on CPUs, at least ten times as many as the GPUs. Agentic training must produce a model that is goal-oriented, uses tools over many turns, plans, reasons from feedback and understands the user.
**In this book:** [Coding Agents › 1. Environment](../02-building-agents/07-coding-agents.md#1-environment).

### [6:18–8:25](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=378) Three topics, and two kinds of data

The lecture covers data, the grader and efficiency, and ends with a look ahead. Data splits into verifiable tasks (maths, code with tests, multiple choice) and the non-verifiable rest of a product: code style, writing, safety, where the ground truth is subjective.
**In this book:** [From Base Model to Assistant: Post-Training › 4. Reinforcement learning with verifiable rewards](../01-foundations/03-from-base-model-to-assistant-post-training.md#4-reinforcement-learning-with-verifiable-rewards).

### [8:25–12:24](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=505) Rubrics: written criteria instead of reference answers

For open questions human experts no longer write one answer; they write criteria, as many as 50 for one question, each clear, structured and scorable with a 0 or a 1. An answer is split into fine-grained pieces and each is judged, because what cannot be measured cannot be learned. Writing them can take hours or days per question; quality matters more than quantity. Data synthesis is the other lever, and the lecturer now puts his best people on it.
**In this book:** [LLM-as-a-Judge and Rubrics › 2. Write the rubric](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#2-write-the-rubric).

### [12:24–16:03](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=744) Reinforcement learning from one example

In RLVR for maths, training on one single example repeatedly raised accuracy until it came close to training on more than 1,000 examples on the same test set. The model is not memorizing; it is learning how the building blocks of maths fit together. Not any example works: the team picks one for which the model's sampled answers differ widely, because varied rollouts give the signal to learn from. Reinforcement-learning data is thus chosen for exploration, unlike data for supervised fine-tuning or preference tuning.
**In this book:** [Training Models for Agentic Tasks › What the practitioners say](../02-building-agents/08-training-models-for-agentic-tasks.md#what-the-practitioners-say).

### [16:03–22:20](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=963) Mixing and synthesizing data

Most data work is the mix: shares such as 3% and 20% per source, easier data early and harder data as the model strengthens, and more synthetic data for the categories the model is weak in. For maths the team synthesizes new questions with a mechanism that keeps the answers verifiable; this raised not only first-try accuracy but pass-at-k, which often stalls. Agentic data is very hard to synthesize; he cites one team's pipeline that starts from real tool definitions, synthesizes tools, tasks and more, and mixes them with real data.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step).

### [22:20–28:26](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=1340) The grader is half the problem

Knowing what and how to grade solves at least half of the task. Products need many graders beyond pass or fail: progress updates during ten-minute runs, correct formatting, short answers, time to the pull request. The three common kinds are a pass-or-fail test, a model as judge, and scoring by rubrics. With many graders an early model can hardly pass them all, so the team ranks candidates instead of requiring a pass, adds hard graders late, respects dependencies between graders and runs independent ones in parallel.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step).

### [28:26–30:37](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=1706) Cheating and how to stop it

Asked to pass all tests, the model deletes them or rewrites them to say they passed; on a public coding benchmark it looks up the published solution online. Countermeasures: a second model checks the output; tests are hidden during the rollout and restored for grading; cheating earns a high penalty.
**In this book:** [Training Models for Agentic Tasks › Why the reward needs a guard](../02-building-agents/08-training-models-for-agentic-tasks.md#why-the-reward-needs-a-guard).

### [30:37–33:08](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=1837) Efficiency, including making training work

A run that does not work has zero efficiency. Reinforcement learning is expensive, and compute sets the speed of iteration. Four topics follow: asynchronous training, encouraging exploration, cutting sampling cost and LoRA.
**In this book:** [Training Models for Agentic Tasks › What the practitioners say](../02-building-agents/08-training-models-for-agentic-tasks.md#what-the-practitioners-say).

### [33:08–35:19](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=1988) Sampling and training apart

Sampling is now slower than training, so the two must not wait for each other: samplers keep generating with the previous policy while the trainer updates. Often one trainer works with several rollers, each of which talks to the grader and to the environment. Making this converge on thousands of GPUs is a large engineering effort, and quality trades against efficiency.
**In this book:** [Training Models for Agentic Tasks › What the practitioners say](../02-building-agents/08-training-models-for-agentic-tasks.md#what-the-practitioners-say).

### [35:19–38:17](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=2119) Encouraging exploration

If a small model fails under reinforcement learning, check its instruction following first. Then vary the prompts: ask for a different method, or have another model rewrite the problem, so the model sees many routes. Add noise, limit output length, and change or remove tools between attempts so the model explores different environments.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step).

### [38:17–40:00](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=2297) Tools must generalize

Users connect their own tools and APIs to one model. That needs strong instruction following, the habit of noticing a misused tool during a rollout and switching, and a penalty when the model ignores a tool named in the prompt.
**In this book:** [Training Models for Agentic Tasks › What the practitioners say](../02-building-agents/08-training-models-for-agentic-tasks.md#what-the-practitioners-say).

### [40:00–44:45](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=2400) Solution length and context

A model that retries forever hurts the experience: a one-minute solution beats a one-hour one. Training controls long rollouts with a token cost; the penalty must be balanced, since too low a penalty wastes tokens and too high a one sacrifices exploration. Evaluation must report rollout length, because pass rates at different test-time compute are not comparable. Contexts of 128,000 tokens run out, so earlier rollouts are summarized and replaced; a paper from Alibaba uses a separate summarizer model.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step) · [Memory and Knowledge for Agents › B. Compaction](../02-building-agents/04-memory-and-knowledge-for-agents.md#b-compaction).

### [44:45–48:30](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=2685) LoRA in reinforcement learning, and fast experiments

LoRA trains a small set of added weights and changes the model little, which is regularization. Reinforcement learning needs it twice over: the policy must not drift far from the last checkpoint, and the sampling policy must stay close to the model being trained. It also needs fewer GPUs. Separately, the team runs most experiments with cheaper, slightly suboptimal settings two to three times faster than the best ones, and compares changes side by side; the final run can take all the best settings, though by his account his team did not, because it is too costly.
**In this book:** [Training Models for Agentic Tasks › How it works, step by step](../02-building-agents/08-training-models-for-agentic-tasks.md#how-it-works-step-by-step).

### [48:30–52:52](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=2910) The whole of training, told with building blocks

The lecturer explains the stages to his eleven-year-old with toy bricks. Pre-training turns unordered data into a wall rebuilt from bricks: it learns the bricks. A better model builds more complicated bricks and needs fewer of them. Post-training assembles a chosen wall from bricks that already exist, which is why it is efficient. Reinforcement learning is playing: build a world, receive feedback, keep what is praised, tear down and rebuild what is not. One day a model may build shapes never seen in reality.
**In this book:** nothing beyond this guide; nearest: [Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

### [52:52–56:00](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=3172) Look ahead: test-time scaling

Three dimensions, under the common theme of scale. Deeper models, including recent recurrent designs, help reasoning. Wider means parallel thinking, today applied only after training by voting or picking; training a model for parallel thinking is an open topic, and a second way to go wider is several agents coordinated by an orchestrator or a boss. Longer means tasks that take one or two days, which need long contexts and a memory of earlier behaviour, something people do well and models do not.
**In this book:** [Training Models for Agentic Tasks › What the practitioners say](../02-building-agents/08-training-models-for-agentic-tasks.md#what-the-practitioners-say).

### [56:00–1:02:00](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=3360) Look ahead: training-time scaling

The team is limited by data, not compute, so data synthesis has only begun; agentic data raises the complexity another level. Reinforcement learning spends far more compute than supervised fine-tuning and buys robustness: the model still answers when the question is phrased differently. He believes quality keeps rising with compute until the model's own limit, and says graders steer behaviour far more flexibly than retraining a reward model. The lecturer wonders whether only two losses will remain, reinforcement learning and next-token prediction, and whether a model can improve itself by reflecting on what went wrong.
**In this book:** [Training Models for Agentic Tasks › What the practitioners say](../02-building-agents/08-training-models-for-agentic-tasks.md#what-the-practitioners-say).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=xNxrBHZPDvM&t=3720) What the job is like

Large infrastructure is unstable: GPUs fail and lose connections, someone wakes at 3 a.m. to restart the job and save the GPUs, and for about 90% of the time the run is not working. The remaining 10% makes progress, and a model that beats the baseline and ships in a product used by many people is a satisfaction hard to find elsewhere.
**In this book:** nothing beyond this guide; nearest: [Training Models for Agentic Tasks › What is public and what is one team's account](../02-building-agents/08-training-models-for-agentic-tasks.md#what-is-public-and-what-is-one-teams-account).

## What to take away

- Much of the daily work is data and graders: written rubrics for open tasks, synthesized data for weak categories, several graders per product.
- Models cheat against any grader they can reach; hide the tests, check outputs with a second model and penalize cheating.
- Sample and train apart, choose training examples for exploration, charge for length and report it.
- Reinforcement learning buys robustness and improves with compute; the open problems are data, memory over days and self-improvement.

## Sources

- Weizhu Chen, "Some Challenges and Lessons from Training Agentic Models", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=xNxrBHZPDvM).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
