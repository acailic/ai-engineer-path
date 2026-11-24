# 05. Testing Generative and LLM Components

**Level:** Practitioner · **Reading time:** 30 min · **Exercise:** 120 min
**Prerequisites:** [Testing Without Oracles](04-testing-without-oracles.md)

> **In one sentence:** After this chapter you can turn "the output should be good" into a rubric of yes-or-no questions and run it as an automated test suite, with a calibrated LLM judge, inside CI and on a budget.

## Why this matters

Your team ships a feature that summarizes each support conversation for the next agent. A reviewer reads five summaries and says they look fine.

Two weeks later someone rewrites the prompt. Summaries start to promise refunds that no agent offered. The unit tests pass, because none of them looks at the text. The problem surfaces when a customer quotes a promise the company never made.

You know how to test a function. You do not yet know how to test prose.

## The core idea

A **rubric** is a short list of criteria, each written as a question with a yes-or-no answer. It converts one vague request, "write a good summary", into several small ones. Each question is a separate oracle.

A **judge** is whatever answers those questions. Three kinds exist, and you should use them in this order:

1. **Code.** Cheap, exact, and fast. Use it for everything checkable: valid JSON, required strings, length, a language, a date format.
2. **An LLM judge.** Using a model to grade another model's output is called **LLM-as-a-judge**. Use it for meaning: Is every fact in the summary present in the conversation?
3. **A person.** Slow and expensive. Use people to calibrate the judge and to settle the cases the judge gets wrong.

The analogy is a linter, a junior reviewer, and a senior reviewer. A linter never tires and never understands intent. A junior reviewer with a checklist catches most violations and makes mistakes of their own. A senior reviewer audits the junior. The analogy breaks on consistency: a human junior gives the same answer twice, while an LLM judge can grade the same output differently on two runs, so its results are a rate.

<!-- SOURCE GAP: the book covers human judgment against stated criteria, property checks, and LLM-generated test data. The rubric pipeline below, the judge calibration, flakiness handling, cost estimate and CI tiering are the author's, not the book's. Judge design and judge biases are treated in part 03. -->

## How it works, step by step

### 1. Write the rubric

Write six to eight criteria. Give each one three parts:

- a name;
- a yes-or-no question answerable from the input and the output alone;
- a severity: **must** (a hard requirement, such as "invents nothing") or **should** (a quality preference, such as "neutral tone").

Bad criterion: "Is the summary good?". Good criterion: "Does the summary state how the conversation ended: resolved, pending, or no reply?".

### 2. Give each criterion the cheapest oracle

| Criterion | Oracle |
|---|---|
| Output parses as JSON | Code |
| States the refund amount that was offered | Code, with the amount supplied per test case |
| At most three sentences | Code |
| Every fact appears in the conversation | LLM judge |
| No action is promised that nobody agreed to | LLM judge |
| Tone is neutral | LLM judge, then a person on a sample |

### 3. Build the test set

Collect 30 to 100 real inputs. Then add cases designed to tempt each failure: an empty conversation, a rude customer, a very long thread, two issues in one message, a thread with no reply, a language switch in the middle. For each case, write down what a correct output must contain.

Keep a held-out set that you never tune the prompt on. [Measuring Model Quality](02-measuring-model-quality.md) explains why.

### 4. Design the judge call

- Ask about **one criterion at a time**. A judge that scores five criteria at once is harder to debug.
- Grade with the **input beside the output**, so the judge can check facts against the source.
- Ask for **evidence**: the exact words that justify the verdict. Then check that those words occur in the output. A judge that cannot quote real text has not read it.
- Require a **fixed output format**, such as JSON, so parsing never becomes the failure.
- Call the model at its **most deterministic setting** (temperature 0, where the provider offers it).

### 5. Calibrate the judge against people

An uncalibrated judge is an opinion. Before it gates any merge:

1. Have two people label the same 50 to 100 outputs against each criterion, with written guidelines.
2. Measure how often the two people agree. That is the ceiling: a judge cannot be more reliable than the humans it imitates.
3. Measure how often the judge agrees with the people, **per criterion**.
4. Rewrite the criteria with low agreement. A low score usually means a vague question, not a bad judge.

### 6. Handle flakiness

Both the model under test and the judge can vary between runs. Four habits keep the suite trustworthy:

- Compare parsed fields, never raw text.
- Assert **strictly** for musts and **as a rate** for shoulds.
- Fix a seed where the provider supports one.
- Run each case a few times when a result is close to the threshold, before calling it a regression.

### 7. Run it in tiers inside CI

| Tier | What runs | Cost and time |
|---|---|---|
| Every commit | Code checks on canned outputs | Free, under a second |
| Every pull request | 20 to 50 fixed cases, musts and shoulds | Cents, a few minutes |
| Nightly | Full set, held-out set, repeated runs for variance | Dollars |

