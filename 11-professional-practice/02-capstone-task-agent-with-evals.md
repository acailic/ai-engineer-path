# 02. Capstone 1: A Task Agent with Evals

**Level:** Practitioner · **Reading time:** 25 min · **Exercise:** 35 h
**Prerequisites:** [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md), [Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md), [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md). Read [Statistics for Evals](../03-evaluation/05-statistics-for-evals.md) before milestone 4.

> **In one sentence:** After this project you have a task agent that completes small office tasks in a simulated workspace, and an evaluator that states how often it succeeds, how reliably, at what cost, and where it fails.

## Why this matters

An agent is easy to demo and hard to trust. You can show it booking a meeting. You cannot say how often it books the wrong one, until you build the thing that checks. Berkeley's Agentic AI course makes that the first rule of its project: students build the evaluating agent before the agent that is evaluated ([the case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)).

This capstone has you build both, at a size one person can finish. The workspace is fake. Nothing real can break, and every run starts from the same state.

## The goal

Build a **task agent**, an agent that carries out small office tasks such as scheduling a meeting or adding a to-do, in a simulated workspace. Then build the evaluator that grades it: an evaluation set of at least 30 tasks with expected outcomes, a harness that runs them, and a report. You finish with numbers that another engineer can reproduce with one command.

## Deliverables

1. **An environment.** A simulated workspace with a calendar, a to-do list, contacts and a read-only inbox. It can be reset and inspected.
2. **Six tools.** They are the only way the agent reaches the workspace.
3. **An agent loop.** A real model sits behind one interface, and a scripted model serves the offline tests.
4. **An evaluation set.** At least 30 tasks, each with a start state and an expected end state.
5. **An evaluator.** It resets the workspace, runs each task several times, checks the end state and the route, and prints a report by slice.
6. **A report and a README.** Both record the model, the prompt version, the date and every decision.

## The environment

[A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md) puts the system under test behind one method. [Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md) adds what an agent needs: an environment that responds, resets, and allows inspection. Use a plain Python dictionary loaded from a JSON file.

| Store | Fields | Who writes it |
|---|---|---|
| `calendar` | events: day, start, minutes, title, attendees | `create_event` |
| `todos` | items: id, title, due day, done | `add_todo`, `complete_todo` |
| `contacts` | names and email addresses | nobody |
| `inbox` | messages: from, subject, body | nobody |

Fix "today" in the fixture, for example December 1, 2026, so that "tomorrow" means the same day in every run. **Reset** means loading the fixture again. **Inspect** means comparing the final state with the expected one. The tools are the only way to reach the workspace: they are the environment written as code.

## The minimal agent

Start from [`examples/minimal_agent.py`](../examples/minimal_agent.py). Keep four things as they are:

- The model behind one method, `step(messages, tools)`.
- `ScriptedModel`, the deterministic stand-in that replays fixed decisions. It lets you test the loop without an API key.
- The tool registry. A failing tool returns an `Error:` text to the model instead of raising.
- Two stop conditions, a final answer and a step limit. Keep both, and add the third that the anatomy chapter asks for, a time or token budget.

Add one class whose `step` makes a single chat API call and maps the provider's tool-call format to the loop's dictionary. No chapter shows a real call. Each provider publishes an SDK, its official client library, whose quick start shows three things: how the key reaches the code (an environment variable, such as `PROVIDER_API_KEY`); the request, a list of messages plus the tool schemas in JSON; and the response, whose tool calls hold a name and an argument string in JSON. Write the system prompt to state the rules: which tools exist, that a missing contact or a full day means "tell the user and change nothing", and when to stop.

An agent earns its place here for one reason: the number of steps varies with the task.

## The tools

