# 07. Evals in Production

**Level:** Practitioner · **Reading time:** 20 min · **Exercise:** 75 min
**Prerequisites:** [A Minimal Evaluation Harness](02-a-minimal-eval-harness.md), [Statistics for Evals](05-statistics-for-evals.md)

> **In one sentence:** After this chapter you can record a trace of every attempt, choose online metrics that mean something, gate each change on a regression run, and turn production failures into new evaluation tasks.

## Why this matters

The agent passed the offline evaluation and shipped. Two weeks later the escalation rate climbs. Offline you tested 60 tasks that you wrote yourself. Production sends thousands that you did not write, and their mix changes every week.

The question: how does evaluation continue after release?

## The core idea

Three activities feed each other:

1. **Observe.** Record what happened, attempt by attempt.
2. **Measure.** Turn those records into a few numbers you trust.
3. **Return.** Turn production failures into tasks, run them as a regression check on every change, and ship the next version.

The loop is often called a **data flywheel**: each release produces evidence that makes the next evaluation more like the real world.

Clay Bavor of Sierra describes what changed. Before agents, he says, most calls to a call center were never transcribed, so nobody could analyze them or run a controlled experiment on them. With agents every conversation is digital, and the methods of twenty years of website testing apply to conversations ([14:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=840)).

A **trace** is the recorded trajectory of one attempt in production. **Observability** is being able to ask questions of all your traces.

**The analogy, and where it breaks.** Tracing is logging, as you know it from servers and request IDs. It breaks on one point. An agent's trace is also its explanation. The answer alone does not tell you why the agent refunded the wrong order. The tool calls do.

## How it works, step by step

### 1. Log a trace for every attempt

| Field | Why it is there |
|---|---|
| `request` | To reproduce the attempt |
| `calls`, with arguments and results | To see the route, not only the destination |
| `answer` | What the user actually saw |
| `model`, `prompt_version` | To know which system produced it |
| `tokens_in`, `tokens_out`, `latency_ms` | Cost and speed |
| `outcome` | The label you evaluate on later |

Requests contain personal data. Bavor's list of what sits below the surface of an agent product includes detecting and encrypting personal information, and keeping traces for audit. Decide what you store before the first request arrives. Part 4 covers the security side: [defenses and guardrails](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md).

### 2. Choose online metrics that mean something

| Metric | What it catches | What to watch for |
|---|---|---|
| Outcome from the system of record (refund issued, ticket reopened) | Real results | Exists only for actions that change state |
| Escalation or handoff to a person | Tasks the agent could not finish | Depends on your handoff policy |
| Repeat contact: the same customer returns about the same issue | Wrong answers that looked fine | Depends on recognizing the customer |
| Explicit feedback: ratings | Strong dissatisfaction and strong delight | Sparse, and skewed to strong feelings |
| Guardrail triggers | Attempts that broke a rule | Counts rule hits, not real harm |
| Latency and cost per resolved attempt | Slow or expensive answers | Meaningless without quality |

Always split these by intent, the kind of request. An average over all requests hides the one intent that broke. Part 8 covers the technique: [slicing](../08-quality-assurance/03-slicing.md).

**Use metrics that fit your job, not the ones that exist.** Bavor's example is speech recognition in a voice agent. Word error rate, the share of words transcribed wrongly, "is terrible" as a measure of transcription quality, because it rewards transcribing the television in the background. His advice: "don't assume that whatever metrics are out there to measure a component of what you're doing is necessarily the right set of yardsticks" ([24:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=1440)). Decide what a great experience is, then measure that.

### 3. Use user feedback with care

Explicit feedback, such as a rating, is rare and biased toward strong reactions. Implicit signals, such as a customer rephrasing the same request three times, are plentiful and ambiguous. Use both to *find* conversations to read. Use people to *label* them. Sample the reading across intents and outcomes instead of reading the most recent ones.

### 4. Gate every change on a regression run

Kästner describes continuous integration: a service that runs all tests whenever code is submitted, in a clean environment, and that can refuse to merge a change which breaks a test (chapter 14). People forget to run tests; the service does not.

For an LLM system the same works with three adjustments:

- **Compare, do not just score.** Run the main branch and the change on the same tasks and use a [paired comparison](05-statistics-for-evals.md).
- **Use tolerance.** A metric that moves by less than the noise is not a regression.
- **Pin the conditions.** Fix the model version, the temperature, and the seeds. A model name that silently points to a new version breaks the comparison.

A small set of tasks runs on every change. The full set runs nightly.

### 5. Run the flywheel

1. Each week, pull the attempts that escalated, were re-asked, or tripped a guardrail.
2. Have a person confirm each one's failure class. A model can suggest the label.
3. Add each one to the dataset as a task record with the expected outcome and a tag.
4. Fix the largest class and re-run.
5. Keep a fresh sample of production tasks that you do not tune on. Check it monthly, so that a rising score on the regression set still means something.

