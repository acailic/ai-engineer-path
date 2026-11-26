# 03. Agents for Scientific Discovery

**Level:** Practitioner · **Reading time:** 18 min · **Exercise:** 45 min
**Prerequisites:** [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) (tools and the agent loop)

> **In one sentence:** After this chapter you can describe how agent teams are used across the research loop, judge which parts of their output still need a human check, and see how your level of access to a model limits what you can evaluate about it.

## Why this matters

A lab wants a protein that blocks a virus. The work loops: read the literature, form a hypothesis, design the experiment, analyze the data, write it up. Each step has its own tool, and no single tool covers the loop. James Zou describes the old pattern as AI as a tool: a narrow, well-defined problem handed to a well-curated model such as AlphaFold, which predicts a protein's 3D shape. The new pattern is AI as a co-scientist that moves through the whole loop ([0:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=0)).

## The core idea

Science has two loops. The outer one is the research loop: hypothesis, experiment, analysis, paper. The inner one is the agent loop you already know: observe, decide, act. The difference from [web agents](01-multimodal-agents-web-and-computer-use.md) is the verifier. A web task has a script that checks the end state. In science the final check is an experiment plus a human reading the result. Work done only on a computer is called **in silico**; work with real lab materials is **wet-lab** work. Most agent research so far is in silico.

The check need not be an experiment; it can be a fit to data already collected. Swarat Chaudhuri describes empirical discovery, which, he says, is what most of the natural sciences do, as starting from data and fitting hypotheses to it. Its steps are a question, hypotheses, a setup, data, analysis, interpretation and a report. The task he picks is **symbolic regression**, finding an equation from observations, for example Kepler's law from measurements of Mars. A language model looks unfit for it, since the data are bare numbers, yet it can bring in prior scientific knowledge. What it lacks is a check, so it must be paired with separate machinery that scores each hypothesis against the data. The result is a loop much like the one with a proof assistant: the language model proposes and a separate program scores ([62:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=3720)). His system for it, LaSR, is described in [Agents for Formal Mathematics](04-agents-for-formal-mathematics.md).

Zou's **Virtual Lab** copies the shape of a real lab. A **PI agent** plays the principal investigator, the professor who runs a lab. Specialist agents play students. The analogy breaks at the bench: the agents can plan an experiment and analyze the result, but in the cases he presents people still run the experiment.

## How it works, step by step

The Virtual Lab, as Zou describes it ([4:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=240)):

1. A person describes the project to the PI agent.
2. The PI agent decides which areas of expertise the project needs.
3. The PI agent creates and trains a specialist agent for each area. Each is a frontier language model, fine-tuned to use tools such as AlphaFold and to reach current scientific knowledge.
4. The team holds group meetings to write a research plan, and one-on-one meetings to review a subtask such as an analysis or a piece of code.
5. Agents then attend an agent school. On a topic a person names, such as the latest AlphaFold, each agent writes its own questions, searches PubMed, an archive of biomedical papers, for open-access papers, and fine-tunes on them as it reads. Teacher agents quiz it, and a failing agent trains again before it graduates. A run takes about a day ([10:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=600), [12:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=720), [14:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=840)).

### Two more Zou systems

- **Paper2Agent.** Each research paper becomes an interactive agent, what Zou calls a virtual corresponding author. Worker agents set up the paper's code in a virtual environment, extract its tools and test that the original results reproduce. The outcome is packaged as **MCP**, the Model Context Protocol, which he calls an industry standard for passing resources to a language model, and is connected to a chatbot ([26:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1560), [28:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1680)). An agent for AlphaGenome, a DeepMind model that interprets mutations in the genome, found a candidate gene linked to LDL cholesterol ([30:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1800), [32:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1920)). On his benchmark the paper agent solved every task, where Claude Code with the same paper and code made more mistakes and took over three times as long ([32:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1920)). Failed conversions turn into feedback to the authors ([40:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2400)).
- **Agents4Science 2025.** Zou calls it the first conference where the authors and the reviewers are both AI agents: an AI agent must be first author and do most of the work, and every submission and review is public ([44:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2640)). It ended on October 22 with 48 papers accepted from over 300 submissions ([46:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2760)). Each submission passed three reviewer agents, GPT-5, Gemini 2.5 Pro and Claude Sonnet 4, each scoring from 1 to 6. The reviewers were calibrated on accepted and rejected papers from a previous ICLR, a major machine-learning conference ([50:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000)). Every paper also carried a checklist of human and AI contribution at each stage; accepted papers showed more human involvement ([46:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2760), [48:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2880)).

