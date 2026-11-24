# 01. Evaluation Is the Product

**Level:** Practitioner · **Reading time:** 20 min · **Exercise:** 45 min
**Prerequisites:** [The anatomy of an agent](../02-building-agents/01-the-anatomy-of-an-agent.md), so that "tool" and "prompt" already have a concrete shape for you.

> **In one sentence:** After this chapter you can place any "does it work?" question at one of four levels of evaluation, and you can run a development loop in which every change is kept or rejected on evidence.

## Why this matters

You own a customer-support agent that refunds orders. A colleague rewrites its **prompt**, the instruction text that tells the model how to behave. You try the new version by hand on five conversations. Four look better than before. You ship it.

Nine days later a customer receives a refund on an order they never proved was theirs. Nobody touched the refund tool. The new prompt made the agent more helpful and less careful at the same time, and five conversations could not show it.

This chapter answers two questions. What exactly do you have to measure? And how do you measure it on every change, so that "it works" becomes a claim with evidence behind it?

## The core idea

**Evaluation** is systematic, repeatable measurement. In their Fall 2025 lecture, the Berkeley course staff describe it as a systematic and reproducible way to measure the performance of a model or an agent, useful for tracking progress and assessing risk, and needed at every step: while training, while validating, when selecting a model, and before deployment ([2:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=120)).

Three words first. A **tool** is a function the agent can call, such as `lookup_order`. An **environment** is everything the agent acts on and reads from: tools, databases, files, a browser. A **trajectory** is the ordered record of one attempt: every message, every tool call, every result.

Because an agent is software, evaluation is a software engineering activity. Christian Kästner lists four ingredients of an automated test: call the code under test, provide inputs, control the environment, and check whether the result matches expectations (chapter 14). An evaluation **harness**, the program that runs the evaluation, has the same ingredients, plus one that testing does not need.

| In testing | In an LLM evaluation | What it is |
|---|---|---|
| Code under test | The system | Prompt, model, tools and guardrails, treated as one unit |
| Test inputs (fixtures) | Dataset | A list of tasks with the behavior you accept |
| Environment setup | Sandbox | Tools over fake data, reset before each attempt |
| Assertion | Grader | Code, or a judge, that scores one attempt |
| Test report | Metrics and report | Numbers that summarize all attempts |
| No counterpart | A grader you must test | The scorer itself can be wrong, so it needs its own checks |

**Where the analogy breaks.** Three differences change how you work.

1. **There is no specification.** A unit test encodes a rule someone wrote down. For an LLM system nobody wrote the rules down. You have goals and examples, so you measure how well the system fits the job, not whether it is correct.
2. **Output is not deterministic.** The model picks each next piece of text partly at random, so the same input can give a different answer. A run that passed once may fail on the next run.
3. **Results are rates.** A unit test passes or fails. An evaluation returns "43 of 60 tasks". One wrong answer is not a bug to fix. It is a rate to push down.

The title is a claim: features decide what your system *can* do, and the evaluation decides what *good* means. If your evaluation checks only whether the final answer sounds helpful, you will build an agent that sounds helpful.

## Four levels of evaluation

Each level answers a different question, costs a different amount, and catches a different failure.

| Level | Question it answers | Example: refund agent | Typical grader | Cost per attempt |
|---|---|---|---|---|
| Component | Does one piece do its job alone? | Does the first prompt turn "my order 1042 is broken, give me my money back" into `{"intent": "refund", "order_id": "1042"}`? | Exact match against known answers | Lowest: one model call |
| Trajectory | Did the agent take an allowed route? | Did it call `authenticate` before `refund`? Did it stay under ten steps? | Rules over the recorded tool calls, or a judge reading the trace | Medium |
| Outcome | Did it reach the right end state? | Is order 1042 refunded exactly once? | A program that compares the final database state with the goal | Medium to high |
| Online | Does it work for real users, now? | What share of refunds lead to a complaint within a week? | Production logs, user feedback, sampled human review | Highest, and only after release |

The sources slice the same idea three ways:

