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
