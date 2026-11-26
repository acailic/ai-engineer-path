# Lecture guide: LLM agents: brief history and overview

**Lecturer:** Shunyu Yao (OpenAI) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 2 · **Length:** 1:10:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=RM6ZArd2nVc) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/llm_agent_history.pdf)
**Chapters that cite this lecture:** [05. Prompting and In-Context Learning](../01-foundations/05-prompting-and-in-context-learning.md) · [08. A Short History of LLM Agents](../01-foundations/08-a-short-history-of-llm-agents.md)

> **In one sentence:** A history of how LLM agents grew out of rule-based systems, reinforcement learning and question answering, for engineers who want the ideas behind ReAct, memory and agent benchmarks.

## Before you watch

Read [08. A Short History of LLM Agents › The definition this repository uses](../01-foundations/08-a-short-history-of-llm-agents.md#the-definition-this-repository-uses) first: the lecture uses its terms freely. It assumes you have seen chain-of-thought prompting and names many research systems in passing.

## The lecture, part by part

### [0:00–4:09](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=0) What is an LLM agent?

An agent behaves intelligently while acting on an environment, physical, digital or human. Three notions nest: a text agent acts in language, an LLM agent is one built on an LLM, and a reasoning agent thinks first.
**In this book:** [08. A Short History of LLM Agents › The definition this repository uses](../01-foundations/08-a-short-history-of-llm-agents.md#the-definition-this-repository-uses).

### [4:09–6:08](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=249) Before LLMs

ELIZA, a 1960s chatbot of a few rules, seemed human by echoing its user, but rules are task-specific. Reinforcement learning on text games shares those limits and needs a reward signal many tasks lack.
**In this book:** [08. A Short History of LLM Agents › Stage 1: agents before LLMs](../01-foundations/08-a-short-history-of-llm-agents.md#stage-1-agents-before-llms).

### [6:08–10:27](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=368) From prompting to reasoning

LLMs are trained only to predict the next token, yet a prompt adapts them to new tasks; reasoning tasks and acting tasks were first explored apart. Question answering is the running example, with three obstacles: reasoning, fresh knowledge and real computation.
**In this book:** [08. A Short History of LLM Agents › Stage 2: reasoning and acting, separately](../01-foundations/08-a-short-history-of-llm-agents.md#stage-2-reasoning-and-acting-separately) · [05. Prompting and In-Context Learning › 3. Ask for reasoning on multi-step tasks](../01-foundations/05-prompting-and-in-context-learning.md#3-ask-for-reasoning-on-multi-step-tasks).

### [10:27–15:14](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=627) Tools and two paradigms

Three fixes arrive: generate and run a program; retrieve passages into the context; emit special tokens that call a calculator, a search or an API. One abstraction unites such scattered fixes: reasoning (chain of thought) adds test-time compute, acting (tools, retrieval) adds knowledge and feedback, and ReAct generates both.
**In this book:** [08. A Short History of LLM Agents › Stage 2: reasoning and acting, separately](../01-foundations/08-a-short-history-of-llm-agents.md#stage-2-reasoning-and-acting-separately) · [08. A Short History of LLM Agents › Stage 3: ReAct joins them](../01-foundations/08-a-short-history-of-llm-agents.md#stage-3-react-joins-them).

### [15:14–20:47](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=914) ReAct in action

The prompt shows a hand-written trajectory of thoughts, actions and observations, given as one example, a few, or through fine-tuning. Asked whether $7 trillion buys Apple, Nvidia and Microsoft, GPT-4 searches for the market caps and adds them: not enough. When a search returns nothing, reasoning re-plans.
**In this book:** [08. A Short History of LLM Agents › Stage 3: ReAct joins them](../01-foundations/08-a-short-history-of-llm-agents.md#stage-3-react-joins-them).

### [20:47–24:37](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=1247) Thinking as an action

Once the screen is captioned and sentences are mapped to key presses, many tasks reduce to text games. Mapping observation straight to action only imitates examples, so ReAct adds one more action, thinking, which no environment fixes: it changes nothing in the world and only the agent's own context.
**In this book:** [08. A Short History of LLM Agents › Stage 3: ReAct joins them](../01-foundations/08-a-short-history-of-llm-agents.md#stage-3-react-joins-them).

### [24:37–38:28](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=1477) Long-term memory

The context window is the agent's short-term memory: append-only, bounded (a thousand tokens two years ago, a million now, ten million next year), and gone once the task ends. Reflexion adds a very simple long-term memory: a program fails its unit tests, the agent writes down why and reads the note next time. No gradient is taken: feedback can be a test result or a compiler error, and the agent updates text, which steers later behavior. A later game agent saves each skill as code, and Generative Agents gives about twenty townsfolk a log of events plus conclusions drawn from it. Weights are memory too, so any agent reduces to memory, action space and decision procedure.
**In this book:** nothing beyond this guide; nearest: [04. Using LLMs: Tokens, Context and Sampling › 2. The call does not remember](../01-foundations/04-using-llms-tokens-context-and-sampling.md#2-the-call-does-not-remember).

### [38:28–43:26](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=2308) Three paradigms of agents

A minimal history, offered as certainly wrong: Symbolic AI, an AI winter, deep reinforcement learning (Atari-DQN, AlphaGo), then LLM agents. They differ in what sits between observation and action: a symbolic state, a neural embedding, or language. The first two do not transfer across tasks; language comes pre-trained, so a prompt is enough.
**In this book:** [08. A Short History of LLM Agents › Stage 1: agents before LLMs](../01-foundations/08-a-short-history-of-llm-agents.md#stage-1-agents-before-llms) · [08. A Short History of LLM Agents › Stage 3: ReAct joins them](../01-foundations/08-a-short-history-of-llm-agents.md#stage-3-react-joins-them).

### [43:26–51:22](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=2606) Practical applications

LLM agents enable digital automation, and WebShop (2021–2022) was an early practical test: a simulated shop built from more than one million real products, scored from 0 to 1 on how well the purchase matches the instruction. A software-engineering benchmark then asks for a file diff that fixes a reported issue, and ChemCrow carries the idea into a chemistry lab.
**In this book:** [08. A Short History of LLM Agents › WebShop and what followed](../01-foundations/08-a-short-history-of-llm-agents.md#webshop-and-what-followed).

### [51:22–59:17](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=3082) Lessons and a look ahead

First, lessons: some of the most important work is sometimes also the simplest (chain of thought, ReAct), and simple means general; good research pairs abstraction above individual tasks with close knowledge of them, though familiarity with one task's tricks can breed incremental work. Then five future directions: training, interface, robustness, humans, benchmarks. Training: model makers and agent builders were different groups, and a model trained to predict text was not trained to act as an agent. The fix: let prompted agents generate trajectories and fine-tune on them, adding data the web lacks: the thoughts and actions behind finished blog posts.
**In this book:** nothing beyond this guide.

### [59:17–1:10:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=3557) Interfaces and robustness

Two directions close the talk. Interface: in the lecturer's coding agent, a file search that returns ten results at once beat listing directories or paging one hit at a time, with the same model and prompt, because models read longer contexts than people can hold. Robustness: more samples raise the chance of one correct program, but customer service needs every attempt to succeed. In his benchmark with a simulated user and company tools, the share of tasks solved on every sample falls as samples grow, for every model size.
**In this book:** nothing beyond this guide; nearest: [07. Why LLM Outputs Are Noisy, and What To Do About It › 4. Know what repeated answers buy](../01-foundations/07-why-llm-outputs-are-noisy.md#4-know-what-repeated-answers-buy).

## What to take away

- Reasoning changes only the agent's own context, not the world.
- The context window is short-term memory; Reflexion adds notes that persist.
- Benchmarks reward solving a task once; deployment needs every attempt to succeed.

## Sources

- Shunyu Yao, "LLM agents: brief history and overview", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=RM6ZArd2nVc).
