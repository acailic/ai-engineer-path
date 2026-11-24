# 01. From Models to Systems and Products

**Level:** Foundation · **Reading time:** 25 min · **Exercise:** 60 min
**Prerequisites:** none. The three definitions in *The core idea* are all you need; [Machine Learning in a Nutshell](../01-foundations/01-machine-learning-in-a-nutshell.md) goes deeper.

> **In one sentence:** After this chapter you can look at any feature that contains a model and describe the system around it: the goal, the other components, the interfaces, and what happens when the model is wrong.

## Why this matters

A data scientist on your team opens a notebook. It holds a model for support-ticket triage: given the text of a ticket, it predicts which team should handle it (billing, technical, or general). On held-out test data it is right 91 percent of the time. Someone asks, "So when does it ship?" and the room goes quiet.

Nobody in the room can answer these questions:

- Where does the model run, and who paged whom when it is down?
- A ticket goes to the wrong team. Who notices, and how does it get back on track?
- Support creates a new team next quarter. Who retrains the model, and with which tickets?
- The model learned from last year's tickets. Are they still like this year's?
- Is 91 percent good? Good for whom?

None of these is a question about the model. They are questions about the system the model lives in. This chapter gives you the vocabulary and the habit for answering them.

## The core idea

Three definitions first. A **model** is a function whose rules were not written by hand but fitted to examples. **Training** is that fitting step. **Inference**, or **prediction**, is running the trained model on a new input to get an output. An **ML component** is the model plus the code that wraps it: the request, the parsing, the retries. Every other part of the product is a **non-ML component**: the web interface, the API, the queue, the database, payments, logging.

A **system** is all of these components working together toward one goal, sitting in an **environment**: users, other software, and the world. Kästner calls the result an **ML-enabled product**: a software product with machine-learning components.

The claim of this chapter is simple. Engineers are trained to look at the model. The product succeeds or fails on the system around it.

### Three levels of zoom

Kästner describes three views of the same work (chapter 2). Each one answers a real question, and each one misses something.

| Zoom level | Who tends to sit here | Question it answers | What it misses |
|---|---|---|---|
| Model | Data science | How accurate is the function on test data? | Where the data comes from and how predictions are used |
| Pipeline (MLOps) | ML engineering | Can we retrain, deploy and monitor reliably, again and again? | It ends at the model's API |
| System (product) | The whole team | Does the product reach its goal, safely? | Nothing, if you do it properly |

**MLOps** is the name for automating the **pipeline**: everything that produces, deploys and updates the ML component. It is necessary. It is also still model-centric: the pipeline starts with model requirements and stops when the model is served.

### The analogy, and where it breaks

An ML component behaves like a flaky third-party API. You do not control its internals, it sometimes returns the wrong answer, and your code has to work anyway.

