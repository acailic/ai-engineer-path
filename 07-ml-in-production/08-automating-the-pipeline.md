# 08. Automating the Pipeline

**Level:** Practitioner · **Reading time:** 25 min · **Exercise:** 60 min
**Prerequisites:** [Deploying a Model](07-deploying-a-model.md), for where the model that this pipeline produces will run.

> **In one sentence:** After this chapter you can turn a notebook that trained a model once into a pipeline of tested stages that anyone can re-run, that updates the model on a schedule, and that stops a bad model before users see it.

## Why this matters

Retraining the triage model took three days. The computation took forty minutes. The rest was toil: finding last month's script, deleting odd rows by hand in a spreadsheet, re-running cell after cell, remembering the export format.

One month the export had an extra column and nobody noticed. Nobody could say which data had produced the model in production. The next month a new product launched, and for three weeks the model kept routing its tickets to "other", because nobody had scheduled a retrain.

Kästner has a name for training a model once and walking away: *set and forget*. He lists it among the antipatterns.

## The core idea

A **pipeline** is the set of stages that turns raw data into a deployed, monitored model: collect, label, clean, train, evaluate, deploy, monitor. **MLOps** is the practice of automating that pipeline so that updating and operating models becomes routine.

Three ideas support it.

**Models change.** Kästner gives four reasons: better features, new versions of the ML library, new data, and **drift**, a change in the real world that makes old data unrepresentative. When the product's own usage produces the new data, he speaks of *closed-loop intelligence*.

**Notebooks are for exploring. Pipelines are for repeating.** A **notebook**, such as a Jupyter notebook, is a file of code cells that you run one at a time, in any order. That is ideal for looking at data. It is unreliable for a job that must give the same result every month, because cells can run out of order on stale state. A pipeline stage is a function with declared inputs and outputs.

**Automation pays for itself in experiments.** A retrain that costs three days of toil happens twice a year. One that costs forty minutes happens every week, and leaves time to try twenty variants.

A pipeline is like a build system: declared steps, each with inputs and outputs, that anyone can trigger. The comparison breaks in one place. A build's inputs are fixed. A pipeline's input, the data, changes under it on every run. "It worked yesterday" says nothing about today.

Three more terms belong here:

- **Continuous integration (CI)** checks every change to the code automatically, as soon as it is pushed: tests and static analysis.
- **Continuous delivery (CD)** keeps every change that passes those checks ready to release through an automated process.
- **Infrastructure as code** describes servers, containers and pipeline steps in files under version control, instead of setting them up by hand.

## How it works, step by step

### The stages

| Stage | What happens | What to automate | What goes wrong |
|---|---|---|---|
| Data collection | Read fresh data from where the product writes it | A scheduled read from the database | A local file that grows stale |
| Labeling | People attach correct answers | A steady queue for annotators | Labels arrive once, then never |
| Cleaning and feature engineering | Remove outliers, fill missing values, encode inputs | The same functions on every run | Bugs that never crash. The model just gets worse |
| Training | Fit the model | One command, with settings and data version logged | A setting changed by hand and forgotten |
| Evaluation | Score the model on **held-out data**, labeled examples that training never saw | A gate: below the minimum, the run stops | Evaluation examples leak into training |
| Deployment | Put the model behind the API | Automatic upload, **canary release**, rollback | A new model overwrites the last good one |
| Monitoring | Watch inputs, outputs and outcomes | Alerts, and a trigger for the next run | Customers find the problems first |

A canary release sends the new model to a small share of the traffic first. If quality drops for those users, the model is rolled back before anyone else receives it.

### From notebook to pipeline

1. **Turn each group of cells into a function** with explicit inputs and outputs, one module per stage.
2. **Make every stage read and write only declared places.** No hidden files.
3. **Test each stage alone against dirty data**: missing values, wrong formats, empty input.
4. **Run the tests on every change.** Pipeline code gets the same gates as any other code: unit tests, integration tests, static analysis, code review.
5. **Describe the order in one place.** Which stages run in sequence, what is retried, who is told when a stage fails. A run can start by hand, on a schedule, or from a monitoring alert.
6. **Deploy automatically, only after the gate passes.** Use a canary and keep the previous model.
7. **Close the loop.** Let monitoring start the next run.

## Worked example

A pipeline of plain functions, tests that feed it dirty data, and a CI file that runs the tests. Everything needs Python 3.10 or newer and nothing else.