| Tool | Arguments | Writes | Error it returns |
|---|---|---|---|
| `list_events(day)` | a day | no | a date in the wrong format |
| `find_free_slot(day, minutes)` | a day, a length | no | `No free slot of <minutes> minutes on <day>` |
| `create_event(title, day, start, minutes, attendees)` | a title, a day, a start, a length, names | yes | overlaps an existing event; a name not in contacts |
| `add_todo(title, due)` | a title, a day | yes | a date in the wrong format |
| `complete_todo(id)` | an item id | yes | no such item |
| `lookup_contact(name)` | a name | no | no such contact |

[Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md) gives the rules. One job per tool. A description written as a prompt. A schema for the arguments. An error message that says what to do next.

One decision follows from them. `create_event` refuses a name that is not in the contacts, instead of guessing an address. That removes a whole class of failures before any model runs.

Leave out any tool that deletes or moves events in the base project. It would give the agent a way to damage the calendar that no task in the set needs. It returns as a stretch goal.

## The evaluation set

Each task record has six fields: `id`, `goal` (the request), `expected` (the end state, and for a `cannot` task the phrase the final message must contain), `must_call` (required calls, in order), `forbid_call`, and `tag`. Eight examples:

| id | Request (`goal`) | Expected end state | `must_call` | `forbid_call` |
|---|---|---|---|---|
| `todo-1` | Add a to-do "Renew the domain", due December 5. | One new to-do. Nothing else changes. | `add_todo` | `create_event`, `complete_todo` |
| `event-1` | Book "Dentist" on December 2, from 15:00, for 45 minutes. | One new event at that time. No overlap. | `create_event` | `add_todo` |
| `slot-1` | Find a 30-minute slot on December 3 and book a design review with Dana Reyes. | A 30-minute event in a free slot, with Dana's address from the contacts. | `find_free_slot`, `lookup_contact`, `create_event` | `complete_todo` |
| `keep-1` | Book a one-hour "Budget sync" on December 2. Keep my standup where it is. | The standup is unchanged. The new event does not overlap it. | `create_event` | none |
| `two-1` | Add "Send the invoice" to my to-dos for December 4, and mark "Water the plants" as done. | One new to-do. "Water the plants" is done. | `add_todo`, `complete_todo` | `create_event` |
| `cannot-1` | Book a call with Ana Petrova on December 3. | No change. Ana Petrova is not in the contacts. The final message says so. | none | `create_event` |
| `cannot-2` | Book a two-hour "Offsite" on December 2. | No change. Less than two hours are free. The final message says so. | `find_free_slot` | `create_event` |
| `unclear-1` | Move my meeting to the afternoon. | No change. The agent asks which meeting, because no tool moves events. | none | `create_event`, `add_todo` |

Build five slices of at least six tasks each, 30 in total:

- **`single`**: one call, one change.
- **`multi`**: several calls that depend on each other. A slot must be found before it is booked.
- **`constraint`**: an existing item must survive the request unchanged.
- **`cannot`**: the request cannot be fulfilled. The right behavior is to change nothing and say why.
- **`unclear`**: the request is ambiguous. The right behavior is to ask.

Keep two rules. First, every task is checkable by comparing two states and searching the final message for that phrase, so no judge is needed. Second, the `cannot` and `unclear` slices are part of the set, not an afterthought. An agent that acts on a request it cannot fulfill is worse than one that asks.

Hold back two tasks per slice, 10 of the 30. Nobody opens them while developing. The other 20 form the development set.

## The metrics

The harness chapter defines the metrics, and they carry over unchanged:

| Metric | The question it answers |
|---|---|
| Outcome | Does the final state equal the expected state? Ignore item ids when you compare. |
| pass^3 | On what share of tasks do all three attempts succeed? This is reliability. |
| pass@3 | On what share does at least one of three attempts succeed? This is what retrying buys. |
| Process | What share of attempts have no missing, out-of-order, or forbidden call? |
| Cost | How many tokens and dollars does one attempt cost? |
| Latency and steps | What are the median and the 95th percentile of one attempt? |

