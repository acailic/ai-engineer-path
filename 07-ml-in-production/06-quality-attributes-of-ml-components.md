# 06. Quality Attributes of ML Components

**Level:** Practitioner · **Reading time:** 25 min · **Exercise:** 60 min
**Prerequisites:** [Architecture for ML Systems](05-architecture-for-ml-systems.md) and, for measures, [Goals and Requirements](03-goals-and-requirements.md).

> **In one sentence:** After this chapter you can write down the qualities an ML component must have, find the candidate designs that are worth discussing, and lead the trade-off talk between the teams that own the system.

## Why this matters

Five designs for ticket routing, measured on the same labeled tickets. The numbers are illustrative.

| Design | Error rate | Cost per 1,000 tickets | p95 latency |
|---|---|---|---|
| Keyword rule | 17 percent | $0.00 | 1 ms |
| Small classifier | 8 percent | $0.01 | 12 ms |
| Small LLM | 5 percent | $1.20 | 900 ms |
| Large LLM | 4 percent | $9.00 | 2,400 ms |

Four people look at the table and pick four winners.

- The data scientist picks the large LLM. Lowest error.
- The product manager picks the small LLM. Under one second.
- The finance owner vetoes both. At 50,000 tickets a day, the large LLM costs $450 a day.
- The engineer picks the classifier.

Each person read one column. This chapter is about reading the whole table.

## The core idea

A **quality attribute** is a measurable quality of a component: its latency, its cost, its accuracy, its robustness. Kästner uses this software-engineering term for ML components too (chapter 9). He notes that data scientists say "model properties" and operators say "service-level objectives" for much the same idea.

Two rules follow.

**System qualities become component qualities.** Kästner's example is a fraud-detection service that has to follow new fraud patterns within days. That is a system quality. A model that takes weeks to retrain cannot serve it, however accurate it is. Training latency, a quality of the component, is then disqualifying.

**No component excels at everything.** So you trade. Kästner's vocabulary for trading makes the argument shorter:

- The **design space** is every combination of choices: algorithm, settings, hardware, extra data.
- A **hard constraint** is a limit you cannot negotiate. It cuts the space. Kästner's examples: fraud detection that must cost under $0.001 per prediction, and video analysis at 25 frames per second, which allows 40 ms per frame.
- A **dominated design** is worse than another design on every quality. Drop it without discussion.
- The remaining designs lie on the **Pareto front**: each is better than the others on at least one quality and worse on at least one. Choosing among them takes negotiation and judgment.

This is like choosing a laptop by screen size, weight, price and battery life. A model that is heavier, dearer and shorter-lived than another is out. What is left is a matter of taste. The comparison breaks in one place. Laptop specifications are published and stable. For an ML component, you must measure every quality yourself, on your own data, and the measurements change as the data changes.

### The attributes of a model

| Attribute | Definition | Example target for the triage model |
|---|---|---|
| Accuracy | Share of correct predictions on held-out data, in the conditions of use | 92 percent on an evaluation set of real tickets |
| Inference latency | Time for one prediction. Report a percentile, because it varies by input | p95 under 100 ms |
| Inference throughput | Predictions per unit of time | 600 per minute at peak |
| Model size | File size of the stored model. It drives memory and download size | A few megabytes |
| Cost per prediction | Operating cost of one prediction, including a share of training | Under $0.001 |
| Determinism | The same input always gives the same output | Yes |
| Calibration | The confidence score matches the real probability of being right | A score of 0.8 is right 8 times in 10 |
| Robustness | Output is stable when the input changes a little | A typo does not change the category |
| Fairness | Accuracy and outcomes are comparable across groups | Error by language |
| Explainability | The model gives useful reasons for an output | A reason code per prediction |
| Privacy | Training examples cannot be recovered from the model | Customer text stays out of third-party data |

Kästner separates **interpretability**, whether a person can understand a model's internals, from explainability, whether the model can give reasons for one output. A small decision tree has the first and usually the second. A large neural network has neither by default.

Model size is easy to underestimate. The book's example: a small three-layer network for 28 by 28 pixel images has 266,610 parameters and takes about 1 megabyte at 4 bytes each. GPT-3, an LLM released in 2020, had about 175 billion weights and needed about 700 gigabytes of memory.

### The attributes of the learning process

When a model is retrained regularly, the qualities of training matter as much as the qualities of the model.

| Attribute | Definition | Why it matters |
|---|---|---|
| Training latency | Time to train or retrain the model | Sets how fast you can follow change |
| Incremental training | The model can learn from new data without starting over | Cuts the cost of retraining |
| Reproducibility | The same data and settings produce the same model | Debugging and audits |
| Deployment latency | Time from a finished model to a served model | Sets how fast a fix reaches users |
| Observability | How well you can see what the component does in production | Finds drift and silent bugs |

### Changeability and the feedback loop

These five attributes decide one thing: how long the feedback loop takes. The loop runs from a wrong prediction in production, through the logged correction, to a retrained model that is deployed. Every attribute above is one segment of that loop.

