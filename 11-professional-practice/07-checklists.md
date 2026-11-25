# 07. Checklists for Shipping AI Systems

**Level:** Practitioner · **Reading time:** 20 min · **Exercise:** 45 min
**Prerequisites:** None. [Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md) ends with two checklists that two of these extend.

> **In one sentence:** After this chapter you have five checklists you can copy into a project, one for each stage from the first line of code to an incident, and every item links to the chapter that explains it.

## Why this matters

Every part of this course ends with a method that is easy to agree with and easy to skip under a deadline. Write the goal. Build the evaluator. Threat-model the system. Rehearse the rollback. A checklist turns "we should" into a box that is either ticked or empty.

[Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md) ends with two checklists of its own. This chapter gathers the discipline of all ten parts into five.

## The core idea

A checklist item earns its place when four things hold:

1. It is one line, and it can be answered yes or no.
2. It names an artifact: a page, a table, a number or a test. It does not name an intention.
3. It links to the chapter that explains it.
4. It has caught something, or it was added after something went wrong.

### How to keep a checklist usable

- **Keep it short.** Around ten items, and twelve at most after you cut. Nobody reads a checklist with sixty.
- **Copy, then cut.** Copy the five below into your project. Delete what does not apply, and write down why.
- **A tick names a file.** An item is done when the artifact exists in the repository.
- **Someone else checks.** The person who did the work does not tick the last box alone. Someone who knows the users reads the result ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md)).
- **Fix, or decide.** Some items end with "or a written decision to accept the risk". A decision recorded with its reason is a valid tick. Silence is not.
- **Review it on a schedule.** Repeat the analysis after every incident and before every release that changes the model ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md)).
- **Remove dead items.** An item that has never caught anything is taking space from one that would.
- **Do not ask for a person at every step.** A gate that fires on everything trains people to click approve ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md)). An item that everyone ticks without looking is worse than no item.

## How it works, step by step

The five checklists follow the order of a project. Copy the ones you need.

### 1. Before the first line of code

- [ ] The goal is written at four layers, organization, product, users and model, with one measure for each. ([Goals and Requirements](../07-ml-in-production/03-goals-and-requirements.md))
- [ ] "Good enough" is a number for this use and this data. It is not the word "correct". ([From Models to Systems and Products](../07-ml-in-production/01-from-models-to-systems-and-products.md))
- [ ] I can name who is harmed by a wrong output, and how badly. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))
- [ ] I measured the simplest baseline, a rule or a keyword, and wrote down the cost of anything smarter. ([When to Use ML, and When Not To](../07-ml-in-production/02-when-to-use-ml-and-when-not-to.md))
- [ ] I chose workflow or agent, and wrote down why the steps do or do not vary. ([The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md))
- [ ] The environment is defined: what the system may read and what it may change. Everything else is out of reach. ([The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md))
- [ ] Every automated action is labeled automate, prompt or augment. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))
- [ ] The data exists, I may use it, and I know how good its labels are. ([Data Quality](../08-quality-assurance/06-data-quality.md))
- [ ] Model work and system work are joined by an interface contract, with decision points set in advance. ([Process Models: Planning and Iteration](../08-quality-assurance/10-process-models-planning-and-iteration.md))
- [ ] Someone who knows the users read this page. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))

### 2. Evaluation

- [ ] Every task has its expected outcome written down before the first run. ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md))
- [ ] A cheap oracle grades what a program can check. A judge calibrated against human labels grades the rest. ([Evaluation Is the Product](../03-evaluation/01-evaluation-is-the-product.md), [LLM-as-a-Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md))
- [ ] I read failed and passed attempts, to catch a grader that is too strict or too loose. ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md))
- [ ] Every task runs several times, and pass^k is reported beside pass@k. ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md))
- [ ] Scores carry standard errors, and two versions are compared on the same tasks, paired. ([Statistics for Evals](../03-evaluation/05-statistics-for-evals.md))
- [ ] A held-out set was never opened during development. ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md))
- [ ] The set includes requests the agent must refuse, such as a refund for a missing order. ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md))
- [ ] The report is sliced, and each slice has a decision: fix it, mitigate it, accept it with monitoring, or move it out of scope. ([Slicing: Finding Where the Model Fails](../08-quality-assurance/03-slicing.md))
- [ ] Cost and latency are printed beside quality. ([A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md))
- [ ] For an agent, the outcome and the route are graded separately, in an environment that resets. ([Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md))
- [ ] The evaluator itself was tested on cases with known verdicts. ([the green agent case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md))
- [ ] A gate blocks any change that makes a metric worse. ([Evals in Production](../03-evaluation/07-evals-in-production.md))

### 3. Security review

