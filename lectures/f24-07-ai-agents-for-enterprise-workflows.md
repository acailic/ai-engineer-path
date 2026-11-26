# Lecture guide: AI Agents for Enterprise Workflows

**Lecturer:** Nicolas Chapados (ServiceNow) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 7 · **Length:** 1:12:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=-yf-e-9FvOc) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/agentworkflows.pdf)
**Chapters that cite this lecture:** [06. Agent Infrastructure: Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) · [07. Agents in the Enterprise](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md)

> **In one sentence:** Nicolas Chapados and Alexandre Drouin of ServiceNow show what it takes to put agents into company workflows: a framework built on one log, web agents that click through interfaces, and benchmarks that measure how far those agents still are from people.

## Before you watch

Read [Agents in the Enterprise](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) first, then [Agent Infrastructure: Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md); its second half covers web agents and their benchmarks. You do not need any chapter of part 06.

## The lecture, part by part

### [0:00–4:50](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=0) Agents in the context of work

The lecture frames agents by the people who use them: who they are, their role, their work and the context of deployment. ServiceNow, with 25,000 employees, sells a platform for automating company workflows in IT, human resources and customer support.
**In this book:** not needed (course introduction).

### [4:50–9:31](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=290) What an LLM agent is, and its two kinds

An LLM agent plans, acts, receives feedback and pursues a goal over several iterations. Unlike a game-playing agent, it has read the documentation of everyday business software. Two kinds follow: an API agent calls formally specified tools; a web agent clicks and fills forms like a person.
**In this book:** [Agent Infrastructure: Sandboxes, Browser Use and Protocols › Part 2: Browser and computer use](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#part-2-browser-and-computer-use).

### [9:31–15:00](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=571) Enterprise workflow automation

One access problem takes a human agent many manual steps, although a generative feature now writes the resolution notes. Automation has climbed from scripting and robotic process automation to agentic workflows, which suit the long tail: tasks too varied to script, tiny one by one and huge in aggregate.
**In this book:** [Agents in the Enterprise › Chapados: what deployment looks like](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#chapados-what-deployment-looks-like).

### [15:00–17:04](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=900) Web agent demonstration

A short video shows a web agent asked for directions from a company's headquarters to a conference. It searches, reaches a maps service, and cannot find the event there. It then asks the person for more details, is told that the destination is the GTC conference, and plans again: it searches, finds the venue and enters it in the maps service. The lesson: an agent should be allowed to ask a person for clarification, and it should plan and replan on its own.
**In this book:** nothing beyond this guide.

### [17:04–23:53](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=1024) TapeAgents: one log for building and optimizing

Building frameworks such as LangGraph and AutoGen give fine control; optimization frameworks such as DSPy tune prompts. TapeAgents joins the two around the tape, a structured log of every agent's thoughts, actions and the environment's replies, which is itself data: other agents read it to debug, tune prompts or produce training data.
**In this book:** [Agents in the Enterprise › Worked example: two lecturers, one system](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#worked-example-two-lecturers-one-system).

### [23:53–32:08](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=1433) Case study: a cheap student from a costly teacher

For an assistant that helps users fill in complex forms, a teacher agent on a 405-billion-parameter Llama model records its tapes. From them an 8-billion-parameter student is fine-tuned, and it matches the teacher's score at more than 300 times lower cost. Quality is scored on six attributes, from grounded to helpful.
**In this book:** [Agents in the Enterprise › Chapados: what deployment looks like](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#chapados-what-deployment-looks-like).

### [32:08–37:47](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=1928) A basic web agent in one prompt

The second speaker builds a web agent from three parts: a prompt with the goal, the page as HTML and the allowed actions; a model call that returns actions; and a driver, Python with Playwright, that applies them. A GPT-4 agent fills in an expense report, but the video runs eight times faster than reality.
**In this book:** [Agent Infrastructure: Sandboxes, Browser Use and Protocols › Part 2: Browser and computer use](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#part-2-browser-and-computer-use).

### [37:47–44:16](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=2267) Three kinds of benchmark

MiniWoB++ holds toy tasks. Trace-based benchmarks on real websites compare an agent with recorded human steps, which ignores alternative solutions and risks memorization. Live benchmarks check the end result instead: WebArena serves local copies of open-source sites, while remote benchmarks add real latency but can be unreliable.
**In this book:** [Multimodal Agents: Web and Computer Use › Benchmarks to know](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#benchmarks-to-know) · [Agent Infrastructure: Sandboxes, Browser Use and Protocols › What the practitioners say](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#what-the-practitioners-say).

### [44:16–52:10](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=2656) WorkArena: tasks on a real product

WorkArena has about 600 tasks on the ServiceNow product; the tasks are open source, the product is not, and back-end APIs check the end state. Humans succeed on about 94 percent of the realistic workflows; a strong agent reaches 42.7 percent on the simplest level, has little success on the second and scores zero on the third. It fails to plan, invents controls and writes wrong action syntax.
**In this book:** [Agent Infrastructure: Sandboxes, Browser Use and Protocols › What the practitioners say](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#what-the-practitioners-say).

### [52:10–55:35](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=3130) BrowserGym and AgentLab

BrowserGym puts most major benchmarks under one interface, with a standard observation space (HTML, accessibility tree, screenshot) and action space (click by element number or by coordinates). AgentLab adds building blocks and an inspection view of a run, and is building public trace repositories with versions and dates, so that results can be reproduced.
**In this book:** [Agent Infrastructure: Sandboxes, Browser Use and Protocols › Part 2: Browser and computer use](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#part-2-browser-and-computer-use) · [Agent Infrastructure: Sandboxes, Browser Use and Protocols › What the practitioners say](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#what-the-practitioners-say).

### [55:35–1:00:01](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=3335) Six hurdles for web agents

A page holds hundreds of thousands of tokens, little of it relevant. The target page lies two or three pages away. Agents must learn from mistakes, use vision, and run faster. And they are unsafe: white-on-white text on a page hijacked the demonstrated agent, and a malicious browser extension could hijack an agent into making a wire transfer.
**In this book:** [Agent Infrastructure: Sandboxes, Browser Use and Protocols › What the practitioners say](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#what-the-practitioners-say) · [Jailbreaks and Prompt Injection](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md).

### [1:00:01–1:04:00](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=3601) A team of agents around one ticket

The lecture returns to the access problem from the start. Before the human agent opens the ticket, one agent proposes a plan as a list of steps, and an orchestrator asks her to approve it. Other agents then execute the sub-tasks, and the agent that changes permissions asks for confirmation again before anything destructive. Two human approvals are built into the flow; the agents do the rest of the work.
**In this book:** [Agents in the Enterprise › How it works, step by step: from notebook to workflow](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#how-it-works-step-by-step-from-notebook-to-workflow).

### [1:04:00–1:08:00](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=3840) Measuring the impact on knowledge work

Knowledge work covers thousands of tasks. To estimate how far agents can automate them, the lecture turns to the O*NET database of the United States Bureau of Labor Statistics, which lists the tasks of every occupation, and to adoption curves published by McKinsey. Technology is only one gate on adoption. Two assessments triangulate: a top-down estimate that asks a model to rate each task, and a bottom-up rate measured on a benchmark such as WorkArena.
**In this book:** nothing beyond this guide.

### [1:08:00–1:12:00](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=4080) Centaur and cyborg, then resources

A study by Harvard Business School and the consulting firm BCG found two patterns in how people divide work with generative AI. In the centaur pattern the person plans the task and hands large chunks to the AI. In the cyborg pattern person and machine collaborate in a fine-grained way. Which pattern suits a person and a task is open research. The lecture ends with a timeline of agent frameworks and benchmarks and with the open-source repositories of all four tools.
**In this book:** nothing beyond this guide.

## What to take away

- The opportunity for agents is the long tail of tasks too varied to script.
- The tape, one structured log of thoughts, actions and replies, serves debugging, prompt tuning and distillation.
- Judge web agents by the end state, not by similarity to a person's steps.
- On realistic workplace workflows people reach about 94 percent and agents nearly zero.
- Injection inside page content is the main safety risk of an agent that browses.

## Sources

- Nicolas Chapados, "AI Agents for Enterprise Workflows", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=-yf-e-9FvOc).
- Slides: <https://rdi.berkeley.edu/llm-agents-mooc/slides/agentworkflows.pdf>.
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
