# Lecture guide: Learning to reason with LLMs

**Lecturer:** Jason Weston (Meta) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 2 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=_MNlLhU33H0) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/Jason-Weston-Reasoning-Alignment-Berkeley-Talk.pdf)
**Chapters that cite this lecture:** [03. From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) · [06. Reasoning in LLMs: From Chain-of-Thought to Search](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md)

> **In one sentence:** Jason Weston explains how a language model can improve its own reasoning: judge its own answers, train on verifiable rewards, and even train its judge.

## Before you watch

Read [From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) first; its sections on preference tuning and on verifiable rewards carry the second half of the lecture.

## The lecture, part by part

### [0:00–5:31](https://www.youtube.com/watch?v=_MNlLhU33H0&t=0) Introduction: self-improving language models

Weston asks whether a language model can train itself: create tasks, judge its own answers, update from them, and so pass human level. He splits reasoning in two. System one is the network's own computation, a fixed amount per token that yields the answer directly. System two is deliberate thinking, mostly a chain of generated tokens before the response, which can carry planning, search and verification.
**In this book:** nothing beyond this guide; nearest: [Reasoning in LLMs: From Chain-of-Thought to Search › The core idea](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#the-core-idea).

### [5:31–17:28](https://www.youtube.com/watch?v=_MNlLhU33H0&t=331) Before 2020: language modeling, attention and memory

He recalls a 2003 neural language model that predicted the next word from learned word embeddings, and a 2008 model from his own group trained end to end on Wikipedia and then fine-tuned on tasks. Stacked attention layers let a network hop through a short story to answer questions needing two facts, a design that led to the transformer and to pre-trained models such as BERT.
**In this book:** nothing beyond this guide; nearest: [How Large Language Models Are Trained › Inference: from prompt to next token](../01-foundations/02-how-large-language-models-are-trained.md#inference-from-prompt-to-next-token).

### [17:28–22:52](https://www.youtube.com/watch?v=_MNlLhU33H0&t=1048) From fine-tuning to RLHF and DPO

Supervised fine-tuning on human demonstrations and training on preference data turn a pre-trained model into an assistant. RLHF trains a reward model on pairwise comparisons and optimizes the policy against it; DPO skips the reward model and directly raises the preferred answer and lowers the rejected one, though its fixed preference data cannot track how the policy changes.
**In this book:** [From Base Model to Assistant: Post-Training › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [22:52–25:30](https://www.youtube.com/watch?v=_MNlLhU33H0&t=1372) Prompting for system two: chain of thought

Between 2022 and 2023 the route to system two was prompting. Few-shot examples that include the reasoning steps make the model imitate them, and a single added line asking it to think step by step works too, lifting a math benchmark from about 10% to 40 or 50%.
**In this book:** [Prompting and In-Context Learning › 3. Ask for reasoning on multi-step tasks](../01-foundations/05-prompting-and-in-context-learning.md#3-ask-for-reasoning-on-multi-step-tasks).

### [25:30–35:47](https://www.youtube.com/watch?v=_MNlLhU33H0&t=1530) Chain of thought beyond mathematics

The same intermediate tokens can repair other failures. Chain-of-Verification has the model write questions about its own draft answer, answer them separately and revise, roughly tripling precision on knowledge tasks. System 2 Attention first rewrites the instruction to drop biased or irrelevant text. Branch-Solve-Merge splits an evaluation into criteria, judges each and merges the verdicts.
**In this book:** [Prompting and In-Context Learning › 6. Expect sensitivity](../01-foundations/05-prompting-and-in-context-learning.md#6-expect-sensitivity) · [LLM-as-a-Judge and Rubrics › 2. Write the rubric](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#2-write-the-rubric).

### [35:47–46:30](https://www.youtube.com/watch?v=_MNlLhU33H0&t=2147) Self-rewarding language models

Human judges struggle to label the code and mathematics that models now write, so the model judges itself instead. A self-rewarding language model scores its own responses from 0 to 5; the highest and lowest of four candidates form a preference pair for DPO. Over three iterations a 70-billion-parameter Llama 2 model's win rate rose from about 10% to 20%, near a version of GPT-4, but it gained little on mathematics, code and reasoning.
**In this book:** [From Base Model to Assistant: Post-Training › How it works, step by step › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [46:30–54:37](https://www.youtube.com/watch?v=_MNlLhU33H0&t=2790) Reasoning with verifiable rewards

To improve reasoning, the reward comes from the known answer instead of a judge: the model writes a chain of thought ending in a marked final answer, which is compared with the gold one, and correct and incorrect attempts form preference pairs for iterative DPO. OpenAI's o1 left its method unpublished, but DeepSeek's R1 paper describes a similar loop at far larger scale, using GRPO.
**In this book:** [From Base Model to Assistant: Post-Training › 4. Reinforcement learning with verifiable rewards](../01-foundations/03-from-base-model-to-assistant-post-training.md#4-reinforcement-learning-with-verifiable-rewards).

### [54:37–1:00:30](https://www.youtube.com/watch?v=_MNlLhU33H0&t=3277) Thinking LLMs: chain of thought without a verifier

Reasoning is useful for tasks without a checkable answer too, such as writing a poem. Thought Preference Optimization applies the same loop there: the model writes internal thoughts, a draft and a final response, and an LLM judge scores the response. Early iterations fall below the model's direct baseline, which was already tuned to answer without thinking; by iterations three and four it overtakes it on AlpacaEval and ArenaHard.
**In this book:** [From Base Model to Assistant: Post-Training › How it works, step by step › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [1:00:30–1:10:00](https://www.youtube.com/watch?v=_MNlLhU33H0&t=3630) Improving the judge: meta-rewarding and thinking judges

Two further methods improve the judge itself. Meta-rewarding language models gives the model three roles, actor, judge and meta-judge, and trains it on preference pairs between judgments as well as between responses; its win rate passes that of self-rewarding training and keeps rising after the latter plateaus. The second trains a judge to think at length: evaluation becomes verifiable when it is known in advance which of two responses is better, a verdict that synthetic data supplies, and the trained model leads RewardBench.
**In this book:** [LLM-as-a-Judge and Rubrics › What the practitioners say](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#what-the-practitioners-say).

### [1:10:00–1:14:00](https://www.youtube.com/watch?v=_MNlLhU33H0&t=4200) Summary, and reasoning without words

He sums up the loop: self-rewarding models may be a path beyond human level, verifiable rewards train chains of thought for reasoning and for judging, better judges can then train models on tasks that have no verifier, and meta-rewarding improves the judgments themselves. One open direction has the model emit vectors instead of tokens as its chain of thought; at small scale they matched text on some tasks and beat it on harder search tasks.
**In this book:** nothing beyond this guide; nearest: [Reasoning in LLMs: From Chain-of-Thought to Search › The core idea](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#the-core-idea).

### [1:14:00–1:18:00](https://www.youtube.com/watch?v=_MNlLhU33H0&t=4440) What comes next

He lists directions: better self-evaluation, which bottlenecks performance; learning from interaction with people, the world or the model itself; and improvements to the network architecture itself. A chain of thought in words also helps safety and interpretability.
**In this book:** not needed (closing remarks).

## What to take away

- A model can supply the judgments it trains on when it is also an able judge; the gains are smaller where its judging is weak, as in mathematics and code.
- A reward computed from a known answer trains chains of thought without any judge, which is the recipe behind recent reasoning models.
- Prompting for reasoning came first; training for it is the current wave.

## Sources

- Jason Weston, "Learning to reason with LLMs", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=_MNlLhU33H0).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25/>.
