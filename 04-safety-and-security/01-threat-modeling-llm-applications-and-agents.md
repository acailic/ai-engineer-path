# 01. Threat Modeling LLM Applications and Agents

**Level:** Practitioner · **Reading time:** 25 min · **Exercise:** 90 min
**Prerequisites:** [The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md)

> **In one sentence:** After this chapter you can write a one-page threat model of an LLM application or agent, with its assets, attackers, trust boundaries, and one control for each serious path.

## Why this matters

Your team ships a travel-planning agent. It reads a calendar, searches the web, sends email, and pays for tickets up to 200 US dollars. The security review asks for the threat model. Someone writes "prompt injection" on the board. The meeting ends, and nobody has asked who can reach the pay tool.

A **threat model** answers three questions about a system before anyone builds a defense: what must be protected, who would attack it, and where their input can enter. This chapter shows how to do that for a system with a language model in it.

## The core idea

An LLM application is not one program with a new library. Dawn Song calls it a **hybrid system**, or compound system: ordinary code, which she calls **symbolic components**, joined to a **neural component**, the model, that turns text into text ([4:00], Fall 2025). Her reason for treating it as a whole: "the overall agent AI system safety and security is much more complex than just the model level" ([4:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=240)).

Three definitions carry the rest.

- An **asset** is anything worth protecting.
- An **attacker** is anyone who controls input the system will read or run. Attackers are not only criminals. A customer who wants a higher refund is an attacker too.
- A **trust boundary** is a line where data crosses from one party to another. The network edge is one. In an agent, every tool result and every fetched page crosses one.

The analogy is threat-modeling a web application: enumerate entry points, assets, and who can reach what. The analogy breaks at the parser. A web framework rejects input that does not fit its grammar. A language model has no grammar for "instruction" against "data". Everything it reads arrives in one channel, so every input is a possible instruction.

## How it works, step by step

### 1. Draw the system, not the model

Draw five boxes: user, application code, model, tools, and the outside world. Mark what flows on each arrow.

```text
 user ──request──▶ app code ──prompt──▶ model ──text and tool calls──▶ app code ──▶ tools
                     ▲                                                        (mail, calendar, pay)
                     └──── tool results, web pages, files, saved memory ────────┘
```

Song walks a hybrid system in seven steps ([22:00], Spring 2025): the host deploys the model, the user sends a request, the system assembles the prompt and calls the model, the model interacts with the rest of the system, the system touches the outside world, the system answers the user, and the system keeps running for long tasks. She then asks of each step, "what could go wrong?".

### 2. List the assets

Start with the classic three goals, the **CIA triad**:

- **Confidentiality**: only authorized parties can read the information.
- **Integrity**: the system and its data are not altered, on purpose or by accident, and stay accurate.
- **Availability**: authorized users get reliable and timely access.

Song adds what an LLM system has to protect beyond ordinary data ([16:00], Spring 2025): the API key for the model service, the secret system prompt, the users' prompts, the conversation history, the model's own parameters, and the availability of the model service. To these, an agent adds what its tools can reach: the mailbox, the calendar, the wallet.

### 3. Name the attackers and what they control

| Attacker | Controls | Does not control |
|----------|----------|------------------|
| Malicious user | Their own prompts and files | Your code, your model |
| Outside party | A page, a mail, a calendar entry, a review, a code comment the agent will read | The user's request |
| Poisoned supplier | A model file, a package, a data set you depend on | Your deployment |
| Accidental user | Nothing. Their request contains untrusted data without their knowing | Anything |

Fall 2024 gave a short checklist for this step: who causes the harm, who is harmed, was it an accident or on purpose, and what kind of harm ([36:00](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=2160)).

### 4. Mark the trust boundaries

A boundary exists wherever data from one row of the table reaches your system. In the diagram there are three: the request, every tool result, and the deployment itself. The prompt is where the first two merge. That merging is the root cause of the attacks in [Jailbreaks and Prompt Injection](02-jailbreaks-and-prompt-injection.md).

### 5. Follow the model's output

Song lists five ways a system uses what the model produces, each with its own failure (slide, Spring 2025; [28:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=1680)).

| Use of the output | Failure it enables |
|-------------------|--------------------|
| Shown to a user | Leaks information |
| Fed into more model calls | Compounds errors |
| Read as a branch condition | Unexpected control flow |
| Used as parameters of a function call | SQL injection, server-side request forgery |
| Executed as code | Arbitrary code execution |

Two of these deserve names. **Improper output handling** is when the system trusts the output enough to pass it to a shell, a database, or a URL. A **supply chain attack** is when something you imported was already malicious.

### 6. Assume how good the model is

Song sorts models into five **security levels** ([32:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=1920)).

