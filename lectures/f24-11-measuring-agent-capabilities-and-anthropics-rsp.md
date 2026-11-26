# Lecture guide: Measuring Agent capabilities and Anthropic's RSP

**Lecturer:** Ben Mann (Anthropic) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 11 · **Length:** 46:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=6y2AnWol7oo) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/antrsp.pdf)
**Chapters that cite this lecture:** [06. Evaluating Capabilities and Risks](../03-evaluation/06-evaluating-capabilities-and-risks.md)

> **In one sentence:** Ben Mann explains why measuring capability is hard, how Anthropic's Responsible Scaling Policy ties safety commitments to capability levels, and what computer use adds to the problem.

## Before you watch

Read [Evaluating Capabilities and Risks](../03-evaluation/06-evaluating-capabilities-and-risks.md) first; about half the parts of the lecture have a section there.

## The lecture, part by part

### [0:00–4:30](https://www.youtube.com/watch?v=6y2AnWol7oo&t=0) Measurement and elicitation

The capability you measure is only what you manage to elicit: a prompt that asks for step-by-step reasoning draws out behavior that was already there, and new techniques keep arriving, so a release claim must survive them. With agents, which act in the real world, measurement matters more.
**In this book:** [Evaluating Capabilities and Risks › Why capability evaluation is harder than ordinary evaluation](../03-evaluation/06-evaluating-capabilities-and-risks.md#why-capability-evaluation-is-harder-than-ordinary-evaluation).

### [4:30–10:45](https://www.youtube.com/watch?v=6y2AnWol7oo&t=270) Scaling, a coding demo, and longer tasks ahead

Training compute has grown by about 0.6 orders of magnitude a year, and capability with it; he extrapolates to AI as capable as the best researchers around 2028. A demo shows Claude 3.5 Sonnet writing tests for a buggy function, fixing it and rerunning the tests in a sandbox; today's agent tasks are small, and he expects them to grow to days of work.
**In this book:** nothing beyond this guide; nearest: [How Large Language Models Are Trained › Pre-training compute](../01-foundations/02-how-large-language-models-are-trained.md#pre-training-compute).

### [10:45–22:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=645) The Responsible Scaling Policy and its AI Safety Levels

The Responsible Scaling Policy is modeled on biosafety levels. Each AI Safety Level has capability thresholds and required safeguards, and no model moves up before those are in place: ASL-1 is negligible risk, ASL-2 early signs of danger, ASL-3 a significant increase in misuse risk or signs of self-replication. Each model ships with a testing report.
**In this book:** [Evaluating Capabilities and Risks › 1. Name the levels](../03-evaluation/06-evaluating-capabilities-and-risks.md#1-name-the-levels) · [Evaluating Capabilities and Risks › 2. Set the triggers](../03-evaluation/06-evaluating-capabilities-and-risks.md#2-set-the-triggers).

### [22:00–28:40](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1320) Forecasting with the policy

Biosafety handles pathogens that exist; the policy must forecast levels not yet reached. Benchmarks saturate soon after they are defined, so a 2024 evaluation from METR measures the length of human task a model completes: about 5 minutes, 10 and 30 for three Claude models. The environment counts too: an agent that runs its code beat a stronger reasoner working without one. If safeguards lag capabilities, deployment waits or pauses.
**In this book:** [Evaluating Capabilities and Risks › 5. Forecast the lag](../03-evaluation/06-evaluating-capabilities-and-risks.md#5-forecast-the-lag).

### [28:40–38:30](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1720) Computer use: demo, mechanism, prompt injection, defense in depth

Computer use gives the model tools for mouse, keyboard and screenshots; training started from prompt descriptions, then practice in a sandbox. A demo has Claude edit a website through the laptop's own apps. The risk is indirect prompt injection, such as near-white text ordering data theft. The defense is layered: a disposable virtual machine, an instruction hierarchy and reliable oversight models; the last two, he says, still need solving.
**In this book:** [Jailbreaks and Prompt Injection › The path of an indirect injection](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md#the-path-of-an-indirect-injection) · [Multimodal Agents: Web and Computer Use](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md).

### [38:30–46:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=2310) A second demo; benchmarks and governance

A second demo fills in a vendor form from a spreadsheet and a customer-relationship system; the agent loop keeps Claude acting tool after tool and at some point hands control back to the user. Anthropic cannot measure capabilities alone. SWE-bench Verified and a desktop benchmark are reproducible from containers, general across tasks and languages, and close to the real world. On governance, he describes ceding control to board members who hold no financial stake as AI grows more powerful.
**In this book:** nothing beyond this guide; nearest: [Evaluating Agents: Trajectories and Environments › Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

## What to take away

- A test measures only the capability it manages to elicit; the environment is part of the test.
- Tie safety commitments to capability levels in advance, publish the testing, and expect safeguards to lag.
- Benchmarks saturate fast; make them reproducible and realistic.

## Sources

- Ben Mann, "Measuring Agent capabilities and Anthropic's RSP", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=6y2AnWol7oo).
- Course page: <https://rdi.berkeley.edu/llm-agents/f24/>.
