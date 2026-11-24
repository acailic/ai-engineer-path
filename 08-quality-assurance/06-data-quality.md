# 06. Data Quality

**Level:** Practitioner · **Reading time:** 30 min · **Exercise:** 60 min
**Prerequisites:** [Measuring Model Quality](02-measuring-model-quality.md)

> **In one sentence:** After this chapter you can write data tests for the inputs of a model-based feature, tell a hard schema failure from a soft plausibility warning, and set up guards that notice when the data drifts.

## Why this matters

The triage model's accuracy slides from 91 percent to 84 percent over six weeks. Nobody touched the code. Nobody touched the prompt.

Three things changed in the data. A product launch brought tickets full of words the model had rarely seen. The warehouse started storing open tickets with a closing date of year 9999. And a new sign-up form made "en" the default language for everyone.

Nothing crashed. A data bug has no stack trace. The model simply learned from, and reasoned over, the wrong thing, and the dashboard moved a little each week.

## The core idea

**Data quality** is fitness for use: can the model and the operators rely on this data for their job? Two kinds of checks protect it.

A **schema** describes the structure you expect: which fields exist, their types, allowed values, and constraints between them. A schema check is binary. Data either conforms or it does not. Kästner calls conformance to a schema **data integrity** (chapter 16).

Everything else is a judgment of **plausibility**. Is a refund of four million euros possible? Is it likely? No general method can tell whether data truly reflects the world (chapter 16). Plausibility checks flag what looks wrong.

The analogy is a type checker and a linter. Type errors stop the build. Linter warnings are heuristics that need judgment. The analogy breaks at the fix: you can silence a linter without harm, while a data warning ignored means the model trains or predicts on garbage.

Kästner's running example is inventory software for a supermarket. He lists five criteria for judging data (chapter 16). The table gives each one with its supermarket example and a ticket example, and adds a sixth, precision, because he warns separately about random noise.

| Criterion | Question | Supermarket example | Triage example |
|---|---|---|---|
| Accuracy | Was the value recorded correctly? | The wrong number of items for a shipment | The label differs from what an agent would choose |
| Completeness | Was everything relevant recorded? | A whole shipment is forgotten | An open ticket has no closing date |
| Uniqueness | Is each entry recorded once? | The same shipment is entered twice | The same message is imported twice |
| Consistency | Does the data agree with itself? | Two tables hold different prices for one item | A ticket closes before it was created |
| Currentness | Is the data kept up to date? | A delivery is entered a day late | Yesterday's tickets arrive today |
| Precision | How noisy are the values? | A scale that jitters at every weighing | Timestamps rounded to the day |

Later problems cost more. Data-quality problems barely show in offline accuracy scores, and the later one is found, the more it costs to fix, because faulty assumptions are already built into the system (chapter 16).

## How it works, step by step

### 1. Look at the data before checking it

**Exploratory data analysis** means plotting and summarizing the data to learn its shape: types, ranges, distributions, relationships. You cannot write a check for a value you have never seen.

### 2. Write the schema

Turn what you learned into hard rules. Fail loudly on violations. Kästner names **Great Expectations** as a popular library for schema-style checks on data frames, and formats such as Protocol Buffers, Apache Avro and Apache Parquet, which combine schema enforcement with explicit schema versions, so that a change between a producer and a consumer is detected automatically (chapter 16). Where nobody wants to write a schema, tools can infer one from sample data, which is easier to refine than to start from scratch.

### 3. Add plausibility checks

Kästner describes these as **data linting**: heuristics for suspicious encodings, developed from experience with past problems (chapter 16). His examples of suspicious patterns:

- placeholder values standing in for missing data, such as 999 or the date 1/1/1970;
- numbers or dates stored as strings;
- categories encoded as decimals;
- ambiguous date formats and unknown units;
- duplicates.

A linter earns its keep where no schema exists, or where the schema is wrong or too weak for the use. Not every warning is a real problem, and at the time of writing he knew of lists of common problems and academic prototypes but no broadly adopted data-linting tool (chapter 16).

**Anomaly detection** goes one step further and learns the usual distribution. The book's example is a shipment of 80,000 kg of bananas in a system where weekly sales rarely exceed 2,000 kg (chapter 16). Flagged rows go to a human, or get dropped from training. Tune the checks so that they do not drown reviewers in false alarms.

### 4. Encode your assumptions about change

**Drift** means the data, or your assumptions about it, change over time. If the assumptions are never written down, checked, or monitored, nobody notices. Every form of drift degrades accuracy over time, which monitoring shows as a downward trend that a model update reverses only for a while (chapter 16).

Kästner distinguishes three forms, because they have different causes and different repairs (chapter 16):

