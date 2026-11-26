# Lecture guide: On Reasoning, Memory, and Planning of Language Agents

**Lecturer:** Yu Su (Ohio State University) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 3 · **Length:** 1:34:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=zvI4UN2_i-w) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/language_agents_YuSu_Berkeley.pdf)
**Chapters that cite this lecture:** [03. Planning, Search and Decision-Making](../02-building-agents/03-planning-search-and-decision-making.md) · [04. Memory and Knowledge for Agents](../02-building-agents/04-memory-and-knowledge-for-agents.md) · [08. Training Models for Agentic Tasks](../02-building-agents/08-training-models-for-agentic-tasks.md)

> **In one sentence:** Yu Su treats language agents as the newest generation of a classic AI problem and surveys long-term memory, implicit reasoning and model-based planning, for engineers who want the research picture.

## Before you watch

Start with [04. Memory and Knowledge for Agents › The core idea](../02-building-agents/04-memory-and-knowledge-for-agents.md#the-core-idea) and [03. Planning, Search and Decision-Making › The core idea](../02-building-agents/03-planning-search-and-decision-making.md#the-core-idea): the talk assumes retrieval-augmented generation and a planning loop. Transformers and weight decay are taken for granted.

## The lecture, part by part

### [0:00–2:16](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=0) Introduction to agents

Yu Su opens with the hype around agents and the skeptics' reply: thin wrappers with nothing fundamental in them, and autoregressive LLMs that can never truly reason or plan. Auto-GPT, hugely popular yet a prototype, is his cautionary tale; agents are an old AI topic.
**In this book:** not needed (course introduction).

### [2:16–5:13](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=136) Defining modern language agents

The usual definition, a language model connected to an external environment, leaves out self-reflection and multi-agent simulation. Yu Su prefers an agent-first stance: classic AI agents, newly upgraded by a language model, still face perceiving an environment, modeling its state and planning, not LM-first scaffolding.
**In this book:** [06. How Agent System Designs Evolve › A short history](../02-building-agents/06-how-agent-system-designs-evolve.md#a-short-history).

### [5:13–8:56](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=313) Reasoning in language agents

Language as communication brings instruction following and in-context learning; language as reasoning is the rarer gift. A model that first answers no, then yes, is spending an adaptive amount of compute on that problem; in an agent, thinking exists to act better. Adding one action type, generating reasoning tokens, and one internal environment, an inner monologue, reconciles the new agents with the classic picture; self-reflection becomes a meta-level reasoning step.
**In this book:** [03. Planning, Search and Decision-Making › The core idea](../02-building-agents/03-planning-search-and-decision-making.md#the-core-idea).

### [8:56–12:34](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=536) Why call it reasoning, and why language agents

One mechanism, token generation, blends perception-like, intuitive and symbolic steps, as in a model's description of an image, which justifies the word reasoning. Of the many names in use, the one he prefers for this generation is language agents: language is their most salient trait, in multimodal agents it still does the heavy lifting, and that command of language need not come from a language model, which may be a means to an end.
**In this book:** [The Anatomy of an Agent › What the practitioners say](../02-building-agents/01-the-anatomy-of-an-agent.md#what-the-practitioners-say).

### [12:34–16:51](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=754) Core competencies framework

Language agents, he argues, continue a long line of agent designs; a multimodal language model is the first to unify several senses in one representation, making them highly expressive and adaptive, with fuzzy, semi-explicit reasoning. His map of the field stacks core competencies in a loose hierarchy: perception, memory and embodiment at the bottom, reasoning, world models and planning above, plus cross-cutting concerns such as safety and evaluation.
**In this book:** [The Anatomy of an Agent › What the practitioners say](../02-building-agents/01-the-anatomy-of-an-agent.md#what-the-practitioners-say).

### [16:51–25:25](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=1011) Modeling long-term memory

Animals learn continuously; neural networks cannot, because new knowledge disturbs old: editing one fact moves unrelated facts while statements that should flip stay put. The workaround is non-parametric memory, experiences kept outside the weights and retrieved, which works because models proved highly receptive to retrieved context even when it contradicts their parameters.
**In this book:** [04. Memory and Knowledge for Agents › The core idea](../02-building-agents/04-memory-and-knowledge-for-agents.md#the-core-idea).

### [25:25–42:04](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=1525) HippoRAG and retrieval advancements

Asked which professor studies Alzheimer's, embedding retrieval scores every passage holding half the answer alike. HippoRAG mimics the hippocampal-indexing theory of memory: a structured index links dispersed memories, so whole memories resurface from partial cues. Offline, a language model extracts triples into a schema-less knowledge graph; online, query entities seed a random-walk ranking that favors the node joined to both cues, the professor Thomas. HippoRAG beat dense and iterative retrieval on three multi-hop question-answering sets; a second version, he says, matches the best embedding models.
**In this book:** [04. Memory and Knowledge for Agents › D. Retrieval that follows associations](../02-building-agents/04-memory-and-knowledge-for-agents.md#d-retrieval-that-follows-associations).

### [42:04–59:51](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=2524) Implicit reasoning in Transformers

The Grokked Transformers paper asks whether a model can compose two memorized facts, a wife and her birth year, in one forward pass, without chain of thought. A plain decoder-only Transformer trains on a synthetic graph (200 relations) of atomic and composed facts, tested in-distribution and out-of-distribution (atomic facts seen but never composed). Implicit reasoning is learned only through grokking: training accuracy hits 100% at about 10,000 steps, test accuracy only after roughly 20 times more. Composition never generalizes out of distribution, comparison does; speed tracks the ratio of composed to atomic facts (3.6 against 18), not data size.
**In this book:** nothing beyond this guide; nearest: [08. Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

### [59:51–1:16:45](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=3591) Mechanistic interpretation of grokking

Decoding internal states reveals different circuits per reasoning type. Composition forms a staged circuit: early layers look up the bridge entity (reliably by layer 5 of 8), the second relation waiting for upper layers; comparison uses a parallel circuit. Out-of-distribution generalization needs a second copy of the second-hop fact in the upper layers, but an atomic fact never seen composed gives the model no reason to store one, which is why composition fails there; tying lower and upper layer weights supplies the copy, and generalization appears. Grokking is this circuit forming: a state that already names the bridge entity gradually gains the second relation, as weight decay favors the efficient circuit.
**In this book:** nothing beyond this guide; nearest: [08. Training Models for Agentic Tasks › The core idea](../02-building-agents/08-training-models-for-agentic-tasks.md#the-core-idea).

### [1:16:45–1:29:10](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=4605) Planning and world models

Planning means choosing actions that end in a state passing the goal test; language agents bring natural-language goals, actions discovered page by page and goal tests hard to automate. The reactive loop is fast but greedy; tree search backtracks, which real websites rarely allow. Model-based planning simulates each candidate with a world model first; WebDreamer, which uses a language model as that world model, beat reactive planning on a sandbox benchmark and cost far less than tree search. The best planning strategy depends on the underlying model: a stronger one may need less scaffolding.
**In this book:** [03. Planning, Search and Decision-Making › How it works: six patterns](../02-building-agents/03-planning-search-and-decision-making.md#how-it-works-six-patterns).

### [1:29:10–1:34:00](https://www.youtube.com/watch?v=zvI4UN2_i-w&t=5350) Future directions and conclusions

Open problems remain in continual learning and personalization, in reasoning without reliable rewards, in genuine world models and in long horizons. Safety keeps him up at night: the attack surface of a web agent is essentially the whole internet, where a deep research agent can be tricked by a seemingly benign website into revealing private information; he separates endogenous risks, which stem from the agent's own incompetence, from exogenous risks, which come from the external environment. He also sees exciting applications: agentic search or deep research, workflow automation and agents for science.
**In this book:** [The Anatomy of an Agent › What the practitioners say](../02-building-agents/01-the-anatomy-of-an-agent.md#what-the-practitioners-say).

## What to take away

- A language agent is a classic agent plus one new action, reasoning in tokens.
- Keep memory outside the weights; HippoRAG adds a graph index for facts scattered across passages.
- Implicit reasoning comes only through grokking; on the open web, simulate before acting.

## Sources

- Yu Su, "On Reasoning, Memory, and Planning of Language Agents", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=zvI4UN2_i-w).
