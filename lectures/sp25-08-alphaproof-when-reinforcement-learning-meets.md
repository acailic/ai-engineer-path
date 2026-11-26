# Lecture guide: AlphaProof: when reinforcement learning meets formal mathematics

**Lecturer:** Thomas Hubert (Google DeepMind) · **Course:** UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199), lecture 8 · **Length:** 1:16:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=3gaEMscOMAU) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/alphaproof.pdf)
**Chapters that cite this lecture:** [04. Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Thomas Hubert tells how mathematics became code, how reinforcement learning learned to master games from scratch, and how the two met in AlphaProof, which proved three problems in Lean and, with AlphaGeometry solving a fourth, reached silver-medal level at the 2024 International Mathematical Olympiad.

## Before you watch

Read [Agents for Formal Mathematics](../06-frontier-applications/04-agents-for-formal-mathematics.md) first; it contains the recipe and the results of this lecture in a few paragraphs. The lecture assumes you have heard of reinforcement learning, of the search used in AlphaZero and of pre-training; reinforcement learning itself is defined in a sentence.

## The lecture, part by part

### [0:00–3:40](https://www.youtube.com/watch?v=3gaEMscOMAU&t=0) Mathematics as a root of intelligence

A 2019 talk on the future of mathematics started the chain of events that led the lecturer to this lecture on AlphaProof; he will stress big ideas over details. Galileo said the laws of nature are written in mathematics, and a physicist's essay argued that mathematics predicts as well as describes. From describing and predicting comes shaping: mathematics sits under civilization and technology. The lecturer adds a claim: mathematics asks for reasoning, planning, abstraction, knowledge, creativity and a sense of beauty, so it may be a root node of intelligence from which a whole tree grows.
**In this book:** nothing beyond this guide; nearest: [Agents for Formal Mathematics › Why this matters](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-this-matters).

### [3:40–8:08](https://www.youtube.com/watch?v=3gaEMscOMAU&t=220) How proof became precise

Around 500 BC the Greeks grasped the idea of proof. Euclid's Elements arranged definitions, axioms and theorems, the start of axiomatization, which Hilbert's program developed much further early in the 20th century. Notation came later than one might think: a quadratic equation was once stated in words and its solution spelled out step by step, and only in the 17th century did Descartes fix letters for constants and unknowns, so that x squared plus ten x equals thirty-nine fits on a line. Precise notation removed ambiguity, eased complex manipulations and packed information densely; lifted above examples, mathematicians saw patterns, unified fields and created new ones, as dropping Euclid's fifth axiom led to non-Euclidean geometry, which general relativity needed.
**In this book:** nothing beyond this guide; nearest: [Agents for Formal Mathematics › The core idea](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-core-idea).

### [8:08–11:06](https://www.youtube.com/watch?v=3gaEMscOMAU&t=488) Computer formalization and Mathlib

Writing mathematics in code is the next phase of that arc. Several languages exist, among them Coq and Isabelle; Lean, first built, by his account, for software verification and with mathematics in mind, is a programming language, a theorem prover and an interactive proof assistant. Its open-source community is building Mathlib, the library of the future, with two goals: general (weakest assumptions, strongest results) and unified (one definition per concept). Unification takes the most time, because papers define the same idea in different ways that are not necessarily compatible. The library is one connected whole, which modern mathematics needs; it covers about 80% of undergraduate curricula, and most of it lies beyond, with irregular coverage such as complex analysis and partial differential equations.
**In this book:** [Agents for Formal Mathematics › The core idea](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-core-idea).

### [11:06–17:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=666) What perfect verification unlocks

A proof assistant says "correct" or "incomplete" with perfect certainty, so giant proofs can be trusted and checking delegated to the machine; concerns about correctness, mostly felt in abstract fields, disappear. The whole software stack applies. Mathematics becomes a video game whose levels are theorems, with instant feedback, always a harder level, and a meaningful reward; some enthusiasts say they could do it 14 hours a day. It suits education, since detail can adapt to the reader (the lecturer's father got stuck in week four of an online course on Galois theory, and the professor did not answer). Terence Tao argues that formalization will unlock massive collaboration: most papers have one or two authors and five is the maximum, because each author must check the others' work, but with a trusted checker thousands could contribute, as hundreds do on Mathlib.
**In this book:** [Agents for Formal Mathematics › How it works, step by step › Why agents benefit](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-agents-benefit).

### [17:00–18:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1020) Why few mathematicians use it

In his estimate only 0.1 to 1 percent of mathematicians have adopted Lean. The learning curve is steep, and perfect verification demands every detail, which costs time that researchers would rather spend on what they do not yet know; the tooling and the library are still maturing.
**In this book:** [Agents for Formal Mathematics › Demonstrated, and expected](../06-frontier-applications/04-agents-for-formal-mathematics.md#demonstrated-and-expected).

### [18:00–22:04](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1080) A proof in Lean

The lecturer shows the infinitude of primes. Unicode lets the statement read almost as on paper: for every natural number n there is a prime p greater than n. Each line of the proof updates a tactic state that lists what is known and what remains; the key idea is Euclid's, to take the least factor of n factorial plus one. The proof ends with no goals left.
**In this book:** [Agents for Formal Mathematics › The core idea](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-core-idea).

### [22:04–30:27](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1324) Reinforcement learning and the "zero" idea

Reinforcement learning is trial and error toward a goal; the reward need not guide, it can be one when the goal is reached and zero otherwise. Run at scale it mastered Atari games, Go, StarCraft and Stratego, discovered new algorithms, and shaped plasma in a fusion device. The "zero" philosophy: if an agent masters a domain from scratch, it has discovered knowledge by itself and the method should generalize. AlphaGo Zero and AlphaZero learned by playing themselves from random moves, rediscovered thousands of years of human patterns in days and then dropped some, as the Caro-Kann defence showed up and vanished in AlphaZero's self-play while the Queen's Gambit grew. AlphaTensor found new ways to multiply matrices at sizes beyond the two-by-two case, where Strassen's seven multiplications are optimal, in an action space of about 10 to the 30th.
**In this book:** [Agents for Formal Mathematics › How it works, step by step › The AlphaProof recipe](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-alphaproof-recipe).

### [30:27–35:28](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1827) Two worlds meet

Four properties made those systems superhuman: trial and error at scale; grounded feedback, since with invented feedback it is very hard to venture beyond what is known; search, which finds moves of low prior probability such as AlphaGo's move 37; and a curriculum, supplied by self-play. Lean provides trial and error at scale and grounded feedback for mathematics: an environment to explore entirely on a computer that reports what is proved and what remains. The algorithm comes from AlphaZero; the open question is where the levels come from. Problems must come partly from people, because the aim is to help human mathematics and people have already posed interesting problems, and partly from the system itself.
**In this book:** [Agents for Formal Mathematics › Why agents benefit](../06-frontier-applications/04-agents-for-formal-mathematics.md#why-agents-benefit).

### [35:28–39:05](https://www.youtube.com/watch?v=3gaEMscOMAU&t=2128) Formal or natural language

Most work on AI for mathematics uses natural language, because textbooks and papers outweigh Mathlib by orders of magnitude. The cost is verifiability: reasoning in prose cannot be checked, and in mathematics one false statement destroys everything built on it, so complete reliability is required. Lean is already superhuman at verification. The same holds for other data-scarce domains that matter, where a process is needed that keeps discovering new facts and grounding them. AlphaProof's foundational bet, in his words: "perfect verification will, in the long run, be the most important property for mathematics".
**In this book:** [Agents for Formal Mathematics › Demonstrated, and expected](../06-frontier-applications/04-agents-for-formal-mathematics.md#demonstrated-and-expected).

### [39:05–44:14](https://www.youtube.com/watch?v=3gaEMscOMAU&t=2345) The International Mathematical Olympiad

Each country sends its six best high-school students, who tackle six problems over two sittings of four and a half hours each; of the six problems, two are easy, two medium and two hard. In the United States about 17 million students narrow to 60,000 contest entrants, then to a competition whose answers are integers from 1 to 1,000, then 250, a training camp, and six; contestants prepare about a thousand hours. The problems are chosen to resemble nothing seen before, so the event tests reasoning rather than knowledge; the national coach reports needing hours himself, and only half of the contestants solve two problems or more. The 2024 problems had not leaked, so they had to be solved by reasoning.
**In this book:** [Agents for Formal Mathematics › How it works, step by step › Demonstrated, and expected](../06-frontier-applications/04-agents-for-formal-mathematics.md#demonstrated-and-expected).

### [44:14–50:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=2654) Three decisions before the competition

The entry was run like an Apollo program: can the system solve the problems at all, with the compute available? Many expected that to be five or ten years off. Seven months ahead, Euclidean geometry was sparse in Mathlib; by luck another DeepMind team had just published a paper on a system close to gold-medal level on such problems, AlphaGeometry, so it took the geometry problems and AlphaProof took algebra, number theory and combinatorics. For "find all" questions the team rejected the easy mode of proving a supplied answer: Gemini proposes candidates and AlphaProof tries to prove and to disprove each. The problems were formalized by human experts before entering the system, because the target is mathematical reasoning, not translation.
**In this book:** [Agents for Formal Mathematics › How it works, step by step › Demonstrated, and expected](../06-frontier-applications/04-agents-for-formal-mathematics.md#demonstrated-and-expected).

### [50:00–56:54](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3000) Four days at the olympiad

Day one: for the two problems that needed an answer, AlphaProof disproved 99% of the wrong candidates within minutes, a sign it understood them. Day two: AlphaGeometry solved the geometry problem in seconds; the combinatorics problem was so tricky that the human experts could not formalize it that day; on the hardest problem, a functional equation, the system disproved only 7% of guesses. By Thursday it had proved half of one problem, having split it into cases by itself, and arguably all of another. On Friday an automated email announced a full proof of the hardest problem; it was pasted into official Lean and accepted at once, and full proofs of two more followed. Final: three problems fully solved by AlphaProof and one by AlphaGeometry, no partial point on a fifth, silver-medal score one point below gold, with more time and compute than the students had.
**In this book:** [Agents for Formal Mathematics › Demonstrated, and expected](../06-frontier-applications/04-agents-for-formal-mathematics.md#demonstrated-and-expected).

### [56:54–1:00:30](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3414) The hardest problem, and the gaps

Only 5 of 609 students solved that problem completely, and a Fields medallist spent a couple of hours on it without success; the lecturer does not claim Fields-medal level. Gaps hurt: without the geometry system the team might have had to write that part of Mathlib or have skipped geometry; in one proof a needed theorem was missing from the library, so the problem was harder than necessary; a combinatorics problem about agents and strategies was very hard to formalize for lack of the needed library functions. The system made no progress on the two combinatorics problems and used orders of magnitude more compute than people. It landed on the moon; the next trip should be more efficient.
**In this book:** [Agents for Formal Mathematics › Demonstrated, and expected](../06-frontier-applications/04-agents-for-formal-mathematics.md#demonstrated-and-expected).

### [1:00:30–1:04:40](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3630) The two models, and where problems come from

A formaliser model turns a problem in natural language into Lean, since human problems exist in prose and translating them by hand does not scale. A prover model reads the current tactic state and samples several candidate next lines; placed in an AlphaZero-style search, it adds one line at a time, Lean returns the new state, and the search explores little-visited paths as well as likely ones. The team passed about a million informal problems through the formaliser with about a hundred translations each. A translation that Lean accepts as well-formed is at least a statement that is true or false.
**In this book:** [Agents for Formal Mathematics › The AlphaProof recipe](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-alphaproof-recipe).

### [1:04:40–1:08:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3880) Imitate, then reinforce

The prover starts from a model pre-trained on code and is trained with supervision on Mathlib, about 100,000 definitions, 200,000 theorems and 300,000 lines of proof, to predict the next step of human proofs. That gives a good prior but solves close to 0% of olympiad-type problems, few of which Mathlib contains. Reinforcement learning follows: for each formal problem the system searches for a proof or a disproof, Lean verifies, and the prover is reinforced on its successes. It proves the easiest problems first, learns from them and climbs rung by rung to olympiad strength. The method is deliberately not tuned to the olympiad; the proving strategies were discovered by the model.
**In this book:** [Agents for Formal Mathematics › The AlphaProof recipe](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-alphaproof-recipe).

### [1:08:00–1:11:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=4080) Reinforcement learning at test time

Even a great mathematician needs hours on these problems, so solving one resembles an experiment: guess what might be true, try to prove or disprove, learn. AlphaProof generates variants of the target problem and runs the same learning on them. One variant falls inside what the system can already solve; it solves it, learns from that proof, and repeats until the target itself is reachable. That is how the three solved problems went.
**In this book:** [Agents for Formal Mathematics › The AlphaProof recipe](../06-frontier-applications/04-agents-for-formal-mathematics.md#the-alphaproof-recipe).

### [1:11:00–1:16:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=4260) Challenges and what is next

Most human mathematics is still in natural language, though the team is getting a handle on translating it. Harder: mathematics in areas that Mathlib does not support, geometry for one, cannot even be expressed, which calls for the creative building of new objects and theories. The olympiad was a milestone, strongly correlated in his view with the real goal of going beyond human mathematics: the aim is to move past high school mathematics to the frontiers of research, and to make proof a tool for every thinker. The lecturer ends on the team: optimism is needed to prove anything, in mathematics as in machine learning.
**In this book:** [Agents for Formal Mathematics › Demonstrated, and expected](../06-frontier-applications/04-agents-for-formal-mathematics.md#demonstrated-and-expected).

## What to take away

- Lean verifies proofs perfectly, which makes mathematics a place to practise and lets many people collaborate safely.
- Trial and error at scale, grounded feedback, search and a curriculum took systems from random play to superhuman; Lean supplies the first two for mathematics.
- AlphaProof translated about a million problems, imitated human proofs, reinforced against Lean, and learned from variants of a problem at test time.
- It reached silver-medal score at the 2024 olympiad, AlphaGeometry supplying the fourth solved problem, with far more compute than the students; library gaps and unsupportable areas are the next obstacles.

## Sources

- Thomas Hubert, "AlphaProof: when reinforcement learning meets formal mathematics", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (CS 194/294-199): [video](https://www.youtube.com/watch?v=3gaEMscOMAU).
- Course page: <https://rdi.berkeley.edu/adv-llm-agents/sp25>.
