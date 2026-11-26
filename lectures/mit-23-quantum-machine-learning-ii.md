# Lecture guide: Quantum Machine Learning II

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 23 · **Length:** 1:14:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=ZDk-GsyInt8) · **Slides:** [slides](https://www.dropbox.com/scl/fi/wxpnpwkrl6pw7lb4n4vrg/Lec23-Quantum-ML-II.pdf?rlkey=21msd9zdilhry5pydlkvbn7n4&st=aoyc9pzv&dl=0)
**Chapters that cite this lecture:** [11. Course Summary and Outlook](../09-efficient-deep-learning/11-course-summary-and-outlook.md)

> **In one sentence:** Hanrui Wang's second lecture builds quantum machine learning: what makes a parameterized quantum circuit expressive, how to encode data into it, how to train it on real noisy hardware with the parameter-shift rule, gradient pruning and SPSA, the TorchQuantum library, and a search for circuit architectures that stay reliable under noise.

## Before you watch

The lecture is given by Hanrui Wang, as the first quantum lecture was; it assumes that lecture's qubits, gates and circuits. The chapter [Course Summary and Outlook](../09-efficient-deep-learning/11-course-summary-and-outlook.md) lists quantum machine learning among the course's open questions; the material itself is not taught elsewhere in this book. The architecture-search and pruning lectures of the course return here in quantum form.

## The lecture, part by part

### [0:00–2:30](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=0) Plan, and a taxonomy

The plan: parameterized quantum circuits, how to train them for tasks such as classification, noise-aware on-chip training for robustness, the TorchQuantum library, and choosing the most reliable circuit architecture. Wang sorts the field by two dimensions, the algorithm (quantum or classical) and the data (quantum or classical). Classical data with classical algorithms is ordinary deep learning; quantum data with classical algorithms is device control and calibration; quantum data with quantum algorithms includes sensing with qubits. This lecture stays with classical data processed by quantum algorithms.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: from data to a circuit](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-from-data-to-a-circuit).

### [2:30–6:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=150) Parameterized circuits and expressivity

A parameterized quantum circuit mixes gates with tunable angles, such as an RX gate whose rotation is learned, with fixed gates such as CNOT, X and H, much as a classical network mixes weighted layers with parameterless ones. A key property is expressivity: how much of the state space the circuit can reach. Circuit A, a Hadamard and a rotation about Z, traces only a ring on the Bloch sphere as its angle varies; circuit B adds an RX gate and, with random angles, covers the sphere. More parameters, more representational power.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: from data to a circuit](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-from-data-to-a-circuit).

### [6:00–10:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=360) Measuring expressivity and entangling capacity

Expressivity has a rigorous measure. The reference is the Haar distribution over arbitrary states: sample many pairs of random states and record their infidelity. Do the same for states a circuit produces with random parameters, and compare the two distributions by KL divergence. An idle circuit always returns one state, a spike of perfect fidelity and a huge divergence; a circuit reaching any unitary nearly matches the reference. Lower divergence means higher expressivity. Entangling capacity is measured by the Meyer-Wallach measure, between 0 for a product state and 1 for fully entangled qubits, averaged over parameters: a circuit with only single-qubit gates scores zero.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: from data to a circuit](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-from-data-to-a-circuit).

### [10:00–14:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=600) What the measures show

Plotted over the number of layers, the first circuit never entangles, while a circuit rich in CNOTs between neighbouring qubits reaches high entangling capacity within a few layers. Entanglement matters because only entangled qubits use the exponential Hilbert space to store data. Asked why deeper is needed once capacity saturates, Wang attributes it to sampling noise in the measure: a few layers suffice for entangling, whereas expressivity keeps improving with parameters.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: from data to a circuit](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-from-data-to-a-circuit).

### [14:00–16:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=840) Hardware efficiency, and basis encoding

A circuit must also run on a device: it should respect qubit connectivity, placing its qubits so that most two-qubit gates join neighbours, and use native gates, since decomposing an unsupported gate adds many operations and much error. Encoding comes next, in four ways. Basis encoding treats a binary string as a basis state, so the number 2 becomes |10⟩. Encoding one value wastes the space; several values can share it as a superposition, |00⟩ + |11⟩ for the vector (0, 3), made with a Hadamard and a CNOT.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: from data to a circuit](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-from-data-to-a-circuit).

