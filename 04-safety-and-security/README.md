# Part 04: Safety and Security

Threat-model an LLM application or agent, recognize prompt injection and agent-specific attacks, choose defenses and monitoring, and run a red-team exercise.

The reader can build an agent (part 02) and evaluate it (part 03). This part teaches defensive security engineering. It explains the attacker's view only as far as a defender needs it.

## Chapters

| # | Chapter | Level | Read | What you learn to do |
|---|---------|-------|------|----------------------|
| 01 | [Threat Modeling LLM Applications and Agents](01-threat-modeling-llm-applications-and-agents.md) | Practitioner | 25 min | Write a threat model: assets, attackers, trust boundaries, the CIA goals, and where LLM systems differ from ordinary software |
| 02 | [Jailbreaks and Prompt Injection](02-jailbreaks-and-prompt-injection.md) | Practitioner | 25 min | Tell a jailbreak from an injection, explain why instructions and data share one channel, and classify a payload |
| 03 | [Agent-Specific Attacks](03-agent-specific-attacks.md) | Practitioner | 25 min | Recognize memory poisoning, retrieval and tool poisoning, environment injection, propagation, and excessive agency |
| 04 | [Defenses: Guardrails, Detection and Secure Design](04-defenses-guardrails-detection-and-secure-design.md) | Practitioner | 30 min | Assemble a defense in depth, from input filters to privilege separation and human approval gates |
| 05 | [Runtime Monitoring and Detection](05-runtime-monitoring-and-detection.md) | Professional | 20 min | Place runtime protections in an architecture and state their cost, latency, and false-positive trade-offs |
| 06 | [Red-Teaming and Safety Evaluation](06-red-teaming-and-safety-evaluation.md) | Practitioner | 25 min | Run a red-team exercise, build an adversarial data set, measure the attack success rate, and gate regressions in CI |
| 07 | [Trustworthiness Beyond Injection](07-trustworthiness-beyond-injection.md) | Practitioner | 25 min | Test for privacy leakage, stereotyping, and unequal decisions, and explain representation engineering |
| 08 | [AI for Cyber Defense and Vulnerability Detection](08-ai-for-cyber-defense-and-vulnerability-detection.md) | Practitioner | 25 min | Explain how agents find vulnerabilities with interactive tools, and what that changes for defenders |
| 09 | [Policy, Governance and Standards](09-policy-governance-and-standards.md) | Professional | 20 min | Write a marginal-risk assessment, a rollout policy, and place the standards landscape with dates |

## Before you start

You need no machine learning background. Read these three chapters first if you have not:

- [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md), for tools, memory, and the agent loop.
- [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md), because every defense in this part is judged by a measurement.
- [Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md), because most attacks in an agent end in a tool call.

## Two ways through

- **In order, 01 to 09.** Each chapter assumes the one before. The core line is 01, 02, 03, 04, 05, 06.
- **By problem.** Attacked already: start with 01 and 06. Reviewing a design: 01, 03, and 04. Asked about compliance: 09, then 07. Shipping a coding or security agent: 08, then 03.

## What you build

Each chapter ends with an exercise with a deliverable. By the end of the part you have:

1. A one-page threat model of an agent.
2. A harmless injection suite with a canary oracle.
3. An exposure map of the agent's stores, sources, tools, and neighbors.
4. A policy gate on tool calls, with the attack success rate and the utility before and after it.
5. An audit trail and an out-of-band monitor with three rules.
6. A versioned adversarial data set and a CI gate.
7. A trustworthiness report with benign and adversarial results.
8. A small finding loop for memory-safety bugs, in a sandbox.
9. A marginal-risk assessment and a one-page rollout policy.

All demonstration payloads in this part are canaries: harmless words that prove a mechanism. Run them only on systems you own or have written permission to test.

## Sources and dates

- Dawn Song gave the backbone in three Berkeley lectures: Fall 2024 (trustworthiness and policy), Spring 2025 (agentic AI safety and security), and Fall 2025 (agentic AI safety and security, with automatic red teaming and runtime defenses). Chapters attribute each claim to its lecture and timestamp, and the first chapter shows how her frame grew across the three terms.
- Charles Sutton (Google DeepMind) gave the lecture behind chapter 8 (Spring 2025).
- Community lists were checked on November 24, 2026: the OWASP Top 10 for LLM Applications 2025 and the OWASP Top 10 for Agentic Applications 2026.
- Laws, standards, and products change faster than a course. Each dated claim carries its date. Check the current text before you rely on one.

Two topics belong to other parts, which this part links to rather than repeats:

- General security and privacy of ML systems: [Security, Privacy, Transparency and Accountability](../08-quality-assurance/14-security-privacy-transparency-and-accountability.md).
- Capability and risk evaluation: [Evaluating Capabilities and Risks](../03-evaluation/06-evaluating-capabilities-and-risks.md).

## Lecture guides for this part

Each guide maps one lecture from its first minute to its last and says where this book teaches each piece. Where no chapter teaches a part of the lecture, the guide explains it itself; the table counts those parts.

| Lecture | Lecturer | Length | Parts no chapter teaches | Guide |
|---|---|---|---|---|
| Agentic AI Safety & Security | Dawn Song (UC Berkeley) | 1:50:00 | 3 of 10 | [open guide](../lectures/f25-12-agentic-ai-safety-and-security.md) |
| Towards building safe and secure agentic AI | Dawn Song (UC Berkeley) | 1:52:00 | 2 of 10 | [open guide](../lectures/sp25-12-towards-building-safe-and-secure-agentic-ai.md) |
| Towards Building Safe & Trustworthy AI Agents and A Path for Science- and Evidence-based AI Policy | Dawn Song (UC Berkeley) | 1:46:00 | 3 of 19 | [open guide](../lectures/f24-12-towards-building-safe-and-trustworthy-ai-agents.md) |
| Coding Agents and AI for Vulnerability Detection | Charles Sutton (Google DeepMind) | 1:28:00 | 5 of 20 | [open guide](../lectures/sp25-05-coding-agents-and-ai-for-vulnerability-detection.md) |

## Where to go next

- The capstone builds a monitoring agent for prompt injection: [Capstone: Monitoring Agent for Prompt Injection](../11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md).
- Berkeley's course project, in which a green agent prepares tasks and assesses white participant agents, is documented in [the case study](../03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md).
