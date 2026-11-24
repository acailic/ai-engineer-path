# 04. Defenses: Guardrails, Detection and Secure Design

**Level:** Practitioner · **Reading time:** 30 min · **Exercise:** 90 min
**Prerequisites:** [Agent-Specific Attacks](03-agent-specific-attacks.md)

> **In one sentence:** After this chapter you can assemble a defense in depth for an agent, filters at the edges, a policy gate on actions, separated privileges, and a person where it matters, and you can say what each layer does not stop.

## Why this matters

Your team adds an input filter that rejects prompts containing "ignore previous instructions". The attack success rate drops. A week later a planted review that says "Kindly disregard the task above and ..." passes the filter, and the agent follows it.

The question of this chapter: which layers exist, what does each one stop, and in what order should you build them?

## The core idea

No single layer holds. Dawn Song's summary in Fall 2025: "there is no one silver bullet" ([82:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=4920)). The answer is **defense in depth**: several layers, arranged so that an attack has to defeat all of them. Her analogy in Spring 2025 is stacked slices of Swiss cheese: each slice has holes, and the holes do not line up ([76:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=4560)). The analogy breaks in one way: holes in cheese are random. An adaptive attacker looks for your holes on purpose and aims at them.

The layers differ in how they can fail.

- **Prompt-level defenses** ask the model to behave. They lower the success rate and nothing more.
- **Learned detectors** are classifiers. They fail on inputs unlike their training data.
- **Architectural controls** are ordinary code. The model cannot talk its way past a check it does not control.

Build from the strong end. A policy gate on tool calls stops an injected instruction whatever wording it used, because it checks the action and not the text.

Song sorts the mechanisms into two families. **Runtime protections** check while the agent runs: input guards, output guards, information flow control, monitoring, and a human in the loop. **Secure by design** changes the architecture: privilege separation and formal verification ([84:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5040), [94:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5640)).

## How it works, step by step

### 1. Filter the input

An **input guard** blocks, filters, sanitizes, or normalizes untrusted input before it reaches the agent. Song names three examples ([84:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5040)):

- Constitutional Classifiers, a classifier that labels an input harmful or harmless.
- DataSentinel, a detector for prompt injection trained with a game-theoretic method (IEEE Security and Privacy 2025).
- PromptArmor, which uses a language model to detect and remove injected instructions.

Her caution: strong models, prompted well, detect and sanitize many malicious inputs, yet there is no foolproof input guard against adaptive attacks ([86:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5160)).

### 2. Spotlight the data

**Spotlighting** marks where untrusted data begins and ends, so that the model can tell it from instructions. <!-- The name "spotlighting" is from general knowledge (Hines et al., 2024); the techniques are on Song's Fall 2024 slide. --> The prompt-level techniques on her Fall 2024 slide, from Liu et al. (2024), are:

- **Delimiters**: enclose the data in markers.
- **Sandwich prevention**: repeat the instruction after the data, so that the nearest text before the answer is yours.
- **Instructional prevention**: rewrite the instruction to say that text inside the markers is data.
- **Paraphrasing** and **retokenization**: rewrite the data, so that exact character sequences such as a closing marker break apart.

Each of these costs tokens and lowers the rate. None of them is a wall, because the attacker can type your marker.

### 3. Use the instruction hierarchy if you have it

