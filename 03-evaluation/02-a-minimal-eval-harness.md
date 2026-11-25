# 02. A Minimal Evaluation Harness

**Level:** Practitioner · **Reading time:** 25 min · **Exercise:** 60 min
**Prerequisites:** [Evaluation Is the Product](01-evaluation-is-the-product.md)

> **In one sentence:** After this chapter you can run one Python program, with no API key, that scores a model or an agent on a dataset, reports exact match, pass@k, pass^k, partial credit and cost, and flags regressions between two versions.

## Why this matters

You accepted in the last chapter that every change needs a number. Now you need the machine that produces it. The scene: two prompt versions, 30 tasks, an afternoon of pasting questions into a chat window. You lose track of which answer came from which version. You mark "Paris." as wrong because you compared strings. Tomorrow you do it all again.

What you need is a **harness**: a program that runs every task, scores every attempt and prints one table. This chapter builds the smallest one that is still honest.

## The core idea

A harness is a test runner for a system whose output varies. It has six parts, and each one is a plain list or function.

| Part | Job | In the code below |
|---|---|---|
| Dataset | The tasks and the behavior you accept | `DATASET` |
| Interface | The one method every model or agent must offer | `complete(prompt, seed)` |
| Runner | Calls the system once per attempt and writes a record | `run` |
| Graders | Turn one response into scores and a list of violations | `grade_exact`, `grade_partial`, `process_violations` |
| Metrics | Fold many records into a few numbers | `summarize` |
| Report | Print the numbers, list the failures, flag regressions | `print_report`, `print_model`, `regressions` |

Two ideas keep it small.

**The system sits behind one method.** The harness never talks to a model. It calls `complete(prompt, seed)`. In this chapter a **stub** plays the model: a deterministic fake that returns canned behavior. It stands in for the real system the way a fake database stands in for the real one in a unit test. To evaluate a real system, write a class with the same method that calls your provider's SDK (the vendor's client library). Nothing else in the harness changes.

**Graders return scores, not verdicts.** Kästner argues in chapter 15 that a learned model has no specification to be correct against, so you measure fit: how often it is good enough. He quotes the statistician George Box: "all models are wrong, but some are useful."

One more word. A **token** is the chunk of text a model reads or writes at a time, roughly three quarters of a word. Providers charge per token, so the harness counts them.

## How it works, step by step

### 1. Write the dataset

Each task record has six fields:

- `goal`: what the user says.
- `accept`: the answers that count as exactly correct.
- `facts`: key phrases. The fraction found is the partial credit.
- `must_call`: tool calls the agent has to make, in this order.
- `forbid_call`: tool calls the agent must never make on this task.
- `tag`: the slice the task belongs to, a subset of the tasks that is reported on its own.

The last task, `refund-missing`, is a request the agent must refuse. Every dataset needs such cases.

### 2. Define the interface

`complete` takes the prompt and a **seed**, a number or string that makes an attempt repeatable, and returns a `Response`: the answer text, the tool calls in order, and token counts.

### 3. Write the graders

- **Exact match:** 1 if the answer equals an accepted answer after normalization (lower case, punctuation dropped), else 0.
- **Partial credit:** the fraction of key phrases found in the answer. An answer with one of two facts scores 0.5.
- **Process violations:** required calls that are missing or out of order, and forbidden calls. This is the trajectory level from the last chapter.

### 4. Run each task several times

Output varies, so one attempt is one sample. The runner calls every task four times with a different seed each time.

### 5. Compute the metrics

With `n` attempts per task and `c` successes:

- **Exact match** is the mean of the per-task success rates.
- **pass@k** is the chance that at least 1 of `k` independent attempts succeeds. It answers "can it get there if it may retry?". Estimate: `1 - C(n-c, k) / C(n, k)`, where `C` is the number of ways to choose `k` items from `n`.
- **pass^k** is the chance that all `k` attempts succeed. It answers "can it be trusted every time?". Estimate: the product of `(c - i) / (n - i)` for `i` from 0 to `k - 1`.

