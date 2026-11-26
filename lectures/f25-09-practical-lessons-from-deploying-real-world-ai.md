# Lecture guide: Practical Lessons from Deploying Real-World AI Agents

**Lecturer:** Clay Bavor (Sierra) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 9 · **Length:** 48:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=sfJM4LaiYsM) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/Practical_Lessons_AI_Agents.pdf)
**Chapters that cite this lecture:** [04. Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md) · [07. Evals in Production](../03-evaluation/07-evals-in-production.md)

> **In one sentence:** Clay Bavor sets out what Sierra learned in two and a half years of running customer-facing agents for large companies: how to build, test and secure them, and what makes voice hard.

## Before you watch

Read [04. Evaluating Agents: Trajectories and Environments](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md) first: from 28:40 on, the lecture turns to user simulators and to an outcome graded from a final state. [07. Evals in Production](../03-evaluation/07-evals-in-production.md) covers the last ten minutes. The first half of the lecture is a practitioner's tour of a product and needs no chapter.

## The lecture, part by part

### [0:00–3:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=0) Sierra and the three kinds of agents

Sierra, founded in March 2023, builds customer-facing agents for large companies: a sandal brand's warranty line, a home-security firm's replacement parts, a satellite-radio provider moving a subscription to a new car. Bavor sorts agents into three groups: personal assistants, agents that serve a role at work such as coding, and agents that serve a company's customers, which is Sierra's corner.
**In this book:** not needed (course introduction).

### [3:00–4:54](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=180) The agent revolution

Adoption is, he says, faster than anything anyone has seen: the internet needed eleven years, from 1991 to 2002, to reach ten percent of the world in a given week, and ChatGPT needed less than 25 months. His analogy is that agents are to AI what websites were to the internet and apps to mobile: every company will have one that recommends products, handles sign-up and setup, troubleshoots and manages retention. The talk then follows a simple plan: orient the audience in this corner of the agent world, then pass on lessons from meeting reality in deployment.
**In this book:** nothing beyond this guide.

### [4:54–8:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=294) One agent for every channel, priced by outcome

Companies run phone, chat and email as separate channels, each with its own team; Bavor expects them to collapse into one agent, loaded with the company's know-how, that meets customers wherever they write or call. The teams that shape it already call themselves AI architects. Conversation becomes the interface, and nobody has to learn it. Sierra's business model follows: a company pays only when the agent actually resolves a customer's case, for example by shipping a replacement pair of shoes, so that Sierra and the company profit from the same outcome.
**In this book:** nothing beyond this guide.

### [8:00–10:46](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=480) The agent iceberg

