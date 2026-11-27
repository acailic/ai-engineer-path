# Lecture guide: Course Summary + Quantum Machine Learning I

**Lecturer:** Song Han (MIT) for the recap, then Hanrui Wang (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 22 · **Length:** 1:24:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=svjjD2uthhQ) · **Slides:** [slides](https://www.dropbox.com/scl/fi/cn0wr4zxuv4hvpce81lo1/Course-Summary.pdf?rlkey=ycn79vnsu2n7395fz1v04khz0&st=z86d0rap&dl=0)
**Chapters that cite this lecture:** [16. Quantum Machine Learning](../09-efficient-deep-learning/16-quantum-machine-learning.md) · [17. Course Summary and Outlook](../09-efficient-deep-learning/17-course-summary-and-outlook.md)

> **In one sentence:** Song Han recaps the course, then Hanrui Wang, a graduating member of the lab who joins UCLA, introduces quantum computing from qubits and gates through circuits and the noisy devices of today to the compilers that map circuits onto superconducting and neutral-atom hardware.

## Before you watch

The chapter [Course Summary and Outlook](../09-efficient-deep-learning/17-course-summary-and-outlook.md) carries the course map of the first minutes and lists quantum machine learning among the open questions; the chapter [Quantum Machine Learning](../09-efficient-deep-learning/16-quantum-machine-learning.md) teaches the quantum devices, qubits, gates, circuits and compilers themselves. The quantum half needs only complex numbers and matrices.

## The lecture, part by part

### [0:00–3:10](https://www.youtube.com/watch?v=svjjD2uthhQ&t=0) The course in one view

Han looks back: efficient inference by pruning, quantization, architecture search and distillation; efficient training by parallel, distributed and on-device training and gradient compression; application-specific work from language and vision-language models to diffusion models, point clouds and video; and the demos, a vision-language model on a laptop, the TinyChat computer, a TinyML microcontroller, sensor fusion on a Jetson board. The principle throughout is full-stack co-design of algorithms and systems, drawing on electrical engineering, computer science and AI. Five plus one labs were completed, registration doubled against last year and tripled against two years ago, and YouTube views more than doubled between 2022 and 2023.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier](../09-efficient-deep-learning/17-course-summary-and-outlook.md#what-the-course-treats-as-the-frontier).

### [3:10–8:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=190) Where quantum computing stands

The rest of the lecture belongs to Hanrui Wang, who goes by Henry and moves to UCLA as an assistant professor. Context: the day before, Google released AlphaQubit, a transformer that decodes quantum error-correcting codes; earlier came Google's quantum supremacy and IBM's quantum utility, computations hard for classical machines though not yet useful. He will cover qubits, gates, circuits, the noisy era and compilation. Qubit counts have grown from 5 in 2017 to 27 in 2019, 65 in 2020 and over 1,000 on IBM's Condor chip; superconducting qubits sit in dilution refrigerators that cool to millikelvin so that energy levels become discrete.
**In this book:** [Quantum Machine Learning › What the practitioners say › Where the devices stand](../09-efficient-deep-learning/16-quantum-machine-learning.md#where-the-devices-stand).

### [8:00–10:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=480) Quality, not only quantity

A thousand noisy qubits cannot be used together, so progress also aims at logical qubits: error correction adds redundancy, for instance 25 physical qubits per logical one, and Harvard demonstrated 48 logical qubits on neutral atoms. Unlike classical chips, quantum devices follow several roadmaps: superconducting circuits (IBM with over 1,000 qubits, Google's Sycamore with 53), trapped ions steered by lasers, neutral atoms held by lasers, photonics and semiconductor spin qubits.
**In this book:** [Quantum Machine Learning › What the practitioners say › Where the devices stand](../09-efficient-deep-learning/16-quantum-machine-learning.md#where-the-devices-stand).

### [10:00–12:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=600) Why qubits could matter

Qubit counts double every year, and each added qubit doubles the state space, so computing power grows doubly exponentially. The roughly 3 exabytes of data the world produces each day could in principle sit in 64 qubits, and 100 qubits can hold 10 to the 30th bits, as much as humanity would generate in a billion years. Turning that space into results still demands careful manipulation and algorithms designed for it.
**In this book:** [Quantum Machine Learning › The core idea](../09-efficient-deep-learning/16-quantum-machine-learning.md#the-core-idea).

### [12:00–18:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=720) Three stages of quantum algorithms

In the 1980s and 1990s came algorithms such as Shor's, by MIT's Peter Shor, which factors large integers exponentially faster than classical machines and so threatens RSA; the United States launched a National Quantum Initiative in 2018, and NIST has narrowed the replacement, quantum-safe schemes to four. Those algorithms assumed noiseless devices with millions of qubits. Around 1995, quantum error correction showed that good-enough physical qubits plus redundancy give reliable logical ones. The last twenty years built devices at Google, IBM and elsewhere, including photonic ones at USTC, and reached supremacy and utility. Factoring an RSA key needs error rates below 10 to the minus 8, so the field now works on error-correction schemes and on uses for existing devices.
**In this book:** [Quantum Machine Learning › What the practitioners say › Where the devices stand](../09-efficient-deep-learning/16-quantum-machine-learning.md#where-the-devices-stand).

### [18:00–22:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1080) The qubit and its state vector

A quantum system is described by a state vector. Wang's analogy: a car's position can be given as one number, the mile on the highway, or as a one-hot vector over twelve places. For a qubit the vector form is natural, because the car can be in a superposition of all places. In Dirac notation the bit values are written |0⟩ and |1⟩, and a general state is a superposition, two complex numbers rather than one bit, for instance (1/√2)|0⟩ + (i/√2)|1⟩. Reading the state requires measurement, which collapses it to 0 or 1 at random.
**In this book:** [Quantum Machine Learning › How it works, step by step › Qubits, gates and entanglement](../09-efficient-deep-learning/16-quantum-machine-learning.md#qubits-gates-and-entanglement).

### [22:00–27:30](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1320) Measurement

Because one measurement yields one bit, a computation is prepared and measured many times and the answer read from the distribution. The probability of measuring 0 is the squared overlap between the state and |0⟩, one half in the example state, and the probabilities sum to one, so |α|² + |β|² = 1. This observer effect is the point of Schrödinger's cat: until the box is opened the state is undetermined.
**In this book:** [Quantum Machine Learning › How it works, step by step › Qubits, gates and entanglement](../09-efficient-deep-learning/16-quantum-machine-learning.md#qubits-gates-and-entanglement).

### [27:30–30:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1650) The Bloch sphere, and reversible gates

Writing the second coefficient in polar form leaves two real degrees of freedom, so any single-qubit state is a point on a sphere, the Bloch sphere: |0⟩ at the north pole, |1⟩ at the south. A NOT gate turns the pointer to the opposite pole. Quantum gates are reversible: from the output and the gate the input can be recovered, which keeps the system's energy constant; the simplest reversible gate is the identity, which does nothing. Gates are matrices, and rotations of the sphere.
**In this book:** [Quantum Machine Learning › How it works, step by step › Qubits, gates and entanglement](../09-efficient-deep-learning/16-quantum-machine-learning.md#qubits-gates-and-entanglement).

### [30:00–36:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=1800) Pauli gates, bases, and the Hadamard gate

Besides X, the NOT, there are the Y and Z gates. Z leaves |0⟩ and |1⟩ unchanged up to a global phase that no measurement sees, so they form the Z basis; |+⟩ and |−⟩ are unchanged by X and form the X basis; two states with a factor of i form the Y basis. These are the anchor points on the sphere. The Hadamard gate has no classical counterpart: it turns |0⟩ into the superposition |+⟩. Phase gates S and S† follow, and the general single-qubit U gate, with three parameters, rotates any point to any other and is universal for one qubit.
**In this book:** [Quantum Machine Learning › How it works, step by step › Qubits, gates and entanglement](../09-efficient-deep-learning/16-quantum-machine-learning.md#qubits-gates-and-entanglement).

### [36:00–42:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=2160) Several qubits, and the controlled NOT

For n qubits the state vector has 2 to the n complex amplitudes, still normalized, which is why 20 to 50 qubits already defeat classical simulation. Hadamards on three qubits give equal weight to all eight basis states. Gates on different qubits combine by the Kronecker product. The CNOT, controlled NOT, takes a control and a target qubit and flips the target only when the control is 1; Wang reads its truth table.
**In this book:** [Quantum Machine Learning › How it works, step by step › Qubits, gates and entanglement](../09-efficient-deep-learning/16-quantum-machine-learning.md#qubits-gates-and-entanglement).

### [42:00–46:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=2520) Entanglement

A CNOT exchanges two amplitudes. A Hadamard on the control followed by a CNOT produces the state (|00⟩ + |11⟩)/√2: measured a hundred times, it gives 00 half the time and 11 the rest. Separate the two qubits to opposite ends of the universe and the results still agree, the "spooky action at a distance". Yet no message can be sent this way, the no-communication theorem, because each outcome is random and cannot be chosen. Other two-qubit gates: CZ, which equals a Hadamard, a CNOT and a Hadamard on the target; SWAP, which exchanges two qubits and decomposes into three CNOTs; and controlled rotations such as CRX.
**In this book:** [Quantum Machine Learning › How it works, step by step › Qubits, gates and entanglement](../09-efficient-deep-learning/16-quantum-machine-learning.md#qubits-gates-and-entanglement).

### [46:00–52:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=2760) Gates in practice, circuits, and an adder

Asked how gates are built, Wang answers that it depends on the technology: superconducting qubits receive microwave pulses whose area sets the rotation angle, neutral atoms are lit by lasers whose duration does the same. A quantum circuit has three parts, initialize the qubits with the problem, apply gates, measure, and may end with classical post-processing, much as a processor loads, computes and stores. An adder is a CNOT; a full adder adds a multi-controlled CNOT that sets the carry when both inputs are 1.
**In this book:** [Quantum Machine Learning › How it works, step by step › A circuit that classifies digits](../09-efficient-deep-learning/16-quantum-machine-learning.md#a-circuit-that-classifies-digits).

### [52:00–58:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3120) A quantum machine-learning circuit

To classify handwritten digits, the image is first encoded: one way, phase encoding, turns the pixels of a 4 by 4 image into rotation angles; amplitude encoding writes the image into the state's amplitudes; basis encoding spends one qubit per bit. Trainable layers of U3 and controlled-U3 gates follow, tuned by backpropagation, then a measurement and a softmax. To students' questions: measuring four qubits in different bases yields at least sixteen numbers, and a classical layer matches them to the number of classes; a larger image needs more qubits or a different encoder, a design space as wide as architecture search in classical learning.
**In this book:** [Quantum Machine Learning › How it works, step by step › A circuit that classifies digits](../09-efficient-deep-learning/16-quantum-machine-learning.md#a-circuit-that-classifies-digits).

### [58:00–1:00:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3480) The data-loading bottleneck

A long document, costly for a transformer's quadratic attention, would need only a logarithmic number of qubits to store, which would make the processing power large and the qubit count small beside a classical device. The catch is loading: qubits start in |0⟩, and preparing an arbitrary state takes a circuit whose depth grows exponentially. Efficient data encoding is therefore one of the main open problems for quantum machine learning, and research continues on lowering that cost.
**In this book:** [Quantum Machine Learning › What the practitioners say › The limits the lectures leave open](../09-efficient-deep-learning/16-quantum-machine-learning.md#the-limits-the-lectures-leave-open).

### [1:00:00–1:04:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3600) The noisy intermediate-scale era

Machine learning is said to be in its third wave; quantum computing is in the NISQ era, noisy intermediate-scale quantum. A laptop computes 1 + 1 correctly every time; on a quantum device the same adder is wrong part of the time, because pulses are imperfect, qubits interact with their surroundings, and even cosmic rays disturb them. Error rates are about 10 to the minus 3 for single-qubit gates and 10 to the minus 2 for a CNOT, one wrong answer in a hundred, while a quantum model runs through tens, thousands or even millions of gates. Qubits number in the tens to thousands, and connectivity is limited: IBM's Washington chip arranges 127 qubits in a heavy-hexagon lattice. Plotted by size and error tolerance, today's devices fall far short of what Shor's algorithm, Grover's search and quantum chemistry require.
**In this book:** [Quantum Machine Learning › What the practitioners say › Where the devices stand](../09-efficient-deep-learning/16-quantum-machine-learning.md#where-the-devices-stand).

### [1:04:00–1:10:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=3840) Qubit mapping

Systems research can narrow that gap from the middle layer. Qubit mapping chooses the most reliable qubits, since the 127 are not equal, and copes with topology: a gate between two distant qubits needs SWAP gates to bring them together, and every SWAP adds error. SABRE, used in IBM's Qiskit, scores every candidate swap with a heuristic on how many gates it brings within reach. Because circuits are reversible, mapping the reversed circuit also improves the initial mapping, iteratively. QuantumNAS, from the lab, searches mappings with evolutionary search, Bayesian optimization and reinforcement learning, measuring the cost on real devices.
**In this book:** [Quantum Machine Learning › How it works, step by step › Compiling for a real device](../09-efficient-deep-learning/16-quantum-machine-learning.md#compiling-for-a-real-device).

### [1:10:00–1:16:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=4200) Neutral-atom devices

Neutral-atom devices are reached through cloud providers such as AWS and have, by his account, grown from two qubits to over 60,000 atoms in a Caltech demonstration. Atoms are identical by nature, keep their state about ten seconds, a thousand times longer than superconducting qubits, and more than 10,000 fit in a square millimetre. Arrays are static, or movable when the laser pattern moves, so the topology changes during a computation: any two atoms within the Rydberg radius can share a two-qubit gate. The lab's compiler for such devices, Atomique, decides which atoms to use and schedules their movement; in the example, atoms move into place and one pulse of light performs all gates of a layer at once.
**In this book:** [Quantum Machine Learning › How it works, step by step › Compiling for a real device](../09-efficient-deep-learning/16-quantum-machine-learning.md#compiling-for-a-real-device).

### [1:16:00–1:18:45](https://www.youtube.com/watch?v=svjjD2uthhQ&t=4560) Compilation as a graph cut

Because arrays can always be moved together, the device's coupling graph is complete between arrays. So the graph of two-qubit gates is cut into as many parts as there are arrays, a max-k-cut, and atoms are assigned so that the two qubits of a gate sit in different arrays, which the movement of the atoms brings together, so fewer SWAPs are needed. Earlier compilers cast the whole problem as a satisfiability problem for an SMT solver, optimal but exponential; Atomique compiles circuits on over a thousand qubits within minutes and also reports how fast atoms must move, guidance for future devices.
**In this book:** [Quantum Machine Learning › How it works, step by step › Compiling for a real device](../09-efficient-deep-learning/16-quantum-machine-learning.md#compiling-for-a-real-device).

### [1:18:45–1:24:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=4725) Summary, and questions

Wang recaps: qubits and their exponential state space, single- and multi-qubit gates, circuits for an adder and for machine learning, the NISQ era, and compilers for superconducting and neutral-atom devices; the next lecture adds advanced quantum models and methods that use device noise to improve robustness and scale. Asked whether the lab influences device makers, he says one of its compilers is a default in IBM's software ecosystem, that devices will have to be co-designed with error-correcting codes, that the lab's TransformerQEC preceded AlphaQubit, and that it works with William Oliver's group at MIT on qubit placement.
**In this book:** nothing beyond this guide; nearest: [Quantum Machine Learning › Key takeaways](../09-efficient-deep-learning/16-quantum-machine-learning.md#key-takeaways).

## What to take away

- Efficient AI is a full-stack design problem shared by algorithms and systems, the thread of the whole course.
- A qubit holds a superposition of two complex amplitudes, n qubits hold 2 to the n, and measurement collapses that space to classical bits.
- Gates are reversible rotations; Hadamard creates superposition and CNOT creates entanglement, which correlates outcomes without transmitting information.
- Today's devices are few, noisy and constrained in connectivity; mapping and movement, chosen well, bring algorithms closer to running on them.

## Sources

- Song Han and Hanrui Wang, "Course Summary + Quantum Machine Learning I", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=svjjD2uthhQ).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
