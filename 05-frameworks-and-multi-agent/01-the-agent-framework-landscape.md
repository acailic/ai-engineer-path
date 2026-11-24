# 01. The Agent Framework Landscape

**Level:** Practitioner · **Reading time:** 12 min · **Exercise:** 45 min
**Prerequisites:** [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md)

> **In one sentence:** After this chapter you can say what an agent framework does for you, what it takes away, and choose between five layers of abstraction for a task using numbers you measured yourself.

## Why this matters

In part 02 you built one agent by hand: a loop that sends the conversation to a model, runs the tools it asks for, and stops when the task is done. Call it 150 lines of Python. Then a teammate says "we should put this on a framework" and names three. Each has a quickstart that builds a "research team" in 20 lines.

Which one do you pick, and do you need any? The demos do not answer that. This chapter does. It shows what every framework is an abstraction over, maps the layers you can choose from, and gives a procedure for choosing with numbers from your own task.

## The core idea

An agent framework is a set of defaults for three things your hand-written loop already contains:

1. **State.** The list of messages and tool results sent to the model on each call.
2. **Control flow.** Who acts next: your code, the model, or another agent.
3. **Plumbing.** Model clients, retries, streaming, tool schemas, tracing, the button a human clicks to approve a step.

The analogy is a web framework. You can serve HTTP with the standard library; Flask or Django add routing, request parsing and sessions. The analogy breaks in one place. A web framework decides the control flow itself: a request matches a route and your handler runs. An agent framework shares that decision with a model that is **non-deterministic** (the same input can produce different output). So an agent framework is half a library and half a scheduler for a component nobody fully controls.

That split gives the most useful way to sort designs: by who writes the control flow.

- **Workflow.** Your code decides the order of steps. The model fills the steps in: classify this, summarize that.
- **Agent.** The model decides the next step. Your code sets limits: tools, budget, stop condition.

Jerry Liu draws the same line in the Fall 2024 lecture and calls the two ends constrained and unconstrained flows. A constrained flow is a router prompt (a prompt that picks one option out of several), a tool and a reflection step, with no loops; people write the control flow as `if` statements and `while` loops. An unconstrained flow hands the model a set of tools and lets it plan. It solves a wider range of tasks, but it may call tools it should not, loop forever and cost more ([56:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=3360)).

## How it works, step by step

### Five layers

Frameworks differ mainly in the layer they start from. Chi Wang made that point about his neighbors in the same lecture: LangGraph starts from graph-based control flows and CrewAI from high-level, static agent task workflows ([20:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=1200)).

| Layer | What it gives you | Who decides the control flow | Typical cost |
|---|---|---|---|
| 1. Model access | One client for many model providers: retries, streaming, structured output | Your code | Small. It may hide differences you need. |
| 2. Agent loop | One agent with tools, a run loop, a stop condition | The model | Small. You still build the system around it. |
| 3. Workflow engine | Steps as nodes in a graph or as events; saved state; approval steps | Your code | You must design the graph. |
| 4. Multi-agent conversation | Roles, group chats, handoffs between agents | Shared: a chat manager and the model | Tokens and latency grow with each agent and turn. |
| 5. Platform | Hosting, tracing, evaluation and model customization in one product | Your code, inside the product's model of the world | Lock-in and vendor pricing. |

One product can span several layers. AutoGen's documentation page, as of November 2026, describes four of them in one project: Studio, a web interface for prototyping without code; AgentChat, for conversational single- and multi-agent applications; Core, an event-driven framework for scalable multi-agent systems; and Extensions, components that connect to external services.

### What a framework solves, and what it costs

| It solves | It costs |
|---|---|
| Plumbing around model calls: retries, timeouts, structured output | A learning curve, and churn when the API is rewritten |
| Saving and resuming state between steps | Abstraction leaks: when the model misbehaves you need the raw messages, which the framework may hide |
| Multi-agent patterns you would otherwise write by hand | Debugging through layers you did not write |
| Approval steps and handoffs to humans | Lock-in: your application grows into the framework's shape |
| Tracing and logs | Overhead, and hidden prompts that spend tokens |

The churn is not hypothetical. AutoGen, the framework of the first lecture, was rebuilt on a new architecture after the lecture. As of November 2026 its documentation says the project is archived and no longer maintained, advises against production use, and points to Microsoft Agent Framework as the migration target. The lecture is from September 2024, twenty-six months earlier.

### A procedure for choosing

