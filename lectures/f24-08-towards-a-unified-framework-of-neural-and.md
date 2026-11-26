# Lecture guide: Towards a unified framework of Neural and Symbolic Decision Making

**Lecturer:** Yuandong Tian (Meta AI, FAIR) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 8 · **Length:** 1:10:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=wm9-7VBpdEo) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/102824-yuandongtian.pdf)
**Chapters that cite this lecture:** [03. Planning, Search and Decision-Making](../02-building-agents/03-planning-search-and-decision-making.md)

> **In one sentence:** Yuandong Tian shows that language models still fail at planning under constraints, and lays out three responses: scale them, join them with symbolic solvers in three ways, or study how symbolic structure appears inside trained networks.

## Before you watch

Read [Planning, Search and Decision-Making](../02-building-agents/03-planning-search-and-decision-making.md) first; its section "A unified view: neural plus symbolic" already summarizes the lecture up to the modular-addition part. The lecture assumes that you know what a language model is, that you have met the idea of a search algorithm, and that you are willing to look at a few equations in the last fifteen minutes.

## The lecture, part by part

### [0:00–1:37](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=0) Welcome

The lecturer introduces himself and the topic: planning and reasoning with large models.
**In this book:** not needed (course introduction).

### [1:37–4:00](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=97) The travel-planning task

The user names cities, dates and a budget and wants an itinerary that can be executed. A system would search for destinations, flights and hotels, then plan a route through the information collected.
**In this book:** [Planning, Search and Decision-Making › Why this matters](../02-building-agents/03-planning-search-and-decision-making.md#why-this-matters).

### [4:00–8:00](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=240) Current models fail it

On a benchmark from the lecturer's group, the strongest model of early 2024 produced a fully valid itinerary 0.6% of the time, and only 4.4% when given the correct information upfront; a pass means every constraint holds, such as the budget or a non-smoking room. The o1 reasoning models scored worse than a model fine-tuned for the task. Plots from other teams show the same trend: accuracy slides towards zero as the number of cities or people grows, and although the o1 models score far higher on small problems, their curve also drops to zero as the plan gets longer.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [8:00–12:00](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=480) Three kinds of answer

One answer is the scaling law: more data, more compute, larger models, at great cost. A second is hybrid systems. Foundation models understand natural-language instructions but plan badly; symbolic solvers return optimal solutions with guarantees in many scenarios, often run fast without GPUs, but cannot read a request. A third is to show that a symbolic representation emerges inside a network trained by gradient descent.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [12:00–15:13](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=720) Hybrid one: the model calls the solver

The model translates the request into a JSON description; flights and hotels are added; the problem is written as mixed integer linear programming; a solver returns the optimal itinerary, which is turned back into sentences. A fine-tuned translator takes 2 to 2.5 seconds and the solve 0.5 to 7 seconds, so the demo runs in real time, and most human raters were net positive about it against the baselines on usefulness, satisfaction, value for money and efficiency.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [15:13–20:23](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=913) Hybrid one, continued: dialogue that gathers what is missing

Real users start with a rough idea, so a follow-up agent asks questions over several rounds until it has the details, then writes the JSON. It is trained against a written constitution with four demands: accurate, proactive (ask useful questions, not random ones), efficient and adaptive to the traveller, and credible (few hallucinations). With 50 traveller personas that each hide critical facts, several rounds of direct preference optimization made the agent collect more of the overall and of the critical information than an untuned model. A related paper replaces the human judge with an agent that checks every step of the target agent and gives richer feedback.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [20:23–24:32](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=1223) Hybrid two: the solver teaches the model

In Searchformer a transformer does not predict the plan directly. It first outputs the trace of the A* search algorithm, every node it created and explored, and then the plan. The search-augmented model is much longer to generate.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [24:32–32:50](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=1472) Hybrid two, continued: efficient learning, then shorter traces than A*

The search-augmented model is far more efficient: with 15 million parameters and 50,000 training examples it reaches about 80% on unseen 30 by 30 mazes, where a solution-only model of 175 million parameters scores about 20% on that budget and needs about a million examples to reach high performance. A box-pushing puzzle game shows the same trend. The first model imitates A*, so its traces are as long as the algorithm's. The next step samples many traces, keeps the shortest ones that still lead to an optimal plan and retrains on them. Over rounds the average trace length shrinks, the ratio of the A* trace length to the model's (the improved length ratio) rises, and the optimality rate even climbs a little. A 24-million-parameter model then matches solution-only models of 700 million.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [32:50–41:26](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=1970) Dualformer: one model, fast and slow

A long trace can cost thousands of tokens. Dualformer trains on a mixture in which parts of the trace are dropped at random, down to the plan alone. The mixture beats training on plans only or on full traces, and the outputs are more diverse, which helps when more compute is spent at test time. The model also switches by itself between a fast mode (it starts with a plan token and answers at once) and a slow mode (it starts with a create token and searches), and does better than either dedicated model; forcing the first token selects the mode. Dropping sentences from maths explanations in the same way gives shorter reasoning and slightly better accuracy. On mazes it beats a reasoning model of 2024, which the lecturer calls an unfair comparison because that model was not fine-tuned on the data.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [41:26–47:25](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=2486) Hybrid three: train the model and the solver together

Many real problems have a differentiable but nonlinear objective under combinatorial constraints. One example: place embedding tables on GPUs so that no device exceeds its memory and the latency, estimated by a neural network, is minimal. A genetic algorithm can take forever to find a feasible answer, and a solver cannot take the nonlinear objective. SurCo learns a surrogate cost from the problem description, gives it to a linear solver, and backpropagates through the solver so that only the final loss is judged.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [47:25–49:34](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=2845) Three ways to use the surrogate

One variant optimizes the coefficients at test time by backpropagation (slow, good solutions); a second predicts the coefficients once and calls the solver once; a hybrid starts from the prediction and keeps optimizing. All three reach lower loss than domain heuristics, a greedy method and a reinforcement-learning approach, and the second is fastest to deploy.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [49:34–54:02](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=2974) Photonic design, and the limits

The same method designs a device on an 80 by 80 grid of nanometre-scale cells that bends or splits light by diffraction. The design space is binary and constrained by the size of the brush that will carve it, and the loss comes from a physical simulation. The method converges more smoothly than the standard approach without a neural network. Limits remain: the objective must be differentiable, a solver is called in every training step, and that solver must be differentiable.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [54:02–56:36](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=3242) Two stories about what models learn

One camp expects emergent abilities from scale. The other says a model mostly retrieves patterns seen in training. An Apple study supports the second: adding irrelevant sentences to a maths word-problem benchmark, which does not change the answers, makes every model's score drop sharply. The lecturer calls it a core problem to understand what representation a language model uses for reasoning and planning.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [56:36–1:02:00](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=3396) Modular addition and the Fourier basis

The task is addition modulo a number: two inputs, one output, easy to memorize. Networks trained on it do not build a lookup table; earlier work found that they represent numbers with sine and cosine features. The lecturer studies a two-layer network with one-hot inputs and quadratic activations, moves everything into the Fourier domain, and finds that the hidden neurons respond strongly at a few frequencies. Counting neurons per frequency shows sharp peaks at orders four and six, for moduli 7, 23, 71 and 127.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=3720) Why four and six: the algebra of the loss

