# 02. Embodied Agents and Robotics

**Level:** Practitioner · **Reading time:** 10 min · **Exercise:** 45 min

> **In one sentence:** After this chapter you can name the three ingredients behind robot agents that reached expert level, explain where language models fit into that recipe, and apply the same reward-design discipline to a software agent.

## Why this matters

A web agent that clicks the wrong button retries. A warehouse robot that grips the wrong way drops the crate, and the only feedback arrives when someone cleans the floor. Peter Stone's group and Jim Fan's team both hit that wall: real-world experience is scarce. Fan puts a number on one slide: 24 hours of robot data per robot-day. The question this chapter answers: how do you train an agent when experience is that expensive, and what does the answer have to do with agents that only touch software?

## The core idea

An **embodied agent** acts through a body, physical or simulated. Stone defines an agent as "an intelligent system that interacts with the environment through sensors and effectors" ([2:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=120)). Effectors are the parts that act: motors in a robot. Between raw sensors and motors he places three modules: perception (build a model of the situation), cognition (decide what to do), and action (turn the decision into commands) ([4:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=240)).

**Reinforcement learning (RL)** is trial-and-error learning. The agent acts, receives a **reward**, a number that scores how well it is doing, and changes its behavior to earn more. A **policy** is the function from what the agent senses to the action it takes. A **simulator** is a program that imitates an environment so that trials are cheap.

The analogy is a CI loop with a coverage score: run, measure, adjust, repeat. It breaks in two places. A test run is free and repeatable; a robot trial costs time and can break hardware. And code coverage is given, while a reward is something you must design. Stone's racing agent shows both failure directions: without penalties it pushed rival cars off the track, and with too heavy a penalty it braked and let a human pass ([56:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3360)).

## How it works, step by step

Fan's lecture (November 2024) reads as a recipe for one robot skill.

1. **Describe the skill in words.** His running example is spinning a pen with a robotic hand.
2. **Let a language model write candidate reward functions.** In Eureka (Ma et al., ICLR 2024) a coding model proposes several, and agents are trained against each in simulation ([44:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2640), [46:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2760)).
3. **Scale trial and error in simulation.** RoboCasa generates many scenes; MimicGen turns one human demonstration into many successful trajectories across them ([38:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2280)). A **trajectory** is one full record of what the robot sensed and did.
4. **Randomize the physics.** DrEureka varies gravity, friction, weight and size, so the policy cannot depend on one simulated world ([46:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2760)).
5. **Move the policy to the robot.** In Fan's blueprint the model takes a description of the body plus a natural-language instruction and returns actions ([52:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=3120)).

**Voyager-style open-ended agents.** <!-- SOURCE GAP: the chapter scope names Voyager, but the f24-09 packet never mentions it; this paragraph is from general knowledge. --> Voyager (Wang et al., 2023) plays Minecraft with no fixed goal. It has three parts: an automatic curriculum, meaning the model proposes the next task from what the player already has; a skill library, where each learned behavior is saved as executable code and retrieved by its description; and iterative refinement, where errors and environment feedback go back into the next prompt. Fan co-authored that work. His later lecture moves the same idea on: language models stop generating code for skills and start generating the data that trains them.

## What the practitioners say

### Peter Stone (December 2025): agents are older than the buzzword

- Agents have been studied for about three decades, long before "agentic AI" ([0:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=0)).
- **Rewards from people.** He shows a person giving evaluative feedback while an agent plays Tetris, and an extension to video games with Garrett Warnell ([20:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1200), [22:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1320)).
- **Real-world RL.** His group trains a skill on a real robot from about 40 minutes of interaction, with no hand-written reward ([42:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=2520)).
- **GT Sophy**, a racing agent trained with RL inside a driving game ([54:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3240)):
  - *Training:* experience replay (store each step and reuse it) and n-step returns (score an action by several later rewards, not one). Data from different tracks was mixed by hand for each mini-batch, later by an automated method.
  - *Emergent skills:* the slipstream pass, a defensive skill and a double crossover pass. None was programmed or rewarded on its own.
  - *Result, as he recounts it:* humans won in July. After months of fixes, the agents finished first and second in an eight-car race, four against four humans, in October. Driver Emily Jones said she learned from watching them ([58:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3480)).

<!-- VERIFY: Stone says GT Sophy is permanently deployed in the game. Product status changes; confirm before restating as fact. -->

### Jim Fan (November 2024): data is the bottleneck

- **Two kittens.** In Held and Hein's 1963 experiment, two kittens got the same visual experience, but only the one that moved itself developed normal vision. His punchline: today's "passive kitten" is ChatGPT ([0:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=0)). His stated belief is that the future belongs to embodied AI ([2:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=120)).
- **Why humanoids**, in his argument: the human shape already does the valuable physical work, coworkers can predict it, and the world is built for it ([2:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=120)).
- **The diagnosis.** He names data as the culprit ([10:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=600)), and a slide makes the bet: "It's easier to simulate a problem than to solve it" ([9:19](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=559)).
- **MimicGen.** Vary the object positions, keep the motion, and each replay is still a success, so that, in his phrasing, machines teach machines ([32:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=1920)). His arithmetic: RoboCasa turns one demonstration into n scenes and MimicGen into n × n trajectories ([38:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2280)).
- **Sim to real.** A model that masters many randomized worlds "may very well generalize to the 10,000 and first reality, which is the physical world that we live in" ([46:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2760)).
- **Three computers.** One generates data (OVX), one trains the model (DGX), one runs it on the robot (AGX) ([52:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=3120)).