| Kind of drift | What changes | Example in the book | How you notice |
|---|---|---|---|
| Data drift, also called covariate shift | The distribution of the inputs | The self-checkout camera meets an heirloom cucumber unlike any in training | Compare current inputs with the training data or with past inputs |
| Concept drift | The right answer for the same input | A fad diet makes cucumbers sell in winter, so the month no longer predicts demand | Inputs look normal while accuracy falls, so this needs labels or telemetry |
| Schema drift | The format, or what a value means | A terminal records kilograms instead of pounds after an update | A sudden rise in ill-formed inputs, or an abrupt change in a distribution |

For tickets: a new product brings new vocabulary (data drift), refunds move to a new queue (concept drift), and the warehouse renames `lang` to `locale` (schema drift). The repairs differ. Data drift calls for fresh training data, and the old data usually stays valid. Concept drift calls for relabeled or newly labeled data. Schema drift is a technical fault between components and is fixed like any other bug.

A guard for each is a test run on every new batch against a reference window. Kästner lists what to watch: the distance between today's inputs and the reference distribution, the number of outliers and low-confidence predictions, the count of ill-formed inputs and automatic repairs, and the number of wrong predictions where it can be observed. He names Evidently as one open-source tool and warns that the hard part is the threshold at which a change deserves a human's attention (chapter 16).

### 5. Fix the data at its source

Cleaning has less leverage than collecting well. According to a 2019 study the book cites, 65 percent of studied teams at a large tech company had some control over how their data was collected and curated (chapter 16). Kästner names three levers: the forms and incentives people use to enter data, what the telemetry records, and how labeling tasks are specified and paid for (chapter 16).

### 6. Document the data

Write down the purpose, the origin, how it was collected, which checks passed, the distribution of subpopulations, and the known limitations. Kästner points to the **datasheets for datasets** template, which asks 57 questions about a data set's motivation, composition, collection, uses, and maintenance, and to data catalogs that index an organization's data sets with their schemas attached (chapter 16).

### 7. For an LLM feature, widen what counts as data

A prompt-based component also consumes retrieved documents, tool outputs, earlier turns of the conversation, and the examples inside the prompt. Each is data. A retrieval index that is stale, or a tool that returns an error message in place of a result, is a data quality bug that looks like a model mistake.

## Worked example

Data tests for a batch of tickets, in `pytest` style with the standard library only. The file runs with no model and no cost.

```python
# tickets.py -- a small batch as it arrives from the warehouse
ROWS = [
    {"id": "t1", "queue": "billing", "lang": "de", "created_at": "2026-11-01T09:00:00",
     "closed_at": "2026-11-01T11:30:00", "body": "Charged twice."},
    {"id": "t2", "queue": "technical", "lang": "en", "created_at": "2026-11-01T09:05:00",
     "closed_at": "9999-12-31", "body": "App crashes."},
    {"id": "t3", "queue": "other", "lang": "en", "created_at": "2026-11-01T09:10:00",
     "closed_at": "2026-11-01T10:00:00", "body": "Charged twice."},
]
```

```python
# test_ticket_data.py
from collections import Counter
from datetime import datetime
from tickets import ROWS

QUEUES = {"billing", "technical", "account", "other"}

# Hard checks: the schema. A failure means the data is unusable.
def test_schema():
    required = {"id", "queue", "lang", "created_at", "closed_at", "body"}
    for row in ROWS:
        assert required <= row.keys(), f"{row.get('id')} lacks {required - row.keys()}"
        datetime.fromisoformat(row["created_at"])  # raises on a bad timestamp

def test_labels_come_from_the_fixed_set():
    bad = [r["id"] for r in ROWS if r["queue"] not in QUEUES]
    assert not bad, f"unknown queue on {bad}"

# Soft checks: plausibility. A failure means "look at this".
def test_no_placeholder_dates():
    faked = [r["id"] for r in ROWS if r["closed_at"].startswith("9999")]
    assert not faked, f"open tickets stored with a fake date: {faked}"

def test_no_duplicate_messages():
    counts = Counter(r["body"] for r in ROWS)
    assert max(counts.values()) == 1, "the same message text appears twice"

# A drift guard: compare this batch with a reference share.
def test_german_share_is_stable():
    share = sum(r["lang"] == "de" for r in ROWS) / len(ROWS)
    assert 0.02 <= share <= 0.10, f"German share is {share:.2f}"
```

What to observe:

- The two schema tests pass. The batch has the right shape.
- `test_no_placeholder_dates` fails on `t2`. An open ticket was stored with a fake future date. A model would learn that tickets close in year 9999.
- `test_no_duplicate_messages` fails on `t1` and `t3`. The text repeats. That may be a double import, or two customers with the same short message. The test cannot tell. It flags, and a person decides.
- `test_german_share_is_stable` fails, because one ticket in three is German in this toy batch. In a real batch, a sudden jump or collapse in a slice's share is an early sign of drift. [Slicing](03-slicing.md) explains why small groups matter.