Report every metric for every slice, with its standard error. With 30 tasks and a score near one half, the standard error is about 0.09. A difference of two tasks between two versions is noise on this set. Use the paired comparison from the statistics chapter, saved as [`examples/eval_stats.py`](../examples/eval_stats.py), before you call a change an improvement.

## Milestones

### Milestone 1: the environment and the tools (6 to 8 hours)

No model is involved yet. `ScriptedModel` drives the loop. A test is a function that asserts a condition. Part 08 writes them for `pytest`; a plain function that you call by hand also counts.

- [ ] A test drives one call that changes the workspace, resets it, and finds the fixture again.
- [ ] Each tool returns an error text, and raises nothing, when given bad arguments.
- [ ] A scripted model that repeats one call is stopped by the step limit.

### Milestone 2: the evaluator (8 to 10 hours)

Build it before the real agent. It does the green agent's job in the Berkeley project: it hosts the environment, hands out the tasks, and reports the metrics. In the course's terms it is a new, small benchmark with its own validation.

- [ ] The set holds 30 tasks or more, in five slices, each with the six fields.
- [ ] Three scripted agents return the verdicts you expect. One succeeds. One reaches the right end state but skips a required call, so the outcome passes and the process fails. One books the wrong day, so the outcome fails.
- [ ] The report prints every metric for every slice, with the standard error.

### Milestone 3: the real agent (6 to 8 hours)

- [ ] The offline tests pass with the network turned off.
- [ ] A full run with the real model finishes: 30 tasks, three attempts each.
- [ ] You read 20 failed traces and write down three causes.

### Milestone 4: harden and improve (6 to 9 hours)

- [ ] One change, to the prompt, a tool description, or an error message, is tested with a paired comparison on the development set. The decision is written down.
- [ ] A gate script exits with a non-zero code (`sys.exit(1)`) when a metric is worse than the baseline.
- [ ] Each slice has a one-line note on its main failure.

### Milestone 5: package (4 to 5 hours)

- [ ] One command runs the whole evaluation and writes the report.
- [ ] The README answers three questions. What is the environment? What are the stop conditions? Which errors go back to the model?
- [ ] The report names the model, the prompt version, the date, and the score on the held-out tasks, run once at the end.

## You are done when

1. The workspace resets to an identical state, and a test proves it.
2. The evaluator returns the expected verdicts for the three scripted agents.
3. A real model has run all 30 tasks three times, and the report shows every metric by slice.
4. One change was accepted or rejected on a paired comparison, with the decision written down.
5. The gate script catches a regression that you planted on purpose.
6. The held-out tasks were run once, at the end, and that score is in the report.

## Effort, tools and cost

Plan on 30 to 40 hours over two or three weeks. Milestones 1, 2 and 5 need only Python 3.10 or newer and its standard library. A test runner from your usual tooling is optional.

Milestone 3 needs a chat model that supports tool calling, through a provider's API. That costs money. The anatomy chapter estimates a 10-step run at a fraction of a cent to a few cents on small hosted models. One full evaluation is 90 attempts, and you will run it ten times or more. Expect a cost from a few cents to a few dollars per evaluation. These are estimates: check your provider's current prices.

If you cannot spend money, complete milestones 1, 2 and 5 with scripted models. You still build the evaluator, which is the larger lesson.

## Stretch goals

- Add a **user simulator** and a task that takes several turns ([Evaluating Agents](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md)).
- Grade the final message with an LLM judge, calibrated against your own labels ([LLM-as-a-Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md)).
- Rebuild the agent on a framework and hold a bake-off against your hand-written loop ([The Agent Framework Landscape](../05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md)).
- Add a `send_email` tool behind a policy gate, then continue with [Capstone 2](03-capstone-monitoring-agent-for-prompt-injection.md).
- Run the workspace in a sandbox and expose the tools over the Model Context Protocol ([Agent Infrastructure](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md)).
- Integrate an existing agent benchmark into the same evaluator, and check its quality by hand: the correctness, clarity and difficulty of sampled tasks ([the case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)).

## Pitfalls

