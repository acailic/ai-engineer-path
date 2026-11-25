# Lecture guide: Multimodal Agents: From Perception to Action

**Lecturer:** Caiming Xiong (Salesforce AI Research) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 7 · **Length:** 1:30:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=n__Tim8K2IY) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/Multimodal_Agent_caiming.pdf)
**Chapters that cite this lecture:** [01. Multimodal Agents: Web and Computer Use](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Caiming Xiong builds a multimodal computer-use agent from three sides: a real-computer benchmark (OSWorld), a way to synthesize training data from web tutorials (AgentTrek), and a vision-only model that reasons before it clicks (AGUVIS).

## Before you watch

Read [Multimodal Agents: Web and Computer Use](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) first; steps 2 to 4 of its procedure and its section on Xiong describe OSWorld, AgentTrek and AGUVIS. The lecture assumes you know what a vision-language model is and what fine-tuning means.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=0) Why agents

In four or five years almost every benchmark has saturated, so the question is what to do with such strong models. The lecturer's answer is agents: systems that see, hear and speak as well as read, and that carry out computer tasks the way a person does, across several applications.
**In this book:** [Multimodal Agents › Why this matters](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#why-this-matters).

### [2:00–4:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=120) Agents already in use

Coding assistants now accept screenshots and fix bugs from them. Web agents control browsers, mobile agents control phones, and a humanoid robot from Figure AI works with another robot. Some of these are products, some research, some demos, and more uses are coming. What they share is a model that reads more than text and then acts on what it saw, which is why the rest of the lecture asks how such agents should be tested, trained and built.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › Why this matters](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#why-this-matters).

### [4:00–10:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=240) Three questions, and why existing benchmarks fall short

The lecture follows three needs: an interactive, reconfigurable benchmark; data; and the model. Everyday computer work is a workflow across several applications, such as updating a bookkeeping sheet from recent transactions, and an agent should follow such an instruction by itself. To trust it, one needs a benchmark on a real interactive environment that covers many systems and applications. Mind2Web has one recorded demonstration per task and no executable environment, so it assumes a single solution; WebArena is executable but simplifies what the agent sees and can do, and covers a few websites.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [10:00–14:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=600) OSWorld: a real computer for agents

OSWorld is the first scalable environment of a real computer for developing and benchmarking agents. It gives full keyboard and mouse control of real applications and is not a fixed test set: users define their own tasks, from software development to image editing, without building a new simulator. A task has three parts: a natural-language instruction, a setup file that puts files and applications into the starting state, and an evaluation part. The environment runs in a virtual machine, so it is isolated and a task can be restored again and again.
**In this book:** [Multimodal Agents › 2. Give every task a resettable start state](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#2-give-every-task-a-resettable-start-state).

### [14:00–20:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=840) The loop, and the reward

Any model can be the agent. It receives the instruction and observations: a screenshot, the accessibility tree, terminal output, or Set-of-Mark, a screenshot with labels taken from the accessibility tree. A vision-based agent may use only the screenshot; a text-based one only the tree. It emits actions as code strings that move the mouse and keyboard, the virtual machine executes them, and new observations follow. The loop ends when the task is done, has failed, or reaches a step limit of 15 in their experiments. The reward is execution-based: full success scores 1, partial success somewhere in between, failure 0.
**In this book:** [Multimodal Agents › 3. Let the agent act](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#3-let-the-agent-act).

### [20:00–24:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=1200) The benchmark's tasks and scripts

No single metric fits every task, so each task gets its own evaluation script. The benchmark has 369 real-world computer tasks collected from the web and confirmed by people with a computer-science background, who also recorded trajectories and wrote the scripts. Of these, 100 are workflows across several applications and 268 stay in one application; 30 are infeasible on purpose, because an agent should learn to say no; 43 run on Windows, the rest on Ubuntu. The team wrote 134 evaluation scripts for the 369 tasks.
**In this book:** [Multimodal Agents › 4. Score by execution](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#4-score-by-execution).

### [24:00–28:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=1440) How it compares

Against other benchmarks, OSWorld offers a controllable executable environment, scales to new environments, supports multimodal observations, includes cross-application tasks and can start from an intermediate state. Its tasks are also longer: a median completion time near 100 to 110 seconds against 30 to 40 seconds for a widely used screen benchmark, with some tasks taking 900 seconds or more. The team then tested open and closed models.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › Benchmarks to know](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#benchmarks-to-know).

### [28:00–30:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=1680) First results

Four settings were tested: the accessibility tree only (simplified, because it is long and redundant), the screenshot only, both together, and Set-of-Mark. People succeed on about 70 to 75% of the tasks; the best open and closed models of the time are far behind on tasks that are ordinary daily work.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [30:00–36:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=1800) What changes the score

People are stable across settings, within three to five points; models swing, and two models from one company differ by ten points under Set-of-Mark. Higher screenshot resolution helps the screenshot setting clearly and Set-of-Mark less, because its text already carries information. More history helps Set-of-Mark and hurts the screenshot setting, a sign that models read text better than pure images. The accessibility tree is long, about 6,000 tokens at the 90th percentile, which limits how much history fits. Scores on Ubuntu and Windows correlate at 0.7, and moving or resizing a window changes results, so the models are not robust.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [36:00–40:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=2160) Newer models, and a caution about step limits

Claude rose from about 14 to 15% to 22% between versions, still far from people's 72%. Raising the step limit from 15 to 50 helps. OpenAI's computer-use agent reached 38% at 200 steps, while most tasks should be solvable in 15 to 20, so the gap to closing is still large.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [40:00–46:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=2400) AgentTrek: trajectories from tutorials

Agent data is a multi-step trajectory, which is expensive to collect, cannot be scraped, and is slow to annotate. Web tutorials already describe how to do tasks step by step, so AgentTrek turns them into trajectories in three stages. It collects and filters tutorials from large corpora with heuristics and a text classifier and has a language model structure them. A vision-language agent then replays each structured tutorial step by step, recording the task description, each observation, the reasoning and each action. A separate evaluator scores the trajectories and discards poor ones. Fine-tuning on the result confirms the value.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [46:00–52:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=2760) Inside the pipeline

Heuristic filtering removes more than 99.9% of the corpus. A language model labels a sample as tutorial or not, with an F1 score of about 88 to 89% against human checks and better than people on very long documents, and a fastText classifier trained on those labels scores the rest. A model then rewrites each tutorial into five parts: platform and software versions, a task description, prerequisites, step-by-step instructions, and an expected outcome used to verify success. The agent executes the steps and the evaluator checks the recorded trajectory.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [52:00–58:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=3120) What the data looks like, and its limit

The pipeline produced 10,000 trajectories, not its maximum, with about 12 steps each and more information than earlier sets: page source, accessibility tree, reasoning, video and screenshots, across many websites and fields. A model fine-tuned on them beat both open models and GPT-4o on a web benchmark. Two lessons: web corpora remain a rich source of tasks, and reasoning and reflection in the trajectory matter. The limit is one trajectory per instruction, pure imitation; the fix is a second stage of reinforcement learning in OSWorld.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [58:00–62:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=3480) Can calling tools improve understanding itself?

Open vision-language models are far from perfect at grounding, reasoning and using outside knowledge. TACO teaches them to reason and to call actions that zoom into a region, read text, run a calculation or query a language model, so that a hard question becomes a short sequence of tool calls. The training data is synthetic: the model learns when a tool would help and what to ask it for, and then uses the tool's output to answer. The lecturer shows a small open model and a video model doing this after training.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › What this means for someone building agents](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#what-this-means-for-someone-building-agents).

### [62:00–66:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=3720) Two ways to synthesize reasoning-and-action data

In model-based generation, a frontier model receives an image and a question with its answer and writes reasoning with tool calls, or without them; the output is checked, and failures become plain question-answer pairs. In programmatic generation there is no question: detection, depth and text-reading models add annotations to an image, and hand-written templates turn them into questions about counting, two- and three-dimensional spatial reasoning, and mixtures, with the actions needed to answer.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [66:00–70:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=3960) Three findings

The capability had to be fine-tuned; showing examples in the prompt did not work. With actions, models solved tasks they could not solve before, so understanding too improves with tools. The gains held across several benchmarks, and quality of the data counted more than quantity. Adding more examples of the same kind did not help, which matches the lesson from the tutorial-based trajectories: a smaller set of correct, well-checked steps trains a better model than a large set no one verified.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [70:00–78:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=4200) AGUVIS: three problems and the design

Existing computer-use agents have three weaknesses. They rely on text representations that differ per platform (page source, the tree of a desktop, a mobile format), grow very long, and prevent training on several platforms' data at once, because action spaces also differ. Closed models were surprisingly poor at grounding, that is, at pointing to the right element. And they emit an action directly, without the reasoning that hard tasks need. AGUVIS answers with screenshots only, one action format that merges existing data sets, and an inner monologue: a thought and a low-level instruction before every action.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [78:00–86:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=4680) Training and results

Stage one trains grounding, with a packing trick that joins samples from the same image into one multi-turn example. Stage two adds planning and reasoning with the monologue. The data: one million grounding samples and 35,000 multi-step trajectories whose monologues were written by prompting GPT-4o with the highlighted element, the instruction and the action. The model is strong at grounding alone; the second stage improves grounding further; and it leads on offline benchmarks for web and Android and on live web and Android environments. A 7-billion-parameter model paired with GPT-4o as planner reaches the state of the art. Ablations show both stages and the monologue matter, and forcing the monologue repairs about 20% of grounding errors on hard tasks.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

### [86:00–1:30:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=5160) Crossing platforms, and what remains

Trained only on web and mobile data, AGUVIS still does well on OSWorld's desktop tasks, and its 7-billion model with GPT-4o as planner beats a dedicated computer-use model. The takeaways: a unified framework that works across platforms from pixels alone is the direction (a commercial computer-use agent points the same way), and grounding still has more room to improve than reasoning.
**In this book:** [Multimodal Agents › Caiming Xiong (March 2025): the environment, the data, a vision-only agent](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#caiming-xiong-march-2025-the-environment-the-data-a-vision-only-agent).

## What to take away

- A benchmark needs a real, resettable environment and a check of the final state; one demonstration per task is not enough.
- People finish about 72% of OSWorld's daily computer tasks; the best agents a third of that, often with far more steps.
- Tutorials on the web can be turned into verified trajectories at scale; fine-tuning on them beats models that only read examples in the prompt.
- One vision-only model with a shared action format and an inner monologue works across platforms; grounding is the larger remaining gap.

## Sources

- Caiming Xiong, "Multimodal Agents: From Perception to Action", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=n__Tim8K2IY).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25>.