- Kästner sorts tests by granularity: unit tests for one unit, integration tests for units that work together, system tests for the whole system end to end, and acceptance tests from the user's point of view (chapter 14).
- A 2025 survey by Asaf Yehudai and colleagues notes that each agent ability, such as planning or tool use, "can be evaluated in isolation or as part of a full agent workflow" ([survey](https://arxiv.org/abs/2503.16416)). The Berkeley lecture builds a taxonomy from that survey: a specific capability, a specific application, or a general set of applications ([28:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1680)).
- The lecture also sorts tasks by how you score them. Close-ended tasks have few possible answers and can be graded automatically. Open-ended tasks split into verifiable ones, which have an **oracle** (a cheap, trusted procedure that says whether a result is correct, such as running a program), and non-verifiable ones, such as storytelling, which need a human or a judge.

**Why use several levels.** Cheap levels tell you *where* it broke. Expensive levels tell you *whether it matters*. Neither implies the other. A system can pass every component check and fail the user's goal. It can also reach the right outcome by a forbidden route.

The working rule: when something fails, find the lowest level at which the failure appears, and fix it there.

## The eval-driven development loop

Test-driven development asks you to write the test before the code, then keep the code that passes. The loop here has the same shape. It breaks in one place: a unit test verifies, while an evaluation estimates. With 30 tasks the loop only shows large failures (see [the statistics chapter](05-statistics-for-evals.md)).

1. **Define success for one user goal.** Write the outcome and the route: "the order is refunded once, after authentication, for the listed amount".
2. **Collect 20 to 50 real tasks.** Take them from support tickets, chat logs, or your own handwritten variants. Write down the result you expect for each.
3. **Build the smallest harness** that runs all tasks and prints one number. The [next chapter](02-a-minimal-eval-harness.md) is one you can copy.
4. **Read every failure** and sort the failures into classes: "skips authentication", "wrong order id", "gives up".
5. **Fix the largest class.** Change one thing.
6. **Re-run.** Keep the change only if the target metric rises by more than the noise and no other metric falls.
7. **Automate.** Run the harness on every change and add every failure you meet in production to the dataset ([evals in production](07-evals-in-production.md)).

## Worked example

One attempt of the refund agent, with its checks at three levels.

```json
{
  "task": "refund-1042",
  "user": "Please refund order #1042.",
  "component":  {"intent": "refund", "order_id": "1042", "passed": true},
  "trajectory": {"calls": ["lookup_order", "refund"], "passed": false,
                 "why": "refund was called before authenticate"},
  "outcome":    {"order_1042": "refunded", "passed": true}
}
```

What to observe: the same attempt passes two checks and fails one. An outcome-only evaluation calls it a success. So does a component-only one. Only the trajectory level sees the missing step. This is the pattern behind most "it worked in the demo" stories: helpful and careless move together.

## What the practitioners say

**Evaluation grows harder with agents.** The lecture's slides (around [6:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=360)) contrast static text-to-text models with agents that add planning, tool use, memory and multi-step reasoning in dynamic environments. Close-ended tasks are easy to grade but limited to simpler problems, with metrics such as accuracy, precision (of the answers the system flagged as hits, the share that really were) and recall (of the real hits, the share the system found).

**Two kinds of validity.** Drawing on a paper about building rigorous agent benchmarks (arXiv 2507.02825), the lecturers separate two questions ([28:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1680)):

- **Task validity:** does success at the task demonstrate the capability you meant to measure? This is about the task and the environment.
- **Outcome validity:** does the evaluator's verdict faithfully reflect whether the task succeeded? This is about the grader.

**Four ways an evaluation goes wrong.** The lecture lists these failures with a fix for each (slides around [28:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1680)):

| Problem | What it looks like | Fix named in the lecture |
|---|---|---|
| Noisy or biased data | Expected answers are wrong or unrepresentative | Make the test data accurate and diverse enough |
| Not practical | Tasks nobody has, or a setup real users could not use | Think about the practitioner's real needs |
| Not challenging | Every model scores near the top | Design hard cases |
| Shortcuts | A model can score well without solving the task | Look for the shortcuts your evaluation probably has |

**The benchmark can be the bug.** SWE-bench asks agents to fix real issues in open-source repositories. As reported on the lecture's slides ([78:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=4680)), 93 professional developers then checked 1,699 of its tasks. They flagged 38.3% for underspecified issue descriptions and 61.1% for unfair unit tests (the two groups overlap). In total 68.3% of tasks were filtered out, leaving 500 verified ones. On the cleaned set, GPT-4o resolved 33.2% of tasks, against 16% on the original with the best scaffold. The first score measured the benchmark's defects as much as the model's ability.

**Kästner on making it stick.** Quality practices help only if people use them. He describes how continuous integration, a service that runs all tests on every change in a clean environment, can refuse to merge a change that breaks a test (chapter 14). He also notes that testing in production, such as trying a change on a subset of users with a way to roll back, complements offline testing instead of replacing it. Part 8 of this course covers both in depth: [quality assurance basics](../08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md).

## Pitfalls

1. **Judging by vibes.** Five manual tries feel like evidence and are not. Fix: 20 real tasks, one number, printed on every change.
2. **Only end-to-end numbers.** You see 78% but cannot tell which piece broke. Fix: at least one component check for every piece you can swap out.
3. **Only component checks.** The parts pass and the user's goal still fails. Fix: one outcome check per user goal.
4. **A toy dataset.** The lecture's "not practical" failure. Fix: take tasks from real logs, and include requests the system must refuse.
5. **Trusting the benchmark.** As SWE-bench showed, expected answers can be wrong. Fix: read 20 tasks and their expected answers yourself before you believe a score.
6. **Changing two things at once.** You learn nothing about which change did what. Fix: one change per run.
7. **No baseline.** A lone number cannot be interpreted. Fix: always print the previous version's result on the same tasks next to the new one.

## Try it

Pick one user goal of a system you can run: your own agent, or a script that calls a chat model.

**Deliverable:** a file `levels.md` containing:

1. one sentence that defines success for the goal, with the outcome and the route;
2. the four-level table from this chapter, with one check per level for your goal;
3. a list of 20 real tasks, each with the result you expect.

**You are done when** every check names the evidence it looks at (a field, a call order, a database value, a logged event), and when at least two of the 20 tasks are requests the system must refuse.

**Stretch goal:** put the same 20 tasks into the [harness](02-a-minimal-eval-harness.md) and report the numbers for two versions of the system.

## Key takeaways

- Evaluation is systematic, repeatable measurement. For an agent it is test infrastructure: dataset, sandbox, grader, report.
- Four levels: component, trajectory, outcome, online. Find the lowest level at which a failure appears.
- The testing analogy breaks in three places: no specification, non-deterministic output, results that are rates.
- Keep or reject a change by comparing it with the previous version on the same tasks, and only when the gap is larger than the noise.
- The benchmark can be the bug. Check tasks and expected answers before you trust a score.
- Run the evaluation automatically on every change.

## Self-check

1. An agent refunds the right order but never calls `authenticate`. Which level catches it?
   A. Component  B. Trajectory  C. Outcome  D. Online
2. What does *outcome validity* ask?
   A. Whether the dataset is large enough to rank models
   B. Whether the evaluator's verdict reflects real task success
   C. Whether the task demonstrates the capability you meant to test
   D. Whether a second run reproduces the first
3. In Kästner's four ingredients of an automated test, which one covers resetting a fake database before each attempt?
   A. Calling the code under test  B. Providing inputs  C. Controlling the environment  D. Checking the result
4. Your change lifts exact match from 58% to 60% on 60 tasks. What is the right next step?
   A. Merge, because 60 is larger than 58
   B. Merge, then watch production
   C. Check whether the gap is larger than the noise, then decide
   D. Lower the temperature and run again
5. According to the lecture, why did SWE-bench Verified replace the original set in most reports?
   A. The original set was too small to run
   B. Many tasks were underspecified or had unfair tests, so scores understated ability
   C. The original set relied on human judges
   D. Its tasks had leaked into training data
6. Why is one passing run weak evidence for an LLM system?
   A. The harness may be too slow to repeat
   B. The output is chosen partly at random, so the same input can fail next time
   C. Exact match ignores letter case
   D. Token prices change

<details><summary>Show answers</summary>

1. B. The end state is right, so the outcome level passes. Only the recorded calls show the missing step.
2. B. Option C describes task validity.
3. C. Resetting state is environment control.
4. C. Two points on 60 tasks is well inside the noise. Chapter 05 shows the arithmetic.
5. B. Reviewers filtered out 68.3% of the original tasks; the cleaned set gave higher, more trustworthy scores.
6. B. Non-determinism means each attempt is a sample, which is why the harness runs each task several times.

</details>

## Sources

- **Lecture:** Berkeley course staff, "LLM Agent Evaluations & Project Overview", UC Berkeley Agentic AI MOOC, Fall 2025: [video](https://www.youtube.com/watch?v=VfOA2a0dj4w), used at [why evaluation matters](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=120), [task and outcome validity](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1680), [the SWE-bench Verified example](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=4680).
- **Reading:** Asaf Yehudai et al., "A Survey on Evaluation of LLM-based Agents" (arXiv, revised April 2026): [link](https://arxiv.org/abs/2503.16416).
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 14: [link](https://mlip-cmu.github.io/book/14-quality-assurance-basics.html).

## Next

→ [A Minimal Evaluation Harness](02-a-minimal-eval-harness.md), which turns the four levels into a runnable program.
