# Lecture guide: Pruning and Sparsity (Part II)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 4 · **Length:** 1:10:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=upaZrpXkELc) · **Slides:** [slides](https://www.dropbox.com/scl/fi/w5baiyci5cxl1ozpy6lsr/Lec04-Pruning-II.pdf?rlkey=6qxc1nz20isy9izwnqfebtukg&st=59gy1eal&dl=0)
**Chapters that cite this lecture:** [03. Pruning and Sparsity](../09-efficient-deep-learning/03-pruning-and-sparsity.md) · [11. Course Summary and Outlook](../09-efficient-deep-learning/17-course-summary-and-outlook.md)

> **In one sentence:** Song Han finishes pruning: how to choose a pruning ratio for each layer (sensitivity analysis, the reinforcement-learning agent AMC, NetAdapt), how to fine-tune, and how hardware from the Efficient Inference Engine to sparse tensor cores, TorchSparse and PointAcc runs sparse networks.

## Before you watch

The chapter [Pruning and Sparsity](../09-efficient-deep-learning/03-pruning-and-sparsity.md) gathers both pruning lectures into five steps; this lecture covers steps three to five. The first lecture's vocabulary (granularity, criterion) is assumed, and the systems half needs no hardware background beyond knowing that memory is slower than arithmetic.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=0) Recap: what pruning removes

Han reviews the first lecture. Pruning turns a dense network into a sparse one to save computation and memory, formulated as minimizing the loss subject to a bound on non-zero weights. Granularity runs from fine-grained, most free and most irregular, to channel pruning, regular but with fewer weights removed. Magnitude picks the weights to drop. Removing a neuron or a channel also removes every weight attached to it. The open question of this lecture: how much to prune in each layer, then how to fine-tune, and how hardware can run sparse networks.
**In this book:** [Pruning and Sparsity › Step 1: Choose the granularity](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-1-choose-the-granularity).

### [4:00–8:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=240) Sensitivity analysis

Non-uniform pruning, a different ratio per layer, beats uniform pruning: on a plot of latency against accuracy, its curve lies closer to the top-left corner every designer wants. To find the ratios, sensitivity analysis prunes one layer at a time, from 10% up to 90%, and measures accuracy. Repeated for every layer, it yields one curve per layer: some collapse early, others barely move at 60% pruned.
**In this book:** [Pruning and Sparsity › Step 3: Choose the ratio for each layer](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-3-choose-the-ratio-for-each-layer).

### [8:00–10:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=480) Reading the curves

The curves double as a sanity check: accuracy should not move at small ratios and should be very low at large ones, otherwise the code or the granularity is wrong. The measurements are taken before retraining and assume layers are independent; Han acknowledges that layers can be co-sensitive, which the method ignores because otherwise the computation would be too much. A simple heuristic follows: pick an accuracy loss to tolerate, 5% or 10%, and read off each layer's ratio where its curve crosses it.
**In this book:** [Pruning and Sparsity › Step 3: Choose the ratio for each layer](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-3-choose-the-ratio-for-each-layer).

### [10:00–14:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=600) Automating the choice: AMC

The heuristic is not optimal, since it ignores interactions between layers. It also scales badly: a company with many models, for cars, driver monitors and more, cannot assign an engineer to each. AutoML for Model Compression, AMC, makes the choice with reinforcement learning, an actor-critic method with a DDPG agent. It walks the layers like a game: the state is the layer's index, channel count, kernel size and accumulated operations; the action is a continuous pruning ratio between 0 and 1; the model is then fine-tuned and the reward is minus the error, multiplied by the logarithm of the operation count so that fewer operations also earn reward.
**In this book:** [Pruning and Sparsity › Step 3: Choose the ratio for each layer](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-3-choose-the-ratio-for-each-layer).

### [14:00–16:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=840) What the agent found

Pruning ResNet-50 at equal accuracy, a human expert, Han himself in 2017, left 29% of weights in place after about a week of work on four old GPUs in a single server; the agent left 20% after a few GPU hours. Its policy is explainable. Plotted layer by layer over four rounds of gradual pruning, the density forms a regular zigzag: 1 by 1 convolutions keep more weights, having less redundancy, while 3 by 3 convolutions are pruned harder.
**In this book:** [Pruning and Sparsity › Step 3: Choose the ratio for each layer](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-3-choose-the-ratio-for-each-layer).

### [16:00–18:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=960) From ratios to a faster phone

On a Samsung phone, MobileNet 1.0 ran at 569 million MACs, 70.6% top-1 accuracy, 119 milliseconds and 20 megabytes. Told to halve the operations, AMC produced a model with 285 million MACs, nearly the same accuracy (70.5% against 70.6%), 1.8 times lower latency and 14.3 megabytes. Given a target latency instead, 59.7 milliseconds, it found the most accurate model that meets it, something hard to design by hand. Uniformly shrinking every layer does worse on both counts.
**In this book:** [Pruning and Sparsity › Step 3: Choose the ratio for each layer](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-3-choose-the-ratio-for-each-layer).

