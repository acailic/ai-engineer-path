# 09. Evaluating Language Models

**Level:** Practitioner · **Reading time:** 14 min · **Exercise:** 45 min

> **In one sentence:** After this chapter you can pick the kind of evaluation that answers the question you actually have, and name the failure modes that make a benchmark number misleading.

## Why this matters

A leaderboard says model A scores higher than model B. You must pick one for a customer-support bot, and you have a week. Is the score about knowledge, about writing style, about solving problems with tools? Was the test set public when the models were trained? Did anyone ask questions like your customers ask?

CS336's evaluation lecture starts from a plain claim: evaluation looks mechanical. Write prompts, get responses, compute accuracy. It is not mechanical, because "good" is an abstract idea and a benchmark is one concrete stand-in for it ([0:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=0)).

## The core idea

Evaluation turns an abstract construct, such as "good at conversation", into a concrete metric. Every step of that translation is a choice, and each choice fits some questions and misleads others.

The lecture's first takeaway is that there is no single true evaluation. It depends on what you want to know ([76:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=4560)):

| Why you evaluate | What you need |
|---|---|
| Choose between two models for your use case | Tests on your own tasks, including cost and latency |
| Measure raw capability | Hard, broad tasks with little memorized content |
| Understand benefits and harms | Coverage of risky behavior, in context |
| Get feedback while developing the model | Cheap, stable metrics you can run on every run |

Three properties pull against each other:

- **Difficulty**: hard enough that strong models have not saturated it.
- **Realism**, which the lecture calls **ecological validity**: how close the test is to real use.
- **Validity**: the test measures what it claims. The usual threat is **contamination**, test data that was part of the training data.

## How it works: the kinds of evaluation

### Perplexity

**Perplexity** asks how much probability the model assigns to text it has never seen:

`(1 / p(D))^(1 / |D|)`

`p(D)` is the probability the model gives the whole document D, and `|D|` is its length in tokens. The result reads as the number of equally likely tokens the model is torn between at each step. Lower is better.

Perplexity is cheap and moves smoothly as models scale, which makes it the metric behind scaling laws (Chapter 07). It is also blind to what matters in a reply: the lecture's example is the sentence "Stanford was founded in 1885", where every word is scored, not the one you wanted. A narrower version scores only the answer: `p(response | prompt)^(1 / |response|)`.

### Exams

Multiple-choice exams give control over subject and difficulty and are easy to grade.

| Benchmark | Shape | Figure quoted in the lecture |
|---|---|---|
| MMLU | 57 subjects, multiple choice | Tests knowledge more than the name "language understanding" suggests |
| MMLU-Pro | Noisy questions removed, 10 options, chain of thought | Accuracy falls 16% to 33% |
| GPQA | Questions written by 61 PhD-level contractors | PhD experts 65%, non-experts with web access 34%, GPT-4 39% |
| Humanity's Last Exam | 2,500 questions, several formats, filtered by frontier models | $500K in prizes for question authors |

The trend is toward harder questions as models saturate the old ones, and the treadmill shows in the numbers. For MMLU-Pro, noisy and trivial questions were removed and four options became ten, with chain of thought expected. Accuracy fell to 33% and has since climbed back to nearly 90%, which in the lecturer's view makes this benchmark a little too easy as well ([22:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=1320)). GPQA's test of a good question: if you can solve it by searching the web, it is too easy, because the model was trained on the web. Its questions came from 61 PhD-level contractors and went through expert validation ([24:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=1440)).

### Open-ended chat

Nobody asks an assistant multiple-choice questions. For free-form answers there are two routes:

- **Human preference.** Chatbot Arena shows each visitor two anonymous responses to their own prompt and records which one wins. Ratings are combined into an **Elo** score, the rating method from chess: `p(A beats B) = 1 / (1 + 10^((Elo_B − Elo_A) / 400))`.
- **Model as judge.** AlpacaEval scores a model's win rate against a reference model, with a strong LLM as the judge. WildBench takes prompts from real conversations and gives the judge a checklist to work through.

Both have known biases. Voters are whoever showed up: the lecturer calls Arena a wild west, with possible spammers and self-interested teams. A binary preference mixes style with correctness, which makes Elo cleaner for chess, where only winning matters, than for answers. Voters ask a question because they do not know the answer, and sycophancy rewards pleasing answers over honest ones. The strength of Elo is that not every model has to answer the same prompts. A sparse sample suffices as long as the comparisons form a connected graph ([36:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=2160)). Judges favor longer answers, which led to gaming on AlpacaEval until version 2.0 corrected for length.

