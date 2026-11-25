# Part 06: Frontier Applications

Where agents are heading: web and computer use, robotics, scientific discovery and formal mathematics, and the patterns these four domains share.

## Who this part is for

You have built and evaluated an agent (parts 02 and 03). You want to know what the research frontier has already shown, what it only expects, and which of its decisions transfer to ordinary work. You do not need a robotics, biology or mathematics background.

## Chapters

| # | Chapter | Level | Reading | What you learn |
|---|---|---|---|---|
| 01 | [Multimodal Agents: Web and Computer Use](01-multimodal-agents-web-and-computer-use.md) | Practitioner | 10 min | Observation formats, execution-based scoring, WebArena, Mind2Web, VisualWebArena and OSWorld, and why agents still fail on long tasks |
| 02 | [Embodied Agents and Robotics](02-embodied-agents-and-robotics.md) | Practitioner | 10 min | Trial and error, reward design, simulated data, model-written rewards, and what a racing agent teaches about specifications |
| 03 | [Agents for Scientific Discovery](03-agents-for-scientific-discovery.md) | Practitioner | 10 min | The Virtual Lab, Paper2Agent, Agents4Science 2025, and how your access to a model limits what you can evaluate |
| 04 | [Agents for Formal Mathematics](04-agents-for-formal-mathematics.md) | Professional | 12 min | Proof assistants as perfect verifiers, the AlphaProof recipe, autoformalization and proof search |
| 05 | [What Frontier Domains Teach About Agents](05-what-frontier-domains-teach-about-agents.md) | Practitioner | 10 min | The four domains compared on environment, verifier, search, tools and evaluation |

Reading time is about 52 minutes; the five exercises add about 3.5 hours.

## How to read this part

- Chapters 01 to 04 are independent surveys. Read them in any order.
- Read chapter 05 last. It is a synthesis of the other four and of the ten lectures behind them.
- If you have ten minutes, read chapter 05 and then the closing section of each chapter, "What this means for someone building agents".
- Every number is dated and tied to the lecture that reported it. Benchmark scores, model names and products in this area change within months.

## The one idea to take away

Across all four domains, progress followed the same order: an environment with cheap resets, a verifier that answers yes or no without a person, search spent against that verifier, tools for work that language cannot do exactly, and evaluation by outcome rather than by path. Formal mathematics has the only perfect verifier. Science has the weakest. Web and robotics sit between, which is why they moved first and why their agents still need people at the irreversible steps.

## Sources

All chapters are built from UC Berkeley MOOC lectures, cited with timestamps:

- Ruslan Salakhutdinov, "Multimodal Autonomous AI Agents", Advanced LLM Agents MOOC, Spring 2025
- Caiming Xiong, "Multimodal Agents: From Perception to Action", Advanced LLM Agents MOOC, Spring 2025
- Peter Stone, "Autonomous Agents: Embodiment, Interaction, and Learning", Agentic AI MOOC, Fall 2025
- Jim Fan, "Project GR00T: A Blueprint for Generalist Robotics", LLM Agents MOOC, Fall 2024
- James Zou, "AI Agents to Automate Scientific Discoveries", Agentic AI MOOC, Fall 2025
- Percy Liang, "Open-Source and Science in the Era of Foundation Models", LLM Agents MOOC, Fall 2024
- Thomas Hubert, "AlphaProof: when reinforcement learning meets formal mathematics", Advanced LLM Agents MOOC, Spring 2025
- Kaiyu Yang, "Language models for autoformalization and theorem proving", Advanced LLM Agents MOOC, Spring 2025
- Sean Welleck, "Bridging Informal and Formal Mathematical Reasoning with AI", Advanced LLM Agents MOOC, Spring 2025
- Swarat Chaudhuri, "Abstraction and Discovery with Large Language Model Agents", Advanced LLM Agents MOOC, Spring 2025

## Lecture guides for this part

Each guide maps one lecture from its first minute to its last and says where this book teaches each piece. Where no chapter teaches a part of the lecture, the guide explains it itself; the table counts those parts.

| Lecture | Lecturer | Length | Parts no chapter teaches | Guide |
|---|---|---|---|---|
| Multimodal Autonomous AI Agents | Ruslan Salakhutdinov (CMU / Meta) | 1:18:00 | 3 of 16 | [open guide](../lectures/sp25-06-multimodal-autonomous-ai-agents.md) |
| Multimodal Agents: From Perception to Action | Caiming Xiong (Salesforce AI Research) | 1:30:00 | 6 of 19 | [open guide](../lectures/sp25-07-multimodal-agents-from-perception-to-action.md) |
| AI Agents to Automate Scientific Discoveries | James Zou (Stanford) | 1:02:00 | 0 of 11 | [open guide](../lectures/f25-08-ai-agents-to-automate-scientific-discoveries.md) |
| Autonomous Agents: Embodiment, Interaction, and Learning | Peter Stone (UT Austin / Sony AI) | 1:02:00 | 2 of 15 | [open guide](../lectures/f25-11-autonomous-agents-embodiment-interaction-and.md) |
| Project GR00T: A Blueprint for Generalist Robotics | Jim Fan (NVIDIA) | 58:00 | 3 of 11 | [open guide](../lectures/f24-09-project-gr00t-a-blueprint-for-generalist.md) |
| Open-Source and Science in the Era of Foundation Models | Percy Liang (Stanford) | 54:00 | 5 of 15 | [open guide](../lectures/f24-10-open-source-and-science-in-the-era-of-foundation.md) |
| AlphaProof: when reinforcement learning meets formal mathematics | Thomas Hubert (Google DeepMind) | 1:16:00 | 6 of 17 | [open guide](../lectures/sp25-08-alphaproof-when-reinforcement-learning-meets.md) |
| Language models for autoformalization and theorem proving | Kaiyu Yang (Meta FAIR) | 52:00 | 2 of 13 | [open guide](../lectures/sp25-09-language-models-for-autoformalization-and.md) |
| Bridging Informal and Formal Mathematical Reasoning | Sean Welleck (CMU) | 1:14:00 | 5 of 16 | [open guide](../lectures/sp25-10-bridging-informal-and-formal-mathematical.md) |
| Abstraction and Discovery with Large Language Model Agents | Swarat Chaudhuri (UT Austin) | 1:28:00 | 5 of 17 | [open guide](../lectures/sp25-11-abstraction-and-discovery-with-large-language.md) |

## Where to go next

- To turn the verifier idea into daily practice: [Evaluation Is the Product](../03-evaluation/01-evaluation-is-the-product.md).
- To build the reset, sandbox and tools an agent environment needs: [Agent Infrastructure: Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md).