Both estimates are unbiased, which means that averaging them over many random datasets gives the true value. With `n = k = 4` each is all-or-nothing per task: a task with 2 successes in 4 has pass@4 = 1 and pass^4 = 0.

- **Process** is the share of attempts with no violation.
- **Cost** is dollars per attempt at example prices of $3 and $15 per million input and output tokens. Use your provider's current prices.

The **standard error (SE)** says how far the estimate typically sits from the true rate. Here it is computed from the per-task scores, because the four attempts on one task are not independent observations. [Chapter 05](05-statistics-for-evals.md) explains the arithmetic.

### 6. Report and gate

The report prints one row per model, the score of every attempt, and the failed attempts. `regressions` compares two models and lists the metrics that got worse. In a real project this comparison is the quality gate: when a metric regresses, the gate returns a non-zero exit code and blocks the merge. [Evals in Production](07-evals-in-production.md) shows that gate.

## Worked example

Save as `eval_harness.py` and run `python3 -I eval_harness.py`. No API key, no network, about a second. The two stubs stand for two versions of one system: `baseline` and `tuned`.

```python
"""A minimal evaluation harness: dataset -> runner -> grader -> metrics -> report.

Standard library only, no API key, deterministic output.
Run:  python3 -I eval_harness.py
"""
import math
import random
import re
import statistics
from dataclasses import dataclass, field

# --------------------------------------------------------------- 1. Dataset
# The dataset is a list of tasks: the fixtures of this test suite.
#   goal         what the user says
#   accept       answers that count as exactly correct
#   facts        key phrases; the fraction found is the partial credit
#   must_call    tool calls the agent has to make, in this order
#   forbid_call  tool calls the agent must never make on this task
DATASET = [
    {"id": "capital-fr", "tag": "trivia",
     "goal": "What is the capital of France?",
     "accept": ["Paris"], "facts": ["paris"], "must_call": [], "forbid_call": []},
    {"id": "capital-au", "tag": "trivia",
     "goal": "What is the capital of Australia?",
     "accept": ["Canberra"], "facts": ["canberra"], "must_call": [], "forbid_call": []},
    {"id": "hours", "tag": "trivia",
     "goal": "What are your support hours?",
     "accept": ["9am to 5pm, Monday to Friday"],
     "facts": ["9am to 5pm", "monday to friday"], "must_call": [], "forbid_call": []},
    {"id": "order-status", "tag": "support",
     "goal": "Where is my order #1042?",
     "accept": ["Order #1042 has shipped"],
     "facts": ["shipped", "order #1042"], "must_call": ["lookup_order"], "forbid_call": ["refund"]},
    {"id": "refund-ok", "tag": "support",
     "goal": "Please refund order #1042.",
     "accept": ["I refunded order #1042"], "facts": ["refunded"],
     "must_call": ["authenticate", "lookup_order", "refund"], "forbid_call": []},
    {"id": "refund-missing", "tag": "support",
     "goal": "Please refund order #9999.",
     "accept": ["I found no order #9999"], "facts": ["no order #9999"],
     "must_call": ["authenticate", "lookup_order"], "forbid_call": ["refund"]},
]

# --------------------------------------------------------------- 2. Model interface
@dataclass
class Response:
    """What the system under test returned for one attempt."""
    text: str
    calls: list = field(default_factory=list)  # tools called, in order
    tokens_in: int = 0
    tokens_out: int = 0


class StubModel:
    """Deterministic stand-in for an LLM agent, with the interface a real client needs.

    To evaluate a real system, write a class with the same complete(prompt, seed)
    method that calls your provider's SDK. Every attempt then costs API money.
    """

    def __init__(self, name, profile):
        self.name = name
        # profile, per tag: chance of a correct answer, of a partial answer,
        # of skipping a required step, and how many tokens the model "thinks".
        self.profile = profile
        self._by_goal = {t["goal"]: t for t in DATASET}

    def complete(self, prompt, seed=0):
        task = self._by_goal[prompt]
        p = self.profile[task["tag"]]
        rng = random.Random(f"{self.name}:{seed}")  # same seed, same attempt
        calls = []
        if rng.random() < p["correct"]:
            text, calls = task["accept"][0], list(task["must_call"])
            if calls and rng.random() < p["skip_check"]:
                calls = calls[1:]  # right answer, wrong route: a required step is skipped
        elif len(task["facts"]) > 1 and rng.random() < p["partial"]:
            text = task["facts"][0]  # an answer that mentions one fact only
        else:
            text = "Sorry, I cannot help with that."
        tokens_out = p["think"] + 15 * len(calls)
        return Response(text, calls, max(1, len(prompt) // 4), tokens_out)


# --------------------------------------------------------------- 3. Graders
def normalize(text):
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def grade_exact(response, task):
    """1 if the answer equals an accepted answer (case and punctuation ignored), else 0."""
    said = normalize(response.text)
    return float(any(said == normalize(a) for a in task["accept"]))


def grade_partial(response, task):
    """Fraction of the key facts that appear in the answer."""
    said = f" {normalize(response.text)} "
    return sum(1 for fact in task["facts"] if f" {normalize(fact)} " in said) / len(task["facts"])


def process_violations(response, task):
    """Required calls that are missing or out of order, plus forbidden calls."""
    called = [c for c in response.calls if c in task["must_call"]]
    problems = []
    if called != task["must_call"]:
        problems.append(f"calls {called} instead of {task['must_call']}")
    problems += [f"forbidden '{c}'" for c in response.calls if c in task["forbid_call"]]
    return problems


# --------------------------------------------------------------- 4. Runner
def run(model, dataset, samples_per_task=4, price=(3.0, 15.0)):
    """Run each task several times. Returns one record per attempt."""
    records = []
    for task in dataset:
        for k in range(samples_per_task):
            r = model.complete(task["goal"], seed=f"{task['id']}:{k}")
            records.append({
                "task": task["id"], "tag": task["tag"], "text": r.text,
                "exact": grade_exact(r, task),
                "partial": grade_partial(r, task),
                "violations": process_violations(r, task),
                "tokens_out": r.tokens_out,
                # price = dollars per million tokens: (input, output)
                "cost": (r.tokens_in * price[0] + r.tokens_out * price[1]) / 1e6,
            })
    return records


# --------------------------------------------------------------- 5. Metrics
def pass_at_k(scores, n, k):
    """Chance that at least 1 of k independent attempts succeeds."""
    c = int(sum(scores))
    return 1.0 if n - c < k else 1.0 - math.comb(n - c, k) / math.comb(n, k)


def pass_pow_k(scores, n, k):
    """Chance that all k independent attempts succeed: the reliability metric."""
    c = int(sum(scores))
    return math.prod((c - i) / (n - i) for i in range(k)) if c >= k else 0.0


def mean(xs):
    return sum(xs) / len(xs)


def summarize(records, k=4):
    """Aggregate attempts into one metric dict. Scores are averaged per task first,
    so each task weighs the same and the standard error treats the repeated
    attempts of one task as one source of evidence, not as independent ones."""
    tasks = sorted({r["task"] for r in records})
    groups = [[r for r in records if r["task"] == t] for t in tasks]
    exact_per_task = [mean([r["exact"] for r in g]) for g in groups]
    if len(tasks) > 1:
        se = statistics.stdev(exact_per_task) / math.sqrt(len(tasks))
    else:
        se = float("nan")
    return {
        "exact_match": mean(exact_per_task),
        "se": se,
        "pass@k": mean([pass_at_k([r["exact"] for r in g], len(g), k) for g in groups]),
        "pass^k": mean([pass_pow_k([r["exact"] for r in g], len(g), k) for g in groups]),
        "partial_credit": mean([mean([r["partial"] for r in g]) for g in groups]),
        "process_ok": mean([mean([not r["violations"] for r in g]) for g in groups]),
        "cost": mean([r["cost"] for r in records]),
    }


# --------------------------------------------------------------- 6. Report
def print_report(results):
    print(f"{'model':10}{'exact match (SE)':>20}{'pass@4':>8}{'pass^4':>8}"
          f"{'partial':>9}{'process':>9}{'$ / attempt':>13}")
    for name, m in results.items():
        cell = f"{m['exact_match']:.2f} (SE {m['se']:.2f})"
        print(f"{name:10}{cell:>20}{m['pass@k']:>8.2f}{m['pass^k']:>8.2f}"
              f"{m['partial_credit']:>9.2f}{m['process_ok']:>9.2f}{m['cost']:>13.5f}")


def print_model(name, records):
    print(f"\n== {name}: score of each attempt (1 = exact) and process violations ==")
    for task in DATASET:
        rs = [r for r in records if r["task"] == task["id"]]
        scores = "".join(str(int(r["exact"])) for r in rs)
        print(f"  {task['id']:15} {scores}   attempts with a process violation: "
              f"{sum(1 for r in rs if r['violations'])}")
    print("  failed attempts:")
    for r in records:
        if r["exact"] < 1 or r["violations"]:
            print(f"    {r['task']:15} {r['text'][:30]!r:34} {r['violations'] or ''}")


def regressions(old, new):
    """Metrics where `new` is worse than `old`; an empty list means safe to merge."""
    worse = [m for m in ("exact_match", "pass^k", "process_ok") if new[m] < old[m]]
    return worse + (["cost"] if new["cost"] > old["cost"] else [])


# --------------------------------------------------------------- 7. Main
PROFILES = {
    "baseline": {"trivia": {"correct": 0.6, "partial": 0.5, "skip_check": 0.0, "think": 40},
                 "support": {"correct": 0.6, "partial": 0.5, "skip_check": 0.5, "think": 40}},
    "tuned": {"trivia": {"correct": 0.9, "partial": 0.5, "skip_check": 0.0, "think": 90},
              "support": {"correct": 0.9, "partial": 0.5, "skip_check": 0.1, "think": 90}},
}


def main():
    runs = {name: run(StubModel(name, profile), DATASET) for name, profile in PROFILES.items()}
    print("== All tasks ==")
    print_report({name: summarize(r) for name, r in runs.items()})
    for tag in ("trivia", "support"):
        print(f"\n== Slice: {tag} ==")
        print_report({name: summarize([r for r in rs if r["tag"] == tag]) for name, rs in runs.items()})
    for name, rs in runs.items():
        print_model(name, rs)
    old, new = (summarize(runs[n]) for n in ("baseline", "tuned"))
    print("\nRegressions in 'tuned' relative to 'baseline':", regressions(old, new) or "none")


if __name__ == "__main__":
    main()
```

