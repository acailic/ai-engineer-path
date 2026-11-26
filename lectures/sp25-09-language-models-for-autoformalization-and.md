# Lecture guide: Language models for autoformalization and theorem proving

**Lecturer:** Kaiyu Yang (Meta FAIR) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 9 · **Length:** 52:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=cLhWEyMQ4mQ) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/mathverification.pdf)
**Chapters that cite this lecture:** [04. Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Kaiyu Yang explains how language models are trained for mathematics, why that recipe stalls at research-level proofs, and how the proof assistant Lean restores verification: a retriever that supplies useful lemmas, a system that splits proof steps into a finite and an infinite kind, and a benchmark for translating Euclidean geometry into Lean.

## Before you watch

Read [Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) first; it defines formal mathematics and lists this lecture's two systems in its table. The lecture assumes you know what supervised fine-tuning and reinforcement learning are.

## The lecture, part by part

### [0:00–4:08](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=0) Why maths and coding stand at the centre

Each new model is judged on competition maths and coding. In November 2023 a hedge fund offered ten million dollars for an AI that wins a gold medal at the International Mathematical Olympiad; DeepMind's systems reached silver level in July 2024. A benchmark of research-level problems was released, and within a year a reasoning model solved more than a fifth of it. Maths and coding matter for two reasons: they stand for reasoning and planning, and they are comparatively easy to evaluate, since an answer can be checked and code can be tested, unlike a novel or a symphony.
**In this book:** [Agents for Formal Mathematics › Why this matters](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-this-matters).

### [4:08–10:22](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=248) How models are trained for maths

First continued pre-training on maths pages from forums and papers gives a base maths model. Then supervised fine-tuning on problems with step-by-step solutions, sometimes calling Python, teaches it to solve problems; collecting that data is one of the most expensive parts, because people must annotate and clean it. When only final answers exist, reinforcement learning works: the model writes a solution, its final answer is compared with the truth, and the result is the reward, optimized with an algorithm such as GRPO. This simple idea, long known, was first shown to train reasoning models by DeepSeek-R1. Its key is verifiability; whether it works for proofs is the lecture's question. Every lab uses the same algorithms; infrastructure, engineering and data decide.
**In this book:** [From Base Model to Assistant: Post-Training › 4. Reinforcement learning with verifiable rewards](../01-foundations/03-from-base-model-to-assistant-post-training.md#4-reinforcement-learning-with-verifiable-rewards).

### [10:22–14:59](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=622) Why AI has not solved mathematics

Two gaps remain. Successes are mostly pre-college: a leading mathematician found that a reasoning model still struggles with research problems, which are novel and so have little training data, and the research-level benchmark was designed with numerical answers so that it can be scored. Second, models are good at guessing answers and poor at writing proofs: on an undergraduate competition most answers earned one or two points of ten, and on an olympiad every model scored about 5%, with errors such as flipping an inequality when multiplying by a positive number.
**In this book:** [Agents for Formal Mathematics › Why this matters](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-this-matters).

### [14:59–18:28](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=899) Formal reasoning: a checker instead of data

The lecturer's position paper argues for grounding mathematical reasoning in formal systems, here the proof assistant Lean. A checker verifies proofs and gives automatic feedback, which reduces the need for human data and makes evaluation rigorous. Formal mathematics is written like software: a file holds a proof as a tree of goals, files form projects, and one project builds on another's definitions.
**In this book:** [Agents for Formal Mathematics › The core idea](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-core-idea).

### [18:28–23:15](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1108) Two tasks and a first prover

Theorem proving takes a formal statement and asks for a formal proof, which Lean checks, leaving no room to hallucinate. Autoformalization translates informal mathematics into formal. For proving, the central question is the next step. Earlier systems learned it from human proofs with classical machine learning, later with neural networks, and only large language models brought a real jump. LeanDojo, published in 2023, released open data, tools and models: about 10,000 human-written theorems with their proof steps and the lemmas they use. Its model, the retrieval-augmented prover ReProver, encodes the current proof state and every lemma as vectors, retrieves the most similar lemmas, and generates the next step from state and lemmas.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [23:15–25:07](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1395) How a neural prover is built

Two parts: a search over the tree of proof states, with depth-first or Monte Carlo search, and a model that proposes next steps at each node. Expert iteration improves it: the prover attempts new theorems, the new proofs join the training set, and a better prover is trained, with gains up to a saturation point.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [25:07–29:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1507) Two limits, and a small playground

Human proofs online are few compared with Python code. Second, the action space is infinite: Go has a fixed board, a proof allows endless tactics, so human data cannot cover it and exploration in reinforcement learning is hard; in the questions, the lecturer adds that choosing examples neither too easy nor too hard is a major difficulty of curricula. The team chose olympiad inequalities, whose proofs are regular: apply a known inequality such as AM-GM or Cauchy-Schwarz, or rewrite the formula so that one applies, though even then the branching is large.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [29:00–33:15](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1740) LIPS: splitting steps into finite and infinite

On 20 inequalities, an early reasoning model proved none, two stronger ones three or four, and a human gold medallist at least 15. LIPS sorts steps into two kinds. Scaling applies an existing lemma to part of the formula; there is a finite number of lemmas and finitely many ways to apply each, so a symbolic algorithm can enumerate all of them. Rewriting changes the formula and is infinite, so it is left to the language model. Heuristics filter the candidates. LIPS solved 16 of the 20, against 4 for one reasoning model, and found a proof that an olympiad coach had declared impossible with AM-GM, using AM-GM with a clever rewrite. The lesson: domain insight can structure an infinite action space; whether this generalizes is open.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [33:15–36:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1995) Autoformalizing statements: no reliable check

Autoformalizing a statement and autoformalizing a proof are different problems. For statements the difficulty is evaluation: "there are infinitely many primes" has several correct formal versions, and deciding whether two are logically equivalent is computationally infeasible in general. Researchers fall back on heuristics, which are inaccurate, or on people, which is costly and not reproducible.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [36:00–40:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2160) Autoformalizing proofs: holes, and a restricted domain

Human proofs leave holes, such as a case left to the reader, that a model must fill alone. A problem intractable in general can become tractable in one domain; the team chose Euclidean geometry. Their benchmark, LeanEuclid, has 48 problems from Book I of Euclid's Elements and more than 100 from an existing data set, each with a diagram, the informal statement and proof, and a formal statement written by hand. Proposition 1, constructing an equilateral triangle, became a Lean proof of five or six steps that mirror the original. To their knowledge this is the first formalization of the Elements in a proof assistant.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [40:00–46:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2400) Errors in Euclid, and a working equivalence check

Formalizing uncovered mistakes. Proposition 24's proof works for one configuration of two triangles but fails for another, where an angle the argument relies on lies outside the ones compared; a different proof closes the gap, so Euclid omitted the harder case. The benchmark also makes statement checking feasible: two statements are equivalent if each implies the other, and an SMT solver, an automated reasoning tool, can prove both directions because geometry theorems take a particular form.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [46:00–50:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2760) What is obvious in a diagram

Proposition 1 assumes that its two circles intersect, which cannot be proved from Euclid's axioms and which nobody proves because the diagram makes it obvious. Lean knows no diagram, so "obvious in the diagram" needs a computational meaning. A philosopher, now at CMU, had identified the hidden axioms behind such facts, so a fact is obvious when it follows from them. The evaluation pipeline runs the model's formal statement through the SMT solver against the reference; Lean then marks the holes in the model's formal proof, and the solver checks that each hole is obvious in this sense.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [50:00–52:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=3000) First results and the open problem

Without training, only with a few demonstrations, two versions of GPT-4 autoformalized the benchmark problems. More demonstrations helped, yet success stayed just above 20%, which shows how hard the task is; the version that also sees the diagram did slightly better. Both difficulties were met by restricting the domain, with an equivalence checker for statements and a tool that fills the gaps of proofs. Generalizing beyond one domain remains open.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

## What to take away

- Training on answers works because answers can be checked; proofs and research maths lack both data and a check.
- A proof assistant supplies the check, so the model learns from feedback instead of from scarce human proofs.
- Retrieval narrows the next step; splitting steps into a finite kind for a symbolic algorithm and an infinite kind for the model structures the search.
- Restricting autoformalization to one domain makes evaluation rigorous; generalizing beyond that domain is the open problem.

## Sources

- Kaiyu Yang, "Language models for autoformalization and theorem proving", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=cLhWEyMQ4mQ).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25>.
