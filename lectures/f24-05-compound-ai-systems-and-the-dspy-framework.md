# Lecture guide: Compound AI Systems & the DSPy Framework

**Lecturer:** Omar Khattab (Databricks) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 5 · **Length:** 1:06:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=JEMYuzrKLUw) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/dspy_lec.pdf)
**Chapters that cite this lecture:** [05. Compound AI Systems and DSPy](../02-building-agents/05-compound-ai-systems-and-dspy.md)

> **In one sentence:** Omar Khattab explains why a system built from several language-model steps beats one model used as a black box, why hand-written prompts make such systems brittle, and how DSPy turns a pipeline into a short declarative program that an optimizer tunes for you.

## Before you watch

Read [Compound AI Systems and DSPy](../02-building-agents/05-compound-ai-systems-and-dspy.md) first; it teaches the signature, the module, the metric and the optimizer with runnable code. The lecture assumes you have written a prompt and seen a retrieval pipeline, and it uses Python freely.

## The lecture, part by part

### [0:00–1:41](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=0) Fluent mistakes are hard to see

Demos are easy to build. The cost is that a model's mistakes read as smoothly as its correct answers: it gave Stanford's founding year wrong and returned parallel code with the very race condition it was asked to remove. Turning a monolithic model into a reliable system stays hard.
**In this book:** [Compound AI Systems and DSPy › Why this matters](../02-building-agents/05-compound-ai-systems-and-dspy.md#why-this-matters).

### [1:41–6:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=101) Compound systems: modules with narrow jobs

A compound AI system is a modular program in which language models play specialized roles instead of answering as one black box. In retrieval-augmented generation a retriever selects passages and the model writes from them. That buys transparency (you can inspect what was retrieved), efficiency (knowledge sits in a corpus, not in the model) and control over the design, so you can iterate without waiting for the next model release.
**In this book:** [Compound AI Systems and DSPy › The core idea](../02-building-agents/05-compound-ai-systems-and-dspy.md#the-core-idea).

### [6:00–8:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=360) Three further wins of composition

The model can itself split a question into pieces and search for each, which is multi-hop retrieval. A Stanford system for writing Wikipedia-style articles brainstorms, outlines, revises and retrieves per section. A competitive-programming system reflects on the problem and public tests, generates candidate solutions, ranks them by tests passed and iterates. The five advantages named are quality, control, transparency, efficiency and inference-time scaling.
**In this book:** nothing beyond this guide; nearest: [Compound AI Systems and DSPy › The core idea](../02-building-agents/05-compound-ai-systems-and-dspy.md#the-core-idea).

### [8:00–12:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=480) A prompt hides five different jobs

Each module is implemented by thousands of tokens that mix five roles: the signature (inputs, outputs, the transformation), an inference-time strategy (think step by step, call tools, sample many and rank), formatting and parsing of inputs and outputs, the objective (do's, don'ts, what to maximize) and per-model tuning found by trial and error. The design you want is tangled with choices that change with every model and data set.
**In this book:** nothing beyond this guide; nearest: [Compound AI Systems and DSPy › How it works, step by step](../02-building-agents/05-compound-ai-systems-and-dspy.md#how-it-works-step-by-step).

### [12:00–16:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=720) The fix is programming

Such systems are "stringly typed": swap in a cheaper model or add a sixth module and the prompts are worthless, which blocks portability and adoption. The lecturer's proposal is ordinary code with fuzzy natural-language modules that learn from data. Like a compiler that moves C code between processor architectures, an optimizer would translate high-level code into prompts for a given model. DSPy, which he expands as declaratively self-improving Python, calls the result a language-model program: a Python function that calls modules declared in a line or two.
**In this book:** [Compound AI Systems and DSPy › How it works, step by step](../02-building-agents/05-compound-ai-systems-and-dspy.md#how-it-works-step-by-step).

### [16:00–22:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=960) What the optimizer must solve

Given a program and a training set of inputs with a metric, choose for every module the string sent to the model, and sometimes the weights, so that the metric is maximized on average. There are no gradients across a system that runs code and tools, and no labels for each module, because demanding them would break the edit-and-recompile cycle. The running example is a program that loops twice: generate a search query from the context so far, retrieve, then answer.
**In this book:** [Compound AI Systems and DSPy › How it works, step by step](../02-building-agents/05-compound-ai-systems-and-dspy.md#how-it-works-step-by-step).

### [22:00–28:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=1320) Signatures, strategies and adapters

A signature says what a module does; a strategy, applied like a layer in a neural network, says how to spend compute on it. An adapter turns a signature into a first basic prompt, and an optimizer treats all prompts of the program as parameters, chosen the way one picks Adam for a neural network. Instead of tweaking 2,000 tokens by hand for a 33% score, a better program explores a much larger design space.
**In this book:** [Compound AI Systems and DSPy › How it works, step by step](../02-building-agents/05-compound-ai-systems-and-dspy.md#how-it-works-step-by-step).

### [28:00–34:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=1680) Evidence and the shared pattern of optimizers

On multi-hop questions, a small optimized model beats a larger unoptimized one, and the same program serves every model. Optimizers may also fine-tune weights, even by reinforcement learning, which let a text-to-text model from 2019 under a billion parameters outscore the frontier models of 2023. Most optimizers share a pattern: guess a first prompt, run the program many times, keep the traces that scored well, use them as demonstrations, or induce instructions from them.
**In this book:** [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [34:00–38:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=2040) What optimization achieved in practice

Toronto researchers won a medical question-answering competition against 15 teams by a 20-point margin with an early optimizer. A Maryland researcher spent 20 hours on hand-tuned prompts for a classification task; the tool beat his best system, by 40% against 15%, in ten minutes. Further systems train retrievers from synthetic data, classify among 10,000 classes with 50 labels, and write articles from a topic.
**In this book:** [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [38:00–42:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=2280) The setting of the optimizer paper

The metric is defined apart from the program: some metrics need labels, others only check that the answer is grounded in retrieved context. The weights stay frozen; only instructions and few-shot demonstrations are optimized, without log probabilities or labels for intermediate steps, with few example inputs (perhaps 150 to 200) and few model calls. Two difficulties follow: a vast discrete search space, and credit assignment, because a local improvement in one module can hurt a module that relied on its output.
**In this book:** nothing beyond this guide; nearest: [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [42:00–46:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=2520) Three ways to search

The cheapest is to bootstrap demonstrations: run the program, trace each module's inputs and outputs, keep the traces whose final answer the metric liked, and search over which ones to insert. A second family comes from single-prompt optimization: ask a model for many instruction variants, score them, show it the best and repeat. Applying it module by module (coordinate ascent) is expensive and greedy, since each step runs the whole program and freezes the others; proposing all modules jointly is cheaper but a harder request.
**In this book:** [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [46:00–52:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=2760) Ground the proposals in the program

A model that writes instructions works blind unless it sees the program. So the optimizer shows it the bootstrapped examples of that module, a summary of the data set built by a map-reduce pass, a description of the whole pipeline derived from its code (so a query module knows whether it writes SQL or web search), and a random piece of advice for diversity.
**In this book:** [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [52:00–56:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=3120) MIPRO: a surrogate model for credit assignment

Language models are poor at credit assignment, so MIPRO borrows from hyperparameter search. Each module has two bulky parameters: the instruction and the list of demonstrations. MIPRO bootstraps demonstrations, proposes candidate instructions with a grounded proposer, then fits a surrogate model that predicts the quality of any combination. It evaluates a proposed combination on a mini-batch of about 30 of 200 examples, feeds the score back, and repeats; its proposals improve over time, unlike random search.
**In this book:** nothing beyond this guide; nearest: [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [56:00–58:51](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=3360) What helps most on a benchmark of programs

On a benchmark of programs with one to four modules, optimizing instructions alone gives a few points and sometimes overfits. Optimizing demonstrations gives jumps of ten points, and random search over bootstrapped examples varies wildly. Optimizing both does best most of the time. Instructions win on tasks with conditional rules, where no handful of examples shows every case.
**In this book:** [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [58:51–1:02:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=3531) Lessons for natural-language programming

Programs are more accurate, controllable and transparent than a model alone. Write about ten lines of declarative code, state an objective, pick an optimizer, and spend your effort on which modules to build and how to connect them. Optimizers are bad at any single proposal but good in bulk. The real gain is that signatures, optimizers, adapters, metrics and inference-time strategies are separated, so each can improve for everyone.
**In this book:** [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=JEMYuzrKLUw&t=3720) Why open research should lead again

The lecturer closes with a goal: let open research lead progress again. Progress will come through modularity, as when different groups built attention, transformers and convolutions, not from ad hoc tricks that die with the next model. The work is to scope programs well, to develop inference-time strategies that anyone can apply to a signature, and to devise optimizers that lift every program at once.
**In this book:** nothing beyond this guide; nearest: [Compound AI Systems and DSPy › What the practitioners say](../02-building-agents/05-compound-ai-systems-and-dspy.md#what-the-practitioners-say).

## What to take away

- A pipeline of narrow modules is easier to inspect, improve and port than one model asked to do everything.
- A hand-written prompt mixes the design with choices tied to one model; declare what each step does and let an optimizer find how.
- Optimizers search in bulk: many bootstrapped examples and proposed instructions, scored by a metric defined outside the program.
- Demonstrations gave the largest gains; instructions matter most where examples cannot show every case.

## Sources

- Omar Khattab, "Compound AI Systems & the DSPy Framework", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=JEMYuzrKLUw).
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
