# 02. When to Use ML, and When Not To

**Level:** Foundation · **Reading time:** 20 min · **Exercise:** 45 min
**Prerequisites:** [From Models to Systems and Products](01-from-models-to-systems-and-products.md), for the words *model*, *ML component* and *good enough*.

> **In one sentence:** After this chapter you can answer "should we use ML here?" with evidence: a baseline you ran, the cost of a wrong output, and an honest cost table.

## Why this matters

Product asks for "AI" that sorts incoming support tickets into urgent and not urgent. Three things can happen next.

A team spends a quarter labeling tickets and training a model. Or somebody writes forty lines of keyword rules in an afternoon and the feature ships. Or the request dissolves when someone asks, "What will support do differently with that label?"

Every ML component you accept is a permanent tenant. It needs data, an evaluation set, monitoring, retraining and someone on call. This chapter answers one question: when is that worth it?

## The core idea

Machine learning is a way to get a function you could not write by hand. You pay for it in complexity, cost and risk. Kästner's position in chapter 4 of *Machine Learning in Production* is blunt: ML is not appropriate for all problems. When a hand-coded algorithm can do the job, avoiding ML is very often a good idea.

A hand-written rule is like a recipe: exact steps that anyone can follow and check. A trained model is like a cook who learned by tasting thousands of soups. You cannot read the steps. You can only taste the result. The comparison breaks in two places. A cook can usually tell you why a soup failed. A model cannot explain itself reliably. And the cook keeps needing new ingredients: data that reflects how the world looks now.

### Four conditions

Drawing on that chapter, ML earns its place when all four hold:

1. **Rules cannot do the job, or cannot keep doing it.** Kästner follows Geoff Hulten's three classes of problems. *Intrinsically hard problems* mirror human perception: understanding language, recognizing speech and images, predicting what music someone likes. Attempts to program them with rules made limited progress. *Big problems* could be written by hand but would be too large to maintain: a rule for every artist and track, or the hand-curated web directories that search engines replaced. *Time-changing problems* have inputs and answers that keep moving, as music trends do, so fixed rules need constant edits.
2. **Mistakes are tolerable or can be contained.** A model is an unreliable function. The product must survive its wrong answers. Kästner's warning: even a harmless-looking prediction can harm. Music recommendations that systematically sideline LGBTQ+ artists are a wrong answer with real effects. Where the stakes are higher, non-ML steps must contain the mistake. His example is a cancer prognosis model whose output a radiologist oversees, with a biopsy to confirm it before any surgery. Where correct behavior can be specified exactly, such as accounting totals or control signals in an airplane, ML is the wrong tool.
3. **You have data, ideally arriving continuously.** You need examples with the right answer, to train on and to evaluate against. Data is a common bottleneck and a major cost.
4. **The benefits outweigh the costs.** Both sides are hard to estimate before you build.

Kästner compresses this into one line: ML may solve problems that are intrinsically hard, big and time-changing, as long as the risks are tolerable, the data exists and the benefits beat the costs.

### The business angle: cheaper predictions

Kästner borrows a framing from *Prediction Machines* (Agrawal, Gans and Goldfarb, 2018). ML makes **predictions** cheaper. A prediction is a best guess that reduces uncertainty, using past data. Predictions feed decisions, whether a person or a program makes them. Two questions follow:

- Which decision does this prediction improve?
- What new things become worth doing once that prediction is cheap?

A prediction is not a decision. Turning one into the other takes **judgment**: weighing the cost of a false alarm against the cost of a miss, as a doctor does after a model flags cancer in an image. People usually supply that judgment, though a system with enough data can learn to imitate it, which is the step to full automation. In this framing, cheap predictions either replace an expensive expert, like the record-store clerk who suggests music, or make something affordable at scale. Kästner repeats an example from the book: a shop that ships products a model predicts a customer will like, where the hits must pay for the return shipping of the misses.

### The ladder of alternatives

