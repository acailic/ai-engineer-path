# 03. Agents for Scientific Discovery

**Level:** Practitioner · **Reading time:** 10 min · **Exercise:** 45 min
**Prerequisites:** [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) (tools and the agent loop)

> **In one sentence:** After this chapter you can describe how agent teams are used across the research loop, judge which parts of their output still need a human check, and see how your level of access to a model limits what you can evaluate about it.

## Why this matters

A lab wants a protein that blocks a virus. The work loops: read the literature, form a hypothesis, design the experiment, analyze the data, write it up. Each step has its own tool, and no single tool covers the loop. James Zou describes the old pattern as AI as a tool: a narrow, well-defined problem handed to a well-curated model such as AlphaFold, which predicts a protein's 3D shape. The new pattern is AI as a co-scientist that moves through the whole loop ([0:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=0)). The question this chapter answers: what have agent teams demonstrated, where did they fail, and what should a builder copy?

## The core idea

Science has two loops. The outer one is the research loop: hypothesis, experiment, analysis, paper. The inner one is the agent loop you already know: observe, decide, act. The difference from [web agents](01-multimodal-agents-web-and-computer-use.md) is the verifier. A web task has a script that checks the end state. In science the final check is an experiment plus a human reading the result. Work done only on a computer is called **in silico**; work with real reagents is **wet-lab** work. Most agent research so far is in silico.

Zou's **Virtual Lab** copies the shape of a real lab. A **PI agent** plays the principal investigator, the professor who runs a lab. Specialist agents play students. They hold group meetings and one-on-ones. The analogy breaks at the bench: the agents can plan an experiment and analyze the result, but in the cases he presents people still run the experiment.

## How it works, step by step

The Virtual Lab, as Zou describes it ([4:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=240)):

1. A person describes the project to the PI agent.
2. The PI agent decides which areas of expertise the project needs.
3. The PI agent creates and trains a specialist agent for each area. Each is a frontier language model, fine-tuned to use tools such as AlphaFold and to reach current scientific knowledge.
4. The team holds group meetings to write a research plan, and one-on-one meetings to review a subtask such as an analysis or a piece of code.
5. Agents attend an "agent school" where they improve themselves, partly by writing questions relevant to their task ([12:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=720)).

### Two more Zou systems

- **Paper2Agent.** Each research paper becomes an interactive agent that exposes the paper's methods. His example is an agent for AlphaGenome, a model of genome function ([32:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1920)). The agents expose their methods through **MCP**, the Model Context Protocol, an open standard for connecting a model to tools and data. He notes that some paper agents failed to build a robust MCP environment ([40:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=2400)).
- **Agents4Science 2025.** An online conference held on October 22, 2025, where agents wrote the papers and agents reviewed them ([54:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3240)). Each submission passed three reviewer agents, GPT-5, Gemini 2.5 Pro and Claude Sonnet 4, each scoring from 1 to 6. The reviewers were calibrated on accepted and rejected papers from a previous ICLR, a major machine-learning conference ([50:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000)).

## What the practitioners say

### James Zou (November 2025): demonstrated, and still limited

- **COVID-19 case study.** The agent team designed **nanobodies**, small proteins that bind a target. AlphaFold predicted how each design binds, and the designs were then synthesized. He says the human researchers spoke for about 1 percent of the time ([10:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=600), [18:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=1080)). <!-- SOURCE GAP: the packet has no count of designs, no binding results and no numbers from the experiments. -->
- **Reviewer agents disagree.** On the same papers, GPT-5 gave the lowest scores, Gemini the highest, and Claude came closest to human experts ([50:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000)).
- **References.** About 44 percent of the papers had every reference verified by an automated pipeline. The other 56 percent had at least one reference that could not be verified, usually one or two ([54:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3240)). A **hallucinated reference** is a citation to a paper that does not exist.
- **Examples he highlights** ([56:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3360)): a simulated job market with agents playing both applicants and firms, which a human expert reviewed favorably; a simulation of astronaut crews checked against NASA data; and a drug-candidate team with a medicinal-chemist agent and a molecule-evaluation agent.
- **Limitations** ([60:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3600)): project metadata must be captured in a form agents can use; people must keep reviewing the agents' assumptions and key steps; and the work is mostly in silico, so wet-lab validation is still missing.

