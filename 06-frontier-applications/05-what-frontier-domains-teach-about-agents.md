# 05. What Frontier Domains Teach About Agents

**Level:** Practitioner · **Reading time:** 10 min · **Exercise:** 30 min

> **In one sentence:** After this chapter you can compare web, robotics, science and mathematics agents on five axes, environment, verifier, search, tools and evaluation, and apply the pattern to an ordinary software agent.

## Why this matters

You have built and evaluated an agent. You have also seen four research domains that look unrelated: clicking through web pages, controlling robots, running a lab meeting, proving theorems. The same five decisions show up in all of them, and the order in which the researchers made them is the transferable part. The question this chapter answers: which decisions mattered most, and what is still only hoped for?

## The core idea

Read together, the four domains suggest one sequence. First an environment with cheap resets. Then a **verifier**, a check that says whether a result is correct, that runs without a person. Then search, meaning extra attempts spent against that verifier. Then tools for the work that language cannot do exactly. Finally evaluation by outcome rather than by path.

The analogy: progress is proportional to how fast and how honestly the environment says no. It breaks in one place. A fast, honest verifier is not enough; the problems must also come at a graded difficulty, and Thomas Hubert names that curriculum as the ingredient still missing for mathematics ([32:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1920)).

## How it works: the four domains on five axes

| Domain | Environment | Verifier | Search | Tools | Reported result |
|---|---|---|---|---|---|
| Web and computer use | Self-hosted site clones; a virtual machine | End-state scripts | Repeated sampling; tree search with a model as judge | Screenshot, accessibility tree, mouse and keyboard | About 20 percent accuracy for the best models, as of March 2025 |
| Robotics | Simulator, then the robot | A reward function | RL at scale in randomized physics | Model-written rewards; generated demonstrations | First and second against four human drivers |
| Science | Papers, databases, code | Experiments and human reviewers | Agent meetings; evolutionary search, breeding variations on the best equations | AlphaFold, MCP servers | 56 percent of papers had an unverifiable reference |
| Formal mathematics | Lean and its library | The proof assistant | RL, then RL on one problem; retrieval; sketches | Automated provers, SMT solvers | Three of six olympiad problems in 2024, four with AlphaGeometry |

Sources for each row: web ([Salakhutdinov 6:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=360), [24:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1440), [Xiong 24:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=1440)); robotics ([Stone 58:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3480), [Fan 46:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2760)); science ([Zou 54:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3240)); mathematics ([Hubert 56:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3360)).

Terms in the table: RL is **reinforcement learning**, learning by trial and error from a reward. MCP is the Model Context Protocol, a standard for connecting a model to tools. An SMT solver is a program that decides whether a formula follows from given facts. An accessibility tree is the operating system's list of interface elements.

### Verifiers, from perfect to absent

| Strength | Example | What fills the gap |
|---|---|---|
| Perfect | A proof assistant | Review of the formal statement itself ([Yang 36:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2160)) |
| Designed | An RL reward function | Tuning, or candidates ranked by training results ([Fan 44:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2640)) |
| Scripted | OSWorld's 134 end-state scripts for 369 tasks | Writing many scripts ([Xiong 24:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=1440)) |
| One reference path | A Mind2Web demonstration | An executable environment ([Xiong 6:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=360)) |
| Human | Peer review | Several reviewers, calibrated on past decisions ([Zou 50:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000)) |

## What the practitioners say

Five claims, each shared by at least two of the ten lectures.

