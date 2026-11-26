# 11. Course Summary and Outlook

**Level:** Foundation · **Reading time:** 21 min · **Exercise:** 20 min
**Prerequisites:** [Why Efficiency Matters](01-why-efficiency-matters.md) and the four compression chapters, [03](03-pruning-and-sparsity.md) to [06](06-knowledge-distillation.md)

> **In one sentence:** After this chapter you can place any efficiency technique on one map, know which topics the course itself left open, and have a routine for staying current.

## Why this matters

Six months from now a new number format or attention variant appears, with a paper that reports a large speed-up. Should you adopt it? The answer depends on three things you already have: a measurement of your own system, a map of which technique addresses which cost, and the habit of checking claims against your hardware.

This chapter compresses the part into that map and adds the routine. The chapter also follows the final lectures into quantum machine learning, where the course's own architecture search and pruning reappear on noisy devices.

## The core idea: one map, one procedure

Song Han names the through-line of MIT 6.5940 in his first lecture: **algorithm and system co-design** (Lecture 1, [62:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3720)). Change the model and the software or hardware together. Every chapter was one application of that idea:

| Goal | Technique | Chapter |
|---|---|---|
| Efficient inference | pruning and sparsity | [03](03-pruning-and-sparsity.md) |
| | quantization | [04](04-quantization.md) |
| | architecture search | [05](05-neural-architecture-search.md) |
| | knowledge distillation | [06](06-knowledge-distillation.md) |
| | TinyML on microcontrollers | [07](07-tinyml-microcontrollers-and-tinyengine.md) |
| | language model deployment | [08](08-efficient-llm-inference-and-deployment.md) |
| Efficient training | parameter-efficient and on-device training | [09](09-llm-post-training-and-on-device-training.md) |
| | distributed training | [10](10-efficient-vision-generative-models-and-distributed-training.md) |
| Application-specific work | vision transformers, generative models, point clouds | [10](10-efficient-vision-generative-models-and-distributed-training.md) |

The procedure that goes with the map:

1. **Measure.** Latency, memory, energy and quality, on the real hardware and the real workload.
2. **Name the bottleneck.** Weight bytes, activation memory, the KV cache, arithmetic, or communication.
3. **Pick the lever for that bottleneck** (table below).
4. **Apply the cheapest lever first.** Quantize before you retrain. Distill only when the others are not enough.
5. **Re-measure quality and cost.**
6. **Stop when the budget is met.**

| Bottleneck | Levers |
|---|---|
| Too many weight bytes | weight-only quantization, a hardware-supported sparsity pattern, a smaller distilled model |
| Too much activation memory | lower resolution, patch-based inference, in-place operations, a memory-aware architecture |
| KV cache too large | shared heads, paging, cache quantization, attention sinks and windows |
| Decode too slow for one user | 4-bit weights, speculative decoding |
| Arithmetic-bound at large batch | 8-bit weights and activations, fused attention kernels |
| Training does not fit | parameter-efficient fine-tuning, sharding, gradient compression |
| A device with kilobytes | search under the memory constraint, 8-bit everywhere, a code-generating engine |

## What the course treats as the frontier

This part follows the Fall 2024 edition of the course. Four things in the final lectures mark where it was heading:

- **Training everywhere.** Han's closing recap in Lecture 22 lists data, pipeline, tensor and sequence parallelism and FSDP ([2:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120)). The lecture before it ends with training on a microcontroller under 256 KB of memory.
- **Smaller number formats with hardware support.** Lecture 6 covers microscaling formats such as MX4 and the FP4 tensor cores that NVIDIA's Blackwell generation introduced (as of that lecture).
- **Long context and alternatives to attention.** Lecture 15 closes with state-space models that keep a fixed-size state instead of a growing cache.
- **Quantum machine learning.** The last two lectures were given by Hanrui Wang, who had just graduated from Han's lab and was joining UCLA (Lecture 22, [2:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120), [4:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=240)).

