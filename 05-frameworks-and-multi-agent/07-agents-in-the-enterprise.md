# 07. Agents in the Enterprise

**Level:** Practitioner · **Reading time:** 12 min · **Exercise:** 60 min
**Prerequisites:** [LlamaIndex: Building a Knowledge Assistant](03-llamaindex-knowledge-assistants.md) (retrieval over private documents)

> **In one sentence:** After this chapter you can take an agent from a notebook to a company workflow, with a source on every claim, a human approval point, and the evaluation and model-cost decisions that a company needs.

## Why this matters

Your prototype answers questions about contracts, on your laptop. The compliance officer asks three things. Where does this answer come from? Who approved that action? What happens when the vendor changes the model? A demo answers none of them.

Two Fall 2024 lectures do. Burak Gokturk of Google describes what companies ask for. Nicolas Chapados of ServiceNow describes what it takes to put agents into real workflows.

## The core idea

An enterprise agent is a model plus five things around it, and the model is the replaceable part:

1. **Grounding.** Answers come from sources the model was not trained on, and each claim shows its source.
2. **Control points.** A person approves actions above a threshold, and every action is logged.
3. **Adaptation on a cost ladder.** Start with examples in the prompt. Tune the model only when the rungs below fail.
4. **Evaluation.** Automatic checks on every change.
5. **Managed prompts and model choice.** Prompts are versioned and portable across models.

Gokturk's summary, after conversations with many companies, matches: success now rests on access to a broad set of models, choice and flexibility at every level, and the ability to customize ([30:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1800)).

The analogy is turning a contractor into an employee on probation: sources are checked, work is reviewed, and the review is written down. The analogy breaks at learning. An employee improves between reviews. A model improves only when you change its prompt, its data or the model itself.

Two terms carry the chapter. **Grounding** ties each statement to a source fetched at run time. **Attribution** is the share of statements that the cited sources actually support. Gokturk's slides show attribution as a user-experience metric, with an example answer whose supporting sources are counted, 4 out of 7.

## How it works, step by step: from notebook to workflow

1. **Pick the workflow.** High volume, rule-bound, and with a completion that software can check. Chapados's example: coffee spills on a laptop, an employee opens a help-desk ticket, and a person works through manual steps to ship a new one ([2:00](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=120)).
2. **Pick the level of automation.** Draft only, then act after approval, then act alone within limits. Chapados's slides carry a chart of automation levels, and one of his closing slides is titled "Envisioning AI Augmentation to Empower Workers".
3. **Prefer APIs.** The slides separate two kinds of agents. The second half of the lecture is about agents that drive a web interface. Reach for those only when no API exists ([chapter 06](06-agent-infrastructure-sandboxes-browser-use-and-protocols.md)).
4. **Ground with attribution.** Gokturk calls search fundamental, even for making a model work well, and describes what an application needs: "I'm saying this, because here is the exact blurb from exact this document that's saying this" ([30:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1800)). He names healthcare, finance and customer service, where a guess about a bill is not acceptable.
5. **Adapt the model on the ladder.** Gokturk's order, from cheapest to dearest ([38:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2280), [40:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2400)):
   - **Prompt design.** Put one to ten examples in the prompt. Zero-shot means no example; one-shot means one. Most teams stop here, in his account.
   - **Prompt tuning.** Learn a vector to put in front of the prompt. He expected more use of it and sees little.
   - **Parameter-efficient fine-tuning (PEFT).** Update few parameters, or add a small layer. LoRA (low-rank adaptation) freezes the base model and learns an added low-rank component. Less compute, and probably less data.
   - **Full fine-tuning.** Update all the weights. It needs much data and compute, and he says few customers do it.
   - **Distillation.** Train a small **student** model to reproduce the answers of a large **teacher**. The idea appears in Gokturk's slides and again in Chapados's case study.