1. Write the loop by hand for the main path of your task. Keep it small. This is your baseline.
2. Measure the baseline on about 20 real cases: success, cost per case, latency per case.
3. Name the pain. Control flow? State that must survive a restart? Many models? Not knowing what was sent to the model? Each pain maps to one layer.
4. Decide who controls the flow. If the steps are known and must be audited, use plain code or a workflow engine. If the model must explore (a code base, a data set), use a thin agent library and add limits.
5. Run the black-box test. Can you print every message and edit every prompt? If not, stop.
6. Estimate the exit cost. Is the saved state plain JSON? Can your tools run without the framework?
7. Check maintenance: release history, number of active maintainers, any archive notice.
8. Rebuild the same 20 cases on the candidate and compare with the baseline.

## Worked example

The harness below runs two implementations of one task on the same cases. The two `solve` functions are yours: each returns the answer and the dollars it spent.

```python
# bakeoff.py — compare a hand-written loop with a framework on the same cases.
import time

cases = [
    {"input": "What is the standard VAT rate in Germany?", "expected": "19%"},
    {"input": "What is the standard VAT rate in France?", "expected": "20%"},
]  # use about 20 real cases from your own task

def baseline(case):        # your hand-written loop from part 02
    return ask_model_with_tools(case["input"])

def on_framework(case):    # the same task, rebuilt on the candidate framework
    return run_agent_team(case["input"])

def report(name, solve):
    ok, cost, started = 0, 0.0, time.perf_counter()
    for case in cases:
        answer, dollars = solve(case)
        ok += case["expected"] in answer
        cost += dollars
    seconds = time.perf_counter() - started
    print(f"{name:12} success {ok}/{len(cases)}  cost ${cost:.2f}  "
          f"{seconds / len(cases):.1f} s per case")

report("baseline", baseline)
report("framework", on_framework)
```

Observe three things. Success alone does not decide anything. Cost and seconds per case are where a framework hides its price: extra prompts, retries, agents that re-read the whole history. And your own time is a cost too, so record how long each implementation took to build. Adopt the framework only if it raises success, or clearly cuts your development time, without pushing the cost per case past what the task is worth.

Here is how the decision comes out for four common tasks:

| Task | Layer | Reason |
|---|---|---|
| Answer questions over 200 internal PDFs under a fixed policy | 1 and 3: model access plus a fixed workflow | The steps are known and must be identical every time |
| A coding agent that explores an unfamiliar repository | 2: a thin agent loop with strict limits | The model must choose where to look |
| Support triage that drafts a reply and hands hard cases to a person | 3, with an approval step | The path is fixed; the human decision is part of the path |
| Research across many long documents | 2 inside 3: a fixed outer loop, parallel workers inside | The split is known; what each worker reads is not |

## What the practitioners say

Chi Wang (then at AutoGen-AI) and Jerry Liu (LlamaIndex) shared the lecture of September 23, 2024.

- **The unit of programming is the conversation.** Wang shows a program with four agents: one that carries the user's request, a commander, a writer and a safeguard. The commander never executes code. When execution fails, it passes the error back to the writer. Building it takes three steps: create the agents, one line each; register the interaction patterns, each naming a sender, a receiver, the participants and a summary method; send the initial task. The framework runs the rest ([10:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=600)). Chapter 02 takes the idea apart.
- **Frameworks start from different points.** Wang describes AutoGen as covering many design patterns, LangGraph as starting from graph-based control flows and CrewAI from static, high-level task workflows ([20:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=1200)). This is one framework author describing competitors. Read it as a map of starting points, not a ranking.
- **The design is the open problem.** Wang ends by naming the largest open question: how to design the best multi-agent workflow for an application under quality, monetary cost, latency and manual effort at once ([36:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=2160)). No framework makes that choice for you.
- **Constrained beats general for many products.** Liu reports that many teams build constrained architectures on purpose, trading expressiveness for reliability, and that fewer products use wide, unconstrained flows ([54:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=3240), [58:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=3480)).
- **A low bar for the word "agent".** Liu offers what he calls a very rough definition: "a computer program that has non-zero LLM calls" ([58:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=3480)). One toolkit should then cover both ends. LlamaIndex's workflows are event-driven: steps pass messages, and a step can be plain Python or a model call.
- **Production looks ordinary.** In production, Liu says, each agent workflow sits behind an API, agent communication goes through a central message queue, and a human-in-the-loop step is a service that waits for a person's reply ([62:00](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=3720)). Those are distributed-systems problems that existed long before LLMs.

