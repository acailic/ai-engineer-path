# 03. Goals and Requirements

**Level:** Practitioner · **Reading time:** 25 min · **Exercise:** 60 min
**Prerequisites:** [From Models to Systems and Products](01-from-models-to-systems-and-products.md), for the difference between a system goal and model accuracy.

> **In one sentence:** After this chapter you can turn a vague request for an ML feature into layered goals, one precise measure per goal, and a short list of requirements that separates the world from the software.

## Why this matters

The triage model got better. Accuracy on the test set went from 88 to 94 percent. Three months later nothing else had moved. Customers waited as long as ever, and support leads still re-routed one ticket in five.

The data scientist was doing her job. Nobody had written down what the feature was for. Each person held a different goal in their head:

- The data scientist: higher accuracy.
- The support lead: fewer re-routes.
- The business: lower cost per resolved ticket, and no lost customers.

This chapter fixes that. You write the goals down in layers, find where they pull apart, give each one a measure, and turn them into requirements.

## The core idea

### Goals come in layers

Kästner separates four layers (chapter 5). Here they are for the triage feature:

| Layer | Whose goal | For the triage feature | A measure |
|---|---|---|---|
| Organizational | The company | Lower cost per resolved ticket. Keep customers. | Cost per resolved ticket. Churn: the share of customers who leave |
| Product | The feature | A ticket reaches the team that can solve it, the first time | First-time-right rate |
| User | Each kind of user | Customer: a fast, correct answer. Agent: every ticket in my queue is mine to solve | Time to first correct answer. Re-route rate |
| Model | The ML component | Predict the right category | Accuracy on an evaluation set |

For a company, the organizational goal is almost always money, now or later. That goal is far away and hard to observe today. So teams watch **leading indicators**: easier-to-observe measures that they expect to move with future success. Kästner's example is the number of attorneys licensing the company's chatbot, and the ratio of new to canceled licenses. A **proxy** is any measure that stands in for something you cannot observe directly.

The layers are like an org chart: each one exists to serve the level above. The picture breaks at one point. An org chart stays aligned because someone has authority over each level. Goals do not. The model layer can improve while the top layer gets worse.

### The layers pull apart

Kästner's clearest example is a self-help legal chatbot from a real project (chapter 5). A company licenses it to attorneys as a marketing tool. The product goal is to look modern and to generate leads, not to give complete legal advice.

Now give the chatbot a better model. It answers more questions without an attorney. Clients are happier. Attorneys get fewer contracts, so the customer is less happy. A gain at the model layer is a loss at the user and product layers.

His conclusion for that product: it is fine, even intended, for the chatbot to fail on hard questions and hand the client to an attorney. A good-enough model is good enough.

The first two chapters made the same point with Booking.com, where more accurate models did not raise sales. You find such conflicts only if you write every layer down and ask how each one relates to the others.

### Goals become requirements

Goals are high-level requirements. Kästner suggests a chain for finding where ML helps: a goal needs **decisions**, decisions need answers to questions, and some answers can come from predictions. He uses two user-story forms, which you can fill in for the triage feature:

- "As [role], I need to make [decision] to achieve [goal]." As a support lead, I need to decide which team handles a ticket, to keep first-response time under one hour.
- "As [role], I need to know [question] to make [decision]." As a support lead, I need to know which team can solve this ticket.

If no prediction would change a decision, the model has no job.

### Requirements live in two places: the world and the machine

Kästner borrows a distinction called "the World and the Machine" (chapter 6). A goal is a statement about the real world: a state you want out there. The software, the *machine*, only touches that world through its inputs and outputs. So he splits statements three ways:

| Kind | About | Example for triage |
|---|---|---|
| **REQ**, a requirement | The world: the state you want | A customer with a billing problem gets an answer from the billing team within one business day |
| **ASM**, an assumption | The world: what you rely on | Customers describe their problem in their own words. The list of teams changes at most once a quarter |
| **SPEC**, a specification | The software: what it must do | Given ticket text, return one category from the current list and a confidence, in under 200 ms |

The software can satisfy the requirement only while the assumptions hold. If the world breaks an assumption, no change to the code fixes the failure.

Kästner's example is Lufthansa Flight 2904, which overran the runway at Warsaw in 1993. The software had one safety requirement: never engage the thrust reversers while the plane is in the air. After touchdown the crew could not engage them in time. The software had to infer "on the ground" from sensors, and on that runway the inference failed. <!-- VERIFY: the sensor detail is from general knowledge, not from the book chapter, whose copy was trimmed. -->

