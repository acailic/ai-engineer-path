# Roadmap

The course has 101 chapters in eleven parts. Few people should read all of them in order. This page gives five paths through them. Each path lists the chapters by week, the hours, the project to do, and what you can do at the end.

If you have never worked with a model, start with path A or path B.

## The five paths

| Path | For whom | Length | Hours a week | Hours in total |
|---|---|---|---|---|
| [A. Fast track](#path-a-fast-track-build-and-evaluate-an-agent-in-four-weeks) | Someone who needs a working agent, and a number for how well it works, within a month | 4 weeks | about 12 | about 47 |
| [B. Full path](#path-b-full-path-from-zero-to-professional-in-sixteen-weeks) | A software engineer with no ML background who wants the whole discipline | 16 weeks | about 4, then about 12 | about 160 |
| [C. Classical ML engineers](#path-c-for-engineers-who-already-know-classical-ml) | Someone who already trains and tests classifiers, and needs the parts that are new with LLMs | 10 weeks | about 8 to 9 | about 85 |
| [D. Edge and efficiency](#path-d-edge-and-efficiency) | Someone who must make a model smaller, faster or cheaper | 6 weeks | about 8 | about 48 |
| [E. Inside language models](#path-e-inside-language-models) | Someone who wants to build a language model from its first pieces | 20 weeks | about 10 | about 200 |

## How the hours were estimated

- **Reading minutes** are estimates, taken from every chapter's header. They are estimates. They assume that you read without stopping to run anything.
- **Exercises** take two to four times the reading time. The paths name the few that matter.
- **Capstones** take from 8 hours for Capstone 4 on a laptop to about 200 hours for Capstone 5.
- **Hours a week** are budgets, not measurements. A week that holds a capstone milestone needs ten hours or more.

A label such as `01.02` means part 01, chapter 02. Every label is a link. When a whole part is read in one week, the link goes to the landing page of that part.

## Path A. Fast track: build and evaluate an agent in four weeks

You read 17 chapters, in 7 hours 20 minutes, and you do Capstone 1. The order follows the rule of the course: the evaluator comes before the agent.

| Week | Read | Do | Hours |
|---|---|---|---|
| 1. The model and the loop | [01.02](01-foundations/02-how-large-language-models-are-trained.md), [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md), [01.05](01-foundations/05-prompting-and-in-context-learning.md), [01.08](01-foundations/08-a-short-history-of-llm-agents.md), [02.01](02-building-agents/01-the-anatomy-of-an-agent.md), [02.02](02-building-agents/02-tool-design-and-function-calling.md) (160 min) | Run [the minimal agent](examples/minimal_agent.py). Do the exercise of 02.01. Capstone 1, milestone 1. | 10 |
| 2. The evaluator, before the agent | [11.01](11-professional-practice/01-how-to-ship-an-llm-feature-end-to-end.md), [03.01](03-evaluation/01-evaluation-is-the-product.md), [03.02](03-evaluation/02-a-minimal-eval-harness.md), [03.05](03-evaluation/05-statistics-for-evals.md) (100 min) | Run [the evaluation harness](examples/eval_harness.py) and [the statistics](examples/eval_stats.py). Capstone 1, milestone 2. | 11 |
| 3. Make it safe | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md), [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md), [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md), [07.04](07-ml-in-production/04-planning-for-mistakes.md) (110 min) | Capstone 1, milestone 3. Add the policy gate from 04.04. Write the mistake analysis and the threat model (steps 5 and 6 of 11.01). | 13 |
| 4. Ship and watch | [03.07](03-evaluation/07-evals-in-production.md), [07.10](07-ml-in-production/10-planning-for-operations.md), [11.07](11-professional-practice/07-checklists.md) (70 min) | Capstone 1, milestones 4 and 5. Write the rollout levels and the dashboard (steps 7 and 8 of 11.01). | 13 |

**Capstone:** [Capstone 1: A Task Agent with Evals](11-professional-practice/02-capstone-task-agent-with-evals.md), about 30 hours without its stretch goals.

**At the end you can** do five things. Build an agent with tools in a fake, resettable environment. Write an evaluation set of 30 tasks with expected outcomes. Report success with a standard error, pass^k and cost. Threat-model the agent and gate its tool calls in code. Roll it out in levels, with stop conditions and a dashboard.

**What you skip:** judges (03.03), trajectories (03.04), the rest of security (04.03 and 04.05 to 04.09), classical ML in production (parts 07 and 08), and how models are built (parts 09 and 10). Path B covers all of it.

## Path B. Full path: from zero to professional in sixteen weeks

Every chapter, in order, with three capstones. Reading is 35 hours. The capstones are 95 to 125 hours. The first four weeks are light. From week 5 on, plan for about 12 hours a week.

| Week | Read | Do | Hours |
|---|---|---|---|
| 1 | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) to [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) (110 min) | The exercise of 01.04: what an API call costs and takes. | 4 |
| 2 | [01.05](01-foundations/05-prompting-and-in-context-learning.md) to [01.08](01-foundations/08-a-short-history-of-llm-agents.md) (100 min) | The exercise of 01.05: version and test one prompt. | 4 |
| 3 | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) to [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) (120 min) | Run the minimal agent. Do the exercise of 02.01. | 5 |
| 4 | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) to [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) (105 min) | One memory exercise from 02.04, on a long task. | 4 |
| 5 | [03.01](03-evaluation/01-evaluation-is-the-product.md) to [03.05](03-evaluation/05-statistics-for-evals.md), [11.02](11-professional-practice/02-capstone-task-agent-with-evals.md) (140 min) | Run the harness and the statistics. Capstone 1, milestone 1. | 12 |
| 6 | [03.06](03-evaluation/06-evaluating-capabilities-and-risks.md) to [03.08](03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md), [11.01](11-professional-practice/01-how-to-ship-an-llm-feature-end-to-end.md) (80 min) | Capstone 1, milestone 2. | 12 |
| 7 | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) to [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) (105 min) | Capstone 1, milestone 3. | 12 |
| 8 | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) to [04.09](04-safety-and-security/09-policy-governance-and-standards.md), [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) (140 min) | Capstone 1, milestones 4 and 5. | 12 |
| 9 | All of [part 05](05-frameworks-and-multi-agent/README.md) and [part 06](06-frontier-applications/README.md) (147 min) | Capstone 2, milestones 1 and 2. | 12 |
| 10 | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) to [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) (120 min) | The exercises of 07.02 and 07.04: a baseline, then a mistake analysis. Capstone 2, milestone 3. | 12 |
| 11 | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) to [07.10](07-ml-in-production/10-planning-for-operations.md), [11.04](11-professional-practice/04-capstone-model-to-product.md) (145 min) | Capstone 2, milestone 4. | 12 |
| 12 | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) to [08.07](08-quality-assurance/07-pipeline-quality.md) (177 min) | Capstone 2, milestone 5. | 13 |
| 13 | [08.08](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) to [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) (145 min) | Capstone 3, milestones 1 and 2. | 12 |
| 14 | [09.01](09-efficient-deep-learning/01-why-efficiency-matters.md) to [09.06](09-efficient-deep-learning/06-knowledge-distillation.md), [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md), [11.05](11-professional-practice/05-capstone-efficient-inference.md) (147 min) | The exercise of 09.04. Capstone 3, milestone 3. | 12 |
| 15 | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md), [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) to [09.17](09-efficient-deep-learning/17-course-summary-and-outlook.md), [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) to [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md), [10.08](10-llm-internals/08-inference.md), [10.09](10-llm-internals/09-evaluating-language-models.md), [10.13](10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) (151 min) | Capstone 3, milestone 4. | 12 |
| 16 | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) to [10.07](10-llm-internals/07-scaling-laws.md), [10.10](10-llm-internals/10-training-data.md) to [10.12](10-llm-internals/12-alignment-and-multimodality.md), [11.06](11-professional-practice/06-capstone-train-a-small-language-model.md) to [11.08](11-professional-practice/08-staying-current.md) (174 min) | Capstone 3, milestone 5. Check it with the checklists of 11.07. Write your sources file (11.08). | 13 |