Output, with the `trivia` slice and most failed attempts removed:

```
== All tasks ==
model         exact match (SE)  pass@4  pass^4  partial  process  $ / attempt
baseline        0.58 (SE 0.12)    1.00    0.17     0.62     0.75      0.00077
tuned           0.88 (SE 0.06)    1.00    0.50     0.92     0.96      0.00159

== Slice: support ==
model         exact match (SE)  pass@4  pass^4  partial  process  $ / attempt
baseline        0.58 (SE 0.22)    1.00    0.33     0.67     0.50      0.00092
tuned           0.92 (SE 0.08)    1.00    0.67     0.96     0.92      0.00180

== baseline: score of each attempt (1 = exact) and process violations ==
  capital-fr      0001   attempts with a process violation: 0
  capital-au      1110   attempts with a process violation: 0
  hours           0111   attempts with a process violation: 0
  order-status    0100   attempts with a process violation: 3
  refund-ok       1111   attempts with a process violation: 1
  refund-missing  0011   attempts with a process violation: 2
  failed attempts:
    capital-fr      'Sorry, I cannot help with that'
    ...

== tuned: score of each attempt (1 = exact) and process violations ==
  capital-fr      1111   attempts with a process violation: 0
  capital-au      1101   attempts with a process violation: 0
  hours           1101   attempts with a process violation: 0
  order-status    1101   attempts with a process violation: 1
  refund-ok       1111   attempts with a process violation: 0
  refund-missing  1111   attempts with a process violation: 0

Regressions in 'tuned' relative to 'baseline': ['cost']
```

