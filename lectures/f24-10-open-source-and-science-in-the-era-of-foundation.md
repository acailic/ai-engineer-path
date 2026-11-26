# Lecture guide: Open-Source and Science in the Era of Foundation Models

**Lecturer:** Percy Liang (Stanford) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 10 · **Length:** 54:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=f3KKx9LWntQ) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/percyliang.pdf)
**Chapters that cite this lecture:** [03. Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Percy Liang argues that access shapes research, and walks down three levels of access to language models (API, open weights, open source), showing what each one lets researchers build or find out, from agents for machine-learning work to a statistical test of whether two models were trained independently.

## Before you watch

The chapter [Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md) summarizes this lecture in its section on Liang. The lecture needs no mathematics; its one statistical idea, the p-value, is introduced through a thought experiment.

## The lecture, part by part

### [0:00–1:53](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0) Capabilities rose, access fell

The capabilities of models have risen fast in a few years, and access to them has fallen just as fast: early releases came with a paper, weights, code and data, and today often only an API remains. The lecturer's point is that access shapes research. Internet-scale text in digital form created a whole field in the 1990s; in the 2010s large annotated datasets such as ImageNet appeared because crowdsourcing platforms existed; and deep learning took off because GPUs were available. He then distinguishes three levels of access for foundation models: an API, open weights and open source.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [1:53–4:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=113) Three kinds of scientist

With API access you are a cognitive scientist who studies a black box by sending in prompts and reading responses, and you cannot look inside. With open weights you are a neuroscientist who can probe the internals, begin to understand mechanisms and build derivatives such as distillations and fine-tunes. Both remain confined to existing models, their architectures and the decisions of their designers. Open source access makes you a computer scientist building a system and controlling every part of it, free to question the dataset, the architecture and the training procedure. Turning to API models, he asks you to think of one as a universal function: given an instruction in natural language it summarizes, verifies or generates.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [4:00–6:01](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=240) The model as a controller

Composing API calls yields agents, and the lecturer stresses that the model is the controller of execution, not a primitive called at the leaves of a fixed program. His basic architecture records every observation in a memory stream; since a digital agent has no reason to forget, the stream holds everything, so a retrieval step selects the relevant memories into a context. From that context the agent can act in the present (tool use), look back and reflect on its memories, or plan ahead.
**In this book:** [The Anatomy of an Agent › The core idea](../02-building-agents/01-the-anatomy-of-an-agent.md#the-core-idea).

### [6:01–10:22](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=361) A research agent for machine-learning problems

MLAgentBench hands an agent a machine-learning task: some data, a first version of the code and a scorer for test accuracy, and asks for the best model it can build, as a researcher would by writing code, running it, reading the log and revising. The prompt makes the model a research assistant that must reflect on its observations, plan, fact-check the plan to guard against hallucination, think and propose an action such as running a script or editing a file. The observation returns to the memory stream, and the next prompt carries its last three entries. Over 13 benchmarks the results were mixed: the best model, Claude 3, did well on classic Kaggle competitions, perhaps because they were in its training data, and failed on newer ones. The lecturer likes that solving the task improves the model, which may then solve it better.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [10:22–14:45](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=622) A cybersecurity agent

Here the agent has a server, its code and a shell; it must find a vulnerability, exploit it and retrieve a flag, a secret string, as in capture-the-flag competitions. Sub-questions can be added to measure partial progress. The recipe is the same: reflect, plan, think, run a command, update the memory. The best model, Claude 3.5, solved 17.5% of the tasks; the hardest task took an experienced human team 24 hours, while the hardest task any model solved takes humans 11 minutes, a gap that keeps shrinking. The benchmark matters twice: it gives policymakers a quantified view of risk, and it promises better penetration-testing tools that find flaws before deployment.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [14:45–19:07](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=885) Simulating people: retrieval and reflection

The second class of agents imitates people. In an earlier paper the group placed 25 agents in a town called Smallville, each built on the same architecture. Retrieval from the memory stream scores memories by recency, by importance (a tidy desk matters little, a wedding much) and by relevance to the current context, for instance when looking for a water bottle. Reflection abstracts groups of low-level memories into higher-level ones, so that reading about urban design becomes dedication to research, which gives an agent a purpose beyond reacting to details. Because people talk, the agents talk too, and the simulation shows how news of a Valentine's Day party spreads through the town.
**In this book:** nothing beyond this guide; nearest: [Memory and Knowledge for Agents › The core idea](../02-building-agents/04-memory-and-knowledge-for-agents.md#the-core-idea).

### [19:07–24:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1147) Simulating real individuals

Those agents were invented. To simulate real people the group borrowed interviews from the social sciences: a two-hour conversation captures facts, perspectives and personality. A thousand demographically diverse Americans were interviewed by an LLM agent, and the text of each interview seeded one agent's memory. The same surveys, games and experiments were then run on the people and on the agents. People asked again two weeks later match their own answers only 81% of the time, which sets a ceiling; the agents reach 69%, which he describes as capturing 85% of the total accuracy with a baseline of about 20%, and do worse without the interviews. Social scientists see a laboratory in this, where the same agent can be given a control and a treatment and the difference measured, with the caveat that the agents are not people.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [24:00–26:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1440) Agents that learn, and what open weights are

All these agents are static: an off-the-shelf model plus prompts. AlphaGo had two phases, learning from human games and then improving by reinforcement learning, and language models are, by his account, still at the first phase; an agent working in an environment can collect reward signals, which opens the second. That needs deeper access than an API. Open-weight models are, in the wording of a US executive order, "dual-use foundation models with widely available weights"; widely rather than simply available, because licences restrict use, for example above 700 million monthly active users for Llama.
**In this book:** nothing beyond this guide; nearest: [Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

### [26:00–31:10](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1560) What the weights reveal

One advantage is reproducibility: API models are retired, and results obtained on them cannot be reproduced, whereas weights can be kept. Weights also let researchers look inside. Asked which number is larger, 9.8 or 9.11, Llama 3.1 70B Instruct answers 9.11; researchers at Transluce summarized each neuron from the examples that trigger it and found that "11" activates a neuron responding to September 11, as if the numbers were dates. A paper from NVIDIA pruned a 15-billion-parameter model into 8-billion and 4-billion models with little loss, useful because agents call a model in their inner loop and want it fast. An adversarially optimized prompt that jailbreaks an open model also jailbreaks GPT-4, so open weights teach something about closed models.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out) · [Jailbreaks and Prompt Injection › A taxonomy of techniques](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md#a-taxonomy-of-techniques).

### [31:10–38:02](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1870) Were these two models trained independently?

Given two sets of weights, the test asks whether they were trained independently or one derives from the other. Comparing weights by cosine similarity gives a number with no principled threshold. The thought experiment: if the first model's training could be repeated from many random initializations, a truly independent second model would be about as similar to the first as to any retrained copy of it, and the fraction of copies with a similarity more extreme than the observed one is a p-value. Retraining is impossible, so the method fakes it with a symmetry of neural networks: permuting a layer's hidden units gives a model that training could have reached. On models with known history the p-values are spread out for independent pairs and vanishingly small for fine-tunes of Llama 2. The test also confirmed that the leaked model Miqu and StripedHyena-Nous derive from other models, and that Llama 3.2 3B descends from Llama 3.1 8B, identifying which layers were reused, which the announcement had not said.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [38:02–40:10](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2282) What open weights give, and what they keep fixed

Open-weight models have been immensely valuable: they enable work on interpretability, fine-tuning, distillation and model merging, with reproducibility and no fear of deprecation. They also raise new questions, such as the independence test, and they teach us about API models. Two cautions remain. Arbitrary surgery on weights, averaging them or removing layers, has no guarantee of producing a coherent model, and a model usually has to be fine-tuned to heal afterwards. And researchers are still confined to a blueprint: a transformer with the particular weights a company chose.
**In this book:** nothing beyond this guide; nearest: [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [40:10–44:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2410) What open source means for models

Open-source models are, he says, still far weaker than the best open-weight and API models. Open source comes from software, with roots in the hacker culture of MIT in the 1950s and in open science, and it stands for creativity, exploration, transparency, collaboration and resistance to authority; Richard Stallman and Linus Torvalds built the ecosystem around GNU and Linux, and the Open Source Initiative defined the term in 1998. It is now defining it for AI through four freedoms: use without asking permission, study, modify and share. In practice that requires the parameters without restrictions, the code including training and data processing, since data shapes behaviour, and information about the data rather than the data itself, because most web text is copyrighted and redistributing it invites lawsuits. Compute is not in the definition, but without it nobody can modify a model by retraining.
**In this book:** nothing beyond this guide; nearest: [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [44:00–46:32](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2640) Three results that needed the full recipe

With control over data, algorithm and architecture the lecturer's group changed each in turn. A data mixture chosen by distributionally robust optimization, instead of weights set by hand, trained a model 2.6 times faster. An optimizer using second-order information, a clipped diagonal Hessian, was twice as fast as Adam. And the Backpack language model, an architecture more interpretable than a transformer, allows precise edits: an intervention on hidden units makes the model believe that HP, not Apple, made the MacBook.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

### [46:32–50:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2792) Three ways to get compute

The question he often gets is whether these results would hold at a larger scale, and answering it takes compute. The lecturer offers three tracks. Extend scaling laws downward, so that work done on small models carries the belief that it will scale, working at small scale with a mindset of scale. Use idle GPUs: interconnects between them are about a hundred times slower than in a data center, yet scheduling and systems work trained billion-parameter models only twice as slowly, and later algorithms and a community run training a 10-billion-parameter model in a decentralized pool show how far this goes. Or ask for public funding, as the pilot of the National AI Research Resource does.
**In this book:** [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out) · [Scaling Laws › The core idea](../10-llm-internals/07-scaling-laws.md#the-core-idea).

### [50:00–54:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=3000) Conclusion

Other fields have won multi-billion-dollar infrastructure for open research, such as the Human Genome Project, the James Webb telescope and the Large Hadron Collider, and the problems pursued in public differ from those a company pursues. The lecture's theme is that access shapes research: with an API you build agents, with weights you can also fine-tune, distill and inspect, and each step down widens the questions. Most research now lives inside APIs and fixed weights; to make fundamental progress, researchers must be able to question the data, the architecture and the training algorithm instead of sitting in a local optimum. The long-term goal is to understand how data and architecture map to behaviour, a question that is hard even with full access and, he says, hopeless with only an API, and compute is the main obstacle on the way.
**In this book:** nothing beyond this guide; nearest: [Agents for Scientific Discovery › Percy Liang (November 2024): access decides what you can find out](../06-frontier-applications/03-agents-for-scientific-discovery.md#percy-liang-november-2024-access-decides-what-you-can-find-out).

## What to take away

- Access decides what research is possible: an API lets you build agents, open weights let you inspect and change a model, and open source lets you question data, architecture and training.
- A simple loop of reflecting, planning, fact-checking and acting already builds agents for machine-learning work and for security tasks, with mixed results.
- Interviews seeded into an agent's memory reproduce individual behaviour at 85% normalized accuracy, by his account, against an 81% ceiling set by people's own consistency.
- Compute is the bottleneck of open-source research; scaling laws applied downward, pooled decentralized GPUs and public funding are the three ways out.

## Sources

- Percy Liang, "Open-Source and Science in the Era of Foundation Models", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=f3KKx9LWntQ).
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