```python
# pipeline.py — a training pipeline as plain functions.
from datetime import datetime

TEAMS = ("billing", "technical", "other")
MIN_TRAINING_ROWS, MIN_EVAL_ROWS = 500, 100

def collect(from_db):                 # stage 1: read the evolving data set
    """from_db() returns rows like {'subject': str, 'created_at': str, 'team': str}."""
    return from_db()

def clean(rows):                      # stage 2: validate and normalize
    cleaned = []
    for row in rows:
        subject = str(row["subject"] or "").strip()
        created = datetime.fromisoformat(row["created_at"])   # raises on a bad format
        if subject and row["team"] in TEAMS:
            cleaned.append({"subject": subject.lower()[:2000], "created_at": created})
    return cleaned

def train(rows):                      # stage 3: stand-in for model training
    assert len(rows) >= MIN_TRAINING_ROWS, f"only {len(rows)} rows to train on"
    return {"trained_on": len(rows)}

def evaluate(model, held_out):        # stage 4: the gate before any deployment
    """Stand-in: a real gate scores the model on held-out labeled tickets."""
    return len(held_out) >= MIN_EVAL_ROWS

def run(from_db, held_out):           # the order of the stages lives here
    return evaluate(train(clean(collect(from_db))), held_out)
```

```python
# test_pipeline.py — run with: python test_pipeline.py
from pipeline import clean, run

def row(subject="Invoice please", created_at="2026-11-02T09:14:00", team="billing"):
    return {"subject": subject, "created_at": created_at, "team": team}

def test_drops_rows_without_a_subject():
    assert clean([row(subject="   "), row()]) == clean([row()])

def test_refuses_a_timestamp_it_cannot_parse():
    try:
        clean([row(created_at="02/11/2026")])
    except ValueError:
        return
    raise AssertionError("a bad timestamp was accepted silently")

def test_gate_refuses_a_tiny_evaluation_set():
    rows = [row() for _ in range(600)]
    assert run(lambda: rows, held_out=[]) is False

def test_pipeline_runs_end_to_end():
    rows = [row() for _ in range(600)]
    assert run(lambda: rows, held_out=[1] * 100) is True

if __name__ == "__main__":
    for name, obj in sorted(globals().items()):
        if name.startswith("test_"):
            obj()
            print("ok", name)
```

Run `python test_pipeline.py`. Four `ok` lines follow. To run them on every push, add this file to a GitHub repository (action versions as of 2026-11; check the current ones):

```yaml
# .github/workflows/ci.yml — run the pipeline tests on every push
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python test_pipeline.py
```

What to observe:

- **Each stage is a function.** It takes inputs, returns outputs and can be tested alone.
- **The gate is code.** No model leaves this pipeline on an evaluation set of twenty examples, however hurried someone is.
- **The tests use dirty data.** A blank subject, a timestamp in the wrong format, an empty evaluation set.
- **The order lives in `run`.** Three lines say what runs after what. The opposite is a collection of scripts whose order exists only in one person's memory.
- **The timestamp test asks for a loud failure.** A cleaning bug usually does not crash. The model simply learns from damaged data. Write tests that turn silent errors into visible ones.

### What changes for LLM and agent systems

If you do not fine-tune, the pipeline has no training stage. It still has a pipeline, and it still needs automation.

- **The chain is shorter.** Change the prompt, the model version or the retrieved documents. Run the evaluation set. Pass a gate. Deploy to a canary. Monitor. Each link is a stage with an owner.
- **The evaluation set is the test suite.** It runs on every change to a prompt or a model setting, in CI, as these tests run on every push: [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md).
- **Evaluation calls a paid API.** As an illustration, run a sample of fifty examples on every change and the full set before a release.
- **Prompts and settings are pipeline code.** Version them. Record which prompt, which model version and which document index produced each deployment.
- **The loop closes through logs.** Disliked answers and user edits become new evaluation examples. That is how a system without training still learns.

For an agent, infrastructure as code covers the tool definitions, the sandbox configuration and the scopes of the credentials. Each of those is a file that goes through review like any other source file. Running experiments safely on live traffic is the subject of [Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md).

## What the practitioners say

