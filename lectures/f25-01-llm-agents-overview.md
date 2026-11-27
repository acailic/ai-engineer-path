# Lecture guide: LLM Agents Overview

**Lecturer:** Yann Dubois (OpenAI) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 1 · **Length:** 2:00:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=r1qZpYAmqmg) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/lecture1.pdf)
**Chapters that cite this lecture:** [01. Machine Learning in a Nutshell for Software Engineers](../01-foundations/01-machine-learning-in-a-nutshell.md) · [02. How Large Language Models Are Trained](../01-foundations/02-how-large-language-models-are-trained.md) · [03. From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) · [04. Using LLMs: Tokens, Context and Sampling](../01-foundations/04-using-llms-tokens-context-and-sampling.md) · [05. Prompting and In-Context Learning](../01-foundations/05-prompting-and-in-context-learning.md) · [08. A Short History of LLM Agents](../01-foundations/08-a-short-history-of-llm-agents.md) · [05. GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md)

> **In one sentence:** Yann Dubois walks through how a large language model is trained, from web-scale pre-training to reinforcement learning, and why evaluation and systems matter more in practice than architecture and training algorithms.

## Before you watch

Read [Machine Learning in a Nutshell for Software Engineers](../01-foundations/01-machine-learning-in-a-nutshell.md) first: the lecture assumes you know what a loss and a gradient step are. [How Large Language Models Are Trained](../01-foundations/02-how-large-language-models-are-trained.md) and [From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) follow its first 80 minutes closely.

## The lecture, part by part

### [0:00–7:59](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=0) The three stages of training

