# 14. Security, Privacy, Transparency and Accountability

**Level:** Practitioner · **Reading time:** 19 min · **Exercise:** 90 min
**Prerequisites:** [System Quality: End-to-End Tests and Guardrails](08-system-quality-end-to-end-tests-and-guardrails.md)

> **In one sentence:** After this chapter you can run a five-stage threat model over an LLM feature, apply the two design principles that limit most damage, and state what you tell users about the model and who answers for its decisions.

## Why this matters

Three more questions arrive in the same month.

- A customer discovers that a sentence inside a ticket makes the refund suggester propose a payout.
- Legal asks which customer data the model provider can see.
- A customer asks whether a human ever read the complaint, and how to contest an automated decision.

The first is **security**. The second is **privacy**. The third is **transparency and accountability**.

## The core idea

**Security** protects a system from people who intend to harm it. Requirements fall into three classes, the **CIA triad**: confidentiality (only authorized people read sensitive data), integrity (data and decisions are not tampered with), and availability (the service keeps running). Kästner notes that ML adds new things to protect: training data, models, prompts, and telemetry (chapter 28).

**Privacy** means that a person decides which personal information other parties get, and what they may do with it. Security is necessary for privacy and not sufficient for it. A system can break its privacy promises without any attacker, by selling data it promised to guard (chapter 28).

**Transparency** means telling the people affected that a model is involved and what it does. **Accountability** means a named person or role answers for each kind of automated decision, and an affected person can appeal it.

Kästner's conclusion about ML security is sobering. Attack and defense form an arms race, and broad guarantees at the model level are unlikely (chapter 28). The practical rule is to assume the model can be tricked and to secure the system around it. That is the same reasoning as [chapter 08](08-system-quality-end-to-end-tests-and-guardrails.md) on guardrails.

## How it works, step by step

### 1. Know the five attacks specific to ML

| Attack | What the attacker does | In a support product |
|---|---|---|
| **Evasion** | Crafts an input that looks harmless and produces the prediction they want | A message phrased so the triage model routes it to a low-priority queue |
| **Poisoning** | Manipulates training data, to degrade the model or to plant a back door | Flooding the system with mislabeled reports |
| **Model extraction** | Queries a model repeatedly to learn a copy of it | Rebuilding the routing model from its answers |
| **Model inversion and membership inference** | Recovers training data, or learns whether a record was in it | Extracting an earlier customer's text from a fine-tuned model |
| **Prompt injection and jailbreaking** | Puts instructions inside data the model will read, or talks it past its safeguards | The ticket sentence that asks for a refund |

Kästner compares prompt injection to SQL injection and cross-site scripting: data and instructions end up in one channel (chapter 28). He also emphasizes how many routes lead to training data. Public data sets, crowd labels, and telemetry can all be influenced without breaking in.

Defending the model itself is covered in [Defenses and Guardrails](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) in part 04. This chapter stays at the system level.

### 2. Threat-model the whole system