To an engineer inside a company, building an agent looks like choosing a model, picking a search index and wiring up a few tools. Below that surface Bavor lists what else has to be right: version control and release management for the agent, observing what it does, keeping it from inventing facts, and keeping it inside the law, for instance no financial advice in banking and no diagnosis in healthcare. In voice there is latency, names and accents to handle, and there are people who try to poison the context. His comparison is the web in 1997, with no standard stack yet and, as a magazine reported, a bank paying $13 million for a site with a single form.
**In this book:** nothing beyond this guide; nearest: [The Agent Framework Landscape › What a framework solves, and what it costs](../05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md#what-a-framework-solves-and-what-it-costs).

### [10:46–12:22](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=646) From technology to product

Sierra's aim is to move agents from hand-assembled technology to a product: configurable, kept secure and released with a product stack, while keeping the expressiveness of the frameworks. The standard Bavor sets is simple without being simplistic. The second shift is from one-off transactions to relationships. Today's agents forget each session, so a second call starts from nothing. Memory has already appeared in ChatGPT, and retrieval offers a lightweight way to add it; Sierra wants a memory foundation that lets a returning caller pick the conversation up where it stopped.
**In this book:** nothing beyond this guide.

### [12:22–14:30](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=742) Relationships and a new development lifecycle

Memory is what turns transactions into a relationship that holds across many interactions. Agents are also non-deterministic and deal with messy human language, a television in the background, two speakers, so the software development lifecycle has to be rethought from first principles as build, test and optimize. Large companies face a choice between a limited off-the-shelf product and a kit of parts, so Sierra offers a platform to build with: higher-level bricks that hide the lower-level work.
**In this book:** [The Anatomy of an Agent › Memory, in one page](../02-building-agents/01-the-anatomy-of-an-agent.md#memory-in-one-page) · [Evaluation Is the Product › The eval-driven development loop](../03-evaluation/01-evaluation-is-the-product.md#the-eval-driven-development-loop).

### [14:30–17:15](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=870) Developing on a platform

Because every channel is now digital, the methods of website engineering, controlled experiments above all, can be applied to conversations; today a call center can only hand two scripts to two groups of a thousand people and hope. An agent should be defined once, by what it knows and can do, and then pick up any channel. Engineering teams use a declarative SDK that states what the agent should do and fits their release process; operations teams use no-code tools. A new data platform combines long-term memory, imported customer data, and the ability to place outbound calls.
**In this book:** nothing beyond this guide; nearest: [Evals in Production › 6. Test in production, carefully](../03-evaluation/07-evals-in-production.md#6-test-in-production-carefully).

### [17:15–23:16](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=1035) Why voice is a pipeline, and what latency hides

Speech-to-speech models are smaller and, in his experience, uncontrollable, so a reliable voice agent today is a pipeline: speech to text, a reasoning loop, then a synthesizer. Every ten milliseconds counts. The clock starts when the person stops talking, not when the audio ends, so the system must detect the end of an utterance early and may start several reasoning and synthesis runs to be ready; filler phrases cover the wait. Because model latency varies between roughly 500 and 2,500 milliseconds, Sierra sends the same request to the provider several times and uses the first answer. Interruptions are a second problem: a listener's "uh-huhs" should not stop the agent, a real objection should, and Sierra fine-tuned its own models to tell them apart. Failover from one model provider to another is needed because frontier models do not offer the reliability of hardened cloud services.
**In this book:** nothing beyond this guide; nearest: [Using LLMs: Tokens, Context and Sampling › 8. A cost and latency mental model](../01-foundations/04-using-llms-tokens-context-and-sampling.md#8-a-cost-and-latency-mental-model).

### [23:16–25:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=1396) Measuring speech-to-text accuracy

Names and pronunciation are hard: a business may have hundreds of proper nouns, such as drug, provider and product names, and one customer's brand requires English and Hawaiian in the same call. Word error rate is the wrong yardstick, because with a television on it rewards writing down the background speech that an agent should ignore. Sierra wrote its own metrics, and the general advice is not to assume that an existing metric for a component measures what a great experience is in your setting.
**In this book:** nothing beyond this guide; nearest: [Evals in Production › 2. Choose online metrics that mean something](../03-evaluation/07-evals-in-production.md#2-choose-online-metrics-that-mean-something).

### [25:00–28:40](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=1500) Voice synthesis

Synthesis has its own details: whether a phone number is read as eight hundred or as digits, how addresses and names are pronounced, and the prosody across sentences. Text written for a chat window fails on the phone because it is far too long; spoken replies are shorter, with more back-and-forth and acknowledgements. The style is tuned per channel, even between text messages and web chat, and matching the speaker's emotion is limited with today's pipeline. A full-time staff member, with the unofficial title of voice sommelier, rates voices on dimensions such as graveliness, breathiness, nasality and verbal fry, and matches them to a brand.
**In this book:** nothing beyond this guide.

### [28:40–31:47](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=1720) The first user simulator

Bavor shows Sierra's first experiment from 2023: a prototype agent that answered questions about 1099 tax forms, paired with a second agent that played the user, which made testing more efficient. He forgot to give either a way to hang up and came back from lunch to about a hundred messages of mutual thanks. Non-deterministic software cannot be checked with unit or integration tests alone; it has to be exercised in scenarios close to the real one, with a messy multi-turn user, tools, and checks on policy.
**In this book:** [Evaluating Agents: Trajectories and Environments › 3. Add a user simulator](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#3-add-a-user-simulator).

### [31:47–35:56](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=1907) τ-Bench

Sierra's research team built τ-Bench as a realistic test harness for agents before they meet the public: a few domains such as telecom, retail and airlines, each with databases and APIs, policy documents, and hundreds of scenarios; a model-based user with a persona, for instance angry because a phone plan was switched off; and a rule-based success check that compares the final database state with the goal, because what matters is a verifiable action. The user can also act, for example by toggling a switch on a modem, so the agent has to reason about state changes it did not cause. The reported metric is pass^k, the chance that all k trials succeed: an agent right 95% of the time is right 20 times in a row in only about a third of cases, and a business runs millions of conversations. Major labs such as Anthropic and OpenAI cite the benchmark in model releases.
**In this book:** [Evaluating Agents: Trajectories and Environments › 5. Grade the outcome from the state](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#5-grade-the-outcome-from-the-state) · [Evaluating Agents: Trajectories and Environments › 8. Report reliability, and the simulator's health](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#8-report-reliability-and-the-simulators-health).

### [35:56–40:09](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2156) Simulations in the product, and traces

The product's simulations are a hardened industrial version of the benchmark: customers configure synthetic databases and tools, mock personas with an emotional state, and the whole voice pipeline. He plays a minute of two simulated voices talking: a Mandarin speaker, an angry caller in a noisy airport, a caller who corrects an ID number. To cut latency further, a trace tool gives an X-ray view of everything that happens under the hood of an action, so that calls can be parallelized and hedged.
**In this book:** [Evaluating Agents: Trajectories and Environments › Simulation at industrial scale](../03-evaluation/04-evaluating-agents-trajectories-and-environments.md#simulation-at-industrial-scale) · [Evals in Production › 1. Log a trace for every attempt](../03-evaluation/07-evals-in-production.md#1-log-a-trace-for-every-attempt).

### [40:09–42:45](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2409) Using AI to improve AI

Sierra's belief is that the fix for most AI problems is more AI. A supervisor agent watches the main agent for task drift, ungrounded claims and forbidden advice; task-specific micro-agents look over its shoulder. Insights lets a customer ask open questions of all its conversations, such as what drives low satisfaction scores or the top reasons for escalation. Expert Answers closes the loop with people: agents handle 60 to 90 percent of inquiries, the rest go to contact-center staff, and their answers to common escalations are synthesized into new knowledge for later runs.
**In this book:** [Evals in Production › 5. Run the flywheel](../03-evaluation/07-evals-in-production.md#5-run-the-flywheel) · [Runtime Monitoring and Detection › A second model as a monitor](../04-safety-and-security/05-runtime-monitoring-and-detection.md#a-second-model-as-a-monitor).

### [42:45–45:22](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2565) Security and guardrails

Agents in front of real customers face constant abuse: one attack asked for the system instructions in Icelandic, backwards; another tried to get advice on smuggling gold. External and internal red teams hunt for such attacks. The defense is layered: deterministic checks on the input, model-based supervisors in sensitive cases, rules and policies inside the agent, an output check that ends the session if the agent is about to reveal its prompts, and ordinary access-controlled software, never the model, between the agent and systems of record. Classic web vulnerabilities, such as denial of service and SQL injection, arrive together with the new ones.
**In this book:** [Defenses: Guardrails, Detection and Secure Design › What each layer stops](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md#what-each-layer-stops) · [Defenses: Guardrails, Detection and Secure Design › 6. Enforce least privilege on every action](../04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md#6-enforce-least-privilege-on-every-action).

### [45:22–48:00](https://www.youtube.com/watch?v=sfJM4LaiYsM&t=2722) Closing

Bavor closes on the problems Sierra has chased for two and a half years, invites questions and notes that Sierra is hiring.
**In this book:** not needed (course introduction).

## What to take away

- An agent is a new kind of software: non-deterministic, so it needs its own lifecycle of build, test and optimize.
- Product and pricing follow the outcome: Sierra is paid only for resolved cases, and wants agent-building to become a product rather than a craft.
- Voice needs a pipeline of its own: speech to text, reasoning and synthesis, with a tight latency budget, interruption detection and failover between providers.
- Measure what matters in your setting: word error rate does not capture speech-to-text quality for an agent, and pass^k, not a single success, captures reliability at scale.
- Improve with AI and defend in layers: supervisors, insights and expert answers on one side; deterministic checks, policies and access controls on the other.

## Sources

- Clay Bavor, "Practical Lessons from Deploying Real-World AI Agents", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=sfJM4LaiYsM).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
