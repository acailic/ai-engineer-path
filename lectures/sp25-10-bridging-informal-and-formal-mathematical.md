# Lecture guide: Bridging Informal and Formal Mathematical Reasoning

**Lecturer:** Sean Welleck (CMU) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 10 · **Length:** 1:14:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=Gy5Nm17l9oo) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/welleck2025_berkeley_bridging.pdf)
**Chapters that cite this lecture:** [04. Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Sean Welleck shows three ways to carry the flexible way people reason into proofs a machine can check: a model that writes a thought before each formal step, a method that drafts a proof and fills the gaps of its sketch, and tools and a benchmark for research-level formalization.

## Before you watch

Read [Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) first; its table lists Lean-STaR and Draft-Sketch-Prove, and its section on Welleck summarizes this lecture. The lecture assumes no prior knowledge of proof assistants; the Lean shown on screen is illustrative and need not be followed line by line.

## The lecture, part by part

### [0:00–2:32](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=0) Two ways to write mathematics

Can agents help in expert domains such as finance, science, medicine and mathematics? For mathematics the representation matters. Informal mathematics is raw data, text, images or speech, including LaTeX solutions and papers. Its weakness: nothing guarantees that it is correct. A language model's solution can end with the right answer and still make subtle mistakes in its intermediate steps, which may not matter for simple math but is tiresome to check in education or research.
**In this book:** [Agents for Formal Mathematics › Why this matters](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-this-matters).

### [2:32–6:18](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=152) Formal mathematics and a first proof

Formal mathematics is mathematics written as source code: state a lemma or theorem, write a proof, and if the code compiles the proof is guaranteed correct. The lecturer focuses on Lean and, for one of the topics, on Isabelle. In a live demo in an editor he proves that subset relations are transitive; the proof assistant shows the state of the proof at each step, a command changes it, and a built-in rule finishes it. Writing such proofs takes expertise and knowing what the system already contains.
**In this book:** [Agents for Formal Mathematics › The core idea](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-core-idea).

### [6:18–8:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=378) Mathematicians join in

Terence Tao formalized in Lean a theorem from one of his own papers. The community project Mathlib supplies foundations that others build on, which is why transitivity was already available in the demo.
**In this book:** [Agents for Formal Mathematics › The core idea](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-core-idea).

### [8:00–10:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=480) Why proof assistants matter to mathematicians and to AI

A big proof can be split into pieces that anyone may solve by submitting code, trusted because Lean checks it, unlike a paper that must be read on trust. Feedback is instant, which helps learning, and correctness is guaranteed. For AI, the formal system blocks incorrect mathematics, gives a perfect reward signal for reinforcement learning, and offers a playground for reasoning from easy to arbitrarily hard problems.
**In this book:** [Agents for Formal Mathematics › Why agents benefit](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-agents-benefit).

### [10:00–12:15](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=600) A short history of language models in formal math

A 2020 OpenAI system predicted the next steps of proofs and submitted them as pull requests; the library's maintainers found some shorter and more concise than human proofs. Progress on a competition benchmark has been rapid, and a model released the morning of the lecture reached about 80% on it. The lecturer shows a model's proof of an olympiad problem and notes that Tao used a coding assistant during his formalization project.
**In this book:** nothing beyond this guide; nearest: [Agents for Formal Mathematics › Why this matters](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-this-matters).

### [12:15–16:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=735) The gap, the plan, and the loop

The blocker is the gap between how people reason and what the formal system demands: every step must be spelled out, and one must know the system deeply. The lecture pursues three bridges: informal thoughts inside formal proving (Lean-STaR), informal proofs turned into sketches (Draft-Sketch-Prove and a hammer for Lean), and research-level mathematics. The proving loop: Lean shows the proof state, a language model proposes the next step or tactic, and Lean reports an error, the next state, or success; a proof is a sequence of states and tactics.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [16:00–18:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=960) Learning the next step

A model is trained on pairs of proof state and next step, extracted from a corpus such as Mathlib or from proofs a model generates itself. To find a full proof, tree search asks the model for several candidates, scores them, follows the best and backtracks when a branch fails.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [18:00–22:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1080) Lean-STaR: learning to think before each tactic

The aim is a model that writes free-form reasoning before each formal step: breaking the problem down, planning, or doing a computation that never appears in the proof. It gives room to plan and widens the search space; in other domains, chain-of-thought has been shown to make a model more expressive. No Lean proof comes with such thoughts, so the model must learn to produce them by reinforcement learning in two phases. To initialize, a language model looks at a state and the real next step and writes a thought for that transition in hindsight; shown the state alone it might write a meaningless or incorrect thought. Annotating all of Mathlib yields hundreds of thousands of state, thought and step examples. The initialized model then generates full proofs, Lean says which are correct, and reinforcement learning improves it.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [22:00–26:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1320) The algorithm and what it achieved

The team thinks scoring thoughts made best-first search hard to use, so it sampled many proofs in parallel, retrying a path after an error up to a limit, and applied the simplest method: keep the successful trajectories and train a new model on them, known as expert iteration or rejection fine-tuning. On miniF2F, competition problems stated in Lean, the process took an early model from below a baseline built on GPT-4 to above it, and with the best base model of the time it set the state of the art. Models with thoughts gain more from a larger search budget, a sign that thoughts diversify the search.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [26:00–28:16](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1560) The idea spread

Thoughts soon became part of state-of-the-art provers such as DeepSeek Prover, and a prover released by a startup alternates informal reasoning with snippets of code; reasoning models trained with reinforcement learning, such as o1 and DeepSeek R1, rely on long informal thinking. Training on formal code alone may not suffice to learn the thought process behind the code. In his recap, Lean-STaR builds on this observation and gives a simple algorithm for learning to produce thoughts.
**In this book:** nothing beyond this guide; nearest: [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [28:16–32:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1696) Informal proofs as skeletons, and hammers

An informal proof with three steps can be mirrored in Isabelle by intermediate claims that line up with its steps, yet each claim still needs a low-level proof that looks nothing like prose. Hammers supply such proofs: a tool called Sledgehammer passes the claim to external automated provers based on first-order or higher-order logic or on SMT solvers. They excel at small gaps and fail on a whole olympiad problem, because the search space is vast and they cannot invent intermediate statements. The plan is to combine a high-level prover with such a low-level one.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [32:00–37:23](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1920) Draft-Sketch-Prove

Presented at ICLR 2023, the method has three steps. The input is an informal theorem together with its formal statement, which stops the model from proving something else. A person or a model drafts an informal proof; a model translates the draft into a formal sketch with gaps; a low-level prover, here Sledgehammer, closes the gaps, and if all close the proof is complete. Search means sampling many drafts or many translations. On miniF2F one call proved little and the gains grew with sampling until, in the days of Codex and Minerva, enough samples beat the use of a human-written proof. The lecturer's tutorial includes a notebook that implements the method through a model API.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [37:23–46:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=2243) Building a hammer for Lean

Work not yet published brings sketch-based proving to Lean. An interactive prover such as Lean checks proofs but does not find them; an automated prover finds proofs in some logic; a hammer integrates the second into the first. The obstacle is premise selection: Mathlib holds hundreds of thousands of facts, and giving all of them to an automated prover overwhelms it, so premise selection picks the likely useful few. The pipeline runs from premise selection through a translation of Lean's type theory into higher-order logic, to an automated prover, and back through proof reconstruction into a Lean proof. The team's premise selector is a language model trained as a retriever with a contrastive loss on states and on positive and negative premises; details such as how terms are simplified change its behaviour. All parts are wired into a tree search over tactics that can query the automated prover at any step, exposed to the user as a single command.
**In this book:** nothing beyond this guide; nearest: [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [46:00–53:53](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=2760) A demo, and the measurements

In a second demo the hammer fills the gaps of a human sketch proving that the square root of two is irrational, taken from the book Mathematics in Lean: it first proves a lemma about squares divisible by two and reuses it, and at one step calls the automated prover with a list of facts. On Mathlib theorems held out for testing, the hammer ran on the first step of the proof with different premise selectors: without premise selection; with a retriever from earlier work, retrained on the same library snapshot so that it had up-to-date data; with a symbolic selector re-implemented by a Lean community member, which does decently; with the team's retriever, which proves complementary to that selector, since taking the union of their premises adds a boost; and with the exact premises of the human proof, a level the result is starting to approach. The retriever has only 100 million parameters.
**In this book:** nothing beyond this guide; nearest: [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [53:53–1:02:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=3233) Research mathematics, and a tool anyone can use

Tao's blog describes formalizing a theorem from one of his papers: write a blueprint that decomposes the proof into definitions and lemmas as a dependency graph, still in LaTeX, then realize each node formally. The simplest trusted help for AI is to prove one lemma of the blueprint, since Lean checks the result. The first obstacle is an accessibility gap: strong methods are often closed or costly. The lecturer's tool LLMLean connects Lean to a language model: it queries a model for the next step, discards incorrect outputs and shows in green those that finish the proof and in blue those that merely do not err. It works with a model run locally through Ollama or LM Studio or with a commercial API; in demos it proves the transitivity theorem step by step, in one step, end to end, and shortens a proof. It has filled small lemmas in Tao's project. The bottleneck is now the model.
**In this book:** nothing beyond this guide; nearest: [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [1:02:00–1:14:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=3720) A benchmark for theorems that depend on their project

Competition problems are self-contained: a one-line statement and standard results. A theorem in a real project may depend on definitions and lemmas created for that project, sometimes in other files. The new benchmark miniCTX, to be presented as an ICLR oral, takes theorems added after a date cutoff and theorems from recent real Lean projects, among them Tao's project, and comes with tools that extract problems so that the benchmark stays ahead of the models' training data; a second version, already released, adds projects developed in the past couple of months. It separates theorems whose dependencies lie in the same file from those that span files. A baseline that also shows the model all code in the current file makes no difference on miniF2F and opens a dramatic gap on miniCTX; premise selection improves the cross-file cases. A fine-tuned model runs on a laptop, and data, models, tools and evaluation code are open source. Two challenges remain: a gap between AI advances and tools people can use, and benchmarks that do not always reflect all that real formalization requires.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

## What to take away

- Informal mathematics is flexible but unchecked; formal mathematics is checked but demands every detail.
- A model can learn to write useful thoughts before each tactic by seeing state and step pairs in hindsight, then learning from proofs Lean accepts.
- Drafting an informal proof, sketching it formally and letting automated provers close small gaps separates high-level from low-level reasoning.
- Theorems in real projects depend on their project; benchmarks built from such projects measure what competition problems do not always test.

## Sources

- Sean Welleck, "Bridging Informal and Formal Mathematical Reasoning", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=Gy5Nm17l9oo).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25>.