Start from a **security mindset**: any component may be compromised, any user may misbehave, any input may be malicious. Perfect security is out of reach, so the goal is to reduce risk ([chapter 28](https://mlip-cmu.github.io/book/28-security-and-privacy.html)).

The mindset does not come naturally to every developer, and many dislike the negative thinking it asks for. Kästner's remedies are training, building security into the process, and above all bringing in experts ([chapter 28](https://mlip-cmu.github.io/book/28-security-and-privacy.html)).

**Threat modeling** is a structured review of a system's design for security threats, done early in design or as an audit. Kästner describes five stages (chapter 28):

1. **Attacker goals and capabilities.** Teenagers trying to bypass a filter for bragging rights and a state-backed team with patience and budget call for different defenses. The more likely attacker may deserve more attention than the stronger one.
2. **System structure.** Draw a data-flow diagram that includes every store, the training and serving components, and monitoring. Show how training and inference data can be influenced, including by the people who label it.
3. **Threats.** Inspect every component and connection against a checklist. The book names STRIDE, a method from Microsoft with six categories: spoofing an identity, tampering with data, repudiation, in which a user denies an action, information disclosure, denial of service, and elevation of privilege (chapter 28).
4. **Risk.** Rate each threat by likelihood and by damage if it succeeds, on rough scales, and rank by the product. The absolute scores do not matter. The order does.
5. **Implement and test defenses.** Prefer proven standards and libraries over new security ideas, and bring in experts (chapter 28). Some weaknesses are coding mistakes, such as unsanitized input or a misused cryptographic library. The OWASP Top 10 for web applications and MITRE's CWE list the common ones, and **static analysis**, which reads code without running it, catches many during continuous integration, a practice marketed as DevSecOps ([chapter 28](https://mlip-cmu.github.io/book/28-security-and-privacy.html)).

### 3. Apply the two design principles

- **Minimize the attack surface.** Remove ways to interact with the system. Kästner asks whether a model API needs to be public and whether it must return precise confidence scores (chapter 28).
- **Least privilege.** Give each component the minimum access it needs. In the book's example, a content-moderation service can flag a post but cannot delete it, and cannot read payment details (chapter 28). An agent that drafts refunds needs the refund tool and nothing else.

### 4. Monitor, and test as an attacker

Intrusion detection watches for unusual behavior. Kästner notes that the 2017 Equifax breach would have shown up early in network traffic, if an intrusion-detection system had not been offline on an expired certificate (chapter 28). For an agent, the equivalent signals are odd tool-call patterns and data volumes.

**Red teaming** has experts attack a system on purpose and report what they find. It complements threat modeling and tested defenses. It does not replace them, and Kästner thinks the term is overused for work that deserves a more structured method (chapter 28).

### 5. Design for privacy

- **Collect less.** Decide what the service needs and stop there (chapter 28).
- **Know what a model can infer.** ML can predict age, gender, race, or political leaning from a few queries or posts, cheaply and at scale. Data merged from several sources, each shared for another purpose, sharpens such predictions, and users rarely see that coming (chapter 28).
- **Count what you send to a provider.** Text placed in a prompt is data disclosed to the model's operator. Redact it, and read the provider's terms for how inputs may be reused.
- **Keep stored data available and private.** Training data, evaluation sets and logs hold customer text, and later audits and retraining depend on them. Redundant storage and backups protect them from a failed disk or a deleted table; authentication and encryption keep out everyone but the people who need access. Remove identifying details before storage where you can, though Kästner warns that anonymization is notoriously tricky, because models infer missing data well ([chapter 28](https://mlip-cmu.github.io/book/28-security-and-privacy.html)). He notes that an organization can provide the storage infrastructure, with its backups and security, for all teams to build on ([chapter 16](https://mlip-cmu.github.io/book/16-data-quality.html)).
- **Explain and offer controls.** A **privacy policy** is the public record of the system's privacy decisions. Fine-grained controls give users more agency than one blanket agreement (chapter 28).

### 6. Be transparent, and name who is accountable

Kästner separates transparency about the model's *existence* from transparency about *how it works* (chapter 29). In a 2015 study he cites, 62 percent of surveyed Facebook users did not know that an algorithm curated their feed rather than showing every post, and many reacted with surprise and anger when told. He also cites reports of managers who did not know that an automated tool had discarded applicants before they saw them.

Before writing a notice, name its goal: trust at the right level, so that users know when to check the model; support for an appeal; or a feeling of autonomy and dignity. Kästner warns that trust the system has not earned puts users at risk, and says to test the design with users ([chapter 29](https://mlip-cmu.github.io/book/29-transparency-and-accountability.html)).

1. **Say that a model is involved**, where it affects people. Hiding it removes the chance to appeal, and users feel deceived when they find out.
2. **Explain at a useful level.** Users form a mental model of how a system decides, correct or not, and they need some understanding to point out a mistake. For high-stakes decisions such as loans, hiring, or housing, Kästner considers explicit explanations and a stated level of certainty important. For low-stakes ones, such as spelling correction, automation without explanation can be acceptable (chapter 29). Show sources next to generated claims.
3. **Weigh the risk of gaming.** A counterfactual helps a person change what they can (see [chapter 13](13-explainability-fairness-and-safety.md)). It also tells a student how an automatic grader works, or a spammer which words to avoid. Models built on robust, causally related features invite the behavior you want. Models built on weak proxies invite gaming, and hiding their workings is only security by obscurity (chapter 29).
4. **Keep oversight real and allow appeals.** Reviewing every decision is too expensive at scale, and even a complaints team can be costly. Kästner's test: if oversight costs too much to afford, the product may not be viable in its planned form (chapter 29). The principle lists in chapter 23 include human alternatives and human oversight.
5. **Assign an owner to each decision type**, and keep the records from [chapter 12](12-responsible-engineering-versioning-and-reproducibility.md), so that any decision can be reconstructed.
6. **Blame a decision, not "the algorithm".** Harm traces back to human choices about the system's design, evaluation, and safeguards. A producer that integrates third-party models or data is responsible for the whole product, as a car maker is for defective tires (chapter 29).

## What the practitioners say

- **A famous extraction dispute.** In 2011, Google accused Microsoft's search engine of learning from Google's results. In a sting, Google set up results for synthetic queries and found the same answers elsewhere weeks later (chapter 28). Kästner knows of few public real-world cases of model extraction and would not be surprised if it were common.
- **Memorization leaks.** Researchers have recovered medically sensitive information, such as schizophrenia diagnoses or suicide attempts, from a model trained on discharge records (chapter 28, citing published attacks).
- **Jailbreaking changes the frame.** The book's example asks the model to pretend to be a character in a play (chapter 28).
- **The incentives point the other way.** More data means better models, more users, and more data. Kästner cites a social network's long-running argument that privacy is losing importance, and the idea of a data lake that stores everything in case it proves useful (chapter 28).
- **Policies rarely inform.** He describes a restaurant app whose privacy policy takes about fifteen minutes to read and grants broad rights, while the app's controls cover very little (chapter 28).

## Pitfalls

1. **Giving a model-driven agent broad tool access.** Fix: least privilege. Only the tools the task needs.
2. **Trying to make the model impossible to trick, and stopping there.** Fix: assume it can be tricked, and bound the damage in code.
3. **Threat-modeling the model alone.** Fix: the whole data flow, including labels and telemetry.
4. **Detection by a second prompt as the only defense.** Fix: standard controls around it, and tests with hostile input.
5. **Sending raw customer data to a model provider.** Fix: redact, minimize, and check the terms.
6. **Transparency buried in a policy.** Fix: a short notice at the point of use, and a route to a human.
7. **Oversight that rubber-stamps.** Fix: evidence next to each action and a volume a person can read.

## Try it

1. Write a one-page threat model for one feature: the attacker, their capability, a data-flow sketch, and five threats with likelihood and damage scores.
2. Implement two mitigations in plain code: one that narrows the attack surface, one that applies least privilege.
3. Write a three-sentence disclosure for users, and name the appeal path.

You are done when the threats are ranked, when each mitigation has a test with hostile input, when the disclosure says what the model does and what a person can do about it, and when every automated decision type has a named owner. **Stretch goal:** have a colleague who did not build the feature run a fifteen-minute red team against it, and turn each finding into a test.

## Key takeaways

- Security requirements are confidentiality, integrity, and availability. ML adds training data, models, prompts, and telemetry.
- Five attacks are specific to ML: evasion, poisoning, extraction, inversion and membership inference, and prompt injection.
- Threat-model the whole system in five stages, and rank threats by likelihood times damage.
- Assume the model can be tricked. Minimize the attack surface and apply least privilege.
- Privacy is control over one's own information. Collect less, and treat prompt text as a disclosure.
- Tell people a model is involved, explain at a useful level, allow appeals, and name an owner for every decision type.

## Self-check

1. Which attack plants instructions in data that a model will read, and which well-known older attacks does it resemble?
2. Why rank threats by a product of two rough scores if the scores are made up?
3. A model-driven agent has access to every internal tool. Which principle is violated?
4. A system is secure and still breaks privacy. How?
5. What two things does transparency about a model cover, according to the book's chapter 29?

<details><summary>Show answers</summary>

1. Prompt injection. It resembles SQL injection and cross-site scripting, where data and instructions share one channel.
2. Because the ranking is what matters. The absolute values are judgments, and a consistent relative order is enough to decide what to fix first.
3. Least privilege. The agent should hold only the access its task requires, so that a tricked agent can do little.
4. By its own actions, without any attacker: using or sharing data in ways the user did not agree to.
5. That the model exists at all, and how it works.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 28: [link](https://mlip-cmu.github.io/book/28-security-and-privacy.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 29: [link](https://mlip-cmu.github.io/book/29-transparency-and-accountability.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 23, for the principle lists cited above: [chapter 23](https://mlip-cmu.github.io/book/23-responsible-engineering.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 16, for data storage: [chapter 16](https://mlip-cmu.github.io/book/16-data-quality.html)

## Next

→ [Threat Modeling LLM Applications and Agents](../04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) in part 04, because agents that call tools widen the attack surface that this chapter's method needs to cover.