The analogy breaks in one place. A third-party API has a contract: documented inputs, documented outputs, documented errors. An ML component has none. You cannot write down the correct output for every input. If you could, you would write the function by hand and skip the model. As Kästner puts it, "We use machine learning precisely because we do not know how to specify and implement specific functions" ([chapter 1](https://mlip-cmu.github.io/book/01-introduction.html)).

He calls this the **lack of specifications**. Traditional code has a specification: a description of what the function must do, which one developer implements and other developers rely on. His contrast is a tax function documented against the tax code versus `transcribe(audio_file)`, whose docstring can only say what it is for.

Two consequences follow:

1. Replace "is it correct?" with "is it good enough for this use, on this data?" **Good enough** is a decision about the system, not a property of the model.
2. Design the rest of the system to tolerate wrong answers. Software engineers have always built reliable systems out of unreliable parts (networks, disks, other people's services). A model is one more unreliable part.

### Model quality is not system quality

Model accuracy is a means. The goal is something the product or the business needs. The two do not always move together.

Kästner cites experience from the hotel site Booking.com (chapter 2, reporting a 2019 paper by Lucas Bernardi and colleagues): more accurate models of a customer's travel preferences did not reliably raise hotel sales, and in some cases sales fell. One explanation that team offered was that suggestions felt too knowing, almost creepy. Models that did not improve the system outcome were not adopted.

The reverse also holds. Other parts of the system can do more for users than a few points of accuracy: an interface that shows the prediction as a suggestion, a one-click way to correct it, or plain non-ML safety checks. [Chapter 04](04-planning-for-mistakes.md) covers these.

### Predictions have consequences

The system sits in an environment and changes it. So safety, fairness, privacy and security are properties of the whole system, not of the model. You cannot promise any of them by inspecting a model.

The clearest illustration in the book is a smart toaster, an example Kästner borrows from Geoff Hulten. A model decides how long to toast. One day it will pick a time that burns the bread. No amount of training removes that possibility. So the designer adds three mechanisms that contain no ML at all:

1. Non-ML code that caps the toasting time.
2. A temperature sensor that cuts the power above a threshold.
3. A thermal fuse, a cheap hardware part that breaks the circuit when it overheats.

The result: "A smart toaster may occasionally burn some toast, but it shall never burn down the entire kitchen" ([chapter 2](https://mlip-cmu.github.io/book/02-from-models-to-systems.html)).

Consequences also come back as **feedback loops**: the system's predictions change the environment, which changes the data the next model learns from. Kästner's example is crime prediction. A model predicts more crime in an area that was over-policed in the past. Police patrol it more. More arrests are recorded there. Those arrests become training data, and the next model is more certain. Another is YouTube's old recommendation loop for conspiracy videos, which the book says was fixed with hard-coded rules around the model, not with better ML (chapter 1).

## How it works, step by step

The book argues for a system view. The procedure below turns that argument into something you can do in an afternoon for one feature.

1. **Write the system goal in product terms.** Not "classify tickets with 90 percent accuracy" but "route tickets to the right team on first attempt, without anyone waiting more than a day". The second sentence tells you what to measure and what "good enough" means.
2. **List every component and mark it ML or non-ML.** Include the boring ones: upload, queue, storage, the page that shows the result, the log.
3. **Mark the interfaces.** For each ML component write what goes in, what comes out, and what the consuming code assumes. The router assumes the category is one of three known values. The interface assumes a confidence score means something.
4. **Trace one wrong prediction through the system.** Follow it from the model's output to the effect on a person. Ask who notices, how fast, and who can undo it. This is a first pass; [chapter 04](04-planning-for-mistakes.md) does the full analysis.
5. **Plan for change.** Name where new training data will come from, how the model gets updated, and how you will find out that it went stale. [Chapter 10](10-planning-for-operations.md) covers the last part.

### Decide where humans belong

For each automated decision, pick one of three patterns:

| Pattern | The system | Example from the book |
|---|---|---|
| Fully automated | Acts, with no human in the path | Few settings justify this for risky decisions |
| Automated, with an appeal path | Acts, then lets a person reverse it | Fraud detection on an auction site: take the listing down, let the seller appeal |
| Human confirms | Proposes, and waits for a person | Audit-risk estimate in tax software: show it, ask the user what to do |

Kästner's warning is that people are poor monitors of a system that is right most of the time. A human who clicks "approve" on two hundred correct suggestions will approve the wrong one too. Human review is a design decision, not a safety guarantee.

### Know your role

The book's picture of a team is **T-shaped**: deep in one specialty, conversant in the neighbors. You are the software engineering bar of that T. You own the non-ML components and the interfaces, and you need enough ML to plan for its mistakes. The data scientist owns the model and needs enough engineering to know why latency and cost are requirements, not nitpicks.

## Worked example

The code below is the triage feature in miniature. It needs Python 3.10 or newer and nothing else. The "model" is a stand-in with the shape of a real one: it takes text, returns a label and a confidence.

```python
# triage.py — a support-ticket triage feature. Standard library only.
from dataclasses import dataclass

CATEGORIES = ("billing", "technical", "other")

@dataclass
class Decision:
    ticket_id: str
    category: str
    route: str      # "auto" or "human_review"
    reason: str

# The ML component: in production this calls a trained model.
# Here a small stand-in plays that role, including a shaky prediction.
def predict_category(subject: str) -> tuple[str, float]:
    s = subject.lower()
    if "invoice" in s or "charged" in s:
        return "billing", 0.93
    if "log in" in s or "crash" in s:
        return "technical", 0.55
    return "other", 0.30

# Non-ML code: the system decides what to DO with a prediction.
def triage(ticket_id: str, subject: str, predict=predict_category) -> Decision:
    category, confidence = predict(subject)
    if category not in CATEGORIES:                 # guardrail 1: known output only
        return Decision(ticket_id, "other", "human_review", "unknown category from model")
    if confidence < 0.80 or category == "other":   # guardrail 2: act only when confident
        return Decision(ticket_id, category, "human_review", "low confidence")
    return Decision(ticket_id, category, "auto", "confident prediction")

def test_confident_prediction_is_automated():
    d = triage("t1", "I was charged twice")
    assert (d.category, d.route) == ("billing", "auto")

def test_uncertain_prediction_goes_to_a_human():
    d = triage("t2", "I cannot log in")
    assert (d.category, d.route) == ("technical", "human_review")

def test_system_survives_a_broken_model():
    def broken(subject):
        return "REFUND-NOW", -1.0                  # garbage output
    d = triage("t3", "I was charged twice", predict=broken)
    assert d.route == "human_review"

if __name__ == "__main__":
    for name, obj in sorted(globals().items()):
        if name.startswith("test_"):
            obj()
            print("ok", name)
```

Run it with `python triage.py`. You should see three `ok` lines.

What to observe:

- **No ML library is installed, and the tests pass.** The safety of this feature comes from the non-ML code around the model. A **guardrail** is a plain check that limits what a model's output can cause.
- **The model is an argument.** `triage` takes the predictor as a parameter, so tests can pass in a broken one. That is the toaster's time cap in software form.
- **The third test is the one to remember.** Now imagine a model that answers `("billing", 0.95)` for every ticket. It passes both guardrails. No wrapper catches a model that is confidently wrong. Only evaluation on labeled real tickets and monitoring in production do. See [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md) and [chapter 10](10-planning-for-operations.md).

Here is the same feature as a system map, the deliverable of this chapter's exercise:

| Component | ML? | Owner | Assumes |
|---|---|---|---|
| Ticket intake form and API | No | Backend | Ticket text is present |
| Category predictor | Yes | Data science | Subject and body resemble training data |
| Guardrails and router | No | Backend | Category is known; confidence is calibrated |
| Human review queue | No | Support lead | Reviewers can spot a wrong route |
| Correction log | No | Data science | Edits reflect the true team |
| Dashboard and alerts | No | Operations | Volume and routes stay in range |

### What changes for LLM and agent systems

For a feature built on a large language model (LLM), you rarely train anything. The model belongs to someone else and you reach it through an API. Your ML component is four things: the prompt, the model name and settings, the code that parses the reply, and the retries. Put all four in version control and treat a change to any of them like a dependency upgrade.

The lack of a specification gets more severe. A prompt is a request, not a contract. The same prompt can return different answers on two runs. That is **non-determinism**: the model samples its output, so it does not always pick the same words. The provider can also replace the model behind the same name. Your only substitute for a specification is an evaluation set with expected outputs, run on every change: [evaluation is the test suite](../03-evaluation/01-evaluation-is-the-product.md).

An **agent** is a program that lets the model decide which tools to call. This turns "predictions have consequences" from a design risk into a runtime one. The output is not a label. It is an action: send an email, write a file, run a command. The guardrails change shape accordingly:

- An allow-list of tools, and credentials scoped to exactly what the task needs.
- A sandbox for anything that runs code: [Agent Infrastructure, Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md).
- Human confirmation before any step that cannot be undone.
- The assumption that any text the agent reads may be hostile. A ticket can contain instructions as easily as a web page can: [Jailbreaks and Prompt Injection](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md).

The system view still pays. A thumbs-down button or an edited reply is a labeled example, which is the triage feature's correction log under another name. For the structure of an agent itself, start with [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md).

## What the practitioners say

Christian Kästner wrote *Machine Learning in Production* to argue that ML products need more engineering discipline, not less. Four of his points shape this part of the course.

**ML introduces three challenges for software projects** (chapter 1):

1. **No specifications.** Reasoning shifts from deductive (apply rules) to inductive (generalize from observations). You cannot prove a component correct, only show it works well enough.
2. **Interaction with the real world.** Data comes from the environment and may be skewed. Users adapt to the system. Inputs can be adversarial.
3. **Data focus and scale.** Large models need expensive hardware, so they run on dedicated machines and are reached remotely.

He is careful to add that none of these is wholly new. Formal specifications were always rare. Software without ML has hurt people. Data pipelines and cloud operation predate ML.

**ML projects drift toward the risky end.** His stated conjecture is that teams use ML for ambitious ideas, often without planning for wrong or biased predictions. So teams get away with sloppy engineering less often and should invest more in requirements, risk analysis and testing. He presents this as an opinion in an open debate.

**Most projects do not reach production.** The book opens with two figures from consultants: 87 percent of ML projects fail (a 2019 VentureBeat report) and 53 percent never make it from prototype to production (a Gartner press release from 2020). Neither source defines "fail" in the book, so read them as a warning about scale, not as a measurement.

**The ideas outlast the tools.** Writing as LLMs arrived, Kästner argues that each wave, from deep learning to foundation models, adds tools without replacing the old ones. He lists five durable ideas: knowing the customer's tolerance for mistakes, designing safe systems from unreliable components, trading off accuracy against cost, latency and time to release, planning a responsible test strategy, and building systems that update quickly and are monitored. The rest of this part follows them.

## Pitfalls

1. **Treating accuracy as the goal.** Fix: write the system goal as a product outcome and measure that. Report accuracy as one input to it.
2. **Testing only the model in the notebook.** Fix: add system tests that inject a deliberately broken predictor, as in the worked example.
3. **Assuming the data is given and stable.** Fix: for every model, write down the data's source, its owner and its refresh date.
4. **Automating a decision with no way back.** Fix: give every automated action an undo, an appeal, or both.
5. **Confusing the pipeline with the product.** A reliable retraining pipeline is necessary. It says nothing about whether the feature helps the user.
6. **Forgetting feedback loops.** If triage auto-closes "general" tickets, users learn to write "urgent" in every subject line. Next quarter's training data has changed because of the model.
7. **Waiting for a specification from the data scientist.** None can exist. Agree instead on an evaluation set and on how good is good enough: [Goals and Requirements](03-goals-and-requirements.md).

## Try it

Draw a one-page system map for one feature that contains a model. Use the triage feature, or one from your own product.

Include:

1. The system goal in one sentence, with a measurable outcome.
2. A component table with an ML/non-ML column and an owner for every row.
3. For the ML component: inputs, outputs, and the assumptions consumers make.
4. A wrong-answer walk-through: pick one wrong prediction and follow it to the person affected.
5. Three tests, one of which injects a broken model.

**You are done when** a colleague who knows no ML can point to the place where a wrong prediction gets caught, every component has an owner, and the ML component has at least one non-ML mechanism around it.

**Stretch goal:** find one feedback loop in the feature and name one event you would log to detect it.

## Key takeaways

- A model is one component of a system. The system, not the model, has to reach the goal.
- ML components have no specification. Ask "good enough for what?", then design the rest of the system to tolerate mistakes.
- Model accuracy and system quality are different things. Interface, correction paths and plain safety code often matter more.
- Predictions change the environment, and the environment changes the next training data. Look for the loop.
- The pipeline view (MLOps) is necessary and still model-centric. Zoom out one more level.

## Self-check

1. A colleague says, "The model is 94 percent accurate, so the feature is done." Name two things that test accuracy does not tell you.
2. In one sentence, why can you not write a specification for an ML component the way you would for a tax-calculation function?
3. The triage model returns the wrong team with confidence 0.95, so both guardrails pass. Which two practices catch this?
4. Which of these is a feedback loop?
   - A. The model is retrained each month on the previous month's tickets.
   - B. Auto-closing low-priority tickets teaches users to write "urgent" in every subject, which changes next quarter's training data.
   - C. Support adds a new team, so the list of possible categories grows by one.
   - D. Latency rises after a library upgrade, so the team puts a cache in front of the model.
5. What separates the pipeline view from the system view?
   - A. The pipeline view includes monitoring, while the system view leaves it to the operations team.
   - B. The pipeline view ends at the model's API, while the system view includes how predictions are used.
   - C. The pipeline view is used by small teams, while the system view is used by large organizations.
   - D. The pipeline view ignores automation, while the system view depends on it for every release.
6. Name the toaster's three safety mechanisms and what each one is made of.

<details><summary>Show answers</summary>

1. Any two of: whether the predictions help the product goal; what happens to a person when the prediction is wrong; whether the test data resembles production data; how the model will be updated and monitored.
2. A specification states the correct output for each input, and for an ML task nobody can write that down. If we could, we would write the function by hand and not need a model.
3. Evaluation on labeled real tickets before release, and monitoring or sampling of predictions in production.
4. B. The system's output changes user behavior, which changes the data the next model learns from. A and C are maintenance events. D is an ordinary performance fix.
5. B. The pipeline covers producing, deploying and updating the ML component. The system view adds the non-ML components, the users and the environment.
6. Non-ML code that caps the toasting time; a temperature sensor that cuts power above a threshold; a thermal fuse, a hardware part that breaks the circuit when it overheats.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 1: [Introduction](https://mlip-cmu.github.io/book/01-introduction.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 2: [From Models to Systems](https://mlip-cmu.github.io/book/02-from-models-to-systems.html)
- **Reading:** David Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (2015), cited in chapter 2 for the observation that model code is a small part of an ML system's code.
- **Reading:** Lucas Bernardi, Themistoklis Mavridis and Pablo Estevez, "150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com" (2019), cited in chapter 2 for model accuracy versus system outcomes.

## Next

→ [When to Use ML, and When Not To](02-when-to-use-ml-and-when-not-to.md), because the cheapest ML component to operate is the one you never build.