- L0: accurate and secure.
- L1: accurate, but not trained to resist attacks.
- L2: inaccurate and insecure. It also hallucinates, meaning it states things that are false.
- L3: poisoned. It has a **backdoor**: a hidden trigger that makes it misbehave.
- L4: malicious, for example a model file that runs code when loaded.

Design for L2. A control that works only with an L0 model is not a control.

### 7. Check the list

Two community lists catch what a team forgets. The names are from the OWASP Top 10 for LLM Applications, 2025 edition (opened November 2026). The questions are mine.

| Name | The question it makes you ask |
|------|-------------------------------|
| LLM01:2025 Prompt Injection | Can someone else's text reach the model? |
| LLM02:2025 Sensitive Information Disclosure | What could the model say, to whom? |
| LLM03:2025 Supply Chain | What do you import, and who built it? |
| LLM04:2025 Data and Model Poisoning | Could your training or retrieval data be altered? |
| LLM05:2025 Improper Output Handling | Where does the output go next? |
| LLM06:2025 Excessive Agency | Which tool has more power than its task needs? |
| LLM07:2025 System Prompt Leakage | What secret lives only in the prompt? |
| LLM08:2025 Vector and Embedding Weaknesses | Who can write into your document index, and who can read whose? |
| LLM09:2025 Misinformation | What happens when the answer is wrong? |
| LLM10:2025 Unbounded Consumption | What stops a loop or a huge input? |

For agents, OWASP publishes a second list, the Top 10 for Agentic Applications 2026 (opened November 2026). It covers agent goal hijack, tool misuse, identity and privilege abuse, supply chain, unexpected code execution, memory and context poisoning, insecure inter-agent communication, cascading failures, human-agent trust exploitation, and rogue agents. [Agent-Specific Attacks](03-agent-specific-attacks.md) walks through them.

## Worked example

A threat model for the travel agent, one row per path. Severity is the worst outcome with no control.

| # | Attacker and entry point | Asset | Goal | Severity | Control |
|---|--------------------------|-------|------|----------|---------|
| 1 | Outside party. A flight page the agent reads | Wallet, mailbox | Integrity | High | Policy gate on every tool call |
| 2 | Outside party. Same page | User's requests | Integrity | Medium | Monitor that flags goal changes |
| 3 | Malicious user. A request naming another user's trip | Other users' trips | Confidentiality | High | Identity checked in the tool, not by the model |
| 4 | Poisoned supplier. A model file | Whole host | All three | High | Pinned and scanned dependencies |
| 5 | Anyone. Model output passed to a database query | Database | Integrity | High | Parameterized queries only |
| 6 | No attacker. A bug grants the pay tool no limit | Wallet | Integrity | Medium | Least privilege, per-task limit |
| 7 | Malicious user. A request that triggers an endless loop | Budget, availability | Availability | Low | Step and token budgets |

What to observe: row 1 is the prompt-injection path, and it has an asset and a control. "Prompt injection" alone named none of the three. Row 6 has no attacker, which is why step 3 lists accidental users.

## Where LLM systems differ from ordinary software

| Aspect | Ordinary software | System with an LLM |
|--------|-------------------|--------------------|
| Meaning of input | Fixed by a grammar. Bad input is rejected. | Interpreted. No rule separates instruction from data |
| Behavior | Written in code | Learned, probabilistic, and different on each run |
| Attack surface | The interfaces you expose | Everything the model reads |
| Output | Computed | Generated, and often used as code, SQL, or a tool call |
| Failure with no attacker | Bugs | Bugs, plus false statements and bias |
| Testing | Unit tests | Tests, plus statistical evaluation and red teaming |

## What the practitioners say

Dawn Song gave versions of this lecture in three terms, and the frame grew each time.

- **Fall 2024: harms.** She organized agent safety around four questions (who causes harm, who is harmed, accident or purpose, which kind of harm) and listed the kinds: loss of utility or denial of service, information leakage, resource hijack such as crypto mining, harmful content, and financial loss ([36:00](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=2160)).
- **Spring 2025: the system.** She added the hybrid-system view, the CIA goals with the new assets, the seven-step walkthrough, the five uses of the output, and the model security levels ([14:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=840)). She separated model misuse from system misuse: the system can amplify a model's risk, and a well-designed one can keep a model misuse from turning into a system misuse ([36:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=2160)). Her verdict on the state of defense: very little existed for hybrid systems, which motivates a secure agent framework ([76:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=4560)).
- **Fall 2025: more surfaces.** She kept the frame and left model-level risks out ([4:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=240)). The examples moved from résumés to calendar entries ([44:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=2640)) and fake re-authentication prompts ([50:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=3000)). She stressed that classic bugs such as SQL injection and remote code execution are now reachable through model output ([26:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=1560)).