The AutoGen status in this chapter comes from its documentation page, opened on November 24, 2026. The current status of LangGraph, CrewAI and the other frameworks was not re-checked for this edition; treat them as examples of a layer, not as a buying guide.

## Pitfalls

1. **Adopting before you can write the loop.** Without a baseline you cannot tell a framework bug from a prompt bug. Fix: write the 150-line version first.
2. **Adding agents because the framework makes it easy.** Each agent multiplies tokens and adds a place to lose information. Fix: start with one agent and read [chapter 05](05-multi-agent-systems-ii-the-llm-era.md) before adding a second.
3. **Choosing by demo or by stars.** Demos show the happy path. Fix: run the bake-off on your own cases, and keep a [small evaluation harness](../03-evaluation/02-a-minimal-eval-harness.md) for it.
4. **Letting the framework hide prompts.** Fix: print every message in a test and assert on what the model was told.
5. **Assuming the API is stable.** AutoGen was rewritten after the lecture and is archived now. Fix: keep the framework behind an interface of your own, such as a function that takes a task and returns an answer and its cost.
6. **Picking a layer that fights the task.** A graph engine for an open-ended explorer, or a free-running agent for a regulated process. Fix: decide who controls the flow before you pick a tool. For the general habit, see [planning for mistakes](../07-ml-in-production/04-planning-for-mistakes.md).

## Try it

Take one task from your work. Build it twice: as a hand-written loop and on one candidate framework. Run at least 20 real cases through both.

Deliver a table with success, cost per case, seconds per case, lines of code and hours to the first successful debug, for each implementation.

You are done when the table has measured numbers and a one-paragraph recommendation that names the layer you chose and who controls the flow.

Stretch goal: switch the model provider in both implementations and record how many lines changed. That number is your lock-in.

## Key takeaways

- A framework supplies defaults for state, control flow and plumbing. It differs from a web framework because it shares control flow with a non-deterministic model.
- Sort frameworks by who writes the control flow, and by the layer they start from: model access, agent loop, workflow engine, multi-agent conversation, platform.
- Write and measure a hand-written baseline before you adopt anything.
- Both lecturers report that constrained flows win where reliability matters; unconstrained agents trade reliability and cost for expressiveness.
- Frameworks churn: AutoGen was rewritten after the lecture and was archived as of November 2026. Keep an exit path.

## Self-check

1. A regulated process requires that every step an agent takes be the same and be auditable. Which design fits best?
   A. An unconstrained agent with many tools
   B. A workflow with fixed steps and a model inside each step
   C. A group chat in which a model picks the next speaker
   D. A sampler that draws N answers and picks one
2. A framework's demo succeeds where your loop fails. What is missing before you adopt it?
   A. A second demo on a harder task
   B. The project's number of stars on GitHub
   C. Your own cases run through both, with cost and latency recorded
   D. A larger model behind the framework
3. In Liu's terms, a router prompt that picks one of several tools and has no loops is which kind of flow?
   A. Unconstrained
   B. Constrained
   C. A nested chat
   D. A population best response
4. What did AutoGen's documentation state as of November 2026?
   A. That version 0.2 is the recommended API
   B. That the project is archived and production use is advised against
   C. That AgentChat replaced Core
   D. That Studio is required to run agents
5. A workflow engine and an agent loop differ mainly in what?
   A. The model providers they support
   B. The price of tokens
   C. Who decides the next step
   D. The programming language they use

<details><summary>Show answers</summary>

1. B. Fixed steps make the path repeatable and auditable. The other designs let a model choose the path.
2. C. A demo shows one happy path. The decision needs your own cases with cost and latency, against your baseline.
3. B. People wrote the control flow; the model only picks an option.
4. B. The page carries an archive notice and points to Microsoft Agent Framework.
5. C. In a workflow engine your code decides; in an agent loop the model decides.

</details>

## Sources

- **Lecture:** Chi Wang and Jerry Liu, "Agentic AI Frameworks & AutoGen + Building a Multimodal Knowledge Assistant", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=OOdtmCMSOo4), used at [Wang's framing](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=0), [three steps](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=600), [starting points](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=1200), [open question](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=2160), [constrained flows](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=3360), [production](https://www.youtube.com/watch?v=OOdtmCMSOo4&t=3720)
- **Web:** Microsoft, AutoGen documentation (layers, install commands, archive notice): [microsoft.github.io/autogen/stable](https://microsoft.github.io/autogen/stable/), opened November 24, 2026

## Next

→ [AutoGen: Conversation Programming](02-autogen-conversation-programming.md), which takes apart the three-step program Wang shows and rebuilds it in plain Python.