## What the practitioners say

### James Zou (November 2025): demonstrated, and still limited

- **COVID-19 case study.** The first project asked the Virtual Lab for binders for recent variants. In the group meeting the immunologist agent suggested **nanobodies**, small proteins that bind a target, a choice Zou calls unorthodox; the machine-learning agent agreed because they are easier to model, and a scientific critic agent warned about overfitting on scarce data ([6:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=360), [8:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=480)). Every question is debated in five parallel meetings, and the PI agent reads the transcripts to reach a consensus ([8:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=480)). The agents then built a pipeline: ESM, a protein language model, scores candidates for stability, AlphaFold predicts each structure bound to the virus's spike protein, and Rosetta, a physics simulator, estimates how strongly it binds. Billions of candidates shrank to 92, all of which people made and tested ([14:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=840), [16:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=960)). Earlier human-designed nanobodies did not bind the JN.1 variant; the new ones bound it, and a different strain, more strongly, and did not bind other viruses or human proteins, which suggests fewer side effects. The design took a few days ([18:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1080)). The people set the goal and the wet-lab budget and, by his pie chart, spoke about 1 percent of the time ([8:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=480), [10:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=600)).
- **Reviewer agents disagree.** On the same papers, GPT-5 gave the lowest scores, Gemini the highest, and Claude came closest to human experts. He shows a review that caught statistics in the text that disagreed with the tables ([50:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000)).
- **References.** About 44 percent of the papers had every reference verified by an automated pipeline. The other 56 percent had at least one reference that could not be verified, usually one or two ([54:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3240)). A **hallucinated reference** is a citation to a paper that does not exist.
- **Examples he highlights**: a simulated job market with agents playing both applicants and firms, which a human expert, a Nobel laureate in economics, reviewed favorably ([54:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3240)); a simulation of astronaut crews checked against NASA data; and a drug-candidate team with a medicinal-chemist agent and a molecule-evaluation agent ([56:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3360)).
- **Limitations** ([60:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3600)): project metadata must be captured in a form agents can use; people must keep reviewing the agents' assumptions and key steps; and the work is mostly in silico, so wet-lab validation is still missing.

### Percy Liang (November 2024): access decides what you can find out

Liang's claim is that "access shapes research" ([0:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0)): researchers study what they can reach. He describes each level of access through a kind of scientist ([0:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0), [2:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=120)).

| Level of access | What you have | His analogy | What it allows |
|---|---|---|---|
| API | Prompts in, responses out | A cognitive scientist measuring behavior | Build agents; measure behavior |
| Open weights | The trained model itself | A neuroscientist probing internals | Fine-tune, distill, inspect internals; the model stays available |
| Open source | Data, architecture, training procedure | A computer scientist building a system | Question every design choice |

