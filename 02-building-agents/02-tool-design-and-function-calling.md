# 02. Tool Design and Function Calling

**Level:** Practitioner · **Reading time:** 30 min · **Exercise:** 60 min
**Prerequisites:** [The Anatomy of an Agent](01-the-anatomy-of-an-agent.md) (the loop, observations and the tool registry)

> **In one sentence:** After this chapter you can write a tool whose schema, description and error messages let a model call it correctly, recover from its own mistakes, and stop when it should.

## Why this matters

You give your agent a `get_orders` tool. You ask for yesterday's failed orders. The model calls the tool with `day="yesterday"`. Your code expects `2026-11-23`, the database query crashes, and the tool returns `None`. The model apologizes and says it cannot find any orders. You conclude that the model is bad.

The model was not the problem. The tool never said which date format it wanted, never said what was wrong, and never distinguished "no orders" from "error". Most "the model is dumb" reports in agent projects are tool problems. This chapter is about designing the other half of every tool call.

## The core idea

A tool has three faces:

| Face | Who reads it | What it must do |
|---|---|---|
| Contract: name, description, argument schema | The model, before every decision | Say when to use the tool and how to fill in the arguments |
| Function: the Python code | Nobody in the loop; it just runs | Do one thing and check its inputs |
| Observation: the text returned | The model, right after the call | State the result or state exactly what was wrong |

The model never sees your source code. It sees the contract and the observation. **Function calling** is the name for this arrangement: you send the model a list of tool contracts, and it answers with a **tool call**, a structured request holding a tool name and arguments in JSON, short for JavaScript Object Notation, the bracket-and-quote format that APIs use to exchange data. Your program runs the function and sends the result back.

The contract is a **schema**: a formal description of what valid arguments look like, written in JSON Schema. And the description is not documentation. It is a **prompt** that the model reads again before every decision.

An analogy: you are designing a command-line tool for a new colleague who will never open the manual and never see the code. Where the analogy breaks: a colleague can ask you a question. A model can only try a call and read what comes back. So the error message is the only place you have to explain yourself.

## How it works, step by step

### 1. Write the contract for the decision

For each tool, answer five questions in the description:

1. What does it do, in one sentence?
2. When should it be used?
3. When should it *not* be used, and what should be used instead?
4. What format and units does each argument take?
5. What does the result look like, including its limits?

Here is a contract for the order tool. The exact key names differ between providers (as of November 2026), so treat the outer shape as illustrative pseudocode and check your provider's documentation. The JSON Schema inside is standard.
```python
STATUSES = ("pending", "paid", "failed", "refunded")

GET_ORDERS = {
    "name": "get_orders",
    "description": (
        "List orders created on one calendar day (UTC). "
        "Returns the total count and at most 50 orders, newest first. "
        "Do not use it to find one order: use get_order for that."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "day": {
                "type": "string",
                "description": "Calendar day in UTC, formatted YYYY-MM-DD. Example: 2026-11-23.",
            },
            "status": {
                "type": "string",
                "enum": list(STATUSES),
                "description": "Optional. Omit to get orders in every status.",
            },
        },
        "required": ["day"],
        "additionalProperties": False,
    },
}
```

Rules that keep schemas easy to call:

- **Few parameters.** Two or three. If a tool needs eight, it is probably two tools.
- **Enums over free text.** `"enum"` turns a status into a closed list the model cannot misspell.
- **Formats the model knows.** ISO dates (`YYYY-MM-DD`), ISO country codes, lowercase currency codes.
- **Units in the description.** "Amount in cents" prevents a class of silent errors.
- **Nothing the model cannot know.** If an argument needs an internal ID, add a search tool that returns IDs.

### 2. Check inputs in the function

The schema tells the model what to send. It does not guarantee what arrives. Check again in code, and raise an error that names the fix.

```python
from datetime import date

def get_orders(day: str, status: str = None) -> str:
    """Return text for the model. Raise ValueError for anything the model can fix."""
    try:
        date.fromisoformat(day)
    except ValueError:
        raise ValueError(
            f"'day' must be YYYY-MM-DD, got {day!r}. Example: 2026-11-23.")
    if status is not None and status not in STATUSES:
        raise ValueError(
            f"Unknown status {status!r}. Choose one of: {', '.join(STATUSES)}.")
    # ... the real query goes here ...
    return f"0 orders found for day={day}, status={status or 'all'}"
```

Note the last line. When a query returns nothing, the tool says so in words. An empty string could mean "nothing found", "error" or "not implemented".

### 3. Return errors the model can act on

Every observation should answer three questions: what happened, what was wrong, and what is allowed. Compare:

