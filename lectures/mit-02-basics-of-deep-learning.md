# Lecture guide: Basics of Deep Learning

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 2 · **Length:** 52:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=I0nKjPpZmMU) · **Slides:** [slides](https://www.dropbox.com/scl/fi/pxvvqyq2yu6mwgk79bq5x/Lec02-Basics.pdf?rlkey=tsumfkhrglic55jnjs4yu66ni&st=cmwnvuvn&dl=0)
**Chapters that cite this lecture:** [02. Neural Network Basics for Efficiency](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md)

> **In one sentence:** Song Han reviews the layers of a neural network, from linear layers and convolutions to attention, and defines the metrics used throughout the course: parameters, model size, activations, MACs, FLOPs, latency and throughput.

## Before you watch

The chapter [Neural Network Basics for Efficiency](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) follows this lecture almost section by section and works the arithmetic. You need only arithmetic and the idea of a neural network; the lecture builds up from the vocabulary.

## The lecture, part by part

### [0:00–3:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=0) Recap and plan

Song Han recalls the gap from the first lecture: hardware roughly doubles every two years, while models grow more than four times as fast. This lecture supplies the technical basics: the vocabulary of neural networks, the common building blocks and the memory and computation each demands, and the efficiency metrics (parameters, model size, activations, MACs, FLOPs, latency, throughput). Lab 0 is an optional PyTorch tutorial; all material is published on the course website, efficientml.ai.
**In this book:** not needed (course introduction and plan of the lecture).

### [3:00–5:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=180) Neurons, synapses, and width versus depth

Three pairs of words mean the same thing: synapses, weights and parameters; neurons, features and activations. The width of the hidden layers matters for efficiency. A wide, shallow network and a narrow, deep one can have the same number of parameters; the wide one is more hardware-friendly, with fewer kernel calls and enough parallelism to occupy a GPU's threads, while depth helps accuracy. Architecture design is the trade-off between the two.
**In this book:** [Neural Network Basics for Efficiency › The core idea](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#the-core-idea).

### [5:00–7:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=300) The fully connected layer

A fully connected, or linear, layer holds a weight matrix of Ci by Co, with Ci input activations, Co output activations and a bias; the output is a weighted sum of the input. Tracking the dimension of every tensor, including the bias, is the habit to build: later techniques such as bias-only updates and LoRA concern the bias, and every count of operations or model size follows from these shapes. With a batch of N inputs the weights stay the same while input and output gain a dimension.
**In this book:** [Neural Network Basics for Efficiency › 1. The fully connected layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#1-the-fully-connected-layer).

### [7:00–10:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=420) Convolution in one and two dimensions

In a convolution the output neuron connects only to inputs inside its receptive field. In one dimension, a filter of width KW slides along the spatial axis; three filters give three output channels, the weights have the shape Ci by K by Co, and there is one bias per output channel. In two dimensions the feature map is really three-dimensional, since each x, y position carries a channel dimension; a filter is KH by KW over the same Ci input channels, and it shifts to produce further outputs. The output size is the input size minus the kernel size plus one: a 4 by 4 input with a 3 by 3 kernel gives 2 by 2.
**In this book:** [Neural Network Basics for Efficiency › 2. The convolution layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#2-the-convolution-layer).

### [10:00–12:30](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=600) Padding

Without padding, feature maps shrink layer by layer. Zero padding at the borders keeps the output the size of the input and is PyTorch's default: with size 5, kernel 3 and one zero on each side, the output is 5 + 2 − 3 + 1, which is 5. Reflection padding fills the border with mirrored values and replication padding repeats the nearest one; zero padding is still the most used.
**In this book:** [Neural Network Basics for Efficiency › 2. The convolution layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#2-the-convolution-layer).

### [12:30–17:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=750) Receptive field, and stride as a shortcut

The receptive field is how much of the previous layer one output pixel can see. With 3 by 3 kernels it is 3 after one layer, 5 after two, 7 after three, by the formula L × (K − 1) + 1. A large one matters, because high-level understanding depends on relations between distant pixels, a car and a pedestrian on the same road; transformers later offered a global receptive field. Earning a large field by depth costs kernel calls and, during training, stored activations, so networks downsample instead. A strided convolution moves the window by two pixels instead of one: two 3 by 3 layers then reach a receptive field of 7. That means fewer layers, weights and activations for the same field, at a possible loss of capacity. No free lunch: design is constrained optimization.
**In this book:** [Neural Network Basics for Efficiency › 2. The convolution layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#2-the-convolution-layer).

### [17:00–19:30](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=1020) Group and depthwise convolution

To cut computation further, grouped convolution divides the channels into G groups; each output channel sees only Ci / G input channels and the weights shrink by a factor of G. The extreme, G equal to the channel count, is depthwise convolution: each output channel connects to one input channel and the weights number only C × KH × KW. It has been widely used since MobileNet appeared around 2015.
**In this book:** [Neural Network Basics for Efficiency › 2. The convolution layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#2-the-convolution-layer).

### [19:30–21:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=1170) Pooling

Pooling shrinks a feature map to condense information, which is useful for large inputs. A 4 by 4 map becomes 2 by 2 by taking the maximum or the average of each block. Pooling has no learnable parameters at all.
**In this book:** [Neural Network Basics for Efficiency › 2. The convolution layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#2-the-convolution-layer).

### [21:00–24:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=1260) Normalization

Batch normalization arrived around 2015 to stabilize training, and layer normalization serves the same purpose in transformers. Both subtract a mean and divide by a standard deviation plus a tiny constant that avoids division by zero, then apply a learned scale and bias so that representational power is not lost. Four common choices of the set to normalize over: batch normalization across the batch dimension for one channel; layer normalization across channels and space for each input, so that each token is normalized before attention; instance normalization over height and width only; and group normalization over channel groups when the channel count is large. Two efficiency uses: the layer has so few parameters that fine-tuning can update only them, and it can absorb transformations such as those in SmoothQuant without an extra kernel call.
**In this book:** nothing beyond this guide; nearest: [Neural Network Basics for Efficiency › 2. The convolution layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#2-the-convolution-layer).

### [24:00–28:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=1440) Activation functions, chosen for efficiency

Each popular activation carries an efficiency story. The sigmoid ranges from 0 to 1, which makes it easy to quantize, but its gradient vanishes at both ends. ReLU keeps a gradient of one for positive inputs and brings natural sparsity, since negative inputs become zero: such a feature map needs only a one-bit mask, and zero times anything is zero. Its costs are dead neurons and an unbounded range that is hard to quantize. ReLU6 caps the output at 6, a purely empirical choice that narrows the range. Leaky ReLU adds a small slope below zero so that gradients flow there, giving up sparsity. Architecture search found Swish, which is x times a sigmoid of x, awkward to compute in hardware, so hard Swish approximates it: zero below −3, x above 3, a line in between.
**In this book:** nothing beyond this guide; nearest: [Neural Network Basics for Efficiency › 2. The convolution layer](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#2-the-convolution-layer).

### [28:00–32:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=1680) Transformers and attention in outline

Transformers, introduced in 2017 and the subject of a later lecture, have an encoding and a decoding stage, each combining multi-head attention with a feed-forward network. Attention works on query, key and value tensors, which with the output make four activation tensors; the weights sit only in the transformations that produce them. Han likens it to retrieval in video search: the query is the typed text, the key the title and description, the value the video itself; a dot product of query and key, scaled by the square root of the dimension for stability, passes through a softmax and weights an average of the values. The resulting attention map has one entry per pair of tokens, so it grows with the square of the sequence length, and for images the token count itself grows with the square of the resolution. It is the bottleneck for both computation and memory, which later lectures attack with sparse attention, FlashAttention, which keeps memory almost constant without reducing the arithmetic, and long-context techniques. The KV cache, an activation when computed, behaves like a weight during generation, so it too can be quantized or pruned.
**In this book:** [Neural Network Basics for Efficiency › 3. Attention, in one paragraph](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#3-attention-in-one-paragraph).

### [32:00–34:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=1920) Smaller, faster, greener: the metrics

Three goals at once: a smaller model, so that an app store download stays reasonable; a faster one, for a car that must not miss a pedestrian or for instant image generation on a phone; and a greener one that spares the battery. Memory and computation determine them. Memory-related metrics count the parameters, the stored size of the model, and the activations both in total and at their peak; computation-related ones are MACs, FLOPs, FLOPS, OPs and OPS. Latency is the delay of one task, 45 milliseconds per frame in his example; throughput is the rate of processing, 77 videos per second against 6.
**In this book:** [Neural Network Basics for Efficiency › 6. Latency and throughput](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#6-latency-and-throughput).

### [34:00–36:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=2040) Latency and throughput are independent

Design 1 processes an image in 50 milliseconds, one at a time: 20 images per second. Design 2 processes four images concurrently, each in 100 milliseconds: 40 per second with a longer latency. So higher throughput does not imply lower latency, nor the reverse; mobile applications mostly care about latency, batch jobs in data centers about throughput, and a report should give both. Two first-order terms set latency: computation time, the number of operations divided by the operations the hardware performs per second, and memory time, the sizes of the activations and weights moved divided by the memory bandwidth; training adds communication of gradients.
**In this book:** [Neural Network Basics for Efficiency › 6. Latency and throughput](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#6-latency-and-throughput).

### [36:00–38:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=2160) Energy: computation is cheap, movement is expensive

A well-known energy table makes the point: a 32-bit integer add costs 0.1 picojoules and a DRAM access 640, several thousand times more. The battery goes to moving data, not to arithmetic.
**In this book:** [Neural Network Basics for Efficiency › 7. Energy](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#7-energy).

### [38:00–42:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=2280) From parameters to model size

An exercise counts the parameters of AlexNet's layers: a convolution with 3 input and 96 output channels, a grouped variant with half as many weights, a 3 by 3 layer going from 256 to 384 channels, and the fully connected layers, where input channels times output channels gives the bulk of the 61 million weights. Model size is the number of parameters times the bits per parameter: in 32-bit floating point, four bytes each, that is about 240 megabytes; in 8-bit integers 61 megabytes; and weight-only 4-bit quantization halves it again, which is what lets a large language model fit on a laptop.
**In this book:** [Neural Network Basics for Efficiency › 5. Counting memory](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#5-counting-memory).

### [42:00–46:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=2520) Activations are the memory bottleneck

For inference the bottleneck is activations, not parameters. Against ResNet-50, a MobileNetV2 of matched accuracy cuts parameters more than four times while the peak activation size does not fall; in training, a batch multiplies the activations, which can be about seven times the parameters. The peak, set by the largest layer, decides the memory needed. The distribution is lopsided in convolutional networks: early layers have few weights but large activations because the resolution is high, late layers the reverse because the channels are many, a U shape when plotted. A microcontroller with 256 kilobytes of SRAM must fit that largest layer. An activation block has C × H × W values, the total is their sum, and the peak is, to first order, the input block plus the output block of a layer. For large language models the parameters are also a bottleneck, which led to sharding them across devices.
**In this book:** [Neural Network Basics for Efficiency › 5. Counting memory](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#5-counting-memory).

### [46:00–52:00](https://www.youtube.com/watch?v=I0nKjPpZmMU&t=2760) MACs, FLOPs and OPs

A MAC, multiply and accumulate, is a = a + b × c, usually a single instruction on a GPU. A matrix-vector product of an m by n matrix takes m × n MACs; a general matrix multiplication of m by k with k by n takes m × n × k. A linear layer needs Ci × Co; a convolution six factors multiplied, output width × output height × output channels × kernel width × kernel height × input channels; a grouped convolution divides by G; depthwise convolution drops the input-channel factor. Summed over AlexNet that gives 724 million MACs. A FLOP is one floating-point operation, so one MAC is two FLOPs and AlexNet needs 1.4 gigaflops; FLOPS, with a capital S, is FLOPs per second, a speed. OP generalizes the count to any operation, integer, binary or bitwise, so the same network needs 1.4 gigaOPs, and OPS is operations per second. He closes by reviewing the layers and metrics covered.
**In this book:** [Neural Network Basics for Efficiency › 4. Counting operations](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#4-counting-operations).

## What to take away

- Weights and activations are the only two kinds of number in a network, and every efficiency count follows from tensor shapes.
- The N × N attention map grows with the square of the sequence length, and activations, not parameters, are the usual memory bottleneck.
- Latency and throughput are independent: mobile devices care about the first, data centers about the second.
- Computation is cheap and data movement expensive; count MACs, FLOPs or OPs and say which you used.

## Sources

- Song Han, "Basics of Deep Learning", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=I0nKjPpZmMU).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