## Pitfalls

1. **A reward with no guardrails.** Fix: penalize the behavior you do not want, as Stone's team did for at-fault collisions.
2. **Guardrails that are too strong.** Fix: test both directions on purpose, aggression and timidity.
3. **One fixed simulator.** Fix: randomize what you cannot model exactly.
4. **Collecting every example by hand.** Fix: take a few good demonstrations and generate variations.
5. **Trusting a model-written reward because the code reads well.** Fix: keep the candidate whose trained agent performs best.
6. **Expecting prompting alone to cross the gap.** Fan's whole argument is that data, not prompts, is the limit.

## Try it

Run a miniature Eureka: let a model write reward functions, and judge them by measurement.

```python
# Illustrative, standard library only: score one candidate reward by rollouts.
import random

def rollout(reward, steps=50):
    x, total = 0, 0.0                     # robot starts at position 0
    for _ in range(steps):
        action = random.choice([-1, 1])   # fixed policy: random walk
        nxt = max(-5, min(5, x + action)) # walls at -5 and +5
        total += reward(x, action, nxt)
        x = nxt
    return total

def reward_a(state, action, next_state):  # candidate a model wrote for you
    return 1.0 if next_state == 5 else -0.01
```

- **Deliverable:** five candidate `reward(state, action, next_state)` functions for "reach position 5, do not bump walls", each scored as the mean of 200 rollouts.
- **Acceptance criteria:** you are done when the table shows the measured score of every candidate, names the best by score, and records one guardrail you added after seeing behavior you did not want.
- **Stretch:** replace the random walk with a small learner and check whether the ranking changes. A real Eureka loop trains an agent per candidate.

## Key takeaways

- Robot agents that reached expert level combined scaled trial and error, grounded feedback and a curriculum of problems.
- Real-world data is the bottleneck, so teams generate data in simulation and randomize it.
- Language models help most where the bottleneck is language: writing rewards, curricula and variations of demonstrations.
- The reward is a specification. Both aggression and timidity in GT Sophy were reward-design problems.

## What this means for someone building agents

1. Treat every metric as a reward. Agents exploit it, so test both failure directions; see [LLM-as-a-judge and rubrics](../03-evaluation/03-llm-as-a-judge-and-rubrics.md).
2. When feedback is slow, build a fast stand-in with the same check. For a software agent that is a test suite; for a robot it is a simulator. Sandboxes play this role too: [agent infrastructure](../05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md).
3. Let the model propose and let a measurement decide. Candidate rewards, candidate plans and candidate patches all work this way; see [planning, search and decision making](../02-building-agents/03-planning-search-and-decision-making.md).
4. Save what works as reusable code or tools, as Voyager's skill library does; see [tool design and function calling](../02-building-agents/02-tool-design-and-function-calling.md).

## Self-check

1. In Eureka, what decides which candidate reward function is kept?
   A. A roboticist reads each function and picks one
   B. Agents are trained with each, and training results decide
   C. The language model ranks its own candidates
   D. The function with the fewest lines is kept
2. What is domain randomization, and which problem does it address?
3. GT Sophy was first too aggressive, then too timid. What changed in between?
4. What did the two kittens in Held and Hein's experiment share, and what differed?
5. What does Voyager store in its skill library?

<details><summary>Show answers</summary>

1. B. Each candidate is scored by training an agent against it.
2. Varying physical parameters such as gravity and friction across simulated worlds, so a policy does not depend on one imperfect simulation and still works in reality.
3. The reward signals: penalties for avoidable and at-fault collisions were added, then balanced.
4. The same visual experience. Only the active kitten controlled its own motion.
5. Each learned behavior as executable code, retrieved by a description of what it does.

</details>

## Sources

- **Lecture:** Peter Stone, "Autonomous Agents: Embodiment, Interaction, and Learning", UC Berkeley Agentic AI MOOC, Fall 2025 (December 1, 2025): [video](https://www.youtube.com/watch?v=iDhzzugMOLA), used at [agent definition](https://www.youtube.com/watch?v=iDhzzugMOLA&t=120), [reward from people](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1200), [GT Sophy](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3360)
- **Lecture:** Jim Fan, "Project GR00T: A Blueprint for Generalist Robotics", UC Berkeley LLM Agents MOOC, Fall 2024 (November 4, 2024): [video](https://www.youtube.com/watch?v=Qhxr0uVT2zs), used at [two kittens](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=0), [MimicGen](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=1920), [Eureka and sim to real](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2760)
- **Reading:** Ma et al., "Eureka: Human-Level Reward Design via Coding Large Language Models" (ICLR 2024): [arXiv](https://arxiv.org/abs/2310.12931)
- **Reading:** Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models" (2023): [arXiv](https://arxiv.org/abs/2305.16291)
- **Reading:** Wurman et al., "Outracing champion Gran Turismo drivers with deep reinforcement learning", *Nature* (2022): [DOI](https://doi.org/10.1038/s41586-021-04357-7)
- **Reading:** Held and Hein, "Movement-produced stimulation in the development of visually guided behavior" (1963): [DOI](https://doi.org/10.1037/h0040546)

<!-- VERIFY: the three DOI and arXiv links and the 1963 paper title come from my knowledge, not from the lecture packets. -->

## Next

→ [03. Agents for Scientific Discovery](03-agents-for-scientific-discovery.md), where the environment is a laboratory and the verifier is a human reading the references.
