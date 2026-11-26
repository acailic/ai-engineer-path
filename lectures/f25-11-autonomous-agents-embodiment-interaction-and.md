# Lecture guide: Autonomous Agents: Embodiment, Interaction, and Learning

**Lecturer:** Peter Stone (UT Austin / Sony AI) · **Course:** UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196), lecture 11 · **Length:** 1:02:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=iDhzzugMOLA)
**Chapters that cite this lecture:** [02. Embodied Agents and Robotics](../06-frontier-applications/02-embodied-agents-and-robotics.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Peter Stone, who has studied autonomous agents for three decades, defines an agent as a system that senses and acts, surveys robot soccer, learning from human feedback and robot navigation, and goes deep into two cases: a robot that learns a new skill in 40 minutes in the real world, and a racing agent that beat champion drivers.

## Before you watch

Read [Embodied Agents and Robotics](../06-frontier-applications/02-embodied-agents-and-robotics.md) first; its section on Stone condenses most of this lecture. The lecture assumes you know what reinforcement learning is in outline (states, actions, rewards); the equations are mentioned, not derived.

## The lecture, part by part

### [0:00–2:29](https://www.youtube.com/watch?v=iDhzzugMOLA&t=0) Introduction

The lecturer sets out to give a broad view of autonomous agents, with emphasis on embodiment (robots), interaction and learning, then a deeper look at one or two projects.
**In this book:** not needed (course introduction).

### [2:29–8:11](https://www.youtube.com/watch?v=iDhzzugMOLA&t=149) What an agent is

An agent senses its environment and acts on it through effectors (in a robot, the motors); a chatbot that waits to be invoked is a borderline case, an autonomous agent runs a continuous loop in which each action changes the next sensation. A robot differs only in that its environment is physical, so all robots are agents but not all agents are robots. A complete agent perceives, decides (by planning, teamwork or modelling others) and acts. The question that has guided the lecturer's lab since his 1998 thesis: to what degree can agents learn among teammates and adversaries in real-time dynamic domains?
**In this book:** [Embodied Agents and Robotics › The core idea](../06-frontier-applications/02-embodied-agents-and-robotics.md#the-core-idea).

### [8:11–13:11](https://www.youtube.com/watch?v=iDhzzugMOLA&t=491) Robot soccer and other inspirations

RoboCup aims for a humanoid team that beats the world champions by 2050. In 2025 his robots played their first match alongside people, because people still win too easily; one robot kicked the ball between the legs of the RoboCup president. Progress on physical systems is much harder than in software. Service robots that set tables or put away groceries, and autonomous driving, inspire the lab in the same way.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [13:11–16:43](https://www.youtube.com/watch?v=iDhzzugMOLA&t=791) A racing agent that beat the best drivers

With a team at Sony AI the lecturer trained agents, by reinforcement learning inside the driving game Gran Turismo, to outdrive the best humans, the first such result on a physically realistic real-time control task. The game models slipstream and tyre grip well enough that a professional's lap times in the simulator and in a real car differ by under a tenth of a second. The agents lost in July 2021, won in October 2021 on three track combinations, and now race permanently in the game. Training started from random driving; a day on a bank of consoles beat the best lap on an empty track and a week was enough for races, where it learned a defensive line on its own.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [16:43–19:11](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1003) An image benchmark built ethically

A second Sony team published a benchmark for human-centric vision. Instead of scraping social media, the team collected 10,000 images from 81 countries with consent: everyone pictured was paid and chose the labels that describe them. That is too small for training and enough for evaluation. The authors used it to confirm known biases of vision-language models and to find new ones.
**In this book:** nothing beyond this guide; nearest: [Embodied Agents and Robotics › What this means for someone building agents](../06-frontier-applications/02-embodied-agents-and-robotics.md#what-this-means-for-someone-building-agents).

### [19:11–23:10](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1151) Learning from a person's approval

A former student built a system, TAMER, in which a person says good move or bad move while the agent plays Tetris. Plain reinforcement learning needed hundreds of thousands of games; with this feedback the agent cleared hundreds of lines by its third game. It learns faster but ends weaker, in line with the "bitter lesson" that human input can lower the final performance, so a follow-up learns from both sources. An extension moved to image input, which the lecturer calls the first reinforcement learning from human feedback. A later system learns from implicit cues, an idea he illustrates with frightened passengers in a car.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [23:10–26:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1390) Navigation: learn the settings, not the actions

Off-the-shelf navigation stacks carry many opaque parameters that differ between corridors, open spaces and tight passages, and a roboticist had to tune them for each place. The lab treats the stack as a black box and learns only its settings, a parameter policy. The human input can be a remote-controlled demonstration, an intervention when the robot errs, good-move and bad-move feedback, or none at all.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [26:00–28:33](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1560) Ad hoc teamwork

People join a pickup basketball game and cooperate at once with strangers. Ad hoc teamwork asks for an agent that cooperates with teammates it did not train with and cannot choose, as when a disaster rescue brings together robots from many different people. The lab posed the problem in 2010 and has studied it theoretically and in experiments since. He wants such robots to work out on the fly how to work together, without being reprogrammed.
**In this book:** [Embodied Agents and Robotics › What the practitioners say › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [28:33–34:50](https://www.youtube.com/watch?v=iDhzzugMOLA&t=1713) Why real-world reinforcement learning needs a new action space

A recent paper from the lab teaches a robot whole-body mobile manipulation, such as wiping a whiteboard while avoiding a bin, by reinforcement learning on the real robot, with no demonstrations. A robot cannot run millions of trials overnight; a faithful simulator is costly and a crude one does not always transfer; collecting demonstrations is expensive. Random commands to every motor would exhaust the battery or the patience first. The idea: learn a small, abstract action space in a crude simulator by unsupervised reinforcement learning, exploration with no reward, the way a baby in a playpen plays without a task.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [34:50–38:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=2090) A structured latent action space

A latent action space has a few dimensions whose values produce meaningfully different behaviour. Earlier work had shown that an agent can discover diverse skills on its own; the lab made the space disentangled, so that changing one variable moves only the base, only the arm or only the camera. Two rewards do it: one that makes changing a single latent variable change only one aspect of behaviour, and a hand-coded safety term against self-collision. The decoder that maps latent actions to motor commands is trained in the crude simulator and then frozen.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [38:00–44:15](https://www.youtube.com/watch?v=iDhzzugMOLA&t=2280) Learning the task on the real robot in 40 minutes

A factorized version of a popular actor-critic algorithm exploits the structure: each reward term, such as where the base is or what the arm touches, depends on only some action factors, and a learned mask records which. The robot then learns from its own camera and joint angles. From random motion it learned to wipe the board in 40 minutes; the same action space served four tasks, each trained in under an hour, with higher success and fewer safety violations than learning everything in simulation or two existing methods, one of which learns in the raw action space. The lesson is to use simulation to prepare learning, not to transfer a policy. The lab is also testing whether foundation models can supply common sense instead of low-level control.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [44:15–52:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=2655) Inside the racing agent: control

The agent acts ten times a second at the edge of control: any faster and it spins out, any slower and it is passed. Its action space is naturally two-dimensional (steering, and throttle or brake), so no latent space was needed. Rewards paid for speed and penalized tyre slip, leaving the track and hitting walls. A bank of consoles generated rollouts for an experience replay buffer. A new variant of the algorithm, which learns the full distribution of outcomes rather than their mean and scores actions over several steps, cut about a second off a lap compared with the standard version. After an hour the car stayed on the track, after eight hours it drove like an expert, and after a day it matched the best human's average on one track and beat it on two others.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [52:00–56:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3120) Inside the racing agent: tactics

Speed alone does not win races. The state now included nearby cars, with a reward for passing and a penalty for being passed. The team staged traffic on purpose: one car behind one, two, three or seven others, starting on a straight or in a corner. The agent learned the slipstream pass and a double crossover pass without being told or rewarded for them specifically. The mix of such situations in the training data was engineered by hand for the paper; the team has since worked on choosing it automatically.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

### [56:00–59:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3360) Inside the racing agent: etiquette

A human steward judges what is sportsmanlike, so the agent must not push rivals off the track. It must not be too timid either: it once braked and let a human pass, being too concerned about causing a collision. The team added reward signals against collisions, above all those judged the agent's fault. In October 2021 the agents finished first and second in an eight-car race against four humans; a driver said she had learned from watching them.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword) · [Embodied Agents and Robotics › Pitfalls](../06-frontier-applications/02-embodied-agents-and-robotics.md#pitfalls).

### [59:00–1:02:00](https://www.youtube.com/watch?v=iDhzzugMOLA&t=3540) Style, difficulty and conclusion

Rewarding drifting produced a spin into corners that no human driver uses. To be fun in the game the agent needed an adjustable skill level. The lecturer closes: agents have been studied for a long time, and interaction, learning and embodiment are their key parts.
**In this book:** [Embodied Agents and Robotics › Peter Stone (December 2025): agents are older than the buzzword](../06-frontier-applications/02-embodied-agents-and-robotics.md#peter-stone-december-2025-agents-are-older-than-the-buzzword).

## What to take away

- An agent senses, decides and acts in a continuous loop; robots are agents with a body.
- Feedback from people cuts the trials needed from hundreds of thousands of games to three, but caps the final skill; combine it with autonomous learning.
- On a real robot, learn a small structured action space in a crude simulator first; the task then takes minutes, not days.
- An agent optimizes the reward it is given, so unwanted behaviour such as tyre slip, leaving the track or collisions must be penalized too.

## Sources

- Peter Stone, "Autonomous Agents: Embodiment, Interaction, and Learning", UC Berkeley Agentic AI MOOC, Fall 2025 (CS 294/196): [video](https://www.youtube.com/watch?v=iDhzzugMOLA).
- Course page: <https://rdi.berkeley.edu/agentic-ai/f25>.
