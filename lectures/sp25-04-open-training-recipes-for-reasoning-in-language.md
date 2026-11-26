# Lecture guide: Open Training Recipes for Reasoning in Language Models

**Lecturer:** Hanna Hajishirzi (University of Washington) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 4 · **Length:** 1:22:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=cMiu3A7YBks) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/OLMo-Tulu-Reasoning-Hanna.pdf)
**Chapters that cite this lecture:** [03. From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md)

> **In one sentence:** Hanna Hajishirzi walks through the open Tülu 3 recipe for post-training a language model so that it reasons, then adds test-time scaling and mid-training.

## Before you watch

Read [From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) first; the lecture follows its stages in order.

## The lecture, part by part

### [0:00–5:58](https://www.youtube.com/watch?v=cMiu3A7YBks&t=0) Open science, OLMo and Tülu

Hajishirzi argues that fully open models, with data and recipe published, are what let researchers study and improve language models. Her team builds OLMo, an open model family, and Tülu, an open post-training recipe whose largest model approaches GPT-4o.
**In this book:** [From Base Model to Assistant: Post-Training › 6. Open training recipes](../01-foundations/03-from-base-model-to-assistant-post-training.md#6-open-training-recipes).

### [5:58–10:51](https://www.youtube.com/watch?v=cMiu3A7YBks&t=358) Modern post-training and the Tülu recipe

A modern model is built in two stages: pre-training on web-scale next-token prediction, then post-training, which makes it safe, instructable and able to reason. Tülu grew from the best supervised fine-tuning data through preference tuning to Tülu 3, which adds RLVR.
**In this book:** [From Base Model to Assistant: Post-Training › 6. Open training recipes](../01-foundations/03-from-base-model-to-assistant-post-training.md#6-open-training-recipes).

### [10:51–16:45](https://www.youtube.com/watch?v=cMiu3A7YBks&t=651) Instruction tuning and where the data comes from

Evaluations come first: the team fixes target skills, keeps some test sets hidden, then collects prompts, checks licences and removes overlap with the tests. Supervised fine-tuning trains on prompt–answer pairs; answers from people cost time and money and vary in quality, synthetic ones are noisy, and a mix works best.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers) · [Evaluating Agents: Trajectories and Environments › Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [16:45–23:00](https://www.youtube.com/watch?v=cMiu3A7YBks&t=1005) Data mixing and why step-by-step data helps

Mixing data is a balancing act: more poetry data can weaken mathematics, and vice versa. For reasoning, a bare final answer teaches little; step-by-step solutions help with multi-step problems and expose errors, but are slow and expensive to write.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers).

### [23:00–30:00](https://www.youtube.com/watch?v=cMiu3A7YBks&t=1380) Persona-driven synthetic data and filtering

To scale reasoning data, the team has a model write problems for a persona, the same skill aimed at a researcher, a six-year-old or a musician, and has GPT-4o and Claude produce the solutions. The data raised accuracy on MATH far more than on GSM8K; a majority vote over several reasoning paths filtered out about 40% at equal performance.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers).

### [30:00–33:40](https://www.youtube.com/watch?v=cMiu3A7YBks&t=1800) Other routes to reasoning data; the final SFT mix

Other routes trade something away: hand annotation is accurate but limited, turning problems into Python guarantees correctness by execution but reads less naturally, and self-generated chains depend on the base model. Tülu 3 mixes all three, and its safety data did not reduce general capability.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers).

### [33:40–40:00](https://www.youtube.com/watch?v=cMiu3A7YBks&t=2020) Preference data, RLHF with PPO, and DPO

