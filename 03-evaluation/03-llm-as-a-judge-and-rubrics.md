# 03. LLM-as-a-Judge and Rubrics

**Level:** Practitioner · **Reading time:** 20 min · **Exercise:** 90 min
**Prerequisites:** [A Minimal Evaluation Harness](02-a-minimal-eval-harness.md)

> **In one sentence:** After this chapter you can write a rubric a model can apply, turn it into a judge prompt, and measure the judge against human labels before you let it score anything.

## Why this matters

Your support agent now writes its own answer: "I'm sorry the router keeps dropping. I've sent a replacement, and you will have it tomorrow." There is no string to compare. A keyword check passes a confident lie, as long as it contains "replacement". Reading 300 answers yourself takes an afternoon, every time the prompt changes.

The question: how do you grade open-ended output as fast as your development loop, without fooling yourself?

## The core idea

An **LLM-as-a-judge**, or **judge**, is a model that reads an output and scores it. A **rubric** is the list of criteria it applies: short, concrete statements, each of which can be checked by reading the output.

The judge is cheap and fast, like an assertion. It is also unreliable, like a flaky test. Call it a **flaky oracle**. It is an oracle because it says pass or fail. It is flaky because it can disagree with itself between two runs, and with a person who reads the same output.

**Where the flaky-test analogy breaks.** You fix a flaky test by fixing its timing. You cannot remove a judge's noise. You can shrink it, and you must measure what is left. That measurement is **calibration**: you label a sample of outputs by hand, let the judge score the same sample, and compare. Before that comparison, a judge score is a number with an unknown bias.

The rubric exists because a judge asked "Is this a good answer?" decides for itself what good means, and decides differently each time. The rubric moves that decision into text that you control.

## How it works, step by step

### 1. Decide whether you need a judge

Use a program when one exists: exact match, a unit test run on generated code, a comparison of database states (see the [harness](02-a-minimal-eval-harness.md) and [agent evaluation](04-evaluating-agents-trajectories-and-environments.md)). Use a judge only for what reading can decide: is the tone right, does the answer fit the customer's actual situation, is every claim supported by the source document. Use a person when the decision is expensive or cannot be undone.

### 2. Write the rubric

1. **One criterion per line, each decidable from the output.** Not "quality of tone" but "the answer does not blame the customer".
2. **Binary verdicts, or a three-point scale with every point described.** A scale from 1 to 10 adds digits, not information.
3. **Give the judge the ground truth.** A *reference-based* criterion lists the facts the answer must contain. A *reference-free* criterion can only judge the form of the text.
4. **Ask for evidence.** For every failed criterion the judge must quote the fragment that fails. This makes it look before it concludes, and it gives you something to check.
5. **Say what to ignore:** length, formatting, confidence of the wording.
6. **Test the rubric on fakes.** Feed it known-good outputs, and known-bad outputs that each fail exactly one criterion. This is the mutation-testing idea Kästner describes for test suites: inject a defect and see whether the checks notice (chapter 14). The Berkeley checklist asks the same of evaluators: write cases that succeed and fail in different ways, each with the verdict you expect ([88:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5280)).

A rubric for the refund agent's final answer:

| # | Criterion | Type |
|---|---|---|
| 1 | States the refund amount from the order record | Reference-based |
| 2 | States the refund time from the policy | Reference-based |
| 3 | Makes no promise the policy does not allow | Reference-based |
| 4 | Has at most three sentences | Reference-free |
| 5 | Does not blame the customer | Reference-free |

### 3. Write the judge prompt

The prompt carries the rubric, the ground truth, and the required output format. A fixed format such as JSON, a notation for nested key-value pairs, lets the harness read the verdict without parsing prose.

### 4. Choose the setup

- **Pointwise:** the judge scores one output at a time. You get a number you can track from version to version.
- **Pairwise:** the judge compares two outputs. This is better at ranking two versions, but it has a **position bias**: it favors the one listed first. Show each pair in both orders and average.
- **Repeated:** run the same judgment several times and take the majority.

### 5. Calibrate against human labels

Label 30 to 100 outputs yourself. Two people are better, because their disagreement shows the ceiling. Then compute three numbers, shown below.

### 6. Fix or accept, then recalibrate

If the judge passes outputs that people reject, the rubric is missing a fact or a criterion. Rewrite, then calibrate again. Calibrate again after every change of judge model, prompt or rubric.

## Worked example

**The judge, inside the harness.** A judge is only another model behind `complete(prompt, seed)`. This function is illustrative: it needs a real model, and each call costs API money.

