# 03. Slicing: Finding Where the Model Fails

**Level:** Practitioner · **Reading time:** 28 min · **Exercise:** 75 min
**Prerequisites:** [Measuring Model Quality](02-measuring-model-quality.md)

> **In one sentence:** After this chapter you can take a green dashboard, find the subgroups of inputs where the model fails, search for those subgroups automatically, and turn each one into an action.

## Why this matters

The triage model holds at 91 percent accuracy for a month. Then a support lead from the Berlin team writes: chat tickets in German are routed to the wrong queue "all the time". You check. She is right. The dashboard never moved, because those tickets are 3 percent of the traffic.

Three questions follow, and this chapter answers them:

1. How do I measure quality on a subgroup without fooling myself?
2. Nobody tipped me off about the next bad subgroup. How do I find it?
3. When I find one, what do I do about it?

## The core idea

A **slice** is a subset of your evaluation data, chosen by a rule called a **slicing function**. You compute the model's accuracy inside each slice and compare it with the overall number.

Software testers already think this way. Nobody tests a date function on random dates. They test month-ends, leap years, and invalid inputs, because the specification says those are the interesting classes. Slicing applies the same instinct to a model.

The analogy breaks in two places. A model has no specification to derive the classes from, so you have to invent them. And a class does not pass or fail. It has a rate, which can be 99 percent or 60 percent.

Kästner's rules for slices (chapter 15):

- Slices come from test data or production data. One example can sit in any number of slices.
- Two slices can be **intersected** to make a new one: chat tickets *and* German.
- Small slices give unreliable numbers.

The last rule explains the dashboard. If German chat tickets are rare in your test set, a total failure there barely moves the average.

| Kind of slice | Membership comes from | Example |
|---|---|---|
| Metadata | A field you already have | Channel is chat, plan is free |
| Input property | A function of the text | Longer than 2,000 characters, contains a stack trace |
| Behavior | What the task demands | Asks two questions in one message |
| Intersection | Two or more of the above | Chat, German, and asks two questions |

