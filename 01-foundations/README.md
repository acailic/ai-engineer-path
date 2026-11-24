# Part 01 — Foundations: How LLMs Work and How to Use Them

This part takes you from "I have never used an ML model" to "I understand what an LLM is, why it behaves the way it does, and how reasoning is prompted, trained and measured".

It is written for a software engineer who knows Python, Git and the terminal. You do not need any mathematics beyond arithmetic. Every idea is built from something you already know: a function and its parameters, a cost function, a prompt as a function argument.

## What you can do after this part

- Explain what happens between a prompt and the next token.
- Say what a base model is, and what post-training added to it.
- Call a model with settings you chose on purpose, and estimate the cost and latency.
- Write prompts that use examples and reasoning steps deliberately, and test them like code.
- Choose between one answer, a vote over several answers, search and refinement.
- Put an error bar on an evaluation result.
- Define "agent", and place a system on the scale from workflow to agent.

## Chapters

| # | Chapter | Level | Reading | Core question |
|---|---|---|---|---|
| 01 | [Machine Learning in a Nutshell for Software Engineers](01-machine-learning-in-a-nutshell.md) | Foundation | 25 min | Why can't unit tests verify a learned model? |
| 02 | [How Large Language Models Are Trained](02-how-large-language-models-are-trained.md) | Foundation | 30 min | What is a base model, and how was it built? |
| 03 | [From Base Model to Assistant: Post-Training](03-from-base-model-to-assistant-post-training.md) | Practitioner | 30 min | What turns a text-continuer into an assistant that reasons? |
| 04 | [Using LLMs: Tokens, Context and Sampling](04-using-llms-tokens-context-and-sampling.md) | Foundation | 25 min | What do the API settings do, and what does a call cost? |
| 05 | [Prompting and In-Context Learning](05-prompting-and-in-context-learning.md) | Foundation | 25 min | Why do examples and reasoning steps change behavior? |
| 06 | [Reasoning in LLMs: From Chain-of-Thought to Search](06-reasoning-in-llms-from-chain-of-thought-to-search.md) | Practitioner | 30 min | When do several samples or a search beat one answer? |
| 07 | [Why LLM Outputs Are Noisy, and What To Do About It](07-why-llm-outputs-are-noisy.md) | Practitioner | 25 min | Is this score difference real? |
| 08 | [A Short History of LLM Agents](08-a-short-history-of-llm-agents.md) | Foundation | 20 min | What is an agent, and where did the idea come from? |

**Levels.** *Foundation* chapters need no ML background. *Practitioner* chapters assume the Foundation chapters before them and help you at work.

## How to read

**The shortest path** (about two hours): chapters 01, 02, 04, 05 and 08. These five give you a correct mental model of the model, the API, the prompt and the agent.

**The full path** (about three and a half hours): all eight chapters in order. Chapters 03, 06 and 07 go deeper. They show how assistants are trained, how to spend compute on reasoning, and how to read an evaluation without fooling yourself.

Each chapter ends with key takeaways, recall questions and one exercise with acceptance criteria. Every chapter stands on its own, and each says which earlier chapter it expects you to have read.

## How the part was built

The chapters synthesize two of the course's four open sources: the UC Berkeley LLM-agent MOOCs of 2024 to 2025, and chapter 3 of Christian Kästner's *Machine Learning in Production* (MIT Press, 2025). Each chapter lists the lectures it draws on, with links to the moments it uses. Statements from a lecturer are attributed and dated. Model names, prices and API details change quickly, and the text marks them with the date they were checked.

## Where to go next

→ [Part 02: The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md). Chapter 08 defined the agent loop. Part 02 takes it apart and shows how to build one.