Three stages, each with its own bottleneck: pre-training on over 10 trillion tokens of web text (data and compute); classic post-training on about 100,000 problems (data quality, evaluation); reinforcement learning on checkable questions, as in DeepSeek R1 (environments and hacking).
**In this book:** [How Large Language Models Are Trained › The core idea](../01-foundations/02-how-large-language-models-are-trained.md#the-core-idea) · [From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md).

### [7:59–12:15](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=479) Five ingredients; prompting and fine-tuning

Five things decide a run: architecture, training algorithm, data, evaluation and systems. Research long favored the first two; the last three matter more in practice. A released model is specialized by prompting, which needs a good evaluation, or by fine-tuning on domain data.
**In this book:** [Prompting and In-Context Learning › 7. Engineer the prompt like code](../01-foundations/05-prompting-and-in-context-learning.md#7-engineer-the-prompt-like-code).

### [12:15–25:59](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=735) Next-token prediction: five steps, and why a network

Pre-training predicts the next token: tokenize, forward pass, a probability per token, sample, convert back to text; sampling happens only at inference. Counting could predict the next word too, but counts need unmanageable memory and fail on unseen text, so a network is used instead.
**In this book:** [How Large Language Models Are Trained › Inference: from prompt to next token](../01-foundations/02-how-large-language-models-are-trained.md#inference-from-prompt-to-next-token).

### [25:59–36:46](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=1559) Pre-training data: cleaning, mix and FineWeb

A public crawl of about 250 billion pages is mostly unusable as it is: text is extracted, harmful content removed, duplicates dropped, odd documents cut, and a classifier trained on pages Wikipedia links to scores quality. Domains are re-weighted to the goal; in FineWeb, deduplication and each later filter raised aggregate accuracy.
**In this book:** [How Large Language Models Are Trained › Pre-training data](../01-foundations/02-how-large-language-models-are-trained.md#pre-training-data).

### [36:46–41:48](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=2206) Mid-training and the open questions on data

Mid-training continues pre-training on under a tenth as many tokens to add what the main run lacked: more code or science, under-represented languages, a longer context (DeepSeek V3: 4,000 to 128,000 tokens), formatting. Labs say little about their data, for competitive and copyright reasons.
**In this book:** [How Large Language Models Are Trained](../01-foundations/02-how-large-language-models-are-trained.md).

### [41:48–53:27](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=2508) Compute: scaling laws, Chinchilla, the cost of a run

Loss falls in a straight line against compute on log axes, so small runs predict large ones and about 90% of the budget goes into one final run. Chinchilla's 20 tokens per parameter ignores inference cost. LLaMA 3 400B, at the time the largest open-source model by his account: 15.6 trillion tokens, 16,000 H100 GPUs, about 70 days.
**In this book:** [How Large Language Models Are Trained › Pre-training compute](../01-foundations/02-how-large-language-models-are-trained.md#pre-training-compute).

### [53:27–1:02:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=3207) Why post-training, and supervised fine-tuning

A base model only continues text: asked "explain the moon landing to a six-year-old", GPT-3 lists more such questions. Post-training steers it toward answers people prefer or checkable tasks. SFT is language modeling on desired answers, from people or from a stronger model, as Alpaca did.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers).

### [1:02:00–1:08:12](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=3720) SFT data without a stronger model

A lab training the best model has nobody to copy, so DeepSeek R1 samples many answers and keeps those a verifier accepts. SFT also teaches format, tool use (one model plays the user, another the tools, in the Kimi K2 pipeline) and early reasoning. Little data suffices for skills pre-training already saw.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers).

### [1:08:12–1:17:44](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4092) Why reinforcement learning, and the cost of sampling

Cloning answers caps a model at its teacher's skill and teaches it to invent references. Reinforcement learning optimizes a reward instead: a rule such as a passing test, a preference model, or an LLM as judge. GRPO scores several answers to one question and moves the policy toward the best; sampling is a key bottleneck.
**In this book:** [From Base Model to Assistant: Post-Training › 2. Why imitation is not enough](../01-foundations/03-from-base-model-to-assistant-post-training.md#2-why-imitation-is-not-enough) · [Training Models for Agentic Tasks › Why the reward needs a guard](../02-building-agents/08-training-models-for-agentic-tasks.md#why-the-reward-needs-a-guard).

### [1:17:44–1:23:03](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4664) Reinforcement learning from human feedback

Where no answer can be checked, preference is the reward: a person picks the better of two answers, a reward model learns that judgment, and PPO or DPO optimizes it. Human labels need detailed rubrics and drift toward style; AlpacaFarm shows an LLM can give such feedback far more cheaply.
**In this book:** [From Base Model to Assistant: Post-Training › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [1:23:03–1:29:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4983) Evaluation: closed-ended, open-ended, model as judge

Evaluation tells whether a run improved, which model suits an application, and whether it is ready for production. Closed-ended sets such as MMLU react to prompt wording and leaked test data. Open-ended answers are compared in pairs: Chatbot Arena asks people, AlpacaEval asks an LLM.
**In this book:** [LLM-as-a-Judge and Rubrics › 1. Decide whether you need a judge](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#1-decide-whether-you-need-a-judge).

### [1:29:00–1:46:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=5340) Systems: GPUs, the memory bottleneck, four optimizations

The best GPUs are scarce, and talking between GPUs is slow, so a run is only as good as its engineering. A GPU applies one instruction to all its threads at once, with matrix-multiplication cores about ten times faster than its other arithmetic. Because compute has grown faster than memory and communication, the bottleneck is feeding the processor: matrix multiplication holds most of a transformer's FLOPs but only about two-thirds of its running time. Memory is a hierarchy, small and fast near the cores, and the score to maximize is model FLOP utilization, achieved throughput over the hardware's peak. Four tricks follow: compute in bf16 while weights stay in 32-bit floats; fuse successive operations so they run on-chip before writing back, as `torch.compile` does; tile, so each value a thread reads is used more than once; and, in FlashAttention, recompute values instead of storing them, for a 1.7× speed-up.
**In this book:** nothing beyond this guide.

### [1:46:00–2:00:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=6360) Parallelism and sparsity

In 32-bit training with Adam, a model with P parameters needs about 16P bytes: weights, gradients and two optimizer states each, so 112 GB for 7 billion parameters, more than one GPU holds. Data parallelism copies the model to every GPU and splits the batch; four GPUs train four times faster, but memory does not shrink. Sharding, as in ZeRO, spreads optimizer states, gradients and weights across GPUs. Pipeline parallelism puts different layers on different GPUs; tensor parallelism splits the matrices inside a layer. In a mixture of experts each token passes through only some parameters, so different GPUs can hold different experts. The recording ends without questions.
**In this book:** nothing beyond this guide.

## What to take away

- Each training stage has its own bottleneck: data and compute, then data quality and evaluation, then environments and hacking.
- Small runs predict large ones, so most of the compute goes into one final run.
- SFT copies answers; reinforcement learning optimizes a reward, which may be a rule, a preference model or another LLM.
- The systems half hour has no counterpart in the book.

## Sources

- Yann Dubois, "LLM Agents Overview", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=r1qZpYAmqmg).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