### 6. Test in production, carefully

Kästner writes that testing in production complements offline testing. You observe the real system to see whether its behavior changed. You can inject a fault on purpose, known as chaos testing. You can show two versions to different users, which is an **A/B test**. And you limit it to a subset of users, with a way to roll back quickly (chapter 14).

For an agent, a useful injected fault is a tool that returns an error. The question is whether the agent recovers or invents an answer.

## Worked example

**A trace.** One line of a `.jsonl` file, in which each line is one JSON object:

```json
{"trace_id": "t-8f21", "time": "2026-11-24T09:14:02Z",
 "model": "model-x", "prompt_version": "refund-v7",
 "request": "Please refund order #1042.",
 "calls": [["authenticate", {"ok": true}],
           ["lookup_order", {"order": "1042", "amount": 42.5}],
           ["refund", {"ok": true}]],
 "answer": "I refunded $42.50 to your card.",
 "tokens_in": 310, "tokens_out": 131, "latency_ms": 1840,
 "outcome": {"escalated": false, "rating": null, "repeat_contact_48h": false}}
```

**One online metric.** The repeat-contact rate is computed from the `outcome` field:

```python
import json

def repeat_contact_rate(path):
    """Share of non-escalated conversations whose customer returned within 48 hours."""
    with open(path) as f:
        traces = [json.loads(line) for line in f]
    handled = [t for t in traces if not t["outcome"]["escalated"]]
    return sum(t["outcome"]["repeat_contact_48h"] for t in handled) / len(handled)
```

**The gate.** It reuses the [harness](02-a-minimal-eval-harness.md). Keep the file next to `eval_harness.py`.

```python
# ci_gate.py: keep it in the same folder as eval_harness.py
import sys

from eval_harness import DATASET, PROFILES, StubModel, regressions, run, summarize


def metrics(system):
    return summarize(run(system, DATASET))


# In real use, `baseline` is a metrics file saved from the main branch and
# `candidate` is the system that the pull request builds.
baseline = metrics(StubModel("baseline", PROFILES["baseline"]))
candidate = metrics(StubModel("tuned", PROFILES["tuned"]))

bad = regressions(baseline, candidate)
print("regressions:", bad or "none")
sys.exit(1 if bad else 0)  # exit code 1 fails the build
```

```text
regressions: ['cost']
```

What to observe:

- The gate prints the one metric that got worse and exits with code 1. The three quality metrics improved. A person now decides whether the higher cost is acceptable.
- The trace records the route (`authenticate` before `refund`), the versions, and the outcome in one object. The [trajectory checks](04-evaluating-agents-trajectories-and-environments.md) and the online metric read the same record.
- `repeat_contact_rate` counts only conversations the agent handled. An escalated call says nothing about whether the agent's answer would have held.

## What the practitioners say

**Most of an agent product is not the model.** Bavor shows a slide he calls the agent iceberg. Above the water sit the model, retrieval and tool use. Below it sit several dozen production concerns, among them observability and monitoring, changelogs, regression testing, user simulation, an experimentation framework, staged releases, and sampling for quality review ([8:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=480)).

**Agents need a different development cycle.** An agent is not deterministic: for a given input you cannot know the output in advance. So the lifecycle becomes build, test and optimize, continuously ([12:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=720)).

**Simulate before and after launch.** Sierra's simulations, described in the [previous chapter on environments](04-evaluating-agents-trajectories-and-environments.md), are a hardened form of the τ-bench setup: synthetic databases and tools, and mock user personas that include an emotional state ([36:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2160)). Sierra's Voice Sims blog post says the simulations are generated as new conversation flows are added and run inside the delivery pipeline, gating releases. His slides add that testing in production needs much more than a benchmark: continuous, integrated systems that evolve with the agent.

**Use AI to check AI, then add deterministic rules.** Bavor's belief is that "the solution to most problems with AI is more AI" ([40:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2400)). He describes a supervisor agent that watches whether the main agent stays on task and grounds its answers in the knowledge base. He also describes asking open questions of the transcripts, such as what drives low customer satisfaction or why calls escalate. He says the agents handle between 60% and 90% of incoming inquiries and hand the rest to people. These are his figures about his company's deployments. For attacks, he layers deterministic input checks, supervising models, internal rules, and output checks that end a session when the agent starts revealing its prompt ([44:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2640)). Systems of record are reached only through ordinary deterministic software with access controls.

**Kästner's caution.** Quality practices help only if they are used. Enforcement by tooling works better than good intentions (chapter 14). Part 8 covers production experiments in depth: [testing and experimenting in production](../08-quality-assurance/09-testing-and-experimenting-in-production.md).

