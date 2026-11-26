# Lecture guide: Project GR00T: A Blueprint for Generalist Robotics

**Lecturer:** Jim Fan (NVIDIA) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 9 · **Length:** 58:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=Qhxr0uVT2zs) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents/assets/jimfangr00t.pdf)
**Chapters that cite this lecture:** [02. Embodied Agents and Robotics](../06-frontier-applications/02-embodied-agents-and-robotics.md) · [05. What Frontier Domains Teach About Agents](../06-frontier-applications/05-what-frontier-domains-teach-about-agents.md)

> **In one sentence:** Jim Fan sets out three principles behind NVIDIA's plan to build one foundation model for humanoid robots: a pyramid of data, a life spent in simulation, and one agent for many bodies, skills and realities.

## Before you watch

Read [02. Embodied Agents and Robotics](../06-frontier-applications/02-embodied-agents-and-robotics.md) first: it defines **reward**, **policy** and **simulator**, which the lecture uses throughout. You do not need any chapter of part 09.

## The lecture, part by part

### [0:00–2:12](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=0) The vision for embodied AI

In Held and Hein's 1963 experiment, two kittens saw the same scenes; only the one that moved itself developed normal vision. A model that has read the internet but never moved is that passive kitten, the lecturer says; babies learn by touching, failing and retrying.