| Situation | Unhelpful observation | Useful observation |
|---|---|---|
| `day="yesterday"` | `None`, or a 12-line traceback | `Error: 'day' must be YYYY-MM-DD, got 'yesterday'. Example: 2026-11-23.` |
| No orders that day | `""` | `0 orders found for day=2026-11-23, status=all` |
| 5,000 failed orders | 5,000 rows in the context | `Total: 5,000. First 50 shown: ... Narrow the day or filter by status.` |
| Service rate-limited | `Error: something went wrong` | (the program retries; then) `Error: service unavailable after 3 attempts. Try again later.` |

A **stack trace** is for you. It goes to your logs. The model gets one sentence.

### 4. Sort errors by who can fix them

| Error class | Examples | Who fixes it | What the program does |
|---|---|---|---|
| Model-fixable | Bad argument, unknown ID, file not found | The model, by changing the call | Returns `Error: ...` with the allowed values |
| Transient | Timeout, rate limit, service unavailable | Nobody: wait | Retries with **backoff**, a wait that grows between attempts, up to a cap |
| Fatal | Missing API key, a bug in the tool, no permission at all | The developer | Stops the run with an exception |

### 5. Retry on purpose

There are two kinds of retry, and newcomers mix them up.

- **Program retries** handle transient errors. Cap them (three is common), grow the wait between attempts, and give up with an observation the model can understand.
- **Model retries** happen when the model reads `Error: ...` and tries a different call. Cap them too: count attempts per task, or a model can loop on the same mistake until the budget is gone.

Never let the program retry a tool with side effects unless you know the first call did nothing. Sending an email twice is worse than failing once. Make such tools **idempotent**, meaning that calling them twice has the same effect as calling them once, for example by passing an ID that the server uses to drop duplicates.

## What the practitioners say

**Graham Neubig (Fall 2024)** builds coding agents, and coding agents live or die by their tools.

- **Actions can be code.** Traditional agents call one tool and get one result per step. CodeAct, he explains, acts by writing code that can run shell or notebook commands ([22:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1320)). His example: to find the cheapest country to buy one phone model, a tool-calling agent may need some 15 API calls, one per lookup, where CodeAct writes a single loop over the countries. A failed loop still returns an error, so the model gets feedback, but at a coarser step. He reports that the original work found faster resolution and a higher success rate than direct tool use ([24:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1440)). His own platform OpenHands combines this with the editing commands of SWE-agent: every action is a call to code, so ten search hits can be edited by one loop ([28:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1680)).
- **Finding where to act is a tool problem.** He says file localization, finding the right files for a request, "might even be the biggest problem in coding agents nowadays" ([38:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2280)). One fix is a search tool, as in SWE-agent, but search alone is "not like the equivalent to going in and opening all the cabinets before you start" ([42:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2520)). Two other designs: Aider builds a tree-shaped map of the repository up front, and Agentless runs a search that narrows from the whole repository down to files and then functions ([42:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2520)).
- **Context assembly is part of the tool.** He cites a write-up of how GitHub Copilot builds its prompt: text before and after the cursor, the 20 most recently used files in the same language, imported files, path and language metadata. In his view agents had not yet invested as much in this kind of prompt engineering ([38:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2280)).
- **Fix from error messages.** One of his slides lists repairing code based on error messages as a recovery method, citing InterCode (slide 45, [50:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=3000)). That only works if the error reaches the model in a form it can use.

