# 08. Quality Assurance and Responsible Engineering

Testing and debugging for software whose behavior was learned instead of written.

This part gives a software engineer the testing toolkit for systems that have no specification: how to measure a model-based feature, find where it fails, test generated text, check the data and the code around the model, guard against catastrophic mistakes, and learn safely from real traffic. It closes with the practices that make such a system answerable to the people who use it: planning under uncertainty, versioning, fairness, safety, security, privacy, and accountability.

All examples run on one product: a support system that routes tickets to queues, summarizes conversations, and suggests refunds. Every code listing is plain Python and `pytest`, calls no model, and costs nothing, except where a chapter says the code is illustrative and uses a paid API.

## The chapters

| # | Chapter | Level | Reading |
|---|---|---|---|
| 01 | [Quality Assurance Basics and the Oracle Problem](01-quality-assurance-basics-and-the-oracle-problem.md) | Foundation | 22 min |
| 02 | [Measuring Model Quality](02-measuring-model-quality.md) | Practitioner | 25 min |
| 03 | [Slicing: Finding Where the Model Fails](03-slicing.md) | Practitioner | 28 min |
| 04 | [Testing Without Oracles](04-testing-without-oracles.md) | Practitioner | 26 min |
| 05 | [Testing Generative and LLM Components](05-testing-generative-and-llm-components.md) | Practitioner | 30 min |
| 06 | [Data Quality](06-data-quality.md) | Practitioner | 30 min |
| 07 | [Pipeline Quality](07-pipeline-quality.md) | Practitioner | 28 min |
| 08 | [System Quality: End-to-End Tests and Guardrails](08-system-quality-end-to-end-tests-and-guardrails.md) | Practitioner | 28 min |
| 09 | [Testing and Experimenting in Production](09-testing-and-experimenting-in-production.md) | Practitioner | 28 min |
| 10 | [Process Models: Planning and Iteration](10-process-models-planning-and-iteration.md) | Practitioner | 22 min |
| 11 | [Teams and Technical Debt](11-teams-and-technical-debt.md) | Practitioner | 25 min |
| 12 | [Responsible Engineering, Versioning and Reproducibility](12-responsible-engineering-versioning-and-reproducibility.md) | Practitioner | 26 min |
| 13 | [Explainability, Fairness and Safety](13-explainability-fairness-and-safety.md) | Practitioner | 26 min |
| 14 | [Security, Privacy, Transparency and Accountability](14-security-privacy-transparency-and-accountability.md) | Practitioner | 19 min |

About six hours of reading, and roughly sixteen hours of exercises.

## Where to start

- **New to machine learning.** Read 01 to 05 in order. They build one idea at a time: the missing oracle, an honest score, the slices behind the score, tests that need no labels, and tests for generated text.
- **Shipping an LLM feature soon.** Read 05, 08, and 09, then 12. They cover the test suite, the guardrails, the safe release, and the record that lets you answer questions later.
- **Debugging a live quality problem.** Read 03, then 06, 07, and 09. Find the failing slice, rule out bad data and silent pipeline failures, then measure in production.
- **Asked about responsible engineering.** Read 12 to 14.

## How this part relates to the others

- [Evaluation](../03-evaluation/01-evaluation-is-the-product.md) covers agent-specific evaluation: harnesses, judge design and biases, trajectories, and statistics. This part does not repeat it. [Chapter 05](05-testing-generative-and-llm-components.md) is about putting rubrics and judges into a software test suite.
- [Safety and Security](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) covers threat modeling for agents, prompt injection, and defenses in depth. [Chapter 14](14-security-privacy-transparency-and-accountability.md) stays at the level of the whole system and links there.
- [ML in Production](../07-ml-in-production/04-planning-for-mistakes.md) covers planning for mistakes, deployment, and operations, which chapters 08 and 09 assume.
- [Checklists](../11-professional-practice/07-checklists.md) supports chapters 11 to 14, where most practices only work if someone works through them.

## About the sources

The main source is Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapters 14 to 29. The book is licensed CC BY-NC-ND 4.0. Every chapter here explains the ideas in its own words and links to the book chapter it draws on.

Every statement that a chapter attributes to the book was checked against the chapter text. Where a chapter goes beyond the book, for example the rubric suite in [chapter 05](05-testing-generative-and-llm-components.md) or the two-track plan in [chapter 10](10-process-models-planning-and-iteration.md), the chapter says so, and the book supplies the argument around it.
