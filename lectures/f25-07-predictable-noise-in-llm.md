# Lecture guide: Predictable Noise in LLM

**Lecturer:** Sida Wang (Meta) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 7 · **Length:** 44:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=HV8pugcFVO0) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/PredEval.pdf)
**Chapters that cite this lecture:** [07. Why LLM Outputs Are Noisy, and What To Do About It](../01-foundations/07-why-llm-outputs-are-noisy.md) · [05. Statistics for Evals: Error Bars and Significance](../03-evaluation/05-statistics-for-evals.md)

> **In one sentence:** Why a few points on a small, hard benchmark mean little, how to put an error bar on a score or on the gap between two models, and how to predict that bar from accuracy and dataset size, for anyone who reads an LLM leaderboard.

## Before you watch

Read [07 › The core idea](../01-foundations/07-why-llm-outputs-are-noisy.md#the-core-idea) for the vocabulary of noise and [07 › Compute the error bar](../01-foundations/07-why-llm-outputs-are-noisy.md#1-compute-the-error-bar) for the formula the lecture derives. The lecture assumes that you have run a benchmark and are comfortable with a mean, a variance and a hypothesis test.

## The lecture, part by part

### [0:00–1:39](https://www.youtube.com/watch?v=HV8pugcFVO0&t=0) Research introduction

Sida Wang traces a path from learning by human feedback, through code models and several code benchmarks, to reinforcement learning for a code world model. The talk asks how far such benchmark scores deserve trust.
**In this book:** not needed (course introduction).

### [1:39–4:21](https://www.youtube.com/watch?v=HV8pugcFVO0&t=99) Evaluating LLM benchmarks

A ten-point gain on ImageNet, with 100,000 images, was beyond doubt. Generative and agentic benchmarks are slow to build and run; the gains reported on them are small, and many fail the conventional test for significance, because the sets shrank: MNIST had 10,000 examples and MMLU about as many, HumanEval has 164, LiveCodeBench aims for about a thousand, and SWEbench-style runs number in the hundreds while spending hundreds of thousands of tokens and hours.
**In this book:** nothing beyond this guide; nearest: [07 › Why this matters](../01-foundations/07-why-llm-outputs-are-noisy.md#why-this-matters).

### [4:21–11:02](https://www.youtube.com/watch?v=HV8pugcFVO0&t=261) Exploratory data analysis

One hard question, the counterargument goes, informs more than a multiple-choice item: the school-level math olympiad poses six problems, the Putnam contest twelve. To test whether hard questions make up for low statistical power, he plots per-question results as a grid: models ordered by overall score, questions by difficulty, color for accuracy over repeated draws. On a 500-question math benchmark, HumanEval, MBPP, a SWEbench leaderboard and LiveCodeBench, easy and hard bands still show, even where only a pass-or-fail verdict exists.
**In this book:** nothing beyond this guide; nearest: [07 › Treat small, hard benchmarks with suspicion](../01-foundations/07-why-llm-outputs-are-noisy.md#6-treat-small-hard-benchmarks-with-suspicion).

### [11:02–16:24](https://www.youtube.com/watch?v=HV8pugcFVO0&t=662) Reliability of small datasets

The grids show inconsistency: the best model fails easy questions, models solving only 20–30% of the set solve some hard ones, and close models each win questions the other loses. One question that only strong models answer reliably is still solved 30% of the time by weak models over a thousand samples. A non-zero chance can be raised by retrying under a verifier, so a correct answer on a hard question proves little: models err on simple steps, as one did by calling a kettle part a robot, and errors compound, leaving small benchmarks unreliable.
**In this book:** [07 › Treat small, hard benchmarks with suspicion](../01-foundations/07-why-llm-outputs-are-noisy.md#6-treat-small-hard-benchmarks-with-suspicion).

### [16:24–26:35](https://www.youtube.com/watch?v=HV8pugcFVO0&t=984) Statistical methodology

A score is an average of 0/1 results over n questions, treated as a sample from a larger population of possible questions, a framing a paper by Miller sets out for LLM evaluation; its standard error shrinks with the square root of n. For a comparison, take the per-question difference, −1, 0 or 1: when two models track each other, this paired variance nearly vanishes. Divide the gap by its standard error to get a z-score; two standard errors is the conventional 5% threshold. On HumanEval the standard error is about 4%, so roughly a 10-point gap is needed without pairing and about 8 points with it, more than many reported gains.
**In this book:** [07 › Compute the error bar](../01-foundations/07-why-llm-outputs-are-noisy.md#1-compute-the-error-bar) · [07 › Compare on the same questions](../01-foundations/07-why-llm-outputs-are-noisy.md#3-compare-on-the-same-questions).

### [26:35–30:53](https://www.youtube.com/watch?v=HV8pugcFVO0&t=1595) Measuring noise in models

Models can answer the same question many times, so an evaluation has two noise sources: which questions were drawn, possibly the larger one, and what the model's sampling produced. The total variance then splits into a question part and a sampling part that simply add. His example has eight questions: model A has a 10% chance on each, model B is certain on four and hopeless on the rest; B averages far higher, yet with a verifier that rejects wrong attempts, A is the better model. Plain mean and variance estimators suffice; bootstrap resampling agrees, and so does the sign test when the two models are close.
**In this book:** [07 › Know what repeated answers buy](../01-foundations/07-why-llm-outputs-are-noisy.md#4-know-what-repeated-answers-buy).

### [30:53–37:24](https://www.youtube.com/watch?v=HV8pugcFVO0&t=1853) Noise and distribution theory

Averaged over all model pairs, the paired standard error is about as large as the unpaired one, as if two models' results were only half correlated; the unpaired figure follows from accuracy and dataset size alone. The cause is a regularity in per-question success rates: apart from questions no model solves, they fit a bimodal beta distribution for a strong model, while weak models fit the plain independent formula, as on MMLU, where guessing earns about 20%. LiveCodeBench and SWEbench fit too; the lone outlier, SWEFixer against its filtered variant, is a strict improvement with an unusually small error.
**In this book:** [07 › Use Wang's shortcuts](../01-foundations/07-why-llm-outputs-are-noisy.md#7-use-wangs-shortcuts).

### [37:24–40:09](https://www.youtube.com/watch?v=HV8pugcFVO0&t=2244) Practical evaluation advice

Other estimates, such as the variance along a training curve, tend to underestimate noise, so use the measurements instead, in three steps of rising accuracy: read the standard error from the table, read it from a chart at your model's accuracy, or supply per-question results to the accompanying code, which places your comparison among all the others. Doing your own test is possible but error-prone, because several kinds of variance are easy to confuse.
**In this book:** [07 › Use Wang's shortcuts](../01-foundations/07-why-llm-outputs-are-noisy.md#7-use-wangs-shortcuts).

### [40:09–44:00](https://www.youtube.com/watch?v=HV8pugcFVO0&t=2409) Benchmarking audit tools

Per-question data also audits the benchmark: look for items where better models do worse. Most such items are not real errors, but in MBPP many are inconsistent or wrong, and the mistakes reached a later version of the set; a model that returns a flawed item's reference answer exactly, on several such items, may have seen the evaluation data in training. For builders, the question is what effect size a benchmark can detect: doubling model size brings a steady gain that MMLU reliably registers, while HumanEval cannot separate a doubled model from its predecessor.
**In this book:** nothing beyond this guide; nearest: [07 › Pitfalls](../01-foundations/07-why-llm-outputs-are-noisy.md#pitfalls).

## What to take away

- Small, hard benchmarks are not rescued by hard questions; on HumanEval a gap of 8 to 10 points is needed for significance.
- Noise has two sources, question choice and model sampling, yet is predictable from accuracy and dataset size.
- A higher average is not always better: with a verifier, a model with a modest chance on every question beats one certain on half.

## Sources

- Sida Wang, "Predictable Noise in LLM", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=HV8pugcFVO0).