## What the practitioners say

- **Cleaning eats the job.** According to the reports Kästner cites, data scientists spend more than half their time cleaning data and rarely enjoy it (chapter 16).
- **Noise and bias are different problems.** **Imprecise** data has random noise, which most learning methods tolerate, especially with a lot of data. **Inaccurate** data has a systematic error: a miscalibrated scale that underreports banana sales makes the model order too few bananas. More data does not help if it all has the same bias, and Kästner adds that systematic bias, not noise, is the source of most fairness issues (chapter 16).
- **Most problems are avoidable.** A Google study he cites, titled "Everyone Wants to Do the Model Work, Not the Data Work", found that catching data-quality problems early would have prevented most of them. It also found that data scientists underestimate how messy their data is and tend to assume it will stay stable (chapter 16).
- **Integrity is strict, and it is not enough.** Schema enforcement is well established and covers only format and internal consistency (chapter 16).
- **Beyond the schema, you check plausibility.** His position is that most checks identify suspicious data rather than clear violations (chapter 16).
- **Expected distributions are learned, not written.** Teams learn them from data and then tune detection to surface useful problems (chapter 16).
- **Producers and consumers are strangers.** The people who enter and label data are often separated from the people who use it, and data is rarely documented or managed well (chapter 16).
- **Manage it as a project concern.** Set data-quality requirements early, then check, measure, and monitor against them. He suggests the ISO/IEC 25012 standard for data quality as a checklist (chapter 16).

## Pitfalls

1. **Cleaning forever, fixing nothing.** A script patches the same defect in every batch. Fix: change the form, the exporter, or the labeling instructions at the source.
2. **Stopping at the schema.** Well-formed nonsense passes. Fix: add plausibility checks and drift guards.
3. **Running data tests once.** Data changes, tests do not. Fix: run them on every batch, where the data enters.
4. **Deleting every outlier.** Rare inputs may be your most important ones. Fix: route outliers to review and keep a slice for them.
5. **Trusting labels because they exist.** A label reflects the instructions and conditions of the annotator. Fix: audit a sample, and collect independent labels on a subset.
6. **Treating retrieved text as truth.** Stale or wrong documents make the model wrong. Fix: test the index's freshness and coverage like any other data source.

## Try it

Pick the input data of one component: a table, a retrieved document set, or conversation logs.

1. Explore it. Write five sentences about what you found.
2. Write four schema tests.
3. Write four plausibility tests.
4. Write two drift guards that compare a batch with a reference share.
5. Break a batch on purpose and confirm that a test catches it.

You are done when all ten tests run with one command, when each failing message names the offending rows, and when a deliberately broken batch fails at least one test. **Stretch goal:** trace one failing check back to the form, job, or instruction that produced the bad value, and fix it there.

## Key takeaways

- Schema checks are strict and cheap. They protect structure, not meaning.
- Most data problems are found by plausibility checks: placeholders, duplicates, outliers, and odd distributions. They flag, and a person decides.
- Drift is a change in the data or in your assumptions. Assumptions that are never written down go unnoticed until accuracy falls.
- The most leverage is at the source: how data is entered, recorded, and labeled.
- For an LLM feature, retrieved documents, tool outputs, and conversation history are data too.
- Run data tests on every batch, not once.

## Self-check

1. A batch passes every schema test yet trains a bad model. What kind of problem escaped?
2. A column of open tickets holds the closing date 9999-12-31. Which dimension is hurt, and what should the value be?
3. Refund tickets start going to a new queue after a policy change. Which kind of drift is that?
4. Why fix a data defect at its source rather than in a cleaning script?
5. Why does a duplicate check fail without telling you whether the duplicates are wrong?

<details><summary>Show answers</summary>

1. A problem of meaning: wrong values, mislabeled rows, stale data, or a shifted distribution. The schema checks only structure and internal consistency.
2. Completeness, and consistency as a consequence. The ticket is not closed, so the field should be empty or null, not a fake date.
3. Concept drift. The inputs are the same, and the correct answer for them has changed.
4. The cleaning script must be maintained and run for every batch, while every other consumer of the data still sees the defect. A fix at the source repairs it once, for everyone.
5. A duplicate is a heuristic signal. Repeated text can come from a double import or from two customers writing the same short message, and only a person can tell which.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 16: [link](https://mlip-cmu.github.io/book/16-data-quality.html)

## Next

→ [Pipeline Quality](07-pipeline-quality.md), because the code that moves and transforms this data is ordinary code, and it fails without an error message.
