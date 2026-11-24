# 09. Scaling the System

**Level:** Practitioner · **Reading time:** 15 min · **Exercise:** 45 min
**Prerequisites:** [Deploying a Model](07-deploying-a-model.md), where inference appears as a function without state.

> **In one sentence:** After this chapter you can tell which parts of an ML feature need to scale, do the arithmetic that shows by how much, and name the standard building blocks for each part.

## Why this matters

The head of support asks: "Can triage handle ten times the volume?"

The honest answer needs arithmetic, not a purchase order. Ten times 50,000 tickets a day is still under six requests a second at peak. One copy of the classifier handles that.

The same question about the LLM version has a different answer. Each request holds an accelerator chip for about a second. This chapter shows how to reach both answers with numbers.

## The core idea

**Scalability** is the ability of a system to handle more work when you give it more resources.

Kästner gives three ways to get capacity (chapter 12): use a more efficient algorithm, use a faster machine, or use more machines. The first two work for a while. Then they grow expensive and hit physical limits. Real scalability almost always comes from the third: **distribution**, splitting storage and computation across many machines.

A kitchen with one cook who cannot keep up has the same three answers: a better recipe, a faster cook, more cooks. The comparison breaks at coordination. Cooks see each other and talk. Machines coordinate over a network that is slow and that can fail without a visible sign. So "more machines" costs design as well as money.

### Where ML features need scale

Kästner names four places:

| Where | What grows | What you need |
|---|---|---|
| Training data | Rows to store, clean and encode | Distributed storage and data processing |
| Telemetry | Logged predictions and outcomes | Distributed storage and data processing |
| Inference | Requests per second, each holding hardware | Many copies of a stateless service behind a load balancer |
| Training | Days of accelerator time for one job | Splitting one job across machines |

For scale, his reference point is Google Photos, which reported in 2020 that it held more than 4 trillion photos for over a billion users and received 28 billion new photos a week, about 46 thousand uploads a second. You will probably never need that. The ideas are the same at any size.

### The building blocks to recognize

**Storage.** The book names three common forms of data: relational data, in tables with a fixed shape that you query in SQL; document data; and unstructured data. Two ideas distribute any of them:

- **Partitioning** splits the data, so that different parts sit on different machines.
- **Replication** stores the same data on several machines, so that one can fail.

<!-- SOURCE GAP: the copy of book chapter 12 used here was trimmed. The sections on document and unstructured storage, on data encoding and on partitioning details, and the definitions of data warehouse and data lake were not available. -->

**Processing.** Four strategies cover most needs:

| Strategy | How it works | Optimized for | Example |
|---|---|---|---|
| Service | Answers each request as it arrives | Low response time | The triage inference service |
| Batch | Runs one long computation over all the data and writes the results | Throughput | The nightly training run |
| Stream | Processes events from a queue as they arrive | Throughput with little delay | Scoring each new comment within seconds |
| Lambda architecture | Batch recomputes everything on a schedule. Stream keeps the results fresh in between. Services answer queries | Both | A weekly full retrain, with small updates between runs |

**Training.** Training a large model is a distributed job in its own right. For GPT-3, released in 2020, Kästner reports an estimate of 355 years of sequential training, done instead on a cluster with 285,000 CPU cores and 10,000 GPUs, at an estimated cost of nearly 5 million US dollars for one run.

**Caching.** A **cache** keeps the result of an expensive computation and reuses it. Three caches are common in ML features: predictions for inputs that repeat ([chapter 07](07-deploying-a-model.md)), feature vectors (the feature store in the same chapter), and upstream results such as the numerical form of a stored document. A cache goes stale the moment the model changes. So every cache needs an invalidation rule, such as the model version in the cache key.

## How it works, step by step

**Capacity planning** is estimating the load, the cost per unit and the needed resources before you build.

1. **Write the load**: the average and the peak, per second.
2. **Measure the cost of one unit** on one copy: requests per second, memory, bytes per logged event.
3. **Multiply into budgets** for compute, storage and network.
4. **Find the bottleneck.** Kästner notes that it is often the database.
5. **Take the cheap options first**: a more efficient model, a faster machine, a cache.
6. **Distribute what is left.** Services without state scale by adding copies. Data scales by partitioning and replication. Big jobs scale through batch or stream processing.
7. **Leave the door open.** Even if you delay the infrastructure, design so that machines can be added later.

## Worked example

The script needs Python 3.10 or newer and nothing else.

```python
# capacity.py — back-of-envelope load for the triage feature
import math

TICKETS_PER_DAY, PEAK_FACTOR = 50_000, 10
PEAK_PER_SECOND = TICKETS_PER_DAY / 86_400 * PEAK_FACTOR   # 86,400 seconds per day
BYTES_PER_LOGGED_REQUEST = 2_000

for name, capacity in [("classifier", 100), ("LLM", 1)]:   # requests per second per copy
    copies = math.ceil(PEAK_PER_SECOND / capacity)
    print(f"{name:10} needs {copies} instance(s) at peak ({PEAK_PER_SECOND:.1f} req/s)")
print(f"telemetry: {TICKETS_PER_DAY * BYTES_PER_LOGGED_REQUEST / 1e9:.2f} GB per day")
```

Run `python capacity.py`. The output:

```
classifier needs 1 instance(s) at peak (5.8 req/s)
LLM        needs 6 instance(s) at peak (5.8 req/s)
telemetry: 0.10 GB per day
```

What to observe:

