# 03. From Base Model to Assistant: Post-Training

**Level:** Practitioner · **Reading time:** 30 min · **Exercise:** 60 min
**Prerequisites:** [How Large Language Models Are Trained](02-how-large-language-models-are-trained.md) (the training loop and what a base model is)

> **In one sentence:** After this chapter you can explain what each post-training stage adds to a base model, and choose between prompting, fine-tuning, preference tuning and reinforcement learning for a product.

## Why this matters

You can download a base model today. Ask it a question and it answers with more questions, because it only continues text ([Chapter 02](02-how-large-language-models-are-trained.md)). The chat model you call through an API behaves differently. It answers, follows instructions, refuses some requests and reasons step by step.

Something was done to it. If you want a model to behave differently for your product, you have to know what that something is. You also have to choose a lever, and the levers differ by two orders of magnitude in cost.

## The core idea

**Post-training** is every training stage that comes after pre-training. It uses the same loop you met in [Chapter 01](01-machine-learning-in-a-nutshell.md): parameters, a loss, small nudges. What changes is the objective. Pre-training rewards predicting the next token of web text. Post-training rewards something you actually want.

Yann Dubois states the problem in his Fall 2025 lecture. Pre-training data scales, but it is not what you want. The answers you want are scarce and expensive ([58:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=3480)). Post-training is the bridge: a pre-trained model plus a little of the right data.

It comes as a ladder. Each rung optimizes a different thing, from a different kind of data. The top three rungs rely on **reinforcement learning (RL)**: the model tries, a score called a **reward** rates the try, and training nudges the model toward the tries that scored higher.

| Rung | What it optimizes | The data | An algorithm |
|---|---|---|---|
| Supervised fine-tuning | Imitating good answers | Prompt and answer pairs | Next-token loss on the answer |
| Preference tuning | Answers people prefer | Prompt, two answers, a choice | RLHF with PPO, or DPO |
| RL with verifiable rewards | Answers a program accepts | Tasks with checkable answers | GRPO and similar |
| Agentic RL | Task success in an environment | Environments, tools, verifiers | RL on whole trajectories |

An analogy is onboarding a brilliant new hire. Pre-training is their education. Supervised fine-tuning is showing them examples of good work. Preference tuning is reviewing pairs of their drafts and saying which is better. Verifiable-reward training is handing them problems with an answer key and letting them practice until they solve them. The analogy breaks on memory. The hire keeps what they learn. The model changes only when a training run updates its parameters.

## How it works, step by step

### 1. Supervised fine-tuning: imitate good answers

**Supervised fine-tuning (SFT)** keeps the pre-training objective and changes the data. The model practices predicting the tokens of a good answer, given a prompt. "Supervised" means each prompt comes with a target answer.

- **What it teaches.** Dubois lists instruction following, format and style, tool use and early reasoning ([64:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=3840)).
- **How much data.** His slides report that about 10,000 examples are enough for style and instruction following. DeepSeek-R1 used about 800,000 to teach reasoning ([66:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=3960)).
- **Why so little works.** His mental model: the knowledge is already in the pre-trained model. SFT selects one way of using it, as if specializing to one kind of user (same moment).
- **Where the answers come from.** From people, which is slow. From a stronger model, which is the idea of Alpaca. Or by **rejection sampling**: let a model write many answers and keep the ones a checker accepts, as DeepSeek-R1 does.

Hanna Hajishirzi's team, which builds the open Tülu recipes, adds two findings. Step-by-step solutions train better than bare final answers ([20:00](https://www.youtube.com/watch?v=cMiu3A7YBks&t=1200)). And data quality beats quantity: on her slides, about 60% of the curated data gave the same or better results.

Jiantao Jiao, in his Fall 2025 lecture, adds a warning about the dose. SFT should be light, and its examples diverse. A model fine-tuned heavily on one "right" answer per question loses the ability to find answers itself ([46:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=2760)).

### 2. Why imitation is not enough

Dubois describes SFT as behavior cloning, and names three costs ([68:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4080)):

1. **It is bounded by what people can write.** People can recognize a better answer than they can produce.
2. **It teaches hallucination.** If the training answer contains a reference the model never saw, the lesson is: produce plausible-looking references even when you do not know.
3. **Good answers are expensive.**

