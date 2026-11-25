# 04. Capstone 3: From Model to Product

**Level:** Practitioner · **Reading time:** 20 min · **Exercise:** 40 h
**Prerequisites:** [Goals and Requirements](../07-ml-in-production/03-goals-and-requirements.md), [Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md), [Measuring Model Quality](../08-quality-assurance/02-measuring-model-quality.md). Read the other chapters of parts 07 and 08 as each milestone needs them.

> **In one sentence:** After this project you have taken one feature with a classical machine-learning component, not an LLM, from a vague request to a monitored service, with a document for every decision along the way.

## Why this matters

Not every feature with a model is an LLM feature. A classifier inside an ordinary product needs the same discipline, and the discipline is easier to see there. A model predicts a label. The label drives an action. The action has a cost.

[Part 07](../07-ml-in-production/README.md) teaches that discipline from Kästner's *Machine Learning in Production*, on one running example: support tickets routed to the team that can solve them. [Part 08](../08-quality-assurance/README.md) teaches how to test it. This capstone asks you to build the whole thing once, end to end, so that the habit is yours.

## The goal

Take one feature with a classical ML component through the book's whole discipline: goals, requirements, planning for mistakes, guardrails, a pipeline, deployment and monitoring. The suggested feature is a **ticket router**. It reads an incoming support ticket and predicts which team should handle it: billing, technical, or another team. If you have a real feature at work, use that instead, with personal data removed.

You finish with a small service and a folder of documents that show why each design decision was made.

## Deliverables

1. **Goals and requirements.** Four goal layers, one measure each, and requirements in three kinds.
2. **A baseline and a decision.** The simplest rule, measured, and a written answer to "is ML worth it here?".
3. **A quality report.** A confusion matrix, precision and recall per class, and a slice table.
4. **A mistake analysis.** System failures, an FMEA table, a fault tree, and the design changes.
5. **A pipeline.** One command runs data checks, training, the evaluation gate and the export.
6. **A deployment.** The model behind an interface, with guardrails, a fallback and a model card.
7. **An operations plan.** Objectives, monitors, a rehearsed rollback, a kill switch, and an incident response plan.

## The feature

| Part of the feature | What it does |
|---|---|
| Keyword rules | Catch the obvious tickets. Anything with "invoice" goes to billing |
| Classifier | Predicts the team for the rest, with a confidence score |
| Guardrail | Accepts only labels from the current list |
| Threshold rule | Below a confidence threshold, the ticket goes to the general queue |
| Fallback | If the model is down, slow, or returns something unparseable, the general queue takes every ticket |
| Appeal | A "wrong team?" button on every routed ticket |
| Telemetry | Re-routes per team, fallback rate, latency |

The model can be a logistic regression or a small set of decision trees on text features: for a start, a count of each word in the ticket. The point of the project is everything around it.

## Milestones

### Milestone 1: goals, requirements and the decision (5 to 7 hours)

Read [When to Use ML, and When Not To](../07-ml-in-production/02-when-to-use-ml-and-when-not-to.md), [Goals and Requirements](../07-ml-in-production/03-goals-and-requirements.md) and [Measuring Model Quality](../08-quality-assurance/02-measuring-model-quality.md).

Write the goals at four layers. Organization: tickets reach the right team sooner. Product: the median time to first response falls. Users: a customer with an urgent ticket is not misrouted. Model: the share of tickets routed to the wrong team, on held-out data. Then write the requirements in three kinds. A **REQ** is a state you want in the world. An **ASM** is an assumption the software makes about the world. A **SPEC** is what the software must do.

- [ ] Four goals, each with one measure and the rule that computes it.
- [ ] A keyword baseline, scored on the held-out set.
- [ ] A cost table for the ML component: building, running and maintaining it.
- [ ] A written decision to use ML or not, with the reduction in error that the model must show over the baseline.
- [ ] At least 1,000 labeled tickets in 3 to 10 classes, or a written reason for fewer. They are split into training, validation and test sets.
- [ ] The agreement between two labelers, measured on 50 tickets.

### Milestone 2: measure quality and find where it fails (6 to 8 hours)

Read [Slicing: Finding Where the Model Fails](../08-quality-assurance/03-slicing.md) and [Explainability, Fairness and Safety](../08-quality-assurance/13-explainability-fairness-and-safety.md).

- [ ] A confusion matrix on the test set, with precision and recall for each class.
- [ ] The reduction in error against the baseline.
- [ ] A slice table with at least three slices, such as language, ticket length and product area. Each slice shows its size and its score.
- [ ] One decision per slice: fix it, mitigate it outside the model, accept it with monitoring, or move it out of scope.
- [ ] If one slice splits people by a protected attribute, one fairness criterion is chosen and stated.
- [ ] You read 30 misclassified tickets and write down three causes.

### Milestone 3: plan for mistakes and design the system (8 to 10 hours)

