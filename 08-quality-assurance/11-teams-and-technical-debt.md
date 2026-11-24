# 11. Teams and Technical Debt

**Level:** Practitioner · **Reading time:** 16 min · **Exercise:** 60 min
**Prerequisites:** [Process Models: Planning and Iteration](10-process-models-planning-and-iteration.md)

> **In one sentence:** After this chapter you can map who owns what across a model-based feature, and you can keep a register of technical debt that says what each shortcut costs and who repays it.

## Why this matters

The triage feature shipped after a six-week push. Three months later, the prompt is copied into four services. The evaluation set is a spreadsheet that nobody owns. The data scientist has left, and nobody can say why the threshold is 0.7. Every new request takes longer than the last.

Two things produced this. The team was split into groups that each did their own part and handed it over. And the shortcuts taken under deadline were never written down.

<!-- SOURCE GAP: the packets for book chapters 21 (Interdisciplinary Teams) and 22 (Technical Debt) contain section headings only, no body text. This survey is the author's, arranged under those headings. Every statement attributed to the book comes from another chapter and is cited to it. -->

## The core idea

### Teams

No single person is expert in modeling, software engineering, product, and the domain. A team needs all four, so it needs several people who can talk to each other. A useful shape is the **T-shaped** person: deep in one specialty and able to follow the others. Kästner uses the term in chapter 26 as the standard a reader should aim for on any one of these subjects.

Kästner observes in chapter 20 that ML products are built by interdisciplinary teams whose habits differ, and that conflicts follow when members do not understand each other's process. The conflicts are structural. They do not come from difficult people, and they do not go away with goodwill alone.

### Technical debt

**Technical debt** is the future cost of a shortcut taken today. The metaphor is Ward Cunningham's, from 1992. A quick fix is a loan. Each later change that works around it pays interest.

The analogy breaks on visibility. A loan comes with a statement that shows the balance and the rate. Debt in a system shows up only when someone touches the shortcut, and often nobody can say what it costs.

The book's outline for chapter 22 has a section on debt that is **deliberate and prudent**. A prudent shortcut is chosen, recorded, and has a repayment plan. That is the difference between borrowing and losing track.

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
2. **Write down the interfaces.** For each boundary, record what one side provides and what the other may assume. Kästner calls for documenting expectations and assurances at the interfaces between teams, and treats it as a recurring theme of the book (chapter 26).
3. **Agree on vocabulary.** He avoids the word "performance" because data scientists read it as prediction accuracy and software engineers as speed (chapter 15). One term for one thing prevents many false arguments.
4. **Review across specialties.** Review spreads knowledge: a data scientist learns another's techniques and catches a bad transformation (chapter 17).
5. **Bring in outside eyes.** Kästner sees value in dedicated testers for an independent view late in a project (chapter 14), and in security experts for design and testing (chapter 28).
6. **Review without blame.** He recommends retrospectives and avoiding blame as part of building a quality culture (chapter 14). A team that punishes bad news stops hearing it.

### Manage the debt

1. **Walk the system and list what you would rather not touch.** Each item is a candidate.
2. **Record each one with its interest and its owner.** The interest is how it slows work today.
3. **Add tests before you change it.** Refactoring untested pipeline code trades one debt for a bug (chapter 17).
4. **Repay in small steps, next to related work.** Fix the prompt duplication when you next edit a prompt.
5. **Measure what is covered.** The ML Test Score paper, listed in chapter 17, scores a team by how many of 28 testable concerns it covers.
6. **Take debt on purpose or not at all.** Under deadline, a recorded shortcut with a date is a decision. An unrecorded one is a surprise for someone else.

## What the practitioners say

- **The people who make the data are strangers.** The people who gather, type in and label data often sit apart from the people who use it, and few teams count them as members (chapter 16).
- **Documentation is coordination.** Data usually crosses team boundaries, so documenting its meaning and quality matters and is often neglected (chapter 16).
- **Culture needs management.** A quality culture takes time and money and buy-in from managers and the whole team, not rules imposed from above (chapter 14).
- **Specialists without power accomplish little.** In fairness work, Kästner finds that most teams do nothing concrete, that individuals push what gets done without institutional support, and that central teams for responsible ML are often research-focused with little influence on product teams (chapter 26).
- **Security shows the same pattern.** Managers must plan time for it, contributions must be valued, and steps must not be skipped under deadline pressure (chapter 28).
- **Debt grows silently.** Chapter 15 notes that frequent evaluation wears out a test set, and chapter 19 that a fast rollback depends on rigorous versioning. Both are habits that decay unless someone owns them.

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

- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 21 (section outline consulted): [link](https://mlip-cmu.github.io/book/21-interdisciplinary-teams.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapter 22 (section outline consulted): [link](https://mlip-cmu.github.io/book/22-technical-debt.html)
- **Book:** Christian Kästner, *Machine Learning in Production: From Models to Products* (MIT Press, 2025), chapters 14 to 20, 26 and 28, for the points cited above: [chapter 14](https://mlip-cmu.github.io/book/14-quality-assurance-basics.html), [chapter 26](https://mlip-cmu.github.io/book/26-fairness.html)
- **Reading:** Ward Cunningham, "The WyCash Portfolio Management System" (1992), the origin of the debt metaphor: [link](https://c2.com/doc/oopsla92.html)

## Next

→ [Responsible Engineering, Versioning and Reproducibility](12-responsible-engineering-versioning-and-reproducibility.md), because "nobody can reproduce that result" is the most common debt of all, and versioning is how it is repaid.