### [18:00–22:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=1080) NetAdapt: a rule-based search

NetAdapt, from Google, reaches per-layer ratios by rule. Define a small latency step. For each layer in turn, prune it just enough to save that step, fine-tune briefly, and measure accuracy; since every candidate saves the same latency, keep the layer that lost the least accuracy. Repeat until the target latency is met, then fine-tune the whole model for long. The short fine-tuning runs inside the loop many times and must be cheap; the final one runs once and can be thorough. A by-product is a family of models along the latency-accuracy curve, better than applying one multiplier to all layers. Han expects the idea to carry over to large language models, whose layers can be treated as roughly independent.
**In this book:** [Pruning and Sparsity › Step 3: Choose the ratio for each layer](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-3-choose-the-ratio-for-each-layer).

### [22:00–28:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=1320) Fine-tuning the pruned network

Before the systems half, Han covers fine-tuning. It recovers up to 2.5% of accuracy; the learning rate should usually drop 10 to 100 times, though it depends on the case, because the model already sits near a good minimum. Iterative pruning, 30% then 50% then 70% with fine-tuning between steps, beats pruning 70% at once, and raised AlexNet's compression from 5 times to 9 times. Regularization during fine-tuning pushes weights toward zero; L1 and L2 differ little in his experience, his 2015 work used L2 and Network Slimming used L1 on channel scales, so compare them. He then sums up the algorithm half and takes a break.
**In this book:** [Pruning and Sparsity › Step 4: Fine-tune, a little at a time](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-4-fine-tune-a-little-at-a-time).

### [28:00–32:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=1680) The Efficient Inference Engine: three sources of savings

Three systems follow: EIE for weight and activation sparsity, sparse tensor cores for 2:4 sparsity, and TorchSparse with a point-cloud accelerator for activation sparsity. EIE, the Efficient Inference Engine, compresses a model before running it instead of deploying the dense one, since memory traffic costs more than arithmetic. It exploits weight sparsity: at 90% sparsity computation falls ten times and memory only five, because indices must be stored; activation sparsity, about 70% of zeros after ReLU, dynamic with the input, which saves about three times the computation and no weight memory; and 4-bit weights, found sufficient with weight sharing, four times smaller than FP16.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [32:00–38:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=1920) Inside EIE

Han showed in 2016 that 4 bits suffice for weights, and the same holds for modern language models such as Llama 2 and Llama 3 with weight-only quantization. On the hardware side, a pruned matrix is stored in compressed sparse column form: only non-zero weights, each with its relative distance to the previous non-zero, plus pointers to where each column starts; the work is split over several processing elements. At run time zeros in the activation are skipped and each non-zero activation is broadcast to the elements, which multiply and accumulate. One element holds an activation queue of non-zeros only, uses the activation's position to fetch weights from the sparse matrix in SRAM, decodes 4-bit codes to 16-bit values through a k-means codebook, and ends with a unit that detects non-zero outputs for the next layer. Because compression makes weights small enough for SRAM instead of DRAM, energy and delay fall. Fully connected layers needed ten to thirty-three times fewer operations; LSTMs gained less, as their activations are dense without ReLU.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [38:00–42:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=2280) What counts as worth accelerating

His rule of thumb: an acceleration is worth engineering only if the theoretical reduction exceeds ten times. EIE, the first work to use weight sparsity to speed up networks, brought large gains in throughput and energy efficiency, and was listed among the five most exciting papers in fifty years of ISCA, the computer architecture conference, alongside Google's TPU paper; two of the five were only seven years old.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [42:00–46:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=2520) A retrospective: what lasted