### Agents

An **agent** is a model plus a **scaffold**, the code that decides when the model runs, what tools it gets and how it remembers. Agent benchmarks test what the model does: SWE-bench (2,294 tasks from 12 Python repositories, graded by unit tests), Terminal-Bench (229 terminal tasks), CyBench (40 capture-the-flag tasks), MLEBench (75 machine-learning competitions). The lecture's warning: you are evaluating the scaffold and the model together.

### Reasoning, safety and real work

- **Reasoning** apart from knowledge: ARC-AGI, whose puzzles are solvable by people, unique enough that memorization does not help. Pretrained models made no progress on it at all, as its creators intended; reasoning models did ([56:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=3360)).
- **Safety**: HarmBench (510 harmful behaviors) and AIR-Bench (314 risk categories, 5,694 prompts). Safety is contextual, and tools such as capable cybersecurity agents are dual-use.
- **Real work**: GDPVal (44 occupations), MedHELM (121 clinical tasks), and Clio, which analyzes real usage. The lecture notes that realism and privacy are often at odds.

## How it works: keeping evaluations valid

**Contamination** is the quiet failure. Four routes from the lecture:

1. Infer the overlap from the model's own behavior. A model that consistently prefers one option order, in line with the benchmark, probably trained on it.
2. Expect providers to report overlap, as they report confidence intervals. The lecturer argues for a norm: a claimed GPQA score should come with justification that the test set was not trained on ([70:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=4200)).
3. Use fresh evaluations built from newly scraped material (LiveCodeBench, UncheatableEval), past the models' cutoff. His caveat: timestamps are not always safe, since new code can be derived from an old repository ([70:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=4200)).
4. Use private evaluations: internal code, or your own writing. His example is a folder of rejected papers never put online. He adds that private data suits perplexity evaluation well, because it needs only a good dataset and log probabilities ([72:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=4320)).

Dataset quality is the other half. SWE-bench was repaired into SWE-bench Verified; other benchmarks have "Platinum" versions. Agentic benchmarks fail in their own ways: too few test cases, or tasks a trivial agent can solve.

A last distinction: before foundation models, researchers evaluated methods on fixed train-test splits. Today they mostly evaluate whole systems, where anything goes. Both are fine, but say which game you are playing.

## Worked example

A crude contamination check in a few lines:

```python
def shingles(text, n=8):
    """All sequences of n consecutive words, lowercased."""
    words = text.lower().split()
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}

def overlap(question, training_text, n=8):
    """Fraction of the question's word sequences that occur in the training text."""
    q = shingles(question, n)
    return len(q & shingles(training_text, n)) / max(len(q), 1) if q else 0.0   # a question under n words has no shingles

copied = "What is the capital of France and why is it called the City of Light?"
training = "Practice quiz: what is the capital of France and why is it called the City of Light?"
print(overlap(copied, training))                       # 1.0: every 8-word run of the question is present
print(overlap("Name France's capital city.", training))  # 0.0
```

What to observe:

- The copied question is caught: every one of its 8-word sequences appears in the training text.
- A short paraphrase with no run of eight words in common scores zero, so the check finds copying, not paraphrasing.
- Lowering `n` catches more and raises false alarms. That trade-off is yours to tune.

## What the practitioners say

The lecturer's framing is that evaluation shapes the field, because it sets the goals everyone then optimizes: "Evaluation sets North Stars" ([0:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=0)).

On perplexity, the lecturer calls the argument for it possibly fantastical, and presents it as a strong driver of scaling work rather than as settled ([10:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=600)). The argument is that the best achievable perplexity belongs to the true distribution of text, and a model that reached it could solve any task. The lecturer credits that belief with sustaining scaling work before the payoff was obvious, before GPT-3, while also noting that perplexity scores more than you need.

On exams, the stated problem is that they do not capture real usage ([30:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=1800)). On human and model judges, the lesson is that pairwise comparisons between similar answers carry more signal than absolute scores, and that a checklist improves reliability for either kind of judge ([44:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=2640)).

The closing advice has two parts. First, "there's no one true evaluation, choose what you're trying to measure" ([76:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=4560)). Second, a warning about trade-offs: "It's hard to have really real and difficult and ecologically valid and no training test contamination" ([78:00](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=4680)). Something has to give, and the question you are asking decides what.