- **Environments: resets must be cheap and the start state exact.** OSWorld gives every task a setup file and starts a virtual machine from it ([Xiong 12:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=720), [14:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=840)). Fan's bet is that simulating a problem is easier than solving it, and his kitchens number a hundred thousand ([Fan 16:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=960), [30:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=1800)). Science lacks this: the work is mostly on a computer, and the real test is a wet lab ([Zou 60:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3600)). Zou's stand-in for a shared environment is a meeting: each question goes to five parallel agent discussions, and the PI agent reads the transcripts to reach a consensus ([Zou 8:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=480)).
- **Verifiers: quality of feedback decides the rest.** Sean Welleck's whole argument is that compiling code removes doubt about a proof ([Welleck 2:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=120)). Even a perfect checker guards only what it is given: Yang's team checks a translated geometry statement by proving it equivalent to the reference, which works only in a restricted domain ([Yang 44:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2640)). A designed verifier can still be wrong: Peter Stone's racer was first too aggressive, then too timid ([Stone 56:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3360)), so Fan lets training results choose among model-written rewards ([Fan 44:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2640)).
- **Search: spend compute only against a check, after narrowing the choices.** Web agents gain from resampling and tree search ([Salakhutdinov 34:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=2040), [40:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=2400)). Proof search explodes because tactics are unlimited ([Yang 26:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1560)); LIPS shrinks it by enumerating lemma applications symbolically and leaving only the rewrites to a model ([Yang 30:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1800)). Copra needs no training: a model proposes tactics inside a depth-first search, and each error goes back into the prompt ([Chaudhuri 26:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=1560), [30:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=1800)). Where a score is hard to assign, as for Lean-STaR's thoughts, Welleck's team sampled many proofs in parallel instead ([Welleck 22:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1320)). Hypothesis spaces are infinite, so prior knowledge must steer the search ([Chaudhuri 4:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=240)).
- **Tools and data: the model does language, exact tools do exact work.** Tutorials become trajectories ([Xiong 50:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=3000)), one demonstration becomes many ([Fan 32:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=1920)), a model writes rewards ([Fan 44:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2640)), and a sketch is filled by automated provers ([Welleck 30:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1800)). Specialization comes from reading: Zou's agents fine-tune on the papers they fetch for their own topics ([Zou 12:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=720)), and small models can suffice inside such loops: Welleck's model that retrieves relevant lemmas has 100 million parameters ([Welleck 52:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=3120)).
- **Evaluation: numbers travel only with their conditions.** Human and model scores sit side by side on WebArena, 78 percent against about 14 percent ([Salakhutdinov 6:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=360)). On OSWorld, the 38 percent Xiong reports for OpenAI's Operator took up to 200 steps, where most tasks need 15 to 20, and raising the limit from 15 to 50 moves a score ([Xiong 38:00](https://www.youtube.com/watch?v=n__Tim8K2IY&t=2280)). Competition scores and research-level scores separate ([Welleck 66:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=3960)). Liang sets the ceiling for his simulated people with people: humans re-answering a survey agree with their own earlier answers only 81 percent of the time ([Liang 22:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=1320)). He adds that the level of access to a model bounds what can be evaluated at all ([Liang 0:00](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0)).

### Demonstrated, or expected

| Claim | Status |
|---|---|
| A racing agent beats expert humans | Demonstrated, in one game ([Stone 58:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3480)) |
| Silver-medal standard at the IMO 2024 | Demonstrated, with people translating the problems; one point below gold ([Hubert 52:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3120), [56:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3360)) |
| Web agents do economically valuable work | Not shown; the tasks were made low-stakes on purpose ([Salakhutdinov 26:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1560)) |
| Agents run science on their own | Partly; mostly on a computer, with people reviewing assumptions ([Zou 60:00](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3600)) |
| Perfect verification will matter most in the long run | Hubert's stated expectation ([Hubert 38:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=2280)) |
| 2025 to 2026 as "the year of agents" | What many people expect, in Salakhutdinov's opening ([Salakhutdinov 0:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=0)) |

## Pitfalls

1. **Quoting a frontier number without its date and setup.** Fix: state benchmark, model, step limit and date.
2. **Adding retries and search before any automatic check exists.** Fix: write the check first; see [a minimal eval harness](../03-evaluation/02-a-minimal-eval-harness.md).
3. **Using a model as judge where an exact check is available.** Fix: compile, run the test, look up the reference.
4. **Treating a model-written reward or rubric as correct by construction.** Fix: measure both failure directions.
5. **Checking the solution and forgetting the specification.** Fix: review the task statement, as formal mathematicians review the formal statement.
6. **Expecting autonomy where the verifier is weak.** Fix: keep a person at the review points.
7. **Ignoring adversarial environments.** A web page altered on purpose can steer an agent ([Salakhutdinov 76:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=4560)); see [planning for mistakes](../07-ml-in-production/04-planning-for-mistakes.md).

## Try it

Score your own agent on the five axes.

- **Deliverable:** a five-row table, one row per axis. Each row names the concrete artifact: the reset script, the check function, the retry policy, the tool list, the benchmark file.
- **Acceptance criteria:** you are done when every row names a file or function that exists, you mark the weakest row, and you upgrade that one row and report a before-and-after number.
- **Stretch:** ask a model to write three candidate checks for the weakest row and keep the one that best separates good runs from bad runs you planted.

## Key takeaways

- The order is the lesson: environment, verifier, search, tools, evaluation.
- Formal mathematics has the only perfect verifier; science has the weakest; web and robotics sit between.
- Search pays only against a check, and only after the action space is narrowed.
- Language models earn their place by generating what used to be hand-made: rewards, trajectories, sketches, problems.
- A number without its benchmark, step limit and date is not evidence.

## What this means for someone building agents

