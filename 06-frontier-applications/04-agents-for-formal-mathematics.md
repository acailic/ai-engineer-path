# 04. Agents for Formal Mathematics

**Level:** Professional · **Reading time:** 12 min · **Exercise:** 60 min

> **In one sentence:** After this chapter you can explain why a proof assistant gives an agent a perfect verifier, describe the AlphaProof recipe and where it stopped, and decide when a checker you fully trust is worth its cost.

## Why this matters

Sean Welleck shows a language model solving a math problem. The final answer is right. Intermediate steps contain subtle mistakes ([2:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=120)). For a homework hint that is fine. For a proof that other proofs will build on, a person has to check every line, which cancels the gain. The question this chapter answers: what changes when a program, not a person, checks each step, and how far has that been pushed?

## The core idea

**Formal mathematics** is mathematics written as source code. The language is a **proof assistant**, also called an interactive theorem prover; Lean, Coq and Isabelle are examples. A theorem becomes a specification and a proof becomes code. If the code compiles, the proof is correct ([2:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=120)). **Informal mathematics** is everything else: prose, LaTeX, papers.

Three more terms carry the chapter. A **tactic** is one small proof step, such as applying a known lemma. **Mathlib** is the open-source Lean library of formalized mathematics. **Autoformalization** translates a statement or a proof from prose into formal code.

For a programmer the analogy is a type checker: a proof assistant rejects a wrong argument the way a compiler rejects an ill-typed expression. The analogy breaks twice. A type checker looks at shape; a proof assistant checks the whole argument. And it only says that the proof matches the formal statement: if autoformalization wrote the wrong statement, a proof of it compiles without complaint.

| | Informal | Formal |
|---|---|---|
| Form | Prose, LaTeX, papers | Source code in Lean |
| Who checks | A person | The proof assistant |
| Guarantee | None | Correct if it compiles |
| Coverage | All of mathematics | What the library supports |
| Cost to write | Low | Every step spelled out |

## How it works, step by step

### Why agents benefit

Thomas Hubert names three ingredients behind systems that beat experts: scaled-up trial and error, grounded feedback, and a **curriculum**, a graded sequence of problems ([32:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1920)). Lean supplies the first two: it is "the environment to explore mathematics completely in silico", and it reports what is proved and what remains. Kaiyu Yang adds the other half: current training leans on abundant data and checkable answers, and advanced mathematics has neither, so formal tools must supply the feedback ([14:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=840)).

### The AlphaProof recipe

Hubert's slides list four steps (section at [56:54](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3414)):

1. **Autoformalize.** A formaliser model turns a problem into a Lean statement.
2. **Imitate.** The prover model trains on Mathlib to propose tactics for the current proof state.
3. **Reinforce.** The prover trains by **reinforcement learning (RL)**, trial and error against a reward, with Lean as referee and search over tactics.
4. **Train at test time.** On one very hard problem the system generates easier variants, solves one it can, learns from that proof, and repeats until it reaches the target ([70:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=4200)).

### Demonstrated, and expected