### Quantum computing: where the devices stand

Google had shown **quantum supremacy** a few years before the lecture, a computation its device performed better than the best classical computer, and IBM **quantum utility**, a computation that is hard to run classically but not yet useful. A day earlier, Google had released AlphaQubit, a transformer model for decoding a quantum computer's error-correcting codes. Superconducting chips held 5 qubits, the quantum counterpart of a bit, in 2017, 27 in 2019 and 65 in 2020, before IBM's Condor chip passed 1,000. Size is one measure, quality another: error correction trades redundancy for reliability, and in Wang's example 25 physical qubits stand in for one logical qubit; a Harvard team had built 48 logical qubits from neutral atoms. Quantum devices, unlike classical chips, follow several roadmaps, superconducting circuits, trapped ions and neutral atoms among them (Lecture 22, [4:20](https://www.youtube.com/watch?v=svjjD2uthhQ&t=260), [6:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=360), [8:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=480)).

Shor's algorithm belongs to the first stage of quantum algorithms, the 1980s and 1990s: it factors large integers with an exponential speed-up over classical machines, which puts RSA at risk. A National Quantum Initiative followed in the United States in 2018, and NIST has since narrowed the quantum-safe schemes to four (Lecture 22, [12:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=720)). Wang puts the error rate needed to factor an RSA key below one in a hundred million ([16:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=960)).

Today's devices are far from that. Wang places them in the **NISQ era**, where NISQ is noisy intermediate-scale quantum: the control pulses are not perfect and the environment disturbs the qubits, so an adder that a laptop gets right every time is wrong some of the time on a quantum device. Error rates are about one in a thousand for single-qubit gates and one in a hundred for a CNOT, while a model needs tens, thousands or even millions of gates. On a plot of size against error tolerance, today's devices are nowhere near what Grover's database search, quantum chemistry and Shor's algorithm require (Lecture 22, [60:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3600)).

### Qubits, gates and circuits

The attraction is the state's size. One more bit adds one bit; one more qubit doubles the **state vector** that describes the system, so n qubits need 2 to the power of n complex amplitudes. Wang says qubit counts have doubled every year, which makes computing power grow doubly exponentially. By his figure, the 3 exabytes the world produces in a day would in principle fit into 64 qubits. The same growth is why, as he puts it, 20 to 50 qubits are already too many to simulate classically (Lecture 22, [10:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=600), [38:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=2280)).

A qubit's state is a weighted sum of the 0 state and the 1 state, a **superposition** whose two weights are complex numbers. A **measurement** returns one classical bit, 0 or 1 at random, and collapses the state to the bit it returned. The chance of reading a 0 equals the squared overlap of the state with the 0 state, so the two squared weights add up to 1. A quantum computation is therefore repeated many times, and its answer is the distribution of the results (Lecture 22, [18:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1080), [22:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1320)).

Every quantum gate is reversible: from the gate and its output you recover its input. A single-qubit gate is a rotation on the **Bloch sphere**, the sphere of single-qubit states; the Hadamard gate turns the 0 state into an equal superposition of 0 and 1. With several qubits comes the CNOT, a controlled NOT that flips a target qubit only when its control qubit is 1. A Hadamard on one qubit followed by a CNOT yields **entanglement**: prepared and measured a hundred times, the pair reads 00 in half of the runs and 11 in the rest, even when the qubits are far apart (Lecture 22, [26:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1560), [30:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1800), [36:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=2160), [40:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=2400)).

A **quantum circuit** has three stages: the qubits are initialized with the problem, gates are applied, and the qubits are measured, with classical post-processing allowed afterwards. A gate is a pulse: microwave on a superconducting chip, laser light on a neutral-atom device, with the angle set by the pulse's area or duration. Wang's adder is a single CNOT (Lecture 22, [46:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=2760)).