1. Build the reset and the end-state check before the agent. Everything else, retries included, reuses that check; see [evaluation is the product](../03-evaluation/01-evaluation-is-the-product.md).
2. Narrow before you search: fewer actions, retrieved context, a sketch to fill in; see [planning, search and decision making](../02-building-agents/03-planning-search-and-decision-making.md).
3. Invest in generating data and checks, not only in prompts: examples, variants, candidate rubrics, then filter by measurement; see [testing generative and LLM components](../08-quality-assurance/05-testing-generative-and-llm-components.md).
4. Separate demonstrated from expected in every report you write, and keep a person where the verifier is weak; see [checklists](../11-professional-practice/07-checklists.md).

## Self-check

1. Which domain has the strongest verifier, and what still needs a person there?
   A. Robotics; the reward function is never right
   B. Web agents; the end-state script needs updating
   C. Formal mathematics; the formal statement itself
   D. Science; the reviewers need calibration
2. Why did Xiong's team build OSWorld rather than use Mind2Web?
3. What do Eureka and AgentTrek have in common?
4. In Hubert's account, what supplied the curriculum in two-player games, and what is open for mathematics?

<details><summary>Show answers</summary>

1. C. The proof assistant never passes a wrong proof, but the translated statement still needs review.
2. Mind2Web has one demonstration per task and no executable environment, so other correct solutions are penalized.
3. A language model generates candidates, rewards in one case and trajectories in the other, and executing them decides which are kept.
4. Self-play always supplied an opponent at the right level. For mathematics, where problems of graded difficulty come from is still the open question.

</details>

## Sources

- **Lecture:** Ruslan Salakhutdinov, "Multimodal Autonomous AI Agents", UC Berkeley Advanced LLM Agents MOOC, Spring 2025: [video](https://www.youtube.com/watch?v=RPINOYM12RU), used at [WebArena](https://www.youtube.com/watch?v=RPINOYM12RU&t=360), [search](https://www.youtube.com/watch?v=RPINOYM12RU&t=2040)
- **Lecture:** Caiming Xiong, "Multimodal Agents: From Perception to Action", same course: [video](https://www.youtube.com/watch?v=n__Tim8K2IY), used at [benchmark gap](https://www.youtube.com/watch?v=n__Tim8K2IY&t=360), [OSWorld](https://www.youtube.com/watch?v=n__Tim8K2IY&t=960)
- **Lecture:** Peter Stone, "Autonomous Agents: Embodiment, Interaction, and Learning", UC Berkeley Agentic AI MOOC, Fall 2025: [video](https://www.youtube.com/watch?v=iDhzzugMOLA), used at [reward design](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3360)
- **Lecture:** Jim Fan, "Project GR00T: A Blueprint for Generalist Robotics", UC Berkeley LLM Agents MOOC, Fall 2024: [video](https://www.youtube.com/watch?v=Qhxr0uVT2zs), used at [simulation](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=960), [Eureka](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2640)
- **Lecture:** James Zou, "AI Agents to Automate Scientific Discoveries", UC Berkeley Agentic AI MOOC, Fall 2025: [video](https://www.youtube.com/watch?v=yqPIsTTdUkc), used at [reviewers](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3000), [limitations](https://www.youtube.com/watch?v=yqPIsTTdUkc&t=3600)
- **Lecture:** Percy Liang, "Open-Source and Science in the Era of Foundation Models", UC Berkeley LLM Agents MOOC, Fall 2024: [video](https://www.youtube.com/watch?v=f3KKx9LWntQ), used at [access](https://www.youtube.com/watch?v=f3KKx9LWntQ&t=0)
- **Lecture:** Thomas Hubert, "AlphaProof: when reinforcement learning meets formal mathematics", UC Berkeley Advanced LLM Agents MOOC, Spring 2025: [video](https://www.youtube.com/watch?v=3gaEMscOMAU), used at [three ingredients](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1920)
- **Lecture:** Kaiyu Yang, "Language models for autoformalization and theorem proving", same course: [video](https://www.youtube.com/watch?v=cLhWEyMQ4mQ), used at [search space](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1560)
- **Lecture:** Sean Welleck, "Bridging Informal and Formal Mathematical Reasoning with AI", same course: [video](https://www.youtube.com/watch?v=Gy5Nm17l9oo), used at [verification](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=120), [context](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=3840)
- **Lecture:** Swarat Chaudhuri, "Abstraction and Discovery with Large Language Model Agents", same course: [video](https://www.youtube.com/watch?v=IHc0TEMrEdY), used at [search](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=240)

## Next

→ [Evaluation Is the Product](../03-evaluation/01-evaluation-is-the-product.md), where the verifier idea from these four domains becomes daily practice for a software agent.