- **Agents built with API access only.** In MLAgentBench the agent gets a machine-learning problem, data and starter code, and must reflect, plan, fact-check its plan and act ([6:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=360), [8:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=480)). On a cybersecurity benchmark the best model, Claude 3.5, solved 17.5 percent of the tasks: the hardest task took a human team 24 hours, and the hardest task any model solved takes humans 11 minutes ([12:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=720)).
- **Simulation agents.** His group gave each of a demographically diverse thousand Americans a two-hour interview with an LLM agent and seeded an agent's memory with the transcript, then ran the same surveys and games on people and agents. Asked again two weeks later, real people match their own answers only 81 percent of the time; the agents reach 69 percent, which he describes as 85 percent normalized accuracy against a baseline of about 20 percent, and they do worse without the interviews ([20:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1200), [22:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1320)).
- **What weights add.** Asked whether 9.8 or 9.11 is larger, Llama 3.1 70B answers 9.11; researchers at Transluce traced it to a neuron that responds to September 11, as if the numbers were dates ([26:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1560), [28:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1680)). His group's model-independence test, which checks whether two models were trained independently, showed that some layers of Llama 3 8B were used to build the 3B model, a fact the release notes did not mention ([38:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2280)).
- **What weights do not change.** Liang counts open-weight models as immensely valuable, but draws two limits ([38:02](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2282)). Rough surgery on the weights, averaging two models or cutting out layers, is not guaranteed to give a coherent model; in general the model must be fine-tuned afterwards to heal. And open weights keep a researcher inside a blueprint written by others: the same transformer architecture and the particular parameters a company released. Going deeper, he says, means opening up the hood, which is the step to open source.
- **What open source requires.** Liang traces the term to open-source software and to the Open Source Initiative, founded in 1998, which defined it and is now writing a definition for AI ([40:10](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2410)). Its four freedoms are to use a system without asking permission, to study it, to modify it and to share it. For a model, he says, that takes three things. The parameters must be available without restrictions. The code must cover not only inference but also training and the processing and filtering of data, because the data shapes how a model behaves. And there must be a description of the data, not the data itself: most web text is copyrighted, or not clearly free to use, so developers hold no license to redistribute it, and lawsuits over whether training on it is fair use were pending. Compute, he adds, is not part of the definition, but without it a model cannot be modified in practice, since new data means retraining or at least continued pre-training.
- **What open source adds.** With data, training code and compute a group can change the recipe. His examples: a data mixture found by optimization that trains 2.6 times faster than hand-set weights, and an optimizer, the rule that updates a model as it trains, twice as fast as Adam ([44:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2640)). The catch is compute, and open-source models are still far weaker than the best open-weight and API models ([40:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2400)).
- **Public infrastructure.** Other fields, Liang notes, have won multi-billion-dollar projects for open academic research, among them the Large Hadron Collider, the James Webb telescope and the Human Genome Project. The problems pursued in public differ from the ones a company would take on ([50:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=3000)). His conclusion restates the theme: more and more research lives inside APIs and fixed weights, and staying there means sitting in a local optimum. Fundamental progress needs researchers who can question the data, the architecture and the way a model is trained, with the eventual goal of understanding how data and architecture map to behavior. He calls that question hard even with full access and hopeless with an API alone.
- **His closing advice:** work "at small scale, but with a mindset of scale", and pool compute across groups ([52:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=3120)).

## Pitfalls

1. **Trusting references because they look right.** Fix: verify every citation by an automated lookup before a human reads; see [evaluating capabilities and risks](../03-evaluation/06-evaluating-capabilities-and-risks.md).
2. **Using one reviewer model.** Fix: use several, know each one's bias, and calibrate against past decisions; see [LLM-as-a-judge and rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md).
3. **No record of who did what.** Fix: document the human and agent contribution at every step, as the conference required.
4. **Expecting the agent to run experiments.** Fix: plan for people at the bench.
5. **Designing an evaluation that needs the model's internals when you only have an API.** Fix: match the question to the access level.

## Try it

Audit a model-written research note: ask a model for the note on a topic you know. Crossref, a registry of scholarly papers, returns the closest match to a query; count a reference as verified only if the title and first author match.

```python
# Illustrative pseudocode: check that each cited paper exists in Crossref.
import json, urllib.parse, urllib.request

def first_hit(title):
    query = urllib.parse.urlencode({"query.bibliographic": title, "rows": 1})
    with urllib.request.urlopen(f"https://api.crossref.org/works?{query}") as r:
        return json.load(r)["message"]["items"][0]
```

- **Deliverable:** a one-page note with five references, and a table with each reference marked verified or unverified.
- **Acceptance criteria:** you are done when every reference has a verdict from the lookup, the note states the share that failed, and one failure is traced to its cause: wrong year, wrong authors, or no such paper.
- **Stretch:** have two different models review the note on a 1-to-6 scale and compare where they disagree.