6. **Add the control points.** Function calling lets the model act, not only answer. Each action needs permissions, an approval threshold and a log.
7. **Evaluate.** Gokturk points to automatic side-by-side evaluation, with the largest model as the rater, because human raters are scarce ([58:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=3480)). For workflow agents, check the end state, as the ServiceNow team does.
8. **Manage prompts and models.** Gokturk lists what teams ask for: a prompt management system with storage, revision history, and the ability to convert a prompt from one model to another ([58:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=3480)).

## Worked example: two lecturers, one system

The two lectures describe the same system from two seats.

| Concern | Gokturk (Google: the platform) | Chapados (ServiceNow: the workflow) |
|---|---|---|
| Grounding | Search with the exact passage shown; attribution as a metric | Completion checked through back-end APIs on real tasks |
| Model cost | API cost "approaching 0", one of his trends | A student agent "330x cheaper" in a case study |
| Control | Function calling for developer control | Levels of automation; a human in the process |
| Record | Prompt management with history | The **tape**: a structured, granular, semantic-level log |
| Evaluation | Automatic side-by-side with a large model as rater | Benchmarks on real workplace tasks |

The tape deserves a sentence more. TapeAgents, the ServiceNow framework, is built around that log. In the map of the lecture, the optimization loops take the tapes produced during execution as their input: the trace is not only an audit record but also the data for the next model.

## What the practitioners say

### Gokturk: what companies ask for

He describes his lecture as a view of the market, not of algorithms. He reports six trends ([15:57](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=957), [30:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1800)):

1. AI is moving much faster.
2. Technical trends in the models: his slides ask where models are headed and name separate models for different tasks, dense models and single-modality models.
3. The choice of platform matters.
4. The cost of API calls is approaching zero.
5. Search, because the model and search need each other.
6. The enterprise search tool or assistant, including tools for employees' own productivity. He names Glean and ChatGPT Enterprise.

His slides list a slide on minimizing hallucinations as three problems, of which the packet shows only the first, "right context". A slide on function calling says it "is all about developer control and flexibility".

He also tells a story from his PhD. A small medical data set of 50 patients trained in 42 seconds, so he built intuition fast. Large models take weeks per run, and his worry is that intuition now arrives more slowly. The lesson for agents: keep the feedback loop short enough to learn from.

### Chapados: what deployment looks like

He frames the question by people, not by models: who the users are, what role they have, what work they do, and in which context the agent should help ([0:00](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=0)). ServiceNow, he says, has 25,000 employees and sells a platform for enterprise workflows in IT, human resources and customer support. He groups trustworthiness, governance, safety and security with deployment: all are needed for an agent to succeed in practice.

His slides add three points for which the packet has only the titles:

- Two kinds of LLM agents, the first labeled API agents.
- A case study of an inexpensive assistant that finds the right form for a user and helps complete it; its slide is titled "Student is 330x Cheaper".
- An assessment of impact both top-down and bottom-up, next to a slide saying that technology adoption takes time and that uncertainty about generative AI adoption remains high.

<!-- SOURCE GAP: the packet holds 22% of each transcript. For f24-04 the slides' "3 problems" for hallucinations are cut after "Right context". For f24-07 the comparison behind "Student is 330x Cheaper" (which two systems, at what accuracy) lies in the skipped 30 minutes; do not read the number as more than a slide title. -->

## Pitfalls

1. **Fine-tuning to fix a knowledge gap.** Weights are the slowest way to teach this quarter's facts. Fix: ground the answer in retrieval first.
2. **Answers without a source.** Fix: retrieve, show the passage, and put attribution into the evaluation.
3. **Full autonomy on day one.** Fix: climb the ladder: draft, approve, then act within limits; see [planning for operations](../07-ml-in-production/10-planning-for-operations.md).
4. **A browser agent where an API exists.** Fix: the API, for reliability and for permissions.
5. **No evaluation before launch.** Fix: automatic side-by-side comparison and end-state checks, with the judge's biases in mind ([LLM as a judge](../03-evaluation/03-llm-as-a-judge-and-rubrics.md)).
6. **Prompts scattered in code.** Fix: a registry with history, and a test run whenever a prompt moves to another model, as in [testing generative components](../08-quality-assurance/05-testing-generative-and-llm-components.md).
7. **One vendor for everything.** Fix: keep the model behind an interface and run the evaluation when you swap it; [deploying a model](../07-ml-in-production/07-deploying-a-model.md) covers that change.
8. **No record.** Fix: log every step in a structured form, and treat the log as training data too.