<!-- SOURCE GAP: the copy of book chapter 6 used here was trimmed. Its full definitions of REQ, ASM and SPEC, and the rest of the Lufthansa account, were not available. The table above applies the visible labels to my own example. -->

### Behavioral and quality requirements

Requirements also split by kind:

- A **behavioral requirement** says what the software does. "If the input is 'fall detected', call the emergency responder after 30 seconds."
- A **quality requirement** says how well it must do it, or how it must be built. "The fall detector has a latency under 100 ms."

Kästner lists common qualities: safety, security, reliability and fairness; latency, throughput and cost; usability and convenience; development cost, development time, maintainability and extensibility. Every quality requirement needs a measure and the conditions under which you take it. "Fast" is a wish. "Under 200 ms for 95 of 100 requests at 50 requests per second" is a requirement. [Chapter 06](06-quality-attributes-of-ml-components.md) goes deeper on these.

## How it works, step by step

Run this on one feature. It produces a one-page note.

1. **List the goal layers.** One line each for organization, product, every kind of user and the model.
2. **Find the conflicts.** For each pair of layers, ask whether improving one can hurt the other.
3. **Write one measure per goal.** Use the three ingredients below.
4. **Check each measure** with the tests in *Is the measure any good?*
5. **Separate the world from the machine.** Write REQ, ASM and SPEC statements.
6. **Add quality requirements with numbers.**
7. **Review the note like code.** Show it to the stakeholders named in it and ask what is missing.

### Three ingredients of a measure

Kästner's test for a precise measure: imagine arguing in front of a judge that you met the goal, while an independent party recomputes the measure. To pass, each measure needs three ingredients.

| Ingredient | Question it answers | Kästner's latency example |
|---|---|---|
| Measure | What quantity, under what conditions? | 90 percent of chatbot requests get a response within X ms under normal load |
| Data collection | Which data, gathered how? | Log the time of every request and every response on the server |
| **Operationalization** | How do you compute the number from the data? | Take the fastest 90 percent of the last 24 hours and report the slowest among them |

**Operationalization** is the rule that turns raw observations into a number. It is where most disagreements hide.

### Is the measure any good?

**Noise or bias?** For measurements, Kästner separates two properties that share names with classifier metrics but mean something else. The **accuracy of a measure** is how close its values lie, on average, to the true value. Its **precision** is how reliably it gives the same value when you repeat it.

- Low precision is noise. You can see it, and it averages out over many observations.
- Low accuracy is systematic. The measure is quietly wrong every time, so no statistic reveals it. Kästner's example is a revenue count that includes expired subscriptions.

**Does it measure what you meant?** Kästner's minimum: plot the distribution of the values and inspect a sample by hand. For important measures he names three questions:

| Validity | Question |
|---|---|
| Construct | Does the measure capture the concept you intended? |
| Predictive | Does it tell you something about the outcome you care about? |
| External | Does it still hold outside the data it was designed on? |

### Two traps

- **The streetlight effect.** People measure what is easy to observe, the way a drunkard looks for his keys under the streetlight instead of where he dropped them. Kästner's example: counting chat messages as a proxy for client satisfaction, because the logs have them.
- **Goodhart's law.** "When a measure becomes a target, it ceases to be a good measure" ([chapter 5](https://mlip-cmu.github.io/book/05-setting-and-measuring-goals.html)). Reward developers for fixing bugs and some will write bugs to fix. Kästner's advice is to set goals with measures and never to use them as incentives.

### Bringing the stakeholders in

Kästner defines a **stakeholder** as anyone with an interest in the system or affected by it, including people who never use it: regulators, responders, competitors. His advice for gathering requirements (chapter 6):

- Interview stakeholders about the problems they have, not only the solution they imagine. Users often change their mind once they see mistakes: people who wanted the fall-detecting watch to call for help automatically reversed that after it mistook a hand gesture for a fall.
- Ask about trade-offs directly. Is a more accurate answer worth a longer wait or a higher price?
- Negotiate conflicts by choosing one option, a compromise or a setting. His example: call for help after 30 seconds unless the wearer presses "I'm fine".
- Write the result as "shall" statements, including assumptions and the responsibilities of things that are not software.
- Expect requirements to change as prototypes appear. That is a reason to keep the note short, not a reason to skip it.