- **Train once and forget is an antipattern.** Kästner opens chapter 11 with it. A production model must be updated, and automation is what makes updates routine.
- **Bad pipelines have names.** He uses *pipeline jungles* and the *big-ass script architecture* for pipelines whose steps are ad hoc scripts, and *undeclared consumers* for scripts that depend on files nobody remembers creating. His summary adds *dead experimental paths* ([chapter 11](https://mlip-cmu.github.io/book/11-automating-the-pipeline.html)).
- **The step from notebook to pipeline is hard.** He cites experience reports: organizations struggle to turn exploratory code into pipelines that re-execute, take new data unchanged and run on a schedule. It takes an engineering stance, new infrastructure and a learning curve, and it may not pay off in the short term.
- **Cleaning bugs hide.** Researchers have found subtle bugs in data transformations. They are hard to notice because the code does not crash. The model only becomes less accurate.
- **Labeling is a process, not an event.** His example of labeling inside another task is a security check that asks users to transcribe hard-to-read words.
- **Monitoring can start the pipeline.** A system that notices poor estimates for one region can trigger a retraining run or alert the data scientists.

## Pitfalls

1. **Leaving the model as it shipped.** Fix: a scheduled retrain and a monitor that can trigger one.
2. **Running cells by hand for each release.** Fix: one function per stage and one place that states the order.
3. **Testing only the training step.** Fix: dirty-data tests for cleaning and encoding, where bugs hide.
4. **A deployment without a gate.** Fix: evaluation as code, and a canary before full rollout.
5. **Files nobody declared.** Fix: each stage reads and writes only what is declared.
6. **Holding pipeline code to a lower standard.** Fix: the same reviews, static analysis and CI as the rest of the system.
7. **Automating before the design is stable.** Fix: automate the stages that repeat, and keep experiments in notebooks until they settle.

## Try it

Take one model that is retrained by hand. Build its pipeline.

Include:

1. A stage table: seven stages, what each reads and writes.
2. A function for each stage that exists in your case.
3. At least four dirty-data tests for the cleaning stage.
4. One gate that can stop a deployment.
5. A CI file that runs the tests on every change.

**You are done when** a colleague can produce a new model with one command from a clean checkout, and the gate refuses to deploy on your test input.

**Stretch goal:** make the gate compare the new model with the currently deployed one and refuse any candidate that scores lower.

## Key takeaways

- A production model changes. A pipeline of automated stages is how it changes safely.
- Notebooks explore. Functions with declared inputs and outputs repeat.
- Bugs in cleaning and encoding rarely crash. Test them with dirty data.
- The evaluation gate, the canary and the rollback turn deployment from an event into a routine.
- CI, CD and infrastructure as code apply to pipelines as much as to any other software.

## Self-check

1. Name the seven pipeline stages in order.
2. What is a canary release?
   - A. A release that is announced to users before it is deployed.
   - B. A release to a small share of traffic first, rolled back if quality drops.
   - C. A release that is installed on a staging server and never reaches users.
   - D. A release in which two model versions answer every request together.
3. Why does a bug in a data-cleaning step often go unnoticed, and what kind of test catches it?
4. A script in the pipeline reads a file that nobody remembers creating. Which antipattern is this, and what is the fix?
   - A. Set and forget: retrain the model on a fixed schedule instead of once.
   - B. Dead experimental path: delete every branch that is not on the main path.
   - C. Undeclared consumer: let each stage read only what an earlier stage declares as its output.
   - D. Pipeline jungle: split the code into more scripts with shorter names.
5. Define continuous integration and name one thing it adds to an ML pipeline.
6. What are the three things that can start a pipeline run?

<details><summary>Show answers</summary>

1. Data collection, labeling, cleaning and feature engineering, training, evaluation, deployment, monitoring.
2. B. It limits the users who receive a bad model to a small group and makes rollback quick.
3. The cleaning code keeps running and the model still trains. It only learns from damaged data and becomes less accurate. A test that feeds a malformed row and expects either a loud error or the documented output catches it.
4. C. The stage depends on data whose origin is not written down. Declaring inputs and outputs for every stage removes the problem.
5. Every change to the code is checked automatically as soon as it is pushed. For an ML pipeline it adds a check on every change to cleaning code, settings and gates, before a model is ever built from them.
6. A person, a schedule, or a monitoring alert.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 11: [Automating the Pipeline](https://mlip-cmu.github.io/book/11-automating-the-pipeline.html)
- **Reading:** Katie O'Leary and Makoto Uchida, "Common Problems with Creating Machine Learning Pipelines from Existing Code" (MLSys 2020), cited in chapter 11.

## Next

→ [Scaling the System](09-scaling-the-system.md), because an automated pipeline and a popular model both grow until one machine is no longer enough.