**Capstones:** [Capstone 1](11-professional-practice/02-capstone-task-agent-with-evals.md), [Capstone 2](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) and [Capstone 3](11-professional-practice/04-capstone-model-to-product.md), in that order. If efficiency matters more to you than classical ML, do [Capstone 4](11-professional-practice/05-capstone-efficient-inference.md) in weeks 14 and 15 instead of Capstone 3.

**At the end you can** ship one LLM feature end to end, with every artifact from the goal page to the dashboard. You can run an evaluation with error bars and a gate. You can run a security review and measure an injection monitor. You can take a classical ML feature from a request to a monitored service. You can read a paper or a model release critically, and say what each part of a language model costs.

## Path C. For engineers who already know classical ML

You already know training sets, test sets and precision. You need the parts that are new: sampling noise, agents, judges, prompt injection and post-training. You read 62 chapters and skim 15. A skimmed chapter takes about a quarter of its reading time.

| Week | Read | Do | Hours |
|---|---|---|---|
| 1 | [01.02](01-foundations/02-how-large-language-models-are-trained.md) to [01.08](01-foundations/08-a-short-history-of-llm-agents.md) (185 min). Skim 01.01. | The exercise of 01.07: add error bars to a score you already have. | 5 |
| 2 | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) to [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) (120 min) | The exercises of 02.01 and 02.02. | 6 |
| 3 | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) to [02.08](02-building-agents/08-training-models-for-agentic-tasks.md), [03.01](03-evaluation/01-evaluation-is-the-product.md) to [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) (170 min) | Run the harness and the statistics. | 7 |
| 4 | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) to [03.08](03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md), [11.01](11-professional-practice/01-how-to-ship-an-llm-feature-end-to-end.md), [11.02](11-professional-practice/02-capstone-task-agent-with-evals.md) (155 min) | Capstone 1, milestones 1 and 2. | 11 |
| 5 | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) to [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) (125 min) | Capstone 1, milestone 3. | 9 |
| 6 | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) to [04.09](04-safety-and-security/09-policy-governance-and-standards.md), [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) (120 min) | Capstone 1, milestones 4 and 5. | 12 |
| 7 | All of [part 05](05-frameworks-and-multi-agent/README.md) and [part 06](06-frontier-applications/README.md) (147 min) | Capstone 2, milestones 1 and 2. | 10 |
| 8 | 07.03, 07.04, 07.07 (85 min). 08.03, 08.05 (58 min). Skim the rest of [part 07](07-ml-in-production/README.md) and [part 08](08-quality-assurance/README.md). | Capstone 2, milestone 3. | 9 |
| 9 | 07.08, 07.10 (55 min). 08.08, 08.09, 08.12 (74 min). [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md), [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md), [10.13](10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) (47 min) | Capstone 2, milestone 4. | 10 |
| 10 | [11.07](11-professional-practice/07-checklists.md), [11.08](11-professional-practice/08-staying-current.md) (40 min). Optional: [09.04](09-efficient-deep-learning/04-quantization.md), [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) (46 min) | Capstone 2, milestone 5. Check both capstones with the checklists. | 8 |