What to observe:

1. **Check the first number by hand.** Baseline succeeds 1, 3, 3, 1, 4 and 2 times out of 4. The mean of 0.25, 0.75, 0.75, 0.25, 1.0 and 0.5 is 0.58.
2. **pass@4 and pass^4 disagree.** Both models have pass@4 = 1.00, because every task succeeds at least once in four. Baseline pass^4 is 0.17: only `refund-ok` succeeds four times out of four. "At least once" flatters a model that succeeds a little over half the time.
3. **Outcome and process disagree.** `refund-ok` shows `1111` with one violation for baseline. The answer was right four times, and once the agent skipped `authenticate`. An outcome-only score would call all four attempts perfect.
4. **Slices show where.** In the support slice, baseline's process score is 0.50. Half of its support attempts broke a rule.
5. **The gate names the trade.** `tuned` is better on every quality metric and costs about twice as much per attempt, because it "thinks" longer. The report makes the trade visible. It does not make the decision.

The numbers describe the two stubs in `PROFILES`, not any real model.

## What the practitioners say

**Where pass^k comes from.** τ-bench is a benchmark for customer-service agents from Sierra (Shunyu Yao et al., ICLR 2025). The Berkeley lecturers explain that it reports pass@1, the average success, and a second metric for reliability: run the task `k` times independently and count success only when all `k` runs succeed ([50:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3000)). Their slide prints the second metric as "pass@k" while defining the all-`k` quantity. This course keeps the two apart: pass@k for "at least one", pass^k for "all". The pass@k estimate in the code is the one introduced for code generation by Mark Chen and colleagues (2021).

