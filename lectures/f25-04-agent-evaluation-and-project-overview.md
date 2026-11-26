# Lecture guide: Agent Evaluation & Project Overview

**Lecturer:** Berkeley course staff · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 4 · **Length:** 1:36:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=VfOA2a0dj4w) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/LLM Agent Evaluations & Project Overview.pdf)
**Chapters that cite this lecture:** [01. Evaluation Is the Product](../03-evaluation/01-evaluation-is-the-product.md) · [02. A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md) · [03. LLM-as-a-Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md) · [04. Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md) · [05. Statistics for Evals: Error Bars and Significance](../03-evaluation/05-statistics-for-evals.md) · [08. Case Study: Berkeley's Green Agent and White Agent Project](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)

> **In one sentence:** The course staff explain how to evaluate LLM agents and what makes an agent benchmark good, then set out what the green agent, the evaluator of the course project, must do.

## Before you watch

Read [Case Study: Berkeley's Green Agent and White Agent Project](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) before the second half of the lecture.

## The lecture, part by part

### [0:00–10:45](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=0) Why evaluation matters, and what kinds of tasks there are

Evaluation gives a systematic, reproducible measure of a model or agent at every step, from the training loss to a published benchmark. Agents are harder to evaluate than bare models because they also plan, call tools and keep memory. Closed-ended tasks have few possible answers; open-ended tasks accept any text.
**In this book:** [Evaluation Is the Product › Why this matters](../03-evaluation/01-evaluation-is-the-product.md#why-this-matters) · [LLM-as-a-Judge and Rubrics › 1. Decide whether you need a judge](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#1-decide-whether-you-need-a-judge).

### [10:45–20:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=645) Verifiable and non-verifiable tasks; human and LLM judges

An open-ended task is verifiable when an oracle can check the output; otherwise quality is a matter of degree. People are the gold standard but slow and inconsistent; an LLM judge is cheaper yet sometimes less reliable, random and biased, so it should be run several times and checked against a small human-labeled sample.
**In this book:** [LLM-as-a-Judge and Rubrics › 1. Decide whether you need a judge](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#1-decide-whether-you-need-a-judge) · [LLM-as-a-Judge and Rubrics › 5. Calibrate against human labels](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#5-calibrate-against-human-labels).

### [20:00–28:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1200) Static and dynamic benchmarks; a taxonomy of agent benchmarks

A static benchmark keeps its test cases fixed, which makes results reproducible but lets training data absorb them. A dynamic one regenerates cases periodically, so it stays current and is harder to game. Benchmarks for agents then fall into three groups: those that test one capability, such as planning, tool calling or memory; those that test one application, such as web browsing, software engineering (SWE-bench Verified), cybersecurity (CyberGym, RedCode), science, law or finance; and those that cover many applications.
**In this book:** [Evaluating Agents: Trajectories and Environments › Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [28:00–34:30](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1680) Task validity, outcome validity and judging text

A good evaluation needs task validity (success really requires the capability tested) and outcome validity (the grader's verdict matches true success). String matching must accept equivalent wording and resist guessing; an LLM judge must be accurate, consistent and immune to hidden pleas for full marks.
**In this book:** [A Minimal Evaluation Harness › 3. Write the graders](../03-evaluation/02-a-minimal-eval-harness.md#3-write-the-graders).

### [34:30–42:30](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=2070) Judging code and state; what a benchmark needs

Generated code needs diverse unit tests; multi-step tasks need the environment's state checked at each step. Evaluations fail through noisy data, toy problems, hackable graders and tasks every model solves. A good agentic benchmark states goal, task, environment and metrics, and is relevant, graded in difficulty, hard to contaminate and slow to saturate.
**In this book:** [Evaluating Agents: Trajectories and Environments › 5. Grade the outcome from the state](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#5-grade-the-outcome-from-the-state) · [Evaluating Agents: Trajectories and Environments › 1. Define a task as three things](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#1-define-a-task-as-three-things).

### [42:30–48:30](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=2550) Case study: reproducing vulnerabilities with CyberGym

The agent gets a vulnerability description and the code before the fix, and must write an input that triggers the bug in a sandbox. Tasks come from the ARVO dataset and from real-world vulnerabilities found by OSS-Fuzz, an open-source fuzzing project. Success is an observed crash, and vulnerabilities found after a model's cutoff expose contamination.
**In this book:** [Evaluating Agents: Trajectories and Environments › Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [48:30–56:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=2910) Case study: tool agents under policy

In τ-bench, an agent serves a simulated user through APIs while obeying a policy document. Success is decided by comparing the final database state with the goal state, reported as average success and as the rate of succeeding several times running. Its successor τ2-bench gives the user tools too, composes tasks from sub-tasks and asserts on single steps.
**In this book:** [Evaluating Agents: Trajectories and Environments › 3. Add a user simulator](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#3-add-a-user-simulator) · [Evaluating Agents: Trajectories and Environments › 8. Report reliability, and the simulator's health](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#8-report-reliability-and-the-simulators-health).

### [56:00–1:04:45](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3360) Case studies: knowledge work and enterprise workflows

GDPval, a benchmark from OpenAI, gives models realistic assignments written by professionals, with reference files, and has blinded experts compare the deliverables with their own, recording time and cost as well. CRMArena, built on Salesforce's sandbox, tests customer-relationship workflows for service, analyst and manager roles on synthetic data; it scores knowledge questions with F1 and the other tasks by exact match on identifiers, and reports reliability over repeated runs and efficiency in turns, tokens and dollars.
**In this book:** [Evaluating Agents: Trajectories and Environments › Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [1:04:45–1:14:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3885) Green agents

A green agent is the examiner: it defines the assessment, prepares the environment, hands out tasks, collects results and reports its own metrics to the platform over A2A, MCP or plain APIs. It needs a task dataset, a test procedure and an environment with tools; a prompt-based toolkit yields a prototype, but students taking more than one unit are expected to hand-code theirs.
**In this book:** [Case Study: Berkeley's Green Agent and White Agent Project › What the green agent must do](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md#what-the-green-agent-must-do).

### [1:14:00–1:22:30](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=4440) Type 1: integrate an existing benchmark

A type 1 green agent wraps a published benchmark and reuses its metrics in three steps: integrate, analyse the benchmark's quality, then correct and expand it. SWE-bench Verified shows why: of 1,700 tasks reviewed by 93 developers, 68.3% were removed, and GPT-4o resolves 33.2% of the Verified tasks, against about 16% on the original benchmark with the best scaffold.
**In this book:** [Case Study: Berkeley's Green Agent and White Agent Project › Two kinds of project](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md#two-kinds-of-project).

### [1:22:30–1:30:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=4950) Type 2: a new benchmark; the build checklist

A type 2 project proposes a new benchmark of realistic tasks that need an agent, with automatic or lightweight human checks; multi-agent tasks are encouraged. The checklist: choose the task, design the environment, define the metrics early, beyond success alone, then write test cases with enough coverage.
**In this book:** [Case Study: Berkeley's Green Agent and White Agent Project › Two kinds of project](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md#two-kinds-of-project).

### [1:30:00–1:36:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5400) Grading

New benchmarks are graded on goal, novelty, scope and scale, evaluator quality, reliability and realism; integrated ones the same way, with faithfulness to the original results in place of novelty. A conference checklist for datasets and benchmarks is recommended.
**In this book:** [Case Study: Berkeley's Green Agent and White Agent Project › How submissions are scored](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md#how-submissions-are-scored).

## What to take away

- Evaluation is needed at every step of building a model; for agents it must also cover tools, environment state and cost.
- Where a task has an oracle, the evaluation only has to follow the criteria; otherwise use human or LLM judges, and cross-check an LLM judge with a small human evaluation.
- A benchmark is itself something to evaluate: task validity, outcome validity, contamination and saturation.

## Sources

- Berkeley course staff, "Agent Evaluation & Project Overview", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=VfOA2a0dj4w).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25/>.
