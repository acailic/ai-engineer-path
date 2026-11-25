# Lecture guide: Multimodal Autonomous AI Agents

**Lecturer:** Ruslan Salakhutdinov (CMU / Meta) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 6 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=RPINOYM12RU) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/ruslan-multimodal.pdf)
**Chapters that cite this lecture:** [01. Multimodal Agents: Web and Computer Use](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Ruslan Salakhutdinov explains why agents that act on web pages still fail, through a benchmark of visual tasks (VisualWebArena), search at inference time that recovers from wrong clicks, and a pipeline that manufactures training tasks on the real web.

## Before you watch

Read [Multimodal Agents: Web and Computer Use](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) first; its first five steps and its section on Salakhutdinov cover most of the lecture. The lecture assumes you have met reinforcement learning terms such as state, action and value.

## The lecture, part by part

### [0:00–2:13](https://www.youtube.com/watch?v=RPINOYM12RU&t=0) Why agents, beyond chat

Language models already answer questions well. The next step is systems that do laborious computer and web tasks: setting up a cloud machine, turning a paper into slides, working a spreadsheet. The lecture covers web agents: how to evaluate them, how to search at inference time, and how to get training data.
**In this book:** [Multimodal Agents › Why this matters](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#why-this-matters).

### [2:13–5:21](https://www.youtube.com/watch?v=RPINOYM12RU&t=133) Two demonstrations, honestly labelled

An agent finds a well-reviewed Thai restaurant in Pittsburgh and books a table for the earliest date, then stops because a confirmation code is needed; another finds a shirt like the one in a photo. The lecturer calls these heavily cherry-picked: in about 30 attempts one succeeded. Each attempt shows the same three parts, a task, a chain of reasoning and one action at a time. A commercial agent of early 2025 points the same way, in his view, and the lecture then turns to measuring how far the research systems still are from that goal.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › Why this matters](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#why-this-matters).

### [5:21–8:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=321) WebArena and why HTML alone is not enough

WebArena is a self-hosted copy of shopping, forum and code-hosting sites. People solve about 78% of its tasks, the language models of the time about 14%. Its tasks use the page source only, and source is messy: interactive elements do not render in it, a page can fill 100,000 tokens, and it carries no spatial layout. VisualWebArena adds visual grounding.
**In this book:** [Multimodal Agents › Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#ruslan-salakhutdinov-march-2025-the-gap-the-failures-the-fixes).

### [8:00–11:48](https://www.youtube.com/watch?v=RPINOYM12RU&t=480) VisualWebArena's tasks

The environment is a simulator with the same three site types. Tasks need sight: find the exact bicycle listed at a high price and offer ten dollars less in a comment; buy the cheapest colour photo printer and ship it to the address in a photo that is upside down; read a chart to learn which region produced most sugarcane in 2021, then look up that region's gross domestic product on another site.
**In this book:** [Multimodal Agents › Benchmarks to know](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#benchmarks-to-know).

### [11:48–17:15](https://www.youtube.com/watch?v=RPINOYM12RU&t=708) The environment and how it scores

The environment is a partially observable decision process: observations (page source, a screenshot, or the accessibility tree, a cleaned-up source), actions (click, hover, type, open, focus or close a tab, go to an address, back, forward, scroll, stop with an answer), deterministic transitions and a sparse reward for success. Buying the printer takes a long chain: find the category, sort by price, pick, add to the cart, check out, fill in the form, order. There are about 950 tasks; roughly 15% are easy, and tasks are rated separately for visual and reasoning difficulty, so one can tell which ability is missing. Scoring is by execution: a final state is checked by verifiers for an exact answer, a yes-or-no visual question, or a number inside a range.
**In this book:** [Multimodal Agents › 4. Score by execution](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#4-score-by-execution).

### [17:15–20:19](https://www.youtube.com/watch?v=RPINOYM12RU&t=1035) What the agent sees

Raw source is cluttered. Set-of-Mark draws a box with an ID around each clickable element, so the agent acts by naming an ID, but it is cluttered too. A third choice is to predict coordinates. The lecturer expects a combination. The loop: goal and observation go to a multimodal model, which writes its reasoning and ends with one action.
**In this book:** [Multimodal Agents › 1. Choose what the agent sees](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#1-choose-what-the-agent-sees).

### [20:19–24:44](https://www.youtube.com/watch?v=RPINOYM12RU&t=1219) How far models are from people

Text alone reaches about 9% of the tasks; adding captions of the images, then a multimodal model, then Set-of-Mark, brings the best of 2024 to about 18%, while students at CMU reached 85 to 86%. People fail in silly ways: they compare two bicycles and stop, or fill the cart and forget to order, which counts as failure. Newer models score higher each year; a model of 2025 reached about 90% on WebArena but the best remain near 20% on the visual tasks.
**In this book:** [Multimodal Agents › Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#ruslan-salakhutdinov-march-2025-the-gap-the-failures-the-fixes).

### [24:44–30:22](https://www.youtube.com/watch?v=RPINOYM12RU&t=1484) Architecture and failure modes

An agent observes, parses, forms a high-level plan and executes low-level actions, refining the plan until it stops. Hierarchical designs plan a few steps ahead (go to a category, sort, choose an item under a price, buy it) and expand each into clicks. The tasks were made simple on purpose and carry little economic value; the open question is whether valuable tasks can be automated. Failures: oscillating between two pages, no memory of what was done, completing a subtask and undoing it, giving up early, clicking the wrong element, and weak spatial reading such as "the first row". The needs: long-horizon planning, search by running several instances, asking a person when unsure, stronger vision-language models, and the right level of abstraction, whether screenshots, source or an API.
**In this book:** [Multimodal Agents › Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#ruslan-salakhutdinov-march-2025-the-gap-the-failures-the-fixes).

### [30:22–34:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=1822) Errors compound; sample again

A model right 90% of the time per step succeeds on about 4% of 30-step tasks. A click at one point changes everything after it, and typing makes the action space huge. The simplest remedy is search by repeated sampling: run the agent to its stop, check the result with a verifier, and run again if it failed. It is inefficient, yet the lecturer notes that reasoning models train on the same idea with thinking tokens. Success within ten samples rises with the number of samples.
**In this book:** [Multimodal Agents › 5. Spend more compute after a failure](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#5-spend-more-compute-after-a-failure).

### [34:00–44:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=2040) Tree search guided by a value function

To explore an exponential space with direction, a value function scores each intermediate state with its probability of success. The method is best-first search with three ingredients: the base agent proposes its most likely actions; the environment can be reset to an earlier state; and a value function, here a large model acting as judge on the whole trace, with self-consistency. The search follows an action, sees the value drop, backtracks and tries the next. It improves results on both benchmarks; more expansions help, and so does choosing depth against breadth. A good value function matters as much as the base policy, and judging a trace is easier than choosing the next click. Future models will have trained value functions.
**In this book:** [Multimodal Agents › 5. Spend more compute after a failure](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#5-spend-more-compute-after-a-failure).

### [44:00–48:06](https://www.youtube.com/watch?v=RPINOYM12RU&t=2640) The limits of search

Backtracking here replays the recorded actions from the start, which is slow. On the real web some actions are destructive: an order cannot be unmade, and an airline blocks or re-prices a flood of bookings, so agents cannot learn by trying there. Search can also improve the policy itself: the traces it finds become training data for supervised fine-tuning or reinforcement learning, and a value function can be fine-tuned instead of prompted with Monte Carlo rollouts. Better base models and more efficient search are both needed.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › 5. Spend more compute after a failure](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#5-spend-more-compute-after-a-failure).

### [48:06–56:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=2886) The data problem and a pipeline that makes tasks

Language models train on text scraped from the web; a task with its full sequence of actions cannot be scraped, and companies pay for it in-house. The team's pipeline uses open Llama models for every step. First, a model reads a real site and proposes realistic tasks a user could finish in one session, restricted to tasks that do not change the site's state. Starting from about a million sites, most tasks are information seeking and many need several steps: fonts suited to a children's book, the meaning of an ancient symbol, the newest fabric designs of a small studio.
**In this book:** [Multimodal Agents › Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#ruslan-salakhutdinov-march-2025-the-gap-the-failures-the-fixes).

### [56:00–64:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=3360) Verifying success with a model as judge

A model then executes the task, and another pass judges from the action sequence and the last page whether it succeeded, with a confidence from 0 to 1. Of 150,000 tasks about 15% were judged successes, some 22,000. Against human checks the judge was right about 85 to 90% of the time when it said yes. In one example the agent looks up invasive plants native to North America, first clicks the wrong link, recovers, and answers with the first 165 species of a sorted list.
**In this book:** [Multimodal Agents › Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#ruslan-salakhutdinov-march-2025-the-gap-the-failures-the-fixes).

### [64:00–68:04](https://www.youtube.com/watch?v=RPINOYM12RU&t=3840) Collecting at scale

The top million pages were filtered to about 150,000 live sites, dropping harmful ones with about 97% detection. About 89% of generated tasks were feasible, and completion was judged with 82% accuracy. Training on synthetic and human data together scaled better than human data alone and raised step accuracy. Human annotation concentrates on popular sites; synthetic tasks help most on the tail. Some 385 million domains remain, and the procedure could run as reinforcement learning at internet scale, with care because the real web cannot be reset.
**In this book:** [Multimodal Agents › Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#ruslan-salakhutdinov-march-2025-the-gap-the-failures-the-fixes).

### [68:04–74:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=4084) The same design in a robot

The recipe transfers to physical agents: observe an image with depth, segment the scene, plan at a high level, act at a low level. In the lab's system a language model writes the plan, a sequencing module grounds each step with segmentation, inverse kinematics and a motion planner, and a small policy learned by reinforcement learning executes the motion. It solved about 25 long-horizon tasks across four benchmarks with about 85% success and transferred to a real robot and unseen objects at 80 to 90%.
**In this book:** nothing beyond this guide; nearest: [Multimodal Agents › What this means for someone building agents](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#what-this-means-for-someone-building-agents).

### [74:00–1:18:00](https://www.youtube.com/watch?v=RPINOYM12RU&t=4440) Robustness and safety

An agent that books the right flight 80% of the time is unacceptable; asking for clarification is a missing skill. Agents are also brittle: an image altered so that its caption becomes an instruction made the agent post flattering comments on a product page. The lecturer retells two reports about a computer-use agent that stopped a long screen recording and left a coding demo to browse photos of Yellowstone; one wrong action without search to recover explains them.
**In this book:** [Multimodal Agents › Ruslan Salakhutdinov (March 2025): the gap, the failures, the fixes](../06-frontier-applications/01-multimodal-agents-web-and-computer-use.md#ruslan-salakhutdinov-march-2025-the-gap-the-failures-the-fixes).

## What to take away

- On visual web tasks the best models of 2024 solved under a fifth; people solved almost all, and execution-based verifiers make the gap measurable.
- Errors compound over a long task; sampling again, then tree search with a value function, recovers some of the loss.
- Training data for agents does not exist on the web; models can propose, execute and verify tasks on real sites without changing them.
- Reliability and robustness to altered pages are the open problems before agents handle anything valuable.

## Sources

- Ruslan Salakhutdinov, "Multimodal Autonomous AI Agents", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=RPINOYM12RU).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25>.
