# 08. Case Study: Berkeley's Green Agent and White Agent Project

**Level:** Practitioner · **Reading time:** 15 min · **Exercise:** 30 min
**Prerequisites:** [Evaluating Agents: Trajectories and Environments](04-evaluating-agents-trajectories-and-environments.md)

> **In one sentence:** After this chapter you can describe Berkeley's Fall 2025 course project as its lecturers defined it: a green agent that hosts an evaluation, a white agent that attempts the tasks, and a grading scheme that rewards testing the evaluator itself.

## Why this matters

Everything in this part is practice for one role: the team that builds the evaluator. Berkeley's Agentic AI course makes that role the first half of its project. Students do not build an agent first. They build the thing that will judge agents.

The project is a compact specification of what an evaluator must do. This chapter is the reference for it.

## The project in one paragraph

The course is CS 294/194-196, *Agentic AI*, Fall 2025, taught by Dawn Song. In the lecture of October 6, 2025, two members of the course staff introduced Phase 1 of the project: building a **green agent**. Their analogy: "Like math exams are designed by math teachers and physics exams by physics teachers" ([64:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3840)). Each subject has its own examiners. Each evaluation should have its own hosting agent.

| Term | Meaning in the course |
|---|---|
| **Green agent** | The hosting agent. It defines the assessment, prepares the environment, hands out tasks, and reports the metrics. |
| **White agent** | A participant agent: the one being tested. The lecture also calls it the competition agent. |
| **AgentBeats** | The platform that hosts assessments, where green agents and white agents meet. |
| **A2A** | The Agent2Agent protocol, an open convention for agents to exchange tasks and messages over the network. |
| **MCP** | The Model Context Protocol, an open convention through which a server exposes tools to a model. |

The colors have a history, which the lecture gives. In early work on safety benchmarks the team used red-team and blue-team setups. To name the judges and the other participants it introduced more colors, green and gray. "Green agent" stayed as the name of the host, and everyone else became a "white agent".

**One point of precision.** In this lecture the white agent is the agent under test. It is not an attacker, and it is not a monitor. The only link to adversarial testing is the naming history.

<!-- SOURCE GAP: The brief for this part lists "the kinds of attacks the white agent must catch" as a topic of this chapter. Neither the f25-04 lecture packet nor the Fall 2025 course page describes attacks between agents or any attack category, and in both sources the white agent is the agent under test. No attack content could be written from the sources. -->

## What the green agent must do

The lecture lists five responsibilities ([66:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3960)):

1. Prepare the environment.
2. Distribute the test tasks to the participant agents.
3. Collect their results.
4. Verify the environment.
5. Report back to the platform.

The lecturer's image is the technician at a repair shop, who runs the whole inspection. The green agent also designs and implements the metrics. It talks to the platform through MCP, A2A or plain APIs, can request permissions and resources, and submits results at the end.

An assessment runs in four steps:

1. The platform confirms that all agents, including the green agent, are online and reset.
2. It sends a task to the green agent, with the URLs of the participant agents to be tested.
3. The green agent orchestrates the interaction: assigning tasks, supervising execution, managing tools and environments, and reporting updates to the platform.
4. The green agent submits the metrics, which it defines through its implementation.

A green agent is built from three parts ([72:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=4320)):

- **A dataset of test tasks.**
- **A predefined testing process:** which agent is tested first, in what order tasks are sent, and how tools are provided.
- **The environment where tasks run:** extra tools or MCP modules, and instructions that tell white agents how to use them.

AgentBeats offers a prompt-based toolkit for a quick prototype. Stricter workflows and custom environments are hand-coded. The staff expected students taking two or more units to hand-code their green agents. Any web service that complies with A2A can serve as one.

## What the white agent must do

The white agent receives tasks over A2A and attempts them with the tools and environment the green agent provides. Students build white agents in Phase 2, after the green agent is finished. In the course's worked example, which integrates τ-bench, the white agent is prompt-based and built with Google's Agent Development Kit.

## Two kinds of project

| | Type 1: integrate an existing benchmark | Type 2: build a new benchmark |
|---|---|---|
| Goal | Adapt a published benchmark into a green agent on AgentBeats | Create a benchmark where none exists |
| Examples named | SWE-bench Verified, Terminal-Bench | Organizing a calendar, scheduling meetings, managing to-dos |
| Metrics | Reuse the benchmark's own | Design them; automatic checks or light human checks |
| Scope for one unit | Same | Prompt design and simple data generation |
| Scope for more units | Same | Also evaluation rubrics and multi-round setups |
| Distinctive demand | A quality analysis of the original benchmark | Realistic tasks that need reasoning; multi-agent tasks encouraged |

