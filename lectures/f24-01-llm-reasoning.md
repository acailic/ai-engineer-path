# Lecture guide: LLM Reasoning

**Lecturer:** Denny Zhou (Google DeepMind) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 1 · **Length:** 1:04:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=QL-FS_Zcmyo) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/llm-reasoning.pdf)
**Chapters that cite this lecture:** [04. Using LLMs: Tokens, Context and Sampling](../01-foundations/04-using-llms-tokens-context-and-sampling.md) · [05. Prompting and In-Context Learning](../01-foundations/05-prompting-and-in-context-learning.md) · [06. Reasoning in LLMs: From Chain-of-Thought to Search](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) · [08. A Short History of LLM Agents](../01-foundations/08-a-short-history-of-llm-agents.md)

> **In one sentence:** Denny Zhou shows why written-out intermediate steps make a large language model reason, how to elicit them and where they fail, for engineers who want to know when to trust chain-of-thought.

## Before you watch

Read [05. Prompting and In-Context Learning › Start with zero-shot](../01-foundations/05-prompting-and-in-context-learning.md#1-start-with-zero-shot) and [06. Reasoning in LLMs: From Chain-of-Thought to Search › The core idea](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#the-core-idea) first. The lecturer explains that a large language model is a transformer trained to predict the next word, and leans on basic machine-learning notions, such as argmax probability, for self-consistency.

## The lecture, part by part

### [0:00–2:10](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=0) Introduction

The course instructor introduces the team and sets out the subject: LLM agents, in which the model reasons and plans while the system observes, acts and calls tools.
**In this book:** [08. A Short History of LLM Agents › The definition this repository uses](../01-foundations/08-a-short-history-of-llm-agents.md#the-definition-this-repository-uses).

### [2:10–3:31](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=130) Agent capabilities

Such agents are flexible: with little specific training they handle the web, robots and multimodal input.
**In this book:** not needed (course introduction).

### [3:31–3:53](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=211) Multi-agent collaboration

Agents also collaborate with other agents, humans included, on harder tasks.
**In this book:** not needed (course introduction).

### [3:53–4:54](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=233) Why agent frameworks

Real tasks take trial and error, tools and retrieval extend the model, and a workflow permits task decomposition, with subtasks given to specialized modules.
**In this book:** not needed (course introduction).

### [4:54–5:12](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=294) Applications

Agents already work in education, law, finance, healthcare and cybersecurity, and leaderboards improve fast.
**In this book:** not needed (course introduction).

### [5:12–5:19](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=312) Deployment challenges

Despite that fast progress, a number of key challenges still stand in the way of deployment.
**In this book:** not needed (course introduction).

### [5:19–5:34](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=319) Reasoning and planning

The instructor's first open problem is reasoning and planning: agents still go wrong on complex tasks.
**In this book:** not needed (course introduction).

### [5:34–8:59](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=334) Challenges, syllabus and guest speakers

Further challenges (feedback, continual learning, safety, human–agent interaction) shape the syllabus: model capabilities, agent frameworks, applications, and safety and ethics, taught with a team of guest speakers.
**In this book:** not needed (course introduction).

### [8:59–19:27](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=539) Few-shot prompting

Before his talk, the lecturer asks what the room expects from AI: unsolved mathematics, new scientific theories. Machine learning lacked reasoning, he concluded. Take last-letter concatenation (Elon Musk gives NK): a transformer trained on a large labeled set stalls near 85–90%, while a person needs only one or two examples. Few-shot prompting, solved examples joined with the test item, fails too; one example spelling out the steps gives 100%.
**In this book:** [05. Prompting and In-Context Learning › Add exemplars when format or judgment is off](../01-foundations/05-prompting-and-in-context-learning.md#2-add-exemplars-when-format-or-judgment-is-off).

### [19:27–21:26](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=1167) Earlier work

Machine learning still matters, he cautions; intermediate steps are an old idea. A 2017 paper by Ling and colleagues solved math word problems with natural-language rationales and a simple sequence-to-sequence model trained from scratch. In 2021 Cobbe and colleagues published GSM8K, a dataset of grade-school math problems, each with intermediate steps and a final answer, and used it to fine-tune a large model.
**In this book:** nothing beyond this guide.

### [21:26–21:59](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=1286) Program synthesis

In 2021 a group at Google found the idea independently, in program synthesis. Their paper, Show Your Work, introduced scratchpads: before giving a result, the model writes out each intermediate computation, using abstract symbols instead of sentences. By then the same recipe existed in two forms, words for math problems and symbols for code, with the steps part of the training data in both.
**In this book:** nothing beyond this guide.

### [21:59–24:39](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=1319) Intermediate steps

Chain-of-thought prompting (Jason Wei, Quoc Le and colleagues) tested prompting with intermediate steps across NLP tasks. Whatever the mechanism, examples with intermediate steps make a model answer with them.
**In this book:** [06. Reasoning in LLMs: From Chain-of-Thought to Search › The core idea](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#the-core-idea).

### [24:39–25:06](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=1479) Task decomposition

Following a classic book on problem solving, he presents least-to-most prompting as a strategy the examples can carry: show the model how to split a problem into simpler sub-problems and solve them one after another, generalizing from easy to hard. Example: Elsa has three apples, Anna has two more than Elsa; answer how many Anna has (five), then how many both have together (eight).
**In this book:** nothing beyond this guide.

### [25:06–34:13](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=1506) Serial problems

Least-to-most prompting reaches 99.7% on a compositional generalization task with 0.1% of the demonstration examples. His 2024 result shows why: a transformer that writes intermediate steps solves any serial problem at constant depth, however long the input, provided the steps are long enough; one answering directly needs enormous depth or fails. Asking for step-by-step thinking without examples also works, but is usually significantly worse than few-shot prompting.
**In this book:** [05. Prompting and In-Context Learning › Ask for reasoning on multi-step tasks](../01-foundations/05-prompting-and-in-context-learning.md#3-ask-for-reasoning-on-multi-step-tasks).

### [34:13–34:50](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=2053) Analogical reasoning

Returning to a classic book on problem solving, he asks whether a related problem is known: LLMs as analogical reasoners recall a relevant problem and its solution before solving the new one.
**In this book:** [05. Prompting and In-Context Learning › Let the model supply the examples](../01-foundations/05-prompting-and-in-context-learning.md#4-let-the-model-supply-the-examples).

### [34:50–47:20](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=2090) Reasoning without prompts

Self-generated analogies beat the zero-shot step-by-step instruction and hand-written chain-of-thought prompts. In chain-of-thought reasoning without prompting, the decoder continues greedily from each of the top few first tokens; step-by-step paths appear by themselves. In the Nicolas Cage birth-year example, such a path is far more probable than the direct answer. He then raises a concern: decoding favors the most probable reasoning path, while the goal is the most probable answer, whose probability sums over every path leading to it.
**In this book:** [06. Reasoning in LLMs: From Chain-of-Thought to Search › Search: branch at each step](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#3-search-branch-at-each-step).

### [47:20–47:51](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=2840) Self-consistency

Self-consistency estimates that sum by sampling: sample several chains and count final answers, not reasoning paths. By his account it crushed the state of the art of the time.
**In this book:** [06. Reasoning in LLMs: From Chain-of-Thought to Search › Self-consistency: sample, then vote](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#1-self-consistency-sample-then-vote).

### [47:51–1:04:00](https://www.youtube.com/watch?v=QL-FS_Zcmyo&t=2871) Limitations and conclusion

Universal self-consistency handles free-form answers. An irrelevant added sentence derails a solution, and trivia padding hurts every model. A review step fixes wrong answers but overturns right ones, so benchmarks show no gain; published gains relied on an oracle, and a debate yielding nine responses did not beat self-consistency on nine samples. Moving one sentence within GSM8K problems costs about ten points; shuffled rules cause a significant drop in accuracy on a logical inference task.
**In this book:** [06. Reasoning in LLMs: From Chain-of-Thought to Search › Why "review your answer" often hurts](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#2-why-review-your-answer-often-hurts) · [06. Reasoning in LLMs: From Chain-of-Thought to Search › Ordering effects](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#4-ordering-effects).

## What to take away

- Intermediate steps, not the recipe that delivers them, make a model reason.
- Decode for the most probable answer: sample several chains and vote.
- A single run is fragile: irrelevant sentences, self-review without an oracle and premise order all move the result.

## Sources

- Denny Zhou, "LLM Reasoning", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=QL-FS_Zcmyo).