### Quantum machine learning: from data to a circuit

Wang sorts the field by whether the algorithm and the data are quantum or classical; classical algorithms on quantum data control and calibrate devices. Both lectures build their machine learning on classical data handled by quantum algorithms (Lecture 23, [0:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=0)). The model is a **parameterized quantum circuit**: some gates carry a learned angle, an RX gate for instance, while others, such as CNOT, X and H, are fixed (Lecture 23, [2:30](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=150)). For handwritten digits, an encoder turns each pixel of the 4 by 4 image into a rotation angle, trainable U3 and controlled-U3 gates follow, and a measurement and a softmax close the circuit (Lecture 22, [52:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3120)).

Lecture 23 names four encodings, and each trades qubits against gates. In **basis encoding** a binary string is stored as one basis state, the number 2 as the state 10. **Amplitude encoding** loads the input vector into the state vector, so n features take only the base-2 logarithm of n qubits; the input must first be normalized, and loading four numbers already needs many gates. **Angle encoding** puts each value into a rotation, one rotation gate per qubit, and needs no state-preparation circuit, which makes it cheap. **Arbitrary encoding** mixes them: rotation gates, then CNOT gates to entangle, then more rotations (Lecture 23, [14:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=840), [17:30](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1050), [20:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1200)).

**Expressivity** says how much of the state space a circuit can cover: a Hadamard and a Z rotation trace only a ring of the Bloch sphere as the angle varies, and adding an RX gate covers the sphere. **Entangling capacity** runs from 0 for a state that is not entangled to 1 for fully entangled qubits, by the Meyer-Wallach measure: a circuit whose gates each act on one qubit never entangles, and one with many CNOTs joining neighbouring qubits gets close to 1 within a few layers. Data fills the exponential state space only when the qubits are entangled. A circuit must also follow the device's connectivity and use its native gates (Lecture 23, [6:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=360), [10:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=600), [14:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=840)).

### Quantum machine learning: training on noisy devices

Training follows the classical recipe until the gradient. A finite-difference gradient depends on the size of its step, and a bad step gives a derivative far from the true one. The **parameter-shift rule** yields an analytic gradient instead: run the circuit twice, with the angle moved up by π/2 and down by π/2, and take half the difference. Backpropagation through the circuit yields the same gradients, but only on a simulator, since it needs every intermediate state and a real device exposes none. On hardware, backpropagation covers only the classical part, giving how the loss changes with each measured value; the device supplies how each measured value changes with each angle; and the chain rule joins them (Lecture 23, [22:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1320), [26:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1560), [30:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1800)).

The rule costs two circuit evaluations per parameter, so its cost grows with the parameters, as in classical training. **SPSA**, simultaneous perturbation stochastic approximation, cuts that cost: it nudges all the parameters together, each in a random direction, measures the circuit once for the upward and once for the downward perturbation, and gives every parameter an estimate of the same magnitude. Its training curve stays close to that of plain gradient descent. The quantum natural gradient performs best, though it costs far more (Lecture 23, [34:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2040)).

On an IBM device, gradients from the parameter-shift rule lose accuracy to noise. Wang's observation: a gradient of small magnitude carries a large relative error, because a little noise can reverse its direction, whereas a large gradient is unlikely to change direction (Lecture 23, [46:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2760)). So his group's **probabilistic gradient pruning** sums each parameter's absolute gradient across a few steps, ranks the parameters by that sum, updates only those at the top, and drops none for good. He credits it with about 5 to 10% more accuracy on classification tasks, though his slide says 2 to 4%, and with half the training time, because dropped gradients are never computed ([48:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2880)). On-chip training with pruning also closes most of the gap to the ideal curve, and it scales where a simulator does not, since a simulator's time and memory grow exponentially with the number of qubits ([50:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3000)).

