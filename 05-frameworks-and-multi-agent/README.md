# Part 05: Frameworks, Infrastructure and Multi-Agent Systems

**Level:** Practitioner · **Seven chapters** · **About 95 minutes of reading and 7.5 hours of exercises**

In part 02 you built one agent by hand. This part answers what comes next:

- Should a framework carry that loop, and which one?
- What are the design ideas behind the major frameworks?
- When do several agents pay for themselves?
- What infrastructure do agents run on, and what does an agent need before a company will trust it?

## The chapters

| # | Chapter | Reading | You learn to |
|---|---|---|---|
| 01 | [The Agent Framework Landscape](01-the-agent-framework-landscape.md) | 12 min | Say what a framework solves and costs, sort frameworks into five layers, and choose one against a measured baseline |
| 02 | [AutoGen: Conversation Programming](02-autogen-conversation-programming.md) | 14 min | Describe an agent system as a conversation between peers and build a small one in plain Python |
| 03 | [LlamaIndex: Building a Knowledge Assistant](03-llamaindex-knowledge-assistants.md) | 13 min | Turn messy private documents into a retrieval pipeline, and add agent reasoning only where retrieval fails |
| 04 | [Multi-Agent Systems I: Games and Self-Play](04-multi-agent-systems-i-games-and-self-play.md) | 13 min | Say when self-play finds an unbeatable strategy on its own and why cooperating with people needs human data |
| 05 | [Multi-Agent Systems II: The LLM Era](05-multi-agent-systems-ii-the-llm-era.md) | 15 min | Decide, with a measured reason, whether a second LLM agent earns its cost |
| 06 | [Agent Infrastructure: Sandboxes, Browser Use and Protocols](06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) | 16 min | Choose where an agent's actions run, decide between APIs and a browser, and read a tool protocol |
| 07 | [Agents in the Enterprise](07-agents-in-the-enterprise.md) | 12 min | Take an agent from a notebook to a company workflow with sources, approvals and evaluation |

## How to read this part

Read it in order the first time. Chapters 01 to 03 come from one lecture and build on each other. Chapters 04 and 05 form a pair: what game research proved, and what of it applies to LLM systems. Chapter 06 is about the machinery underneath, and chapter 07 puts it into a company.

If you only need a decision, read 01, then 05, then 06.

Every chapter has runnable code that needs no API key: the models are stubs, and the point of each example is in the part around the model. Where an exercise calls a real model, the chapter says so and estimates the cost.

## A note on dates

The lectures are from September 2024 to November 2025. This field moves, so the chapters mark what was checked and when.

- **AutoGen is archived.** Its documentation, opened on November 24, 2026, says the project is no longer maintained and points to Microsoft Agent Framework. Chapters 01 and 02 teach the design ideas and say so.
- **MCP is described from its documentation**, opened the same day, plus the 2025 revisions of its specification, which were not re-opened.
- **Sandbox and browser-use products were not re-checked.** Chapter 06 describes categories and selection criteria and names no products as recommendations.

## Capstone project

A grounded assistant for one company workflow. It brings the whole part together.

1. **Grounding.** Pick about 20 documents and 20 questions with known answers, including one about a table and one about a figure (chapter 03). Show the source passage next to every answer.
2. **Choice.** Write the first version as a hand-written loop, then decide with the procedure of chapter 01 whether a framework earns its place.
3. **Design.** Keep the flow constrained. If you add a second agent, justify it with the four reasons of chapter 05 and compare against the single-agent baseline.
4. **Infrastructure.** Run every model-written command in a sandbox, and expose the tools behind one interface (chapter 06).
5. **Evaluation.** Report success, cost and latency on the 20 questions, plus the share of claims that a cited source supports (chapter 07).

You are done when a colleague can run your evaluation and get the same numbers, and your report names the design, the reason for each agent, and the cost per question.

## Sources

- Chi Wang and Jerry Liu, "Agentic AI Frameworks & AutoGen + Building a Multimodal Knowledge Assistant", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=OOdtmCMSOo4) · [guide](../lectures/f24-03-agentic-ai-frameworks-and-autogen-building-a.md). Chapters 01, 02, 03.
- Noam Brown, "Multi-Agent AI", UC Berkeley Agentic AI MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=SrLcGdVOb9w) · [guide](../lectures/f25-06-multi-agent-ai.md). Chapters 04, 05.
- Oriol Vinyals, "Multi-Agent Systems in the Era of LLMs", UC Berkeley Agentic AI MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=ntjOxjZMaac) · [guide](../lectures/f25-10-multi-agent-systems-in-the-era-of-llms.md). Chapters 05, 06.
- Nicolas Chapados, "AI Agents for Enterprise Workflows", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=-yf-e-9FvOc) · [guide](../lectures/f24-07-ai-agents-for-enterprise-workflows.md). Chapters 06, 07.
- Burak Gokturk, "Enterprise trends for generative AI, and key components of building successful agents/applications", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=Sy1psHS3w3I) · [guide](../lectures/f24-04-enterprise-trends-for-generative-ai-and-key.md). Chapter 07.

## Lecture guides for this part

Each guide maps one lecture from its first minute to its last and says where this book teaches each piece. Where no chapter teaches a part of the lecture, the guide explains it itself; the table counts those parts.

| Lecture | Lecturer | Length | Parts no chapter teaches | Guide |
|---|---|---|---|---|
| Agentic AI Frameworks & AutoGen + Building a Multimodal Knowledge Assistant | Chi Wang (AutoGen-AI); Jerry Liu (LlamaIndex) | 1:06:00 | 0 of 17 | [open guide](../lectures/f24-03-agentic-ai-frameworks-and-autogen-building-a.md) |
| Multi-Agent AI | Noam Brown (OpenAI) | 56:00 | 2 of 18 | [open guide](../lectures/f25-06-multi-agent-ai.md) |
| Multi-Agent Systems in the Era of LLMs | Oriol Vinyals (Google DeepMind) | 1:00:00 | 1 of 16 | [open guide](../lectures/f25-10-multi-agent-systems-in-the-era-of-llms.md) |
| Enterprise trends for generative AI, and key components of building successful agents/applications | Burak Gokturk (Google) | 1:04:00 | 2 of 17 | [open guide](../lectures/f24-04-enterprise-trends-for-generative-ai-and-key.md) |
| AI Agents for Enterprise Workflows | Nicolas Chapados (ServiceNow) | 1:12:00 | 4 of 14 | [open guide](../lectures/f24-07-ai-agents-for-enterprise-workflows.md) |

## Where to go next

- Evaluation of agents, including multi-agent systems: part 03.
- Security of agents: part 04.
- Deploying and operating a system in production: parts 07 and 08.