<!-- SOURCE GAP: The brief lists chapter 19 of the CMU book (Testing and Experimenting in Production) as a source for this chapter, but that chapter was not in the reading packets. The book content here comes from chapter 14, from its sections on continuous integration and testing in production. -->

## Pitfalls

1. **Logging only the final answer.** You cannot see the route. Fix: log every tool call with its result.
2. **No versions in the trace.** You cannot tell which system produced a failure. Fix: model and prompt version on every record.
3. **Raw ratings treated as truth.** Fix: sample and read, across intents and outcomes.
4. **One average over all requests.** Fix: slice by intent.
5. **A flaky gate.** An unseeded model, or a model name that changes underneath you. Fix: pin versions and seeds, add tolerance.
6. **The regression set becomes the whole truth.** Scores rise on it and fall in production. Fix: a fresh held-out sample each month.
7. **No way back.** Fix: a tested rollback before any production experiment.
8. **Production examples added without labels.** A wrong expected answer poisons the set. Fix: a person confirms each one.

## Try it

**Deliverable:** tracing plus a gate, for one agent or for a script that calls a chat model.

1. Write one JSON trace per attempt to a `.jsonl` file, with the fields from this chapter.
2. Define three online metrics for it. Write down which trace field each one uses.
3. Add the gate script, and make it run on every change to the prompt.

**You are done when** one command over your trace file lists the last ten attempts that escalated, and a deliberately broken change makes the gate exit with code 1.

**Stretch goal:** each night, score a random 5% of production attempts with your offline graders, and compare the result with your offline dataset.

## Key takeaways

- Evaluation does not end at release. Observe with traces, measure with online metrics, and return failures to the dataset.
- A trace is a trajectory: request, tool calls, answer, versions, cost, outcome.
- Use metrics that fit your job. Off-the-shelf component metrics can reward the wrong thing.
- Gate every change on a paired comparison against the main branch, with pinned conditions and a tolerance for noise.
- Keep a fresh sample of real tasks, so that the regression set does not become the whole truth.
- Test in production on a subset of users, with rollback.

## Self-check

1. What must a trace contain so that a failure can be reproduced and diagnosed?
   A. Only the final answer
   B. The request, each tool call and result, and the model and prompt versions
   C. The customer's name and address
   D. The model's training data
2. Why does Bavor reject word error rate as a measure for a voice agent's transcription?
   A. It is too cheap to compute
   B. It rewards transcribing background sound that the agent should ignore
   C. It needs human labels
   D. It is too slow
3. What does the data flywheel add to the evaluation dataset?
   A. Synthetic tasks from a generator
   B. Failures seen in production, confirmed by a person, with an expected outcome
   C. Benchmark scores from other companies
   D. More model versions
4. A change raises exact match and doubles the cost. What should the gate do?
   A. Pass, because quality rose
   B. Report the cost regression so that a person decides
   C. Block the change with no way to override it
   D. Change the price
5. What is the role of a subset of users in testing in production?
   A. To speed up the rollout
   B. To measure a change's effect while limiting the damage it can do
   C. To collect more ratings
   D. To train the model
6. Why keep a fresh sample of production tasks every month?
   A. To grow the regression set faster
   B. To check that scores on the regression set still predict performance on unseen tasks
   C. To lower the cost of evaluation
   D. To calibrate a judge

<details><summary>Show answers</summary>

1. B. Without the route and the versions, a failure cannot be reproduced.
2. B. The metric measures every word in the audio. The agent should transcribe only the caller.
3. B. A production failure becomes a task with a label and a tag.
4. B. `regressions` lists `cost`. The exit code tells the pipeline, and a person makes the trade.
5. B. It is a controlled experiment with a rollback path.
6. B. Tuning against the regression set inflates its scores. The fresh sample is the check.

</details>

## Sources

- **Lecture:** Clay Bavor, "Practical Lessons from Deploying Real-World AI Agents", UC Berkeley Agentic AI MOOC, Fall 2025: [video](https://www.youtube.com/watch?v=sfJM4LaiYsM), used at [the agent iceberg](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=480), [every channel is digital](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=840), [metrics that fit](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=1440), [AI to check AI](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2400).
- **Reading:** Kumar Pandya and Sachi Shah, "Voice Sims: test agents in real world conditions before they talk to your customers", Sierra blog (September 11, 2025): [link](https://sierra.ai/blog/voice-sims-test-agents-in-real-world-conditions-before-they-talk-to-your-customers).
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 14, sections on continuous integration and testing in production: [link](https://mlip-cmu.github.io/book/14-quality-assurance-basics.html).

## Next

→ [the case study of Berkeley's green agent and white agent project](08-case-study-the-green-agent-and-white-agent-project.md), a course that asks students to build the evaluator first.