The **instruction hierarchy** is a model-level defense: the model is trained to privilege some instructions over others. A system prompt outranks a user message, which outranks text that arrives as data (as described on Song's Fall 2024 slide, which attributes the idea to OpenAI). She describes it as training models to prioritize more privileged instructions ([50:00](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=3000)). You cannot add it with a prompt. Either the provider trained the model that way, or it did not, and your own fine-tuning can weaken it (see [Trustworthiness Beyond Injection](07-trustworthiness-beyond-injection.md)).

### 4. Add a learned detector, and measure it

Two detection ideas from the same slide are cheap to try:

- **Known-answer detection**: add a question with a known answer to the prompt. If the model no longer answers it, something has taken over.
- **Response-based detection**: check that the answer is a valid answer to the task.

A detector is a classifier, so evaluate it as one. The **false positive rate** is the share of legitimate inputs it blocks. The **false negative rate** is the share of attacks it lets through. A false positive costs you a blocked customer. A false negative costs you an incident. Measure both on labeled data before you trust either.

### 5. Validate the output

An **output guard** validates what the agent produces, including tool calls and generated content, against a security policy ([86:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5160)). The basic rule for **improper output handling** is: never pass model output to a shell, a database, or a URL without validation. Use parameterized queries and allowlists for destinations.

### 6. Enforce least privilege on every action

**Least privilege** says that a component gets only the permissions its current task needs. Song's group built **Progent**, a programmable privilege control for agents. Its parts:

- A small language for writing policies.
- A baseline of global, human-written policies that always hold.
- Contextual policies, generated for the current task and updated as the agent's state changes.
- An enforcement component that watches each action and allows or blocks it.

Her example from Fall 2025: for "summarize unread emails", the policy allows only reading. For "send an email to Alice", it allows only sending. Once the agent has looked up Alice's address, the policy narrows again to that one address ([88:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5280), [90:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5400)). An injected instruction can still reach the model, and the allowed actions are too few for it to matter.

In Spring 2025 she reported that adding Progent to an existing agent took about ten lines of change in their experiments, that it lowered the attack success rate while keeping utility, and that manual policies brought the rate to zero on their benchmarks ([98:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=5880)).

### 7. Separate privileges and sandbox

**Privilege separation** splits a system into parts with different permissions. A compromised part cannot borrow the permissions of another. **Sandboxing** is the enforcement: each part runs in a container that the operating system confines.

The idea is older than agents. Song's own work from 2004, Privtrans, splits a program into a privileged **monitor** and an unprivileged **slave**. The slave does the risky work with no privileges. The monitor holds the privileges and exports a narrow interface. For an agent, the pattern is: the model-driven planner has no tools and no secrets. It proposes actions. A small executor, which the model cannot change, checks each proposal and performs it.

In Fall 2025 she described the agent version: instead of one monolithic agent, separate components, each in its own container with its own privileges ([94:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5640)). She also cited a rule of thumb, the **Rule of Two**: in one session, an agent should have at most two of these three properties ([96:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5760), [98:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5880)).

1. It processes untrusted input.
2. It has access to sensitive systems or private data.
3. It can change data or communicate externally.

A component that reads web pages, holds the user's mailbox, and can send mail has all three. Split it until no component does. The rule limits the damage of an attack, and it also limits what the agent can do.

### 8. Put a person before high-impact actions

A **human approval gate** pauses the agent before a critical or high-impact action until a person approves it ([94:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5640)). Three rules keep a gate real:

- The approver sees the actual arguments of the action, not a summary written by the model.
- Few actions need approval. A gate on everything becomes a rubber stamp.
- No answer means no action.

### 9. Track untrusted data

**Information flow control**, also called **taint tracking**, labels data that came from an untrusted source and follows it through the system. Song names two problems: over-tainting, when too much is labeled, and runtime overhead ([92:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5520)).

### What each layer stops

| Layer | Stops | Does not stop | Cost |
|-------|-------|---------------|------|
| Input filter | Known and obvious payloads | Rephrased, hidden, or adaptive payloads | Latency, tokens, blocked legitimate users |
| Spotlighting | Some naive payloads | An attacker who types your marker | Tokens |
| Instruction hierarchy | Attacks the model was trained on | Attacks it was not trained on, or your own fine-tune | None, if the provider trained it |
| Learned detector | Payloads similar to its training data | New payload families | A model call, false positives |
| Output validation | Malformed output, injection into downstream systems | A well-formed harmful action | Small |
| Policy gate on actions | Any action outside the task's privileges | Actions the policy wrongly allows | Writing and testing policies |
| Privilege separation and sandbox | Damage from one compromised component | Misuse of a component's legitimate permissions | Engineering |
| Human approval | High-impact actions nobody approved | Low-impact harm, approver fatigue | People's time |

## Worked example

A policy gate in plain Python: the Progent idea in miniature. It needs no model.

```python
# policy_gate.py: check every tool call against a per-task policy, in code.
from dataclasses import dataclass


@dataclass(frozen=True)
class Call:
    name: str
    args: dict


# Rules per task. Your code derives the task from the request.
POLICIES = {
    "summarize_email": {"read_email": lambda args: True},
    "send_email": {"send_email": lambda args: "@" in args.get("to", "")
                                            and not args.get("attachments")},
}
SENSITIVE_TOOLS = {"pay", "delete_email", "shell"}


def enforce(task: str, call: Call) -> tuple:
    """Allow only what the task's policy permits. Unknown tasks allow nothing."""
    if call.name in SENSITIVE_TOOLS:
        return False, f"{call.name} is sensitive: needs a human approval gate"
    rule = POLICIES.get(task, {}).get(call.name)
    if rule is None:
        return False, f"{call.name} is not permitted for task {task!r}"
    if not rule(call.args):
        return False, f"arguments of {call.name} violate the policy"
    return True, "allowed"


if __name__ == "__main__":
    print(enforce("summarize_email", Call("read_email", {})))
    print(enforce("summarize_email", Call("send_email", {"to": "a@b.c"})))
    print(enforce("summarize_email", Call("pay", {"amount": 200})))
```

The output is `allowed`, then a refusal for the email, then a refusal for the payment. What to observe:

- Every tool call passes through `enforce`. The agent has no other route to a tool.
- The policy is code. Whatever text reaches the model, the worst it can do is produce a call, and the call is checked.
- The default is deny. A task without a policy can do nothing.

## What the practitioners say

Song's defense story grew across three terms, and her caution stayed the same.

- **Fall 2024: a taxonomy and a warning.** She sorted defenses into prompt level (prevention and detection), model level, and system level. Her verdict then: "none of these defenses currently are effective against the new and adaptive attacks", and many degrade model performance ([50:00](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=3000)). She pointed at system-level defenses: application isolation, information flow control, least privilege.
- **Spring 2025: principles.** Defense in depth, least privilege and privilege separation, and secure by design, which she grounded in Saltzer and Schroeder's 1975 principles and the formally verified seL4 kernel ([76:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=4560)). She listed eight mechanism families and closed with open questions: how to give agents identities, how to keep full auditability at a reasonable storage cost, and how to write formal specifications for a component as vague as a model ([106:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=6360)).
- **Fall 2025: more principles and named tools.** She added fail-safe by default, complete mediation (every access is checked), economy of mechanism (keep it small), and open design (secrecy is not a control) ([82:00](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=4920)). She named working input guards, and repeated that none is foolproof.

Her Fall 2024 point about model-level defenses still applies. Hardening the model is the provider's work: data cleaning, safety pre-training, alignment after training, and unlearning ([82:00](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=4920)). Use it. Do not depend on it alone.

## Pitfalls

- **One filter and done.** Every layer fails. Build the next one before you need it.
- **A blocklist of phrases.** "Ignore previous instructions" has a thousand paraphrases. Check actions, not strings.
- **A guard that reads the whole conversation.** A guard built on a language model can be injected too. Give it the untrusted data alone.
- **A policy written only by a model.** Generated policies are useful for one task and wrong in ways you did not predict. Keep a human-written baseline, as Progent does.
- **Approve everything.** A gate that fires on every step trains people to click approve.
- **Blocking without a record.** Log each blocked call with its arguments and the rule it broke, or you cannot investigate or tune.
- **Trusting the provider's safety after your fine-tune.** Re-run your tests on the model you ship.

## Try it

Add a policy gate to an agent you control, and measure what it costs.

1. List the tasks your agent handles. For each, list the tools it needs and the rules on their arguments.
2. Route every tool call through an `enforce` function with a default of deny.
3. Run your injection suite from [Jailbreaks and Prompt Injection](02-jailbreaks-and-prompt-injection.md) before and after the gate.
4. Run twenty benign tasks through the gate and count how many it blocks.

You are done when you have three numbers: the attack success rate before the gate, the rate after it, and the share of benign tasks the gate blocked. Every blocked call must be logged with a reason. Stretch goal: split the agent into a planner without tools and an executor that only runs approved calls, and run the executor in a container.

## Key takeaways

- Defense in depth means several layers whose weaknesses differ. An adaptive attacker aims at the holes, so the analogy with cheese goes only so far.
- Prompt-level defenses and learned detectors lower the attack success rate. Architectural controls in code are what hold.
- Least privilege on actions stops an injected instruction whatever wording it used, because it checks the action and not the text.
- Privilege separation and the Rule of Two limit the damage a compromised component can do, and they also limit the agent.
- Song's caution was the same in every term: no prompt-level or model-level defense holds against adaptive attacks on its own.

## Self-check

1. Why is a policy gate on tool calls stronger than an input filter against a rephrased injection?
2. In Progent, why does the policy for "send an email to Alice" change after the agent reads Alice's address?
3. An agent reads web pages, holds a mailbox, and can send mail. What does the Rule of Two say about it?
4. What are the two error rates of a learned detector, and what does each cost you?
5. Which three properties of a human approval gate keep it from becoming a formality?

<details><summary>Show answers</summary>

1. The gate checks the action that results, not the words that caused it. A rephrased injection still has to produce a tool call, and the call is checked against the policy.
2. Least privilege: once the address is known, the task needs only to send to that one address, so the policy narrows to it.
3. It has all three properties, which the rule forbids. Split it into components such that no component has more than two.
4. The false positive rate, which blocks legitimate users, and the false negative rate, which lets attacks through.
5. The approver sees the real arguments, only a few actions need approval, and no answer means no action.

</details>

## Sources

- **Lecture:** Dawn Song, "Agentic AI Safety & Security", UC Berkeley Agentic AI MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=CvZDJxd4LKM), used at [defense principles](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=4920), [input guards](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5040), [output guards and limits](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5160), [contextual policies](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5280), [taint tracking](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5520), [containers and human in the loop](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5640), [Rule of Two](https://www.youtube.com/watch?v=CvZDJxd4LKM&t=5880)
- **Lecture:** Dawn Song, "Towards building safe and secure agentic AI", UC Berkeley Advanced LLM Agents MOOC (Spring 2025): [video](https://www.youtube.com/watch?v=ti6yPE2VPZc), used at [defense in depth](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=4560), [hardening and input guardrails](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=4920), [Progent results](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=5880), [open questions](https://www.youtube.com/watch?v=ti6yPE2VPZc&t=6360)
- **Lecture:** Dawn Song, "Towards Building Safe & Trustworthy AI Agents and A Path for Science- and Evidence-based AI Policy", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=QAgR4uQ15rc), used at [taxonomy of defenses and its limits](https://www.youtube.com/watch?v=QAgR4uQ15rc&t=3000)
- **Reading:** David Brumley and Dawn Song, "Privtrans: Automatically Partitioning Programs for Privilege Separation" (USENIX Security Symposium 2004)
- **Reading:** Yupei Liu, Yuqi Jia, Runpeng Geng, Jinyuan Jia, and Neil Zhenqiang Gong, "Formalizing and Benchmarking Prompt Injection Attacks and Defenses" (USENIX Security 2024), the source of the defense taxonomy on the Fall 2024 slides
- **Reading:** "Progent: Programmable Privilege Control for LLM Agents" (2025) and "DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks" (IEEE Security and Privacy 2025), as cited on the lecture slides

## Next

→ [Monitoring Agents: The White Agent Approach](05-monitoring-agents-the-white-agent-approach.md), for the layer that watches everything else while it runs.