**Type 1 has three steps** ([74:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=4440)):

1. **Integration.** Convert the problem format to A2A, implement dataset loaders and interfaces, and add quality checks for correctness and reproducibility.
2. **Benchmark quality analysis.** Sample tasks and check correctness, clarity and difficulty by hand. Confirm that the metrics and judges match real task success. Write down biases and limitations.
3. **Correction and expansion.** Fix errors you found, and extend the benchmark where its coverage is thin.

The lecture's proof that step 2 matters is SWE-bench Verified, described in [the first chapter](01-evaluation-is-the-product.md): most of the original tasks were filtered out on review, and the cleaned set gave a different picture of model ability.

**Type 2** asks for useful, realistic daily tasks that showcase reasoning. Students were encouraged to build multi-agent benchmarks, for instance one agent that proposes solutions and another that analyzes them ([84:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5040)).

## How submissions are scored

The project rubric has two variants. Several criteria are shared.

| Criterion | New benchmark | Existing benchmark |
|---|---|---|
| Goal and novelty | Important, novel, covers new capability space | |
| Analysis | | Find the original benchmark's quality issues |
| Faithfulness | | Reproduce the original results, apart from the flaws fixed |
| Correction and expansion | | Fix flaws and extend coverage |
| Scope and scale | Large and diverse enough for reliable results | |
| Evaluator quality | Metrics clear, judge consistent | Same |
| Validation | Manual spot checks of the green agent's outputs | Same |
| Reliability | Scripts and green agent run robustly on AgentBeats | Same |
| Bias and contamination checks | Included | Included |
| Realism | Real-world workload, not a toy setting | |
| Impact | Reusable, well documented, clearly presented | Same |

The lecturer's summary of the difference: for a new benchmark the staff care about goal and novelty. For an existing one they care about faithfulness, meaning that the implementation reproduces the original results apart from the flaws you fixed ([92:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5520)).

The course page gives the weights for the course grade, as published for Fall 2025:

| | 1 unit | 2 units | 3 or 4 units |
|---|---|---|---|
| Participation | 40% | 30% | 20% |
| Quizzes | 20% | 10% | 10% |
| Article | 40% | | |
| Project, Phase 1 (green agent) | | 45% | 50% |
| Project, Phase 2 (white agent) | | 15% | 20% |

Phase 1 splits into a proposal (5%), an early demo with a milestone report (10%), and the final green agent submission (30% for two units, 35% for more). Phase 2 splits into the white agent implementation (10% or 15%) and a report of one to two pages (5%). Students taking one unit could replace the article with Phase 1, with minimal coding. Participation in the AgentX-AgentBeats competition earned a bonus.

The timeline ran as follows: proposal released September 27 and due October 8; demo and short report October 7 to October 20; final green agent submission, with documentation and a recording, November 7 to December 17; white agent submission, with its report, November 24 to December 17.

## What makes it hard

The lecture's last section walks through the course's own τ-bench integration. It shows where the difficulty sits.

**The interface has to serve two masters.** A human should be able to solve the task when it is presented the same way. The procedure should also be as agent-friendly as possible. The staff's examples: give a browsing agent a URL rather than raw actions; give a coding agent an environment rather than only a repository.

**Tools do not travel well across agents.** In the original benchmark, tools are handed straight to the model's completion interface. Over a standardized agent protocol, the lecture lists three options, none clean:

1. Build special white agents that have tool access.
2. Explain the tools to any white agent and ask it for tool names and arguments. This is less standardized and cannot use the agent's own tool-calling mechanism.
3. Provide an MCP server and require the agent to discover it at run time.

**The evaluator loses sight of the calls.** The tool trace is not directly visible to the green agent, so the scoring has to be migrated.

**The last stretch is packaging.** Once the kickoff script, the green agent and the white agent exist, the slide reads "90% DONE". The rest makes the work reproducible on the platform: obtain the remote agent URL or MCP server URL, access the model API, report results and add traces, and package the repository for hosting.

**The evaluator has to be tested too.** The lecture's four-step checklist for building a green agent ends with test cases for the green agent itself ([88:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5280)): white agents that succeed and fail in different ways, each with the verdict you expect, with as many edge cases as possible. For a ticket-booking agent: one agent books the ticket, one books a ticket that is too expensive, one never finds the booking site.