## Key takeaways

- The Virtual Lab copies a real lab: a PI agent assembles specialists per project, and the team meets.
- Agents4Science 2025 ran with agent authors and agent reviewers; 56 percent of papers had at least one unverifiable reference.
- Reviewer agents differ in strictness, so one model is not a fair panel.
- Agent research is mostly in silico; experiments and final review remain with people.
- What you can evaluate about a model depends on your access: behavior with an API, internals with weights, everything with open source.

## What this means for someone building agents

1. Let a coordinator assemble specialists per task; see [the agent framework landscape](../05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md).
2. Expose every capability as a tool behind a standard interface, as Paper2Agent does with MCP; see [tool design and function calling](../02-building-agents/02-tool-design-and-function-calling.md).
3. Turn each class of error into an automatic check before a human reviews: references, statistics, code. That is the [minimal eval harness](../03-evaluation/02-a-minimal-eval-harness.md) idea applied to documents.
4. Write down the human review points in advance; see [checklists](../11-professional-practice/07-checklists.md).

## Self-check

1. In the Virtual Lab, who decides which areas of expertise a project needs?
   A. The human who describes the project
   B. The PI agent
   C. The specialist agents vote
   D. A fixed list set by the platform
2. How were the Agents4Science reviewer agents calibrated?
3. What share of AI-led papers had at least one unverifiable reference?
4. Name one thing open weights let researchers check that an API does not.
5. Give two limitations Zou names for AI scientist agents.
6. By Liang's account, what three things does open source require of a model, and what is left out of the definition?

<details><summary>Show answers</summary>

1. B. The PI agent decides and then creates and trains a specialist for each area.
2. On papers that human reviewers had already accepted or rejected at a previous ICLR.
3. About 56 percent.
4. Any one: probing internals, such as which layers of Llama 3 8B were reused in the 3B model; fine-tuning or distilling; results that stay reproducible because the model stays available.
5. Any two: work is mostly in silico without wet-lab validation; metadata is not captured in an agent-friendly form; people must keep reviewing assumptions and key steps.
6. The parameters, without restrictions; the code for training and for processing and filtering data as well as for inference; and a description of the data, not the data itself. Compute is left out of the definition, though without it a model cannot be modified in practice, since new data means retraining.

</details>

## Sources

- **Lecture:** James Zou, "AI Agents to Automate Scientific Discoveries", UC Berkeley Agentic AI MOOC, Fall 2025 (November 3, 2025): [video](https://www.youtube.com/watch?v=yqPIsTTdUkc) · [guide](../lectures/f25-08-ai-agents-to-automate-scientific-discoveries.md), used at [tool to co-scientist](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=0), [Virtual Lab](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=240), [Agents4Science](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000), [limitations](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3600)
- **Lecture:** Percy Liang, "Open-Source and Science in the Era of Foundation Models", UC Berkeley LLM Agents MOOC, Fall 2024 (November 18, 2024): [video](https://www.youtube.com/watch?v=f3KKx9LWntQ) · [guide](../lectures/f24-10-open-source-and-science-in-the-era-of-foundation.md), used at [levels of access](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0), [model independence](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2280), [compute](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=3120)
- **Lecture:** Swarat Chaudhuri, "Abstraction and Discovery with Large Language Model Agents", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (April 21, 2025): [video](https://www.youtube.com/watch?v=IHc0TEMrEdY) · [guide](../lectures/sp25-11-abstraction-and-discovery-with-large-language.md), used at [empirical discovery](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=3556)
- **Reading:** Swanson et al., "The Virtual Lab of AI Agents Designs New SARS-CoV-2 Nanobodies with Experimental Validation" (*Nature*, 2025): [article](https://www.nature.com/articles/s41586-025-09442-9)

## Next

→ [04. Agents for Formal Mathematics](04-agents-for-formal-mathematics.md), the one scientific domain where a machine, not a human, checks every step.