### [16:00–20:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=960) Amplitude encoding

Amplitude encoding writes the input vector straight into the state vector, so two qubits hold four features and n features need only log base 2 of n qubits. Asked whether the vector must have unit length, Wang answers yes: normalize it first and keep the normalization factor on a classical device. The price is state preparation: every qubit starts in |0⟩, and even preparing four chosen numbers takes a long circuit of gates.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: from data to a circuit](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-from-data-to-a-circuit).

### [20:00–22:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1200) Angle encoding, and arbitrary encoding

Angle encoding stores each value in a rotation angle, one RX gate per qubit for a vector such as (0, π/2, π). It needs no state-preparation circuit: the values simply become the gate angles, which makes it efficient. Arbitrary encoding combines methods: a layer of rotations, a layer of CNOTs to entangle, and another layer of rotations, which packs twelve values into one circuit.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: from data to a circuit](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-from-data-to-a-circuit).

### [22:00–26:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1320) Training, and the parameter-shift rule

Training resembles classical deep learning: preprocess and encode the data, pass it through trainable circuit layers, and iterate on a cost such as cross-entropy. Gradients by finite differences depend on the step size, a poor choice giving a derivative far from the truth. The parameter-shift rule gives the analytic gradient: evaluate the circuit with the angle shifted by π/2 and again by −π/2; half the difference is the derivative. The intuition is periodicity: shifting a cosine by π/2 yields its derivative, the sine, and rotation gates decompose into sines and cosines.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [26:00–30:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1560) Backpropagation or parameter shift

On a simulator, backpropagation through the circuit gives the same analytic gradients; Wang's plots show it agreeing with the parameter-shift rule. But backpropagation needs every intermediate state, which only a simulator has. On a real device the intermediate quantum states cannot be read, so backpropagation is impossible there, while the parameter-shift rule needs nothing but final measurement outcomes and therefore works on hardware.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [30:00–34:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=1800) Training on a real device

The full loop on hardware runs the circuit without shifts to obtain the measured values, computes the classical part, softmax and cross-entropy, and backpropagates that part to get the loss's derivative with respect to the measurements. The device supplies the derivative of each measurement with respect to each angle by the parameter-shift rule. The chain rule joins the two into the gradient of the loss with respect to every angle, which then updates the parameters. A student notes the cost: two runs per parameter.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [34:00–38:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2040) SPSA, and natural gradients

Wang agrees: circuit runs grow linearly with the number of parameters, 2n for n parameters, as training cost does in classical learning. SPSA, simultaneous perturbation stochastic approximation, lowers the constant: perturb every parameter at once by small random signs, evaluate once with plus and once with minus, and give each parameter a gradient of equal magnitude whose sign follows its perturbation. One round then estimates all gradients, and its training curve tracks vanilla gradient descent. The quantum natural gradient converges best of all, at a much higher cost.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [38:00–40:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2280) Barren plateaus