The group's PyTorch library, TorchQuantum, models a circuit as an ordinary module and converts it to Qiskit for IBM's devices (Lecture 23, [52:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3120)). Gate types, counts and positions make circuit design a search problem. QuantumNAS trains once and reuses the result. It builds a supercircuit that contains every candidate and trains it by sampling one subcircuit per step and updating its parameters once, so that inherited weights are less accurate than a from-scratch run but keep the order of the subcircuits, which is all the search needs. An evolutionary search or reinforcement learning, scored on the real device under noise, then picks a subcircuit and the qubits to place it on; the winner is retrained from scratch and pruned, since a gate set to an angle close to zero does nothing ([59:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3540), [64:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3840), [68:30](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=4110)).

### Compiling for real devices

**Qubit mapping** picks the most reliable physical qubits, since the 127 of an IBM device are not equal, and works around the topology: a gate that joins qubits which are not neighbours can run only after SWAP gates have moved them next to each other, and every SWAP adds error. SABRE, which IBM's Qiskit uses, gives each possible swap a score from a heuristic that favors swaps bringing pending gates together. Since every circuit is reversible, the compiler can also map the circuit backwards and use the result to improve the initial mapping (Lecture 22, [64:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3840)).

Wang's second platform is the neutral-atom device, whose qubits are identical atoms that can be moved by moving the laser light, so the topology can change during a computation. The group's compiler for the platform, Atomique, schedules that movement and splits the graph of two-qubit gates into one part per array, a max-k-cut, to reduce the SWAPs. It compiles, by his account, circuits of more than a thousand qubits within minutes, where an SMT solver would be optimal but exponential in cost (Lecture 22, [70:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=4200), [76:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=4560)).

### What the course leaves open

Han's summary slides (Lecture 22, slides 2 to 9) do not list open problems. They draw the course as one map: efficient inference, efficient training (distributed training, on-device learning, federated learning) and application-specific work on language, vision-language and diffusion models, with a system layer from electrical engineering, an algorithm layer from computer science and an application layer from AI. His opening remark gives the principle behind it: open up the whole stack and co-design across it, because that opens a much larger design space ([0:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=0)).

The open questions he states are questions he hands to the class. Of quantum machine learning he asks what it is founded on and "how far away are we from quantum machine learning" ([2:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120)). Earlier in the course he leaves two concrete suggestions: trying network augmentation on small language models (Lecture 9), and fitting language models in on-chip memory with many small chips, which he says startups have since done (Lecture 4, [44:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=2640)).

Wang's lectures give that question a scale. Loading data is expensive: a document long enough to make a transformer's attention cost quadratic would occupy only a logarithmic number of qubits, but qubits start in the 0 state, and the circuit that prepares an arbitrary state in them has a depth that grows exponentially. He counts the cost of encoding data among the field's main open problems (Lecture 22, [58:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3480)). The other is the **barren plateau**, the quantum cousin of vanishing gradients: with many qubits and many layers, the variance of the gradients falls exponentially, so circuits cannot simply be stacked deeper (Lecture 23, [38:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2280)). Residual connections are no complete fix: the **no-cloning theorem** rules out the copy of an intermediate state that a skip connection would need ([40:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2400)).

## How to keep track of it

This routine is this repository's own suggestion, not course content.

| What to watch | Where | How often | What to do with it |
|---|---|---|---|
| Benchmark results (MLPerf) | published result tables | each release | read which techniques the fast submissions used |
| The course's own materials | [efficientml.ai](https://efficientml.ai) and its lab code | each new offering | redo one lab |
| Research papers | arXiv, systems conferences such as MLSys | skim weekly | read one paper a month in depth |
| Hardware announcements | chip-makers' documentation | when released | check which formats and sparse patterns are supported |
| Inference engine release notes | the engine you use | monthly | test one new feature against your baseline |

The habit that matters most is the last row of the table above: test what you use against your baseline, and reproduce one number a month. A speed-up you have reproduced on your own hardware is knowledge. A speed-up you have read is a rumor.