## Try it

Choose one workflow in your company that people still do by hand.

1. Write a one-page proposal: volume per month, the check that proves completion, the proposed level of automation, the approval step, the fallback to a human, and three ways it could fail.
2. Prototype only the check, as code.

You are done when a colleague can run your check on a finished case and on a broken one, and it tells them apart. Before you hand the page over, walk it through the [professional-practice checklists](../11-professional-practice/07-checklists.md).

Stretch goal: run 20 past cases through a draft-only agent and measure how often a person accepts the draft unchanged. With a small model this costs cents.

## Key takeaways

- The model is the replaceable part. Grounding, control points, evaluation, managed prompts and model choice make an enterprise agent.
- Ground every claim in a source fetched at run time, show the source, and measure attribution.
- Adapt on the cost ladder: examples in the prompt, then LoRA or another light method, then distillation, and full fine-tuning last.
- Function calling turns answers into actions, so each action needs permissions, an approval threshold and a log.
- A structured log is both the audit trail and the data for the next improvement.
- Evaluate automatically: side-by-side comparison for answers, end state for workflows.

## Self-check

1. A company's agent gives outdated answers about this quarter's policy. What is the cheapest fix to try?
   A. Full fine-tuning on the policy documents
   B. Prompt tuning on a large corpus
   C. Retrieval that puts the current policy in the prompt, with the passage shown
   D. A larger model
2. What does attribution measure?
   A. How many tokens each answer costs
   B. The share of statements that the cited sources support
   C. The number of tools the agent called
   D. The latency of the retrieval step
3. In Gokturk's account, which adaptation did most teams use in practice?
   A. Prompt design with a few examples
   B. Prompt tuning
   C. Full fine-tuning
   D. LoRA
4. Why does Chapados's team check results through back-end APIs?
   A. It is faster than loading the page
   B. The end state proves completion, whatever path the agent took
   C. It avoids using a browser at all
   D. It removes the need for a benchmark
5. What is a student model, in the lectures' use of the word?
   A. A model trained by self-play
   B. A small model trained to reproduce a larger model's answers
   C. A model used only for evaluation
   D. A prompt with one example

<details><summary>Show answers</summary>

1. C. Grounding changes with the documents; weights do not.
2. B. It is shown as a user-experience metric on Gokturk's slides.
3. A. He says few customers fine-tune all weights and that prompt tuning surprised him by how little it was used.
4. B. The database state is checked, so other valid paths also pass.
5. B. The ServiceNow slides call the student "330x cheaper" in a form-filling case study.

</details>

## Sources

- **Lecture:** Burak Gokturk, "Enterprise trends for generative AI, and key components of building successful agents/applications", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=Sy1psHS3w3I), used at [feedback-loop anecdote](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=120), [trends and success factors](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1800), [adaptation ladder](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2280), [prompt management and evaluation](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=3480)
- **Lecture:** Nicolas Chapados, "AI Agents for Enterprise Workflows", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=-yf-e-9FvOc), used at [framing](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=0), [help-desk example](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=120), [end-state checks](https://www.youtube.com/watch?v=-yf-e-9FvOc&t=2400)

## Next

→ [Multi-Agent Systems I: Games and Self-Play](04-multi-agent-systems-i-games-and-self-play.md), if you came here for the enterprise chapters first, or back to [The Agent Framework Landscape](01-the-agent-framework-landscape.md) to choose what to build on.