- **Demonstrated.** At the International Mathematical Olympiad (IMO) 2024, AlphaProof fully solved problems 1, 2 and 6 (slide at [44:14](https://www.youtube.com/watch?v=3gaEMscOMAU&t=2654)). Human experts failed to translate problem 5 into Lean, and the system made no progress on problem 3 ([52:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=3120)). Paired with the geometry system AlphaGeometry it reached silver-medal standard: 28 of 42 points, as DeepMind announced in July 2024.
- **Expected.** Hubert's stated bet is that "perfect verification will, in the long run, be the most important property for mathematics" ([38:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=2280)). He also wants a method not tuned to the IMO ([68:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=4080)).
- **Not yet.** Mathlib covers about 80 percent of undergraduate curricula in his estimate ([10:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=600)), has gaps such as geometry, and research mathematics needs new objects and theories ([70:00](https://www.youtube.com/watch?v=3gaEMscOMAU&t=4200)). His slide puts Lean adoption at 0.1 to 1 percent of mathematicians (section at [11:06](https://www.youtube.com/watch?v=3gaEMscOMAU&t=666)).

<!-- VERIFY: the 28 of 42 result and DeepMind's announcement date come from my knowledge; the packet lists only the three problems AlphaProof solved. -->

## What the practitioners say

Four lectures, four ways to use the same checker:

| System | Lecturer | Model proposes | Checker | Idea |
|---|---|---|---|---|
| AlphaProof | Hubert | Tactics, after RL | Lean | RL at scale, then RL on one problem |
| ReProver | Yang | Tactics, after retrieving useful lemmas | Lean | Retrieval narrows the search |
| LIPS | Yang | Inequality steps | Symbolic reasoning | Restrict the action space |
| Lean-STaR | Welleck | A thought, then a tactic | Lean | Think in prose before each step |
| Draft-Sketch-Prove | Welleck | An informal proof, then a formal sketch | Automated provers | Separate high-level and low-level work |
| Copra | Chaudhuri | Tactics, with optional informal hints | Lean | No training, all in context |

- **Yang on search.** Go has a 19 by 19 board, so the legal moves are finite; proving allows countless tactics, which makes it a harder search ([26:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1560)). LIPS answers with two step types for inequalities, applying a lemma and rewriting into an equivalent form. His slide reports that it surpasses IMO gold medalists on inequalities (section at [25:07](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1507)).
- **Yang on autoformalization.** Statements have no reliable automatic evaluation, and human proofs leave holes, some marked as left to the reader ([36:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2160)). His answer is to restrict the domain: "problems intractable in general can be made tractable in a specific domain". In Euclidean geometry his team checks a translated statement by proving that it and the reference statement imply each other, with an **SMT solver**, a program that decides whether a formula follows from given facts ([44:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2640)). Prompted without training, GPT-4 still translated only just over 20 percent correctly ([50:00](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=3000)).
- **Welleck on the gap.** Each formal step must be spelled out, which is the gap between how people reason and what Lean accepts ([12:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=720)). Automated provers fill small gaps well and fail on whole olympiad problems, so Draft-Sketch-Prove splits the work ([30:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=1800)). For research mathematics, theorems depend on long, cross-file context, and his miniCTX benchmark shows that methods with similar competition scores separate there ([64:00](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=3840)).
- **Chaudhuri on in-context agents.** Proof trees are wide and deep, harder than any game solved so far ([24:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=1440)). Copra, published at COLM 2024, trains nothing: a model proposes steps and the prover executes them. The absolute numbers are modest, and he calls the Lean feedback essential ([38:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=2280), [46:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=2760)). In one demo an agent invents a helper lemma and proves a compiler correct (section at [46:38](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=2798)). His other theme is abstraction: LaSR searches for equations that fit data and names the concepts they contain, and with local models it beat a genetic-programming baseline ([76:00](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=4560)).

## Pitfalls

1. **Trusting a compiled proof as trust in the theorem.** Fix: review the formal statement; check equivalence with the intended one where a solver can.
2. **Searching an unrestricted action space.** Fix: define the allowed step types and prune with a symbolic tool.
3. **Reading an olympiad score as research-level ability.** Fix: evaluate with long-context benchmarks such as miniCTX.
4. **Tuning everything to one competition.** Fix: hold out problem types, as Hubert says he wants to.
5. **Expecting coverage.** Fix: check that the library supports the area before promising automation.
6. **Assuming your own domain has a perfect checker.** Most software requirements are not formal; the next best thing is a test suite, which checks examples, not all cases.

## Try it

Feel the checker accept and reject.

```lean
-- Minimal Lean 4, no library needed. Illustrative; check it in a Lean 4 web editor.
theorem add_flip (a b : Nat) : a + b = b + a := Nat.add_comm a b

theorem wrong (a b : Nat) : a + b = b - a := by rfl   -- rejected: not true
```

- **Deliverable:** ask a model to translate five one-line statements into Lean. Record for each one: rejected by Lean, accepted but meaning something else, or accepted and right.
- **Acceptance criteria:** you are done when the table has five verdicts with a one-line reason each, and you found at least one statement that compiles yet says the wrong thing, or can explain why none did.
- **Stretch:** take one accepted proof, change a hypothesis, and see which tactics still succeed.

## Key takeaways

- A proof assistant is a verifier that cannot pass a wrong proof of a formal statement.
- AlphaProof combined autoformalization, imitation of Mathlib, RL and RL at test time; at IMO 2024 it solved three of six problems.
- The statement itself is the weak point: autoformalization can be wrong and still compile.
- Search is hard because the action space is unbounded; retrieval, restricted step types and sketches all narrow it.
- Competition results do not transfer automatically to research mathematics.

## What this means for someone building agents

1. Where a true checker exists, make it the reward and the evaluation, and spend your design effort on the curriculum of problems; see [evaluation is the product](../03-evaluation/01-evaluation-is-the-product.md).
2. Separate what language does well, such as plans and sketches, from what symbolic tools do well, such as exact gaps; see [tool design and function calling](../02-building-agents/02-tool-design-and-function-calling.md).
3. Verify the specification, not only the solution. The software analogue is a test that passes against the wrong requirement; see [testing generative and LLM components](../08-quality-assurance/05-testing-generative-and-llm-components.md).
4. When a case is too hard, generate easier neighbors, solve one, and carry the lesson back; see [reasoning in LLMs](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md).

## Self-check

1. A proof compiles in Lean. What exactly is now guaranteed?
   A. The theorem is true as the author intended it
   B. The proof is correct for the formal statement
   C. The statement was translated faithfully
   D. The proof is the shortest possible one
2. Put the four AlphaProof steps in order.
3. Why is proof search harder than searching moves in Go, in Yang's argument?
4. In Draft-Sketch-Prove, what fills the gaps of the formal sketch?
5. What does test-time RL do with a problem that is too hard, in Hubert's account?

<details><summary>Show answers</summary>

1. B. Only the proof of the formal statement. The statement itself still needs review.
2. Autoformalization, supervised training on Mathlib, reinforcement learning, then RL at test time on the target problem.
3. Go has finitely many legal moves on its board; proving allows countless tactics and lemmas, so the action space is unbounded.
4. Automated theorem provers, called by tools such as a hammer.
5. It generates easier variants, solves one that is within reach, learns from that proof, and repeats until the original is solved.

</details>

## Sources

- **Lecture:** Thomas Hubert, "AlphaProof: when reinforcement learning meets formal mathematics", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (March 31, 2025): [video](https://www.youtube.com/watch?v=3gaEMscOMAU), used at [Lean and Mathlib](https://www.youtube.com/watch?v=3gaEMscOMAU&t=480), [three ingredients](https://www.youtube.com/watch?v=3gaEMscOMAU&t=1920), [test-time RL](https://www.youtube.com/watch?v=3gaEMscOMAU&t=4200)
- **Lecture:** Kaiyu Yang, "Language models for autoformalization and theorem proving", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (April 7, 2025): [video](https://www.youtube.com/watch?v=cLhWEyMQ4mQ), used at [why formal](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=840), [search](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=1560), [autoformalization](https://www.youtube.com/watch?v=cLhWEyMQ4mQ&t=2160)
- **Lecture:** Sean Welleck, "Bridging Informal and Formal Mathematical Reasoning with AI", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (April 14, 2025): [video](https://www.youtube.com/watch?v=Gy5Nm17l9oo), used at [informal and formal](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=120), [the gap](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=720), [miniCTX](https://www.youtube.com/watch?v=Gy5Nm17l9oo&t=3840)
- **Lecture:** Swarat Chaudhuri, "Abstraction and Discovery with Large Language Model Agents", UC Berkeley Advanced LLM Agents MOOC, Spring 2025 (April 21, 2025): [video](https://www.youtube.com/watch?v=IHc0TEMrEdY), used at [proof search](https://www.youtube.com/watch?v=IHc0TEMrEdY&t=1440)
- **Reading:** Yang et al., "Formal Mathematical Reasoning: A New Frontier in AI" (2024): [arXiv](https://arxiv.org/abs/2412.16075)
- **Reading:** DeepMind, "AI solves IMO problems at silver-medal level" (July 2024): [post](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/)

<!-- VERIFY: the Lean snippet, the DeepMind post URL and the attribution of 28/42 were not checked against sources; the Lean code was not run. -->

## Next

→ [05. What Frontier Domains Teach About Agents](05-what-frontier-domains-teach-about-agents.md), which compares all four domains on environments, verifiers, search, tools and evaluation.