## Worked example

This is step 3 for one measure: first-time-right rate. The code needs Python 3.10 or newer and nothing else.

```python
# measure.py — operationalizing "first-time-right rate" for ticket routing
from datetime import datetime, timedelta

# Routing events in time order, as the system logs them.
ROUTING_LOG = [
    {"ticket": "t-101", "auto": True,  "at": "2026-11-02T09:14:00"},
    {"ticket": "t-101", "auto": False, "at": "2026-11-02T11:02:00"},  # a human re-routes
    {"ticket": "t-102", "auto": True,  "at": "2026-11-02T09:20:00"},
    {"ticket": "t-103", "auto": True,  "at": "2026-11-03T10:00:00"},
    {"ticket": "t-103", "auto": False, "at": "2026-11-12T10:00:00"},  # nine days later
]


def first_time_right_rate(log, window=timedelta(days=7)):
    """Share of automatically routed tickets that no human re-routes
    within `window` of the automatic routing."""
    first_auto, re_routed = {}, set()
    for event in log:
        when = datetime.fromisoformat(event["at"])
        if event["auto"]:
            first_auto.setdefault(event["ticket"], when)
        else:
            first = first_auto.get(event["ticket"])
            if first is not None and when - first <= window:
                re_routed.add(event["ticket"])
    assert first_auto, "no automatically routed tickets in the log"
    return 1 - len(re_routed) / len(first_auto)


print(f"{first_time_right_rate(ROUTING_LOG):.0%}")   # 2 of 3 tickets: 67%
```

Run `python measure.py`. It prints `67%`: three tickets were routed automatically and one of them was re-routed within a week.

What to observe:

- **All three ingredients are visible.** The measure is the share in the docstring. Data collection is `ROUTING_LOG`. The operationalization is the function.
- **The definition hides three choices.** The window is seven days. Only automatically routed tickets count. A human re-route is the only accepted signal of a wrong route. Each is a decision someone can dispute, so write them next to the measure.
- **It is a proxy.** An agent who answers an off-topic ticket without re-routing it is invisible to this measure. Pair it with time to first correct answer.
- **Do not make it a target.** Score agents on this number and re-routes will stop, whether or not the tickets were routed well.

### What changes for LLM and agent systems

The layers stay the same. What changes is the bottom layer and the nature of the measures.

The model goal is no longer plain accuracy. It is a score on an evaluation set that you wrote: labeled examples with expected outputs. Helpfulness ratings from users are proxies with known bias, since happy users rate less often than angry ones. Treat evaluation as the product's test suite: [Evaluation Is the Product](../03-evaluation/01-evaluation-is-the-product.md).

The same input can produce different outputs on two runs. A measure taken from one run is noisy by construction. Run each evaluation several times and report a range, not a number.

Two quality requirements move to the front. Cost per request, in tokens, is now a first-class number in the spec. So is resistance to hostile input: "a ticket containing instructions does not change the system's behavior" is a quality requirement you can test, as in [Threat Modeling LLM Applications and Agents](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md).

For an agent, write one goal layer per step and one for the whole task. The measure that matters is end-to-end task success. A high score on each step can still add up to a failed task. The ASM row grows too: an agent assumes that its tools work, that the pages it reads are honest and that its credentials are scoped. Part 02 covers the structure: [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md).

## What the practitioners say

- **Goals are statements of intent that many actors must deliver** (chapter 5). They give the rationale for requirements and design, and they say how to measure success.
- **Everything is measurable, at a price.** Kästner follows Douglas Hubbard's definition of measurement as "a quantitatively expressed reduction of uncertainty based on one or more observations". If you care about a property, you can detect it; if you can detect it, you can rank better against worse. Better measurements cost more, so spend according to the value of the decision.
- **Prefer standard measures** when they exist, and state them with their conditions. For complex qualities, he recommends the **Goal-Question-Metric** approach: name the goal, list the questions that tell you whether you reached it, then pick one measure per question. It keeps you from measuring only what is convenient.
- **Requirements engineering has a poor reputation** (chapter 6): long, formulaic documents. Kästner argues that it is not all-or-nothing. A light analysis early, at least for the critical parts, surfaces problems while they are cheap.
- **Many safety, fairness and security problems are requirements problems.** They are among the most expensive to fix after deployment.

## Pitfalls

