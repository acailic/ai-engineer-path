# Part 3 — Evaluation: Knowing Whether It Works

You built a small agent in Part 2. This part answers the question that follows: does it work, where does it fail, and how do you stop it from getting worse?

Evaluation is treated here as a software engineering activity. A harness is test infrastructure. A dataset is a set of fixtures. A judge is a flaky oracle that must be calibrated before you trust it. The part draws on UC Berkeley's LLM-agent MOOCs of 2024 and 2025, on Christian Kästner's *Machine Learning in Production* (MIT Press, 2025), and on the papers those lectures assign.

## The chapters

| # | Chapter | Level | Read | After it you can |
|---|---|---|---|---|
| 01 | [Evaluation Is the Product](01-evaluation-is-the-product.md) | Practitioner | 20 min | Place any "does it work" question at one of four levels and run a development loop driven by evidence |
| 02 | [A Minimal Evaluation Harness](02-a-minimal-eval-harness.md) | Practitioner | 25 min | Run a 170-line Python harness with no API key and read its report |
| 03 | [LLM-as-a-Judge and Rubrics](03-llm-as-a-judge-and-rubrics.md) | Practitioner | 20 min | Write a rubric, turn it into a judge prompt, and calibrate the judge against human labels |
| 04 | [Evaluating Agents: Trajectories and Environments](04-evaluating-agents-trajectories-and-environments.md) | Practitioner | 25 min | Grade an agent on its route and on the state it leaves behind, in a resettable fake environment |
| 05 | [Statistics for Evals: Error Bars and Significance](05-statistics-for-evals.md) | Practitioner | 25 min | Compute a standard error and a paired comparison, and recognize a difference that is not evidence |
| 06 | [Evaluating Capabilities and Risks](06-evaluating-capabilities-and-risks.md) | Professional | 15 min | Explain a dangerous-capability evaluation and a responsible scaling policy, and write capability tiers |
| 07 | [Evals in Production](07-evals-in-production.md) | Practitioner | 20 min | Trace every attempt, choose online metrics, gate changes, and feed failures back into the dataset |
| 08 | [Case Study: Berkeley's Green Agent and White Agent Project](08-case-study-the-green-agent-and-white-agent-project.md) | Practitioner | 15 min | Describe a course project that asks students to build the evaluator first |

## How to read this part

Read the chapters in order the first time. Each one assumes the harness of chapter 02.

- **With one hour:** chapters 01, 02 and 05. They cover the loop, the tool and the arithmetic that tells you whether a change mattered.
- **If your output is open-ended:** go on to chapter 03.
- **If your agent uses tools:** chapter 04 is the one you cannot skip.
- **Before anything ships:** chapter 07.
- **Before you grant permissions:** chapter 06.

You need to be comfortable with Python, Git and the terminal. You do not need a machine-learning background. Part 2, [the anatomy of an agent](../02-building-agents/01-the-anatomy-of-an-agent.md), is the only real prerequisite.

## One running example

The same customer-support agent that refunds orders appears in every chapter. It is asked for a refund on order #1042. It has to authenticate the customer, look the order up, and refund once. It also has to refuse order #9999, which does not exist.

That one task shows every idea in the part:

- **Four levels.** The intent is parsed correctly, the route skips a step, the end state is right, and a customer complains a week later.
- **Two metrics that disagree.** The agent succeeds at least once in four tries every time, and succeeds all four times far less often.
- **A flaky oracle.** A judge passes one in four of the answers that a person rejects.
- **A paired comparison.** Version A beats version B on 15 tasks and loses on 4.

## Code you can run

| File | Chapter | Needs |
|---|---|---|
| `eval_harness.py` | 02 | Python 3.8 or newer, standard library only |
| `eval_stats.py` | 05 | The same |
| A fake environment with an end-state check | 04 | The same |
| A trace reader and a regression gate | 07 | `eval_harness.py` in the same folder |

The harness and the statistics file print the numbers shown in their chapters. Run them with `python3 -I <file>` so that nothing from your machine interferes. The two snippets that call a model are marked as illustrative.

## What this part does not cover

- **General testing of ML systems:** the oracle problem, slicing, and production experiments are in Part 8. Start with [quality assurance basics](../08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md).
- **Attacks on agents:** Part 4, starting with [threat modeling](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md).
- **Building the agent itself:** Part 2.

## Where it leads

The case study in chapter 08 is the basis of two capstone projects in Part 11: integrate an existing benchmark as an evaluator, with a quality analysis, or build a new small benchmark with its own rubric and validation. Everything in this part is preparation for those.

## Lecture guides for this part

Each guide maps one lecture from its first minute to its last and says where this book teaches each piece. Where no chapter teaches a part of the lecture, the guide explains it itself; the table counts those parts.

| Lecture | Lecturer | Length | Parts no chapter teaches | Guide |
|---|---|---|---|---|
| Agent Evaluation & Project Overview | Berkeley course staff | 1:36:00 | 0 of 12 | [open guide](../lectures/f25-04-agent-evaluation-and-project-overview.md) |
| Practical Lessons from Deploying Real-World AI Agents | Clay Bavor (Sierra) | 48:00 | 5 of 16 | [open guide](../lectures/f25-09-practical-lessons-from-deploying-real-world-ai.md) |
| Measuring Agent capabilities and Anthropic's RSP | Ben Mann (Anthropic) | 46:00 | 1 of 6 | [open guide](../lectures/f24-11-measuring-agent-capabilities-and-anthropics-rsp.md) |

## Sources

- **Lectures:** Berkeley course staff, "LLM Agent Evaluations & Project Overview" (Fall 2025); Clay Bavor, "Practical Lessons from Deploying Real-World AI Agents" (Fall 2025); Sida Wang, "Predictable Noise in LLM Benchmarks" (Fall 2025); Ben Mann, "Measuring Agent Capabilities and Anthropic's RSP" (Fall 2024).
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapters 14 and 15.
- **Readings:** Yehudai et al., *A Survey on Evaluation of LLM-based Agents*; Yao et al., *τ-bench*; Barres et al., *τ²-Bench*; Miller, *Adding Error Bars to Evals*; Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
