# Lecture guide: Evolution of system designs from an AI engineer perspective

**Lecturer:** Yangqing Jia (NVIDIA) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 2 · **Length:** 1:20:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=xqRAS6rAouo) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/Yangqing.pdf)
**Chapters that cite this lecture:** [01. The Anatomy of an Agent](../02-building-agents/01-the-anatomy-of-an-agent.md) · [02. Tool Design and Function Calling](../02-building-agents/02-tool-design-and-function-calling.md) · [04. Memory and Knowledge for Agents](../02-building-agents/04-memory-and-knowledge-for-agents.md) · [06. How Agent System Designs Evolve](../02-building-agents/06-how-agent-system-designs-evolve.md)

> **In one sentence:** Yangqing Jia follows how models, applications and infrastructure evolved together, and argues that AI compute breaks the rules of conventional cloud yet brings back older engineering wisdom.

## Before you watch

Read [How Large Language Models Are Trained](../01-foundations/02-how-large-language-models-are-trained.md) first; the opening analogy assumes that a language model predicts the next token.

## The lecture, part by part

### [0:00–3:35](https://www.youtube.com/watch?v=xqRAS6rAouo&t=0) Introduction and background

Yangqing Jia did his PhD at Berkeley, moved from research into engineering at Google, Facebook and Alibaba, and founded Lepton AI, a cloud for AI workloads that NVIDIA acquired.
**In this book:** not needed (course introduction).

### [3:35–10:29](https://www.youtube.com/watch?v=xqRAS6rAouo&t=215) The Chinese typewriter and next token prediction

An early Chinese typewriter carried thousands of characters, and its speed depended on the distance from one character to the next, so people counted which pairs occurred together and placed those side by side. That counting is next token prediction done by hand, the principle behind today's language models.
**In this book:** [How Large Language Models Are Trained › Inference: from prompt to next token](../01-foundations/02-how-large-language-models-are-trained.md#inference-from-prompt-to-next-token).

### [10:29–19:36](https://www.youtube.com/watch?v=xqRAS6rAouo&t=629) New algorithms keep coming

Closed models still lead, but open-source models such as DeepSeek and Qwen catch up in about six months, and usage reported by the routing site openrouter.ai grew about tenfold in a year. He reads each new wave as an older idea returning: mixture of experts as sparse parameters, test-time scaling as prediction repeated along time, reinforcement learning as scoring a whole rollout.
**In this book:** [How Agent System Designs Evolve › What the practitioners say](../02-building-agents/06-how-agent-system-designs-evolve.md#what-the-practitioners-say) · [From Base Model to Assistant: Post-Training › 4. Reinforcement learning with verifiable rewards](../01-foundations/03-from-base-model-to-assistant-post-training.md#4-reinforcement-learning-with-verifiable-rewards).

### [19:36–28:57](https://www.youtube.com/watch?v=xqRAS6rAouo&t=1176) Consumer applications: hype, fluidity and who pays

Retrieval-augmented generation slides down the hype cycle while prompt engineering and agentic AI climb, and one engineer he knows built elmo.chat, a browser companion that summarizes a page, in two days. The consumer market stays fluid, so a thin layer over a model is no moat, and the products that earn hundreds of millions of dollars are those built into daily work, such as a coding assistant or a meeting recorder.
**In this book:** [How Agent System Designs Evolve › What the practitioners say](../02-building-agents/06-how-agent-system-designs-evolve.md#what-the-practitioners-say).

### [28:57–32:49](https://www.youtube.com/watch?v=xqRAS6rAouo&t=1737) Enterprise applications and the synergy with model builders

Enterprise applications grow more slowly than consumer AI because they need unglamorous integration: an enterprise search product took over three years to reach $100 million in annual recurring revenue. A language-learning app expected to die instead uses models to create course content faster, so model builders and application builders reinforce each other.
**In this book:** [The Anatomy of an Agent › What the practitioners say](../02-building-agents/01-the-anatomy-of-an-agent.md#what-the-practitioners-say) · [How Agent System Designs Evolve › What the practitioners say](../02-building-agents/06-how-agent-system-designs-evolve.md#what-the-practitioners-say).

### [32:49–50:00](https://www.youtube.com/watch?v=xqRAS6rAouo&t=1969) AI infrastructure as a third pillar: a different workload, and how to run it

AI infrastructure is now a third pillar of IT strategy because AI workloads differ from web services: they compute far more than they move, one failed GPU machine can end a whole training run, and machines are not interchangeable, which opened the market for the neocloud. Researchers want a few machines and a rerun when one dies; operators need abstractions because GPUs fail more often than expected. His practices for AI startups: several cloud suppliers, watched utilization, one platform that hides the orchestration, and your own team around the model. Old wisdom returns as well: a restarted chatbot model was killed by its queue of waiting requests until a component admitted traffic gradually.
**In this book:** [How Agent System Designs Evolve › What the practitioners say](../02-building-agents/06-how-agent-system-designs-evolve.md#what-the-practitioners-say).

### [50:00–59:14](https://www.youtube.com/watch?v=xqRAS6rAouo&t=3000) Hardware back toward the mainframe, and a problem outside text

A 1985 supercomputer acted as one machine on a shared bus; the cloud era replaced it with small, swappable servers; AI goes back toward the mainframe, with rack-scale systems whose switches let every processor reach every other machine's memory, so a model need not be split across machines. He closes with a digital twin of an airport that finds taxiways silently blocking traffic: hard real problems take data that is not text and return actions that are not text.
**In this book:** nothing beyond this guide.

### [59:14–71:15](https://www.youtube.com/watch?v=xqRAS6rAouo&t=3554) Questions: what hyperscalers sell, what tokens cost, why retrieval stays

Hyperscalers now sell results or tokens rather than resources, but many training jobs are still not written to be interrupted and rerun. Some applications pay more for tokens than they collect; he expects falling prices to close that gap within a year. Retrieval is not obsolete: it runs as cheap coarse ranking followed by fine ranking by a language model, and the unclear line between common knowledge and supplied facts feeds hallucination. Work also moves poorly between clouds: training wants its machines on one rack, and petabytes of data travel slowly.
**In this book:** [How Agent System Designs Evolve › What the practitioners say](../02-building-agents/06-how-agent-system-designs-evolve.md#what-the-practitioners-say) · [Memory and Knowledge for Agents › What the practitioners say](../02-building-agents/04-memory-and-knowledge-for-agents.md#what-the-practitioners-say).

### [71:15–1:20:00](https://www.youtube.com/watch?v=xqRAS6rAouo&t=4275) Questions: startup lessons

Technical founders, he says, build from the inside out and underweight attention, which matters as much as the product; his own useful skill is speaking both languages, papers with researchers and machines with engineers. Startups do better in enterprise verticals that big labs will not focus on than in training another foundation model, and robotics and phone-side intelligence will need efficient models and compute near the user. His hardest problem was GPU supply: procuring capacity and negotiating contract terms consumed the founders' time.
**In this book:** nothing beyond this guide.

## What to take away

- Models advance in waves with older analogues, and application builders and model builders reinforce each other.
- AI compute breaks the promises of conventional cloud, yet old operating wisdom returns once AI becomes a product.
- Long context does not replace retrieval, and the line between common knowledge and supplied facts stays unclear.

## Sources

- Yangqing Jia, "Evolution of system designs from an AI engineer perspective", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=xqRAS6rAouo).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25/>.
