# 13. Explainability, Fairness and Safety

**Level:** Practitioner · **Reading time:** 26 min · **Exercise:** 75 min
**Prerequisites:** [Slicing: Finding Where the Model Fails](03-slicing.md)

> **In one sentence:** After this chapter you can pick an explanation tool that fits your question, compute and justify one fairness criterion for your feature, and run a four-step hazard analysis on the system around a model.

## Why this matters

Three questions reach you in the same week, after the triage feature goes live.

- A support lead asks why a ticket was routed to billing.
- A country manager asks whether the routing is worse for customers who write in German.
- A director asks what the worst outcome is when the refund suggestion is wrong, and what stops it.

The first is about **explainability**, the second about **fairness**, the third about **safety**. Each has tools, and none has a single right answer.

## The core idea

**Explainability** is how far a person can understand how a model works, or why it made one prediction. Kästner makes three cautions (chapter 25). Explanations are usually partial. Several different partial explanations of one prediction can all be correct. And an explanation shows how the model used its inputs, not why the answer is right. He adds that people rarely explain their own decisions exactly either. They give a justification after the fact.

**Fairness** has no single accepted definition. It can be formalized as several criteria that can conflict with each other (chapter 26). Which one a product should meet is a decision to be made and defended, not a formula to look up.

**Safety** is the prevention of harm from system failure: death or serious injury, severe damage to property, or harm to the environment or society. Kästner insists that it is a property of the whole system. Software alone cannot be unsafe. Harm arises when the system acts on the world, or when people act on what it shows them (chapter 27).

## Explainability: match the tool to the question

| Question | Tool | How it works |
|---|---|---|
| Which inputs matter most overall? | **Feature importance** | Measure the accuracy lost when a feature is shuffled |
| How does one input move the output? | Partial dependence plot | Vary one feature, hold the rest still |
| What simple model behaves like this one? | **Global surrogate** | Train a small interpretable model on the original's predictions |
| Why this one prediction? | Feature influences | Attribute the prediction to inputs (the book names LIME and SHAP) |
| What is the smallest rule behind it? | **Anchor** | Find the few conditions that suffice for the prediction |
| What would change it? | **Counterfactual** | Find a small change to the input that flips the result |
| Which past cases does it resemble? | **Similarity-based** | Show the nearest labeled training examples; needs an understandable distance and meaningful examples |
| What is odd in the training data? | Prototypes and criticisms | Typical examples, and outliers poorly covered by them |

Most of these work without access to the model's internals (chapter 25), which is why outside auditors use surrogates on models available only through an API. Two details from the book help in practice. **LIME** learns a small linear model of the decision boundary, the border between the model's answers, near one input. Its influence values are known to be unstable, and **SHAP**, built on Shapley values, a rule for splitting a prediction fairly among the inputs, has largely replaced it as the more stable choice. Every prediction has many counterfactuals, so a tool must choose among them, usually the counterfactual that changes little, or that touches few inputs (chapter 25).

One more tool debugs the training data. **Influential instances** are training examples that move the decision boundaries far more than the others. They are often outliers, possibly mislabeled, from regions where training data is sparse: Kästner's example is one eighty-five-year-old who keeps being arrested and bends the model's use of age. To find them, retrain with one example left out at a time and compare the resulting models; cheaper approximations exist for many models.

Kästner's running example is a commercial tool that scores a defendant's risk of re-offending. Journalists at ProPublica found that Black defendants were almost twice as likely as white defendants to be labeled high risk without then re-offending. The model's internals were not open to inspection. Researchers have trained a simple points-based scorecard from the same data, as accurately, that a judge can read in full and audit (chapter 25).

His warning is the "dark side" of explanations. They are approximations and can create an illusion of understanding. For decisions as serious as bail, he prefers models that are interpretable by design (chapter 25).

For an LLM system, add one rule. The reasons a model writes for its own answer are text it generated, not a record of its process. Treat them as a draft justification to check, not as evidence. To test whether a claim rests on a retrieved document, remove that document and see whether the claim survives. That is feature influence applied to the context.

## Fairness: choose a criterion and defend it