Kästner notes two facts that shape the loop. Standard decision-tree training must look at all the data at once, so it restarts from scratch when the data changes. Neural networks can be trained incrementally. On reproducibility, the picture flips. Deep networks are nondeterministic in training and can reach noticeably different accuracy with identical settings, whereas a basic decision tree reproduces itself exactly.

## How it works, step by step

This procedure turns the opening table into a decision.

1. **Write the system quality requirements**, with numbers, as in [chapter 03](03-goals-and-requirements.md).
2. **Derive a target for each ML component** for each quality that matters. Include a minimum accuracy and the baseline it must beat.
3. **Mark the hard constraints.**
4. **Measure every candidate** on the same data, under the same load.
5. **Drop what violates a constraint. Then drop what is dominated.**
6. **Argue only about the Pareto front**, with the people who own each quality. Write the outcome down as a contract between teams.

## Worked example

The script needs Python 3.10 or newer and nothing else.

```python
# pareto.py — find the designs worth arguing about.
# (name, error rate, cost per 1,000 predictions in USD, p95 latency in ms)
CANDIDATES = [
    ("keyword rule",     0.17, 0.00,    1),
    ("old classifier",   0.09, 0.03,   25),
    ("small classifier", 0.08, 0.01,   12),
    ("small LLM",        0.05, 1.20,  900),
    ("large LLM",        0.04, 9.00, 2400),
    ("LLM + reranker",   0.05, 4.50, 3100),
]
MAX_COST, MAX_P95_MS = 2.00, 1000            # hard constraints

def dominates(a, b):
    """a dominates b: a is no worse on every quality and better on one."""
    return all(x <= y for x, y in zip(a[1:], b[1:])) and a[1:] != b[1:]

feasible = [c for c in CANDIDATES if c[2] <= MAX_COST and c[3] <= MAX_P95_MS]
pareto = [c for c in feasible
          if not any(dominates(o, c) for o in feasible if o is not c)]

for c in CANDIDATES:
    if c not in feasible:
        print(f"dropped {c[0]}: violates a hard constraint")
    elif c not in pareto:
        print(f"dropped {c[0]}: dominated by another design")
print("--- Pareto front ---")
for name, err, cost, p95 in sorted(pareto, key=lambda c: c[1]):
    print(f"{name:18} error {err:.0%}  cost ${cost:.2f}  p95 {p95} ms")
```

Run `python pareto.py`. The output:

```
dropped old classifier: dominated by another design
dropped large LLM: violates a hard constraint
dropped LLM + reranker: violates a hard constraint
--- Pareto front ---
small LLM          error 5%  cost $1.20  p95 900 ms
small classifier   error 8%  cost $0.01  p95 12 ms
keyword rule       error 17%  cost $0.00  p95 1 ms
```

What to observe:

- **The hard constraints removed the most accurate design.** The large LLM is never discussed. Nobody needs to defend that choice.
- **The old classifier left without an argument.** The small classifier is better on all three qualities.
- **The keyword rule survived.** It is not dominated, because nothing is cheaper. Whether a 17 percent error rate clears the minimum from step 2 is a separate question. That is the ladder from [chapter 02](02-when-to-use-ml-and-when-not-to.md).
- **The real argument is the last two rows.** Going from the small classifier to the small LLM cuts the error rate from 8 to 5 percent. It multiplies the cost by 120 and the latency by 75. At 50,000 tickets a day, the LLM costs $60 a day and avoids 1,500 misroutes. Is one avoided misroute worth four cents? That is a question for the support lead and the finance owner, not for the model.

### What changes for LLM and agent systems

The attributes stay. The way you measure them changes.

**Accuracy** has no single form for generated text, because many outputs are acceptable. You grade outputs with a rubric, by hand or with a model acting as a judge: [LLM as a Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md).

**Latency** splits in two: the time until the first token appears, and the total time. Total time grows with the length of the answer. Throughput depends on how the model is served: batching requests and shrinking the model with quantization: [Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) and [Quantization](../09-efficient-deep-learning/04-quantization.md).

**Cost** is priced per token and changes often. Measure it; do not copy it from a blog post.

**Determinism** is off by default, because the model samples its words. Setting the sampling temperature to zero makes a model close to deterministic for short answers. It is not a guarantee.

**Explainability** needs care. The reasons an LLM writes are generated text. They may not reflect what produced the answer, so do not show them to users as facts.

**Changeability** works differently. You rarely retrain. You change the prompt, the model version or the retrieved documents. A provider can also retire a model you depend on, so a migration path and a regression evaluation set are part of the design.

For an **agent**, per-step qualities multiply. If each of five steps succeeds 95 percent of the time, the whole task succeeds about 77 percent of the time. Each step also adds its own latency and cost. Measure the end-to-end task, not only the steps: [Planning, Search and Decision Making](../02-building-agents/03-planning-search-and-decision-making.md).

## What the practitioners say