She also draws the line between **safety** and **security**. Security protects the system from outsiders. Safety means the system does no harm to the outside world. Safety has to assume adversaries, she says, because a compromised system cannot keep its own safety promises ([2:00](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=120)).

Teams that already use the MITRE ATT&CK knowledge base for conventional systems can look at its companion for AI systems, MITRE ATLAS. <!-- VERIFY: MITRE ATLAS was not opened for this chapter. -->

## Pitfalls

- **The threat model is one line.** "Prompt injection" names a technique, not an asset. For each path, write who attacks, through what, to reach which asset.
- **Trusting tool results.** A tool returns what the outside world contains. Treat every result as untrusted input, like a request from the internet.
- **Assuming your user is on your side.** A user can be malicious, or can paste data someone else wrote.
- **Letting the model enforce the policy.** A prompt that says "never pay without approval" is a request to an L2 model. Enforce in code.
- **Forgetting availability.** A loop or a huge document costs money and blocks service. Add budgets.
- **Modeling attacks only.** Misuse by the person holding the tool is a threat with no injection in it.
- **Modeling the model instead of the system.** Most incidents come from the join between the model and your code.

## Try it

Write a one-page threat model for an agent you have built or used.

1. Draw the five boxes and the arrows.
2. List the assets, including what each tool can reach.
3. Fill the attacker table.
4. Write at least eight path rows in the format of the worked example.
5. Check the rows against both OWASP lists.

You are done when every tool and every outside data source appears in at least one row, and every row of high severity names a control that lives in code. Stretch goal: turn your two simplest rows into harmless tests, as described in [Red-Teaming and Safety Evaluation](06-red-teaming-and-safety-evaluation.md).

## Key takeaways

- A threat model names assets, attackers, and trust boundaries. In an agent, every tool result crosses a boundary.
- The model's output is an input to the rest of your system, and it can become code, SQL, or a tool call.
- Design for an inaccurate and insecure model. Security level L2 is the safe assumption.
- Song's frame grew over three terms: harms first, then the hybrid system with CIA goals and output paths, then more entry points.
- Use the OWASP lists as a checklist for what your team forgot, not as the threat model itself.

## Self-check

1. Your agent fetches a web page and passes its text to the model. Which trust boundary does the page cross, and why does that matter?
2. What are the five security levels for a model, and which one should you design for?
3. A colleague says the pay tool is safe because the system prompt forbids unauthorized payments. What is the flaw?
4. Why does step 5 distinguish output used as a branch condition from output used as a function parameter?
5. Name the three CIA goals and one asset that only exists because the system uses an LLM.

<details><summary>Show answers</summary>

1. The boundary between the outside world and the application. The page's text is merged into the prompt, so it can act as an instruction.
2. L0 accurate and secure; L1 accurate but vulnerable; L2 inaccurate and vulnerable; L3 poisoned; L4 malicious. Design for L2.
3. A system prompt is a request to the model, not a rule enforced by code. An inaccurate or attacked model can ignore it.
4. A branch condition changes which code runs next. A function parameter reaches a tool such as a shell or database, where it can inject SQL or a command.
5. Confidentiality, integrity, availability. Examples: the system prompt, the API key, the conversation history, the model's parameters.

</details>

## Sources

- **Lecture:** Dawn Song, "Towards building safe and secure agentic AI", UC Berkeley Advanced LLM Agents MOOC (Spring 2025): [video](https://www.youtube.com/watch?v=ti6yPE2VPZc), used at [CIA goals and new assets](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=840), [seven-step walkthrough](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=1320), [uses of the output](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=1680), [security levels](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=1920), [misuse](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=2160), [little defense for hybrid systems](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=4560)
- **Lecture:** Dawn Song, "Agentic AI Safety & Security", UC Berkeley Agentic AI MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=CvZDJxd4LKM), used at [hybrid systems](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=240), [classic bugs through model output](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=1560), [calendar example](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=2640), [re-authentication example](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=3000)
- **Lecture:** Dawn Song, "Towards Building Safe & Trustworthy AI Agents and A Path for Science- and Evidence-based AI Policy", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=QAgR4uQ15rc), used at [safety and security](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=120), [four questions and kinds of harm](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=2160)
- **Web:** OWASP Gen AI Security Project, "OWASP Top 10 for LLM Applications 2025": [list](https://genai.owasp.org/llm-top-10/), opened 2026-11-24
- **Web:** OWASP Gen AI Security Project, "OWASP Top 10 For Agentic Applications 2026": [list](https://genai.owasp.org/top-10-for-agentic-applications-2026/), opened 2026-11-24

## Next

→ [Jailbreaks and Prompt Injection](02-jailbreaks-and-prompt-injection.md), for the attack that crosses every boundary drawn here.
