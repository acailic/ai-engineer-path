# AI Engineer Path

A free, self-contained course that takes a software engineer **with no machine-learning background to a professional level** in building with large language models: how the models work, how to build agents, how to evaluate them, how to secure them, how to ship them, and how to run them cheaply.

It has 101 chapters in eleven parts, five capstone projects, five checklists and four runnable example programs. Everything here is synthesized from four open university sources and links back to them.

You can also read it as a website: **[acailic.github.io/ai-engineer-path](https://acailic.github.io/ai-engineer-path/)**. Every page there has a **Read aloud** button that reads the page to you with your browser's own voices, follows the text, and lets you change the speed and the voice. It works in Chrome, Edge and Safari, on a computer and on a phone; it needs no account.

Start with [how to use this repository](#how-to-use-this-repository). If you already know what you want, go to the [roadmap](ROADMAP.md), the [table of contents](#table-of-contents) or the [glossary](GLOSSARY.md).

## Who it is for

A software engineer who has never worked with ML or LLMs, who is comfortable with Python, Git and the terminal, and who wants to get from zero to professional level. You do not need to have trained a model. You do need the habit of asking what a component assumes, what happens when it fails, and how you would know.

## What "professional level" means here

It means you can do seven things for a system that contains a language model:

- **Decide.** Say no to ML when a rule would do, with a measured baseline as evidence, and state what "good enough" is as a number.
- **Build.** Write an agent loop, tools with contracts and error messages, and a workflow when the steps do not vary.
- **Evaluate.** Build the evaluator before the features, report error bars, reliability and cost, and test the evaluator itself.
- **Secure.** Threat-model the system, gate every action in code, and measure an injection suite.
- **Ship.** Plan for mistakes, roll out in levels with stop conditions, monitor whether the model was right, and rehearse the rollback.
- **Make it cheap.** Measure latency, memory and quality, and compress a model without losing what it can do.
- **Explain.** Describe how a language model is trained, from tokens to post-training, and read a paper or a model release critically.

It does not mean training a frontier model. It does not replace experience with your own users and data.

## How to use this repository

**1. The full path.** Sixteen weeks from zero: every chapter in order, with three capstones. Plan on about 4 hours a week for the first month and about 12 after that. This is [path B of the roadmap](ROADMAP.md#path-b-full-path-from-zero-to-professional-in-sixteen-weeks).

**2. The fast track.** Four weeks to a working agent and a number for how well it works: 17 chapters and Capstone 1, at about 12 hours a week. This is [path A](ROADMAP.md#path-a-fast-track-build-and-evaluate-an-agent-in-four-weeks).

**3. Look it up by problem.** Each row names the chapters that teach the fix.

| Your problem | Go to |
|---|---|
| I cannot tell whether it works | [Evaluation Is the Product](03-evaluation/01-evaluation-is-the-product.md), [A Minimal Evaluation Harness](03-evaluation/02-a-minimal-eval-harness.md) |
| The score moves between runs | [Why LLM Outputs Are Noisy](01-foundations/07-why-llm-outputs-are-noisy.md), [Statistics for Evals](03-evaluation/05-statistics-for-evals.md) |
| No program can grade the output | [LLM-as-a-Judge and Rubrics](03-evaluation/03-llm-as-a-judge-and-rubrics.md), [Testing Generative and LLM Components](08-quality-assurance/05-testing-generative-and-llm-components.md) |
| The agent loops, calls the wrong tool, or never stops | [The Anatomy of an Agent](02-building-agents/01-the-anatomy-of-an-agent.md), [Tool Design and Function Calling](02-building-agents/02-tool-design-and-function-calling.md) |
| It invents facts | [Agents in the Enterprise](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md), [Planning for Mistakes](07-ml-in-production/04-planning-for-mistakes.md) |
| It reads web pages, mail or documents written by strangers | [Threat Modeling LLM Applications and Agents](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md), [Jailbreaks and Prompt Injection](04-safety-and-security/02-jailbreaks-and-prompt-injection.md), [Defenses: Guardrails, Detection and Secure Design](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| It worked in the demo and fails in production | [Evals in Production](03-evaluation/07-evals-in-production.md), [Testing and Experimenting in Production](08-quality-assurance/09-testing-and-experimenting-in-production.md), [Planning for Operations](07-ml-in-production/10-planning-for-operations.md) |
| A wrong answer would be expensive | [Planning for Mistakes](07-ml-in-production/04-planning-for-mistakes.md), [System Quality: End-to-End Tests and Guardrails](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) |
| It costs too much or answers too slowly | [Using LLMs: Tokens, Context and Sampling](01-foundations/04-using-llms-tokens-context-and-sampling.md), [Quantization](09-efficient-deep-learning/04-quantization.md), [Efficient LLM Inference and Deployment](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| I must ship it, or explain it to my team | [How to Ship an LLM Feature End to End](11-professional-practice/01-how-to-ship-an-llm-feature-end-to-end.md), [Checklists for Shipping AI Systems](11-professional-practice/07-checklists.md) |
| A paper or a model release claims a large gain | [Staying Current](11-professional-practice/08-staying-current.md), [Statistics for Evals](03-evaluation/05-statistics-for-evals.md) |
| I want to know how the model is built | [How Large Language Models Are Trained](01-foundations/02-how-large-language-models-are-trained.md), [The Language Modeling Pipeline and Tokenization](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md), [Capstone 5](11-professional-practice/06-capstone-train-a-small-language-model.md) |

**Run the examples.** The [`examples/`](examples/README.md) folder holds four complete listings from the chapters, saved as runnable files: [a minimal agent](examples/minimal_agent.py), [three tools in the agent-computer-interface style](examples/agent_computer_interface.py), [an evaluation harness](examples/eval_harness.py) and [the arithmetic of error bars](examples/eval_stats.py). Each needs Python 3.10 or newer and nothing else: no packages, no API key, no network. From that folder, run `python3 minimal_agent.py`.

**Do a capstone.** Part 11 holds five projects whose acceptance criteria you can test without a teacher: a task agent with evals (30 to 40 hours), a monitoring agent for prompt injection (30 to 40), a classical ML feature taken to product (35 to 45), an efficient-inference report (8 to 25), and a small language model trained from scratch (about 200, over 20 weeks).

## Lecture guides

One guide per lecture of the four courses, in [`lectures/`](lectures/README.md). A guide maps a whole lecture, part by part, and names for each part the chapter section that teaches the same thing; where no chapter teaches it, the guide explains the part itself.

**All 77 guides are written, one for each lecture of the four courses (complete on 2026-11-26).** The table is regenerated from the files.

| Course | Guides | Lectures |
|---|---|---|
| UC Berkeley LLM Agents MOOC (Fall 2024) | 12 | 12 |
| UC Berkeley Advanced LLM Agents MOOC (Spring 2025) | 12 | 12 |
| UC Berkeley Agentic AI MOOC (Fall 2025) | 12 | 12 |
| MIT 6.5940 TinyML and Efficient Deep Learning Computing (Fall 2024) | 23 | 23 |
| Stanford CS336 Language Modeling from Scratch (Spring 2026) | 18 | 18 |

In the guides: 1,207 parts of lectures, of which 230 (19%) are taught by no chapter and are explained only in the guide.

What is checked: each guide passes an automatic check before it is published (the parts cover the lecture end to end, every part links to its moment in the video, every link to a chapter section resolves, no passage is copied from the lecture). What is not checked: nobody has read a guide a second time against the lecture. If a guide and the lecture disagree, the lecture wins.

## Table of contents

### [Part 01 · Foundations: how LLMs work and how to use them](01-foundations/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [Machine Learning in a Nutshell for Software Engineers](01-foundations/01-machine-learning-in-a-nutshell.md) | Foundation | 25 min | A model is fitted to data; quality is a statistic |
| [How Large Language Models Are Trained](01-foundations/02-how-large-language-models-are-trained.md) | Foundation | 30 min | Next-token prediction, pre-training, the base model |
| [From Base Model to Assistant: Post-Training](01-foundations/03-from-base-model-to-assistant-post-training.md) | Practitioner | 30 min | SFT, preference tuning, RLVR, open recipes |
| [Using LLMs: Tokens, Context and Sampling](01-foundations/04-using-llms-tokens-context-and-sampling.md) | Foundation | 25 min | Tokens, the context window, temperature, cost and latency |
| [Prompting and In-Context Learning](01-foundations/05-prompting-and-in-context-learning.md) | Foundation | 25 min | Instructions, examples, versioned and tested prompts |
| [Reasoning in LLMs: From Chain-of-Thought to Search](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) | Practitioner | 30 min | Self-consistency, search, compute at inference time |
| [Why LLM Outputs Are Noisy, and What To Do About It](01-foundations/07-why-llm-outputs-are-noisy.md) | Practitioner | 25 min | Sampling noise, semantic noise, error bars |
| [A Short History of LLM Agents](01-foundations/08-a-short-history-of-llm-agents.md) | Foundation | 20 min | What an agent is; the workflow-to-agent spectrum |

### [Part 02 · Building agents](02-building-agents/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [The Anatomy of an Agent](02-building-agents/01-the-anatomy-of-an-agent.md) | Practitioner | 30 min | The five parts of an agent; a loop in plain Python |
| [Tool Design and Function Calling](02-building-agents/02-tool-design-and-function-calling.md) | Practitioner | 30 min | Contracts, descriptions, error messages, retries |
| [Planning, Search and Decision-Making](02-building-agents/03-planning-search-and-decision-making.md) | Practitioner | 30 min | Six ways an agent chooses its next action |
| [Memory and Knowledge for Agents](02-building-agents/04-memory-and-knowledge-for-agents.md) | Practitioner | 30 min | Compaction, long-term memory, retrieval |
| [Compound AI Systems and DSPy](02-building-agents/05-compound-ai-systems-and-dspy.md) | Practitioner | 30 min | Pipelines of narrow model calls, and optimizing them |
| [How Agent System Designs Evolve](02-building-agents/06-how-agent-system-designs-evolve.md) | Practitioner | 15 min | A timeline from wrappers to context engineering |
| [Coding Agents](02-building-agents/07-coding-agents.md) | Practitioner | 30 min | Sandboxes, action spaces, the agent-computer interface |
| [Training Models for Agentic Tasks](02-building-agents/08-training-models-for-agentic-tasks.md) | Professional | 30 min | Trajectories, verifiers, reward hacking |

### [Part 03 · Evaluation: knowing whether it works](03-evaluation/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [Evaluation Is the Product](03-evaluation/01-evaluation-is-the-product.md) | Practitioner | 20 min | Four levels of evaluation; a loop driven by evidence |
| [A Minimal Evaluation Harness](03-evaluation/02-a-minimal-eval-harness.md) | Practitioner | 25 min | A plain-Python harness: metrics, slices, a gate |
| [LLM-as-a-Judge and Rubrics](03-evaluation/03-llm-as-a-judge-and-rubrics.md) | Practitioner | 20 min | Rubrics, judge biases, calibration against people |
| [Evaluating Agents: Trajectories and Environments](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) | Practitioner | 25 min | Outcomes, routes, resettable environments, user simulators |
| [Statistics for Evals: Error Bars and Significance](03-evaluation/05-statistics-for-evals.md) | Practitioner | 25 min | Standard errors, intervals, paired comparisons |
| [Evaluating Capabilities and Risks](03-evaluation/06-evaluating-capabilities-and-risks.md) | Professional | 15 min | Dangerous-capability evaluations and capability tiers |
| [Evals in Production](03-evaluation/07-evals-in-production.md) | Practitioner | 20 min | Traces, online metrics, gates, the data flywheel |
| [Case Study: Berkeley's Green Agent and White Agent Project](03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) | Practitioner | 15 min | The course project that builds the evaluator first |

### [Part 04 · Safety and security](04-safety-and-security/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [Threat Modeling LLM Applications and Agents](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) | Practitioner | 25 min | Assets, attackers, trust boundaries, security levels |
| [Jailbreaks and Prompt Injection](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) | Practitioner | 25 min | Why instructions and data share one channel |
| [Agent-Specific Attacks](04-safety-and-security/03-agent-specific-attacks.md) | Practitioner | 25 min | Memory, retrieval, tool and environment poisoning |
| [Defenses: Guardrails, Detection and Secure Design](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) | Practitioner | 30 min | Layers of defense, from filters to policy gates |
| [Runtime Monitoring and Detection](04-safety-and-security/05-runtime-monitoring-and-detection.md) | Professional | 20 min | Where runtime protections sit, and what they cost |
| [Red-Teaming and Safety Evaluation](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) | Practitioner | 25 min | An attack suite, the attack success rate, a safety gate |
| [Trustworthiness Beyond Injection](04-safety-and-security/07-trustworthiness-beyond-injection.md) | Practitioner | 25 min | Leaked data, stereotyping, unequal decisions, hidden limits |
| [AI for Cyber Defense and Vulnerability Detection](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) | Practitioner | 25 min | Agents that find vulnerabilities with tools |
| [Policy, Governance and Standards](04-safety-and-security/09-policy-governance-and-standards.md) | Professional | 20 min | Marginal risk, evidence gates, a dated map of standards |

### [Part 05 · Frameworks, infrastructure and multi-agent systems](05-frameworks-and-multi-agent/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [The Agent Framework Landscape](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) | Practitioner | 12 min | Choosing a framework against a hand-written baseline |
| [AutoGen: Conversation Programming](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) | Practitioner | 14 min | Agents as conversational peers; a tiny runtime |
| [LlamaIndex: Building a Knowledge Assistant](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) | Practitioner | 13 min | Parsing, indexing and retrieval over private data |
| [Multi-Agent Systems I: Games and Self-Play](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) | Practitioner | 13 min | What self-play teaches, and where language helps |
| [Multi-Agent Systems II: The LLM Era](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) | Practitioner | 15 min | When run-time multi-agent designs pay off |
| [Agent Infrastructure: Sandboxes, Browser Use and Protocols](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) | Practitioner | 16 min | Sandboxes, computer use, the Model Context Protocol |
| [Agents in the Enterprise](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) | Practitioner | 12 min | Grounding, levels of automation, a ladder of costs |

### [Part 06 · Frontier applications](06-frontier-applications/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [Multimodal Agents: Web and Computer Use](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) | Practitioner | 10 min | Why agents that click through interfaces still fail |
| [Embodied Agents and Robotics](06-frontier-applications/02-embodied-agents-and-robotics.md) | Practitioner | 10 min | Trial and error, rewards, simulated data |
| [Agents for Scientific Discovery](06-frontier-applications/03-agents-for-scientific-discovery.md) | Practitioner | 10 min | Virtual Lab, Paper2Agent, levels of access |
| [Agents for Formal Mathematics](06-frontier-applications/04-agents-for-formal-mathematics.md) | Professional | 12 min | Proof assistants as verifiers; AlphaProof |
| [What Frontier Domains Teach About Agents](06-frontier-applications/05-what-frontier-domains-teach-about-agents.md) | Practitioner | 10 min | Environments, verifiers, search, tools, evaluation |

### [Part 07 · ML in production: from idea to deployed system](07-ml-in-production/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [From Models to Systems and Products](07-ml-in-production/01-from-models-to-systems-and-products.md) | Foundation | 25 min | The model inside a product; "good enough" |
| [When to Use ML, and When Not To](07-ml-in-production/02-when-to-use-ml-and-when-not-to.md) | Foundation | 20 min | Conditions, alternatives, costs, a keyword baseline |
| [Goals and Requirements](07-ml-in-production/03-goals-and-requirements.md) | Practitioner | 25 min | Layered goals, measures, and three kinds of requirement |
| [Planning for Mistakes](07-ml-in-production/04-planning-for-mistakes.md) | Practitioner | 30 min | FMEA, fault trees, six design strategies |
| [Architecture for ML Systems](07-ml-in-production/05-architecture-for-ml-systems.md) | Practitioner | 20 min | Components, interfaces, decision records |
| [Quality Attributes of ML Components](07-ml-in-production/06-quality-attributes-of-ml-components.md) | Practitioner | 25 min | Latency, cost, size, hard constraints, the Pareto front |
| [Deploying a Model](07-ml-in-production/07-deploying-a-model.md) | Practitioner | 30 min | Forms of serving, where it runs, model cards |
| [Automating the Pipeline](07-ml-in-production/08-automating-the-pipeline.md) | Practitioner | 25 min | Tested stages, data checks, gates, canaries, CI |
| [Scaling the System](07-ml-in-production/09-scaling-the-system.md) | Practitioner | 15 min | Capacity arithmetic, partitioning, caching |
| [Planning for Operations](07-ml-in-production/10-planning-for-operations.md) | Practitioner | 30 min | Objectives, monitors, rollback, kill switch, incidents |

### [Part 08 · Quality assurance and responsible engineering](08-quality-assurance/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [Quality Assurance Basics and the Oracle Problem](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) | Foundation | 22 min | Why learned models have no test oracle |
| [Measuring Model Quality](08-quality-assurance/02-measuring-model-quality.md) | Practitioner | 25 min | Measures, baselines, splits, the pitfalls of offline accuracy |
| [Slicing: Finding Where the Model Fails](08-quality-assurance/03-slicing.md) | Practitioner | 28 min | Quality per group, and a search for failing slices |
| [Testing Without Oracles](08-quality-assurance/04-testing-without-oracles.md) | Practitioner | 26 min | Behavioral tests, invariants, differential testing |
| [Testing Generative and LLM Components](08-quality-assurance/05-testing-generative-and-llm-components.md) | Practitioner | 30 min | Rubrics as a test suite; judges in CI |
| [Data Quality](08-quality-assurance/06-data-quality.md) | Practitioner | 24 min | Fitness for use, linting, four kinds of drift |
| [Pipeline Quality](08-quality-assurance/07-pipeline-quality.md) | Practitioner | 22 min | Making pipeline failures loud |
| [System Quality: End-to-End Tests and Guardrails](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) | Practitioner | 28 min | Testing composed systems; guardrails in plain code |
| [Testing and Experimenting in Production](08-quality-assurance/09-testing-and-experimenting-in-production.md) | Practitioner | 28 min | Telemetry, shadow, canary and A/B releases, rollback |
| [Process Models: Planning and Iteration](08-quality-assurance/10-process-models-planning-and-iteration.md) | Practitioner | 16 min | A model track and a system track, planned apart |
| [Teams and Technical Debt](08-quality-assurance/11-teams-and-technical-debt.md) | Practitioner | 16 min | Ownership across a feature; a register of debt |
| [Responsible Engineering, Versioning and Reproducibility](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) | Practitioner | 18 min | Versioning code, prompts, data and models |
| [Explainability, Fairness and Safety](08-quality-assurance/13-explainability-fairness-and-safety.md) | Practitioner | 20 min | Explanation tools, three fairness criteria, hazards |
| [Security, Privacy, Transparency and Accountability](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) | Practitioner | 19 min | Attacks on ML, privacy, the right to appeal |

### [Part 09 · Efficient deep learning and edge AI](09-efficient-deep-learning/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [Why Efficiency Matters](09-efficient-deep-learning/01-why-efficiency-matters.md) | Foundation | 10 min | Storage, memory, compute, energy; where to win |
| [Neural Network Basics for Efficiency](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) | Foundation | 18 min | Counting a layer's parameters, memory and operations |
| [Pruning and Sparsity](09-efficient-deep-learning/03-pruning-and-sparsity.md) | Practitioner | 20 min | Removing weights so that the model really runs faster |
| [Quantization](09-efficient-deep-learning/04-quantization.md) | Practitioner | 22 min | Fewer bits per number, with little loss of quality |
| [Neural Architecture Search](09-efficient-deep-learning/05-neural-architecture-search.md) | Practitioner | 15 min | Search spaces, search strategies, hardware-aware search |
| [Knowledge Distillation](09-efficient-deep-learning/06-knowledge-distillation.md) | Practitioner | 18 min | A small student learns from a large teacher |
| [TinyML: Microcontrollers and TinyEngine](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) | Practitioner | 19 min | Models that fit in kilobytes of memory |
| [Efficient LLM Inference and Deployment](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) | Practitioner | 24 min | Weights, the KV cache, prefill, decode, batching |
| [LLM Post-Training and On-Device Training](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) | Practitioner | 15 min | Adapters, LoRA, the memory of a fine-tuning run |
| [Efficient Vision, Generative Models and Distributed Training](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) | Practitioner | 15 min | A survey of three areas |
| [Course Summary and Outlook](09-efficient-deep-learning/11-course-summary-and-outlook.md) | Foundation | 12 min | A map of the part, and a routine for keeping up |

### [Part 10 · LLM internals: language modeling from scratch](10-llm-internals/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [The Language Modeling Pipeline and Tokenization](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) | Practitioner | 16 min | From bytes to tokens; a BPE tokenizer from scratch |
| [Resource Accounting: FLOPs, Memory and Arithmetic Intensity](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) | Practitioner | 15 min | Pen-and-paper accounting for a training run |
| [Transformer Architectures and Hyperparameters](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) | Practitioner | 16 min | What modern Transformers agree on, and where they differ |
| [Attention Alternatives and Mixture of Experts](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) | Professional | 15 min | Cheaper attention; more parameters without the compute |
| [GPUs, TPUs and Kernels](10-llm-internals/05-gpus-tpus-and-kernels.md) | Professional | 16 min | How accelerators work; what makes training fast |
| [Parallelism](10-llm-internals/06-parallelism.md) | Professional | 15 min | Training on many GPUs |
| [Scaling Laws](10-llm-internals/07-scaling-laws.md) | Professional | 16 min | Fitting and extrapolating the loss |
| [Inference](10-llm-internals/08-inference.md) | Practitioner | 15 min | Why generation is limited by memory; the levers |
| [Evaluating Language Models](10-llm-internals/09-evaluating-language-models.md) | Practitioner | 14 min | Perplexity, exams, judges, and validity |
| [Training Data](10-llm-internals/10-training-data.md) | Practitioner | 16 min | Extraction, filtering, deduplication, mixtures |
| [Post-Training: SFT, RLHF and RLVR](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) | Professional | 17 min | What each stage adds; the failure modes |
| [Alignment and Multimodality](10-llm-internals/12-alignment-and-multimodality.md) | Professional | 14 min | Alignment as the course defines it; images as tokens |
| [Building Your Own: A Roadmap Through the Assignments](10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) | Practitioner | 14 min | Five assignments, their order and their compute |

### [Part 11 · Professional practice: capstones and checklists](11-professional-practice/README.md)

| Chapter | Level | Read | What it covers |
|---|---|---|---|
| [How to Ship an LLM Feature End to End](11-professional-practice/01-how-to-ship-an-llm-feature-end-to-end.md) | Practitioner | 30 min | One feature from idea to production, as nine decisions |
| [Capstone 1: A Task Agent with Evals](11-professional-practice/02-capstone-task-agent-with-evals.md) | Practitioner | 25 min | Build the evaluator, then the agent it grades |
| [Capstone 2: A Monitoring Agent for Prompt Injection](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) | Practitioner | 25 min | A monitor that flags injected instructions, measured |
| [Capstone 3: From Model to Product](11-professional-practice/04-capstone-model-to-product.md) | Practitioner | 20 min | A classical ML feature through goals, pipeline and operations |
| [Capstone 4: Efficient Inference](11-professional-practice/05-capstone-efficient-inference.md) | Practitioner | 20 min | Measure a model, quantize it, report the trade-off |
| [Capstone 5: Train a Small Language Model](11-professional-practice/06-capstone-train-a-small-language-model.md) | Professional | 25 min | Tokenizer, Transformer, optimizer and loop, in five stages |
| [Checklists for Shipping AI Systems](11-professional-practice/07-checklists.md) | Practitioner | 20 min | Five checklists, each item linked to its chapter |
| [Staying Current](11-professional-practice/08-staying-current.md) | Foundation | 20 min | What to follow, and how to read a release critically |

## Sources

Four open university sources. The lectures were recorded between September 2024 and June 2026.

1. **UC Berkeley.** Three MOOCs on LLM agents: the [LLM Agents MOOC (Fall 2024)](https://rdi.berkeley.edu/llm-agents/f24), the [Advanced LLM Agents MOOC (Spring 2025)](https://rdi.berkeley.edu/adv-llm-agents/sp25) and the [Agentic AI MOOC (Fall 2025)](https://rdi.berkeley.edu/agentic-ai/f25), taught by Dawn Song. They are behind parts 01 to 06.
2. **Carnegie Mellon University.** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025): [the book](https://mlip-cmu.github.io/book/) and [the course, 17-645 / 11-695](https://mlip-cmu.github.io/). It is behind parts 07 and 08, and chapters of parts 01 and 03.
3. **MIT 6.5940.** TinyML and Efficient Deep Learning Computing (Fall 2024), by Song Han: [course page](https://hanlab.mit.edu/courses/2024-fall-65940). It is behind part 09.
4. **Stanford CS336.** Language Modeling from Scratch, by Percy Liang and Tatsunori Hashimoto: [course page](https://cs336.stanford.edu/). It is behind part 10.

This repository explains these sources and links to them. It copies nothing from them: every explanation is rewritten, and short quotations are marked and attributed. [SOURCES.md](SOURCES.md) lists the lectures, their speakers and their links. If a chapter and its source disagree, the source wins.

## How it was made

The chapters were written by AI writers from the lectures and from the book. The lectures were read through machine transcripts made for this project, and a transcript can garble a name or a number. Every claim taken from a lecture links to its moment in the video, so that you can check it against the source. Nothing is copied. The explanations are rewritten, not copied. The courses and the book are the authority. This repository is the study guide, and a chapter that disagrees with its source is wrong.

The [lecture guides](lectures/README.md) were made the same way, from the same machine transcripts: one guide per lecture, 77 in all, each written after reading the lecture from its first minute to its last.

## What is verified, and what is not

The chapters were checked in two ways, described in [VERIFICATION.md](VERIFICATION.md) with the results per part.

**Automated checks, run on 2026-11-25.** All 2,636 internal links resolved at that point; the count is 4,735 with the lecture guides, all resolving on 2026-11-26. All 119 arXiv citations (103 papers) carry the title and year of the arXiv record. All 1,459 links to a moment in a lecture were checked against the transcript at that moment. No chapter shares more than 23 words in a row with a source. The 66 standalone Python listings run, and 16 tests pass.

**The verification pass, 2026-11-24.** Every statement that a chapter attributes to a lecture or to the book was compared with the source at the cited place. About 1,500 statements were checked and more than 210 corrected. In 72 chapters, passages were deepened with the lecturers' own content.

**Second review, 2026-11-25.** Every part was then read again by a fresh reviewer. About 2,100 attributed statements were re-checked against their sources and more than 130 corrected. Every self-check answer was re-derived; in many chapters the correct option had been the first or the second, so options were reordered. Exercises that could not be started were completed, and 81 diagrams were added.

**Lecture guides, 2026-11-25 and 2026-11-26.** All 77 lectures now have a guide: 1,207 parts. Before a guide is published, an automatic check confirms that its parts cover the lecture end to end without a gap or an overlap, that every part links to the second of the video that its heading names, that every link to a chapter section resolves, and that no run of eight or more words is copied from the lecture outside quotation marks.

**Glossary, 2026-11-25.** Every row of the glossary was checked against the chapter it links to: 12 definitions corrected, 7 links moved to a better chapter, 13 duplicates merged, 16 rows removed and 24 added. The glossary has 1,086 terms.

**Not verified:**

- The five capstones were specified, not carried out, and the hours and costs in the capstones and in the roadmap are estimates.
- Engineering judgment is marked as this repository's own and was not checked against a source.
- Where no source covers a topic, the chapter uses general knowledge (see below).
- Facts that change fast (model names, prices, APIs, products, regulation) are true as of the date each chapter gives.
- YouTube links were not checked, and not every external link was reopened.
- The transcripts are machine-made and can garble names. The lectures are the authority.
- The lecture guides passed the automatic check only. Nobody has read a guide a second time against the lecture, and no second reviewer went over them.
- The chapters in parts 07 and 08 were checked statement by statement against the book *Machine Learning in Production*, but not for coverage. A word-overlap count flagged 82 of its 399 sections as possibly reflected only in part, and those sections were not read against the chapters.

## Status and gaps

Each part's main limitations are below. [VERIFICATION.md](VERIFICATION.md#further-limitations-by-part) lists further ones.

### Part 01 · Foundations

- **01.01, 01.02, 01.04, 01.05** Loss, data splits, attention, temperature and the system prompt as an API field are general knowledge.

### Part 02 · Building agents

- **02.03, 02.04, 02.06, 02.07** ReAct, plan-then-execute, reflection and the timeline of agent designs are general knowledge. HippoRAG, context length, code-editing tools and error recovery have no transcript.
- **02.05** The DSPy API is shown as in the October 2024 lecture, not as in current documentation.

### Part 03 · Evaluation

- **03.03, 03.05** The judge biases and the claims attributed to Evan Miller's paper are general knowledge; neither paper was checked.
- **03.06** The responsible scaling policy is one speaker's account, dated 2024-11-25. The current text was not checked.
- **03.08** No source describes attack categories; as in the lecture, the green agent evaluates and the white agents are under test.

### Part 04 · Safety and security

- **04.01, 04.09** MITRE ATLAS, the OWASP lists and the regulation rows were not opened; their state on 2026-11-24 is unconfirmed.
- **04.03, 04.04, 04.07** Tool poisoning, "spotlighting" and representation engineering are general knowledge.
- **04.05** No lecture covers monitoring agents: its positions, signals and trade-offs are engineering judgment.

### Part 05 · Frameworks and multi-agent

- **05.01 to 05.03** AutoGen is archived as of November 2026; 05.02 teaches its ideas without the framework. The other frameworks and the LlamaIndex API were not verified.
- **05.06** Sandboxes have no lecture behind them, and no sandbox product was verified. The MCP section follows the specification revision of 2026-07-28; its toy server keeps the 2025 message shapes.

### Part 06 · Frontier applications

- **06.01, 06.02** The Mind2Web task counts and the Voyager sentences are general knowledge.

### Part 07 · ML in production

- **07.01 to 07.10** No source is missing.

### Part 08 · Quality assurance

- **08.05, 08.08, 08.12, 08.14** The book does not cover LLM judges or rubric pipelines. The LLM testing pipeline, guardrails, prompt versioning and threat model are this repository's own.
- **08.12, 08.14** The EU AI Act is described as the book states it for late 2023.

### Part 09 · Efficient deep learning

- **09.03, 09.05 to 09.09** The lottery ticket hypothesis, architecture search strategies, distillation formulas, TinyEngine's memory planner, PagedAttention, FlashAttention tiling and parameter-efficient training are general knowledge; the chapters did not draw on the lectures for them. The lectures are now covered by the [lecture guides](lectures/README.md), and the chapters were not rewritten from those guides.

### Part 10 · LLM internals

- **10.08** No lecture covers decoding strategies, best-of-n or search at inference time; the chapter says so.

### Part 11 · Professional practice

- **11.01, 11.03, 11.07** The refund assistant and the ten payload families are illustrative. The latency, timeout and false-positive budgets are starting values, not measurements.

## License

The text in this repository is licensed under [Creative Commons Attribution 4.0](LICENSE). The source courses and book keep their own licenses. The CMU book is licensed CC BY-NC-ND 4.0. This repository explains and links to these sources and copies nothing from them.