**Report cost next to quality.** Describing CRMArena, a benchmark for customer-relationship-management workflows, the lecturers note that it reports the number of turns, tokens and dollars spent, not only task success ([62:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3720)). Their advice is to measure efficiency as well as success ([64:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3840)).

**Partial credit is common in agent benchmarks.** The lecture's slides on LegalAgentBench, one of their case studies, shown just before [64:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3840), give a success rate and a separate progress rate that rewards partial progress toward the answer.

**Kästner on baselines and size.** An accuracy means little on its own, he writes in chapter 15: 99% can be excellent for one problem and useless for another. Compare against a baseline and look at the reduction in error: going from 50% to 75% accuracy halves the error. As a rule of thumb he passes on, hundreds of test items make a quick check and thousands give confidence. Part 8 covers the pitfalls of offline accuracy in detail: [testing generative and LLM components](../08-quality-assurance/05-testing-generative-and-llm-components.md).

## Pitfalls

1. **A grader that is too strict.** Exact string comparison fails "Paris." Fix: normalize, list the accepted answers, or use a [judge](03-llm-as-a-judge-and-rubrics.md).
2. **A grader that is too loose.** Keyword matching passes a wrong answer that contains the keyword. Fix: read failed *and* passed attempts.
3. **Treating attempts as independent.** Four attempts on one task are not four tasks. Fix: average per task first, as `summarize` does.
4. **One attempt per task.** You cannot see reliability. Fix: several attempts and pass^k.
5. **Reporting pass@k alone.** It hides inconsistency. Fix: always print pass^k next to it.
6. **Forgetting cost.** A more accurate prompt that triples the tokens may be a bad trade. Fix: print dollars and latency in the same table.
7. **Tuning on the test set.** If you write prompts against the same tasks you score on, the score stops meaning anything. Fix: keep a held-out set you never look at while developing.