```python
import json

def judge(model, task, response):
    """Score one answer. `task["facts"]` is the ground truth."""
    head = ("You are grading one answer from a customer-support agent.\n"
            "Apply each criterion. A criterion passes only if the answer shows it.\n"
            "Ignore length and formatting. For every failed criterion, quote the "
            "fragment of the answer that fails it.\n")
    body = (f"\nGround truth: {task['facts']}\n"
            f"Customer's request: {task['goal']}\n"
            f"Agent's answer: {response.text}\n")
    tail = ("\nCriteria: state_amount, state_time, no_false_promise, no_blame.\n"
            'Return only JSON, with one entry per criterion, for example\n'
            '{"state_amount": {"pass": true, "quote": ""}}\n')
    return json.loads(model.complete(head + body + tail).text)
```

**Calibration by hand.** A person and the judge each graded 40 answers on one question: is the answer acceptable?

| | Judge passes | Judge fails |
|---|---|---|
| Person passes | 18 | 4 |
| Person fails | 5 | 13 |

- **Agreement:** (18 + 13) / 40 = 77.5%.
- **False passes:** 5 of the 18 answers the person rejected, or 27.8%. This is the dangerous error: bad output marked good.
- **False fails:** 4 of the 22 answers the person accepted, or 18.2%. This one sends good output back for no reason.
- **Agreement by chance:** the judge passes 23 of 40 and the person passes 22 of 40, so two labelers who ignored the answers would still agree on (23/40)(22/40) + (17/40)(18/40) = 50.75% of them.

The last number is why agreement alone flatters. If two labelers each pass 90% of items at random, they agree on 82% of them without reading a word.

**Cohen's kappa** removes the chance agreement. It is the share of the gap to perfect agreement that the two labelers actually covered:

```python
def kappa(human, judge):
    """Cohen's kappa for two lists of 0/1 labels of the same items."""
    n = len(human)
    agree = sum(h == j for h, j in zip(human, judge)) / n
    p_human, p_judge = sum(human) / n, sum(judge) / n
    by_chance = p_human * p_judge + (1 - p_human) * (1 - p_judge)
    return (agree - by_chance) / (1 - by_chance)

human = [1] * 22 + [0] * 18                # the table above
judge = [1] * 18 + [0] * 4 + [1] * 5 + [0] * 13
print(kappa(human, judge))                 # 0.54
```

What to observe: kappa is (0.775 − 0.5075) / (1 − 0.5075) = 0.54. Under a widely used reading of the statistic (Landis and Koch, 1977), 0.41 to 0.60 is moderate agreement. That makes this judge good for comparing two versions and for finding bad outputs to read. It makes the judge's own pass rate a poor estimate of the real pass rate, because one in four bad answers slips through.

## What the practitioners say

**People are the reference, and people are a problem.** The Berkeley lecturers call human evaluation the gold standard and list five defects: it is slow, expensive, marked by disagreement between annotators, marked by disagreement of one annotator over time, and not reproducible (slides 19 and 20).

**Judges have known defects, each with a fix.** At [18:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1080) the lecturer explains that a judge's output varies from run to run and that different models have different strengths, so he averages repeated judgments and combines several judges. The slide adds the rest:

| Problem with a judge | Fix named in the lecture |
|---|---|
| Unreliable | Majority vote between different judge models |
| Random output | Repeat the judgment with the same model |
| Different models, different biases | Cross-check against human evaluation |
| Scores are hard to interpret | Continuous scores instead of discrete ones; several rubrics |
| Sensitive to vague prompts | Detailed prompts; chain of thought or a reasoning mode |

**Chain of thought** means telling the model to write out its steps before it gives the verdict. The lecturer's closing advice is "you should use some human evaluation to do some small-scale cross-checking" ([18:00](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1080)). Judges cost much less than people, which is why he expects most course projects to use them for tasks that have no programmatic check.

**Biases research has named.** The lecture does not catalog them, so these come from the research literature rather than from the course: *position bias* (the first of two outputs wins more often), *verbosity bias* (longer outputs score higher when they add nothing) and *self-preference* (a model rates its own output higher). Lianmin Zheng and colleagues documented the first two, and a self-enhancement bias, for pairwise judging in 2023.

<!-- VERIFY: The bias names are from general knowledge. The citation is Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023), arXiv:2306.05685; confirm the identifier and that the paper names position, verbosity and self-enhancement bias before publishing. -->

**Kästner on generative output.** Many different outputs can be right, he writes in chapter 15, so the question is not "is it correct" but how often the output is satisfactory for the task. He also describes **red teaming**, experts who attack a system creatively to find failures. Red teaming finds failures you did not think of. It does not measure a rate. Use it to extend the rubric, not to replace calibration. Part 8 has more: [testing generative and LLM components](../08-quality-assurance/05-testing-generative-and-llm-components.md).

## When not to use a judge