- [ ] The threat model names the assets, the attackers and every trust boundary. ([Threat Modeling LLM Applications and Agents](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md))
- [ ] Every tool result and every fetched page is treated as untrusted input. ([Threat Modeling LLM Applications and Agents](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md))
- [ ] Every tool call passes a policy gate whose default is deny. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))
- [ ] Model output never reaches a shell, a database or a URL without validation. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))
- [ ] Each agent has at most two of the three properties in the Rule of Two. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))
- [ ] A sensitive action waits for a person who sees the real arguments. No answer means no action. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))
- [ ] Memory, retrieved documents and tool descriptions were reviewed for planted content. ([Agent-Specific Attacks](../04-safety-and-security/03-agent-specific-attacks.md))
- [ ] The defenses are layered: prompt level, detector, and controls in code. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))
- [ ] An injection suite was run. The attack success rate and the utility are reported, with the number of runs. ([Red-Teaming and Safety Evaluation](../04-safety-and-security/06-red-teaming-and-safety-evaluation.md))
- [ ] Each detector's false positive rate and false negative rate are measured. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))
- [ ] Every blocked call is logged with its arguments and the rule it broke. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))
- [ ] The model that ships, fine-tuned or not, was tested again. ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md))

### 4. Pre-deployment and rollout

- [ ] A mistake analysis exists, with an FMEA table and a fault tree. No cut set of size one is left without a written acceptance. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))
- [ ] The fallback for a model that is down, slow or returning garbage is defined and tested. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))
- [ ] Guardrails in plain code bound the damage of a wrong output, and are tested with a hostile stub of the model. ([System Quality: End-to-End Tests and Guardrails](../08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md))
- [ ] The end-to-end tests and the acceptance tests pass on the whole system. ([System Quality: End-to-End Tests and Guardrails](../08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md))
- [ ] Code, prompts, data, models and settings carry versions, and a decision record exists. ([Responsible Engineering, Versioning and Reproducibility](../08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md))
- [ ] Telemetry can tell whether the model was right in production. ([Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md))
- [ ] The pipeline re-runs with one command, and the evaluation gate runs in continuous integration. ([Automating the Pipeline](../07-ml-in-production/08-automating-the-pipeline.md))
- [ ] Service-level objectives are written for the system and for the model component. ([Planning for Operations](../07-ml-in-production/10-planning-for-operations.md))
- [ ] The rollout has levels: shadow, canary, then all users. Each level has a written stop condition. ([Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md), [Policy, Governance and Standards](../04-safety-and-security/09-policy-governance-and-standards.md))
- [ ] The rollback was rehearsed and timed, and the kill switch was tested. ([Planning for Operations](../07-ml-in-production/10-planning-for-operations.md))
- [ ] Users can undo or appeal an automated decision. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))
- [ ] The model card is written: intended use, supported inputs, accuracy and limits. ([Deploying a Model](../07-ml-in-production/07-deploying-a-model.md))
- [ ] An incident response plan and an on-call rotation exist, with a runbook for each alert. ([Planning for Operations](../07-ml-in-production/10-planning-for-operations.md))

### 5. Incident response

- [ ] Contain first: the kill switch or the rollback. The rest of the system keeps running. ([Planning for Operations](../07-ml-in-production/10-planning-for-operations.md))
- [ ] Record the versions of the model, the prompt, the data and the settings. The decision record shows what ran. ([Responsible Engineering, Versioning and Reproducibility](../08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md))
- [ ] Pull the traces of the affected attempts. Every attempt was traced. ([Evals in Production](../03-evaluation/07-evals-in-production.md))
- [ ] Measure the blast radius: which users, how many, and since when. ([Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md))
- [ ] Name the failure: a component mistake or a system failure, and which FMEA row it belongs to. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))
- [ ] If an attack is suspected, keep the blocked-call log and add the payload to the versioned adversarial data set. ([Red-Teaming and Safety Evaluation](../04-safety-and-security/06-red-teaming-and-safety-evaluation.md))
- [ ] The affected people are told, and they have a way to appeal. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md), [Security, Privacy, Transparency and Accountability](../08-quality-assurance/14-security-privacy-transparency-and-accountability.md))
- [ ] The failing inputs become evaluation tasks. ([Evals in Production](../03-evaluation/07-evals-in-production.md))
- [ ] The fix is kept only if the evaluation improves beyond the noise and nothing regresses. ([Evaluation Is the Product](../03-evaluation/01-evaluation-is-the-product.md))
- [ ] The fault tree and the checklists get an item, and the analysis is repeated. ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md))
- [ ] A named stop condition sends the system back one rollout level. ([Policy, Governance and Standards](../04-safety-and-security/09-policy-governance-and-standards.md))

## Worked example

One item of checklist 4, in three states. The example is illustrative.

| State | What the box says | What it is worth |
|---|---|---|
| Intention | "We will rehearse the rollback before launch" | Nothing yet |
| Tick without evidence | "Done" in a meeting | Unknown |
| Tick with an artifact | `docs/rollback-drill.md`, with the date and the time from alert to the previous version | A rehearsed rollback |

The third state is the only one the checklist accepts.

## What the practitioners say