Invited seven years later to write a retrospective, Han lists what succeeded: special-purpose hardware made sparse operations cheap even at 50% density; EIE used both weight and activation sparsity and fine-grained patterns; and its weight-only quantization, 4 bits in memory decoded to 16-bit arithmetic, now called W4A16, was reborn in language models through GPTQ, AWQ, llama.cpp and MLC. What did not: the design did not scale to arrays of processors, for which the suggested improvement is structured sparsity such as 2:4; control flow and storage were heavy, since every non-zero needs pointers and indices, which coarser pruning relieves; and it served fully connected layers, a limit that matters less now that transformers are all fully connected. Fitting everything in SRAM suited TinyML, yet startups now chain SRAM-only chips with pipeline parallelism to run large models.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware) · [Course Summary and Outlook › What the course leaves open](../09-efficient-deep-learning/17-course-summary-and-outlook.md#what-the-course-leaves-open).

### [46:00–48:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=2760) Be lazy

His lesson from the work is a one-line motto: "First principle of efficient AI is to be lazy." Avoid redundant computation, reject work quickly when a value is zero, use fewer bits, or delay the work. Each domain has its own opening: image editing needs only the edited region; language has redundant tokens, so attention can be sparse; video has temporal redundancy, so a simple shift can model the temporal dimension instead of 3D convolution; point clouds are mostly empty space.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [48:00–52:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=2880) Sparse tensor cores for 2:4 sparsity

NVIDIA's sparse tensor cores accelerate 2:4 weight sparsity. In an 8 by 8 matrix with two non-zeros per group of four, the payload shrinks to four values per row; each non-zero needs two bits to say which of four slots it came from, so the metadata costs one byte per row. At run time the indices select the matching entries of the activation matrix, and only those are multiplied. The theoretical speed-up is two; measured, it is about 1.9 for large matrices and 1.2 to 1.3 for small ones. Accuracy holds from dense FP16 through sparse FP16 to sparse INT8, which shows sparsity and quantization combine well.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [52:00–56:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=3120) Sparse convolution keeps the pattern

Activation sparsity comes next, with TorchSparse and an accelerator named PointAcc. Ordinary convolution dilutes sparsity: a sparse input spreads out, and after a few layers the feature map is dense. Sparse convolution computes an output only where the input is non-zero, so input and output share the same pattern of non-zeros. In his 3 by 3 example the dense form needs nine matrix multiplications and the sparse form two, each over the channel dimension.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [56:00–1:02:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=3360) The rule map, and adaptive grouping

The kernel needs a rule map between input, output and weights, built weight by weight: for each weight position, a list of input-output pairs that interact. The workloads differ greatly from one weight position to another, five multiplications for one and one for another, which unbalances the GPU. Adaptive grouping gathers matrix multiplications of similar size into batches. Three designs trade wasted computation against regularity: no padding wastes nothing but leaves threads out of step; padding everything to the largest wastes most and is perfectly regular; grouping by similar size sits between, and about six groups gave the best speed-up in his sweep. The right grouping depends on the sparsity pattern, hence algorithm-hardware co-design. Fixed grouping sometimes reports higher TFLOPS, but part of that work is redundant, and adaptive grouping is faster end to end.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [1:02:00–1:04:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=3720) TorchSparse++: sort neighbours together

TorchSparse++ overlaps memory access with computation, for 3D perception in autonomous driving, with a kernel generator and an auto-tuner. Its trick is reordering: adjacent outputs are computed in parallel, so a neighbour's work is padded into each; treating each output's pattern as a binary number and sorting outputs by it puts similar patterns side by side, cutting redundant multiplications from 12 to 10 in his example, and splitting channels reduces them further, to 8, at a small cost in sorting.
**In this book:** [Pruning and Sparsity › What the practitioners say](../09-efficient-deep-learning/03-pruning-and-sparsity.md#what-the-practitioners-say).

### [1:04:00–1:06:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=3840) PointAcc: the rule map in hardware

PointAcc moves the rule map into a specialized accelerator. For a weight at offset (−1, −1), the input point cloud is shifted by adding the reverse offset, here (1, 1), to every index; the shifted input and the output are merge-sorted, and a hardware intersection unit finds the indices present in both. Those pairs are the interactions of that weight. The accelerator is much faster and more energy-efficient than CPU or GPU.
**In this book:** [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

### [1:06:00–1:10:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=3960) Summary

Han recaps the lecture in two halves. Algorithms: pruning ratios by sensitivity analysis, by the reinforcement-learning agent AMC and by NetAdapt's rules, plus good fine-tuning practice. Systems: hardware for each granularity, EIE for fine-grained sparsity, sparse tensor cores for 2:4, TorchSparse and PointAcc for sparse activations. The next lecture starts quantization: FP16, FP8, FP4, INT8 and INT4, and common methods. Lab 1 is released.
**In this book:** nothing beyond this guide; nearest: [Pruning and Sparsity › Step 5: Match the hardware](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-5-match-the-hardware).

## What to take away

- Layers tolerate different pruning ratios: measure each layer's sensitivity or let a search such as AMC or NetAdapt choose, and prune gradually with fine-tuning between steps.
- Fine-grained sparsity compresses most but costs indices and control flow; 2:4 sparsity gives up half of that for hardware that can skip known slots.
- EIE's weight-only 4-bit storage with 16-bit arithmetic returned years later as a popular way to run language models.
- Be lazy: avoid work, skip zeros, use fewer bits, delay what can wait.

## Sources

- Song Han, "Pruning and Sparsity (Part II)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=upaZrpXkELc).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