### Percy Liang (November 2024): access decides what you can find out

Liang's claim is that "access shapes research" ([0:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0)): researchers study what they can reach.

| Level of access | What you have | His analogy | What it allows |
|---|---|---|---|
| API | Prompts in, responses out | A cognitive scientist measuring behavior | Build agents; measure behavior |
| Open weights | The trained model itself | A neuroscientist probing internals | Fine-tune, distill, inspect; no deprecation |
| Open source | Data, architecture, training procedure | A computer scientist building a system | Question every design choice |

- **Agents built with API access only.** His problem-solving agents reflect, plan and run commands such as editing a file ([12:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=720)). A slide defines success as the fraction of eight trials in which the agent improves on a reference by 10 percent; the hardest task took 24 hours ([6:01](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=361)). His simulation agents, simply prompted, reproduce human survey answers with 85 percent normalized accuracy on one slide ([19:07](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1147)).
- **What weights add.** His group's model-independence test showed that some layers of Llama 3 8B were used to build the 3B model, a fact the release notes did not mention ([38:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2280)).
- **His closing advice:** work "at small scale, but with a mindset of scale", and pool compute across groups ([52:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=3120)).

## Pitfalls

1. **Trusting references because they look right.** Fix: verify every citation by an automated lookup before a human reads; see [evaluating capabilities and risks](../03-evaluation/06-evaluating-capabilities-and-risks.md).
2. **Using one reviewer model.** Fix: use several, know each one's bias, and calibrate against past decisions; see [LLM-as-a-judge and rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md).
3. **No record of who did what.** Fix: document the human and agent contribution at every step, as the conference required.
4. **Expecting the agent to run experiments.** Fix: plan for people at the bench.
5. **Losing project metadata.** Fix: store it where agents can read it.
6. **Designing an evaluation that needs the model's internals when you only have an API.** Fix: match the question to the access level.

## Try it

Audit a model-written research note.

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

1. Let a coordinator assemble specialists per task instead of one generalist agent doing everything; see [the agent framework landscape](../05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md).
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

<details><summary>Show answers</summary>

1. B. The PI agent decides and then creates and trains a specialist for each area.
2. On papers that human reviewers had already accepted or rejected at a previous ICLR.
3. About 56 percent.
4. Any one: probing internals (for example which layers of Llama 3 8B were reused in the 3B model), fine-tuning and distillation, reproducibility without deprecation.
5. Any two: work is mostly in silico without wet-lab validation; metadata is not captured in an agent-friendly form; people must keep reviewing assumptions and key steps.

</details>

## Sources

- **Lecture:** James Zou, "AI Agents to Automate Scientific Discoveries", UC Berkeley Agentic AI MOOC, Fall 2025 (November 3, 2025): [video](https://www.youtube.com/watch?v=yqPIsTTdUkc), used at [tool to co-scientist](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=0), [Virtual Lab](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=240), [Agents4Science](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000), [limitations](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3600)
- **Lecture:** Percy Liang, "Open-Source and Science in the Era of Foundation Models", UC Berkeley LLM Agents MOOC, Fall 2024 (November 18, 2024): [video](https://www.youtube.com/watch?v=f3KKx9LWntQ), used at [levels of access](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0), [model independence](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=2280), [compute](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=3120)
- **Reading:** Swanson et al., "The Virtual Lab of AI Agents Designs New SARS-CoV-2 Nanobodies with Experimental Validation" (*Nature*, 2025): [article](https://www.nature.com/articles/s41586-025-09442-9)

<!-- VERIFY: the arXiv link and the Crossref query shape come from my knowledge, not from the lecture packets. -->

## Next

→ [04. Agents for Formal Mathematics](04-agents-for-formal-mathematics.md), the one scientific domain where a machine, not a human, checks every step.