## Pitfalls

1. **Chasing every new paper without a measurement problem.** Fix: start from your own bottleneck table.
2. **Adopting a format your engine does not implement.** Fix: check kernel support before promising a speed-up.
3. **Comparing numbers from different hardware and batch sizes.** Fix: compare only like with like, or measure yourself.
4. **Skipping the quality measurement.** Fix: pair every speed number with an evaluation result.
5. **Treating Fall 2024 numbers as current.** Fix: date every figure you reuse.

## Try it

Write a one-page efficiency review of a system you know.

1. Fill in the bottleneck table with measured numbers.
2. Choose one or two levers and write the saving you expect.
3. Find one technique published in the last twelve months that applies, with its source and date.

**You are done when** every claim has a date and a source, and every lever is tied to a measured bottleneck.

**Stretch:** reproduce the technique's headline number on your own hardware and report the gap.

## Key takeaways

- The map has three rows: efficient inference, efficient training, application-specific work.
- The procedure has one rule: measure, name the bottleneck, pick the lever for it, re-measure.
- The course's final topics were distributed and on-device training, low-bit formats, long context, and quantum machine learning.
- Everything here is dated Fall 2024. Re-check before relying on it.
- Reproduce one result a month to stay current in practice, not in theory.
- Quantum devices are noisy: about one error in a thousand per single-qubit gate, against below one in a hundred million for factoring, so the quantum lectures work around noise.

## Self-check

1. A model is too slow for one user on a laptop, and profiling shows memory is the limit. Which lever comes first?
2. Why does quantization come before distillation in the procedure?
3. Name two topics from the course's final lectures.
4. A paper reports a 3 times speed-up on hardware you do not own. What do you do before using the number?
5. What is a barren plateau?
6. Why does backpropagation train a quantum circuit only on a simulator?

<details><summary>Show answers</summary>

1. Weight-only quantization to 4 bits, since weight traffic is the limit and no retraining is needed.
2. Because quantization needs no training run and no data, and distillation costs a full training run.
3. Any two of: distributed and on-device training, low-bit formats, long-context attention and state-space models, quantum machine learning.
4. Check the hardware and batch size, check that your engine supports the method, and measure it yourself if it matters.
5. A region where the gradients of a quantum circuit become vanishingly small as the circuit grows, which makes training stall.
6. It needs every intermediate state, and a real device exposes none. The device instead supplies gradients by the parameter-shift rule, two circuit runs per parameter.

</details>

## Sources

- **Lecture:** Song Han, "Lecture 22: Course Summary + Quantum Machine Learning (Part I)", MIT 6.5940 TinyML and Efficient Deep Learning Computing (Fall 2024): [video](https://www.youtube.com/watch?v=svjjD2uthhQ) · [guide](../lectures/mit-22-course-summary-quantum-machine-learning-i.md), used at [closing recap](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120)
- **Lecture:** Song Han, "Lecture 23: Quantum Machine Learning (Part II)", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=ZDk-GsyInt8) · [guide](../lectures/mit-23-quantum-machine-learning-ii.md), used at [barren plateaus](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2280), [architecture search for circuits](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3600)
- **Lecture:** Song Han, "Lecture 1: Introduction", MIT 6.5940 (Fall 2024): [algorithm and system co-design](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3720)
- **Reading:** EfficientML.ai course site, slides, videos and labs: [efficientml.ai](https://efficientml.ai)
- **Reading:** Hanrui Wang, Yongshan Ding, Jiaqi Gu, et al., "QuantumNAS: Noise-Adaptive Search for Robust Quantum Circuits" (HPCA 2022): [arXiv](https://arxiv.org/abs/2107.10845)

## Next

→ Two directions. For the architecture underneath all of this, [transformer architectures](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md). For putting a compressed model into production, [deploying a model](../07-ml-in-production/07-deploying-a-model.md).