The medical-imaging literature has a name for the failure this catches: **hidden stratification**. A label looks uniform, but it hides subgroups on which the model performs very differently (Oakden-Rayner et al., 2020, listed in the chapter's further readings).

## How it works, step by step

### 1. List candidate attributes

Start with three sources:

- **Requirements and risk.** Which inputs matter most, and where would a mistake hurt? Give each one a slice.
- **Available metadata.** Channel, language, plan, time of day.
- **Hypotheses from mistakes.** Read twenty wrong predictions. Guess what they share.

In practice, teams slice by whatever fields happen to exist. Kästner argues this is the wrong order: the requirements should drive the slices, and missing fields should be built (chapter 15).

### 2. Write slicing functions

A metadata slice is a filter. A behavior slice needs a classifier that decides membership, which takes real work. For text, an LLM can label inputs with properties such as "contains a complaint and a question". Treat those labels as noisy until you have checked a sample by hand.

### 3. Report accuracy and size together

Never report a slice's accuracy without its size. "0 percent on two tickets" is a lead, not a result.

### 4. Search automatically

Manual slicing finds what you already suspect. An automatic search finds what you do not. The procedure:

1. Enumerate every single attribute value, then every pair, and stop at depth two or three.
2. Drop slices below a minimum size. A few hundred examples is a common floor for trust; the book cites Hulten's rule of thumb that hundreds give a quick check and thousands give confidence (chapter 15).
3. For each remaining slice, compute its error rate.
4. Rank by **extra mistakes**: the slice's mistakes minus the mistakes the overall error rate predicts for a group of that size.
5. Confirm the top slices on data the search did not use.

Step 5 matters because of **multiple comparisons**. If you test two hundred slices with a test that is wrong 5 percent of the time, about ten will look bad by pure chance. The more you search, the more false alarms you get. A statistical test and a second look on fresh data separate real failures from luck.

<!-- SOURCE GAP: the book names SliceFinder, Zeno, Errudite and Overton, and says SliceFinder uses statistical tests to find underperforming slices and intersections, but it does not describe how automatic slice search works. The five-step procedure, the multiple-comparison warning and the worked example below are the author's, not the book's. -->

### 5. Read the errors in the worst slice

A slice names *where*. It rarely explains *why*. Open the misrouted tickets. The fix depends on the cause, and the cause is often one of four:

| What you see in the errors | Likely cause | Typical fix |
|---|---|---|
| The model never saw similar examples | Training or prompt coverage | Add labeled examples for this slice |
| The input is missing information the task needs | Upstream data problem | Fix the pipeline (see [Data Quality](06-data-quality.md)) |
| The task is genuinely ambiguous on this slice | Unclear requirement | Clarify the rule with the support team |
| A shortcut works elsewhere but not here | Wrong reasoning | Add a behavioral test (see [Testing Without Oracles](04-testing-without-oracles.md)) |

### 6. Turn the slice into an action

Kästner splits the responses into two kinds (chapter 15). A **fix** changes the model, usually with more training data for the slice. A **mitigation** changes the system around it: detect these inputs and restrict what the model does for them, or let the model suggest and let a person decide.

| Decision | When it fits |
|---|---|
| Fix the model | The slice matters and you can get data for it |
| Mitigate: route to a human, or change the workflow | The slice matters and the fix will take a while |
| Accept and monitor | The slice is rare and the mistake is cheap |
| Re-scope the product | The slice is common and no fix works. Exclude it from the promise |

Never make the number better by deleting the slice from the test set.

### 7. Keep the slice as a regression test

Once a slice is fixed, add its slicing function to the test suite and track its accuracy over time. A later model or prompt change can reopen it. In production, the same functions become monitoring groups (see [Testing and Experimenting in Production](09-testing-and-experimenting-in-production.md)).

## Worked example

Eight tickets with three metadata fields. The fourth element of each tuple records whether the model routed it correctly. Plain Python, no libraries, no cost.

```python
from itertools import combinations

# (channel, language, plan, routed_correctly)
tickets = [
    ("email", "en", "free", True),  ("email", "en", "paid", True),
    ("email", "de", "free", True),  ("email", "de", "paid", True),
    ("chat",  "en", "free", True),  ("chat",  "en", "paid", True),
    ("chat",  "de", "free", False), ("chat",  "de", "paid", False),
]
FIELDS = {"channel": 0, "language": 1, "plan": 2}

def accuracy(rows):
    return sum(r[3] for r in rows) / len(rows)

def in_slice(row, condition):
    """A condition is a tuple of (field, value) pairs; all must match."""
    return all(row[FIELDS[f]] == v for f, v in condition)

def find_slices(rows, min_size=2, max_depth=2):
    """Rank attribute values and their pairs by the mistakes they hold."""
    base_miss_rate = 1 - accuracy(rows)
    values = {f: {r[i] for r in rows} for f, i in FIELDS.items()}
    singles = [(f, v) for f in FIELDS for v in values[f]]
    found = []
    for depth in range(1, max_depth + 1):
        for combo in combinations(singles, depth):
            if len({f for f, _ in combo}) != depth:  # skip "chat AND email"
                continue
            members = [r for r in rows if in_slice(r, combo)]
            if len(members) < min_size:
                continue
            acc = accuracy(members)
            extra = (1 - acc - base_miss_rate) * len(members)
            found.append((round(extra, 2), acc, len(members), combo))
    return sorted(found, reverse=True)

for extra, acc, size, combo in find_slices(tickets)[:3]:
    print(f"{combo}: accuracy {acc:.2f} on {size} tickets ({extra} extra mistakes)")
```

Output:

```
(('channel', 'chat'), ('language', 'de')): accuracy 0.00 on 2 tickets (1.5 extra mistakes)
(('language', 'de'),): accuracy 0.50 on 4 tickets (1.0 extra mistakes)
(('channel', 'chat'),): accuracy 0.50 on 4 tickets (1.0 extra mistakes)
```

What to observe:

- The overall accuracy is 75 percent, which looks acceptable.
- Each single attribute tells half the story. German tickets are at 50 percent. Chat tickets are at 50 percent. Neither looks like an emergency.
- The intersection fails completely. Ranking by extra mistakes puts it first.
- The same two wrong tickets appear in all three top slices. Slices overlap, so do not add their mistakes up.
- Eight examples are far too few for a real decision. A search like this tells you where to look. Confirm on hundreds.

## What the practitioners say

- **Not every input matters equally.** Kästner's example is a voice assistant: a mistake on "Call mom" is not forgiven, while a mistake on an obscure shopping item is (chapter 15). He advises creating slices for important inputs whether or not they are frequent.
- **Slices should come from requirements.** Slicing by available features is common, he writes, but the better source is your understanding of the problem: important inputs, rare inputs, groups you worry about for fairness, and specific behaviors (chapter 15).
- **Debugging is hypothesis-driven.** If reports say young children's cancers go undetected, build slices by cancer type and age group to test whether a few reports reflect a wider pattern (chapter 15).
- **Small slices need more data.** Accuracy on a tiny slice is unreliable. If the slice matters, collect more test data for it (chapter 15).
- **Tools exist for the search.** He cites SliceFinder, which explores many slices and intersections and uses statistical tests to flag underperforming ones, and Zeno, which lets testers visualize slices and inspect their examples (chapter 15).
- **Overton at Apple.** Developers write slicing functions for hard subsets, such as nutrition-related queries or queries with complex disambiguation. They improve one slice at a time, usually by adding labeled training data through **weak supervision**, meaning labels produced by rules instead of hand. Kästner credits the approach with making progress tractable and visible (chapter 15).
- **The software parallel.** He maps slicing onto equivalence class testing: a weak design tests each class once, a strong one tests each combination of classes. Combinatorial testing and decision tables help when combinations multiply (chapter 15).

## Pitfalls

1. **Slicing only by the fields you have.** Language may be recorded. "Contains a code block" is not. Fix: derive fields from the inputs, and label a sample with an LLM, then verify.
2. **Trusting a tiny slice.** Fix: set a minimum size, and collect more examples before acting.
3. **Testing hundreds of slices once.** Some look bad by chance. Fix: rank by extra mistakes, apply a statistical test, and confirm on fresh data.
4. **Stopping at the slice's name.** "German chat tickets" is a location, not a cause. Fix: read the failures before choosing a fix.
5. **Removing the bad slice from the test set.** The score improves and the product does not. Fix: every known slice stays in the suite.
6. **A wrong membership rule.** If the slicing function mislabels inputs, the slice's accuracy measures the rule, not the model. Fix: hand-check a sample of members and non-members.

## Try it

Take a labeled set of at least 300 inputs for one of your components, with at least three attributes per input.

1. Write five slicing functions: three from metadata, two from input content.
2. Compute accuracy and size for each slice and for every pair.
3. Rank by extra mistakes. Take the top slice and read all of its failures.
4. Write one sentence on the cause, and choose an action from the table in step 6.

You are done when you have a table of slices with accuracy and size, a ranked top three, a written cause for the worst one, and a chosen action. **Stretch goal:** run the search on one half of the data and confirm the top slices on the other half.

## Key takeaways

- An overall accuracy number hides the groups where a model fails. Slices make those groups visible.
- Derive slices from requirements and risk first, and from available fields second.
- Report accuracy and size together, and distrust small slices.
- Automatic search enumerates attribute values and their pairs and ranks by extra mistakes. Searching many slices creates false alarms, so confirm on fresh data.
- A slice says where, not why. Read the failures, then choose to fix, mitigate, accept, or re-scope.
- Keep every important slice as a regression test and a monitoring group.

## Self-check

1. A model's overall accuracy is unchanged, yet one team reports many more failures than before. What is the simplest explanation?
2. Why report a slice's size next to its accuracy?
3. A search over 400 slices returns fifteen with low accuracy. What should you do before filing fifteen bugs?
4. You find that short chat messages fail. What is the next step before writing a fix?
5. Why rank slices by extra mistakes instead of by the lowest accuracy?

<details><summary>Show answers</summary>

1. The failing group is a small share of the traffic, so its drop barely moves the average. An overall number is an average weighted by how common each input is.
2. An accuracy from a handful of examples is unstable and can look extreme by chance. The size tells you how much to trust the rate.
3. Confirm on data the search did not use, and apply a statistical test with a minimum size. With that many comparisons, several low scores are expected by chance.
4. Read the failing messages to find the cause, such as missing context or an unclear rule. The slice only tells you where the problem lives.
5. The lowest accuracy often belongs to the smallest slice, which holds few mistakes. Extra mistakes weigh how bad the slice is against how many inputs it affects.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 15: [link](https://mlip-cmu.github.io/book/15-model-quality.html)
- **Reading:** Luke Oakden-Rayner, Jared Dunnmon, Gustavo Carneiro, and Christopher Ré, "Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging" (2020), listed in the chapter's further readings: [link](https://doi.org/10.1145/3368555.3384468)
- **Reading:** Yeounoh Chung, Neoklis Polyzotis, Kihyun Tae, and Steven Euijong Whang, "Automated Data Slicing for Model Validation: A Big Data-AI Integration Approach" (2019), the SliceFinder paper, listed in the chapter's further readings: [link](https://arxiv.org/abs/1807.06068)

## Next

→ [Testing Without Oracles](04-testing-without-oracles.md), because many failures need no labels at all to expose: compare the model's answers on two versions of the same input.