**Yangqing Jia (Fall 2025)** comes from infrastructure and makes a narrower point. Asked about orchestration, he names retrieval-augmented generation and "accurate data processing pipelines" as what matters ([68:00](https://www.youtube.com/watch?v=xqRAS6rAouo&t=4080)). A tool is only as good as the pipeline behind it.

### Lessons from agent-computer interface research

The SWE-agent paper gave the design of an agent's tools a name: the **agent-computer interface**, or ACI. It argues that the commands an agent uses to view, search and edit files matter as much as the model. The interface they built includes:

- A file viewer that shows line numbers and at most 100 lines per call, so edits can quote exact lines and long files do not flood the context.
- Search commands with a capped number of results.
- An edit command that refuses to touch a file the agent has not viewed, and that runs a syntax check after each edit and undoes the edit if the check fails.
- A guard that interrupts the agent when it repeats the same action, and a history that drops the text of old file views.

Neubig walks through the same idea in his lecture ([26:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1560)). SWE-agent gives the model a set of commands designed to be friendly to it and returns feedback in the same style. A command that shows a file around one line returns a window of lines, not the whole file, so a file of thousands of lines can be read without spending the whole context; an edit command then replaces a range of lines ([28:00](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1680)).

The paper reports that GPT-4 Turbo with this interface solved 12.5% of SWE-bench, a benchmark of real GitHub issues, and that removing the line limit, the search tools or the syntax check each lowered the result sharply.

An ACI is like a CLI with one difference that changes everything: a person reads the manual once and learns; a model rereads the tool description on every turn and learns nothing between calls.

## Pitfalls

1. **Vague descriptions.** "Gets data" gives the model nothing to decide with. Fix: state when to use it, when not to, and the formats.
2. **Free text where a list would do.** Fix: use `enum` for closed sets and documented formats for dates and codes.
3. **Returning empty or `None` on failure.** The model reads it as success. Fix: say `0 results` or `Error: ...` in words.
4. **Dumping whole results into the context.** Fix: return counts and a bounded page, and tell the model how to narrow.
5. **Dozens of tools.** With many similar tools the model picks the wrong one. Fix: keep the list short, merge near-duplicates, and describe each tool's boundary.
6. **Retrying side effects.** Fix: retry only transient errors, and make side-effecting tools idempotent.
7. **Trusting tool output.** Text returned by a tool can contain anything, including instructions written by a third party. Fix: treat observations as data, never as commands ([prompt injection](../04-safety-and-security/02-jailbreaks-and-prompt-injection.md)).

## Try it

Design three tools for an agent that answers questions about a folder of meeting notes: one that lists files, one that searches them, one that reads a page of a file.

1. Write the contract of each tool: description, parameters, formats, limits.
2. Write the functions so that every wrong input raises a one-sentence error naming an allowed value.
3. Write contract tests: call each tool with a missing argument, a wrong format and an unknown name, and assert the observation starts with `Error:` and contains one allowed example.
4. Write one test for the empty case and assert the result states the count zero.

**Deliverable:** the three tools, the tests, and a short table of every error each tool can return and who fixes it.

**You are done when:** the tests pass offline; no tool returns an empty string or `None`; no observation is longer than 2,000 characters; and each description says when *not* to use the tool.

**Stretch goal:** give the tools to a real model with ten questions and log every call. Count how many errors the model repaired on its next step. That log is your first [evaluation](../03-evaluation/02-a-minimal-eval-harness.md) of tool design.

## Key takeaways

- The model sees only the contract and the observation. Design both as prompts.
- A description says what the tool does, when to use it, when not to, and the format of every argument.
- Errors are sorted by who can fix them: the model, time, or the developer.
- An error message is a prompt: say what was wrong and what is allowed.
- Program retries are for transient errors only, and never for side effects unless the tool is idempotent.
- The interface between the agent and the computer can matter as much as the model.

## Self-check

1. A tool returns an empty string when a query finds nothing. Why is that a problem, and what should it return instead?
2. A tool call fails with a timeout. Who fixes this class of error, and what does the program do?
3. Name three things a tool description should state beyond what the tool does.
4. Why must the program avoid retrying `send_email` after a timeout?
5. In the SWE-agent interface, why does the edit command refuse a file the agent has not viewed?
6. What is the difference between a program retry and a model retry?

<details><summary>Show answers</summary>

1. The model cannot tell "no results" from "failed" or "not implemented", so it may guess. It should return a sentence that states the count, such as `0 results for query X`.
2. Nobody changes code for it; it is transient. The program waits and retries with growing waits up to a cap, then returns an observation saying the service is unavailable.
3. Any three of: when to use it; when not to use it and what to use instead; the format and units of each argument; what the result looks like, including limits.
4. The first call may have sent the email before the timeout. A blind retry can send it twice. Make the tool idempotent or confirm the first call's outcome first.
5. So that the edit quotes line numbers from text the model has actually seen, instead of numbers it invented. The refusal is an error message that tells the model what to do first.
6. A program retry repeats the same call automatically after a transient error. A model retry is the model choosing a different call after reading an error observation.

</details>

## Sources

- **Lecture:** Graham Neubig, "Agents for Software Development", UC Berkeley LLM Agents MOOC (Fall 2024): [video](https://www.youtube.com/watch?v=f9L9Fkq-8K4), used at [acting through code](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1320), [CodeAct's loop example](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1440), [file localization and context assembly](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2280), [search tools and repository maps](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=2520), [agent-friendly commands](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=1560), [fixing from error messages](https://www.youtube.com/watch?v=f9L9Fkq-8K4&t=3000)
- **Lecture:** Yangqing Jia, "Evolution of System Designs from an AI Engineer Perspective", UC Berkeley Agentic AI MOOC (Fall 2025): [video](https://www.youtube.com/watch?v=xqRAS6rAouo), used at [accurate data pipelines](https://www.youtube.com/watch?v=xqRAS6rAouo&t=4080)
- **Reading:** John Yang, Carlos E. Jimenez, et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering" (2024): [link](https://arxiv.org/abs/2405.15793)
- **Reading:** Xingyao Wang, Yangqiao Song, et al., "Executable Code Actions Elicit Better LLM Agents" (2024): [link](https://arxiv.org/abs/2402.01030)
## Next

→ [03. Planning, Search and Decision-Making](03-planning-search-and-decision-making.md), because once an agent can act, the next question is how it decides what to do next.
