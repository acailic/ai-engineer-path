# Lecture guide: Multi-Agent AI

**Lecturer:** Noam Brown (OpenAI) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 6 · **Length:** 56:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=SrLcGdVOb9w) · **Slides:** [slides](https://rdi.berkeley.edu/agentic-ai/slides/multiagent_berkeley_2025.pptx.pdf)
**Chapters that cite this lecture:** [04. Multi-Agent Systems I: Games and Self-Play](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) · [05. Multi-Agent Systems II: The LLM Era](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md)

> **In one sentence:** Noam Brown shows what self-play can and cannot do: it solves two-player zero-sum games without any human data, but cooperating with people requires human data; for language-model agents that work together he names lower latency and a choice of models as the gains, and their collaboration is still brittle.

## Before you watch

Read [Multi-Agent Systems I: Games and Self-Play](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) first; its first six sections teach the vocabulary the lecture starts using in its fourth minute (equilibrium, exploitability, best response). The lecture assumes only that you have heard of reinforcement learning and of chain-of-thought reasoning.

## The lecture, part by part

### [0:00–0:16](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=0) Welcome

The lecturer opens and announces a broad tour of multi-agent AI, starting with self-play.
**In this book:** not needed (course introduction).

### [0:16–2:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=16) Self-play made game AI strong; language models lack it

Self-play drove the game breakthroughs (Go, a battle-arena game, a strategy game, poker). The lecturer compares the path of language models with that path: pre-training on good human data, then large-scale compute at inference, then the model improving by playing against itself. Language models have the first two steps and not the third. His takeaway: people's intuitions about self-play are overfitted, as he puts it, to Go and chess, two-player zero-sum games with perfect information.
**In this book:** [Multi-Agent Systems I › What the practitioners say](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#what-the-practitioners-say).

### [2:00–6:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=120) Two answers to "who is the better player"

Outside such games, he says, the nice properties go away. One player wins head to head against anyone over a million hands; another makes the most money in a year by punishing weak players. In poker these can be two different people; in chess or Go, he says, the same person would top both. The first is a minimax equilibrium, the second a population best response. Exploitability measures the distance from equilibrium: a player who always throws rock in rock-paper-scissors loses every round to paper, so their exploitability is one.
**In this book:** [Multi-Agent Systems I › 1. "Who is the better poker player?" has two answers](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#1-who-is-the-better-poker-player-has-two-answers) · [Multi-Agent Systems I › 2. Measure the distance from the top](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#2-measure-the-distance-from-the-top).

### [6:00–9:36](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=360) Why the opponent is assumed to know your strategy

Exploitability assumes that your strategy is common knowledge while the outcome of your random choices is not. The reason: a system used by billions will have its weaknesses found and used. For rock-paper-scissors the fix is to choose each move with probability one third, which ties every opponent but never wins. Poker is different: an equilibrium strategy makes many opponent moves losing moves, so the opponent's mistakes become your profit, and professionals now play that way and deviate only when they spot a weakness.
**In this book:** nothing beyond this guide; nearest: [Multi-Agent Systems I › 2. Measure the distance from the top](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#2-measure-the-distance-from-the-top).

### [9:36–12:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=576) Sound self-play needs no human data

A sound self-play algorithm, starting even from random play, is guaranteed to converge to a minimax equilibrium in any finite two-player zero-sum game, given enough memory and compute. No human data is needed. In perfect-information games the method is close to ordinary single-agent reinforcement learning with enough exploration.
**In this book:** [Multi-Agent Systems I › 3. Why self-play is almost free in two-player zero-sum games](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#3-why-self-play-is-almost-free-in-two-player-zero-sum-games).

### [12:00–13:43](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=720) The guarantee is theoretical

Networks approximate an equilibrium imperfectly, and finding an exploit is easier than defending against one: a 2023 paper showed people could beat leading Go programs with adversarial tricks. The lecturer then changes the payoffs of rock-paper-scissors slightly and shows that a standard policy-gradient method (PPO) does not converge to an equilibrium even there, because nothing in it forces the right balance between moves.
**In this book:** [Multi-Agent Systems I › 4. Hidden information changes the problem](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#4-hidden-information-changes-the-problem).

### [13:43–18:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=823) The value of a move depends on how often you play it

In a modified rock-paper-scissors the equilibrium mixes three moves with probabilities 40, 40 and 20 percent. A depth-limited search, as in chess, returns the same value for every first move and so cannot find the mix. The cause: if you throw rock 80 percent of the time, the opponent adapts and the value of rock drops. In chess the value of an opening hardly depends on how often you use it; in poker, bluffing 10 or 90 percent of the time is a different strategy. He adds a caveat: chess today, with players preparing strategies against each other, starts to resemble a game with hidden information.
**In this book:** [Multi-Agent Systems I › 4. Hidden information changes the problem](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#4-hidden-information-changes-the-problem).

### [18:00–22:33](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=1080) Algorithms that find the probabilities

Fictitious play lets each player best-respond to the average of the opponent's past strategies; the averages converge, but slowly. Regret matching and hedge choose a regularized best response, putting probability on moves in proportion to how much they beat a baseline; a linear variant converges orders of magnitude faster. These iterative algorithms beat four top professionals at heads-up no-limit Texas Hold'em without neural networks. Their weakness is weak performance in single-agent settings; very recent algorithms do well in both.
**In this book:** [Multi-Agent Systems I › 4. Hidden information changes the problem](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#4-hidden-information-changes-the-problem).

### [22:33–25:33](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=1353) Talking to an opponent never helps

In a two-player zero-sum game all equilibria give player one the same value, so any talk either raises that value (the opponent ignores it), lowers it (the speaker stays silent) or changes nothing. Outside two-player zero-sum games most of the nice properties disappear.
**In this book:** [Multi-Agent Systems I › 5. Where language becomes useful](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#5-where-language-becomes-useful).

### [25:33–32:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=1533) The ultimatum game: self-play learns an offer people reject

The lecturer's central claim: learning to cooperate with humans without human data is a dead end. Alice splits 100 dollars and Bob accepts or rejects; rejection means both get nothing. In general, he says, people accept roughly 20 to 30 percent and reject lower offers. Pure self-play converges to the game-theoretic solution, a token offer that a reward-maximizing partner accepts, which real people turn down. Tweaking the game with priors or repetition is a rabbit hole.
**In this book:** [Multi-Agent Systems I › 6. Cooperation needs human data](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#6-cooperation-needs-human-data).

### [32:00–34:07](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=1920) Culture is learned only from human data, and the game of Diplomacy

Acceptance in the ultimatum game differs by culture: somewhere 20 percent is fine, elsewhere anything under an even split is refused, and no algorithm finds that out without data on people. The proof case is Diplomacy, a seven-player board game from the 1950s in which the tactics are simple and the difficulty is negotiation.
**In this book:** [Multi-Agent Systems I › 6. Cooperation needs human data](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#6-cooperation-needs-human-data).

### [34:07–36:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=2047) Why Diplomacy is about trust

Two armies entering the same province both bounce unless one is supported, and support can come from another player. Each turn brings about fifteen minutes of private negotiation, then all moves are written down and carried out at once, so promises can be broken. The experiments use the version without talk, where communication is implicit in the moves.
**In this book:** [Multi-Agent Systems I › The Diplomacy experiment](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#the-diplomacy-experiment).

### [36:00–40:02](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=2160) Two equilibria that do not understand each other

DORA learned no-press Diplomacy by pure self-play and crushed a two-player version. Among seven players, one human-data-trained bot against six DORA copies won about 1 percent of games (a tie would be 14), yet one DORA against six of those bots won only 11 percent. In games that are not two-player zero-sum, an equilibrium reached with copies of yourself does not transfer, and the meaningful target becomes the best response to a population, which requires data on that population.
**In this book:** [Multi-Agent Systems I › The Diplomacy experiment](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#the-diplomacy-experiment).

### [40:02–42:55](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=2402) The recipe that worked

Collect human data and train a model that imitates those humans; scale inference-time compute so the imitation is more faithful, not so it scores higher; then run reinforcement learning with the imitation models as part of the environment. In a 200-game human tournament of no-press Diplomacy the bot trained this way took first place, while DORA fell below the average human. CICERO, built the same way for the game with natural-language negotiation, ranked in the top 10 percent of a human league, second among players with five or more games, with more than double the average score; the limit was the quality of the language models of late 2022. The same recipe beat expert humans at cooperating in a cooperative card game.
**In this book:** [Multi-Agent Systems I › The Diplomacy experiment](../05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md#the-diplomacy-experiment).

### [42:55–46:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=2575) Reasoning models improve fast

The lecturer motivates cooperation between agents with the rise of reasoning models: performance rises with thinking time, and newer models reach the same performance with less of it. On competitive programming the percentile among contestants went from below the fifth in early 2022 to above the 99th in 2025, with a first place among humans in a major contest. Longer thinking has many challenges, he says, and he asks whether a model could be made to think for hours, days or weeks.
**In this book:** nothing beyond this guide; nearest: [Multi-Agent Systems II › Brown: what parallel sampling buys](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#brown-what-parallel-sampling-buys).

### [46:00–48:41](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=2760) Thinking is serial: two parallel alternatives, consensus and best of n

Nobody wants to wait weeks for an answer, and a chain of thought runs one step after another, so latency becomes the bottleneck. Consensus samples the model a dozen or a hundred times and keeps the most common answer; it gives a large gain on competition maths and fails for essays. Best of n samples many times and needs a way to judge the answers, which works when a solution is easy to check, as with a sudoku. Both trade more compute for lower latency than one long chain of thought.
**In this book:** [Multi-Agent Systems II › Brown: what parallel sampling buys](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#brown-what-parallel-sampling-buys).

### [48:41–51:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=2921) Diversity: the best model for each task

A model asked to multiply 15-digit numbers should use a calculator, as a person would. In the same way an agent can hand a task to the model that suits it, because the largest model is not always the best or the cheapest for a query. Routing, where a model sends each query to the model that fits it, is already a simple form of multi-agent AI.
**In this book:** [Multi-Agent Systems II › Brown: what parallel sampling buys](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#brown-what-parallel-sampling-buys) · [Multi-Agent Systems II › So, when do several agents beat one?](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#so-when-do-several-agents-beat-one).

### [51:00–56:00](https://www.youtube.com/watch?v=SrLcGdVOb9w&t=3060) Where systems of language-model agents stand

Multi-agent scaffolds today are heavily engineered and brittle, with no clear success yet of the kind seen in other fields. The field is nevertheless exciting: how agents should communicate was an open problem for decades, and language models settled it by talking in natural language. The lecturer recommends two recent blog posts, one from Cognition and one from Anthropic; the first concludes that today's agents cannot yet hold the long, proactive discussions that parallel work would need, though the technology is close.
**In this book:** [Multi-Agent Systems II › Brown: on run-time collaboration](../05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md#brown-on-run-time-collaboration).

## What to take away

- A sound self-play algorithm solves any finite two-player zero-sum game without human data, but only in theory: real networks stay open to exploits.
- With hidden information the value of a move depends on how often you play it, so the algorithm must find probabilities, not just moves.
- To cooperate with people, train on human data: an equilibrium learned with copies of yourself does not transfer to others.
- Several agents buy lower latency and a choice of models at the price of more compute, and their collaboration is still brittle.

## Sources

- Noam Brown, "Multi-Agent AI", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=SrLcGdVOb9w).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