Only very strong weight decay changes this picture: every solution collapses to zero. The mean-squared loss is rewritten as one minus a term plus three sums of squares. Setting the term to one and the squares to zero is a sufficient condition for a global optimum. The space of two-layer networks, with concatenation of neurons as addition and a product along the hidden units as multiplication, forms a semi-ring, and two terms of the loss are ring homomorphisms: they respect that addition and multiplication. So two partial solutions, each satisfying one term, can be multiplied into a solution that satisfies both. Global optima of order six and order four can be built this way, with no gradient descent at all.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

### [1:06:00–1:10:00](https://www.youtube.com/watch?v=wm9-7VBpdEo&t=3960) What gradient descent finds is the constructed solution

Networks trained by gradient descent land almost entirely on the order-four and order-six solutions. Factorizing them under the ring multiplication, 95% split into a two times a three or a two times a two, as the construction predicts, and, entry by entry, 98% of the solutions match the constructed forms. The implication: a network trained by gradient descent converged to a solution that is symbolic. Perhaps larger networks do the same in a form nobody has constructed yet, and solutions could one day be assembled algebraically from small ones.
**In this book:** [Planning, Search and Decision-Making › A unified view: neural plus symbolic](../02-building-agents/03-planning-search-and-decision-making.md#a-unified-view-neural-plus-symbolic).

## What to take away

- Models still fail at planning under hard constraints, and accuracy falls as the problem grows.
- When a sub-problem has a known algorithm, let the model translate the request and let the solver decide.
- Training a model to output a solver's trace makes it ten times smaller and ten times cheaper in data; trimming the traces then makes them shorter than A*'s.
- In one small task, gradient descent finds a solution that algebra could have built directly.

## Sources

- Yuandong Tian, "Towards a unified framework of Neural and Symbolic Decision Making", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=wm9-7VBpdEo).
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
