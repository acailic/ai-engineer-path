# 06. Evaluating Capabilities and Risks

**Level:** Professional · **Reading time:** 15 min · **Exercise:** 45 min
**Prerequisites:** [Evaluation Is the Product](01-evaluation-is-the-product.md)

> **In one sentence:** After this chapter you can explain what a dangerous-capability evaluation and a responsible scaling policy are, as an Anthropic co-founder described them in late 2024, and you can write capability tiers that decide what your own agent may be trusted with.

## Why this matters

Your agent works. Someone asks whether it can now be given the keys to production: the payment system, the deployment pipeline. "It has not misbehaved in our tests" is not an answer. It has two holes. The tests may not have asked hard enough. And the question is about **capability**, what the system can do in the worst case, not about **behavior**, what it did on a good day.

## The core idea

**Capability evaluation** measures what a model or an agent can do, including the things you do not want it to do. A **dangerous-capability evaluation** measures whether a system has crossed the line from "could not help with serious harm" to "could".

Ben Mann, a co-founder of Anthropic, gave a lecture on this at Berkeley on November 25, 2024. His first point was that measurement is very hard because of **elicitation**: the choice of prompts and techniques that draws a capability out of a model ([2:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=120)). Chain of thought, telling the model to reason step by step, is one such technique. A small change in prompting can change the output a great deal. A claim about a level of capability has to hold even if somebody later finds "some breakthrough new technique for elicitation". Otherwise a measurement of what the model did is mistaken for a measurement of what it can do.

His second point was that the answer is to measure early and to commit in advance. That is the **Responsible Scaling Policy (RSP)**, which he describes as Anthropic's public commitment that model capability will not outstrip the company's ability to build effective guardrails for that capability.

> **Since the lecture.** This chapter describes the policy as Mann presented it on 2024-11-25. Anthropic has revised it several times since. When this was checked on 2026-11-24, the policy page showed version 3.4, effective 2026-07-08, still using the ASL labels and the term *Required Safeguards*. Read the current text before you rely on any level definition: [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy).

**The analogy, and where it breaks.** The RSP is modeled on **biosafety levels**, the rules that decide which precautions a laboratory needs for a given pathogen, from a lab coat up to a sealed suit. Mann makes the comparison himself ([12:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=720)). He also names where it fails ([22:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1320)). The dangerous pathogens already exist. The AI capabilities that would warrant the highest precautions do not exist yet, so the levels have to be forecast.

## How it works, step by step

### 1. Name the levels

Mann presented four **AI Safety Levels (ASL)**, as of his lecture:

| Level | As presented in the lecture | Examples he gave |
|---|---|---|
| ASL-1 | Smaller models, with no meaningful risk of harm to society | GPT-1, GPT-2, small Llama models |
| ASL-2 | Present large models, with early signs of potentially dangerous capabilities | Frontier models of the time: some information relevant to biological weapons, but not enough to raise the risk above using a search engine, or reachable only with expert knowledge |
| ASL-3 | Significantly higher risk: the model could significantly increase the risk of misuse | "We are preparing for ASL-3" |
| ASL-4 | Speculative | None yet |

### 2. Set the triggers

Two things move a model toward a new level: a capability threshold, shown by an evaluation, and a training-compute threshold. Mann says Anthropic hired biologists with the relevant expertise to help evaluate the models, and testified before the United States Senate about the models' biological capabilities ([14:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=840)).

### 3. Require the safeguards first

When a model approaches a new level, the policy requires the safety and security measures for that level to be ready. The commitment is not to develop or deploy a model at the next level until those measures are in place ([22:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1320)).

### 4. Publish and revise

Each new model ships with a report on the testing. Mann describes the goals as structure for hard decisions, public accountability, learning in public, and a template for policymakers ([12:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=720)). He compares the commitment to Odysseus tying himself to the mast. A lab with a finished model and no prior commitment may be tempted to deploy it without proper testing. An update published on October 15, 2024, as he describes it, lengthened the testing window after training from three to six months and added more testing at capability thresholds, even below the compute trigger ([14:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=840)).

### 5. Forecast the lag

If capabilities reach a level in two years and the safeguards take three, deployment waits a year. In an extreme case, safety falls so far behind that development pauses until it catches up ([28:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1680)).

## Why capability evaluation is harder than ordinary evaluation

1. **Elicitation.** The measured capability depends on how hard you tried to get it ([2:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=120)).
2. **The environment is part of elicitation.** Mann reads a benchmark result in which Claude 3.5 Sonnet beat OpenAI's o1-preview on agentic coding despite weaker raw reasoning. His explanation is the setup: one model wrote code as if on paper in an exam, the other wrote, ran, tested and iterated ([26:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1560)).
3. **Benchmarks do not last.** In his words, "just by defining a benchmark, we suddenly make massive advances in that area" ([24:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1440)). Scores rush past the human baseline and the benchmark saturates. Few benchmarks raise difficulty smoothly up to the levels that matter. As a different yardstick he cites an August 2024 evaluation by METR, a research organization, of how long a task a model can complete: roughly five minutes of human task time for Claude 3 Sonnet, ten for Opus, and about thirty for the earlier Claude 3.5 Sonnet.
4. **The target does not exist yet.** You are preparing for a capability nobody has measured ([22:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1320)).

One case shows the mindset. Anthropic released computer use, a model's ability to control a desktop, as a reference implementation in a GitHub repository rather than inside a product, because, as Mann put it, "nobody really knows how to make computer use safe yet" ([28:00](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1680)).

## From a lab's policy to your deployment decision