- **Cost per prediction includes training.** Kästner warns that training cost can dominate when predictions are few or retraining is frequent. For scale, he cites an estimate that one training run of GPT-3 cost between 4 and 12 million US dollars, about 355 GPU-years ([chapter 9](https://mlip-cmu.github.io/book/09-quality-attributes-of-ml-components.html)).
- **Inference cost can sink a product.** The book quotes a press report that Microsoft was losing, on average, $20 per user per month on its $10 GitHub Copilot subscription. Treat it as a report, not an audited figure.
- **Accuracy gains are often not worth the engineering effort.** He quotes Netflix's engineers on the winning entries of its recommendation contest: the extra accuracy did not justify the work of running them in production. He adds that many organizations now choose smaller, faster LLMs for the same reason.
- **Trade-offs cross team boundaries.** His examples: will the front-end team accept less explainability for more accuracy? Will engineers accept a less accurate model if it is calibrated? Can operations retrain daily and still leave room for experiments?
- **Write the contract.** He argues that quality requirements for each component should be documented as an agreement between teams, to be renegotiated when one team cannot deliver.

Kästner's checklist for an ML component, paraphrased from chapter 9: set a minimum accuracy and a baseline; estimate the prediction volume, the latency need and the cost budget; know what data exists, in quantity, quality, format and origin; know how often the model must change and what the training budget is; state explainability needs; name the protected groups and fairness concerns; state the security, privacy and legal constraints.

## Pitfalls

1. **Optimizing one column.** Fix: put every quality in one table before anyone picks.
2. **Reporting average latency.** Fix: a percentile, such as p95, under a stated load.
3. **Comparing candidates on different data.** Fix: one evaluation set and one load for all.
4. **Using confidence without checking calibration.** Fix: measure how often each confidence level is right.
5. **Leaving training cost out.** Fix: spread training and experimentation over the predicted volume.
6. **Treating a measurement as permanent.** Every attribute depends on the algorithm, the settings and the data. Fix: re-measure on each model change.
7. **Keeping the trade-off in one person's head.** Fix: write the contract between teams.

## Try it

Fill in a quality table for one ML component.

Include:

1. The system quality requirements it must support, with numbers.
2. At least six attributes for the component, each with a target and a way to measure it.
3. The hard constraints, marked.
4. At least three candidate designs, measured on the same data.
5. The candidates you dropped, each with the design that dominates it or the constraint it violates.

**You are done when** a colleague can reproduce your table from the note and can tell, for each remaining candidate, which quality it wins on.

**Stretch goal:** run the script on your own numbers and write the one question that would settle the choice on the Pareto front.

## Key takeaways

- A quality attribute is a measurable quality of a component. Accuracy is one of many.
- System qualities become component targets. A model that cannot retrain fast enough is unfit, however accurate.
- Hard constraints cut the design space. Dominated designs leave without discussion. The Pareto front is where the real argument happens.
- Measure every candidate yourself, on the same data, and measure again when the data changes.
- Latency, training time, deployment time and observability together decide how fast the feedback loop runs.

## Self-check

1. Name four quality attributes of a model other than accuracy, with one line of definition each.
2. Design A: error 6 percent, cost $0.04, p95 30 ms. Design B: error 9 percent, cost $0.03, p95 25 ms. Which statement is right?
   - A. A dominates B, because its lower error outweighs the other differences.
   - B. Neither dominates the other, because each is better on at least one quality.
   - C. B dominates A, because it is cheaper and faster on the same data.
   - D. Both are dominated by any design that reaches a lower error rate.
3. What is a hard constraint, and what does it do to the design space?
4. Why does cost per prediction include a share of the training cost, and when does that share dominate?
5. A fraud model has the best accuracy and needs three weeks to retrain. Which attribute makes it unfit, and why?
6. What does it mean for a model to be calibrated, and which rule from chapter 01 depends on it?

<details><summary>Show answers</summary>

1. Any four with a definition, for example: inference latency, the time for one prediction; cost per prediction, the operating cost of one prediction including training; robustness, stability of output under small input changes; calibration, agreement between confidence and real accuracy.
2. B. A wins on error. B wins on cost and latency. Neither is worse on everything.
3. A limit that cannot be negotiated, such as 40 ms per frame at 25 frames per second. It removes every design that violates it from consideration.
4. Training and experimentation have to be paid from the predictions the model makes. The share dominates when the volume of predictions is low or the model is retrained often.
5. Training latency. The system must follow new fraud patterns within days, and this component cannot deliver a new model in less than three weeks.
6. It means that predictions made with confidence 0.8 are right about 80 percent of the time. The rule "act only when confidence is at least 0.8" assumes exactly that.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 9: [Quality Attributes of ML Components](https://mlip-cmu.github.io/book/09-quality-attributes-of-ml-components.html)
- **Reading:** Valliappa Lakshmanan, Sara Robinson and Michael Munn, *Machine Learning Design Patterns* (O'Reilly, 2020), recommended in the neighboring chapters for two-phase prediction and related patterns.

## Next

→ [Deploying a Model](07-deploying-a-model.md), which turns the latency and cost targets into a choice about where the model runs and how it is updated.