In weeks 8 and 9, the part 07 and part 08 chapters are numbered as in the [table of contents](README.md#table-of-contents).

**Capstones:** Capstone 1 in full, and Capstone 2. Capstone 1 has a stretch goal that plays to your background: a judge calibrated against your own labels.

**At the end you can** do everything the fast track promises. You can also measure a detector as a classifier, with held-out attacks and hard negatives. And you can say what transfers from classical ML, such as held-out data, baselines and mistake analysis, and what is new, such as sampling noise, injection, judges and post-training.

## Path D. Edge and efficiency

Come here after path A, or after chapters 01.02 and 03.02. You read 22 chapters, in 6 hours 45 minutes, and you do Capstone 4.

| Week | Read | Do | Hours |
|---|---|---|---|
| 1 | [09.01](09-efficient-deep-learning/01-why-efficiency-matters.md) to [09.04](09-efficient-deep-learning/04-quantization.md) (70 min) | The exercise of 09.04: quantize a small classifier. Capstone 4, milestone 1. | 7 |
| 2 | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) to [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) (52 min) | Capstone 4, milestones 2 and 3 on track A: the table for float, 8-bit and 4-bit. | 9 |
| 3 | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md), [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md), [10.08](10-llm-internals/08-inference.md) (54 min) | Capstone 4, milestones 1 to 3 on track B: a small open language model. | 9 |
| 4 | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md), [09.17](09-efficient-deep-learning/17-course-summary-and-outlook.md), [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md), [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) (58 min) | Capstone 4, milestone 4, optional: one pruning or distillation pass. | 7 |
| 5 | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md), [10.06](10-llm-internals/06-parallelism.md) (31 min). [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md), [07.07](07-ml-in-production/07-deploying-a-model.md), [07.09](07-ml-in-production/09-scaling-the-system.md) (70 min) | Capstone 4, milestone 5: measure again and write the report. | 8 |
| 6 | [03.02](03-evaluation/02-a-minimal-eval-harness.md), [03.05](03-evaluation/05-statistics-for-evals.md), [11.05](11-professional-practice/05-capstone-efficient-inference.md) (70 min) | Tighten the quality evaluation: error bars and a written limit. Review the report against the brief. | 9 |

