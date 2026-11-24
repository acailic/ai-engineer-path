# 11. Teams and Technical Debt

**Level:** Practitioner · **Reading time:** 25 min · **Exercise:** 60 min
**Prerequisites:** [Process Models: Planning and Iteration](10-process-models-planning-and-iteration.md)

> **In one sentence:** After this chapter you can map who owns what across a model-based feature, and you can keep a register of technical debt that says what each shortcut costs and who repays it.

## Why this matters

The triage feature shipped after a six-week push. Three months later, the prompt is copied into four services. The evaluation set is a spreadsheet that nobody owns. The data scientist has left, and nobody can say why the threshold is 0.7. Every new request takes longer than the last.

Two things produced this. The team was split into groups that each did their own part and handed it over. And the shortcuts taken under deadline were never written down.

## The core idea

### Teams

No single person is expert in modeling, software engineering, product, and the domain. Job discussions sometimes ask for a **unicorn**, a developer who combines all of these. Kästner's judgment is that such people are rare or may not exist, are hard and expensive to hire, and would not be enough anyway: every product beyond toy size needs a division of labor (chapter 21). So a team needs several people who can talk to each other. A useful shape is the **T-shaped** person: deep in one specialty and able to follow the others. A data scientist need not be a privacy lawyer, but should grasp the principles well enough to understand the lawyer's concern (chapter 21). Kästner uses the term again in chapter 26 as the standard a reader should aim for on any one of these subjects.

Conflicts are normal in such teams. They arise inside a team when goals clash or members do not understand each other, and between teams when responsibilities are unclear or teams are siloed by role (chapter 21). In one organization Kästner describes, four data scientists build a model that the customer's engineers, with little ML experience, must integrate. In another, a single data scientist sits in a team of eight, feels isolated, and has little idea how the model fits the larger system (chapter 21). The conflicts are structural. They do not come from difficult people, and they do not go away with goodwill alone.

### Technical debt

**Technical debt** is the future cost of a shortcut taken today. The metaphor is Ward Cunningham's, from 1992. A quick fix is a loan. Each later change that works around it pays interest. Kästner values the metaphor for its plainness: it lets a developer explain to a manager why time for infrastructure and maintenance is worth spending now (chapter 22).

He follows Martin Fowler's quadrant, which sorts debt along two dimensions (chapter 22). **Deliberate** debt is a known trade. His example is a team that ships an obstacle-detection model for sidewalk delivery robots by copying data by hand and running a notebook, instead of building an automated pipeline first. **Inadvertent** debt comes from not knowing better, and shows only when hours go to copying files. Debt is **prudent** when the shortcut serves a real gain, as when a company deploys many robots early to reach a market first and pays for human oversight of weak navigation models. It is **reckless** when it risks the project, as when safety testing of the same perception models is skipped to save time. Borrowing well is deliberate and prudent. Losing track is inadvertent and reckless.

| Debt common in an LLM feature | How you notice it | Repayment |
|---|---|---|
| The same prompt copied into several services | A fix in one place misses the others | One prompt module with tests |
| Evaluation sets with no owner | Scores cannot be compared over time | A versioned, labeled set |
| A threshold or setting with no recorded reason | Nobody dares change it | A note and a test for the decision |
| A notebook that produced an artifact | The result cannot be reproduced | Pipeline code (see [Pipeline Quality](07-pipeline-quality.md)) |
| An output consumed by an undocumented component | A change breaks a stranger | A list of consumers and a contract |

## How it works, step by step

### Structure the team

