# Lecture guide: Multi-Agent Systems in the Era of LLMs

**Lecturer:** Oriol Vinyals (Google DeepMind) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 10 · **Length:** 1:00:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=ntjOxjZMaac)
**Chapters that cite this lecture:** [05. Multi-Agent Systems II: The LLM Era](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) · [06. Agent Infrastructure: Sandboxes, Browser Use and Protocols](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md)

> **In one sentence:** Oriol Vinyals revisits AlphaStar, the agent that reached grandmaster level at StarCraft, to show how its lessons (imitation learning first, reinforcement learning in a league of exploiters, non-transitivity among opponents) bear on language-model agents.

## Before you watch

The chapter [Multi-Agent Systems II: The LLM Era](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) summarizes most of this lecture in its section on Vinyals. The lecture assumes only that you know what reinforcement learning and imitation learning are.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=ntjOxjZMaac&t=0) Introduction

Oriol Vinyals speaks online to Berkeley, where he has deep roots. The lecture has two parts and is, in his words, a meta-lecture: he recovered the slide deck of the AlphaStar project, six or so years old, to show that many issues and solutions of modern language models go back further than people think, and also to see what the project did that language-model agents do not yet match. So the talk mixes AlphaStar with Gemini and other LLM agents, seen with hindsight and foresight.
**In this book:** not needed (lecture introduction).

### [2:00–5:27](https://www.youtube.com/watch?v=ntjOxjZMaac&t=120) What an agent is, then and now

