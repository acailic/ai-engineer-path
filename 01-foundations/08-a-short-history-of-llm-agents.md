# 08. A Short History of LLM Agents

**Level:** Foundation · **Reading time:** 20 min · **Exercise:** 30 min
**Prerequisites:** [How Large Language Models Are Trained](02-how-large-language-models-are-trained.md) (what an LLM does)

> **In one sentence:** After this chapter you have one precise definition of "agent", you can place any system on the line from workflow to agent, and you know the three stages that led to today's LLM agents.

## Why this matters

People call a thermostat an agent. They call a chatbot an agent. They call a coding assistant that edits files an agent, and so do the vendors of a framework that chains three model calls. If you have to build, buy or evaluate one, you first need to answer two questions. What makes a system an agent? And what should you build instead, when an agent is the wrong tool?

## The definition this repository uses

> **An agent is a system that pursues a goal by acting on an environment in steps. At each step it observes the environment, decides the next action itself, and acts again, until the goal is met or a budget runs out. An LLM agent is an agent in which an LLM makes the step-by-step decisions.**

The definition assembles what the Berkeley lecturers say:

- **Agent and environment.** Shunyu Yao, then speaking as a researcher on language agents, opens his Fall 2024 lecture by asking the room for a definition and seeing about three hands. His own is "an intelligent system that can interact with some environment" ([0:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=0)). The environment can be physical, such as a robot's surroundings, or digital, such as a game or a phone. If humans count as the environment, a chatbot is a kind of agent too ([2:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=120)).
- **The loop.** Dawn Song describes the same loop in her Fall 2024 introduction: the LLM is used for reasoning and planning, the agent observes the environment, takes actions in it, and uses tools and retrieval along the way ([0:00](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=0)).
- **Language in the middle.** Yao sorts agents into three nested levels. A **text agent** is one whose actions and observations are both in language. These existed long before LLMs. An **LLM agent** is a text agent that uses an LLM to act. A **reasoning agent** uses the LLM to reason in order to act (same moment).

Three words in the definition do most of the work:

- **Goal.** An end state that something outside the model can check: the order was placed, the tests pass.
- **Environment.** Whatever the system acts on and observes: a file system, a browser, an API, a database, a simulated shop.
- **Decides itself.** The model chooses among actions at run time. This is the part that separates an agent from a workflow.

Two things the definition does not say. It does not say "uses an LLM". Rule-based and reinforcement-learning agents qualify, and Yao insists on that history. It also excludes a single prompt-and-answer. One call has no steps and no environment.

## The workflow-to-agent spectrum

Yao's three levels describe what an agent is made of. Engineers also need a scale for how much control they hand over.

- A **workflow** is a set of LLM calls connected by code that you wrote. Your code decides the order. The model fills in the steps.
- An **agent** is a system where the model decides what to do next and when to stop, within a set of tools and a budget.

Most real systems sit between the two:

| Position | Who decides the next step | Example | Predictability | Cost |
|---|---|---|---|---|
| Single prompt | Your code (one step) | Classify a ticket | Highest | Lowest |
| Fixed workflow | Your code | Summarize, then translate, then check the format | High | Low |
| Workflow with a bounded loop | Your code, with a limit | Draft, critique, revise, at most three rounds | Medium | Medium |
| Agent | The model | A coding agent that reads a repository, edits files and runs tests until they pass | Lower | Higher and variable |
| Multi-agent system | Several models with roles | A reviewer agent and a coder agent that argue about a patch | Hardest to predict | Highest |

Dawn Song's Fall 2025 course-introduction slides use the phrase "agent workflow" and list what such workflows make possible: decomposing a task, assigning subtasks to specialized modules, dividing labor, and letting several agents generate answers together. The table above sharpens that wording into a scale. It is this repository's own synthesis, not a framework from the lectures.

<!-- SOURCE GAP: no packet states a workflow-to-agent spectrum. The two definitions and the table are the author's, built on Song's "agent workflow" slide and common industry usage. -->

A quick test for any system: **who decides?** If you can draw the sequence of model calls as a flowchart before anything runs, it is a workflow. If the sequence depends on what the model says at run time, it is an agent. Start at the left of the table. Move right only when the steps of the task cannot be written down in advance.

## A short history

Yao tells the history as three stages ([6:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=360)).