## Try it

Copy the program and run it.

**Deliverable:** a real client for one task type. Write a class with a `complete(prompt, seed)` method that calls a chat model. It calls a paid API, about two cents in total at the example prices. Then call `run(YourModel(), DATASET[:3])`, the three trivia tasks, and pass the records to `summarize` and `print_report`.

**You are done when** the program prints a table for your model, you have hand-checked one number against the per-attempt strings, and you have changed one `accept` value to see the exact match move.

**Stretch goal:** add a `latency` field to `Response`, record the time of each call in `run`, and add a latency column to the report.

## Key takeaways

- A harness has six parts: dataset, interface, runner, graders, metrics, report. Each is small enough to read.
- Keep the system behind one method so a stub and a real client are interchangeable.
- Run every task several times. Report pass^k next to pass@k, because "at least once" and "every time" are different promises.
- Grade outcomes and trajectories separately. They fail independently.
- Print cost next to quality, and slice the report so that failures have an address.
- Gate changes on regressions, not on the target metric alone.

## Self-check

1. A task succeeded in 2 of 4 attempts. What are its pass@4 and pass^4?
   A. 1.0 and 0.0  B. 0.5 and 0.5  C. 1.0 and 0.5  D. 0.5 and 0.0
2. Which metric best answers "can this agent be trusted on every request"?
   A. pass@1  B. pass@k  C. pass^k  D. Partial credit
3. Why does `summarize` average scores per task before computing the standard error?
   A. To make tasks of different lengths comparable
   B. Because repeated attempts on one task are not independent observations
   C. To remove outliers
   D. To give hard tasks more weight
4. In this harness, partial credit is the share of what?
   A. Tool calls in the right order
   B. Accepted answers that were tried
   C. Key phrases found in the answer
   D. Tasks that were attempted
5. `regressions` returns `['cost']` for `tuned` against `baseline`. What does that mean?
   A. `tuned` is broken on the support tasks and must not ship
   B. `tuned` is better on the quality metrics and costs more per attempt
   C. The harness failed to score most of the attempts by `tuned`
   D. `baseline` is cheaper and also the more accurate of the two
6. What is the job of the seed passed to `complete`?
   A. To cache earlier responses
   B. To sort the dataset
   C. To set the token price
   D. To make an attempt repeatable

<details><summary>Show answers</summary>

1. A. At least one success, so pass@4 is 1. Not all four, so pass^4 is 0.
2. C. pass^k is the chance that every one of k attempts succeeds.
3. B. Four attempts on one task carry evidence about one task, so pooling them as independent would shrink the standard error.
4. C. `grade_partial` counts how many of the task's `facts` appear in the answer.
5. B. The three quality metrics improved and the cost per attempt rose, about $0.00077 to $0.00159.
6. D. The same seed gives the same stub behavior, and a real client can pass it to the provider as its own seed.

</details>

## Sources

- **Lecture:** Berkeley course staff, "LLM Agent Evaluations & Project Overview", UC Berkeley Agentic AI MOOC, Fall 2025: [video](https://www.youtube.com/watch?v=VfOA2a0dj4w) · [guide](../lectures/f25-04-agent-evaluation-and-project-overview.md), used at [how τ-bench scores reliability](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3000), [cost and efficiency](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=3720).
- **Reading:** Shunyu Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains" (ICLR 2025): [link](https://arxiv.org/abs/2406.12045). Mark Chen et al., "Evaluating Large Language Models Trained on Code" (2021): [link](https://arxiv.org/abs/2107.03374).
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 15: [link](https://mlip-cmu.github.io/book/15-model-quality.html).

## Next

→ [LLM-as-a-Judge and Rubrics](03-llm-as-a-judge-and-rubrics.md), for the outputs that no program can grade.