His basics slide is the one from DeepMind's early pitch: an agent with goals that observes an environment and acts to maximize reward. It was not mainstream when he joined; the field connected agents to single environments with well-defined observations and actions, and in games the reward was fully specified and cheap to compute. Today the answer to whether something is an agent varies with whom you ask. Assistants that help users fit the paradigm less neatly: the environment and the actions become diffuse, and it is more useful to think of the agent as a package that includes a harness, which controls how the model is called to issue an action, a search or a terminal command, together with the environment it acts on, whether a computer, a network or a game.
**In this book:** [The Anatomy of an Agent › The core idea](../02-building-agents/01-the-anatomy-of-an-agent.md#the-core-idea).

### [5:27–9:29](https://www.youtube.com/watch?v=ntjOxjZMaac&t=327) Why StarCraft was the hardest game

When DeepMind was acquired it had just mastered Atari; an internal curriculum then led through Go to StarCraft, which he sees as the graduation to full complexity, though games are still studied. A personal note: in 2011, as a graduate student in Dan Klein's group at Berkeley, he saw a project there attack StarCraft with machine learning, and he later led AlphaStar, having loved both machine learning and the game. It then seemed impossible that one neural network could play it. The game is chess in which you do not see the whole board: real time, partially observable, with an action space that mixes high-level strategy and the control of individual units. Players gather resources, build buildings and units, and win by destroying every enemy building; it is fast, and it started esports in South Korea in the late 1990s.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [9:29–11:51](https://www.youtube.com/watch?v=ntjOxjZMaac&t=569) What AlphaStar achieved

One network issued every command. Playing online from the office against opponents who had opted in, it reached grandmaster status, which he puts at roughly the top 100 players per region. In 2019, just before the pandemic, the team took it to BlizzCon, the game's big conference, and played many visitors, including one of the game's legends; a few weeks later that player said he had copied a build he had played against. To Vinyals the episode closed DeepMind's phase of mastering one-on-one games: a human had learned from AlphaStar, and AlphaStar had learned from many humans.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [11:51–14:07](https://www.youtube.com/watch?v=ntjOxjZMaac&t=711) What later projects took from the games

Reporters at the time did not see what playing games had to do with the real world; Vinyals answers with a timeline. Games were a sandbox for trying ideas and for scaling up neural networks, and each major project borrowed algorithms or lessons from the one before. After StarCraft came early work on coding, DeepMind's first language models such as Chinchilla, vision-language models such as Flamingo and Gato, and AlphaFold, which borrowed from transformers and from distilling data. Today most of the research and the resources go into one very large project, Gemini, which he co-leads technically and which aims at the most general system possible; playing a game is now one of many abilities.
**In this book:** nothing beyond this guide; nearest: [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [14:07–20:00](https://www.youtube.com/watch?v=ntjOxjZMaac&t=847) Three training stages, and actions as API calls

The Nature paper describes how the single network was built in three stages: supervised learning from human data, then reinforcement learning that ran inside a massive multi-agent system, the league, which he maps onto what are now called pre-training and post-training. The first technical problem was actions. StarCraft exposes an API in which different functions take different arguments: a force field, say, is issued to a set of units at given coordinates, with a delay and a count of repeats. The team hand-built a small autoregressive recurrent network whose separate softmaxes emitted each argument in turn, and trained it by imitation and reinforcement learning. He calls this strikingly close to tool use in language models, which also call APIs, described today in natural language or code. The difference: the network's architecture fixed AlphaStar's interface, so every design choice had to be ablated by retraining, whereas one transformer now writes calls for any environment, and its output format can be changed by instruction.
**In this book:** [Agent Infrastructure: Sandboxes, Browser Use and Protocols › What the practitioners say](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md#what-the-practitioners-say).

### [20:00–26:28](https://www.youtube.com/watch?v=ntjOxjZMaac&t=1200) Imitation learning came first

In StarCraft, unlike Go or Atari, the action space is combinatorial and the time horizon long, so exploration is hard and a random policy achieves almost nothing. Reinforcement learning from scratch did beat the hardest built-in AI, by sending all its workers to attack, an exploit rather than good play; he doubts that pure reinforcement learning could go all the way, in games or in language models. The team turned to human games: with Blizzard's help they released over one million replays. They also gave the network metadata about each game, such as what the players built and how good they were, as a conditioning signal; it uses information from the end of the game, so he calls it a little like cheating, but it taught the correlations between a coming unit and the steps to build it. That was prompt-following before the term: told to build certain units, or to play like a professional or a novice, the agent played in whatever style the user asked. The differences from language models: about 5 billion training tokens against more than a trillion, instructions encoded as vectors rather than language, and instructions read off from a complete game rather than written by people.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [26:28–29:49](https://www.youtube.com/watch?v=ntjOxjZMaac&t=1588) Reinforcement learning on top, and three tricks

With imitation the agents reached believable game states they had not experienced. Post-training by reinforcement learning is, in his view, the least mature part of language models too. AlphaStar measured progress in Elo; the supervised policy alone reached about 900 Elo, whereas training from scratch without human data gave a weak agent. Plain reinforcement learning on top of it added little and collapsed behaviour, as the diversity learned by imitation was lost, something also seen in language models. Three tricks followed. A penalty keeping the trained policy close to the original one, a form of distillation, preserved diversity of styles and added about 400 Elo. Explicit conditioning on the desired style added almost 150 more. And the value function, which predicts who is winning, was allowed to see the whole board, which made it more accurate and reduced variance, a chronic problem of reinforcement learning.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [29:49–31:58](https://www.youtube.com/watch?v=ntjOxjZMaac&t=1789) Where language models differ

StarCraft's reward is fully specified: you win or you lose. A request such as writing a nice poem has no such test, and rewarding behaviour on general problems is very hard. Two linked differences annoy him. The compute of language models is heavily skewed toward pre-training, whereas in AlphaStar most weight updates happened in the reinforcement learning stage. And language models overfit easily because the number of tasks people find interesting is limited, while every game of StarCraft is unique.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [31:58–36:44](https://www.youtube.com/watch?v=ntjOxjZMaac&t=1918) Robustness: five kinds of opponent

Multi-agent was what he learned during the project, and its purpose was robustness. Good models fail in simple ways: language models with medal-level mathematics miscount the r's in strawberry, and AlphaStar, after training, was tried against humans and found helpless against simple strategies. He sorts the failures into kinds of opponent. Adversarial policies are like adversarial examples, where a panda becomes an airplane: a unit moved in certain ways makes the network degenerate, and users probing the system find this. Exploiters play one fixed policy again and again until they find a weakness and press it. Cheeses are tricks that work against many opponents without being optimal play; professionals use them too, because in a partially observable game unpredictability matters, as in poker. Then come normal policies and the optimal policy, which is very hard to reach with deep reinforcement learning.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [36:44–39:34](https://www.youtube.com/watch?v=ntjOxjZMaac&t=2204) Non-transitivity

The question behind the kinds is whether a policy would work against a different opponent, a property called non-transitivity. An adversarial policy is tied to one network's weights; an exploiter to one opponent; cheese generalizes, and he suspects that weaknesses shared by models from different companies, such as the strawberry miscount, belong there. A colleague's observation gives the shape: strength, measured by Elo or a leaderboard score, is one axis, and within a slice of it agents beat one another in cycles like rock-paper-scissors, especially at lower strength, while at the very top a dominant strategy appears. The picture was drawn for zero-sum games; language models need some abstraction to fit it, but their strengths are plainly uneven within one level.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [39:34–44:00](https://www.youtube.com/watch?v=ntjOxjZMaac&t=2374) Self-play drifts: rock, paper, scissors in StarCraft

Naive self-play does not converge well in such games. In rock-paper-scissors, where a strategy is a distribution over the three moves, it oscillates around the centre while sitting, at any moment, on one pure strategy. Populations of policies that all play one another help; playing against the strongest opponents looked the most promising, even in this toy case, though AlphaStar did not quite do that. StarCraft has its own rock-paper-scissors in three units: the Void Ray, an air unit; the Immortal, a strong ground unit that cannot attack air; and the Stalker, which can attack air. Void Rays beat Immortals, Immortals beat Stalkers, Stalkers beat Void Rays. Starting from human games, the policy first covered the whole distribution; under self-play, even with distillation losses, it drifted until every policy built Void Rays, played superbly against itself and had no answer to anything else. The agent was, in his word, delusional.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [44:00–48:00](https://www.youtube.com/watch?v=ntjOxjZMaac&t=2640) Exploiters: the key idea of the league

The fix is the exploiter. While the main agent trains, a second agent is added whose only goal is to beat it, and the setup is asymmetric: the exploiter learns from their games, the main agent does not. If the main agent specializes in Void Rays, the exploiter naturally builds Stalkers; the main agent is then exposed to the strategy that beats it and learns to answer, for instance by building Immortals when it sees many Stalkers. In the full AlphaStar League, three main agents, one per race, are the ones deployed; many other agents exist only to make them stronger. Main agents play against everyone all the time. A main exploiter starts from the prior policy and trains in secret against the main agents until its win rate is high; only then does it release a checkpoint into the league, where the main agents must now play against it, and it starts again from the prior.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [48:00–50:50](https://www.youtube.com/watch?v=ntjOxjZMaac&t=2880) League exploiters, and the shape of the population

League exploiters work the same way but try to beat everyone in the population, finding exploits that work against all, which resembles cheese. Over time the league held more than a thousand agents of different strengths: an exploiter beats the current main agents, and they catch up and beat it. Plotted by strength, the population looks like a spinning top: the weakest agents are highly non-transitive, with cycles of length up to 30,000, and the strongest dominate. He recalls an exploiter that found the cannon rush, a cheese the main agent had rarely seen; playing against that frozen exploiter, it learned to defend with workers and scouting.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [50:50–54:33](https://www.youtube.com/watch?v=ntjOxjZMaac&t=3050) What the league bought, and the details that matter

With main agents alone, a form of training he calls fictitious self-play, the system reached a certain strength, though he warns that the gaps shown are probably smaller than in reality. Main exploiters made it much stronger, and league exploiters produced the final system, robust against many strategies and very strong. Two details matter. The path of learning changes the final policy: whether an agent is exploited often, rarely or never leaves its mark. And matchmaking had two recipes for choosing among a thousand opponents, the one that beats the main agent most, or the one nearest a 50% win rate, since a hopeless opponent gives no learning signal; the second had slightly lower variance. Finally, controllability: exploiters were sometimes told to attack with a specified unit type, hands partly tied, which added robustness and diversity.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

### [54:33–1:00:00](https://www.youtube.com/watch?v=ntjOxjZMaac&t=3273) What this means for language models

Diversity of the main policy, hard-won in StarCraft, is trivial with language models: they can be asked to solve a theorem in Catalan or at great length. One difference is that users are mostly collaborative, not zero-sum opponents, though adversarial users hunt for failure modes and more powerful systems will attract misuse, so both settings could use multi-agent techniques. The complexity is far beyond StarCraft: there is no clear reward, and prompting is unbounded natural language instead of a few bits about which units to build. Language models can sort of play StarCraft, a dream of his, but not well; games are coming back as evaluations, and some red teaming uses multi-agent ideas, in its infancy. He closes with three beliefs: pre-language-model agents hold many gems worth revisiting, from tool use to architectures, losses, regularization and value functions; human priors with knowledge and experience built on top, as in AlphaGo, are the shortest path to AGI; and post-training for language models is in its infancy next to a league that ran 10 to the 10th training steps, so multi-agent reinforcement learning may bring the next scalability breakthrough.
**In this book:** [Multi-Agent Systems II: The LLM Era › Vinyals: why a population helps, at training time](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#vinyals-why-a-population-helps-at-training-time).

## What to take away

- Imitate human data first, then reinforce: AlphaStar's recipe is, in Vinyals's telling, the recipe of modern language models.
- Plain self-play drifts into one strategy; an exploiter that trains in secret against the main agent forces it to learn an answer.
- Strength is one axis, but within one level agents beat one another in cycles; weaknesses shared across language models look like cheese.
- Language models differ in reward, in where the compute goes and in overfitting; multi-agent post-training has, in his view, barely begun.

## Sources

- Oriol Vinyals, "Multi-Agent Systems in the Era of LLMs", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=ntjOxjZMaac).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