1. **List the roles the feature needs.** Model, software, data, product, domain, operations. Name the gaps instead of looking for one person who covers all of them.
2. **Draw team boundaries where the component boundaries are.** People working on one component must coordinate daily, so they should sit in one team. Kästner cites this as **Conway's law**, and counts the cost of ignoring it: communication links grow with n(n−1)/2, so seven people have 21 links until they split into teams that talk through representatives (chapter 21).
3. **Write down the interfaces, and expect them to move.** The classic way to limit communication is information hiding: an interface stands for a component, and others need nothing more. Kästner warns that ML projects strain it. Data science is exploratory, so interfaces change. No good formalism describes what a model can do and where it fails. And qualities such as safety, usability, fairness, and operational efficiency emerge from the interaction of components, so each team assumes another one owns them. For fairness he asks teams to negotiate and to document expectations and assurances at the interface (chapter 26).
4. **Add awareness where interfaces cannot be stable.** The opposite strategy is to broadcast: cross-team meetings, mailing lists, a chat channel, an issue tracker people subscribe to. Informal contacts depend on personal relationships and break when people leave, so write down whom to contact for which issue (chapter 21).
5. **Make goals visible and negotiate them.** Operators want small, fast models. Designers want reliable confidence scores and explanations. Lawyers and data scientists may disagree about which data may be analyzed at all. Kästner asks each member to state what they aim for and how they measure success, and treats the resulting conflict as useful input to a goal for the whole project (chapter 21).
6. **Guard against groupthink.** A team can minimize conflict by not exploring alternatives, suppressing dissent, and shutting out outside views. He sees this with hyped technology, such as reaching for a well-known commercial LLM without considering other techniques, and with risks such as safety and fairness that nobody raises before a deadline. The remedies he lists: hire for diversity, involve outside experts, ask every member for an opinion, let high-status members speak last, moderate meetings, and always explore a second solution (chapter 21).
7. **Decide where specialists sit.** In a **matrix organization** experts belong to departments that lend them to projects, which spreads knowledge across projects and builds deep expertise. In a **project organization** they belong to one team, which gives focus but invites duplicate work. A common hybrid keeps rare experts, in privacy law or security, in a department that every team consults (chapter 21).
8. **Agree on vocabulary, and review across specialties.** DevOps did this for developers and operators, who used to blame each other for unstable code and slow releases, with shared goals, shared terms, and shared tools. MLOps extends it to data scientists and operators (chapter 21). One term for one thing prevents many false arguments: Kästner avoids the word "performance" because data scientists read it as prediction accuracy and software engineers as speed (chapter 15). Review spreads knowledge: a data scientist learns another's techniques and catches a bad transformation (chapter 17).
9. **Bring in outside eyes.** Kästner sees value in dedicated testing teams for an independent perspective in later stages, focused on system testing, security audits, penetration testing, and fairness audits (chapter 14).
10. **Review without blame.** He recommends retrospectives and avoiding blame as part of building a quality culture (chapter 14). A team that punishes bad news stops hearing it.

### Manage the debt

Kästner's list of where ML projects incur debt is a good place to look for candidates (chapter 22):

- **Using ML where a rule would do.** The problem looked quick to solve with ML and carries maintenance costs nobody priced.
- **Data debt.** Nobody checks or monitors the data the model depends on.
- **Infrastructure debt.** Models are moved from a notebook to production by hand, so updates are rare and robots end up on mismatched versions.
- **Versioning debt.** Results cannot be reproduced, and a regression cannot be traced to a change in data or code.
- **Observability debt.** There is no monitoring, so each production problem is investigated by guesswork.
- **Code quality debt, architectural debt, and test debt.** Dead experiments, glued scripts, and models stacked on models with no integration tests. The team can only guess which of five recently updated models sends robots into bike lanes.
- **Requirements debt.** A skipped analysis lets a feedback loop loose, as when a robot optimized for speed makes pedestrians dodge, which rewards even more speed.

Then repay in this order:

1. **Record each debt with its cost and its owner.** Kästner asks for more than an issue: a named person responsible, the extra maintenance cost watched, and a goal for whether and when to pay it back. Some teams set aside fix-it days (chapter 22).
2. **Fix design debt first.** Debt in requirements and design is much harder to repay than debt in code quality or missing automation. A robot built without redundant sensors cannot be patched. Monitoring can be added later (chapter 22).
3. **Add tests before you change it.** Refactoring untested pipeline code trades one debt for a bug (chapter 17).
4. **Repay in small steps, next to related work.** Fix the prompt duplication when you next edit a prompt.
5. **Measure what is covered.** The ML Test Score, described in chapter 17 of the book, scores a team by how many of 28 testable concerns it covers.
6. **Take debt on purpose or not at all.** Under deadline, a recorded shortcut with a date is a decision. An unrecorded one is a surprise for someone else.

## What the practitioners say

