# Lecture guide: AI Agents to Automate Scientific Discoveries

**Lecturer:** James Zou (Stanford) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 8 · **Length:** 1:02:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=yqPIsTTdUkc)
**Chapters that cite this lecture:** [03. Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** James Zou shows three ways agents change research: a Virtual Lab in which a team of agent scientists designs proteins, a method that turns any paper into an agent that applies its methods, and a conference written and reviewed by agents, with what it revealed about how well agents do science.

## Before you watch

Read [Agents for Scientific Discovery](../06-frontier-applications/03-agents-for-scientific-discovery.md) first; it summarizes this lecture and Percy Liang's in a few pages. The lecture assumes only that you know what a language model agent is; the biology is explained as it appears.

## The lecture, part by part

### [0:00–3:11](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=0) From tool to co-scientist

AI in science used to mean one curated tool for one well-defined problem, as a structure predictor is for protein folding. The shift of the past year is toward AI as a co-scientist that helps form hypotheses, design experiments, analyze data and write papers. Agents built on language models make this possible because they can use domain tools and reach databases. Three examples follow: the Virtual Lab, paper to agent, and a conference run by agents.
**In this book:** [Agents for Scientific Discovery › Why this matters](../06-frontier-applications/03-agents-for-scientific-discovery.md#why-this-matters).

### [3:11–10:57](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=191) The Virtual Lab: a research group of agents

The open-source platform mirrors a real lab. A human describes a project to the professor agent, which decides what expertise is needed and creates student agents with it; each is a frontier model tuned to use scientific tools. The agents hold group meetings to plan and one-on-one meetings to review subtasks. In the first project, designing binders for new coronavirus variants, the immunologist agent proposed nanobodies, small relatives of antibodies found in camels; the machine-learning agent agreed because their small size makes structures easier to predict; a scientific critic warned that public nanobody data are scarce, so models may overfit. Meetings take a few seconds to a minute and run in parallel, five per question; the professor agent reads the records of all five meetings and picks the consensus. Humans speak about 1% of the time.
**In this book:** [Agents for Scientific Discovery › How it works, step by step](../06-frontier-applications/03-agents-for-scientific-discovery.md#how-it-works-step-by-step).

### [10:57–15:03](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=657) The agent school: how specialists are trained

Frontier models sometimes lack the newest knowledge or tools of a narrow field. Given topics, an agent writes its own curriculum as questions, searches the web, downloads open-access papers for each question, and reads them while supervised fine-tuning updates its weights by next-token prediction. Teacher agents then quiz it; a failing agent returns to train more before it graduates. Agents that start from the same base model diverge into specialists, and a team of specialists collaborating beats one agent taught everything. The school takes about a day and is almost fully autonomous.
**In this book:** [Agents for Scientific Discovery › How it works, step by step](../06-frontier-applications/03-agents-for-scientific-discovery.md#how-it-works-step-by-step).

### [15:03–20:01](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=903) Case study: nanobodies for a new variant

The agents built a design pipeline: a protein language model scores each candidate sequence for stability, a structure predictor models how it binds the viral spike protein, and a physics simulator relaxes the structure and estimates binding affinity. They changed the scoring function of the first tool and combined the tools in a way no earlier publication had, which the lecturer calls combinatorial creativity. Billions of possible designs shrank to 92 candidates. Humans then made the nanobodies: a human-designed one failed to bind the new variant while the agent-designed one bound it, and the new designs did not stick to unrelated human or viral proteins, a sign of fewer side effects. The agents designed the pipeline and the protein within a few days.
**In this book:** [Agents for Scientific Discovery › How it works, step by step](../06-frontier-applications/03-agents-for-scientific-discovery.md#how-it-works-step-by-step).

### [20:01–26:11](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1201) What the Virtual Lab taught about teams of agents

Other groups now use the platform for Alzheimer's biomarkers and new materials. Teams often beat a single agent because they debate and must resolve disagreements, which yields more creative and robust reasoning. Each agent keeps notes of past meetings and a sandbox in which it can modify tools. Who speaks first or most changes which ideas win, so the parallel meetings can assign different personalities and speaking orders and show which team works best, a petri dish for the science of science. In the questions, the lecturer adds: an idea reached by several parallel meetings tends to be more reliable; drift and compounding errors are curbed by external memory, a periodic summary by the professor agent, the critic, and humans who read meeting summaries and redirect.
**In this book:** [Agents for Scientific Discovery › How it works, step by step](../06-frontier-applications/03-agents-for-scientific-discovery.md#how-it-works-step-by-step).

### [26:11–33:41](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1571) Paper to agent: every paper becomes its own correspondent

A paper is a passive artifact; its code is hard to reuse. The idea is to turn each paper into an interactive agent, a virtual corresponding author that knows the paper and can apply its methods to a reader's problem. Worker agents set up the paper's code in a virtual environment, extract its tools and check that the original results reproduce. The result is packaged with the Model Context Protocol, an industry standard for passing resources to a language model, and connected to a chatbot. Examples: an agent for a single-cell analysis tool whose figures matched human experts' exactly, and an agent for a DeepMind model of mutation effects that proposed a candidate gene for LDL cholesterol. On a set of real tasks the paper agents solved every task with less than a third of the running time of a coding agent given the paper and its repository.
**In this book:** [Agents for Scientific Discovery › Two more Zou systems](../06-frontier-applications/03-agents-for-scientific-discovery.md#two-more-zou-systems).

### [33:41–43:42](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2021) Agents that collaborate with other agents' papers

A method agent from one university and a data agent from another can ask whether the method fits the data and work without the emails and meetings that stall human collaboration. The mutation-effects agent joined a large genetic study of ADHD and found a splicing change associated with risk that no earlier paper reported. In the questions: converting a paper costs under a dollar; a paper with a poorly documented or irreproducible code base cannot be converted, which is itself a useful signal to its authors; large data sets are linked, not loaded.
**In this book:** [Agents for Scientific Discovery › Two more Zou systems](../06-frontier-applications/03-agents-for-scientific-discovery.md#two-more-zou-systems).

### [43:42–50:01](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2622) A conference written and reviewed by agents

Existing venues forbid AI-authored papers, which makes it hard to collect the data needed to learn how creative agent scientists are or how well agents review. The Agents4Science 2025 conference reversed the rule: an AI agent must be the lead author and do most of the work, other agents review, and every submission and review is public. Each paper documents the human-AI split per stage, and human experts assessed the top papers. There were over 300 submissions and 48 accepted papers, across engineering, physics, medicine and the social sciences. Accepted papers had more human involvement than the pool; humans were relatively more involved in hypothesis generation and experimental design, though AI still contributed a lot, while AI was given full autonomy most often in data analysis and writing.
**In this book:** [Agents for Scientific Discovery › Two more Zou systems](../06-frontier-applications/03-agents-for-scientific-discovery.md#two-more-zou-systems).

### [50:01–54:35](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3001) How the reviewing agents behaved

Three models did the reviewing, calibrated on earlier accept and reject decisions, scored each paper from 1 to 6. On the same papers GPT-5 gave the lowest scores, Gemini the highest, and Claude sat between and came closest to the human experts. One review caught statistics in the text that disagreed with the tables. Gemini also flattered, calling a study groundbreaking where humans noted important limitations. An automated pipeline searched for every cited title: 44% of papers had every reference verified, 56% had at least one that could not be found, usually one or two.
**In this book:** [Agents for Scientific Discovery › What the practitioners say](../06-frontier-applications/03-agents-for-scientific-discovery.md#what-the-practitioners-say) · [Agents for Scientific Discovery › Pitfalls](../06-frontier-applications/03-agents-for-scientific-discovery.md#pitfalls).

### [54:35–57:48](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3275) Three agent-led papers

One simulated a job market with agents playing both applicants and firms and tested how information changes market efficiency; a Nobel laureate in economics reviewed it favorably. Another simulated astronaut crews and their stress before and after crises, agreeing with real mission data. A third set a team of agents, among them a medicinal chemist, on drug candidates.
**In this book:** [Agents for Scientific Discovery › What the practitioners say](../06-frontier-applications/03-agents-for-scientific-discovery.md#what-the-practitioners-say).

### [57:48–1:02:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3468) Limits, and where people still matter

Agents use and adapt existing tools better than they invent new ones; they could not build the next structure predictor. They search breadth-first across many fields where human researchers go deep into one, so they complement each other in interdisciplinary work. They misjudge a problem when its context is missing, so metadata must be captured in a form agents can use and scientists must keep reviewing their assumptions. Most work stays computational; real experiments still depend on people.
**In this book:** [Agents for Scientific Discovery › What the practitioners say](../06-frontier-applications/03-agents-for-scientific-discovery.md#what-the-practitioners-say).

## What to take away

- A team of specialist agents with a critic, parallel meetings and a memory plans research and designs protein candidates in days.
- A paper converted into an agent lets readers apply its methods and lets papers collaborate with each other.
- Agents reviewed papers differently from each other and from people, and more than half of agent-written papers cited at least one unverifiable reference.
- People still supply the goal, the context, the new methods and the wet-lab validation.

## Sources

- James Zou, "AI Agents to Automate Scientific Discoveries", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=yqPIsTTdUkc).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