- **The classifier needs one instance.** Nothing in this feature needs a distributed system. Run a second copy so that a failure does not stop routing, not for the load.
- **Swapping in the LLM changes the problem.** Six copies at peak, each holding an accelerator. That is a cost created by a model choice ([chapter 06](06-quality-attributes-of-ml-components.md)), not by growth.
- **Telemetry is small.** A tenth of a gigabyte a day is about 37 gigabytes a year. One machine stores it.
- **Two numbers carry the result.** The peak load and the capacity of one copy. Both should come from measurements. Here they are guesses, and a wrong peak factor changes every line.

### What changes for LLM and agent systems

LLM inference is the scaling problem most teams now meet.

- **Throughput comes from batching.** One request is slow. A serving stack that packs many requests onto one copy raises throughput several times over: [Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) and [Parallelism](../10-llm-internals/06-parallelism.md).
- **Copies start slowly.** Loading a large model's weights into memory takes far longer than starting a web server. As of 2026-11 that is often tens of seconds or more for open models of a few billion parameters. Scaling on demand means waiting for that load.
- **A provider's API moves the problem.** Scaling becomes the provider's job, and rate limits become yours. A **rate limit** is the maximum number of requests or tokens per minute that a provider allows. Treat a "429 Too Many Requests" reply as a normal event: queue the request and retry with increasing waits. Put an alert on cost, because a prompt change can double it.
- **New data grows.** A retrieval index is one more store to partition and replicate. Logs of prompts and answers are far larger than prediction logs, so sample them.

For an **agent**, one task can last minutes and make dozens of model calls. A single request that waits for an answer no longer fits. Put tasks in a queue, let a worker handle each one, and keep state so that an interrupted task resumes. Cap the steps and the spending per run. A loop in an agent is a scaling incident. The structure is in [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md).

## What the practitioners say

- **Scaling knowledge is not specific to ML.** Kästner's stated goal for chapter 12 is a working knowledge of the concepts and their trade-offs, enough to choose among existing infrastructure. Teams almost always build on existing abstractions instead of writing their own.
- **Use all three options, in order.** Better algorithms and faster machines help first. Distribution carries the rest.
- **Distribution happens for two reasons.** Systems need it for scale, and also because the application runs on distributed hardware such as phones.
- **Planning varies.** Some teams estimate workloads and simulate designs, with queueing theory. More build on scalable infrastructure and deal with scale when it arrives. Kästner accepts that this can be prudent technical debt.
- **Distribution has a price.** His summary is that distributed systems bring substantial engineering challenges, and that knowing the basic concepts is what lets a team choose well.

## Pitfalls

1. **Scaling before measuring.** Fix: the load and the capacity of one copy, written down.
2. **Scaling the whole system for one bottleneck.** Fix: find the slow part and scale that.
3. **A cache without an invalidation rule.** Fix: the model version in the cache key.
4. **A design that cannot add machines later.** Fix: keep components stateless where you can, even before you need copies.
5. **Forgetting that telemetry grows.** Fix: bytes per event, times events per day, times retention.

## Try it

Write a one-page capacity note for one feature that contains a model.

Include:

1. The average and peak load, per second.
2. The capacity of one copy: requests per second and memory.
3. The three budgets: compute, storage, network.
4. The bottleneck.
5. The first thing you would change if the load grew tenfold.

**You are done when** every number is either a measurement with its source or a guess labeled as one, and the note says whether the feature needs more than one machine.

**Stretch goal:** find one expensive computation in the feature that a cache could remove, and write the cache's invalidation rule.

## Key takeaways

- Three ways to get capacity: a better algorithm, a faster machine, more machines. Only the last one scales without limit.
- ML features need scale in four places: training data, telemetry, inference and training.
- Partitioning splits data. Replication copies it. Services, batch, streams and the lambda architecture process it.
- Capacity planning is arithmetic: the load, times the cost per unit, against the capacity of one copy.
- A cache removes load and creates staleness. Every cache needs an invalidation rule.

## Self-check

1. Name the three ways to get more capacity, and say why the third is usually the real answer.
2. How do partitioning and replication differ?
   - A. Partitioning copies data to several machines, while replication splits it across them.
   - B. Partitioning splits data across machines, while replication copies it to several of them.
   - C. Partitioning speeds up reads, while replication speeds up writes.
   - D. Partitioning applies to training data, while replication applies to telemetry.
3. Which processing strategy answers each request as it arrives, and which is built for throughput over a large snapshot of data?
4. A cache returns an answer that was computed with last week's model. What was left out?
5. A feature peaks at 8 requests a second, and one copy handles 40. How many copies do you run, and why might the answer be two?

<details><summary>Show answers</summary>

1. A more efficient algorithm, a faster machine, more machines. The first two grow expensive and hit physical limits. Adding machines has no such ceiling.
2. B. Partitioning divides the data so that different parts sit on different machines. Replication stores the same data on several machines so that one can fail.
3. A service answers each request as it arrives. Batch processing is built for throughput over a large snapshot.
4. An invalidation rule. The cache key must include the model version, or the cache must be cleared whenever the model changes.
5. One copy covers the load. Two cover the failure of one copy.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 12: [Scaling the System](https://mlip-cmu.github.io/book/12-scaling-the-system.html)
- **Reading:** Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017), recommended in chapter 12 for the principles behind these building blocks.

## Next

→ [Planning for Operations](10-planning-for-operations.md), because a system built to scale still needs someone to watch it, and to know what to do at three in the morning.