- A program can decide. A judge then adds noise to a precise answer.
- You have not calibrated it.
- The judge is the same model, or from the same family, as the agent it grades.
- The decision is high-stakes and unreviewed: payments, safety, legal commitments.
- You need to explain a verdict to a customer. A rubric line with a quoted fragment can be explained. A bare score cannot.

## Pitfalls

1. **A vague rubric.** "Is the answer good?" Fix: one observable criterion per line.
2. **Several criteria in one question.** "Is it accurate, complete and polite?" yields one blurred verdict. Fix: one verdict per criterion.
3. **No ground truth in the prompt.** The judge cannot tell an invention from a fact. It will pass "you will have it tomorrow" when the policy says ten days. Fix: put the facts in.
4. **Pairwise judging without swapping.** Position bias becomes a systematic error. Fix: both orders.
5. **Calibrating once.** A new judge model or a new rubric is a new judge. Fix: recalibrate on each change.
6. **A parse failure counted as a bad answer.** Malformed JSON turns into a zero and lowers the score. Fix: retry once, then flag the item for review.
7. **The agent judging itself.** Fix: a different model family, or a person.

## Try it

**Deliverable:** a calibrated judge for one output type of your agent.

1. Write a rubric with four criteria. Mark each as reference-based or reference-free.
2. Write 6 fake outputs: 2 good, and 4 that each fail exactly one criterion. Confirm the judge catches all four.
3. Label 30 real outputs by hand. Run the judge on the same 30.

**You are done when** you can state the judge's false-pass rate, its false-fail rate and its kappa on your 30 outputs, and the kappa is at least 0.6 or you have written down why you accept less.

**Stretch goal:** have a second person label the same 30 outputs, and compare human-human kappa with judge-human kappa.

## Key takeaways

- A judge is a flaky oracle: cheap and scalable, noisy and biased. Its noise cannot be removed, only measured.
- The rubric decides what "good" means. Make each criterion observable, give the ground truth, and demand a quote for every failure.
- Calibrate against human labels before use: false-pass rate, false-fail rate, and kappa to remove agreement by chance.
- Prefer a programmatic check whenever one exists.
- Swap positions in pairwise judging, repeat judgments, and cross-check with people.
- Recalibrate whenever the judge model, prompt or rubric changes.

## Self-check

1. Why does the lecture recommend a small human cross-check for every judge?
   A. Human labels are cheaper to collect
   B. To confirm that the judge agrees with people before relying on it
   C. To fine-tune the judge model
   D. To make the judging faster
2. A judge gives the same answer a 3 on Monday and an 8 on Friday. Which fix from the lecture applies directly?
   A. A different rubric for each day
   B. Repeat the judgment several times and combine the results
   C. Remove the ground truth from the prompt
   D. Use a scale with more points
3. Two labelers each pass 90% of items at random. About how often do they agree?
   A. 50%  B. 66%  C. 82%  D. 99%
4. A kappa of 0.54 between a judge and a person means what?
   A. The judge is right 54% of the time
   B. Agreement beyond chance is moderate: the judge is a usable but noisy proxy
   C. The judge is worthless
   D. The person is wrong
5. Which output should be graded by a program rather than a judge?
   A. The tone of an apology
   B. Whether a generated function passes its unit tests
   C. Whether a summary is fair to all sides
   D. Whether an email sounds rude
6. Why does the judge prompt ask for a quoted fragment for each failed criterion?
   A. To make the prompt longer
   B. To lower the cost of the call
   C. To hide the model's reasoning
   D. To tie the verdict to evidence you can check

<details><summary>Show answers</summary>

1. B. Judges are cheaper than people, so the lecture asks for a small human sample to confirm the judge is reliable.
2. B. Random output is the problem, and the lecture's fix is repeated judging.
3. C. 0.9 × 0.9 + 0.1 × 0.1 = 0.82. This is why agreement alone is not enough.
4. B. Kappa removes agreement by chance. 0.54 is moderate agreement.
5. B. A test is a precise oracle. The other three need reading.
6. D. The quote forces the judge to point at the failure, and it lets you audit the verdict.

</details>

## Sources

- **Lecture:** Berkeley course staff, "LLM Agent Evaluations & Project Overview", UC Berkeley Agentic AI MOOC, Fall 2025: [video](https://www.youtube.com/watch?v=VfOA2a0dj4w), used at [judge issues and fixes](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=1080), [testing the evaluator](https://www.youtube.com/watch?v=VfOA2a0dj4w&t=5280).
- **Reading:** Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023): [link](https://arxiv.org/abs/2306.05685).
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapters 14 and 15: [link](https://mlip-cmu.github.io/book/15-model-quality.html).

## Next

→ [Evaluating Agents: Trajectories and Environments](04-evaluating-agents-trajectories-and-environments.md), for the outputs that change the world instead of describing it.
