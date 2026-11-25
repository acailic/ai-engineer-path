# Lecture guide: Agents for Software Development

**Lecturer:** Graham Neubig (CMU) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 6 · **Length:** 1:02:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=f9L9Fkq-8K4) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/neubig24softwareagents.pdf)
**Chapters that cite this lecture:** [01. The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) · [02. Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md) · [03. Planning, Search and Decision-Making](../02-building-agents/03-planning-search-and-decision-making.md) · [07. Coding Agents](../02-building-agents/07-coding-agents.md) · [08. Training Models for Agentic Tasks](../02-building-agents/08-training-models-for-agentic-tasks.md)

> **In one sentence:** Graham Neubig shows what a coding agent must do beyond writing code (find the right files, plan, recover from errors and stay safe), and how benchmarks measure whether it does.

## Before you watch

Read [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) first; it teaches the agent loop that the lecture assumes. [Coding Agents](../02-building-agents/07-coding-agents.md) follows this lecture closely: read it afterwards, as the place where each part is explained a second time.

## The lecture, part by part

### [0:00–3:46](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=0) Why software, and where a developer's time goes

Graham Neubig introduces himself as a professor at CMU, chief scientist at All Hands AI and a maintainer of the open-source coding agent OpenHands. His motivation is a question: if everyone could write software quickly, what would they do? He cites Marc Andreessen's 2011 essay on software spreading through every industry and notes that two of that year's Nobel Prizes went to people who wrote software. A 2019 study at Microsoft then sets the scope: developers spend only 15% of their day writing code and 36% communicating, so writing code faster is not the whole job.
**In this book:** nothing beyond this guide; nearest: [Coding Agents › Why this matters](../02-building-agents/07-coding-agents.md#why-this-matters).

### [3:46–5:55](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=226) Levels of automation: completion versus an agent

He borrows the levels of self-driving cars. Level 0 is writing everything by hand, level 1 is smart completion as in GitHub Copilot or Cursor, level 2 is chat that refactors larger pieces, level 3 automates particular tasks, and level 4 solves a whole development task. Completion works in step with the developer and fills in the next line; this lecture is about the last level.
**In this book:** [Coding Agents › Why this matters](../02-building-agents/07-coding-agents.md#why-this-matters).

### [5:55–9:32](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=355) A development agent at work, and the productivity measured so far

In a live demo, OpenHands receives a request to add unit tests to a repository: it clones the repository, writes the tests, installs the dependencies, runs them, opens a branch and pushes it, and a person reviews the result before anything is merged. A second mode resolves a GitHub issue on request and proposes a pull request. On productivity, a GitHub study with 95 developers found that those with Copilot finished the task 56% faster.
**In this book:** [Coding Agents › OpenHands](../02-building-agents/07-coding-agents.md#openhands) · [Coding Agents › What the practitioners say](../02-building-agents/07-coding-agents.md#what-the-practitioners-say).

### [9:32–12:33](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=572) The challenges and the environments

Six challenges organize the rest of the talk: the environment, the observation and action space, code generation, file localization, planning with error recovery, and safety. Real developers work in source repositories, task boards, office documents and chat tools, yet almost every test environment covers only the coding part.
**In this book:** [Coding Agents › How it works, step by step](../02-building-agents/07-coding-agents.md#how-it-works-step-by-step) · [Coding Agents › 1. Environment](../02-building-agents/07-coding-agents.md#1-environment).

### [12:33–15:06](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=753) Coding benchmarks: from puzzles to real libraries

HumanEval and MBPP ask for a small function from a docstring, which tests algorithmic skill the way an interview puzzle does; it is a necessary condition, not a sufficient one. CoNaLa and ODEX use questions and answers from Stack Overflow, so the model must handle real libraries such as pandas. ARCADE uses data-science notebooks, where each new cell depends on the cells before it.
**In this book:** [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated).

### [15:06–17:45](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=906) SWE-bench and its limits

SWE-bench gives the model a real GitHub issue and its repository and asks for a change that passes the tests added with the fix. It demands long-context understanding and precise edits, but it keeps only well-maintained projects whose fixes came with new tests, so it leans toward bug fixes and away from features, refactoring and documentation. Public code also leaks into training data.
**In this book:** [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated).

### [17:45–21:19](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1065) Metrics and dataset leakage

The common metric is pass@k: the chance that at least one of k samples passes the unit tests, estimated from a larger number of samples to reduce noise. Where tests are missing, overlap with reference code is measured, by n-gram overlap (BLEU), by syntax-aware variants (CodeBLEU) or by embeddings (CodeBERTScore). Leakage shows in ARCADE, where new notebooks score far lower than published ones, and in LiveCodeBench, where some models score high on HumanEval and low on newer problems; a fresh revision of SWE-bench that removes leaked problems is mentioned but not on the slides.
**In this book:** [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated) · [Benchmark design and contamination](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#benchmark-design-and-contamination).

### [21:19–22:32](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1279) Multimodal coding models

Design2Code, a data set from Stanford, shows a model an image of a web page and asks for the code that renders it; a multimodal version of SWE-bench had appeared only days before the lecture. Scoring compares screenshots rather than text. A high-level score measures how close the visual embeddings of the generated page and of the original are, and a low-level score counts how many individual elements the model reproduced. A coding model can therefore start from what it sees, not only from a written specification.
**In this book:** nothing beyond this guide; nearest: [Coding Agents › How coding agents are evaluated](../02-building-agents/07-coding-agents.md#how-coding-agents-are-evaluated).

### [22:32–25:55](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1352) Code as the action space

A coding agent must understand the repository, read code, change or write it, and run it. CodeAct replaces one tool call per step with programs: to compare phone prices in four countries, the model writes one loop instead of some fifteen calls. Feedback still arrives, through errors at run time, but at a coarser grain, and the paper reports faster resolution and higher success than direct tool use.
**In this book:** [Coding Agents › 2. Action space](../02-building-agents/07-coding-agents.md#2-action-space) · [Coding Agents › The agent-computer interface](../02-building-agents/07-coding-agents.md#the-agent-computer-interface).

### [25:55–30:18](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1555) Editing tools and the OpenHands architecture

SWE-Agent gives the model specialized commands: a viewer returns a window of lines around the line it names, so files thousands of lines long fit in the context, and an edit command replaces a range of lines. OpenHands combines the two designs. Every action is a piece of code that can call those commands, so a search that finds ten places to change becomes a loop over ten edits, and the results come back as the next observation.
**In this book:** [Coding Agents › The agent-computer interface](../02-building-agents/07-coding-agents.md#the-agent-computer-interface) · [Coding Agents › OpenHands](../02-building-agents/07-coding-agents.md#openhands).

### [30:18–34:43](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1818) Training code models: data and infilling

Nearly all serious language models now train on code, partly because code also improves general reasoning. The Stack 2 is an open pre-training data set whose licenses were checked one by one. Its language distribution is uneven: Python, PHP, JavaScript, Java and C dominate, while deployment files and the languages of legacy banking systems are thin, and that gap becomes a gap in what models can do. Infilling is the second ingredient: a coherent span is masked out and moved to the end of the document, and the model learns to generate it, which suits a workload of editing more than of writing from scratch.
**In this book:** nothing beyond this guide; nearest: [Pre-training data](../01-foundations/02-how-large-language-models-are-trained.md#pre-training-data).

### [34:43–37:08](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2083) Context window extension

Models pre-train on short chunks, around 4,000 tokens, and generalize badly beyond that length, while code is long. The cause lies in positional encoding. RoPE, the common method, gives each position a set of rotation angles determined by the training length, so a longer input produces angles the model has never seen. Two fixes bring the angles back into the trained range: one multiplies them by a constant factor, the other scales only the low-frequency components and leaves the high-frequency ones alone, which keeps attention over long distances working without losing local detail.
**In this book:** nothing beyond this guide.

### [37:08–39:14](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2228) Context management

A completion model inside an editor has more to draw on than an issue description: the open file, the issue, the repository and other open tabs. A published description of Copilot's prompt shows how much engineering goes into this: text before and after the cursor, the 20 most recently used files in the same language, imported files and path metadata. In his view agent systems have not invested as much in this kind of prompt assembly.
**In this book:** [Coding Agents › 3. Context](../02-building-agents/07-coding-agents.md#3-context) · [Coding Agents › What the practitioners say](../02-building-agents/07-coding-agents.md#what-the-practitioners-say).

### [39:14–44:53](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2354) File localization and four strategies

Localization means finding the files a request is about, and he calls it possibly the largest open problem in coding agents; it resembles a robot first opening every kitchen cabinet. His own feature request names the wanted behavior but not the file. Four strategies follow: let an experienced user name the files; give the agent a search tool; build a map of the repository in advance, as Aider does; or search in stages, as Agentless does, from repository to files to functions.
**In this book:** [Coding Agents › 3. Context](../02-building-agents/07-coding-agents.md#3-context).

### [44:53–46:03](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2693) Retrieval-augmented code generation

The last strategy retrieves similar code with an embedding model and generates from what it found. Documentation can be retrieved as well, and it sometimes serves better than code, because a request written in English and its solution written in Python may look unrelated to a retriever. His impression is that no agent system uses retrieval well yet: deciding when to retrieve during a task remains an unsolved problem, and he expects the field to move in that direction.
**In this book:** nothing beyond this guide; nearest: [C. Retrieval: the standard pipeline](../02-building-agents/04-memory-and-knowledge-for-agents.md#c-retrieval-the-standard-pipeline).

### [46:03–51:51](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2763) Planning and error recovery

Many top systems on the leaderboard hard-code their process: Agentless localizes, generates several patches, validates them and keeps one that passes, which is cheap and effective but cannot decide to read documentation online. CodeR lets a manager write a plan for sub-agents (one reproduces the fault, one localizes it, one edits the code and one verifies the fix), yet plans often rest on wrong assumptions, so an executor needs a way to send a failed plan back to the planner, as CoAct does. Finally, an agent can run the code, read the error and fix it, but one leading model retries the same failed fix until it runs out of turns, so training for recovery is an open topic.
**In this book:** [Coding Agents › What the practitioners say](../02-building-agents/07-coding-agents.md#what-the-practitioners-say) · [Planning, Search and Decision-Making › How it works: six patterns](../02-building-agents/03-planning-search-and-decision-making.md#how-it-works-six-patterns).

### [51:51–57:06](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=3111) Safety: harm, sandboxing and least privilege

Harm comes first by accident: an agent asked to commit pushed to the main branch on its own, and one told to make tests pass deleted them; intentional misuse, such as hacking, is the second case. The mitigations come from ordinary software security. OpenHands runs every action in a Docker container isolated from the host, and credentials follow the principle of least privilege: fine-grained GitHub tokens name the repositories and permissions an agent receives. An agent locked away with no access is safe and useless, so the goal is helpful and harmless at once.
**In this book:** [Coding Agents › 6. Safety](../02-building-agents/07-coding-agents.md#6-safety) · [6. Enforce least privilege on every action](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md#6-enforce-least-privilege-on-every-action).

### [57:06–58:05](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=3426) Post-hoc auditing

Each action is checked after the model generates it and before it runs. A harmless action is executed; a harmful one is blocked, and the agent receives a message that the action is dangerous. The check can use a language model, static analysis or vulnerability-detection tools, or a mix; OpenHands ships such a security analyzer, built with outside partners.
**In this book:** [Coding Agents › 6. Safety](../02-building-agents/07-coding-agents.md#6-safety).

### [58:05–1:02:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=3485) Conclusion and future directions

Copilots already pay off, and in some of his repositories an agent drafted half of the commits; he expects agents to take over mundane tasks within one or two years. Three directions remain: agentic training, so that models follow agent formats, plan and recover better; evaluation of human-in-the-loop work, since watching and steering an agent helps and no benchmark measures it; and tasks beyond coding, where almost no benchmarks exist. He closes by inviting listeners to try the toolkit.
**In this book:** [Coding Agents › What the practitioners say](../02-building-agents/07-coding-agents.md#what-the-practitioners-say) · [Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

## What to take away

- Completion tools already double coding speed, yet coding is 15% of a developer's day; the larger prize is an agent that finishes a whole task.
- Code is a powerful action space: one program can do what many tool calls did.
- Finding the right files is the hardest open step; maps, staged search and retrieval each solve part of it.
- Benchmarks built from public code lean toward bug fixes and are contaminated by training data, so read scores with that in mind.
- Sandboxing, least-privilege credentials and auditing each action before it runs are the three safety measures.

## Sources

- Graham Neubig, "Agents for Software Development", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=f9L9Fkq-8K4).
- Slides: [Agents for Software Development](https://rdi.berkeley.edu/llm-agents-mooc/slides/neubig24softwareagents.pdf).
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