A preference example pairs two responses to one prompt. RLHF trains a reward model on such pairs and optimizes the policy with PPO while keeping it close to the original model; DPO drops the reward model and ranks the preferences directly.
**In this book:** [From Base Model to Assistant: Post-Training › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [40:00–49:21](https://www.youtube.com/watch?v=cMiu3A7YBks&t=2400) What matters in preference tuning

PPO beats DPO in almost all cases but needs two models in memory, so DPO suits ablations. Careful preference-data selection took the score from 56 to 61; PPO added one point, a larger reward model under half a point, and in-domain prompts little on average but much on GSM8K.
**In this book:** [From Base Model to Assistant: Post-Training › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [49:21–54:30](https://www.youtube.com/watch?v=cMiu3A7YBks&t=2961) Over-optimization and a rule-based reward

During DPO training the chat score plateaus, instruction following dips and GSM8K rises then falls: the model over-optimizes the learned reward, whose scores are opaque. For tasks with a checkable result she substitutes a rule: reward 1 when the final answer matches the gold one, 0 otherwise.
**In this book:** [From Base Model to Assistant: Post-Training › 4. Reinforcement learning with verifiable rewards](../01-foundations/03-from-base-model-to-assistant-post-training.md#4-reinforcement-learning-with-verifiable-rewards).

### [54:30–1:04:51](https://www.youtube.com/watch?v=cMiu3A7YBks&t=3270) RLVR: setup, results and scale

RLVR needs only final answers or verifiable constraints, and optimizes with PPO on about 100,000 prompts from GSM8K, MATH and IFEval. It lifts scores after SFT and again after DPO; on MATH the gain is seven points at 405B against three at 70B. It works now, she says, because base models are strong enough to explore.
**In this book:** [From Base Model to Assistant: Post-Training › 4. Reinforcement learning with verifiable rewards](../01-foundations/03-from-base-model-to-assistant-post-training.md#4-reinforcement-learning-with-verifiable-rewards).

### [1:04:51–1:12:30](https://www.youtube.com/watch?v=cMiu3A7YBks&t=3891) s1: 1,000 examples and budget forcing

s1 is a minimal recipe for test-time scaling. From 59,000 difficult math and logic questions, filtering for quality, difficulty and diversity leaves 1,000, with reasoning traces distilled from a thinking model; the full set performs about the same. Budget forcing sets the length of thought: when the model tries to stop early, a word telling it to wait is appended, and a long run is cut off. Accuracy rises with the tokens generated.
**In this book:** [Reasoning in LLMs: From Chain-of-Thought to Search › How it works, step by step › 5. Choosing how to spend the budget](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#5-choosing-how-to-spend-the-budget).

### [1:12:30–1:15:04](https://www.youtube.com/watch?v=cMiu3A7YBks&t=4350) Self-guided generation at inference time

Two further projects, mentioned without detail, push self-guided generation at inference time. One is a retrieval-augmented model trained to emit critique tokens: as it answers, it also judges whether its own response and the retrieved documents make sense. The other applies the loop to scientific literature, synthesizing many sources to answer questions that need long reasoning; a public demo lets users try it.
**In this book:** nothing beyond this guide; nearest: [Reasoning in LLMs: From Chain-of-Thought to Search › 2. Why "review your answer" often hurts](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#2-why-review-your-answer-often-hurts).

### [1:15:04–1:22:00](https://www.youtube.com/watch?v=cMiu3A7YBks&t=4504) Pre-training, mid-training and conclusion

Pre-training itself can add reasoning. After warm-up and a cosine schedule over trillions of tokens, the last stretch, often called mid-training, uses roughly 50 billion tokens of high-quality data, heavy in math, code and reasoning, while the learning rate anneals to zero. Evaluations show what the model lacks and targeted data patches it: OLMo 2 multiplied poorly but added well, so synthetic multiplication data went into the mix.
**In this book:** nothing beyond this guide; nearest: [How Large Language Models Are Trained › Pre-training data](../01-foundations/02-how-large-language-models-are-trained.md#pre-training-data).

## What to take away

- In preference tuning, data curation mattered more than the algorithm: better data took the score from 56 to 61, and switching to PPO added one point.
- RLVR needs only a final answer or a verifiable constraint, and pays off when the base model is strong.
- Open recipes, data and code let others reproduce and extend the results.

## Sources

- Hanna Hajishirzi, "Open Training Recipes for Reasoning in Language Models", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=cMiu3A7YBks).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25/>.
