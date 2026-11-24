# 01. Multimodal Agents: Web and Computer Use

**Level:** Practitioner · **Reading time:** 10 min · **Exercise:** 45 min
**Prerequisites:** [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) (the observe, decide, act loop)

> **In one sentence:** After this chapter you can explain why agents that click through real web pages and desktop apps still fail, name the benchmarks that measure them, and choose an observation format and a scoring method for a computer-use task of your own.

## Why this matters

A stakeholder asks for an agent that buys the cheapest color photo printer and ships it to "the address on the photo". Three things break at once. A text-only agent cannot see that the photo is upside down. An agent that reads the page's source code drowns in markup. An agent that sees only pixels cannot tell which small gray box is the Add to cart button. The failure is silent, too: it buys the wrong item, or quits after two clicks and says the task cannot be done.

Ruslan Salakhutdinov opens his lecture with almost exactly this task ([8:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=480)). The question this chapter answers: how is an agent measured on this kind of work, and what makes it better?

## The core idea

A **multimodal agent** is an agent that reads more than text. Here it reads screenshots as well as page source, and it acts by clicking and typing. A **vision-language model (VLM)** is a language model that also accepts images. **Grounding** is linking a phrase in the instruction ("the cheapest printer") to the thing on screen it refers to. **Execution-based evaluation** scores a run by checking the final state of the environment, not by comparing the agent's steps with one reference path.

The analogy is a unit test: a fixture sets up the state, the code under test acts, an assertion checks the result. The analogy breaks twice. A unit test is deterministic and takes milliseconds; a computer environment is slow, and one click changes everything after it. And the assertion must accept every valid route to the same end state, not only the route its author had in mind.

## How it works, step by step

### 1. Choose what the agent sees

| Observation | What it is | Strength | Weakness |
|---|---|---|---|
| HTML or DOM tree | The page source as text | Exact labels and attributes | Messy and long; layout is lost |
| Accessibility tree | The operating system's list of interface elements with roles and names | Short and structured | Differs per platform; misses purely visual content |
| Screenshot | Pixels | One format on every platform; keeps layout and images | Hard to map words to pixels; small text vanishes at low resolution |

Xiong also shows a hybrid, Set-of-Mark: a screenshot with numbered labels drawn on elements taken from the accessibility tree ([16:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=960)).

### 2. Give every task a resettable start state

In OSWorld, the computer-use benchmark Xiong presents, each task ships with two configuration files: one that creates a **virtual machine (VM)**, a simulated computer, and puts its apps into the starting state, and one that says how to score it. A ruined state costs one reset.

### 3. Let the agent act

The agent emits actions as short code strings that move the mouse and keyboard. The VM runs them and returns a new observation. The loop stops when the agent emits a termination action or hits a step limit.

### 4. Score by execution

An evaluation script inspects the VM: does the spreadsheet contain the new rows, is the file in the right folder? OSWorld has 134 scripts for its 369 tasks ([24:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=1440)).

### 5. Spend more compute after a failure

Salakhutdinov describes two test-time methods. Search by repeated sampling runs several complete attempts and keeps one that passes, which he likens to rejection sampling ([34:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=2040)). Tree search branches in the middle of a run and asks an LLM to judge how promising each intermediate state is ([38:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=2280)). Both need the check from step 4.

### Benchmarks to know

| Benchmark | Year | Environment | Scoring |
|---|---|---|---|
| WebArena | 2023 | Self-hosted clones of a shopping site, Reddit and GitLab | Execution-based; HTML observations |
| Mind2Web | 2023 | 2,350 tasks on 137 real websites | Offline: compared with one recorded human demonstration |
| VisualWebArena | 2024 | The same style, with tasks that need images | Execution-based; screenshots allowed |
| OSWorld | 2024 | 369 tasks on a real desktop operating system | Execution-based scripts on a VM |

<!-- VERIFY: task and website counts for Mind2Web, the years, and the arXiv links below come from my knowledge of the papers, not from the lectures. -->

## What the practitioners say

### Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes

- **The gap.** On WebArena, "the tasks are fairly easy for humans, about 78 success rate, but very difficult for language models", which reached about 14 percent at the time ([6:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=360)). He puts part of the blame on format: pages arrive as HTML, which is messy and can run to 100,000 tokens. A **token** is the small chunk of text, roughly three quarters of a word, that a language model reads or writes at a time. In the performance part of his lecture he puts the best models at around 20 percent accuracy, as of March 2025 ([24:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1440)).
- **The failures.** Agents loop between two pages, keep no memory of what they have done, finish a subtask and then undo it, give up early, click the wrong element, and read layout poorly, for example questions about the prices in the first row of a listing ([26:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1560), [28:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1680)).
- **The fixes.** He lists long-horizon planning, running parallel instances as search, asking a person when uncertain, stronger VLMs, and the right abstraction level: "Do you rely on screenshots, what you're seeing visually? Do you rely on HTML or maybe you rely on APIs?" ([28:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1680)).
- **Data.** His slides call this a data problem: Llama proposes tasks on live websites, automatic checks verify them, and the pipeline scaled to 150,000 live websites. He adds that human-only annotations "struggle with generalization" ([66:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=3960)).
- **Safety.** A page state altered on purpose can push an agent into a wrong action, and he retells two Anthropic anecdotes in which Claude stopped a long screen recording and left a demo to browse photos of Yellowstone ([76:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=4560)). His diagnosis: one wrong action is hard to undo without search.
- **His framing.** The benchmark tasks are low-stakes and were made simpler on purpose; the open question is whether economically valuable tasks can be automated ([26:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1560)).

### Caiming Xiong (March 2025): the environment, the data, a vision-only agent

- **Why a new benchmark.** In his account, each Mind2Web task has one demonstration and no executable environment, so the benchmark assumes a single solution ([6:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=360)).
- **What OSWorld showed.** Higher screenshot resolution improves results; a longer text history improves results, where screenshot-only history does not; raising the step limit from 15 to 50 helps ([38:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=2280)).
- **AgentTrek.** A **trajectory** is one full record of observations, actions and reasoning for a task, and none can be crawled for free. His team turns web tutorials into trajectories: collect tutorials; paraphrase each into a structured tutorial with prerequisites, step-by-step instructions and an expected outcome; let a VLM agent replay it; let a VLM evaluator score the recording and drop weak ones ([50:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=3000)).
- **AGUVIS.** Text representations differ per platform, action formats differ, and closed models grounded poorly; most agents emit an action with no reasoning ([72:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=4320)). AGUVIS uses screenshots only, one action format, and an **inner monologue**, a short piece of reasoning written before each action. Its first training stage uses one million grounding examples ([82:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=4920)), and his slide reports that the monologue helps on harder tasks. He closes: improve grounding, not only reasoning ([88:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=5280)).

<!-- SOURCE GAP: the packets hold about a fifth of each transcript. Salakhutdinov's tree-search results and Xiong's OSWorld scores for Anthropic's and OpenAI's agents are on slides without text, so no numbers are given here. -->

## Pitfalls

1. **Scoring by matching steps against one recording.** Fix: check the end state; see [a minimal eval harness](../03-evaluation/02-a-minimal-eval-harness.md).
2. **Feeding raw HTML.** Fix: pick one observation format on purpose and measure the others against it.
3. **Small screenshots.** Fix: raise the resolution and measure the token cost.
4. **Going vision-only and dropping the text history.** Fix: keep a compact text log of past actions.
5. **A step limit set too low.** Fix: raise it, but add loop detection, because more steps also mean longer loops.
6. **Reading a benchmark score as product readiness.** Fix: build the same fixture, action and assertion around your own environment.
7. **Letting the agent act on a real account.** Fix: run in a sandbox and confirm irreversible actions; see [prompt injection](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md).

## Try it

Build a five-task harness for one web app you control.

- **Deliverable:** for each task, a setup script, a one-line instruction and a check function that inspects the final state. Run your agent three times per task.
- **Acceptance criteria:** you are done when every check passes on a hand-completed run and fails on an empty run, the report states success rate per task, and each failure is labeled loop, gave up early, wrong element or undone work. This is [slicing](../08-quality-assurance/03-slicing.md) by failure type.
- **Stretch:** rerun with two observation formats and two step limits, and report what changed.

## Key takeaways