Read [Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md), [Architecture for ML Systems](../07-ml-in-production/05-architecture-for-ml-systems.md), [Quality Attributes of ML Components](../07-ml-in-production/06-quality-attributes-of-ml-components.md) and [System Quality: End-to-End Tests and Guardrails](../08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md).

- [ ] Two or three system failures, written as violated requirements.
- [ ] An FMEA table with at least eight rows and a severity for each.
- [ ] A fault tree for the worst failure, with its minimal cut sets. No cut set of size one remains without a written decision to accept it.
- [ ] Every automated action is labeled automate, prompt or augment.
- [ ] Guardrails in plain code: only labels from the list, the confidence threshold, the timeout with its fallback.
- [ ] End-to-end tests with a hostile stub of the model. An unknown label is rejected. A low confidence sends the ticket to the general queue. A dead model sends every ticket there.
- [ ] Components with one responsibility each, and interfaces that say what happens on failure. One decision record.
- [ ] Numbers for latency, cost per prediction and model size, with the hard constraints marked.

### Milestone 4: build the pipeline and deploy (8 to 10 hours)

Read [Deploying a Model](../07-ml-in-production/07-deploying-a-model.md), [Automating the Pipeline](../07-ml-in-production/08-automating-the-pipeline.md), [Data Quality](../08-quality-assurance/06-data-quality.md), [Pipeline Quality](../08-quality-assurance/07-pipeline-quality.md) and [Responsible Engineering, Versioning and Reproducibility](../08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md).

- [ ] One command runs the stages in order: data validation, training, evaluation, export.
- [ ] A row with a missing field or a wrong type stops the pipeline. An unusual value only raises a warning.
- [ ] The evaluation gate refuses a model that scores worse than the baseline. Test it with a stub.
- [ ] One function turns a ticket into features, and both training and prediction call it. A test proves it.
- [ ] The serving form is chosen and written down: a library call, a service, a batch job, or a precomputed table.
- [ ] A model card states the intended use, the supported inputs, the accuracy per slice, and the limits.
- [ ] Code, data, model and settings carry versions. One decision record reconstructs which model produced a given routing.

### Milestone 5: operate (6 to 8 hours)

Read [Planning for Operations](../07-ml-in-production/10-planning-for-operations.md), [Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md) and [Automating the Pipeline](../07-ml-in-production/08-automating-the-pipeline.md).

- [ ] Service-level objectives for the service and for the model component.
- [ ] One monitor for each "detect by" entry of the FMEA table. Re-route rate per team, fallback rate and latency are three of them.
- [ ] Telemetry that shows whether the model was right: re-routes, appeals, reopen requests.
- [ ] A canary plan. A new model sees a share of the tickets first. The stop condition is written down. The rollback is rehearsed and timed.
- [ ] The kill switch is tested. The model's action is off, and the tickets flow to the general queue.
- [ ] An incident response plan with an on-call rotation and a runbook for each alert. One drill.
- [ ] Guards for drift. A renamed field is caught. A retraining trigger or schedule is written down.

## You are done when

1. The baseline number and the decision to use ML are on record, and the model beats the baseline on the test set.
2. The quality report has the confusion matrix, the precision and recall per class, and the slice table with a decision per slice.
3. The mistake analysis has no minimal cut set of size one without a written acceptance.
4. The pipeline runs with one command, stops on dirty data, and refuses a model worse than the baseline.
5. The tests with the hostile stub pass for the unknown label, the low confidence and the dead model.
6. The rollback was rehearsed and timed, and the kill switch was tested.
7. Every document names its date and the versions it refers to.

## Effort, tools and cost

Plan on 35 to 45 hours over three to four weeks. You need Python 3.10 or newer and a library for classical machine learning. For the data, use your own labeled tickets with personal data removed, or a public dataset whose license allows your use. Models of this kind train on a laptop at this data size. A container and a continuous integration service are optional. Hosting the service in the cloud costs money. A library call behind an interface is enough to pass the tests.

## Stretch goals

- An explainability report, with each explanation tool matched to the question it answers ([Explainability, Fairness and Safety](../08-quality-assurance/13-explainability-fairness-and-safety.md)).
- A shadow release and an A/B experiment on a simulated queue, read with statistics ([Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md)).
- A retraining schedule that runs the evaluation gate each time ([Automating the Pipeline](../07-ml-in-production/08-automating-the-pipeline.md)).
- A **cascade**, in which a small model decides whether a larger one is needed ([Deploying a Model](../07-ml-in-production/07-deploying-a-model.md)).
- Capacity arithmetic for ten times the traffic ([Scaling the System](../07-ml-in-production/09-scaling-the-system.md)).
- Run [How to Ship an LLM Feature End to End](01-how-to-ship-an-llm-feature-end-to-end.md) with the same folder, and note which documents change.

## Pitfalls

