# Lecture guide: Neural Architecture Search (Part II)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 8 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=5ty12mNV4Sg) · **Slides:** [slides](https://www.dropbox.com/scl/fi/kaia5vvmdwb2bj0xnbihm/Lec08-Neural-Architecture-Search-II.pdf?rlkey=vkp9i12ljbk4jmdfp05j3ctdy&st=hincmob7&dl=0)
**Chapters that cite this lecture:** [05. Neural Architecture Search](../09-efficient-deep-learning/05-neural-architecture-search.md)

> **In one sentence:** Song Han continues architecture search: how to estimate accuracy cheaply, why FLOPs mislead and measured latency must drive the search (ProxylessNAS), how one once-for-all network yields a model for every device, how the accelerator can be searched together with the network, and how far the once-for-all idea spreads, from GANs to quantum circuits.

## Before you watch

The chapter [Neural Architecture Search](../09-efficient-deep-learning/05-neural-architecture-search.md) covers this lecture in its last three steps: estimating performance, hardware awareness and once-for-all training. The first lecture's search spaces and strategies are assumed.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=0) Plan

The last of the two lectures on architecture search. The goal stands: design an accurate model from scratch with low latency, low energy and small storage, after the previous lecture's building blocks, search spaces and search strategies. Today: estimating performance quickly, hardware awareness, searching without training, searching the hardware architecture together with the network, and applications from language models to point clouds.
**In this book:** [Neural Architecture Search › Step 4. Estimate performance without paying full price](../09-efficient-deep-learning/05-neural-architecture-search.md#step-4-estimate-performance-without-paying-full-price).

### [2:00–4:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=120) Training from scratch is too expensive

Accuracy can be estimated the plain way: train each candidate to convergence and measure it on the validation set. On CIFAR-10 alone this meant training tens of thousands of models for 22,000 GPU hours, and what counts as large scale today is trillions of tokens. It does not scale.
**In this book:** [Neural Architecture Search › Step 4. Estimate performance without paying full price](../09-efficient-deep-learning/05-neural-architecture-search.md#step-4-estimate-performance-without-paying-full-price).

### [4:00–6:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=240) Inheriting weights: Net2Net

A cheaper way changes the architecture of a trained model while keeping it mathematically equal. Net2WiderNet widens a layer by replicating a hidden neuron and halving weights; Net2DeeperNet deepens the network by inserting a layer initialized as the identity mapping. No retraining is needed, and a search controller can use these two moves as its actions while inheriting the parent's weights.
**In this book:** [Neural Architecture Search › Step 4. Estimate performance without paying full price](../09-efficient-deep-learning/05-neural-architecture-search.md#step-4-estimate-performance-without-paying-full-price).

### [6:00–8:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=360) Hypernetworks

A hypernetwork is a network that generates another network's weights. Each layer gets an embedding from its features (channels, width, height, kernel size); a graph network refines the embeddings by passing information along the connectivity; and a shared multilayer perceptron turns a node embedding into that layer's weights, trained by gradient descent. Han mentions it as an idea that is not widely used.
**In this book:** [Neural Architecture Search › Step 4. Estimate performance without paying full price](../09-efficient-deep-learning/05-neural-architecture-search.md#step-4-estimate-performance-without-paying-full-price).

### [8:00–10:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=480) One model per platform

A general model is inefficient because platforms differ: a Raspberry Pi with little memory, a GPU with much memory and parallelism, a CPU with less, a phone with a battery. Each would do best with its own model, and designing them by hand does not scale. Earlier searches were too costly to repeat: NASNet is listed at tens of thousands of GPU hours for CIFAR, and DARTS at hundreds of gigabytes of memory on ImageNet.
**In this book:** [Neural Architecture Search › Step 5. Make it hardware-aware](../09-efficient-deep-learning/05-neural-architecture-search.md#step-5-make-it-hardware-aware).

### [10:00–12:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=600) Proxy tasks, and why they mislead

Earlier work searched on a proxy: a smaller dataset such as CIFAR-10 instead of ImageNet, a smaller space with one repeated block, a few epochs instead of full training, and FLOPs and parameter counts instead of measured latency. Each proxy misleads: models that win on CIFAR-10 may lose on ImageNet; first and last layers may not want the same block; a model that starts fast may not converge best; and FLOPs do not translate into speed.
**In this book:** [Neural Architecture Search › Step 5. Make it hardware-aware](../09-efficient-deep-learning/05-neural-architecture-search.md#step-5-make-it-hardware-aware).

### [12:00–18:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=720) ProxylessNAS

Han's group searches directly on the target task and target hardware. Each layer has several candidate operations, and besides the weights the network learns an architectural parameter for each: the probability of choosing that operation, the probabilities summing to one. Inference keeps only the most probable path, and during training too the activations are binarized so that one path is active; memory is then constant in the number of choices instead of growing with it. Searching costs about one ordinary training run, so ImageNet can be used directly, the space can be large, training can run to the end, and real latency can replace FLOPs.
**In this book:** [Neural Architecture Search › Step 5. Make it hardware-aware](../09-efficient-deep-learning/05-neural-architecture-search.md#step-5-make-it-hardware-aware).

### [18:00–20:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=1080) FLOPs mislead

A warning against FLOPs, measured on a Google Pixel-1: MobileNet has fewer MACs than MobileNetV2, about 550 against 580 million, yet a latency of 190 milliseconds against under 150. On a GPU, shrinking the hidden dimension barely changes latency, because the GPU is not saturated, while adding layers changes it in proportion.
**In this book:** [Neural Architecture Search › Step 5. Make it hardware-aware](../09-efficient-deep-learning/05-neural-architecture-search.md#step-5-make-it-hardware-aware).

### [20:00–24:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=1200) Latency as the reward, and a predictor

The same change behaves differently per platform: on a Raspberry Pi the hidden dimension does matter. So latency, measured on the target hardware, should be the reward. Measuring is slow, and a farm of phones is expensive, so a latency predictor is learned from a dataset of architectures and their measured latencies. The simplest is a lookup table: profile every operator once, then add the per-layer latencies; estimated against real latency follows the diagonal. A regression on layer features (tensor shape, kernel size) does as well, also for transformers in the hardware-aware transformer work.
**In this book:** [Neural Architecture Search › Step 5. Make it hardware-aware](../09-efficient-deep-learning/05-neural-architecture-search.md#step-5-make-it-hardware-aware).

### [24:00–26:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=1440) Kernel fusion, and the result

Summing per-layer latencies ignores kernel fusion, which frameworks such as TensorRT apply behind the scenes. Han's rule of thumb: a compute-bound kernel followed by a memory-bound one, a matrix multiplication followed by a nonlinearity, can fuse; two compute-bound kernels in a row gain nothing. The payoff: against MobileNetV2, a hand-designed mobile model, the specialized search gives about 80% higher speed with a better accuracy-latency trade-off.
**In this book:** [Neural Architecture Search › Step 5. Make it hardware-aware](../09-efficient-deep-learning/05-neural-architecture-search.md#step-5-make-it-hardware-aware).

### [26:00–28:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=1560) Specialization shows in the architecture

Searched separately for GPU, CPU and mobile, the models differ, and each runs fastest on its own platform. After convergence the GPU model is shallow and wide, with many 7 by 7 kernels, since each kernel call is costly and parallelism is abundant; the CPU model is deeper and narrower and uses only 3 by 3 and 5 by 5 kernels. An animation from one shared initialization shows the architectures drifting apart as training proceeds.
**In this book:** [Neural Architecture Search › Step 5. Make it hardware-aware](../09-efficient-deep-learning/05-neural-architecture-search.md#step-5-make-it-hardware-aware).

### [28:00–34:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=1680) Train once, get many

Searching anew for every chip is too costly. The once-for-all approach trains a single network that contains many sub-networks; a search samples a sub-network, measures its latency and accuracy, and if it does not fit, samples another instead of retraining. One training serves many searches and yields about 10 to the 19 sub-networks, each sparsely activated and sharing weights. A large sub-network goes to an H100, a middle one to a consumer GPU, a small one to a mobile GPU; one training could give language models of 3, 7 and 70 billion parameters, versions for new and old phones, or a tiny model for battery-saving mode.
**In this book:** [Neural Architecture Search › Step 6. Train once for many devices: once-for-all](../09-efficient-deep-learning/05-neural-architecture-search.md#step-6-train-once-for-many-devices-once-for-all).

### [34:00–40:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=2040) How the once-for-all network is built

Four dimensions are made elastic while weights are shared. Kernel size: the centre of a 7 by 7 kernel, through a learned transformation matrix, serves as the 5 by 5, whose centre serves as the 3 by 3, so 49 weights cover all three instead of 83. Depth: a block of four layers can run with three or two by letting the output skip layers. Width: channels are sorted by importance and the first few kept. Resolution: sampled at random per batch, which changes the workload but not the weights. A student asks whether training the small models ruins the large one; Han answers that large and small are sampled in turn, so the large one is not destroyed, and confirms that training a small one still updates the shared weights.
**In this book:** [Neural Architecture Search › Step 6. Train once for many devices: once-for-all](../09-efficient-deep-learning/05-neural-architecture-search.md#step-6-train-once-for-many-devices-once-for-all).

### [40:00–44:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=2400) Roofline, and results across hardware

A roofline chart plots realized operations per second against arithmetic intensity, operations per byte moved: performance rises with intensity while memory-bound, then flattens at the hardware's peak. The once-for-all network sits further up and to the right than MnasNet and MobileNetV2, doing more work per byte and reaching more operations per second. Sampled sub-networks also trace better latency-accuracy curves on many phones, on GPU, CPU and FPGA. Lab 3 hands students a trained once-for-all network to sample from.
**In this book:** [Neural Architecture Search › Step 6. Train once for many devices: once-for-all](../09-efficient-deep-learning/05-neural-architecture-search.md#step-6-train-once-for-many-devices-once-for-all).

### [44:00–50:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=2640) Zero-shot NAS: judging an architecture without training

Can an architecture be judged without any training? Han presents heuristics on randomly initialized networks. One, ZenNAS, scores a network by how much a small perturbation of the input changes the output and by the variance of its batch-normalization statistics: a good network responds to its input. Another, GradSign, rests on the idea that a good network has densely packed local minima, so gradients computed on different samples should mostly share a sign; counting matching signs is cheap. Of the first, Han says it is a coarse check, since weights matter too, yet reports that it works quite well, at least in that paper.
**In this book:** [Neural Architecture Search › How it works, step by step › Step 4: Estimate performance without paying full price](../09-efficient-deep-learning/05-neural-architecture-search.md#step-4-estimate-performance-without-paying-full-price).

### [50:00–1:02:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=3000) Searching the accelerator too

When the chip itself can be designed, hardware, network and the compiler mapping between them can be searched together, in one evolutionary loop, in a method called NAAS for neural accelerator architecture search, that minimizes the energy-delay product. The hardware space covers buffer sizes, the number of processing elements and their connectivity; the compiler's covers loop order, tiling and data flow; the network's covers layers, channels, kernels and precision. Choices such as which dimension to parallelize in space or in which order to loop are not numbers, so the method gives each dimension an importance value, sorts them, parallelizes the most important ones in space and runs the least important in the innermost loop. Sizing alone improved the energy-delay product by about a fifth, or by 2.1 times as Han also puts it; searching connectivity as well, and the network with it, improved it further, and the found data flow differed from a designer's.
**In this book:** [Neural Architecture Search › What the practitioners say](../09-efficient-deep-learning/05-neural-architecture-search.md#what-the-practitioners-say).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=3720) Application: transformers, and a chip

The once-for-all idea carries over to transformers: one large network with many sub-networks gives small models for devices and large ones for GPUs, with 2.7 times lower latency and a 3.7 times smaller model than the Evolved Transformer, at a far lower search cost. A taped-out chip from his group demonstrates it: a recorded demo classifies sentences about flights, weather and music on the chip, which runs four model sizes that share one set of weights; the chip won a best-demo award.
**In this book:** [Neural Architecture Search › Step 6. Train once for many devices: once-for-all](../09-efficient-deep-learning/05-neural-architecture-search.md#step-6-train-once-for-many-devices-once-for-all).

### [1:06:00–1:12:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=3960) Applications: point clouds, image editing, pose

For LiDAR segmentation in self-driving, SPVNAS raised a slow baseline from 3.4 to 9 frames per second. Anycost GAN edits photos with a small generator in 0.3 seconds on a laptop and runs the full network once at the end; such models differ from pruned ones only in being trained with shared weights, a difference that pays when many sizes must switch seamlessly. Hardware-aware search also made pose estimation four to five times faster on a mobile CPU; his group released models for gaze estimation in driver monitoring and for on-device segmentation.
**In this book:** [Neural Architecture Search › Step 6. Train once for many devices: once-for-all](../09-efficient-deep-learning/05-neural-architecture-search.md#step-6-train-once-for-many-devices-once-for-all).

### [1:12:00–1:18:00](https://www.youtube.com/watch?v=5ty12mNV4Sg&t=4320) Quantum circuits, language models, and a summary

The same recipe applies outside neural networks. Quantum circuits suffer noise, so a measured classifier lost accuracy against theory, from about 80% to 40%; searching sub-circuits of a super-circuit for noise-robust ones raised it to 85% on a real quantum computer. NVIDIA's adaptive language-model inference, Flextron, uses a similar idea, with routers choosing how much of each layer to run on cloud, desktop and mobile hardware. Han closes: performance estimation, ProxylessNAS and once-for-all, to be used in Lab 3; next comes knowledge distillation.
**In this book:** [Neural Architecture Search › Step 6. Train once for many devices: once-for-all](../09-efficient-deep-learning/05-neural-architecture-search.md#step-6-train-once-for-many-devices-once-for-all).

## What to take away

- Training every candidate is hopeless; inherit weights, or search on the target directly by learning path probabilities with one path active.
- FLOPs do not predict latency; use measured latency, or a predictor built from measurements, as the reward.
- Train one network with elastic kernel size, depth, width and resolution, then sample sub-networks for every device.
- Even the hardware and its compiler mapping can join the search.

## Sources

- Song Han, "Neural Architecture Search (Part II)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=5ty12mNV4Sg).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
