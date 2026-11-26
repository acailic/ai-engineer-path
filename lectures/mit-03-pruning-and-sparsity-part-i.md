# Lecture guide: Pruning and Sparsity (Part I)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 3 · **Length:** 58:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=EjsB0WgIfUM) · **Slides:** [slides](https://www.dropbox.com/scl/fi/6qspcmk8qayy7mft737gh/Lec03-Pruning-I.pdf?rlkey=9jpifc92be0sitiknpbhn9ggf&st=lml94lam&dl=0)
**Chapters that cite this lecture:** [03. Pruning and Sparsity](../09-efficient-deep-learning/03-pruning-and-sparsity.md)

> **In one sentence:** Song Han introduces pruning, the removal of redundant weights from a trained network: why it pays, how granularities from single weights to whole channels trade flexibility for speed, which criteria pick the weights, and how gentle prune-and-retrain cycles recover accuracy.

## Before you watch

The chapter [Pruning and Sparsity](../09-efficient-deep-learning/03-pruning-and-sparsity.md) turns this lecture and its sequel into a five-step procedure. It assumes the previous lecture's material on parameters versus MACs, the energy cost of operations and batch normalization.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=0) Why prune

This lecture opens the first section of the course, efficient inference: pruning, quantization, architecture search and distillation, concluded by fitting a network onto a microcontroller. MLPerf, which Han calls the Olympic games of AI computing, measures latency and throughput at a given accuracy in two divisions: the closed one fixes the model and allows only quantization, the open one allows any change. On a recent benchmark a Llama 2 model with 70 billion parameters ran at 4,488 tokens per second on one H200 GPU in the closed division, and above 11,000 in the open division, about 2.5 times faster at good accuracy, after depth pruning from 80 to 32 layers and then width pruning. The hardware reason is energy: a 32-bit add costs under a picojoule and a DRAM access more than 600, so shrinking memory, model size and activations is what pays.
**In this book:** [Pruning and Sparsity › What the practitioners say](../09-efficient-deep-learning/03-pruning-and-sparsity.md#what-the-practitioners-say) · [Pruning and Sparsity › The core idea](../09-efficient-deep-learning/03-pruning-and-sparsity.md#the-core-idea).

### [4:00–6:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=240) What pruning is

Pruning turns a dense network into a sparse one. Formally, it minimizes the loss of the network with pruned weights subject to a bound on the number of non-zero weights. The lecture follows four decisions: granularity, criterion, the ratio of weights to remove, and how to fine-tune afterwards. Nature got there first: a study he cites from the journal Nature counts about 2,500 synapses per neuron in a newborn, 15,000 at the age of four, and about 7,000 in adolescence, when pruning occurs just as people learn most. Artificial networks too can shed redundant synapses and neurons.
**In this book:** [Pruning and Sparsity › The core idea](../09-efficient-deep-learning/03-pruning-and-sparsity.md#the-core-idea).

### [6:00–10:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=360) Prune, retrain, repeat

Han's 2015 experiment on AlexNet: after training, a layer's weights form a rough bell curve; removing the smallest weights zeroed the values around the centre, and the more was pruned, the more accuracy fell. Retraining the surviving weights moved the curve toward the upper-right corner: more weights removed at the same accuracy, and the weight distribution became smoother. Repeating the cycle pushed further still, to about 90% of parameters removed without loss of accuracy. The rule that emerged: prune by magnitude, retrain the survivors, and take many gentle steps rather than one aggressive one.
**In this book:** [Pruning and Sparsity › Step 4: Fine-tune, a little at a time](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-4-fine-tune-a-little-at-a-time).

### [10:00–13:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=600) How far it goes

On AlexNet, VGG, ResNet, SqueezeNet and others, AlexNet shrank from 61 million parameters to 6.7 million, nine times fewer, while the multiply-accumulates fell only three times: fewer parameters are not fewer operations. SqueezeNet, designed in 2016 with AlexNet's accuracy at a fraction of its size, could still be reduced from 1 million to 0.38 million parameters. Image captioning survives 90% pruning with the same meaning; at 95% the caption drifts, so there is a limit.
**In this book:** [Pruning and Sparsity › What the practitioners say](../09-efficient-deep-learning/03-pruning-and-sparsity.md#what-the-practitioners-say).

### [13:00–15:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=780) History and industry

The field began in the 1980s with Optimal Brain Damage, grew slowly, and took off after Deep Compression in 2015–2016 showed that modern networks trained on large data could be pruned aggressively. Han's Efficient Inference Engine (ISCA 2016) then ran the sparse, compressed models directly. Publications now surge. NVIDIA adopted sparsity from the A100 onward with 2:4 sparsity, about two times theoretical and 1.5 times measured speed-up, and Xilinx, now part of AMD, uses sparsity too: by his account it acquired his startup and built its AI optimizer into a software tool chain that prunes and fine-tunes models.
**In this book:** [Pruning and Sparsity › What the practitioners say](../09-efficient-deep-learning/03-pruning-and-sparsity.md#what-the-practitioners-say).

### [15:00–18:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=900) Granularity: fine or coarse

The first decision is the pattern. In a weight matrix, fine-grained pruning removes any weight anywhere: most flexible and with the highest pruning ratio, but irregular, and GPU threads prefer to work in lockstep without branching, so it is hard to accelerate. Coarse-grained pruning removes whole rows or columns; what remains condenses into a smaller dense matrix that ordinary dense multiplication handles: regular and easy to accelerate, less flexible, with a lower ratio. A convolution kernel has four dimensions, input channels, output channels, kernel height and kernel width, which opens more choices between the two extremes.
**In this book:** [Pruning and Sparsity › Step 1: Choose the granularity](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-1-choose-the-granularity).

### [18:00–20:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=1080) Fine-grained pruning

Fine-grained pruning is irregular but most flexible, with the highest ratio: weights compress by up to an order of magnitude. It is the way to go, he says, when the goal is to compress the weights and acceleration is not the concern. It can be sped up on specialized hardware such as the Efficient Inference Engine, but not easily on off-the-shelf hardware.
**In this book:** [Pruning and Sparsity › Step 1: Choose the granularity](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-1-choose-the-granularity).

### [20:00–22:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=1200) Pattern-based pruning: 2:4 sparsity

Pattern-based pruning prunes kernels in fixed shapes, for instance patterns that repeat under 90-degree rotations, which is more regular. The notable case is n:m sparsity; in 2:4, every group of four entries contains at least two zeros, 50% sparsity. An element has four possible positions in its group, so two bits of metadata record where it lies. Accuracy holds across several benchmarks, he says: 76.1% dense against 76.2% sparse.
**In this book:** [Pruning and Sparsity › Step 1: Choose the granularity](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-1-choose-the-granularity).

### [22:00–26:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=1320) Up to channel pruning, and one ratio or many

Vector-level and kernel-level pruning sit in between, each more regular and less free. The extreme is channel pruning, removing whole channels: the network is simply smaller and still dense, so it speeds up on any existing hardware, at the price of a smaller compression ratio, about 30% of parameters for MobileNet. Different layers can take different ratios. Uniform shrinking applies the same sparsity everywhere; searching a ratio per layer does better. Language models repeat identical blocks with the same channel count, which makes them easy to split across GPUs, yet layers may differ in redundancy when inference is to be squeezed. In the example on his slide, a search method, AMC, found ratios with lower latency and higher accuracy than uniform pruning. Sensitivity analysis comes in the next lecture.
**In this book:** [Pruning and Sparsity › Step 1: Choose the granularity](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-1-choose-the-granularity) · [Pruning and Sparsity › Step 3: Choose the ratio for each layer](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-3-choose-the-ratio-for-each-layer).

### [26:00–30:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=1560) Criteria: magnitude

The second decision is which weights to remove, and magnitude is the simplest answer: of 10, −8 and 0.1, drop 0.1. It has worked well in academia and industry for years. A single weight is judged by its absolute value; a row by a norm, L1, L2 or Lp. Scaling-based pruning learns one scale per filter, only n numbers, and pushes the scales toward zero; filters are sorted by scale and the smallest removed.
**In this book:** [Pruning and Sparsity › Step 2: Choose the criterion](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-2-choose-the-criterion).

### [30:00–34:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=1800) Scaling from batch normalization, and second-order pruning

That scale can be borrowed: batch normalization already holds one scale per channel, which, he says, simplifies the calculation. Magnitude may not be the best criterion, and which one wins is an empirical question, so Han sketches the design space. Optimal Brain Damage expands the loss as weights are perturbed, drops terms of third order and above, drops the first-order term because training has converged and the gradient is near zero, and drops cross terms by assuming the errors of deleting different parameters are independent. What remains is a second-order term with the Hessian, which is hard to compute and must be estimated.
**In this book:** [Pruning and Sparsity › Step 2: Choose the criterion](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-2-choose-the-criterion).

### [34:00–38:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=2040) Pruning neurons by their zeros

Neurons can be pruned too, which is coarse-grained weight pruning: removing one output neuron of a linear layer removes a row of the weight matrix, and removing an output channel of a convolution removes its kernel. One criterion for activations is the average percentage of zeros, which requires running a few samples, unlike the static statistics of weights. With a batch of two and three channels of 4 by 4, each channel has 32 values; the channel with the most zeros is judged redundant and removed. After a short break Han restates that these six maps are activations, not weights.
**In this book:** [Pruning and Sparsity › Step 2: Choose the criterion](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-2-choose-the-criterion).

### [38:00–44:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=2280) Regression-based pruning

Supervising pruning with the end-to-end loss is expensive; for a large language model the signal would have to travel through every layer. Regression-based pruning instead minimizes the reconstruction error of one layer, a single matrix multiplication. The product of an activation block with a weight block splits into a sum over input channels, each term an outer product of one activation channel and one weight channel, with a scaling factor per term. The task is to keep the pruned output close to the original while making as many factors zero as possible; a zero factor removes that channel. Solving alternates: fix the weights and solve for the factors to pick channels, then fix the factors and solve for the weights, and repeat.
**In this book:** nothing beyond this guide; nearest: [Pruning and Sparsity › Step 2: Choose the criterion](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-2-choose-the-criterion).

### [44:00–54:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=2640) A demo on handwritten digits

In a Colab notebook on a free T4 GPU, a network learns MNIST to 98.99% in five epochs. Pruning 70% of the weights drops it to 94.6%; two epochs of fine-tuning bring it back to 98.85%. At 90% pruned, accuracy falls to 20% and recovers to 98.3%. At 99% the network predicts the same digit for everything and recovers only to 33%: the limit of this simple scheme. The code is released for students to explore, and Lab 1 asks for a good schedule.
**In this book:** [Pruning and Sparsity › Step 4: Fine-tune, a little at a time](../09-efficient-deep-learning/03-pruning-and-sparsity.md#step-4-fine-tune-a-little-at-a-time).

### [54:00–58:00](https://www.youtube.com/watch?v=EjsB0WgIfUM&t=3240) Questions, and what comes next

Asked how fine-tuning differs from training, Han answers: the same recipe with a learning rate ten times smaller and two epochs instead of five, since the network is already near a solution. Asked about training a small model from scratch, he says it does worse than pruning a large one, because over-parameterization helps optimization: by his account, an extra dimension can turn a local minimum where training is stuck into a saddle from which it goes lower. SVD, pruning, quantization and distillation are orthogonal and combinable. The next lecture covers per-layer ratios, sensitivity analysis, automated search, and hardware support for each granularity.
**In this book:** [Pruning and Sparsity › What the practitioners say](../09-efficient-deep-learning/03-pruning-and-sparsity.md#what-the-practitioners-say).

## What to take away

- Prune by magnitude, retrain the survivors and repeat gently: about 90% of parameters can go without hurting accuracy (his 2015 AlexNet experiment), though fewer parameters are not fewer operations.
- Granularity trades flexibility for speed: fine-grained pruning compresses most but needs special hardware, channel pruning runs anywhere but compresses less, and 2:4 sparsity sits in between.
- Beyond magnitude: learned or batch-normalization scales, second-order saliency, zero-counted activations, and layer-wise reconstruction.
- Too much pruning cannot be recovered: at 99% the demo model got back only to 33%.

## Sources

- Song Han, "Pruning and Sparsity (Part I)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=EjsB0WgIfUM).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