Deep circuits face a barren plateau: with many qubits and layers, the variance of the gradients of early layers falls exponentially, so they cannot be updated and circuits cannot be stacked deep. Asked about residual connections, Wang says analogous bypasses work poorly, because the no-cloning theorem forbids copying an intermediate quantum state to carry it forward as a classical network copies activations.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › What the course leaves open](../09-efficient-deep-learning/11-course-summary-and-outlook.md#what-the-course-leaves-open).

### [40:00–44:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2400) Other uses of parameterized circuits

The classifier from the previous lecture is recast: angle encoding of pixels, trainable U3 and controlled-U3 layers, trained by SPSA or finite differences, then measurement and classical post-processing. The same circuits serve other tasks. The variational quantum eigensolver searches for the smallest eigenvalue of a matrix by tuning the circuit to prepare the corresponding eigenstate; applied to a molecule's Hamiltonian, it gives the ground-state energy and so the stable bond lengths of a chemical reaction. QAOA, the quantum approximate optimization algorithm, attacks combinatorial optimization.
**In this book:** nothing beyond this guide; nearest: [Course Summary and Outlook › What the course leaves open](../09-efficient-deep-learning/11-course-summary-and-outlook.md#what-the-course-leaves-open).

### [44:00–50:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2640) Noise-aware training: prune unreliable gradients

Gradients computed by parameter shift on an IBM device lose accuracy to noise, leaving a gap from simulated training. The observation: a small gradient has a large relative error, since slight noise flips its direction, while a large one keeps its sign. So prune unreliable gradients. Probabilistic gradient pruning accumulates the absolute gradient of each parameter over a window of a few steps, sorts them, and updates only the parameters with large values. It raises accuracy by 5 to 10% on a classification task and halves training time, because unreliable gradients are never computed.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [50:00–52:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3000) Why train on-chip

Against the number of hardware evaluations, on-chip training with pruning closes most of the gap between noisy training and the ideal curve. It also scales: a classical simulator pays time and memory that grow exponentially with qubits, since the state vector does, whereas the device itself does not. Pruning probabilistically, with larger gradients more likely to be kept but none dropped for ever, beats deterministic pruning by 1 to 9% accuracy across tasks.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [52:00–58:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3120) TorchQuantum

Google pairs TensorFlow with TensorFlow Quantum; the lab built TorchQuantum on PyTorch, aiming for speed, convenience, portability through common quantum representations, scalability, GPU acceleration, density-matrix support and converters to other frameworks. PyTorch's dynamic graphs ease debugging. A model is a PyTorch module: it creates a quantum device with a given number of qubits, lists encoder gates and trainable gates, and in its forward pass resets the state, encodes the pixels, applies the gates and measures; any classical layers may follow the measurement before the softmax. Gates can be applied in three styles, including functional calls like PyTorch's own. Macros cover amplitude and phase encoding, converters export to Qiskit for IBM's devices, and the library is at torchquantum.org.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [58:00–1:02:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3480) Searching for a robust circuit

Which circuit suits a task? Gate types, counts and positions make a vast design space. Training each candidate, as random search does, is costly. QuantumNAS trains once and uses many times: build a supercircuit large enough to contain the candidates, train it, search noise-aware for a subcircuit and its qubit mapping by evolutionary search, train that subcircuit from scratch, then prune it.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3720) Training the supercircuit

Each training step samples one subcircuit and updates its parameters once, so that after enough steps every subcircuit has been trained equally. Inherited weights are less accurate than training from scratch, but they preserve ranking: the loss of a subcircuit with inherited weights correlates positively with its loss when trained from scratch, and ranking is all the search needs. Asked whether the barren plateau persists, Wang says it does; the method is orthogonal to it, though the search can be restricted to circuits immune to it.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [1:06:00–1:10:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3960) Search and pruning on the device

An evolutionary or reinforcement-learning search then samples subcircuits and evaluates them on the real device until the best is found. Pruning follows as in the classical course: a gate whose angle is near zero acts as the identity and can be dropped without effect, leaving a circuit with only its essential gates. Asked about scale, Wang notes that the supercircuit, the subcircuits and the search can all run on the quantum device through the parameter-shift rule, so nothing requires exponential classical simulation.
**In this book:** [Course Summary and Outlook › What the course treats as the frontier › Quantum machine learning: training on noisy devices](../09-efficient-deep-learning/11-course-summary-and-outlook.md#quantum-machine-learning-training-on-noisy-devices).

### [1:10:00–1:14:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=4200) Other search methods, and a summary

Other frameworks train a predictor, for instance a graph neural network, of a subcircuit's performance, encode a circuit as a grid image, or let a reinforcement-learning agent add or remove layers and learn from the device's reward; differentiable and proxy-based searches exist too. Wang closes by recapping: parameterized circuits and their training, a simple classifier, noise-aware gradient pruning, the TorchQuantum library, and QuantumNAS for robust architectures.
**In this book:** nothing beyond this guide; nearest: [Course Summary and Outlook › What the course leaves open](../09-efficient-deep-learning/11-course-summary-and-outlook.md#what-the-course-leaves-open).

## What to take away

- A circuit's value shows in expressivity, how close its reachable states come to all states, and in entangling capacity; both must respect native gates and connectivity.
- Angle encoding avoids costly state preparation; amplitude encoding saves qubits but not gates.
- On hardware, gradients come from the parameter-shift rule, costly at two runs per parameter, or from SPSA's one-round estimate; deep circuits hit barren plateaus that skip connections cannot cure.
- Noise makes small gradients unreliable: prune them, train on-chip, and search for the subcircuit that stays accurate.

## Sources

- Song Han and Hanrui Wang, "Quantum Machine Learning II", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=ZDk-GsyInt8).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