This chapter's reading of all that: the hard part is not the tasks. It is that the evaluator must be standardized, must be validated against known outcomes, and must define its own metrics, all at once.

## Pitfalls

1. **Building the agent first.** Fix: build the evaluator, then the agent.
2. **Reusing a benchmark without checking it.** Fix: the three Type 1 steps, including the quality analysis.
3. **No verdicts for the evaluator.** Fix: test cases with known outcomes, including edge cases.
4. **Metrics designed last.** The checklist puts them third of four. Fix: write them down right after the environment.
5. **Stopping at the demo.** Fix: packaging and traces before the deadline.
6. **A toy environment for a new benchmark.** Fix: realistic daily tasks.

## Try it

**Deliverable:** a miniature green agent, with three fake white agents.

1. Use the [harness](02-a-minimal-eval-harness.md) as your green agent, with ten tasks of your own.
2. Write three scripted white agents: one that succeeds, one that reaches the right outcome by a forbidden route, and one that fails.
3. Write the verdict you expect for each, then run them.

**You are done when** your evaluator returns the expected verdict for all three, including the forbidden-route case, and you have written one paragraph on a fourth white agent that you expect to fool it.

**Stretch goal:** wrap the evaluator behind a small HTTP service that accepts a white agent's answers, so that the white agent can live in another process.

## Key takeaways

- The green agent hosts the evaluation. It prepares the environment, hands out tasks, verifies, and reports metrics that it defines itself.
- The white agent is the participant under test. Students build it second.
- There are two project types: integrate an existing benchmark, with a quality analysis, or build a new one, with rubrics and realistic tasks.
- The rubric rewards the evaluator's quality, validation, reliability, and bias checks, in both types.
- The hard parts are standardizing tool access, migrating scoring, packaging, and testing the evaluator with known verdicts.

## Self-check

1. In the course project, what is the green agent?
   A. The agent being tested
   B. The hosting agent that defines tasks and reports the metrics
   C. The sponsor of the competition
   D. The user simulator
2. What does the platform send to the green agent to start an assessment?
   A. A task and the URLs of the participant agents
   B. The model weights
   C. The grading rubric
   D. A dataset of users
3. Which criterion is specific to teams that integrate an existing benchmark?
   A. Goal and novelty
   B. Faithfulness: reproducing the original results apart from fixed flaws
   C. Realism
   D. Scope and scale
4. In the τ-bench example, what makes it hard to move tools behind a standardized agent protocol?
   A. The tools become slower
   B. The original code hands tools straight to the model, and the tool trace is not visible to the green agent
   C. The benchmark has no tasks
   D. The user simulator has to be removed
5. What does the fourth step of the checklist ask for?
   A. Choose a task
   B. Design the environment
   C. Design the metrics
   D. Design test cases with known verdicts, to test the green agent itself
6. For students taking two units, how much of the course grade is the final green agent submission?
   A. 5%  B. 10%  C. 30%  D. 60%

<details><summary>Show answers</summary>

1. B. The white agent is the participant.
2. A. The platform first checks that all agents are online and reset.
3. B. Goal and novelty belong to the new-benchmark track.
4. B. The lecture lists three ways to expose tools across agents and names the lost tool trace as the second challenge.
5. D. The evaluator needs tests with known outcomes, including edge cases.
6. C. The project is 60% for two units: 45% for Phase 1 and 15% for Phase 2.

</details>

## Sources

- **Lecture:** Berkeley course staff, "LLM Agent Evaluations & Project Overview", UC Berkeley Agentic AI MOOC, Fall 2025: [video](https://www.youtube.com/watch?v=VfOA2a0dj4w), used at [green and white agents](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3840), [the two project types](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=4440), [the checklist](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5280), [the grading rubric](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5520).
- **Reading:** UC Berkeley, "CS294/194-196: Agentic AI, Fall 2025", course page: syllabus, grading and project timeline, as archived for this course.

<!-- VERIFY: Add the URL of the Fall 2025 course page to the source above. The archived copy used here contains no URL. -->

## Next

Evaluation never stands alone. Continue with [planning for operations](../07-ml-in-production/10-planning-for-operations.md) to see where monitoring and rollback sit in a production plan, or start the capstones in part 11, which build on this case study.