- Execution-based evaluation checks the end state, which frees the agent to take any valid route.
- As of March 2025, Salakhutdinov reported the best web agents near 20 percent accuracy on VisualWebArena-style tasks, against 78 percent for humans on WebArena.
- The main failures are long-horizon: loops, no memory, undoing work, giving up.
- Grounding, the observation format and the step limit each move the score; so does reasoning before acting.
- Search at test time needs an automatic check to search against.

## What this means for someone building agents

1. Write the check before the agent. An end-state check turns a vague demo into a number, and it is the same check that powers retries and search; see [planning, search and decision making](../02-building-agents/03-planning-search-and-decision-making.md).
2. Treat the observation format as a design decision with a cost: HTML is exact but long, screenshots are universal but hard to ground.
3. Keep a text log of past actions even when the agent is vision-based.
4. Retries only pay when failures are independent; detect loops first, then resample.

## Self-check

1. An agent reaches the goal by a route nobody recorded. Which scoring method passes it?
   A. Step overlap with the reference demonstration
   B. Execution-based check of the final state
   C. Similarity to the reference reasoning text
   D. Trajectory length within reference bounds
2. In Xiong's OSWorld analyses, which change did not help?
   A. Higher screenshot resolution
   B. Longer text-based action history
   C. More screenshots instead of the text history
   D. Step limit raised from 15 to 50
3. What is the difference between search by repeated sampling and tree search?
4. Why does AGUVIS train an inner monologue before each action?
5. Name three long-horizon failure modes Salakhutdinov reports.

<details><summary>Show answers</summary>

1. B. Execution-based evaluation looks only at the end state.
2. C. A longer text history helped; a screenshot-only history did not.
3. Repeated sampling runs whole attempts and keeps one that passes. Tree search branches inside a run and uses an LLM judge to rate intermediate states.
4. To carry the reasoning a language model already learned from text into action generation; Xiong's slide reports it helps most on harder tasks.
5. Any three of: looping between pages, no memory of progress, undoing completed work, giving up early, clicking the wrong element, weak spatial reasoning.

</details>

## Sources

- **Lecture:** Ruslan Salakhutdinov, "Multimodal Autonomous AI Agents", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (March 10, 2025): [video](https://www.youtube.com/watch?v=RPINOYM12RU), used at [WebArena](https://www.youtube.com/watch?v=RPINOYM12RU&t=360), [failure modes](https://www.youtube.com/watch?v=RPINOYM12RU&t=1560), [what is missing](https://www.youtube.com/watch?v=RPINOYM12RU&t=1680), [data](https://www.youtube.com/watch?v=RPINOYM12RU&t=3960)
- **Lecture:** Caiming Xiong, "Multimodal Agents: From Perception to Action", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (March 17, 2025): [video](https://www.youtube.com/watch?v=n__Tim8K2IY), used at [benchmark gap](https://www.youtube.com/watch?v=n__Tim8K2IY&t=360), [OSWorld loop](https://www.youtube.com/watch?v=n__Tim8K2IY&t=960), [AgentTrek](https://www.youtube.com/watch?v=n__Tim8K2IY&t=3000), [AGUVIS](https://www.youtube.com/watch?v=n__Tim8K2IY&t=4440)
- **Reading:** Zhou et al., "WebArena: A Realistic Web Environment for Building Autonomous Agents" (2023): [arXiv](https://arxiv.org/abs/2307.13854)
- **Reading:** Deng et al., "Mind2Web: Towards a Generalist Agent for the Web" (2023): [arXiv](https://arxiv.org/abs/2306.06070)
- **Reading:** Koh et al., "VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks" (2024): [arXiv](https://arxiv.org/abs/2401.13649)
- **Reading:** Xie et al., "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments" (2024): [arXiv](https://arxiv.org/abs/2404.07972)
- **Reading:** "AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials" (2024): [arXiv](https://arxiv.org/abs/2412.09605)
- **Reading:** "AGUVIS: Unified Pure Vision Agents for Autonomous GUI Interaction" (2024): [arXiv](https://arxiv.org/abs/2412.04454)

## Next

→ [02. Embodied Agents and Robotics](02-embodied-agents-and-robotics.md), where the environment stops being a virtual machine and starts pushing back physically.