**Capstone:** [Capstone 4: Efficient Inference](11-professional-practice/05-capstone-efficient-inference.md), both tracks.

**At the end you can** measure a model's latency, memory and quality on named hardware. You can quantize it to 8-bit and 4-bit, and prune or distill it. You can size a language model's weights and its cache of past tokens, choose a serving form, and report the trade-off with a spread, a date and a machine.

## Path E. Inside language models

Capstone 5 is the path. You read part 10 in full and five chapters from other parts, 5 hours 25 minutes in all. You build a tokenizer, a Transformer, an optimizer and a training loop. Then you make the training fast, fit a scaling law, build the data pipeline and align the model. The hours are the project's own estimate.

| Weeks | Read | Do | Hours |
|---|---|---|---|
| 1 to 2 | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md), [10.13](10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md), [01.02](01-foundations/02-how-large-language-models-are-trained.md) (60 min) | Capstone 5, stage 1: the tokenizer. | 10 |
| 3 to 10 | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md), [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md), [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) (61 min) | Stage 2: the model, the optimizer and the training loop. | 10 |
| 11 to 14 | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) to [10.08](10-llm-internals/08-inference.md), [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md), [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) (119 min) | Stage 3: profiling, one optimization, a scaling-law fit. | 10 |
| 14 to 17 | [10.10](10-llm-internals/10-training-data.md) (16 min) | Stage 4: the data pipeline. | 10 |
| 17 to 20 | [10.09](10-llm-internals/09-evaluating-language-models.md), [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md), [10.12](10-llm-internals/12-alignment-and-multimodality.md), [11.06](11-professional-practice/06-capstone-train-a-small-language-model.md) (70 min) | Stage 5: instruction tuning, then RLVR with a math grader. | 10 |

**Capstone:** [Capstone 5: Train a Small Language Model](11-professional-practice/06-capstone-train-a-small-language-model.md). Stages 1 and 2 are a complete project of about ten weeks.

**At the end you can** train a small language model from scratch. You can read a profiler and make one optimization on evidence. You can fit a scaling law and predict before you spend. You can build a data pipeline from HTML to text, and run instruction tuning and RLVR. And you can read the rest of part 10 as a map of work you have done.

## If you fall behind

- Every capstone has a "first hour" section. It is the restart point.
- A path is a budget. Keep the order, drop the stretch goals, and keep the evaluator ahead of the agent.
- When a path is done, [Staying Current](11-professional-practice/08-staying-current.md) says what to follow.
