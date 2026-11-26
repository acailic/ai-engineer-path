# Lecture guide: PyTorch (einops), resource accounting (FLOPs, memory, arithmetic intensity)

**Lecturer:** course staff · **Course:** Stanford CS336 Language Modeling from Scratch, Spring 2026, lecture 2 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=kuYAsz7zspQ)
**Chapters that cite this lecture:** [02. Resource Accounting: FLOPs, Memory and Arithmetic Intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md)

> **In one sentence:** The lecturer counts the two resources a training run spends, memory and computation, from tensors up to a whole training step, and arrives at arithmetic intensity, the number that explains why only large matrix multiplications keep an accelerator busy.

## Before you watch

This is a lecture of code demonstrations with no machine-learning theory in it. It starts from how many bytes a tensor takes and which number format to store it in, shows the einops library for writing tensor operations with named dimensions, and then counts FLOPs, defines model FLOPs utilization and arithmetic intensity, derives why a training step costs about 6 × tokens × parameters FLOPs, and ends with the memory a training step needs and two ways to use less. The chapter [Resource Accounting: FLOPs, Memory and Arithmetic Intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) follows it section by section.

## The lecture, part by part

### [0:00–4:46](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=0) News, and two questions to answer by the end

The Marin project's 10^23-FLOP training run has finished and landed within 0.05 of the loss that its scaling law predicted: each curve of small runs finds the compute-optimal point, the points fit a law, and the law was then tested with one large run. The goal of the course is the best model for a finite budget, so the lecture turns to the systems side, and two questions show what it teaches. Training a model of 70 billion parameters with 15 trillion tokens on 1024 H100s takes 143 days, from the 6 × parameters × tokens formula, the spec sheet and an assumed efficiency of 0.5. The largest model that fits on eight H100s with AdamW has about 53 billion parameters, from 80 GB per card and 12 bytes per parameter. Both ignore activations and are back-of-envelope figures, which is the point: the shape of the answer, not the last digit. The lecture then names three things to take away: the mechanics of PyTorch and tensors, the habit of thinking about the performance of every line of code, and intuitions about where resources go.
**In this book:** [Resource Accounting › The core idea](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#the-core-idea) · [Resource Accounting › Worked example](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#worked-example).

### [4:46–8:06](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=286) Tensors and their storage

Everything in a model is a tensor: parameters, gradients, optimizer states, data and activations, as a look at the tensors of DeepSeek 3.2 shows. A new tensor is float32 by default: one sign bit, eight exponent bits that give the dynamic range, and the rest mantissa. A 4 × 8 float32 matrix is 32 elements times 4 bytes, 128 bytes, and one feed-forward matrix of GPT-3 is about 2.3 GB. Memory is elements times bytes per element.
**In this book:** [Resource Accounting › 1. Count bytes](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#1-count-bytes).

### [8:06–11:01](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=486) Float16, bfloat16 and the trade-off

Lower precision saves memory, and usually time as well. Halving the bits gives float16, with only five exponent bits, so its range is poor: the value 1e-8 becomes zero. Training in float16, as was once done, brings underflow, overflow and NaNs. Bfloat16, introduced in 2018, keeps the same number of bits but moves some from the mantissa to the exponent. It has the range of float32 and a worse resolution, a trade worth making because neural networks are noisy and do not need the resolution. For training, float32 is fine for a small model but costs four bytes per value, float16 is too risky, and bfloat16 is the sweet spot.
**In this book:** [Resource Accounting › 1. Count bytes](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#1-count-bytes).

### [11:01–15:05](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=661) Mixed precision, FP8 and FP4

Mixed-precision training uses bfloat16 for parameters, activations and gradients, and float32 for optimizer states. PyTorch's automatic mixed precision library wraps the code and casts each operation to bfloat16 where that is safe, a matrix product for example, while an exponentiation stays in float32. FP8 was introduced four years ago and standardized in two variants, one with more range and one with more resolution, and NVIDIA's Transformer Engine supports it. FP4 has four bits per value, so few that the lecturer writes every value on one line, from −6 to 6. Blocks of values share a scaling factor, and a model released in the year of the lecture was trained in FP4. Much of this is out of reach: it runs inside NVIDIA's software, not by asking PyTorch for an FP4 tensor.
**In this book:** [Resource Accounting › 1. Count bytes](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#1-count-bytes) · [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [15:05–17:58](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=905) One bit, and the memory calculus

A student asks about one bit. The answer separates training from inference: a model is trained in bfloat16 and quantized afterwards to one or two bits, which is a far easier problem than training a language model at one bit from scratch, which, he says, nobody has done credibly. Tensors are created on the CPU and have to be moved to the GPU to be fast, a step the lecturer can only show and not run, because the slides were executed on a laptop without a GPU.
**In this book:** [Resource Accounting › 1. Count bytes](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#1-count-bytes).

### [17:58–22:50](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=1078) einsum: names instead of axes

Code with `transpose(-2, -1)` is easy to get wrong, which is the motivation for einops, a library where dimensions have names, in the spirit of Einstein summation notation. A matrix product of two matrices becomes `x: seq1 hidden, y: hidden seq2 -> seq1 seq2`: the result is indexed by the named output dimensions, and a dimension that is not mentioned on the right is summed out. In the batched version no transpose appears, because the naming does it; `...` stands for any number of batch dimensions, so a rank-ten tensor needs no enumeration and the code stays modular.
**In this book:** [Resource Accounting › 2. Name your dimensions](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#2-name-your-dimensions).

### [22:50–27:20](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=1370) reduce and rearrange

`reduce` generalizes sum, mean, max and min: the dimensions missing on the right are reduced, and the last argument names the operation. It is only syntactic sugar and runs on the same primitives, so it brings no speed-up. `rearrange` is the powerful one. A 3 × 8 matrix whose second dimension really holds a 2 × 4 matrix can be split into heads and a hidden dimension, multiplied, and merged back. Parentheses in the pattern split a dimension, and the order of the names decides how two dimensions are grouped into one.
**In this book:** [Resource Accounting › 2. Name your dimensions](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#2-name-your-dimensions).

### [27:20–34:03](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=1640) Counting FLOPs

Computation is measured in FLOPs, an addition or a multiplication; the word is ambiguous, so the lecturer writes FLOP/s for the speed of hardware and FLOPs for the amount of work. The H100's spec sheet promises 1979 teraFLOP/s in bfloat16, but a footnote says that this is with sparsity, so the dense figure is half of it, 989. Eight H100s for a week deliver about 5 × 10^21 FLOPs. A linear layer that maps B points of D dimensions to K outputs costs 2 · B · D · K FLOPs, one multiplication and one addition for each triple. An elementwise operation costs its size, and nothing costs as much as a large matrix product. In questions, he says that gains in matrix multiplication come from co-designing with the system rather than from sub-cubic algorithms, and that hardware counts an addition like a multiplication. Read the other way, the formula is twice the number of tokens times the number of parameters, the shape of the 6ND formula.
**In this book:** [Resource Accounting › 3. Count FLOPs](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#3-count-flops) · [GPUs, TPUs and kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [34:03–39:30](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=2043) Timing code, and MFU

FLOPs do not depend on hardware; time does. On a GPU, timings need a `torch.cuda.synchronize()` call before and after the operation, because calls return before the work is done; without it everything looks very fast. Repeat several times and average. The speed you measure divided by the speed the spec sheet promises is the model FLOPs utilization, or MFU. It ignores communication and other overheads, never exceeds 1, and about 0.5 on a modern model is a result to be happy with. A plain matrix product might reach 0.8, and 0.1 means that something is wrong. The promised figure already has the division by two, and why only half of it is reached is the next topic.
**In this book:** [Resource Accounting › 4. Compare with the hardware: MFU](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#4-compare-with-the-hardware-mfu).

### [39:30–44:10](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=2370) Memory bandwidth, and a ReLU on one vector

The speed of FLOPs per second also depends on the data type: float32 runs slowly on current chips, bfloat16 and FP8 fast. The cartoon of an accelerator has a high-bandwidth memory and, apart from it, the compute cores: every input has to be sent from the memory to the accelerator and every output sent back, so a second limit matters: the H100 moves 3.3 terabytes per second. Size therefore influences speed as well as capacity. A ReLU on a BF16 vector of one million elements reads 2n bytes and writes 2n bytes, and does n comparisons. Moving the bytes takes about one microsecond, the arithmetic about one nanosecond.
**In this book:** [Resource Accounting › 5. Find the bottleneck: arithmetic intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#5-find-the-bottleneck-arithmetic-intensity) · [GPUs, TPUs and kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [44:10–48:06](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=2650) Two intensities

Communication and computation are overlapped, so the total time is the larger of the two, an idealization that is good enough here. An operation is memory-bound when moving the bytes takes longer and compute-bound when the arithmetic does; the ReLU is memory-bound. The same comparison is written as one number. The intensity of an accelerator is its FLOPs per second divided by its bytes per second, about 295 for an H100, roughly 300 operations per byte moved. The arithmetic intensity of an operation is the work it does per byte it moves, a quarter for the ReLU. The operation is memory-bound when its intensity is below the accelerator's. Moving data is expensive, so most operations are memory-bound, and an intensity of 0.25 should hurt to see.
**In this book:** [Resource Accounting › 5. Find the bottleneck: arithmetic intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#5-find-the-bottleneck-arithmetic-intensity).

### [48:06–52:00](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=2886) GELU, dot product, matrix-vector: all memory-bound

More work per byte is the way out, and the GELU activation tries: about 20 FLOPs per element for the same 4n bytes, an intensity near 5, still far below 295. A complicated activation therefore costs the same time as a ReLU, because arithmetic is not the bottleneck. A dot product of two vectors moves 4n + 2 bytes for 2n − 1 FLOPs, an intensity near one half. A matrix-vector product moves 2n² + 4n bytes for about 2n² FLOPs, barely better. Both are memory-bound.
**In this book:** [Resource Accounting › 5. Find the bottleneck: arithmetic intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#5-find-the-bottleneck-arithmetic-intensity).

### [52:00–57:00](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=3120) Matrix multiplication is the exception, and the roofline plot

The product of two n × n matrices moves about 6n² bytes and does n² dot products, an intensity near n/3 that grows with the matrix, since n² numbers travel and n³ are computed. This is the reason for large batch sizes and large matrices: below the accelerator's intensity, shrinking a problem does not speed it up, and only past it is the chip saturated. Transformers are large matrix products with small operations in between, and they were designed that way. Inference is different: one token at a time makes the layer a matrix-vector product, which is memory-bound, while training processes a whole sequence at once. Intensity also depends on the precision. Asked why chips are built with compute that idles while waiting for memory, he answers that the GPU lecture will help, and that anyone with a solution should tell NVIDIA's chief executive. The roofline plot puts arithmetic intensity on the horizontal axis and the realized FLOPs per second on the vertical one; each line is one accelerator, such as an H100 or a B200, rising until it flattens at peak speed.
**In this book:** [Resource Accounting › 5. Find the bottleneck: arithmetic intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#5-find-the-bottleneck-arithmetic-intensity) · [Inference › 1. Count one decoding step](../10-llm-internals/08-inference.md#1-count-one-decoding-step).

### [57:00–1:00:00](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=3420) The running example: a deep network

The lecture now counts what training needs, on a running example: a batch of B inputs of D dimensions, then L layers, each a D × D matrix product followed by a ReLU. The parameters are D² times L. In PyTorch it is a stack of blocks, each with its own weight matrix. A small regression example recalls the mechanics of the backward pass: after calling it, the weight's gradient attribute is set.
**In this book:** [Resource Accounting › 3. Count FLOPs](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#3-count-flops).

### [1:00:00–1:06:50](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=3600) Gradients cost twice the forward pass

Take two linear layers without the activation, written with einsum. In the backward pass each layer computes two gradients: the gradient with respect to its input, which is the incoming gradient times the weight matrix, summed over the output dimension, and the gradient with respect to its weight, which is the input times the incoming gradient, summed over the batch dimension. Named dimensions remove the guesswork about which matrix is transposed. Both are matrix products over the same three dimensions as the forward pass, so the backward pass costs exactly twice the forward. For the whole network the forward pass costs 2 × B × parameters FLOPs, the backward pass 4 × B × parameters, and the total is 6 × B × parameters, which is where the 6ND formula comes from. It approximates transformers too, as long as the context length is not large; long contexts add a term that grows with its square.
**In this book:** [Resource Accounting › 3. Count FLOPs](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#3-count-flops) · [Resource Accounting › 6. Count memory for training](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#6-count-memory-for-training).

### [1:06:50–1:12:00](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=4010) Counting memory for training

The other piece of training is the optimizer: the example uses AdaGrad from 2011, which lies between SGD and Adam and keeps the sum of squared gradients. It predates Adam; momentum looks at the first moment of the gradient, Adam at both moments. Assignment 1 asks for Adam. Each parameter group has an optimizer state, storage the optimizer uses while it runs; AdaGrad reads the accumulated squares, adds the new gradient and stores the result back, then updates the parameters by dividing by its square root. Memory has four parts. Parameters take 2 bytes each in BF16, D² times L of them. Activations take 2 bytes for each of B × D elements in each of L layers. Gradients are a copy of the parameters, 2 bytes each. The optimizer state takes 4 bytes per parameter in FP32, because accumulating squares over many steps is not stable in BF16, and 8 bytes with Adam, which stores two moments. The optimizer state is a large share of the memory but not a speed bottleneck; what it limits is the size of the model that fits.
**In this book:** [Resource Accounting › 6. Count memory for training](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#6-count-memory-for-training).

### [1:12:00–1:16:00](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=4320) Two ways to use less memory

Memory limits both the model that fits and sometimes the speed, so it should be reduced. Gradient accumulation: batches should be large enough for stability, up to a critical batch size that a later lecture covers, but activation memory grows with the batch, so compute the gradient on micro-batches and add the gradients up without zeroing them; update the parameters and zero the gradients every batch-size-divided-by-micro-batch-size steps. Activation checkpointing, also called gradient checkpointing or rematerialization: the forward pass keeps the activations of only some layers, and the backward pass recomputes the rest from the last saved one. It is one call, `torch.utils.checkpoint`, on a layer. In the example, where each block stores a pre-ReLU and a post-ReLU tensor, it halves activation memory. At the extreme nothing is stored and the recomputation grows with the square of the depth, because every layer is recomputed from the beginning. The balanced choice stores every square-root-of-L-th layer, for a memory and a recomputation overhead that both grow with the square root of the depth.
**In this book:** [Resource Accounting › 6. Count memory for training](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#6-count-memory-for-training) · [Parallelism › 6. The rest](../10-llm-internals/06-parallelism.md#6-the-rest).

### [1:16:00–1:18:00](https://www.youtube.com/watch?v=kuYAsz7zspQ&t=4560) Summary

Everything operates on tensors. einops is offered as a way of thinking about tensor operations. The formula of six times the batch size times the number of parameters is now a count of the FLOPs of a training step. Arithmetic intensity and roofline analysis tell where the bottleneck of a computation lies, memory or arithmetic, and the rule to remember is that "matrix multiplications are compute bound, basically everything else is memory bound". Gradient accumulation and activation checkpointing reduce memory, and less memory allows larger batch sizes. The next lecture is on architectures.
**In this book:** [Resource Accounting › What the practitioners say](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#what-the-practitioners-say).

## What to take away

- A tensor takes elements times bytes per element; bfloat16 for the model and float32 for the optimizer states is the usual mix.
- A training step costs about 6 × tokens × parameters FLOPs: two for the forward pass, four for the backward pass, which computes two gradients per layer.
- Model FLOPs utilization, measured speed over promised speed, is about 0.5 on a good run; the spec sheet's number includes sparsity and must be halved.
- An operation is memory-bound when its arithmetic intensity is below the accelerator's, roughly 300 FLOPs per byte on an H100; large matrix products are the exception.
- With Adam, a parameter needs 12 bytes for its value, gradient and optimizer states, before activations; gradient accumulation and activation checkpointing reduce memory, checkpointing at the price of recomputation.

## Sources

- Course staff, "PyTorch (einops), resource accounting (FLOPs, memory, arithmetic intensity)", Stanford CS336 Language Modeling from Scratch, Spring 2026: [video](https://www.youtube.com/watch?v=kuYAsz7zspQ).
- Course page: <https://cs336.stanford.edu/>.