| Year | Step | Why it mattered |
|---|---|---|
| 1966 | ELIZA, a rule-based text agent | Agents that converse in text predate LLMs. They worked for one domain. |
| 2015 | LSTM-DQN, a text agent trained by reinforcement learning | Training by reward also predates LLMs. Again one domain, and long training. |
| 2020 | GPT-3 and few-shot prompting | One model handles many new tasks from a few examples, with no task-specific training |
| 2022 | Chain-of-thought prompting, WebShop, ReAct | Written reasoning steps; a realistic shopping environment; reasoning and acting in one loop |
| 2023 | WebArena, SWE-bench, and agent memory (Reflexion, Voyager, Generative Agents) | Benchmarks for real websites and real repositories; agents that remember |
| 2024–2025 | Berkeley's second agents course, open standards for tools and for agent-to-agent communication | Agents become products and infrastructure |

### Stage 1: agents before LLMs

Text agents existed from the beginning of AI, Yao notes. The rules of ELIZA and the reward-trained network of LSTM-DQN each solved one kind of task. Neither could be pointed at a new task without new work.

### Stage 2: reasoning and acting, separately

LLMs changed the economics: one pre-trained model, many tasks. Yao dates the start of LLM agents to GPT-3 in 2020. People then applied LLMs to two kinds of task, which became two separate paradigms ([14:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=840)):

- **Reasoning** means thinking in written steps, as in chain-of-thought. It adds thinking time but no outside knowledge. In Yao's words, "Even the biggest, smartest model in the world does not know the weather in San Francisco today" (same moment).
- **Acting** means calling something outside the model: retrieval, code execution, a tool. It adds knowledge, computation and feedback, but no reasoning.

### Stage 3: ReAct joins them

**ReAct** is Yao's method for doing both in one loop. The model writes a thought, then an action. The action runs in the environment. The observation comes back into the model's input. The loop repeats until the model finishes ([16:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=960)).

His example is a question from the time: could seven trillion dollars buy Apple, Nvidia and Microsoft? The model has two actions, a web search and a final answer. It reasons that it needs the market values, searches, gets them in one result and concludes that the money is not enough. Yao then feeds the model hostile observations. The search returns nothing, then a share price instead of a market value. Each time, the reasoning repairs the plan: search each company alone, then multiply shares by price ([18:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=1080)). Acting supplies facts that reasoning alone lacks. Reasoning recovers from what acting alone cannot.

### WebShop and what followed

**WebShop** (2022) is a shopping environment built on 1.16 million real Amazon products, as Yao's slides describe it. A program scores how well the product the agent finds matches the instruction. He calls it harder than the grid worlds of earlier research, for three reasons: it contains images as well as language, it uses real language, and the agent must plan over a long horizon, perhaps ten searches or products ([48:00](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=2880)). Its importance is that a realistic web task came with automatic scoring.

The next year brought benchmarks closer to work. **WebArena** (2023) tests agents on real websites. **SWE-bench** (2023) gives the agent a repository and an issue and expects a code change that fixes it. Yao describes the task as cleanly defined and hard to solve: the agent must explore the code, write tests and run them, "just like a software engineer" (same moment). His slides also list ChemCrow, an agent that helped plan the synthesis of a new chromophore, a colored compound.

Yao's summary of the stage is that the reasoning agent is a new kind of agent. Reasoning became an internal action the agent can take. Around it grew new methods: memory, planning, learning and multi-agent systems.

### The landscape in 2025

Dawn Song's Fall 2025 introduction notes that the first agents course in Fall 2024 met with "very little" talk of agents, and calls 2025 the year of agents. Her slides list four application areas: code generation, computer use, personal assistants and robotics. They also list what the ecosystem gained: many libraries and products, open standards for tool use (**MCP**) and for communication between agents (**A2A**), and many benchmarks.

Her warning is about evaluation. Open agent evaluation, she writes, suffers from three problems: a lack of standardization, because agents need manual adjustments to run on each benchmark; limited openness, because agents and environments are often not public; and low reproducibility, because results are painful or impossible to reproduce. Her course project responds with a shared platform where "green" agents host tasks and "white" agents are tested on them.

## Pitfalls