- **The people who make the data are strangers.** The people who gather, type in and label data often sit apart from the people who use it, and few teams count them as members (chapter 16).
- **Documentation is coordination.** Data usually crosses team boundaries, so documenting its meaning and quality matters and is often neglected (chapter 16).
- **Culture needs management.** A quality culture takes time and money and buy-in from managers and the whole team, not rules imposed from above (chapter 14).
- **Specialists without power accomplish little.** In fairness work, Kästner finds that what gets done is pushed by individuals acting as internal activists, almost always without institutional support, and that central teams for responsible ML are often research-focused and rarely have the power to influence product teams (chapter 26).
- **Rare specialists are an old problem.** He compares fairness, privacy, usability, and operations experts in ML teams with security experts twenty years earlier: all want to be involved early, no team can afford each of them full time, and training is often seen as a distraction or a compliance exercise (chapter 21).
- **Debt grows silently.** Chapter 15 notes that frequent evaluation wears out a test set. Chapter 22 names versioning debt: results that cannot be reproduced and a regression that cannot be traced to a change in data or code. Both are habits that decay unless someone owns them.

## Pitfalls

1. **Searching for a unicorn.** Fix: build a team and make its members T-shaped.
2. **Handing work over a wall.** Fix: write the interface and review across it.
3. **Two words for one thing.** Fix: a shared glossary, used in documents and code.
4. **Treating debt as a personal failing.** Teams then hide it. Fix: a blameless register.
5. **Refactoring without tests.** Fix: characterize the current behavior first.
6. **Central experts without authority.** Fix: give them a required sign-off, or embed them in the teams.

## Try it

1. Draw an ownership map for one feature: who owns the data, the model or prompt, the guardrails, the evaluation set, and the monitoring. Mark every cell with a named person or with "nobody".
2. Start a debt register. List ten shortcuts. For each, write where it is, what it costs today, and who will repay it.

You are done when no cell in the map says "nobody", and when every entry in the register has a cost and an owner. **Stretch goal:** pick the entry with the highest cost, write a test that pins down the current behavior, and repay it.

## Key takeaways

- ML products need several specialties. Look for T-shaped teammates, not for one person who knows everything.
- Conflicts between data scientists and software engineers are structural. Interfaces, shared vocabulary, and cross-review reduce them.
- Technical debt is the future cost of a shortcut. Prudent debt is chosen and recorded.
- Keep a register of debts with their cost and owner, and repay next to related work.
- Add tests before refactoring.
- Independent views, from testers or specialists, only matter if they have the authority to be heard.

## Self-check

1. Why is searching for one person with every needed skill a poor plan?
2. A data scientist and an engineer disagree about a model's "performance". What is the likely cause?
3. What separates prudent debt from neglect?
4. What should exist before a risky piece of pipeline code is refactored?
5. A central team reviews products for risks and nobody acts on its reports. What is missing?

<details><summary>Show answers</summary>

1. Such people are extremely rare. A team of specialists who each understand a little of the others' work covers the same ground and is far easier to assemble.
2. The word means prediction accuracy to one of them and speed to the other. A shared vocabulary removes the dispute.
3. A decision. Prudent debt is taken knowingly, under a deadline, and recorded with the intent to repay. Neglect is a shortcut nobody noted.
4. Tests that pin down its current behavior, so that a change which breaks something is caught at once.
5. Authority and ownership. Review without the power to require a fix, or a team obliged to act, changes nothing.

</details>

## Sources

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 21: [link](https://mlip-cmu.github.io/book/21-interdisciplinary-teams.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 22: [link](https://mlip-cmu.github.io/book/22-technical-debt.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapters 14 to 20, 26 and 28, for the points cited above: [chapter 14](https://mlip-cmu.github.io/book/14-quality-assurance-basics.html), [chapter 26](https://mlip-cmu.github.io/book/26-fairness.html)
- **Reading:** Ward Cunningham, "The WyCash Portfolio Management System" (1992), the origin of the debt metaphor: [link](https://c2.com/doc/oopsla92.html)

## Next

→ [Responsible Engineering, Versioning and Reproducibility](12-responsible-engineering-versioning-and-reproducibility.md), because "nobody can reproduce that result" is the most common debt of all, and versioning is how it is repaid.