So the next rungs replace "copy this" with "be judged".

### 3. Preference tuning: reward models, RLHF and DPO

For an open-ended request there is no correct answer to copy. There are only judgments: of these two answers, this one is better. Two methods use them.

- **RLHF**, or reinforcement learning from human feedback, works in two training phases. First, people compare pairs of answers to the same prompt. A **reward model**, a second model trained on those comparisons, learns to score answers. Then the language model is trained by RL to maximize that score.
- **DPO**, or direct preference optimization, removes the reward model and the RL loop. It applies a loss directly to the language model: raise the probability of the preferred answer and lower that of the rejected one.

Dubois walks through the original RLHF pipeline: an instruction goes to an SFT model, which writes two answers; labelers pick the better one; the model is then trained to produce more answers like the winner. He adds: "This is really what made ChatGPT work in 2022" ([78:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4680)). The optimizer used for the second phase is usually **PPO**, proximal policy optimization, which improves the model in small clipped steps. His slides show the ordering of results: pre-trained, then SFT, then RL, each better than the last.

Human preference data has known problems, which he lists ([80:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4800)). It is slow and expensive. People judge form, such as length, more than content. The results depend on who the annotators are. A common replacement is an LLM judge: AlpacaFarm used model preferences, and Jason Weston's **self-rewarding language models** let a model score its own answers and train on them in a loop ([40:00](https://www.youtube.com/watch?v=_MNlLhU33H0&t=2400)).

A further risk is **over-optimization**. The model learns to please the reward model in ways people did not intend, such as writing longer. Hajishirzi's slides devote several to this. One remedy is to prefer rewards that are rules.

### 4. Reinforcement learning with verifiable rewards

A **verifiable reward** comes from a program, not from a person or a learned model: a string match, a math check, a unit test that passes. **RLVR**, reinforcement learning with verifiable rewards, trains the model on tasks with such a checker.