- **Two checklists come from the book.** Kästner's chapter 7 ends with one for every design review of a model-backed feature and one for each run of the mistake analysis ([Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md)). Checklists 1 and 4 extend them to agents and LLMs.
- **Test the evaluator.** The Berkeley course staff end their checklist for the evaluating agent with test cases of known verdicts ([the green agent case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md)). It is the eleventh item of checklist 2.
- **A gate on everything is a rubber stamp.** Dawn Song's three rules for a human approval gate ([Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md)). The last rule of this chapter borrows it.
- **A launch checklist exists in operations.** [Planning for Operations](../07-ml-in-production/10-planning-for-operations.md) places it beside the rollback and the incident plan.

## Pitfalls

1. **A checklist nobody copies.** Fix: paste it into the project on day one, and cut it to size.
2. **Items that are intentions.** "Think about security" cannot be ticked. Fix: name the artifact.
3. **Ticking without a file.** Fix: every tick names a path.
4. **The author checks alone.** Fix: someone who knows the users reads the result.
5. **A checklist that never changes.** Fix: add an item after each incident, and remove the dead ones.
6. **Used once, at launch.** Fix: review after incidents and before releases that change the model.
7. **A checklist in place of a decision.** "We ran the checklist" is not a reason. Fix: the written decisions are the output.
8. **Items without links.** Fix: link the chapter, so that a new team member can learn what the item means.

## Try it

Copy checklist 1 into the repository of a project you are working on. Spend 30 minutes ticking it honestly.

**Deliverable:** the filled checklist, with a file name beside every tick and an owner and a date beside every empty box.

**You are done when** every tick names a file, and at least one item changed what you were about to do.

**Stretch goal:** write the item you wish had been on the list after your last incident, and add it to the right checklist.

## Key takeaways

- A checklist turns a method into a box that is ticked or empty.
- An item earns its place by being one line, naming an artifact, linking its chapter, and having caught something.
- A tick names a file. A decision to accept a risk is a valid tick only when it is written down.
- Review the checklists after every incident and before every release that changes the model.
- Five checklists cover a project: before the code, evaluation, security, rollout, and incident response.

## Self-check

1. What four properties must a checklist item have to earn its place?
2. Why must a tick name a file?
3. Which kind of item allows a written decision instead of a fix?
4. When is a checklist reviewed?
5. Why is an item that everyone ticks without looking worse than no item?
6. Why does the evaluation checklist ask whether the evaluator itself was tested?

<details><summary>Show answers</summary>

1. It is one line with a yes-or-no answer. It names an artifact, not an intention. It links to the chapter that explains it. It has caught something, or it was added after something went wrong.
2. An item is done when the artifact exists in the repository. A tick without a file records an opinion, and nobody can check it later.
3. An item about a risk that cannot be removed now, such as a minimal cut set of size one. The decision is written down with its reason. Silence is not a tick.
4. After every incident, and before every release that changes the model.
5. It trains the team to tick without reading, and it takes the place of an item that would have caught something.
6. The evaluator is a program, and it can be wrong. Cases with known verdicts are the only way to know that its verdicts mean something.

</details>

## Sources

- [Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md), [Planning for Operations](../07-ml-in-production/10-planning-for-operations.md), [From Models to Systems and Products](../07-ml-in-production/01-from-models-to-systems-and-products.md), [When to Use ML, and When Not To](../07-ml-in-production/02-when-to-use-ml-and-when-not-to.md), [Goals and Requirements](../07-ml-in-production/03-goals-and-requirements.md), [Deploying a Model](../07-ml-in-production/07-deploying-a-model.md), [Automating the Pipeline](../07-ml-in-production/08-automating-the-pipeline.md) (part 07)
- [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) (part 02)
- [Evaluation Is the Product](../03-evaluation/01-evaluation-is-the-product.md), [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md), [LLM-as-a-Judge and Rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md), [Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md), [Statistics for Evals](../03-evaluation/05-statistics-for-evals.md), [Evals in Production](../03-evaluation/07-evals-in-production.md), [the green agent case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) (part 03)
- [Threat Modeling LLM Applications and Agents](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md), [Agent-Specific Attacks](../04-safety-and-security/03-agent-specific-attacks.md), [Defenses: Guardrails, Detection and Secure Design](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md), [Red-Teaming and Safety Evaluation](../04-safety-and-security/06-red-teaming-and-safety-evaluation.md), [Policy, Governance and Standards](../04-safety-and-security/09-policy-governance-and-standards.md) (part 04)
- [Measuring Model Quality](../08-quality-assurance/02-measuring-model-quality.md), [Slicing: Finding Where the Model Fails](../08-quality-assurance/03-slicing.md), [Data Quality](../08-quality-assurance/06-data-quality.md), [Process Models: Planning and Iteration](../08-quality-assurance/10-process-models-planning-and-iteration.md), [System Quality: End-to-End Tests and Guardrails](../08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md), [Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md), [Responsible Engineering, Versioning and Reproducibility](../08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md), [Security, Privacy, Transparency and Accountability](../08-quality-assurance/14-security-privacy-transparency-and-accountability.md) (part 08)

## Next

→ [Staying Current](08-staying-current.md), for what to follow after the course ends.
