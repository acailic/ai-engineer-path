# 04. Planning for Mistakes

**Level:** Practitioner · **Reading time:** 30 min · **Exercise:** 90 min
**Prerequisites:** [Goals and Requirements](03-goals-and-requirements.md), for requirements, assumptions and specifications.

> **In one sentence:** After this chapter you can run a mistake analysis for a feature that contains a model: list how it fails, trace which failures reach a person, and choose design changes that keep one wrong prediction from becoming an incident.

## Why this matters

The triage model is 96 percent accurate. Support receives 50,000 tickets a day, so the model makes about 2,000 wrong predictions a day. They do not spread evenly. Most come from tickets written in non-native English, or about a product that launched last month. Those customers wait an extra day, every time, and the dashboard shows a healthy average.

Accuracy is an average. Harm lives in the exceptions. This chapter shows how to find the exceptions before your users do.

## The core idea

Treat the model as an unreliable component, and keep two words apart:

- A **component mistake** is a wrong output from one part: the model predicts `billing` for a technical ticket.
- A **system failure** is a violation of a system requirement in the real world: a customer waits three days for an answer.

The first always happens. The job is to stop it from turning into the second.

An ML component is like a brilliant colleague with one blind spot: right most of the time, and wrong in the same way every time you ask. The picture breaks in two places. A colleague learns when corrected. A model repeats its mistake until someone retrains it, and a second model trained on the same data tends to share the blind spot.

Three facts follow, and they shape every design decision in this chapter:

1. **Mistakes are not random.** They cluster on certain inputs or certain groups of people.
2. **Retrying does not help.** The same input gives the same output.
3. **Confidence does not protect you.** A prediction made with 99 percent confidence can be wrong.

So you do two things at once: improve the model, and build the rest of the system so that a wrong prediction causes little harm. Kästner's model for this is a driverless train. Its obstacle detection is imperfect. Fenced tracks, platform screen doors and pressure sensors in the doors keep passengers safe anyway.

### Six design strategies

| Strategy | The idea | For the triage feature | Where it fails |
|---|---|---|---|
| 1. Human in the loop | Let a person check or decide | A review queue for uncertain tickets | People approve by habit |
| 2. Undo and appeal | Make every action reversible | A "wrong team?" button on the ticket | Irreversible actions |
| 3. Guardrails | Plain checks around the model's output | Accept only categories on the current list | When the check shares the model's blind spot |
| 4. Detect and recover | Notice a failure and fall back | Model times out, ticket goes to the general queue | Without an independent signal to watch |
| 5. Redundancy | Independent sources, compared | Two models trained on different data | Two copies of the same model |
| 6. Containment | Limit what depends on the prediction | Nothing else may read the category | Late or unavailable predictions |

**Strategy 1 has three strengths.** Kästner takes three modes of interaction from Geoff Hulten (chapter 7), ordered from most to least forceful:

- **Automate.** The system acts without asking. Spam filters and thermostats work this way. Use it when the cost of a mistake is low or something else contains it.
- **Prompt.** The system asks the user to confirm before acting. It keeps a person responsible, but it interrupts. Too many prompts and people click through without reading. Kästner notes that "humans are poor monitors for machines" ([chapter 7](https://mlip-cmu.github.io/book/07-planning-for-mistakes.html)). The tendency to accept a machine's suggestion is called **automation bias**.
- **Augment.** The system shows information and the user decides: a spelling underline, a ranked list, a suggested reply. It interrupts least, so it suits cases where mistakes are common.

Hybrids are common. Kästner describes a train that automates everything and prompts a remote operator only when an obstacle has not moved for twenty seconds.

## How it works, step by step

A **mistake analysis** is a structured pass over one feature. It takes an afternoon for a small feature, with the engineer, the data scientist and someone who knows the users.

1. **Write the system failures.** Use the REQ statements from the last chapter. Two or three is enough to start.
2. **Work forward with FMEA.** For each component, list the ways it can fail.
3. **Work backward with a fault tree.** Take the worst failure and ask what must happen for it to occur.
4. **Read the cut sets.** Look for failures that a single mistake can trigger.
5. **Choose design changes** from the six strategies.
6. **Write down detection.** Name the signal that would reveal each row in production. [Chapter 10](10-planning-for-operations.md) turns these into monitors.
7. **Repeat** after every incident and before every release that changes the model.

### Step 2: FMEA

**Failure Modes and Effects Analysis (FMEA)** starts from components and reasons forward. Each row holds a component, one failure mode, the effect on the system, the detection and the mitigation. Most teams add a severity score to sort the rows. The method gives no guarantees. It stops teams from stopping at "the prediction is wrong".

### Step 3: Fault trees

A **fault tree** starts from one system failure and reasons backward. The failure is the root. Below it, gates show how causes combine: an **AND gate** needs all its inputs, an **OR gate** needs one. A cause that you do not split further is a **basic event**. Kästner recommends treating model failure as a basic event, because you rarely know why a model failed.

A **cut set** is a group of basic events that together trigger the failure. A **minimal cut set** loses that property if you remove any one of its events. Small cut sets are dangerous: fewer things have to go wrong. Two kinds of mitigation follow:

- **Add an event** to the cut set, so that more must go wrong. A second independent check does this.
- **Remove an event** by redesigning, so that it can no longer occur.

Adding is more common than removing.

### Step 5, with help: HAZOP

**Hazard and Operability Study (HAZOP)** is a guided brainstorm. You apply fixed **guidewords** to each component and output and ask what each would mean there. The classic guidewords include *no or not*, *more*, *less*, *part of*, *reverse*, *other than*, *early*, *late*, *before* and *after*. Researchers have proposed ML-specific ones: *wrong*, *invalid*, *incomplete*, *perturbed* and *incapable*. Apply them to the data, the training pipeline and the monitoring as well as the model: wrong labels, too little data, delayed inputs, missing monitoring.

## Worked example

### A mistake analysis of the triage feature

The feature routes every ticket. When it judges a ticket to be spam, or a duplicate of a known issue, it closes the ticket with a canned reply.

**Step 1: system failures.**

- S1: A customer with a real problem waits more than one business day for the right team.
- S2: A customer with a real problem has the ticket closed without help.

**Step 2: FMEA.** Severity runs from 1 (annoying) to 5 (a customer loses access to help).

| Component | Failure mode | Effect | Detect by | Mitigation | Severity |
|---|---|---|---|---|---|
| Category predictor | Wrong category, high confidence | S1 | Re-route rate per team | "Wrong team?" button | 2 |
| Category predictor | Confident on unusual input | S1 | Input checks: unknown language, huge pasted log | Route to the general queue | 3 |
| Spam check | Real ticket marked spam | S2 | Reopen requests | Human review before closing | 5 |
| Duplicate match | Matches the wrong known issue | S2 | Replies after closure | Ask "did this solve it?" and reopen on "no" | 4 |
| Reply sender | Sends a canned reply after a human reopened the ticket | Confusion | Audit of ticket timelines | Send only while the ticket is still closed | 2 |
| Model service | Down or slow | S1 for every ticket | Error and latency metrics | Timeout, then general queue | 3 |

**Steps 3 and 4: a fault tree for S2, as code.** The script needs Python 3.10 or newer and nothing else.

```python
# faulttree.py — the smallest sets of failures that close a real customer's ticket.
# A node is ("event", name), ("and", child, ...) or ("or", child, ...).

def minimize(sets):
    """Drop supersets, so only minimal cut sets remain."""
    kept = []
    for s in sorted(set(sets), key=len):
        if not any(k <= s for k in kept):
            kept.append(s)
    return kept

def cut_sets(node):
    kind, *children = node
    if kind == "event":
        return [frozenset([children[0]])]
    if kind == "or":
        return minimize([s for child in children for s in cut_sets(child)])
    if kind == "and":                       # combine: pick one cut set per child
        combined = [frozenset()]
        for child in children:
            combined = [a | b for a in combined for b in cut_sets(child)]
        return minimize(combined)

CLOSED = ("or",
    ("and", ("event", "spam check wrong"), ("event", "reviewer misses it")),
    ("and", ("event", "duplicate match wrong"), ("event", "customer does not reopen")))

for s in sorted(map(sorted, cut_sets(CLOSED))):
    print(len(s), s)
```

Run `python faulttree.py`. It prints:

```
2 ['customer does not reopen', 'duplicate match wrong']
2 ['reviewer misses it', 'spam check wrong']
```

What to observe:

- **Each minimal cut set has two events.** No single failure closes a real ticket. A model mistake must coincide with a failed assumption about the world: an inattentive reviewer, or a customer who does not reply.
- **The tree reads as the requirements.** The root is a REQ violation. `spam check wrong` is an unmet SPEC. `reviewer misses it` is a broken ASM.
- **Remove the reviewer to save cost.** Replace the first `and` with the single event `("event", "spam check wrong")` and run it again. The script now prints a cut set of size 1. One wrong verdict reaches a customer.

**Step 5: design changes.** The tree shows where to act.

1. Keep the human review for spam verdicts. It is what makes the cut set size two.
2. Send "did this solve it?" after every closure, and treat a reply within seven days as a reopen. This weakens the second cut set's reliance on the customer.
3. Send canned replies only while the ticket is still closed.

**Step 6: detection.** The "Detect by" column is the start of the monitoring plan: reopen requests, re-route rate per team, model latency. [Chapter 10](10-planning-for-operations.md) covers the rest.

**Step 5 with HAZOP.** A short pass over the category predictor with the guidewords:

| Guideword | Question for the predictor |
|---|---|
| No or not | Does it return no category at all? |
| More or less | Does it return extra fields, or no confidence? |
| Other than | Does it return a category that is not on the list? |
| Early or late | Does the answer arrive after the queue's timeout? |
| Wrong (ML) | Is the category wrong? |
| Perturbed (ML) | Did odd characters or a pasted log change the answer? |
| Incapable (ML) | Is this a kind of ticket it has never seen? |

### Two checklists

Use the first in every design review of a model-backed feature:

- [ ] Every automated action is labeled automate, prompt or augment, with a reason.
- [ ] Every action can be undone or appealed. Irreversible ones need a confirmation.
- [ ] Output guardrails check the allowed values. Input checks catch unusual inputs.
- [ ] A checker independent of the model watches the effect of the action.
- [ ] The fallback for a down, slow or garbage-producing model is defined and tested.
- [ ] The list of components that depend on this prediction is written down.
- [ ] Each failure mode has a signal that someone watches.

Use the second each time you run the analysis:

- [ ] System failures are written in world terms.
- [ ] FMEA covers every ML component, with a severity for each row.
- [ ] A fault tree exists for the worst two or three failures.
- [ ] No minimal cut set of size one remains without a written decision to accept it.
- [ ] A HAZOP pass covered the model, the data, the pipeline and the monitoring.
- [ ] Someone who knows the users reviewed the result.

For how to keep checklists usable, see [Checklists](../11-professional-practice/07-checklists.md).

### What changes for LLM and agent systems

The method transfers unchanged. The rows of the FMEA change.

An LLM-backed feature adds failure modes that have no counterpart in a classifier: invented facts (called **hallucination**), output that breaks the parser, a refusal to answer, answers that differ between runs, and instructions hidden in user text. The last one is an attack, not an accident: [Jailbreaks and Prompt Injection](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md).

Fact 2 changes too. An LLM samples its words, so the same input can give a different answer on a retry. That has two consequences. Retrying becomes a real strategy. And you cannot reproduce an incident from the input alone, so log the model version and settings with every call. [Testing Generative and LLM Components](../08-quality-assurance/05-testing-generative-and-llm-components.md) covers how to test for these modes.

Guardrails built on a second model call are common: a separate check that the draft reply contains no promise the company cannot keep. Independence matters more than ever. A checker from the same model family, judging its own output, tends to share the blind spot: [Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md).

For an **agent**, a program that lets the model call tools, the doer-checker pattern is the core of the design. The model is the doer. The checkers are things it does not control: an allow-list of tools, scoped credentials, a sandbox, and a person's approval before anything irreversible. In practice the dangerous cut sets all have the same shape: *model wrong, and nothing stops the action*. Start with [Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md).

## What the practitioners say

Kästner devotes chapter 7 to this topic. His main points, beyond the methods above:

**Why models fail.** He names common causes. Models learn correlations, not causes: dogs photographed in snow get labeled as wolves. A hidden third factor can explain a correlation, as age explains a link between baldness and COVID risk. Causality can run backward: early chess programs trained on grandmaster games learned that sacrificing the queen wins. Data rarely shows what would have happened otherwise. And inputs far from the training data, called **out-of-distribution** inputs, get confident nonsense: a train's detector may miss children and unicyclists it never saw.

**Mistakes are not random.** A model can reach 99.99 percent average accuracy and still fail consistently on wheelchair users. Inference is mostly deterministic, so each copy of a model fails on the same inputs. Attackers can also force mistakes; he cites work on physical attacks against vision models (Eykholt and colleagues, 2018). A **calibrated** confidence score, one that matches the model's real accuracy on average, is the best case. Even then it supports only careful probabilistic reasoning.

**Guardrails are usually not ML.** Trains rely on fenced tracks, platform screen doors and pressure sensors. In software: hardcoded ranges, overrides for known inputs, rules such as banned-word filters. A model can serve as a guardrail if it was trained for a different task and fails independently.

**Detection uses indirect signals.** In the **doer-checker** pattern, the checker rarely inspects the doer's output, because telling a wrong prediction from a right one is the original problem. It watches effects instead: a gyroscope shows a train leaning in a curve, and the safety controller brakes. **Graceful degradation** then reduces function to stay safe: the email client runs without suggestions; a train without its lidar runs slower with larger gaps.

**Redundancy needs diversity.** Hot standby with two cameras works for hardware failures. For model mistakes, the redundant parts must differ substantially, as radar, lidar, vision and maps do.

**Containment is about data flow.** For ML, mistakes spread through data: a wrong prediction feeds another component. So ask what depends on each model's output and what happens when the model is late or absent. His counterexamples are a US Navy ship that needed about three hours to reboot after a division by zero in a database application spread into its control systems, and a car stopped remotely through its entertainment system.

**No method gives guarantees.** Fault trees are never complete, and domain knowledge decides how far to split events. A structured best effort still beats unstructured brainstorming.

## Pitfalls

1. **Trusting the confidence score.** Fix: treat it as one input to a routing rule, and check calibration on real data.
2. **Adding a second copy of the same model.** Fix: independence, through different data, a different method or a different sensor.
3. **Counting on a human who approves all day.** Fix: limit prompts to the cases that matter, and measure how often reviewers disagree.
4. **Writing "wrong prediction" as one FMEA row.** Fix: split it into the ways it is wrong.
5. **No fallback.** Fix: decide and test what happens when the model is down, slow or returns garbage.
6. **A guardrail that shares the blind spot.** Fix: a different model, different training data, or a plain rule.
7. **Running the analysis once.** Fix: repeat after incidents and before model changes.

## Try it

Run a mistake analysis on one feature with a model in it.

Include:

1. Two or three system failures, written as violations of requirements.
2. An FMEA table with at least eight rows and a severity for each.
3. One fault tree for the highest-severity failure, with its minimal cut sets.
4. Three design changes, each tied to a cut set or a row.
5. One detection signal per row.

**You are done when** every automated action in the feature has either a second independent event that must also fail, or a written decision to accept the risk, and someone who knows the users has read the table.

**Stretch goal:** encode your fault tree in the script and check that each design change grows the smallest cut set or removes an event.

## Key takeaways

- A wrong prediction is a component mistake. Keep it from becoming a system failure.
- Mistakes cluster, repeat on the same input and come with confident scores.
- Work forward with FMEA and backward with fault trees. A cut set of size one is a finding.
- Mitigations either add an independent event to a cut set or remove an event by redesign.
- Humans help most when they decide on few, important cases. Redundancy helps only when the parts are truly different.

## Self-check

1. Which is the component mistake and which is the system failure: "the model predicts `billing` for a technical ticket" and "a customer waits three days for an answer"?
2. A model reaches 99.99 percent accuracy. Which question matters most?
   - A. How large was the test set used to compute it?
   - B. Which inputs does it fail on, and do they share a trait?
   - C. Which algorithm was used to train the model?
   - D. How long does one prediction take to return?
3. Why does running the same model three times and taking a majority vote not create redundancy?
4. Name the three interaction modes, from most to least forceful.
5. A minimal cut set contains one event, "model output wrong". What must a mitigation do?
   - A. Remove the event by retraining the model on more data.
   - B. Add an independent event that must also occur, or remove the event by redesign.
   - C. Lower the severity rating of the failure mode.
   - D. Move the event to a different branch of the tree.
6. In the doer-checker pattern, what does the checker watch, and why not the doer's output?

<details><summary>Show answers</summary>

1. The prediction is the component mistake. The three-day wait is the system failure: a requirement was violated in the world.
2. B. An average hides clusters. If the failures share a trait, one group of users or inputs carries all the harm.
3. Inference is mostly deterministic. All three copies return the same answer, including the same wrong one.
4. Automate, prompt, augment.
5. B. A mitigation makes more go wrong before the failure occurs, or makes the event impossible. Retraining may lower the rate but cannot remove the event.
6. The checker watches the effect of the action through a signal the doer does not control. Judging the output directly would require knowing the right answer, which is the problem the model was built to solve.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 7: [Planning for Mistakes](https://mlip-cmu.github.io/book/07-planning-for-mistakes.html)
- **Reading:** Geoff Hulten, *Building Intelligent Systems* (Apress, 2018), the source of the three interaction modes.
- **Reading:** Kevin Eykholt et al., "Robust Physical-World Attacks on Deep Learning Models" (CVPR 2018), cited in chapter 7 for attacks that force mistakes.

## Next

→ [Architecture for ML Systems](05-architecture-for-ml-systems.md), which turns the mitigations from this chapter into components and the interfaces between them.