The book separates **harms of allocation**, where a group gets fewer resources or worse service, from **harms of representation**, where output reinforces a stereotype or demeans a group ([chapter 26](https://mlip-cmu.github.io/book/26-fairness.html)). Failing German writers causes the first. Calling every doctor "he" causes the second.

Not every use of a protected attribute counts as wrongful discrimination. The question is whether the use is justified, and that depends on the domain. In the US, the customer's sex may not enter a mortgage decision, while a diagnosis may need the patient's sex, because some conditions are far more common in one sex. One system can do both kinds of harm at once: a hiring model that ranks women lower withholds interview slots, gives them a worse service and reinforces a stereotype.

Kästner measures fairness over **protected attributes**, the features that divide the demographic groups of concern. His legal overview lists the characteristics that federal anti-discrimination law protects in the US, among them race, religion, national origin, sex, sexual orientation and gender identity, age from forty, and pregnancy, with further rules for domains such as housing, credit, and employment (chapter 26). He describes three model-level criteria (chapter 26):

| Criterion | It requires | Weakness |
|---|---|---|
| **Anti-classification** | The protected attribute never changes the output | Blind to proxies, such as a postcode standing in for race |
| **Group fairness** (demographic parity) | Similar rates of positive outcomes across groups | Ignores whether the outcomes are correct |
| **Equalized odds** | Similar error rates across groups | Needs ground-truth labels |

Anti-classification can be audited with the invariant tests from [Testing Without Oracles](04-testing-without-oracles.md): flip the attribute in every input and assert that no output changes. One violation proves the criterion broken (chapter 26).

For group fairness, the book also notes a rule of thumb from US employment-law discourse: the group that is worse off should be selected at least 80 percent as often as the other group (chapter 26).

Kästner's example makes the weakness plain (chapter 26). A bank can satisfy group fairness by approving the safest 20 percent of one group's applications and a random 20 percent of the other group's. The approval rates match, and the two groups are served very differently.

The three criteria can be mutually exclusive. Choosing among them is a requirements problem, and Kästner describes it as political, because stakeholders disagree (chapter 26). For the triage feature, a defensible starting point is equalized odds by language: the model should be wrong equally often for every group of customers.

A criterion is measured, and then worked on at four places in the pipeline (chapter 26):

- **Inference.** Replace the protected attribute with a constant to enforce anti-classification. For the other two criteria, choose a separate decision threshold per group, so that positive rates or error rates line up.
- **Training data.** Remove the attribute and the features that stand in for it, and drop or correct examples known to carry a historical bias.
- **Data collection.** In Kästner's view this often has the most leverage, because unequal error rates usually trace back to groups with less, or worse, training data.
- **Toolkits.** IBM's AI Fairness 360 and Microsoft's Fairlearn compute the common measures and fit into test infrastructure.

Four further points from chapter 26:

- **It is a system concern.** Fairness requirements belong in the system requirements and are broken down into requirements for each component, with the protected attributes and the chosen criterion written down. Teams negotiate them across their interfaces.
- **Mitigate outside the model.** The system can drop a distinction it does not need, suppress a category the model gets insultingly wrong, and have a person review rejections first.
- **Document the results.** A **model card** records intended use, intended users, the demographic factors considered, accuracy per subpopulation, the evaluation data, and limitations. Kästner pairs it with a **datasheet** for the training data, which records how the data was collected and which subpopulations it represents.
- **Monitor it.** Group fairness is cheap to watch in production, because it needs no labels: alert when positive rates diverge between groups. Equalized odds is hard, because a missed case is difficult to observe. Also watch for a spike in complaints from one group, and prepare an incident response plan that can shut a feature down (chapter 26). [Testing and Experimenting in Production](09-testing-and-experimenting-in-production.md) supplies the machinery.

Two cautions complete the second point. Human review is no cure by itself. In a study of predictive policing that Kästner cites, officers used a prediction as a pretext when it matched their own bias and ignored it when it did not; a model that looks objective can make an existing bias harder to question. Review is best aimed where the model is weakest: in the bank example, people look at applications from first-time buyers, from lower incomes and with unusual employment. And automated decisions feed the next training data, so Kästner suggests training only on applications a person has reviewed.

Kästner reports that what fairness work gets done is usually pushed by individuals acting as internal activists, almost always without institutional support. His advice is to start early, when requirements and data collection are still open, and to use a checklist such as Microsoft's AI Fairness Checklist (chapter 26).

## Safety: reliability is not safety

**Reliability** is the absence of defects: the system does what it specifies, and how often. Kästner argues that reliability is not enough for safety, because accidents also come from unanticipated interactions, wrong assumptions, and use outside the intended scenario. And that safe systems can be built from unreliable parts (chapter 27).

He borrows an example from Nancy Leveson: a tank of flammable gas. Thicker walls make the tank less likely to burst. When it does, they make the burst more violent. A relief valve serves safety better than thicker walls, by returning the system to a safe state.

By the same reasoning, a more accurate model is a step toward safety and not safety itself. Accuracy and robustness improve reliability (chapter 27). [Guardrails](08-system-quality-end-to-end-tests-and-guardrails.md) are the relief valves.

Robustness has a use at inference time ([chapter 27](https://mlip-cmu.github.io/book/27-safety.html)): check each prediction against small changes it should withstand, and route one that flips to a fallback or a person.

The first question is what an input should withstand. Kästner's example is a stop-sign detector that must tolerate poor light, rain on the lens and a tilted sign. Each anticipated disturbance defines a neighborhood of inputs, and a prediction counts as robust when the inputs in that neighborhood get the same answer. A prediction that passes deserves more confidence. Tools that prove this are expensive, often thousands of inferences per check, so they rarely run in production. No model is robust everywhere, because some inputs always lie near a decision boundary. Robustness is a building block for a safe system, not a safety claim.

Kästner describes safety engineering in four steps (chapter 27):

1. **Identify hazards and safety requirements.** A **hazard** is a condition in which an accident can happen. It makes harm possible, not certain. His example is a sidewalk delivery robot that goes too fast while failing to recognize pedestrians. Analysis can run forward, from the ways a model's prediction can be wrong to the hazards that follow, or backward, from a hazard to the mistakes that could cause it. Named techniques include the fault tree, failure mode and effects analysis, as well as hazard and operability studies. Rank hazards by likelihood times severity.
2. **Find the root causes** of each hazard. The same robot hazard could come from a wrong speed estimate, a missed detection, a bug in the speed controller, or a hardware fault.
3. **Design a mitigation for each one.** Most mitigations make harm less likely by adding independent conditions that must all hold before the hazard can occur. The book's list: keep a human in the loop, make actions undoable and decisions appealable, add guardrails outside the model, install an independent check that detects mistakes, use redundancy, and contain a component's mistakes so they do not spread.
4. **Provide evidence** that the mitigations work. There are two kinds: safe behavior in the field, as when autonomous vehicles move from simulation to test tracks to public roads, and evidence of a rigorous engineering process.

Safety cannot be guaranteed, he writes. Teams demonstrate an acceptable level of it and record claims and evidence in a structured **assurance case**, which breaks one safety claim into subclaims and attaches evidence to each. The autonomous-vehicle company Aurora has published such a structure (chapter 27). He warns against checkbox compliance, where a team goes through the motions to produce paperwork. What he asks for instead is a safety culture: the team takes the safer path when a deadline pushes the other way, and treats a reported concern as something to be thanked for rather than blamed (chapter 27).

Finally, he frames the **alignment problem**, an automated system achieving its assigned objective with unintended consequences, as a requirements problem. An objective that captures only part of the task is met exactly and still misbehaves, because learning algorithms are good at finding such loopholes, a pattern called **reward hacking** (chapter 27). He expects it to matter little for ordinary products with ML components, whose safety concerns yield to hazard analysis. The remedy is still on the requirements page. Write the negative requirements too, "must never" statements, and test them.

## Pitfalls

1. **Quoting a model's rationale as proof.** Fix: test influence by removing inputs and observing the output.
2. **Assuming a blind model is fair.** Fix: audit for proxies, and measure outcomes by group.
3. **Picking a fairness metric silently.** Fix: write the choice and the reason in the requirements.
4. **Measuring equal error rates without labels.** Fix: label a production sample, or fall back to a proxy and say so.
5. **Calling a more accurate model a safer system.** Fix: hazard analysis on the whole system.
6. **A hazard table that lists only solved problems.** Fix: have someone outside the team challenge it.

## Try it

1. Write three hazards for one feature, each with a mitigation that is plain code.
2. Compute one fairness criterion on two slices of your evaluation set, and write one sentence on why you chose that criterion.
3. Take one wrong prediction and produce a counterfactual explanation for it. By hand is fine: change one input value at a time until the prediction flips, and keep the smallest change that did it.

You are done when each hazard names the independent conditions that must hold before harm occurs, when both slices are reported with their sizes, and when the counterfactual names a specific change that flips the prediction. **Stretch goal:** run the anti-classification invariant on every evaluation input and report the violation count.

## Key takeaways

- Match the explanation tool to the question. Explanations are partial approximations, and a model's stated reasons are not evidence.
- Fairness has several formal criteria, and they can conflict. Choosing one is a decision to defend.
- Fairness is a system concern: slices, documentation, monitoring, and process.
- Reliability is not safety. Design mitigations that return the system to a safe state.
- Safety work follows four steps: hazards, causes, mitigations, evidence. Record the evidence, and avoid checkbox compliance.

## Self-check

1. Which explanation tool finds the few conditions that suffice for a prediction, and which finds a change that would flip it?
2. Why can a model that never reads a protected attribute still discriminate?
3. Which fairness criterion needs correct labels, and why?
4. A model's accuracy improves. What has been done for safety?
5. What is a hazard?

<details><summary>Show answers</summary>

1. An anchor finds the sufficient conditions. A counterfactual finds a small change that reverses the result.
2. Because other features correlated with the attribute can act as proxies. The model can learn the same pattern through them.
3. Equalized odds. It compares error rates across groups, and an error can only be identified against the correct answer.
4. Reliability. The model fails less often. Whether the system is safe still depends on the hazards around it and on the mitigations for them.
5. A condition of the system in which an accident can happen. It makes harm possible without making it certain.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 25: [link](https://mlip-cmu.github.io/book/25-explainability.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 26: [link](https://mlip-cmu.github.io/book/26-fairness.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 27: [link](https://mlip-cmu.github.io/book/27-safety.html)

## Next

→ [Security, Privacy, Transparency and Accountability](14-security-privacy-transparency-and-accountability.md), because hazards that come from people who intend harm need a different analysis.