The lecture is about a frontier lab. The reasoning transfers to any team that grants an agent permissions. This translation is this chapter's, not the lecturer's.

| Idea in the RSP | In a team that ships an agent |
|---|---|
| Named risk levels | Tiers that state what the agent may touch |
| Capability thresholds, measured by evaluations | For each tier, the evaluation that admits a model, with a pass rule |
| Safeguards in place before the next level | Guardrails and monitoring that exist before the permission is granted |
| Commitment made in advance, in public | A short written policy agreed before release pressure exists |
| A testing report with every model | An evaluation report attached to every release |

An illustrative set of tiers for a customer-support agent:

| Tier | The agent may | Required before promotion to this tier |
|---|---|---|
| 0 | Read a fake database | The offline [harness](02-a-minimal-eval-harness.md) passes |
| 1 | Read the real database | An evaluation on a sample of real tasks, access controls, a log of every query |
| 2 | Issue refunds up to a fixed amount | An [environment evaluation](04-evaluating-agents-trajectories-and-environments.md) with refusal tasks, spending limits, sampled human review |
| 3 | Move money without a person in the loop | An abuse evaluation covering [prompt injection](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md) at a stated threshold, monitoring, a tested rollback |

Rules that follow from the lecture:

- Measure the capability you fear with the strongest elicitation you can build, not with an average prompt.
- Write the threshold before you see the result.
- Keep "it did not" apart from "it could not".
- Re-run on every model upgrade and every new tool.
- Write down what you did not test.

## Pitfalls

1. **"It refused when I asked" read as "it cannot."** Fix: try the strongest setup: step-by-step instructions, tools, retries.
2. **One prompt style.** Fix: several elicitation variants per capability.
3. **A benchmark that everyone passes, taken as proof of a safety margin.** Fix: a harder evaluation that separates the systems you care about.
4. **Tier names without tests.** Fix: each tier names an evaluation and a pass rule.
5. **A lecture treated as the policy.** Fix: read the current document.
6. **Permissions granted on good behavior instead of measured capability.** Fix: tiers, with the evidence attached.

## Try it

**Deliverable:** a one-page capability-tier policy for one agent you know.

1. Three or four tiers, each stating what the agent may touch.
2. For each tier, the evaluation that admits a model, with a pass rule.
3. Three elicitation variants you tried: a plain request, step-by-step instructions, and an agent with tools and a retry loop.
4. The safeguards each tier requires.
5. A list of what you did not test.

**You are done when** a colleague can refuse a promotion to the next tier by pointing at a single line in your document.

**Stretch goal:** write the abuse evaluation for the highest tier: ten attempts to make the agent break its policy, each with the verdict you expect.

## Key takeaways

- Capability evaluation measures what a system can do, including with hostile use, not what it did on your samples.
- Elicitation, the prompt and setup used, is part of the measurement. A weak setup understates capability.
- As described in the lecture, the Responsible Scaling Policy ties named risk levels to evaluations and requires the safeguards for a level before a model reaches it.
- Committing in advance, in writing, removes the incentive to skip testing when a model is ready.
- For your own systems: tiers, an evaluation with a pass rule per tier, safeguards before permission.
- Policy details change. Date your sources and read the current text.

## Self-check

1. What is elicitation?
   A. Hiding a model's capabilities from users
   B. The choice of prompts and setups that draws a capability out of a model
   C. The ordering of risk levels
   D. The measurement of training compute
2. In the lecture, what must hold before a model at the next AI Safety Level is deployed?
   A. The safety and security measures for that level are in place
   B. Every public benchmark has saturated
   C. A government agency has approved it
   D. The model is cheaper to run
3. Which level did the lecture assign to frontier models of the time?
   A. ASL-1  B. ASL-2  C. ASL-3  D. ASL-4
4. What did the October 15, 2024 update change, as described?
   A. It removed the capability thresholds
   B. It lengthened the testing window from three to six months and added testing at capability thresholds
   C. It made the reports confidential
   D. It ended the compute threshold
5. Why did Claude 3.5 Sonnet beat a stronger reasoning model on agentic coding, in Mann's explanation?
   A. It had more parameters
   B. It worked in an environment where it could write, run and test code, and the other did not
   C. It was released later
   D. The benchmark was contaminated
6. Why does Mann say benchmarks make forecasting hard?
   A. They are expensive to run
   B. They saturate soon after they are defined, so few measure the levels that matter
   C. They are kept secret
   D. They only test simple recall

<details><summary>Show answers</summary>

1. B. Elicitation is how hard and how well you ask.
2. A. The commitment is safeguards first, then the next level.
3. B. ASL-2, with early signs of potentially dangerous capabilities. ASL-3 was the level being prepared for.
4. B. Both changes are about testing earlier and longer.
5. B. The environment, with its feedback loop, is part of elicitation.
6. B. Progress rushes past a benchmark once it is defined.

</details>

## Sources

- **Lecture:** Ben Mann, "Measuring Agent Capabilities and Anthropic's RSP", UC Berkeley LLM Agents MOOC, Fall 2024: [video](https://www.youtube.com/watch?v=6y2AnWol7oo), used at [elicitation](https://www.youtube.com/watch?v=6y2AnWol7oo&t=120), [the policy and its levels](https://www.youtube.com/watch?v=6y2AnWol7oo&t=720), [benchmarks do not last](https://www.youtube.com/watch?v=6y2AnWol7oo&t=1440).

## Next

→ [Evals in Production](07-evals-in-production.md), which returns to the ordinary case: measuring a running system, every day.