- **It is older than it looks.** Hajishirzi calls RLVR the third stage of Tülu 3, and notes that RL on binary signals is not new. What is new is that rule-based rewards make it practical, and that it works better as models grow ([49:21](https://www.youtube.com/watch?v=cMiu3A7YBks&t=2961)).
- **How one step looks.** Dubois explains GRPO, the algorithm DeepSeek-R1 used ([72:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4320)). The model writes several answers to one question. A checker scores each. The scores are compared within the group, and answers above the group's average are made more likely, the others less. A penalty keeps the model close to its starting point, so it cannot drift anywhere it likes.
- **Which tasks.** In DeepSeek-R1, as Dubois describes it, math, code and logic prompts got rule-based checkers. Open-ended writing still used a reward model.

**Reasoning models** are trained this way on hard problems with checkable answers. They learn to write a long chain of thought before the final answer, because that raises their score. OpenAI's o1 (2024) made the approach public. DeepSeek-R1 (January 2025) published a recipe. Weston's slides note that o1's exact method is unknown.

Jiao extends the idea from single answers to whole tasks, which is the last rung. An **agentic model**, in his definition, is aligned to environment feedback and maximizes verifiable rewards in addition to human preference ([0:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=0)). Its training data has three parts:

1. **Environments** the model must understand, such as a code repository or a browser.
2. **Tools** it can call.
3. **Verifiers** that judge the result: unit tests, proof checkers, page checks.

His two rules: verifiers must be diverse, and their quality matters. A verifier must neither accept wrong answers nor reject correct ones. His example is a change problem where ½ and 2/4 are both right, unless the question asks for the simplest form (his slides). He also argues for judging more than correctness: cost in steps and tokens belongs in the score too ([14:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=840)).

### 5. Jiao's recipe: imitate, then explore

Jiao's principle for the order of stages is "imitate first and then explore". SFT removes meaningless attempts. RL then reinforces attempts that succeed. His summary: "RL is there to truly reinforce intelligence" ([48:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=2880)). He names three pillars of good RL:

1. **Train longer.** Watch for **entropy collapse**. As the reward rises, the model becomes certain of one answer per prompt and stops exploring ([58:00](https://www.youtube.com/watch?v=3l0Zxus34es&t=3480)).
2. **Train on hard tasks**, ones with a low but nonzero chance of success. A task everyone solves or nobody solves teaches nothing.
3. **See diverse responses** with high-quality feedback.

### 6. Open training recipes

Tülu 3, from Hajishirzi's group and AI2, is a fully open recipe: base model, SFT, preference tuning with DPO, then RLVR, with data and code published ([10:00](https://www.youtube.com/watch?v=cMiu3A7YBks&t=600)). Her argument is that open recipes are how the field learns which parts matter. Her team's comparisons found that PPO beat DPO for preference tuning, and that high-quality data was the most important factor of all (her slides). Dubois makes a similar point at the start of his lecture: a lab can hide almost anything about a model, but the data recipe is where the work goes ([40:00](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=2400)).

## Worked example

The three kinds of post-training data, and the code that makes the third kind work:

```python
import re
from math import isclose

sft_row = {"prompt": "Explain recursion in one sentence.",
           "answer": "Recursion is a function that solves a problem by calling itself on a smaller case."}

preference_row = {"prompt": "Explain recursion in one sentence.",
                  "chosen": "Recursion is a function that solves a problem by calling itself on a smaller case.",
                  "rejected": "Recursion is when recursion happens."}

task = {"question": "What is 17 * 23?", "answer": "391"}      # for RLVR: a program can check it

def reward(model_output, task):
    """Rule-based verifier: 1 if the number after 'Final answer:' is right, else 0."""
    tail = model_output.split("Final answer:")[-1]
    numbers = re.findall(r"\d+(?:\.\d+)?", tail)
    return int(bool(numbers) and isclose(float(numbers[-1]), float(task["answer"])))

print(reward("17 * 23 = 391. Final answer: 391", task))   # 1
print(reward("Let me compute. Final answer: 390", task))  # 0
print(reward("I am not sure.", task))                     # 0
```

What to observe:

- The reward is ordinary code. You can unit-test it, review it and version it. That is the whole advantage of verifiable rewards.
- A near miss and a non-answer both score 0. The signal is binary, so the model needs many attempts per task.
- The same `reward` function lets you build SFT data by rejection sampling: sample many answers, keep those that score 1.

## Pitfalls

1. **Fine-tuning to add knowledge.** SFT mainly teaches format and behavior. *Fix:* put facts in the prompt or attach them by retrieval. Fine-tune for style, format and tool use.
2. **Training on answers the model cannot know.** You reward confident invention. *Fix:* fine-tune only on what it can learn, or use checkable tasks.
3. **Choosing by data volume.** *Fix:* curate for quality and diversity, then measure with an ablation.
4. **Over-optimizing a learned reward model.** The output gets longer and more flattering. *Fix:* prefer rule-based rewards, keep the drift penalty, and evaluate with people on fresh prompts.
5. **Tuning before evaluating.** *Fix:* define evaluations for each target skill first, as the Tülu team does.
6. **Starting at the top of the ladder.** *Fix:* climb. Prompt, then SFT, then preference tuning, then RLVR.
7. **A weak verifier.** A checker with false accepts trains the wrong behavior. *Fix:* test the verifier with correct answers in every allowed form.

## Try it

**Deliverable:** three data files and one tested checker for a single task of your choice.

1. Write 20 SFT rows, 20 preference rows and 20 verifiable tasks, each as one JSON object per line.
2. Write the checker for the verifiable tasks. Unit-test it with right answers in several forms, wrong answers and non-answers.
3. With any chat model you can call, sample 16 answers per verifiable task. Record how many pass.
4. Convert every passing answer into an SFT row.

Calling a hosted model 320 times costs well under one dollar with a small model (estimate, as of November 2026; check your provider's prices).

**You are done when:** the checker's tests include at least one case that must not be accepted; the three files parse line by line; and you report the share of tasks solved 0 times in 16 and the share solved 16 times. Those are the tasks Jiao says teach nothing.

**Stretch goal:** fine-tune a small open model on your SFT rows with an open recipe such as Tülu. This needs a GPU or a rented one. Compare it against the base model on held-out tasks.

## Key takeaways

- Post-training is the same training loop with a new objective and far less data than pre-training.
- SFT imitates good answers. It teaches format, instruction following and tool use, but cloning what the model cannot know teaches it to invent.
- Preference tuning optimizes what people prefer: RLHF through a reward model and PPO, or DPO directly on pairs. Watch for over-optimization.
- RLVR optimizes what a program can check. It is how reasoning models learn to think at length, and it extends to whole tasks through environments, tools and verifiers.
- Imitate first, then explore. Then train long on hard tasks without letting the model collapse to one answer.
- Climb the ladder: prompt, SFT, preference tuning, RLVR. Each rung costs more than the one below.

## Self-check

1. What does supervised fine-tuning optimize?
   - A. The next-token loss on provided good answers
   - B. The score of a separately trained reward model
   - C. The pass or fail result of a unit test
   - D. The share of human votes won against another model

2. How can SFT teach a model to hallucinate?
   - A. By cloning answers that contain facts the model never knew
   - B. By lowering the sampling temperature during the training run
   - C. By removing the rare tokens from the tokenizer's vocabulary
   - D. By training on web text that was never deduplicated

3. What does DPO leave out compared with RLHF?
   - A. The separate reward model and the RL loop
   - B. The pairs of preferred and rejected answers
   - C. The supervised fine-tuning stage before it
   - D. The evaluation that follows the training

4. What supplies the reward in RLVR?
   - A. A program that checks the answer
   - B. A crowd of human voters on answer pairs
   - C. A reward model trained on human preferences
   - D. The model's own confidence in its output

5. As reported on Dubois's slides, about how many examples does SFT need to teach style and instruction following?
   - A. About ten thousand
   - B. About ten trillion
   - C. About one hundred
   - D. About one million

6. During RL, a model's reward rises and it starts giving the same answer to every prompt. What did Jiao call this?
   - A. Entropy collapse
   - B. Over-optimization
   - C. Data contamination
   - D. Reward sparsity

<details><summary>Show answers</summary>

1. A. SFT reuses the pre-training objective on chosen prompt-answer pairs.
2. A. The model learns that a confident-sounding invented reference is a correct answer.
3. A. DPO applies a loss directly to the language model on the preference pairs.
4. A. A rule, such as a string match or a passing test. No human or learned model sits in the loop.
5. A. About 10,000, against about 800,000 for DeepSeek-R1's reasoning data.
6. A. The model stops exploring. Jiao's first pillar is to train longer while avoiding this.

</details>

## Sources

- **Lecture:** Yann Dubois, "Introduction to training LLMs for AI agents", LLM Agents MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=r1qZpYAmqmg), used at [why post-training](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=3480), [what SFT teaches](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=3840), [limits of imitation](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4080), [GRPO](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4320), [RLHF](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4680), [human data](https://www.youtube.com/watch?v=r1qZpYAmqmg&t=4800)
- **Lecture:** Jiantao Jiao, "Post-Training Verifiable Agents", Agentic AI MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=3l0Zxus34es), used at [agentic models](https://www.youtube.com/watch?v=3l0Zxus34es&t=0), [verifiers](https://www.youtube.com/watch?v=3l0Zxus34es&t=840), [light SFT](https://www.youtube.com/watch?v=3l0Zxus34es&t=2760), [imitate then explore](https://www.youtube.com/watch?v=3l0Zxus34es&t=2880), [entropy collapse](https://www.youtube.com/watch?v=3l0Zxus34es&t=3480)
- **Lecture:** Hanna Hajishirzi, "Open Training Recipes: LLM Reasoning", Advanced LLM Agents MOOC (Spring 2025): [video](https://www.youtube.com/watch?v=cMiu3A7YBks), used at [the Tülu 3 recipe](https://www.youtube.com/watch?v=cMiu3A7YBks&t=600), [step-by-step data](https://www.youtube.com/watch?v=cMiu3A7YBks&t=1200), [RLVR](https://www.youtube.com/watch?v=cMiu3A7YBks&t=2961)
- **Lecture:** Jason Weston, "Learning to Self-Improve & Reason with LLMs", Advanced LLM Agents MOOC (Spring 2025): [video](https://www.youtube.com/watch?v=_MNlLhU33H0), used at [self-rewarding models](https://www.youtube.com/watch?v=_MNlLhU33H0&t=2400)

## Next

→ [Using LLMs: Tokens, Context and Sampling](04-using-llms-tokens-context-and-sampling.md). Post-training produced the assistant. The next chapter covers how to call it: tokens, sampling parameters, context limits and cost.
