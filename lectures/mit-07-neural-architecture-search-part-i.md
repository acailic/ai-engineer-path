# Lecture guide: Neural Architecture Search (Part I)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 7 · **Length:** 1:08:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=3W146_T8eCs) · **Slides:** [slides](https://www.dropbox.com/scl/fi/hxhjhxonwqyw2hfoywzcp/Lec07-Neural-Architecture-Search-I.pdf?rlkey=o6s5dglazyb2o2nrc897ccppg&st=dcjyr42l&dl=0)
**Chapters that cite this lecture:** [05. Neural Architecture Search](../09-efficient-deep-learning/05-neural-architecture-search.md)

> **In one sentence:** Song Han opens neural architecture search: the classic building blocks and what each costs, search spaces at cell and network level and how to narrow them, and the search strategies from grid and random search to reinforcement learning, differentiable search and evolution.

## Before you watch

The chapter [Neural Architecture Search](../09-efficient-deep-learning/05-neural-architecture-search.md) turns the two architecture-search lectures into six steps. The layer arithmetic of the second lecture (MACs and parameters of a convolution) is assumed.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=0) Designing a small model from the start

After pruning and quantization, a third approach: instead of compressing an existing model, design a small and efficient one to begin with. The difficulty is the trade-off among metrics: latency (an image in seconds, a car that must act in time, a robot that must react), energy (a phone's battery, a data centre's cooling and emissions), storage (a 70-gigabyte model is hard to download) and, beneath them all, accuracy, without which nothing else attracts users. The lecture first reviews the primitive operations and classic building blocks, then the search space and search strategies.
**In this book:** [Neural Architecture Search › Why this matters](../09-efficient-deep-learning/05-neural-architecture-search.md#why-this-matters).

### [4:00–6:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=240) Primitive operations, recalled

The primitives from the second lecture, with their shapes: the fully connected layer (N × Ci input, N × Co output, Ci × Co weights and MACs); 1D and 2D convolution (four-dimensional weights, six factors in the MAC count); grouped convolution, which divides weights and MACs by the number of groups; depthwise convolution, the extreme case where each channel interacts only with itself, with one factor fewer; and the 1 by 1 convolution, which projects Ci channels to Co.
**In this book:** [Neural Architecture Search › Step 1. Pick the building blocks](../09-efficient-deep-learning/05-neural-architecture-search.md#step-1-pick-the-building-blocks).

### [6:00–10:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=360) The bottleneck block

These primitives build blocks. The ResNet-50 bottleneck has three layers and a bypass that lets them learn a residual. A 3 by 3 convolution costs nine times a 1 by 1, so the block first cuts the channels four times, from 2048 to 512, with a 1 by 1 convolution, runs the 3 by 3 on the small tensor, and restores 2048 channels with another 1 by 1. Han works the MACs and parameters: 8.5 times fewer than a single 3 by 3 convolution from 2048 to 2048 channels.
**In this book:** [Neural Architecture Search › Step 1. Pick the building blocks](../09-efficient-deep-learning/05-neural-architecture-search.md#step-1-pick-the-building-blocks).

### [10:00–12:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=600) ResNeXt

ResNeXt adds grouped convolution to the block: the 3 by 3 layer has 32 groups, as if 32 small convolutions ran side by side, each mapping a few channels. Han reads the block as 32 parallel paths, a structure that could be turned into a mixture of experts.
**In this book:** [Neural Architecture Search › Step 1. Pick the building blocks](../09-efficient-deep-learning/05-neural-architecture-search.md#step-1-pick-the-building-blocks).

### [12:00–18:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=720) MobileNetV2 and the inverted bottleneck

MobileNet reintroduced the depthwise separable block: a depthwise convolution models the spatial information and a 1 by 1 convolution the interactions across channels, which separates the two kinds of modelling to save computation. MobileNetV2's inverted bottleneck expands the channels six times before the depthwise convolution instead of shrinking them, because depthwise convolution, with one factor fewer, is cheap but weak and needs more channels for capacity. Its MACs and parameters are tiny; the depthwise layer with 960 channels has only 9 times 960 weights. What is hidden: the six-times larger feature maps cost activation memory. Moving from ResNet-18 to MobileNetV2 cuts parameters four or five times, yet the peak activation grows by 80% at batch size one; with a large training batch the activation memory improves only by 10%. The block is good for inference, not for training memory.
**In this book:** [Neural Architecture Search › Step 1. Pick the building blocks](../09-efficient-deep-learning/05-neural-architecture-search.md#step-1-pick-the-building-blocks) · [Neural Network Basics for Efficiency › 5. Counting memory](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#5-counting-memory).

### [18:00–22:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=1080) ShuffleNet and the transformer block

ShuffleNet uses grouped convolution and then shuffles channels across groups so that information flows between them. The transformer block is built on multi-head self-attention: the input is projected to query, key and value; Q times the transpose of K is divided by the square root of d, passed through a softmax and a causal mask, and multiplied by V. Unlike a convolution, whose receptive field is small in one layer, one attention layer reaches all previous tokens. Heads run independently, are concatenated and projected; the three input projections can be fused into one matrix so that one kernel call serves all, since kernel calls cost time.
**In this book:** [Neural Architecture Search › Step 1. Pick the building blocks](../09-efficient-deep-learning/05-neural-architecture-search.md#step-1-pick-the-building-blocks).

### [22:00–24:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=1320) The price of attention, and its map

With n tokens of dimension d, the two matrix multiplications cost 2 times n squared times d: quadratic in the number of tokens, so larger images and longer contexts get expensive fast. The attention map for a sample sentence shows which words attend to which, and some words, nearly all white in the map, attend to nothing; a later lecture will discuss pruning such tokens. Asked why the map is not symmetric, Han answers that attention from future to past need not mirror attention from past to future.
**In this book:** [Neural Network Basics for Efficiency › 3. Attention, in one paragraph](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#3-attention-in-one-paragraph) · [Neural Architecture Search › Step 1. Pick the building blocks](../09-efficient-deep-learning/05-neural-architecture-search.md#step-1-pick-the-building-blocks).

### [24:00–28:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=1440) From hand design to search

Manual architecture design is black magic: kernel sizes among 1, 3, 5 and 7, input resolution, whether to bypass, how many channels at each depth. It is also hard to fit a model to hardware by hand: the first Google TPU had 28 megabytes of on-chip SRAM, which GoogLeNet v1 happens to fit. On a plot of accuracy against MACs, each hand-crafted model, ResNet-50 at about 4 billion MACs and 76% or ResNeXt and Xception near 80%, pays for accuracy with computation, while models found by search in Han's lab match or beat that accuracy at about half a billion MACs, and a whole family of searched models crowds the top-left corner.
**In this book:** [Neural Architecture Search › The core idea](../09-efficient-deep-learning/05-neural-architecture-search.md#the-core-idea).

### [28:00–30:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=1680) The three parts of a search

Neural architecture search has three components: a search space of candidate architectures, a search strategy that proposes one, and a performance estimation strategy that reports accuracy, latency, energy and storage back to the search, which repeats until a model fits the need.
**In this book:** [Neural Architecture Search › The core idea](../09-efficient-deep-learning/05-neural-architecture-search.md#the-core-idea).

### [30:00–34:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=1800) Cell-level search space

The first search space is cell-level. A network starts at high resolution, 224, and ends at a single prediction, so reduction cells, strided convolution or pooling, lower the resolution, 224 to 112 to 56 and so on, while normal cells repeat between them. The idea is to search only two cells, a normal one and a reduction one, and repeat them n times per stage: a 50-layer problem becomes a two-layer one. In the NASNet paper the searched cells look unreadable: each takes its inputs from the previous or the second-previous layer, applies operations such as separable 3 by 3 convolutions, and combines them by addition and concatenation.
**In this book:** [Neural Architecture Search › Step 2. Define the search space](../09-efficient-deep-learning/05-neural-architecture-search.md#step-2-define-the-search-space).

### [34:00–38:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=2040) How large the space is

NASNet generated cells with a recurrent network as controller: choose a first hidden state, a second one, an operation for each, a way to combine them, and repeat B times. Han asks for the size of the space: with two candidate inputs, M candidate operations and N ways to combine, each layer has 2 × 2 × M × M × N choices, raised to the power B. With M = 5 (1 by 1, 3 by 3, 5 by 5 convolutions, identity, pooling), N = 2 and B as in the example, that is about 10 to the 11 candidates, which motivates the search strategies later in the lecture.
**In this book:** [Neural Architecture Search › Step 2. Define the search space](../09-efficient-deep-learning/05-neural-architecture-search.md#step-2-define-the-search-space).

### [38:00–44:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=2280) Network-level search space

Repeating one cell may not be optimal, since deep and shallow layers want different things. A network-level space treats the whole network: the depth of each of five stages; the input resolution, which can even be randomized during training, which usually helps; the width in channels per stage; kernel sizes; and the topology, the path through downsampling factors, which may stay down for classification, return up for segmentation, or go down and up as in the autoencoders of latent diffusion models.
**In this book:** [Neural Architecture Search › Step 2. Define the search space](../09-efficient-deep-learning/05-neural-architecture-search.md#step-2-define-the-search-space).

### [44:00–46:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=2640) Narrowing the space

Searching a huge space blindly is like searching a whole forest for a lost friend: narrow it first. The lecture splits the problem in two: TinyNAS first optimizes the search space itself, then runs a resource-constrained search that specializes a model for one hardware constraint. The constraints differ: latency and energy on phones, memory as well on IoT devices and, for large language models, scarce GPU memory. From cloud to mobile to tiny AI, memory spans tens of gigabytes to a few hundred kilobytes, three orders of magnitude, and storage four.
**In this book:** [Neural Architecture Search › Step 2. Define the search space](../09-efficient-deep-learning/05-neural-architecture-search.md#step-2-define-the-search-space).

### [46:00–52:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=2760) A heuristic for a good design space

How to judge a design space without training to the end? Han's heuristic: a good design space fits more FLOPs under the same memory constraint, since capacity grows with computation and memory, not arithmetic, is what costs. He plots the cumulative distribution of models' FLOPs in two spaces, one narrower with higher resolution and one wider with lower resolution; the space whose models mostly reach a higher operation count also produced the better trained models, 78.7% against 74%. Unlike ResNet-18 at 224 resolution, which runs out of memory on a microcontroller, the space is superior to a larger or a random one. Median FLOPs and accuracy correlate almost linearly.
**In this book:** [Neural Architecture Search › Step 2. Define the search space](../09-efficient-deep-learning/05-neural-architecture-search.md#step-2-define-the-search-space).

### [52:00–56:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=3120) Grid search and compound scaling

A push-button search should need no human expert. Strategies, from the simplest: grid search lays a grid over dimensions such as resolution and width, trains each design for a while and keeps the best that meets the constraints, discarding infeasible designs before training them; easy to write, slow to run. A lesson from scaling a baseline model to twice the size: do not push one knob to the extreme. Scale depth, width and resolution a little each so that their product reaches the target. Compressing a network works the same way: a little pruning, a little quantization, a little distillation, combined.
**In this book:** [Neural Architecture Search › Step 3. Choose a search algorithm](../09-efficient-deep-learning/05-neural-architecture-search.md#step-3-choose-a-search-algorithm).

### [56:00–58:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=3360) Random search and reinforcement learning

Random search samples designs at random and is the first thing to run, also in the homework: if the reward never improves, something is wrong with the space, the search, the evaluation or the reward. Reinforcement learning is trickier and not easy to use in practice: a controller, once a recurrent network and today an autoregressive model, proposes an architecture with some probability; a child network with that architecture is trained; its accuracy and latency give a reward; and the controller's probabilities are updated by the gradient of the probability scaled by that reward.
**In this book:** [Neural Architecture Search › Step 3. Choose a search algorithm](../09-efficient-deep-learning/05-neural-architecture-search.md#step-3-choose-a-search-algorithm).

### [58:00–1:02:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=3480) Gradient descent, and a differentiable latency

Search can be made differentiable. Where a layer could be a 3 by 3, a 5 by 5 or a 1 by 1 convolution, the output is a weighted sum of all candidates and the weights, the probabilities of choosing each, are learned; training runs every candidate, which costs memory, and at inference the most probable path is kept. Latency can join the loss too: measure each building block's latency once, take the expected latency as the sum of probability times latency, and add it to the cross-entropy loss and the weight regularizer, so that gradient descent favours accurate and fast models at once.
**In this book:** [Neural Architecture Search › How it works, step by step › Step 3: Choose a search algorithm](../09-efficient-deep-learning/05-neural-architecture-search.md#step-3-choose-a-search-algorithm).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=3720) Evolutionary search

Evolutionary search imitates evolution. A population of architectures is judged by a fitness function, accuracy against latency, memory or energy; survivors are mutated, by changing a stage's depth or swapping a 3 by 3 convolution for a 5 by 5 or 7 by 7, or crossed over, taking each layer from one of two parents at random; selection and variation repeat until termination. Lab 3 implements mutation and crossover.
**In this book:** [Neural Architecture Search › Step 3. Choose a search algorithm](../09-efficient-deep-learning/05-neural-architecture-search.md#step-3-choose-a-search-algorithm).

### [1:06:00–1:08:00](https://www.youtube.com/watch?v=3W146_T8eCs&t=3960) Summary

Han recaps: primitive operations assembled into building blocks, search spaces at cell and network level, the heuristic that narrows a space to models that fit the most computation under a memory budget, and the search strategies, grid, random, reinforcement learning and evolution. Lab 2 is released.
**In this book:** [Neural Architecture Search › Step 3. Choose a search algorithm](../09-efficient-deep-learning/05-neural-architecture-search.md#step-3-choose-a-search-algorithm).

## What to take away

- Each building block trades something: bottlenecks shrink the expensive 3 by 3 layer, inverted bottlenecks expand channels because depthwise convolution is cheap but weak, and attention buys a global receptive field at a quadratic price.
- Searching two repeated cells makes the problem much simpler; a network-level space is larger but lets layers differ.
- A good design space fits more computation under the same memory budget; judge spaces that way before training.
- Simple searches first: random as a sanity check, then grid, evolution, reinforcement learning or a differentiable relaxation; never push one knob to the extreme.

## Sources

- Song Han, "Neural Architecture Search (Part I)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=3W146_T8eCs).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
