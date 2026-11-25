# Lecture guide: Inference-Time Techniques for LLM Reasoning

**Lecturer:** Xinyun Chen (Google DeepMind) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 1 · **Length:** 1:22:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=g0Dwtf3BH-0) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/inference_time_techniques_lecture_sp25.pdf)
**Chapters that cite this lecture:** [05. Prompting and In-Context Learning](../01-foundations/05-prompting-and-in-context-learning.md) · [06. Reasoning in LLMs: From Chain-of-Thought to Search](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md)

> **In one sentence:** Xinyun Chen explains three families of techniques that make a language model reason better without changing its weights: better prompts, search over several candidates, and iterative self-improvement.

## Before you watch

Read [Prompting and In-Context Learning](../01-foundations/05-prompting-and-in-context-learning.md) first; its sections on exemplars and reasoning steps prepare you for the first half of the lecture.

## The lecture, part by part

### [0:00–8:23](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=0) Agents and reasoning models

After the course welcome, she defines an LLM-based agent: a language model that reasons and plans, acts, reads feedback from the environment and revises its memory before the next step. Reasoning models have improved rapidly since OpenAI's o1.
**In this book:** [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md).

### [8:23–13:23](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=503) Inference-time scaling and demos

o1 solves competition mathematics and programming problems that earlier models could not, and o3 shows that accuracy keeps rising as more compute is spent per problem. On ARC-AGI, a benchmark of pattern puzzles, earlier models score under 25%; o3 matches an average human annotator with about $20 of compute per task and reaches 87.5% with about $1,000 per problem. The demos show what changed: a long hidden thought precedes the answer.
**In this book:** nothing beyond this guide; nearest: [Reasoning in LLMs: From Chain-of-Thought to Search › The core idea](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#the-core-idea).

### [13:23–24:55](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=803) Getting a chain of thought

A chain of thought is triggered by examples that show the steps, by a one-line instruction or by training. Analogical prompting has the model recall related problems with solutions first; those examples are often flawed, yet on a strong model the method beats hand-written ones.
**In this book:** [Prompting and In-Context Learning › 3. Ask for reasoning on multi-step tasks](../01-foundations/05-prompting-and-in-context-learning.md#3-ask-for-reasoning-on-multi-step-tasks) · [Prompting and In-Context Learning › 4. Let the model supply the examples](../01-foundations/05-prompting-and-in-context-learning.md#4-let-the-model-supply-the-examples).

### [24:55–34:42](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=1495) Automated prompt design

Small wording changes in the trigger instruction move accuracy sharply, so a remedy is to let a model write the prompt: it proposes instructions and, as an optimizer, learns from the instructions tried so far. On GSM8K the instruction found beats a plain one by roughly 18 points.
**In this book:** [Prompting and In-Context Learning › 6. Expect sensitivity](../01-foundations/05-prompting-and-in-context-learning.md#6-expect-sensitivity) · [Prompting and In-Context Learning › 4. Let the model supply the examples](../01-foundations/05-prompting-and-in-context-learning.md#4-let-the-model-supply-the-examples).

### [34:42–39:17](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=2082) Variable computation and least-to-most prompting

Chain of thought makes the computation variable: harder problems get more tokens of reasoning. Least-to-most prompting makes decomposition explicit: reduce the problem to simpler subproblems, then solve them in order. Prompted this way, a model reaches nearly perfect accuracy on long SCAN test commands.
**In this book:** [Prompting and In-Context Learning › 3. Ask for reasoning on multi-step tasks](../01-foundations/05-prompting-and-in-context-learning.md#3-ask-for-reasoning-on-multi-step-tasks).

### [39:17–41:36](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=2357) Dynamic examples and Self-Discover

Real languages have more grammar rules and a larger vocabulary than SCAN, so one prompt cannot hold every rule a problem needs. A follow-up method, evaluated on CFQ, keeps the two-stage decomposition and selects for each subproblem the examples with the most relevant rules. Self-Discover hands the model a list of dozens of reasoning strategies and has it compose the ones that suit the task into a structure to follow.
**In this book:** nothing beyond this guide; nearest: [Prompting and In-Context Learning › 4. Let the model supply the examples](../01-foundations/05-prompting-and-in-context-learning.md#4-let-the-model-supply-the-examples).

### [41:36–49:48](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=2496) Recap, then self-consistency

A reasoning prompt should draw longer thinking from harder tasks and support the strategy the task needs. To recover from a single mistake, sample several solutions and keep the most frequent final answer; the vote improves up to 40 samples, whereas picking the most probable stops after about 10.
**In this book:** [Prompting and In-Context Learning › 7. Engineer the prompt like code](../01-foundations/05-prompting-and-in-context-learning.md#7-engineer-the-prompt-like-code) · [Reasoning in LLMs: From Chain-of-Thought to Search › 1. Self-consistency: sample, then vote](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#1-self-consistency-sample-then-vote).

### [49:48–55:39](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=2988) Selecting code and free-form text

AlphaCode discards programs that fail the example tests, runs the rest on inputs generated by another model and keeps one program from each of the ten largest groups with identical outputs. Universal self-consistency instead has the model read all its candidates and pick the one that agrees most with the majority.
**In this book:** [Reasoning in LLMs: From Chain-of-Thought to Search › 1. Self-consistency: sample, then vote](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#1-self-consistency-sample-then-vote).

### [55:39–1:05:05](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=3339) Verifiers and tree-of-thought search

A verifier trained to judge each reasoning step, as in *Let's Verify Step by Step*, scales better with more samples than one judging whole solutions, but it may not transfer across tasks. With a scorer for partial solutions, tree-of-thought search proposes several next steps, evaluates them and expands the most promising first.
**In this book:** [Reasoning in LLMs: From Chain-of-Thought to Search › 1. Self-consistency: sample, then vote](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#1-self-consistency-sample-then-vote) · [Reasoning in LLMs: From Chain-of-Thought to Search › 3. Search: branch at each step](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#3-search-branch-at-each-step).

### [1:05:05–1:12:13](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=3905) Self-reflection and self-debugging

The third family lets the model revise its own answer. Reflexion and Self-Refine have it write feedback on what was observed, then revise, using signals from the environment when they exist. Self-debugging compares feedback for code, from a bare pass-or-fail message to unit-test results and a simulated execution trace; more information helps more.
**In this book:** [Reasoning in LLMs: From Chain-of-Thought to Search › 2. Why "review your answer" often hurts](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#2-why-review-your-answer-often-hurts).

### [1:12:13–1:19:23](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=4333) Limits of self-correction; spending the budget

Without an oracle, a model that judges its own answers often turns a correct one into a wrong one, so accuracy falls with each round; multi-agent debate loses to self-consistency given the same number of samples. Easy math problems gained most from sequential revision in one study and harder ones from a mixture of parallel and sequential compute.
**In this book:** [Reasoning in LLMs: From Chain-of-Thought to Search › 2. Why "review your answer" often hurts](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#2-why-review-your-answer-often-hurts) · [Reasoning in LLMs: From Chain-of-Thought to Search › 5. Choosing how to spend the budget](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#5-choosing-how-to-spend-the-budget).

### [1:19:23–1:22:00](https://www.youtube.com/watch?v=g0Dwtf3BH-0&t=4763) Conclusion and the Bitter Lesson

The right combination of the three families depends on the model's capability and on the task. She closes with Richard Sutton's essay The Bitter Lesson. As she reads it, the methods worth building go on improving as computation grows and succeed by teaching a model how to discover things, not by handing it what people already know. She expects the principle to hold for training techniques as well.
**In this book:** nothing beyond this guide; nearest: [Reasoning in LLMs: From Chain-of-Thought to Search › What the practitioners say](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#what-the-practitioners-say).

## What to take away

- Better prompts are the cheapest way to spend more compute at inference time.
- Sample several answers and keep the most frequent one; beating that takes a trained verifier or a good judge of partial solutions.
- Revise an answer only when tests, an environment or a tool can say it is wrong; self-correction alone makes reasoning worse.

## Sources

- Xinyun Chen, "Inference-Time Techniques for LLM Reasoning", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=g0Dwtf3BH-0).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25/>.