1. **Starting with the model.** Fix: milestone 1, in full, before any training.
2. **An accuracy without a baseline.** Fix: the keyword rules, scored first.
3. **A pipeline that fails silently.** Fix: schema checks that stop the run, and retries that are counted.
4. **Two encoders.** One prepares the features for training and another for prediction. Fix: one function, called by both, with a test.
5. **Set and forget.** Fix: a retraining trigger, and guards for drift.
6. **A reviewer who approves all day.** Fix: prompt for the few cases that matter, and measure how often reviewers disagree.
7. **A guardrail from the same model.** It shares the blind spot. Fix: a plain rule, or a model trained for another task.
8. **No fallback.** Fix: decide and test what happens when the model is down, slow, or returns garbage.
9. **A rollback nobody rehearsed.** Fix: rehearse it and time it, before the launch.
10. **Test data in the training set.** Fix: split first, and keep the test set for the final number.

## What the practitioners say

- **Accuracy hides the harm.** The example that opens [Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md) is a triage model with 96 percent accuracy. At 50,000 tickets a day it makes about 2,000 wrong predictions, and they do not spread evenly. Most come from two kinds of tickets.
- **A wrong prediction is not a failure.** A component mistake becomes a system failure only when nothing stops it. The same chapter.
- **Guardrails are usually not ML.** Kästner's examples are hard-coded ranges, overrides for known inputs, and rules such as banned-word filters. The same chapter.
- **Humans are poor monitors for machines.** Kästner quotes the line in chapter 7 of the book. It is the reason for the threshold rule and the appeal button, and against a review of every ticket.
- **Passing components do not make a working product.** That is the argument of part 08 for testing composed systems ([System Quality](../08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md)).

## Try it

The project is the exercise. Start with one hour:

1. Write the four goals for a ticket queue you know.
2. Find or label 100 tickets.
3. Write one keyword rule and count how many of the 100 it routes correctly.

**You are done with the first hour when** you have one number for a rule that cost no model at all.

## Key takeaways

- The discipline is the product: goals, a baseline, a mistake analysis, a pipeline, guardrails, an operations plan.
- Decide whether ML is worth it with a measured baseline and a cost table.
- A cut set of size one is a finding. Either add an independent check or write down the acceptance.
- Guardrails are plain code, tested with a hostile stub of the model.
- One encoder, one command, versions on everything.
- Rehearse the rollback before the launch, not during the incident.

## Self-check

1. Why measure the keyword baseline before training anything?
2. What are REQ, ASM and SPEC, and which kind is "tickets arrive with a subject line"?
3. A fault tree shows a minimal cut set with one event. What are the two ways to change that?
4. Why must one function prepare the features for training and for prediction?
5. What does the hostile stub model let you test that a real model cannot?
6. Which three signals show whether the router was right in production?

<details><summary>Show answers</summary>

1. It is the number every model must beat, and it may be good enough. If a rule solves the problem, the cost table shows that ML would add cost without benefit.
2. A REQ is a state you want in the world. An ASM is an assumption the software makes about the world. A SPEC is what the software must do. "Tickets arrive with a subject line" is an ASM.
3. Add an independent event that must also fail, such as a second check or a person's review. Or remove the event by redesigning, so that it can no longer occur.
4. Two encoders drift apart. The model is then trained on features that differ from the ones it sees in production. That mismatch is training–serving skew.
5. The failure modes you need to survive but cannot produce on demand: an unknown label, a low confidence, a dead or slow model.
6. Any three of: the re-route rate per team, the share of "wrong team?" appeals, reopen requests, the fallback rate, and the latency of the model component.

</details>

## Sources

- Part 07: [When to Use ML, and When Not To](../07-ml-in-production/02-when-to-use-ml-and-when-not-to.md), [Goals and Requirements](../07-ml-in-production/03-goals-and-requirements.md), [Planning for Mistakes](../07-ml-in-production/04-planning-for-mistakes.md), [Architecture for ML Systems](../07-ml-in-production/05-architecture-for-ml-systems.md), [Quality Attributes of ML Components](../07-ml-in-production/06-quality-attributes-of-ml-components.md), [Deploying a Model](../07-ml-in-production/07-deploying-a-model.md), [Automating the Pipeline](../07-ml-in-production/08-automating-the-pipeline.md), [Scaling the System](../07-ml-in-production/09-scaling-the-system.md), [Planning for Operations](../07-ml-in-production/10-planning-for-operations.md)
- Part 08: [Measuring Model Quality](../08-quality-assurance/02-measuring-model-quality.md), [Slicing: Finding Where the Model Fails](../08-quality-assurance/03-slicing.md), [Data Quality](../08-quality-assurance/06-data-quality.md), [Pipeline Quality](../08-quality-assurance/07-pipeline-quality.md), [System Quality: End-to-End Tests and Guardrails](../08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md), [Testing and Experimenting in Production](../08-quality-assurance/09-testing-and-experimenting-in-production.md), [Responsible Engineering, Versioning and Reproducibility](../08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md), [Explainability, Fairness and Safety](../08-quality-assurance/13-explainability-fairness-and-safety.md)

## Next

→ [Capstone 4: Efficient Inference](05-capstone-efficient-inference.md), for making a model smaller and faster without losing what it can do.