**In this book:** [02. Embodied Agents and Robotics › Jim Fan (November 2024): data is the bottleneck](../06-frontier-applications/02-embodied-agents-and-robotics.md#jim-fan-november-2024-data-is-the-bottleneck).

### [2:12–5:40](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=132) Project GR00T and the case for humanoids

At NVIDIA's 2024 developer conference, humanoid robots from partner companies shared the stage to announce GR00T, the plan to build the AI brain of humanoid robots. Three arguments favor the human shape: it does the valuable physical work, people can predict it, and the world's tools were made for it.

**In this book:** [02. Embodied Agents and Robotics › Jim Fan (November 2024): data is the bottleneck](../06-frontier-applications/02-embodied-agents-and-robotics.md#jim-fan-november-2024-data-is-the-bottleneck).

### [5:40–9:19](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=340) The generalist strategy

The name, he explains, expands to Generalist Robot 00 Technology; the key word is **generalist**. His template is language processing, which once held a separate system for every task, each with its own pipelines. Then one general model arrived that could be prompted for any task and was specialized again by prompting, fine-tuning and distilling into smaller experts that beat the original specialists. Robotics is still at the specialist stage, and GR00T is meant to be its generalist moment.

**In this book:** [Embodied Agents and Robotics › What the practitioners say › Jim Fan (November 2024): data is the bottleneck](../06-frontier-applications/02-embodied-agents-and-robotics.md#jim-fan-november-2024-data-is-the-bottleneck).

### [9:19–13:51](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=559) The data pyramid principle

Robotics lags because text can be downloaded and motor commands cannot. Topping the pyramid is real robot data, scarce at 24 hours per robot per day and gathered by teleoperation. Simulation comes next.

**In this book:** [02. Embodied Agents and Robotics › Jim Fan (November 2024): data is the bottleneck](../06-frontier-applications/02-embodied-agents-and-robotics.md#jim-fan-november-2024-data-is-the-bottleneck).

### [13:51–19:31](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=831) The matrix principle

Below simulation comes internet text and video, the largest and noisiest tier. Robots will live mostly in simulation, the only way to gather trillions of training examples. The reason: simulating a problem is easier than solving it, as the roughly 500 lines of Python that encode the rules of Go show. Two uses follow: reinforcement learning on self-generated data and imitation learning on multiplied demonstrations.

**In this book:** [02. Embodied Agents and Robotics › How it works, step by step](../06-frontier-applications/02-embodied-agents-and-robotics.md#how-it-works-step-by-step).

### [19:31–27:13](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=1171) Whole-body control with HOVER

Reinforcement learning suits skills people cannot explain, such as balance, which needs only 1.5 million parameters. Coordinating the limbs this way is whole-body control, and HOVER is one such network, trained in two stages. First, reinforcement learning in simulation yields a teacher policy that may read exact values a simulator knows. Those inputs are then masked out, and a student policy learns by supervised learning to match the teacher without them, a route more stable than direct reinforcement learning. Masking any subset lets the same network take several command types.

**In this book:** [Embodied Agents and Robotics › How it works, step by step › Whole-body control: a teacher that cheats, a student that cannot](../06-frontier-applications/02-embodied-agents-and-robotics.md#whole-body-control-a-teacher-that-cheats-a-student-that-cannot).

### [27:13–34:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=1633) Generative simulation: RoboCasa and MimicGen

Teleoperated demonstrations arrive at about 20 an hour. A scene needs objects, layouts and task code, usually made by hand; RoboCasa has models generate each, giving about 100,000 kitchens in which one real demonstration can be replayed. MimicGen varies the motion instead, shifting the objects and replaying a demonstration so that it still succeeds and counts as new data.

**In this book:** [02. Embodied Agents and Robotics › How it works, step by step](../06-frontier-applications/02-embodied-agents-and-robotics.md#how-it-works-step-by-step).

### [34:00–38:12](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2040) Two hands, and the limits of generated data

Generated data helps, with limits: on a simple one-arm task, 5,000 generated demonstrations added little over 1,000. DexMimicGen extends the method to two hands and to dexterous hands, sorting subtasks into parallel ones (both arms pick at once), coordinated ones (both lift a tray) and sequential ones (one step must finish first). On these harder tasks the gain is large: 50 times more generated data, from 100 human demonstrations, made the tasks work; one architecture, based on diffusion models, scored best.

**In this book:** [Embodied Agents and Robotics › What the practitioners say › Jim Fan (November 2024): data is the bottleneck](../06-frontier-applications/02-embodied-agents-and-robotics.md#jim-fan-november-2024-data-is-the-bottleneck).

### [38:12–46:42](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2292) The foundation agent principle and Eureka

The third principle places robot research on three axes: the number of bodies, of skills and of realities. For bodies, MetaMorph trains one transformer to control thousands of simple robots. For skills, Eureka has a language model write reward functions as code and tests each by training agents on 10,000 parallel copies, a loop that ends by beating rewards written by human experts.

**In this book:** [02. Embodied Agents and Robotics › How it works, step by step](../06-frontier-applications/02-embodied-agents-and-robotics.md#how-it-works-step-by-step).

### [46:42–52:20](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=2802) DrEureka and sim-to-real

No simulation is exact, so domain randomization varies gravity, friction, weight and size across thousands of simulated worlds; a policy that masters them all may very well also work in the next one, the physical world. DrEureka has the language model write those ranges as well, and the resulting policies moved to hardware with no fine-tuning, including a dog balancing on a yoga ball that was rigid in simulation.

**In this book:** [02. Embodied Agents and Robotics › How it works, step by step](../06-frontier-applications/02-embodied-agents-and-robotics.md#how-it-works-step-by-step).

### [52:20–58:00](https://www.youtube.com/watch?v=Qhxr0uVT2zs&t=3140) The three computers and the closing argument

The target model takes a description of the body plus a natural-language instruction and returns actions. Three computers support it: machines that generate data in simulation (OVX), systems that train the model (DGX) and chips that run it on the robot (AGX). The lecturer closes by calling robotics perhaps the hardest AI problem and humanoid robots worth nothing today and a trillion dollars tomorrow.

**In this book:** [02. Embodied Agents and Robotics › Jim Fan (November 2024): data is the bottleneck](../06-frontier-applications/02-embodied-agents-and-robotics.md#jim-fan-november-2024-data-is-the-bottleneck).

## What to take away

- Real robot data is capped by the clock, so the plan is to live in simulation: generate scenes, multiply demonstrations, randomize physics.
- Reinforcement learning trains what is hard to describe; imitation multiplies what is slow to collect.
- Let a language model write the code that is hard to specify, rewards and simulation ranges, and let measured training results choose.

## Sources

- Jim Fan, "Project GR00T: A Blueprint for Generalist Robotics", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 9: [video](https://www.youtube.com/watch?v=Qhxr0uVT2zs).
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