1. **Building the agent first.** Fix: milestone 2 before milestone 3.
2. **Success you cannot check.** Fix: every task ends in a state comparison. If a task needs a judge, it belongs in a stretch goal.
3. **State that leaks between tasks.** A leftover event makes the next task pass or fail for the wrong reason. Fix: reset inside the harness, never by hand, and keep the reset test.
4. **A grader that is too strict.** Comparing item ids or list order fails correct runs. Fix: compare after normalization, and read the failed and the passed attempts.
5. **Telling the agent the answer.** If the prompt describes the expected state, the score measures your prompt, not the agent. Fix: the expected state is visible to the evaluator only.
6. **Only easy tasks.** Fix: the `cannot` and `unclear` slices stay in the set.
7. **One attempt per task.** Fix: three attempts, and pass^3 in the report.
8. **Judging by the final message.** "Done!" is text, not a result. Fix: the end state decides.
9. **Tuning on the held-out tasks.** Fix: develop on 20, run the other 10 once.

## What the practitioners say

- **Report reliability.** The Berkeley lecturers explain τ-bench's all-runs metric, and the harness keeps it as pass^k beside pass@k ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md)).
- **Test the evaluator.** The course's checklist for its evaluating agent ends with test cases of known verdicts: agents that succeed and fail in different ways ([the case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)). Milestone 2 is that step.
- **The environment comes first.** Neubig's list of problems in a coding agent starts with defining the environment ([The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md)).

## Try it

The project is the exercise. Start with one hour:

1. Write the fixture: a calendar with three events on December 2, two to-dos, and three contacts.
2. Write `add_todo` and `list_events`. Give each an error message.
3. Write the first task record, `todo-1`, by hand.

**You are done with the first hour when** `ScriptedModel` adds the to-do through the loop, and a reset brings the fixture back.

## Key takeaways

- Build the evaluator before the agent. The course that taught this chapter's sources does the same.
- An environment for evaluation must respond, reset, and allow inspection.
- Every task has an expected end state and a route, and both are graded.
- Run each task several times. Report pass^3 beside pass@3, and cost beside quality.
- Thirty tasks give a standard error of about 0.09. Small differences are noise until a paired comparison says otherwise.

## Self-check

1. Why is the evaluator built before the real agent?
2. A scripted agent reaches the right end state but skips a required call. What should the report show?
3. Why must the environment reset between tasks?
4. What does pass^3 add to the outcome score?
5. With 30 tasks and a score near one half, what can you say about a gain of two tasks?
6. Why are `cannot` tasks part of the evaluation set?

<details><summary>Show answers</summary>

1. Without it you cannot keep or reject a change on evidence, and the first tasks would be written to fit the agent you already built. The evaluator is also first tested with scripted agents of known verdicts, before any model call costs money.
2. Outcome pass and process fail. The two are graded separately because they fail independently.
3. A leftover change from one task makes the next task pass or fail for the wrong reason. A reset inside the harness makes every run start from the fixture.
4. Reliability. The outcome score is an average over attempts. pass^3 counts a task only when every attempt succeeds.
5. Nothing yet. The standard error is about 0.09, so two tasks is well inside the noise. Use a paired comparison and more attempts.
6. An agent that acts on a request it cannot fulfill is worse than one that asks. The set must measure that the agent stops, not only that it can go.

</details>

## Sources

- [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md), [Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md), [Memory and Knowledge for Agents](../02-building-agents/04-memory-and-knowledge-for-agents.md) (part 02)
- [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md), [LLM-as-a-Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md), [Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md), [Statistics for Evals](../03-evaluation/05-statistics-for-evals.md), [the green agent case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) (part 03)
- [The Agent Framework Landscape](../05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md), [Agent Infrastructure: Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) (part 05)
- [Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) (part 04, for the stretch goal)

## Next

→ [Capstone 2: A Monitoring Agent for Prompt Injection](03-capstone-monitoring-agent-for-prompt-injection.md), which adds a second program that watches this agent work.