Put the LLM tests in a separate job from unit tests. Unit tests answer "is the code broken?". LLM tests answer "is the behavior still good?". A flaky model call must not block a typo fix.

### 8. Review what the judge says

Log every verdict with its evidence. When a test fails, ask first whether the *judge* is wrong. Sample a few passing verdicts too. A judge that approves everything is worse than no judge.

## Worked example

A `pytest`-style suite for the summarizer. The `ask` function stands in for your provider's SDK. The whole listing is illustrative pseudocode: it was not checked against current API documentation and it is not meant to run as pasted.

```python
# llm.py -- illustrative pseudocode for a chat-model call. Each call costs money.
import json

def ask(system: str, user: str) -> str:
    return client.chat(model=MODEL, temperature=0.0, messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}]).text

SUMMARIZER = ('Summarize the support conversation for the next agent in at most '
              'three sentences. Reply with JSON only: {"summary": "..."}')

def summarize(thread: str) -> str:
    return json.loads(ask(SUMMARIZER, thread))["summary"]
```

```python
# test_summarizer.py
import json
import pytest
from llm import ask, summarize

JUDGE = """You grade a summary of a support conversation.
Answer the question with "yes" or "no".
Copy the exact words from the summary that justify your answer.
Reply with JSON only: {{"answer": "yes or no", "evidence": "quoted words"}}

Conversation:
{thread}

Summary:
{summary}

Question: {question}"""

def judge(thread: str, summary: str, question: str) -> bool:
    """One paid call per question."""
    prompt = JUDGE.format(thread=thread, summary=summary, question=question)
    verdict = json.loads(ask("You are a careful grader.", prompt))
    if verdict["evidence"] not in summary:
        raise ValueError(f"judge invented its evidence: {verdict['evidence']!r}")
    return verdict["answer"] == "yes"

MUSTS = [  # hard requirements: every case must pass, every time
    "Does every fact in the summary appear in the conversation?",
    "Does the summary say how the conversation ended: resolved, pending, or no reply?",
    "Does the summary promise only actions that someone in the conversation agreed to?",
]
SHOULDS = [  # quality preferences: judged as a pass rate
    "Is the summary neutral, blaming no one?",
]
CASES = [
    pytest.param(
        "Customer: I was charged twice for order 42.\n"
        "Agent: Sorry about that. I refunded $42; it arrives within 3 days.",
        ["42"], id="double-charge"),
    pytest.param("Customer: Hello? Is anyone there?", [], id="no-reply"),
    pytest.param(
        "Customer: My app crashed while I was paying, and the invoice "
        "address is wrong.\nAgent: Let me check both and get back to you.",
        ["crash", "address"], id="two-issues-pending"),
]

_summaries = {}  # several tests need the same summary: pay for it once

def summary_of(thread: str) -> str:
    if thread not in _summaries:
        _summaries[thread] = summarize(thread)
    return _summaries[thread]

# 1. Free checks first. No judge needed.
@pytest.mark.parametrize("thread, required", CASES)
def test_hard_checks(thread, required):
    summary = summary_of(thread)
    for word in required:
        assert word in summary, f"{word!r} missing from: {summary}"
    assert len(summary.split()) <= 80, "summary is too long"

# 2. Hard requirements: strict, one test per case and criterion.
@pytest.mark.parametrize("thread, _", CASES)
@pytest.mark.parametrize("question", MUSTS)
def test_must_criteria(thread, _, question):
    summary = summary_of(thread)
    assert judge(thread, summary, question), f"FAILED: {question}\nSummary: {summary}"

# 3. Quality preferences: a rate, because judge and model both vary.
def test_should_criteria_pass_rate():
    checks = [judge(t, summary_of(t), q) for t, _ in CASES for q in SHOULDS]
    assert sum(checks) / len(checks) >= 0.8, f"{sum(checks)} of {len(checks)} passed"
```

What to observe:

- **Cost.** One run makes 3 summarizer calls and 12 judge calls, roughly 7,000 tokens. At an assumed blended price of $0.50 per million tokens that is under half a cent. Replace the assumption with your provider's price, which varies widely as of 2026-11-24. A nightly run of 200 cases with six criteria each is about 650,000 tokens, or roughly $0.33 under the same assumption.
- **The `no-reply` case** is there to tempt the model into inventing an outcome. The third must-criterion is the test that should catch it.
- **The evidence check** turns an unreliable grader into a reviewable one. A verdict with invented evidence raises an error instead of failing the test, because the fault is in the judge.
- **The musts are strict.** If the `double-charge` summary omits the amount, `test_hard_checks` fails and names the missing string.

## What the practitioners say