## Pitfalls

1. **Choosing a benchmark by habit.** Fix: write down the decision the evaluation supports, then pick.
2. **Comparing perplexity across tokenizers.** Fix: compare only models with the same tokenizer.
3. **Trusting a public test set.** Fix: run a contamination check and keep a private set.
4. **Treating one score as the whole model.** Fix: report a small set of measures with confidence intervals.
5. **Letting one kind of eval drive data mixing.** Code benchmarks make you upweight code until poetry suffers (Chapter 10). Fix: hold out a broad set.
6. **Evaluating an agent as if it were a model.** Fix: state the scaffold, and compare models within the same scaffold.
7. **Ignoring a single judge's bias.** Fix: check length and style effects, or use several judges.

## Try it

Pick two open-weight models you can run or call.

**Deliverable:** a one-page evaluation report for a use case you choose.

You are done when:

- The report states the decision the evaluation supports, in one sentence.
- It includes 20 prompts of your own that resemble the use case, with expected properties for each answer.
- It reports scores for both models with a short note on what a judge could get wrong.
- It shows the result of the shingle overlap check between your prompts and one public document collection, calling `overlap` once per document and keeping the largest value, or states why that check does not apply.
- The recommendation names what was traded away: difficulty, realism or validity.

**Stretch:** add a second judge or a human rating for 5 prompts and report where the two disagree.

## Key takeaways

- Evaluation turns an abstract idea of "good" into a metric. No single metric is the true one.
- Perplexity is cheap and smooth. Exams control difficulty. Arenas and judges handle open-ended answers. Agent benchmarks test action.
- Every evaluation trades between difficulty, realism and validity.
- Contamination and dataset quality decide whether a score means anything.
- State the rules: which model, which scaffold, which judge, which data.

## Self-check

1. What is the basic difficulty of evaluation?
   - A. Models are too expensive to run on large test sets
   - B. Turning an abstract idea of quality into a concrete metric
   - C. Benchmarks are always published without answers
   - D. Human raters refuse to compare two responses
2. What does perplexity measure?
   - A. The percentage of exam questions answered correctly
   - B. The average length of a model's responses
   - C. How much probability the model gives to unseen text
   - D. The number of parameters used per token
3. Why did AlpacaEval need a version 2.0?
   - A. Its prompts were all multiple choice
   - B. The judge favored longer answers, which invited gaming
   - C. It required human voters
   - D. Its test set was private
4. What does an agent benchmark actually evaluate?
   - A. The model alone, with tools removed
   - B. The training data of the model
   - C. Only the model's perplexity on code
   - D. The model together with its scaffold
5. Which combination does the lecture call hard to achieve at once?
   - A. Low cost, high speed and small size
   - B. Being realistic, difficult and free of contamination
   - C. A public test set and a large vocabulary
   - D. Human raters and model judges in agreement

<details><summary>Show answers</summary>

1. B. Every benchmark is one concrete stand-in for an abstract construct.
2. C. It is the probability of held-out text, normalized per token.
3. B. A regression was added to remove the length bias.
4. D. The scaffold decides tools, memory and control flow, so it is part of the result.
5. B. Realism, difficulty and freedom from contamination trade off against each other.

</details>

## Sources

- **Lecture:** Stanford CS336, "Lecture 12: Evaluation", Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=JpAxdTWQJxM) · [guide](../lectures/cs336-12-evaluation.md), used at [goals](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=0), [perplexity](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=600), [exams](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=1800), [closing](https://www.youtube.com/watch?v=JpAxdTWQJxM&t=4560)
- **Reading:** Percy Liang et al., "Holistic Evaluation of Language Models" (2022): [arXiv](https://arxiv.org/abs/2211.09110)
- **Reading:** Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023): [arXiv](https://arxiv.org/abs/2306.05685)
- **Reading:** David Rein et al., "GPQA: A Graduate-Level Google-Proof Q&A Benchmark" (2023): [arXiv](https://arxiv.org/abs/2311.12022)
- **Reading:** Carlos Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" (2023): [arXiv](https://arxiv.org/abs/2310.06770)

## Next

→ [Training Data](10-training-data.md), because the evaluations you choose decide what data you collect. For the product side of the same problem, see [evaluation is the product](../03-evaluation/01-evaluation-is-the-product.md), [a minimal eval harness](../03-evaluation/02-a-minimal-eval-harness.md), and [LLM as a judge and rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md).