The four conditions come from the book. So does the habit of trying simpler options first. On the music service, Kästner tries a plain heuristic (recommend the platform's most popular songs by artists the subscriber already played) and a semi-manual solution (a few experts curate twenty playlists, and the system picks the one that overlaps most with recently played songs). He also asks what the product looks like without the feature, and advises being ready to stop the project if the costs outweigh the benefits. The ladder below is this repository's own, and it is the practical form of that advice. Start at the bottom and climb only as far as the evidence forces you.

| Rung | What it is | Use it when | Ongoing cost |
|---|---|---|---|
| 1. Change the workflow | Ask the user to pick a category from a list | The user knows the answer and telling you is cheap | None |
| 2. Rules and keywords | `if`/`else`, regular expressions, lookup tables | There are few patterns and they are stable | Low: edit when patterns change |
| 3. A known algorithm | Sorting, exact matching, a ranking formula | The logic is understood, even if tedious | Low |
| 4. A pretrained model | An API call to a large language model (LLM) or a speech model | The task is perception-like and you have little training data | Medium: cost per call, evaluation, monitoring |
| 5. A model you train | Fitted to your own data | Rung 4 is not good enough and you have the data | High: pipeline, retraining, drift |

An **LLM** is a model trained on huge amounts of text that predicts and generates language; you use it by writing instructions called a prompt. Rungs 4 and 5 are ML components. Rungs 1 to 3 are not. Kästner notes that foundation models, LLMs among them, reduce the need for training data. They do not remove it: you still need examples to design a prompt and to check that it works.

## How it works, step by step

Use this procedure on one candidate feature. It takes an hour for a small feature and a week for a large one.

1. **Write the decision, not the feature.** "What will someone do differently because of this output?" If nothing changes, stop here.
2. **Build the simplest version and measure it.** Run the worked example below on real examples. If it is good enough, ship it. Keep the labeled examples. They become your evaluation set if you need a model later.
3. **Price a wrong output.** What does it cost the user and the business when the answer is wrong once? A thousand times a day? If a wrong answer can cause serious harm and nothing contains it, ML is out until you add non-ML checks or a human decision maker. [Chapter 04](04-planning-for-mistakes.md) shows how.
4. **Check the data.** A **label** is the correct answer attached to an example. How many labeled examples do you have? Who labels new ones? Will they keep arriving? If you have none, you are on rungs 1 to 3, or on rung 4 with an evaluation set you build first.
5. **Ask whether the problem changes.** Patterns that shift over time argue for a model with a retraining loop, and for the commitment to operate it. Stable patterns argue for rules.
6. **Count the costs.** Use the table in the next subsection.
7. **Write the decision down.** What you chose, on what evidence, and when to revisit it.

### What an ML component costs

| Cost | One-time | Ongoing |
|---|---|---|
| Data | Buying, collecting and labeling examples | Fresh labels as the world changes |
| Building | Training a model, or designing a prompt | Retraining, or redoing the prompt work after a model change |
| Evaluation | Building an evaluation set | Re-running it on every change |
| Integration | Guardrails, fallbacks, interfaces | Maintaining them |
| Serving | Deployment work | Compute or API fees, per request |
| Oversight | Training reviewers | People who check or handle the uncertain cases |
| Operation | Monitoring and alerting setup | On-call, incident response |

Kästner names most of these in chapter 4: data acquisition, model building, deployment or API fees, hardware and energy in operation, and humans who oversee the system. A rules-based feature has the integration row and little else.

## Worked example

This is step 2 of the procedure: build the simplest version and measure it. The code needs Python 3.10 or newer and nothing else.

```python
# baseline.py — is a keyword rule good enough to route tickets?
from collections import Counter

# (subject, correct category): 12 hand-labeled tickets
LABELED = [
    ("Please resend my invoice", "billing"),
    ("Refund for last month's charge", "billing"),
    ("Update my credit card", "billing"),
    ("I was charged twice", "billing"),
    ("Cancel my subscription", "billing"),
    ("I cannot log in", "technical"),
    ("The app crashes on export", "technical"),
    ("Export button is greyed out", "technical"),
    ("Sync fails with error 504", "technical"),
    ("Do you offer a student discount?", "other"),
    ("How do I export my invoices?", "other"),
    ("Where is your office?", "other"),
]

BILLING_WORDS = ("invoice", "refund", "charged", "credit card")
TECH_WORDS = ("log in", "crash", "error", "export", "sync", "bug")

def rule(subject: str) -> str:
    s = subject.lower()
    if any(word in s for word in BILLING_WORDS):
        return "billing"
    if any(word in s for word in TECH_WORDS):
        return "technical"
    return "other"

def accuracy(predict) -> float:
    return sum(predict(s) == truth for s, truth in LABELED) / len(LABELED)

if __name__ == "__main__":
    most_common = Counter(truth for _, truth in LABELED).most_common(1)[0][0]
    print(f"always answer {most_common}: {accuracy(lambda _: most_common):.0%}")
    print(f"keyword rule:       {accuracy(rule):.0%}")
    for subject, truth in LABELED:
        if rule(subject) != truth:
            print(f"  miss: {subject!r} is {truth!r}, rule says {rule(subject)!r}")
```

Run `python baseline.py`. The output:

```
always answer billing: 42%
keyword rule:       83%
  miss: 'Cancel my subscription' is 'billing', rule says 'other'
  miss: 'How do I export my invoices?' is 'other', rule says 'billing'
```

What to observe:

- **The first line is a baseline too.** A **baseline** is the score of the simplest alternative, which any smarter solution has to beat. "Always answer the most common category" scores 42 percent, and many solutions do not beat it.
- **The first miss is cheap to fix.** Add `"subscription"` to `BILLING_WORDS` and the rule reaches 92 percent. This loop, look at the misses and patch, is how you find out whether the problem is rule-shaped.
- **The second miss is the interesting one.** "How do I export my invoices?" contains a billing word. Its intent is a question. The rule cannot see intent. That is the boundary where a model starts to earn its keep.
- **Twelve examples prove almost nothing.** They are short, in one language and written by one person. A real check uses at least a few hundred real tickets, sampled from production, including the awkward ones. Hold some back: never measure on the examples you patched the rule against.

Now the decision, with two invented situations:

- Support receives 300 tickets a day, in one language. A wrong route costs one extra hop, and there is a "wrong team?" button. A 92 percent rule with that button is probably good enough.
- Support receives 50,000 tickets a day, across 40 teams and six languages. Nobody can maintain the keyword lists. Rung 4 or 5 pays for itself.

Same feature, opposite answers. The difference is in conditions 3 and 4, not in the technology.

### What changes for LLM and agent systems

LLMs move the goalposts on condition 3. They need no training data to start, and a handful of examples can go straight into the prompt. "We have no training data" is no longer a reason to say no. "We have no labeled examples" is still a reason to say "not yet", because without them you cannot evaluate. Build the evaluation set first: [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md).

Rung 4 becomes the default starting point. The model is someone else's. Your artifacts are the prompt, the model settings and the parsing code, all under version control. An impressive demo is not evidence. Fifty labeled real examples are.

The ladder also tells you where an LLM is the wrong tool. Do not ask a model for arithmetic, an exact lookup, a sort order or an access decision. Use code, or give the model a tool. Models are for jobs where the input is messy human language: classifying it, extracting structured fields from it, summarizing it, drafting a reply.

Agents raise the stakes on every rung. An **agent** lets the model decide which tool to call next, and each extra step multiplies the chance of a wrong one. Apply the ladder to each step separately. The step that needs judgment gets the model. Validation, retries and state stay in plain code: [Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md).

## What the practitioners say

- **Hype is a poor reason.** Kästner observes that adoption is sometimes driven by interest in the technology or by marketing, not by a problem. ML brings complexity, cost and risk, and needs expertise to build, evaluate and integrate ([chapter 4](https://mlip-cmu.github.io/book/04-when-to-use-machine-learning.html)).
- **Hand-coded first.** If hand-coded algorithms can solve the problem, avoiding ML is very often a good idea. ML is worth the effort, he writes, for three classes of problems he takes from Hulten: intrinsically hard, big and time-changing.
- **Tolerance for mistakes is a precondition.** ML should be used only where the application can tolerate mistakes, or where mechanisms around the model bring the risk down to an acceptable level. Those mechanisms can cost so much that they undo the benefit of automation. Then the right decision is not to build.
- **Continuous data is an advantage.** He describes the ML **flywheel**: more users produce more data, better models attract more users. A music service can watch what subscribers play and which recommendations they skip, and feed that back into the model. For a problem that keeps changing, it might even suggest new songs to random subscribers just to learn who likes them.
- **Costs and benefits are both hard to estimate.** How much do recommendations contribute to keeping subscribers? What will operation cost before it is built? He notes that many start-ups simply wager on a large future payoff.
- **Benefits can be large.** For a music streaming service, recommendations are a useful feature. For TikTok, he argues, recommendations created a new kind of social-media experience.

## Pitfalls

1. **Starting from the model instead of the decision.** Fix: write the sentence "someone will do X differently". If you cannot, stop.
2. **Skipping the baseline.** Without the rule's score, you cannot tell whether a model earns its keep. Fix: rung 2 first, every time.
3. **Judging on a dozen friendly examples.** Fix: a few hundred real examples, held out from the ones you tuned on.
4. **Counting only the build cost.** Fix: fill in the cost table, including oversight and on-call.
5. **Trusting a demo.** Five examples that work prove that five examples work. Fix: an evaluation set before any decision.
6. **Using a model where exactness is required.** Sums, eligibility, permissions: these belong in code.
7. **Assuming a casual domain means harmless mistakes.** A wrong song recommendation is cheap. A systematically unfair one is not.

## Try it

Take one request of the form "could we use AI here?" and write a one-page decision note.

Include:

1. The decision the output would change.
2. The simplest version, and its score on at least 50 labeled real examples, next to the always-answer-the-most-common score.
3. The cost of one wrong output, for the user and for the business.
4. The data you have and the data you would need.
5. The cost table, filled in with rough numbers.
6. Your decision and the date on which to revisit it.

**You are done when** the note lets a colleague who disagrees with you see exactly which number would change your mind.

**Stretch goal:** send the same 50 examples through an LLM API with a prompt and compare. This calls a paid API. Fifty short tickets cost a few cents at the prices of small models as of 2026-11; check the provider's current price page before you run.

## Key takeaways

- ML buys a function you could not write by hand. You pay in complexity, cost and risk.
- It earns its place when the problem is intrinsically hard, too big for hand-written rules, or changing over time; mistakes are tolerable; data exists; and the benefits beat the costs.
- Climb the ladder one rung at a time: workflow, rules, known algorithm, pretrained model, trained model.
- Always measure the simplest version against real, labeled examples before building anything smarter.
- The decision depends on volume, languages and the cost of a mistake. The same feature can justify opposite answers.

## Self-check

1. Name the four conditions under which ML earns its place.
2. A keyword rule scores 83 percent on 12 examples you wrote while looking at the rule. Which is the strongest objection?
   - A. The author wrote them while looking at the rule, so they share its assumptions rather than test real tickets.
   - B. The rule relies on keywords, and keyword rules are known to fail on every text-classification task.
   - C. The score is printed without decimals, so the true value could lie anywhere near eighty-three.
   - D. The baseline is a rule, and a rule can never stand in as the baseline for a model.
3. You have no labeled data. An LLM handles the task in five demo examples. What is missing before you ship?
4. Which cost does an ML component add that a rules-based version does not have?
   - A. Editing the rule when support renames one of its teams.
   - B. Retraining the model when ticket wording drifts, and re-running the evaluation set.
   - C. Writing unit tests for the routing code that calls the component.
   - D. Reviewing the feature with the support team before its first release.
5. In one sentence, what does the "cheaper predictions" framing add to the decision?
6. True or false, with a reason: "A music recommendation feature is low-risk, because one wrong recommendation is harmless."

<details><summary>Show answers</summary>

1. The problem is intrinsically hard, too big to hand-code, or changing over time; mistakes can be tolerated or contained; data for training and evaluation is available; the benefits outweigh the costs.
2. A. Examples written by the author of the rule, while looking at the rule, repeat its assumptions. Real production tickets, held out from tuning, are the test.
3. An evaluation set: labeled real examples with expected outputs, large enough to trust, run on every change to prompt, model or settings.
4. B. Retraining and re-evaluation exist only with a learned component. The other three apply to both versions.
5. It tells you which decision the prediction improves, and what becomes worth doing once that prediction is cheap.
6. False. A single wrong recommendation is cheap, but a systematic error, such as consistently downgrading certain artists, harms people at scale. Judge the pattern of mistakes, not one mistake.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 4: [When to use Machine Learning](https://mlip-cmu.github.io/book/04-when-to-use-machine-learning.html)
- **Reading:** Ajay Agrawal, Joshua Gans and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence* (Harvard Business Review Press, 2018), the framing Kästner cites for ML as cheaper predictions.
- **Reading:** Geoff Hulten, *Building Intelligent Systems* (Apress, 2018), chapter 2, the source of the problem classes Kästner refers to.

## Next

→ [Goals and Requirements](03-goals-and-requirements.md), because once you have decided to build, the first question is what "good enough" means in numbers.