Kästner's chapter 15 is the source, and it predates most current judge practice.

- **Three ways to judge generated output.** He lists similarity to a reference, human judgment, and property evaluation (chapter 15).
- **Similarity is a weak fit.** Word-overlap measures such as BLEU and ROUGE compare word sequences. Embedding distance captures meaning better. He notes both are hard to choose for a new task, and of little use when many answers would be acceptable (chapter 15).
- **Human judgment follows criteria.** People should rate outputs against predefined criteria, for example whether a summary is helpful, names the main points, and stays concise. He warns that this is needed after *every* evaluation during development, not once, and becomes expensive at scale (chapter 15).
- **Solo spot checks mislead.** Developers often judge a few examples themselves. It gives a feel for quality and little insight into how general the result is (chapter 15).
- **Some properties need a model.** He names length and vocabulary as properties a program can check, and uses an LLM deciding whether two texts mean the same as an example of a model-checked property (chapter 15).
- **Models can write the tests.** He describes prompting an LLM for test data with specific traits, such as a sarcastic one-line review of a watch, and cites AdaTest, a tool that loops between error analysis and LLM-generated tests (chapter 15).
- **For prompts, test like software.** The chapter's further readings point to Marco Tulio Ribeiro's 2023 essay on testing language models and prompts the way software is tested. For judge design and for the known judge biases, see [LLM-as-a-Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md) in part 03.

## Pitfalls

1. **One vague criterion.** "Is it good?" cannot be calibrated. Fix: split it into specific yes-or-no questions.
2. **Asking the judge what code can check.** Slower, costlier, and less reliable. Fix: code first, judge second.
3. **Gating merges on an uncalibrated judge.** Fix: measure agreement with people per criterion before it can block a merge.
4. **Asserting exact text.** Sampled output always differs in wording. Fix: parse fields, compare facts, use rates.
5. **Running every LLM test on every commit.** The suite is slow, flaky, and resented. Fix: tiers, and a separate CI job.
6. **Blaming the model for every red test.** Fix: read the evidence, and audit the judge before the component.
7. **Tuning the prompt on the test cases.** Fix: keep a held-out set for the reported number.

## Try it

Take one LLM component you can call.

1. Write a rubric of six criteria, each marked must or should, each with its cheapest oracle.
2. Build 30 cases, including five designed to tempt a specific failure.
3. Implement the suite in three parts, as in the example.
4. Label the 30 outputs yourself against every criterion, then measure the judge's agreement with you, per criterion.

You are done when the suite runs from one command, reports failures with evidence, costs less than ten cents per run, and shows at least 80 percent agreement with your labels on every must-criterion. Rewrite any criterion below that mark until it reaches it. **Stretch goal:** have a second person label the same 30 outputs and compute how often the two of you agree.

## Key takeaways

- A rubric turns "good output" into yes-or-no questions. Each question is an oracle.
- Use the cheapest oracle that works: code for anything checkable, an LLM judge for meaning, people for calibration.
- Ask the judge one question at a time, with the source beside the output, and make it quote evidence you can verify.
- Calibrate the judge against human labels, criterion by criterion, before it can block a merge.
- Assert musts strictly and shoulds as a rate. Expect some run-to-run variation.
- Run LLM tests in tiers and in a separate CI job, on a fixed cost budget.

## Self-check

1. A reviewer says the summaries "look good". What is the first thing to ask for?
2. Which oracle should check "the output is valid JSON", and why that one?
3. Why compare a judge's verdicts with human labels one criterion at a time?
4. A must-criterion test fails. The judge's evidence is a sentence that is not in the summary. What happened?
5. Why are should-criteria asserted as a rate while musts are strict?

<details><summary>Show answers</summary>

1. The criteria behind the judgment. "Good" is not testable until it is split into specific yes-or-no questions.
2. Code. It is exact, free, and instant, and a judge would be slower, costlier, and less reliable for it.
3. Agreement is a property of the question, not only of the judge. A low score on one criterion points to a vague question to rewrite, which an overall agreement figure would hide.
4. The judge failed, not the component. The evidence check raised an error so that a grader's mistake is not reported as a product defect.
5. Hard requirements admit no exceptions, so each case must pass. Preferences are judged inconsistently by both the model and the judge, so only their frequency over many cases is stable.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 15: [link](https://mlip-cmu.github.io/book/15-model-quality.html)
- **Reading:** Marco Tulio Ribeiro, "Testing Language Models (and Prompts) like We Test Software" (2023), listed in the chapter's further readings: [link](https://medium.com/towards-data-science/testing-large-language-models-like-we-test-software-92745d28a359)

## Next

→ [Data Quality](06-data-quality.md), because a model can only be as good as the data that reaches it, and data bugs hide longer than code bugs.
