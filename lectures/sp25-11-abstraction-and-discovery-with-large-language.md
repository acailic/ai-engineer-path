# Lecture guide: Abstraction and Discovery with Large Language Model Agents

**Lecturer:** Swarat Chaudhuri (UT Austin) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 11 · **Length:** 1:28:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=IHc0TEMrEdY) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/swarat.pdf)
**Chapters that cite this lecture:** [03. Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md) · [04. Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Swarat Chaudhuri shows language-model agents at work in discovery: Copra proves theorems in Lean without any training by taking the proof assistant's feedback, and LaSR finds equations in data by naming the concepts behind them, with results from olympiad problems, compiler verification and a new scaling law.

## Before you watch

Read [Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) first; its table's row for Copra and the paragraph on Chaudhuri cover both systems of this lecture. The lecture assumes that you know what a language model agent is and refers back to an earlier talk on AlphaProof; the Lean and Coq on screen are illustrations.

## The lecture, part by part

### [0:00–3:32](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=0) How discovery proceeds

Mathematics moves in a loop: model a phenomenon with definitions, conjecture properties, prove them, and let proofs and counterexamples change the models, a social process of convincing one another. The dream of AI for mathematics is to automate large parts of it, settling conjectures and finding new ones. Natural science loops too: hypotheses, experiments, new data, refined or new concepts. There the hope is to have machines that propose hypotheses and design the experiments to test them.
**In this book:** [Agents for Scientific Discovery › The core idea](../06-frontier-applications/03-agents-for-scientific-discovery.md#the-core-idea).

### [3:32–8:14](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=212) Four ideas, and what language models add to each

Discovery searches an infinite space of hypotheses, guided by prior knowledge; it learns from experience, as agents do; and it invents abstract concepts and tools, as calculus did for science. A language model holds knowledge of which hypotheses have worked, so it can steer search. Agents already combine models with interaction and learning. Using models to abstract is new, and the rest of the lecture gives evidence for it.
**In this book:** [What Frontier Domains Teach About Agents › The core idea](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md#the-core-idea).

### [8:14–12:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=494) Where language models stand in mathematics

In 2023 Terence Tao saw AI giving suggestive hints and predicted a trustworthy co-author by 2026, which the lecturer finds plausible. A reasoning model of 2024 far outscored GPT-4o on a competition; DeepMind's system reached silver at the olympiad. Is the model alone enough? The lecturer is sceptical but admits the progress: trained first on general text, then mathematics pages, then problems with step-by-step and tool-using solutions, a model now calls Python and solves hard problems.
**In this book:** [Agents for Formal Mathematics › Why agents benefit](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-agents-benefit).

### [12:00–16:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=720) Two weaknesses of the model alone

Rigorous reasoning beyond school and competitions needs many high-quality traces of reasoning or good reward functions, which are hard to get from human data there. And reasoning in natural language is hard to verify, which matters when reasoning about real systems with real consequences. Scaling may fix this; the lecturer shows an alternative like AlphaProof but closer to an agent: autoformalize the statement into a language such as Lean, Coq or Isabelle, write the proof step by step as code, and have it checked.
**In this book:** [Agents for Formal Mathematics › Why agents benefit](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-agents-benefit).

### [16:00–22:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=960) A proof as a sequence of states

A neural prover emits tactics, rules applied one by one, until nothing remains to prove. Checking a claimed proof is then easy, and during training many candidate proofs can be generated with immediate feedback, which turns proving into a game for reinforcement learning, as AlphaProof did; a thin layer over a pre-trained language model also does well. The example "x even implies x squared even" shows the proof assistant as a state machine: the state lists the context, the hypotheses and the goal; an intro tactic adds the hypothesis x is even; rewrites simplify the goal to zero equals zero and it disappears.
**In this book:** [Agents for Formal Mathematics › The core idea](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-core-idea).

### [22:00–26:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=1320) Two phases, and Copra

Autoformalization turns "there are infinitely many primes" into a Lean theorem; a model given the informal statement can do it. Proving is then a search for a path through a tree of tactics to the end state. The tree is wide and, for advanced theorems with proofs thousands of lines long, deep, a harder problem than any game solved so far. AlphaProof has a formalizer network and a solver network trained with reinforcement learning, also at test time, and even misformalized problems helped it learn. Copra, published at COLM in 2024 and led by the lecturer's doctoral student, keeps the same loop of model and prover but trains nothing.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [26:00–30:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=1560) Why an agent that only prompts is promising

A frontier model receives the proof state and some history of the search, predicts the next step, the prover executes it, and the loop runs inside an external depth-first search with everything in context. It did well with little compute. It gains from every better model at once, mixes natural and formal reasoning, and needs no corpus of training problems, which is hard to build for research mathematics because a research problem is new by design. Its traces can later serve fine-tuning. The proof assistant stays necessary for grounding: an invalid step is reported at once, and the message goes back into the prompt.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [30:00–36:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=1800) Inside Copra

From the formal statement, with optional informal hints, a prompt asks a frontier model for tactics. The text is parsed and executed in Lean, Coq or Isabelle; on an invalid step or remaining goals, the feedback augments the prompt and the search backtracks; a retrieval step adds relevant lemmas from a database. The prompt holds the serialized state (hypotheses such as x being a natural number and even, and the goal), the last step from a stack, and any error. In the worked example a proposed tactic fails twice, each error is returned, and the third one succeeds.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [36:00–39:16](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=2160) Results

In the evaluation, which he dates to late 2023, GPT-4 alone often produced incorrect proofs; with the proof assistant's feedback the same model succeeded on that example. Against the number of queries, Copra proved many theorems quickly where the other methods did not get that far. On miniF2F, mostly high-school competition problems stated in Lean, it proved about 29 to 30% with 60 queries per attempt, comparable to the state of the art then; the state of the art has since moved.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [39:16–46:38](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=2356) Solving hierarchically

New, unpublished work uses the model's abstraction. For an olympiad problem, proving a fraction irreducible for every natural number, a reasoning model first writes an informal plan (define the greatest common divisor, subtract, apply the Euclidean algorithm, conclude). Conditioned on it, the model writes three formal subgoals; Copra proves each; then, given the lemmas and the plan, it proves the theorem. Given the whole theorem as one block, it fails. The lecturer calls this a powerful design pattern: a system built to predict low-level steps does high-level reasoning through prompting alone. Lean's feedback was critical, because one small reasoning model invented lemmas that do not exist.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [46:38–50:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=2798) From mathematics to systems

Formal verification models a real system as definitions and its properties as theorems. It yields systems that are almost impossible to hack: in a program of the US Department of Defense a drone ran a formally verified kernel, and a red team attacked it for six weeks without success. It has been too expensive for most uses, and AI changes that balance. The lecturer's example verifies a compiler: a language has a syntax and a semantics, a compiler is a set of rules translating one language into another, and correctness means the rules preserve the semantics.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [50:00–59:16](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=3000) Verifying a compiler with Copra

In Coq the source language is arithmetic expressions, constants and sums and products; the target language is a list of instructions for a stack machine; the compiler pattern-matches an expression and emits instructions. The correctness theorem says that executing the compiled program gives the same value as evaluating the expression. Copra cannot prove it in one shot, so a reasoning model invents an auxiliary lemma, that compiling one step is correct; Copra proves that, and then the theorem. The lecturer sums up: prompting goes a long way with the proof assistant as grounding; agents for formalization, planning and low-level proof can be combined; and a recent paper led by Dawn Song surveys open challenges.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [59:16–1:04:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=3556) Empirical discovery

Science chooses a question, forms hypotheses, collects and interprets data and reports. Planets seen moving backward led from an Earth-centred model to a Sun-centred one; Tycho Brahe measured Mars precisely; Kepler fitted geometric shapes to the data and found his third law; Newton generalized it into gravitation. Each step traded in abstractions. Symbolic regression, finding equations from observations, seems a poor fit for language models because the data are bare numbers, yet the models bring prior scientific knowledge. They need machinery that evaluates each hypothesis, which yields a loop much like the one with Lean: the model proposes, something else scores.
**In this book:** nothing beyond this guide; nearest: [Agents for Scientific Discovery › The core idea](../06-frontier-applications/03-agents-for-scientific-discovery.md#the-core-idea).

### [1:04:00–1:10:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=3840) Concepts, and LaSR's model

An established method, genetic programming, keeps a pool of expressions, mutates and recombines them, and scores them against the data; the pool forms islands, each a class of functions such as exponential or trigonometric ones. A language model can describe what an island's code does, which is abstraction. LaSR, published at NeurIPS in 2024, starts from two aims: see that laws from different contexts share a concept such as a power law, and attach background knowledge to equations, so that an equation-predicting system can be conditioned on what an expert knows. The model infers programs and concepts together: the likelihood of the data under a program comes from executing it, the likelihood of a program under a concept and the prior over concepts come from the language model.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [1:10:00–1:18:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=4200) The evolutionary loop, and what it found

A population of programs evolves either by classical tweaks to the syntax tree or by an LLM-guided step that is told which concepts look promising, with fitness measured by how well a hypothesis explains the data. The model performs mutation and crossover, as in DeepMind's FunSearch; the concept library is the addition. The library evolves too: the model describes the new programs in words (exponential growth or decay; depends on temperature) and merges concepts into new ones (a Boltzmann distribution). On the task of rediscovering Feynman equations, the method beat pure genetic programming and a variant without concept learning, even with models run locally.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [1:18:00–1:24:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=4680) Hints, leakage and a new law

Hints about the kind of equation gave a modest early benefit. For Coulomb's law, genetic programming returned an unwieldy expression equivalent to the truth, while LaSR reached the truth in four simplification steps. Could the model simply remember the law? The input is only numbers, and experiments on invented synthetic equations still gained. Concepts are natural language with no guarantee of quality, some are meaningless, and formal descriptions are an open idea. Applied to language-model loss versus hyperparameters, where an earlier DeepMind paper had fitted a law by hand, LaSR found a law that also includes the number of examples in the context: many examples hurt weak models and help once a capability threshold is passed. A human combination of the old law and this insight predicted better than either.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

### [1:24:00–1:28:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=5040) Outlook

The same evolution can take images as input when a vision-language model does the describing. The lecturer then lists what is still missing: verifying hypotheses and concepts; concepts live only in natural-language descriptions, and a formal notation might help; the search has not been shown to hold up in larger spaces with more input dimensions; and only one step of discovery, proposing hypotheses, is automated. His closing message is that agents, models combined with other machinery, will matter in mathematics, in science and in engineering.
**In this book:** [Agents for Formal Mathematics › What the practitioners say](../06-frontier-applications/04-agents-for-formal-mathematics.md#what-the-practitioners-say).

## What to take away

- A language model that proposes tactics and reads the proof assistant's errors proves theorems without training; the assistant's feedback is the grounding.
- Asking the model for an informal plan and formal subgoals turns one hard proof into several more tractable ones.
- Finding equations improves when the model names the concepts behind the programs and evolves both together.
- Agents matter for mathematics, for verifying systems and for empirical science; verifying concepts and scaling search are open.

## Sources

- Swarat Chaudhuri, "Abstraction and Discovery with Large Language Model Agents", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=IHc0TEMrEdY).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25>.