1. **Writing the model goal as the project goal.** Fix: four layers, always, with the model last.
2. **Measuring what is in the logs.** Fix: start from the goal with Goal-Question-Metric, then work out how to collect the data.
3. **A precise, wrong measure.** A number that never fluctulates can still be biased. Fix: inspect a sample by hand and compare with an independent source.
4. **Paying people on a proxy.** Fix: measures inform, incentives stay separate.
5. **Mixing world and machine.** "The classifier shall reach 90 percent" is a specification, not a requirement. Fix: one REQ, ASM and SPEC table per feature.
6. **Quality requirements without numbers.** Fix: a value, the load and the window, for each one.
7. **Asking users what they want.** Fix: ask what problem they have and what happens when it goes wrong.

## Try it

Write the one-page goals-and-requirements note for one feature that contains a model.

Include:

1. The four goal layers, with every kind of user.
2. One conflict between layers, or a sentence saying you looked and found none.
3. One measure per goal, each with measure, data collection and operationalization.
4. One REQ, ASM and SPEC table.
5. Three quality requirements with numbers.

**You are done when** a colleague can recompute one of your measures from the note alone and get your number, and can point to the assumption most likely to break in production.

**Stretch goal:** find one place where your measure and the goal it stands for would disagree, and add a second measure that catches the gap.

## Key takeaways

- Goals sit in four layers: organization, product, users, model. They support each other and sometimes conflict.
- A measure needs three ingredients: what you measure, how you collect the data and how you compute the number.
- Noise is visible and averages out. Bias is invisible and does not.
- Measure what matters, not what is easy. Never turn a measure into a target.
- Requirements describe the world. Specifications describe the software. Assumptions connect them, and they break.

## Self-check

1. Name the four goal layers, from the top.
2. Model accuracy rises and the first-time-right rate stays flat. What is the first thing to check?
   - A. Whether the test set is large enough to detect the improvement.
   - B. Whether every team logs its re-routes in the same way.
   - C. Whether better predictions change what the system does with them.
   - D. Whether the accuracy figure was computed for the latest model.
3. A measure gives the same value every time you compute it, and the value is wrong. Is that inaccuracy or imprecision, and why is it the harder problem?
4. Write one REQ, one ASM and one SPEC for "keep junk out of my inbox".
5. Which is the streetlight effect?
   - A. Agents stop re-routing tickets because their team is scored on first-time-right rate.
   - B. The team counts messages per chat because the logs contain them, though the count does not say whether clients were helped.
   - C. The satisfaction survey reaches only five percent of attorneys in any given month.
   - D. Latency is reported from the slowest of the fastest ninety percent of requests.
6. What separates a quality requirement from a behavioral one, and what must every quality requirement contain?

<details><summary>Show answers</summary>

1. Organizational, product, user and model.
2. C. The model layer improved. The question is whether the routing logic, the review queue or the interface turns that into a different outcome.
3. Inaccuracy. Repeatability shows high precision. The error is systematic, so averaging and other statistics never expose it. You find it by inspecting samples or comparing with the true value.
4. Example. REQ: a user loses no important message to the spam folder. ASM: senders of important mail do not write like spammers, and users report misfiles. SPEC: if the spam score is above 0.9, move the message to the spam folder.
5. B. The count is convenient and irrelevant to the goal. A is Goodhart's law. C and D are ordinary limits of a measure.
6. A behavioral requirement says what the software does. A quality requirement says how well. Each quality requirement contains a value, and the conditions under which it is measured.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 5: [Setting and Measuring Goals](https://mlip-cmu.github.io/book/05-setting-and-measuring-goals.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 6: [Gathering Requirements](https://mlip-cmu.github.io/book/06-gathering-requirements.html)
- **Reading:** Douglas W. Hubbard, *How to Measure Anything: Finding the Value of Intangibles in Business* (Wiley, 2014), cited in chapter 5.
- **Reading:** Victor R. Basili, Gianluigi Caldiera and H. Dieter Rombach, "The Goal Question Metric Approach" (1994), cited in chapter 5.
- **Reading:** Samir Passi and Phoebe Sengers, "Making Data Science Systems Work" (2020), the study behind the chatbot scenario.

## Next

→ [Planning for Mistakes](04-planning-for-mistakes.md), because the requirements tell you what must not go wrong, and that chapter shows how to keep a wrong prediction from breaking them.