1. **Calling every LLM call an agent.** *Fix:* apply the who-decides test, and say "workflow" when your code decides.
2. **Starting with an agent.** Agents are costlier and less predictable. *Fix:* begin with a single prompt or a fixed workflow. Move right on the table only when the steps cannot be scripted.
3. **Assuming the model knows the environment.** *Fix:* give it tools and retrieval, and let observations correct its plan.
4. **Letting the loop run unchecked.** Each step is a model call. *Fix:* set a maximum number of steps, a token budget and a stopping condition.
5. **Trusting a benchmark score as proof of readiness.** *Fix:* evaluate in your own environment, with your own tasks. [Evaluation is the product](../03-evaluation/01-evaluation-is-the-product.md) starts there.

## Try it

**Deliverable:** a one-page review of five systems.

Take five systems you use or have read about, for example a ticket classifier, a retrieval question-answering pipeline, a coding agent, a thermostat and a chat support widget.

1. For each, write whether it is an agent, a workflow, or neither, and which position it has on the table.
2. Justify each with two sentences: who decides the next step, and what the budget is.
3. For one agent among them, draw the loop: observation, decision, action, and back.

**You are done when:** all five have a verdict with the two justifying sentences, and the loop diagram names the goal, the environment and the stopping condition.

**Stretch goal:** pick one system and design both a workflow version and an agent version of it. List what changes in predictability, cost and testability.

## Key takeaways

- An agent pursues a goal by observing, deciding and acting on an environment in a loop. An LLM agent has an LLM making the decisions.
- Agents predate LLMs. Text agents, rule-based or trained by reward, existed for decades and worked in one domain each.
- LLMs brought generality. ReAct joined written reasoning with external actions and showed that each repairs the other.
- WebShop, WebArena and SWE-bench moved evaluation from games to realistic websites and real repositories.
- Workflows and agents form a scale. Your code decides in a workflow, the model decides in an agent. Start simple and move right only when you must.

## Self-check

1. What separates an agent from a workflow?
   - A. The model decides the next action at run time
   - B. The system calls a language model more than once
   - C. The system uses at least one external tool
   - D. The system runs for longer than one minute

2. In Yao's terms, what is a text agent?
   - A. An agent whose actions and observations use language
   - B. An agent that answers questions from written documents
   - C. An agent whose decisions are made by an LLM
   - D. An agent that writes and edits long documents

3. What does ReAct interleave?
   - A. Thoughts, actions and observations
   - B. Prompts, fine-tuning and evaluation
   - C. Rewards, parameters and gradients
   - D. Retrieval, caching and compression

4. What made WebShop a step beyond earlier text games?
   - A. A realistic shopping task on real products, scored automatically
   - B. It trained a language model with rewards for the first time
   - C. It removed the need for a separate evaluation
   - D. It solved the task without any language model

5. Which three problems does Dawn Song's 2025 introduction name for open agent evaluation?
   - A. Weak standardization, limited openness, low reproducibility
   - B. High cost, slow response and heavy energy use
   - C. Privacy, copyright and bias in the training data
   - D. Too many benchmarks and too few agents to test

<details><summary>Show answers</summary>

1. A. A workflow connects model calls with code you wrote. An agent lets the model choose the next action.
2. A. Both sides of the interaction are in language. LLM agents are text agents that use an LLM.
3. A. The model thinks, acts in the environment, reads the observation, and repeats.
4. A. It combined real products, images and long horizons with an automatic score for how well the found product matched.
5. A. Agents need manual changes per benchmark, are often closed, and are hard to reproduce.

</details>

## Sources

- **Lecture:** Shunyu Yao, "LLM agents: brief history and overview", LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=RM6ZArd2nVc), used at [definition](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=0), [three levels of agent](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=120), [the storyline](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=360), [reasoning versus acting](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=840), [the ReAct loop](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=960), [hostile observations](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=1080), [WebShop and SWE-bench](https://www.youtube.com/watch?v=RM6ZArd2nVc&t=2880)
- **Lecture:** Dawn Song, course introduction, in Denny Zhou, "LLM Reasoning", LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=QL-FS_Zcmyo), used at [the agent loop](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=0), [why agents](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=120)
- **Slides:** Dawn Song, course introduction, UC Berkeley Agentic AI MOOC (Fall 2025), distributed with Yann Dubois, "Introduction to training LLMs for AI agents": [video](https://www.youtube.com/watch?v=r1qZpYAmqmg), used for the year-of-agents, agent-workflow, standards and evaluation slides
- **Reading:** Shunyu Yao et al., "WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents" (2022): [arXiv](https://arxiv.org/abs/2207.01206)

## Next

→ [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md). This chapter defined the loop. The next part takes it apart and shows how to build one.
