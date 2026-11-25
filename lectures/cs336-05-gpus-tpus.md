# Lecture guide: GPUs, TPUs

**Lecturer:** course staff · **Course:** Stanford CS336 Language Modeling from Scratch, Spring 2026, lecture 5 · **Length:** 1:20:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=izZba4UA7iY)
**Chapters that cite this lecture:** [05. GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md)

> **In one sentence:** Tatsu Hashimoto builds the mental model of a GPU, many simple processors beside a hierarchy of memories, and uses it to explain six tricks that make code fast, then assembles them into FlashAttention.

## Before you watch

This is the first lecture of the systems part, and it assumes no GPU programming. The one idea from earlier lectures that it relies on is arithmetic intensity, computation per byte moved. Hashimoto is not a systems person himself and points to three resources he used: Horace He's explainers, the GPU Mode community (formerly CUDA Mode) and the TPU book by Google engineers, whose exercises resemble one of the course assignments. The chapter [GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md) follows the lecture.

## The lecture, part by part

### [0:00–3:20](https://www.youtube.com/watch?v=izZba4UA7iY&t=0) The systems part begins

Systems, to Hashimoto, is the most reasonable part of the stack: one can reason through every piece in logical steps. A GPU still feels like magic at first. His promise is that by the end the opening plot makes sense: the throughput of a matrix multiplication against its size, which rises and falls in strange patterns. Even people who will work on architectures need the hardware model, since scaling means using resources well. The lecture has three parts: the hardware and its programming model, six tricks, and FlashAttention as the victory lap.
**In this book:** [GPUs, TPUs and Kernels › Why this matters](../10-llm-internals/05-gpus-tpus-and-kernels.md#why-this-matters).

### [3:20–8:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=200) From clock speed to parallelism, and CPU against GPU

Compute is the currency: faster hardware, better utilization, more chips and better parallelization all bring better models. In the 1990s speed came from clock rates; that scaling ended around the 2000s, and transistors kept shrinking without getting faster. So hardware scales horizontally, with more units running in parallel. Floating-point throughput per GPU took off around the P100 and V100, helped by tensor cores from 2017 and later by structured sparsity and lower number formats. A CPU is built for fast serial work with complex branching: large control units, few arithmetic units, low latency. A GPU is built for throughput: a task may take long and be paused for others, but hundreds of lightweight cores add up to a large aggregate.
**In this book:** [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [8:00–13:28](https://www.youtube.com/watch?v=izZba4UA7iY&t=480) Inside a GPU: streaming multiprocessors and the memory hierarchy

The basic unit is the streaming multiprocessor, or SM, close to a core: an independent compute unit, an A100 has 128 of them, each programmable on its own, with access to global memory. The memory side matters as much. Registers are the smallest and fastest. L1 cache and shared memory answer in about 20 to 30 cycles, L2 is much slower, and global memory about ten times slower than L1. The 144 GB of an H200 are global memory. Global memory sits on chips outside; L2 and L1 sit on the chip, next to the compute. Why not build a chip entirely of fast memory? It costs hundreds of times more and draws more power, so practical accelerators keep a hierarchy. He names Grok's chip, with very large fast memory, as the exception that pays off for inference. To a question: a cache is managed by hardware, shared memory is programmable.
**In this book:** [GPUs, TPUs and Kernels › The core idea](../10-llm-internals/05-gpus-tpus-and-kernels.md#the-core-idea) · [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [13:28–17:18](https://www.youtube.com/watch?v=izZba4UA7iY&t=808) The programming model: threads, blocks and warps

Three terms carry the execution model. A thread does work in parallel with others, and all threads execute the same instructions on different inputs, the SIMT model, a trade of programmability for efficiency. A block is a group of threads guaranteed to run on one SM, so it shares that SM's shared memory; this makes tiling possible later. A warp is the scheduling unit: 32 consecutively numbered threads that execute together, which keeps scheduling cheap. In questions he confirms that divergence is a matter of the warp, and that the scheduler picks which warp runs next. The memory model from inside out: registers, local memory within an SM, shared memory within a block, global memory at a latency cost, a rarely used constant memory, and host memory when a model must overflow the GPU. Outside shared memory everything is slow, so grouping work to cut global reads is the theme of the lecture.
**In this book:** [GPUs, TPUs and Kernels › 1. The programming model](../10-llm-internals/05-gpus-tpus-and-kernels.md#1-the-programming-model).

### [17:18–22:37](https://www.youtube.com/watch?v=izZba4UA7iY&t=1038) TPUs: convergent evolution

TPUs get two slides, because they are the alternative evolution of the same idea. They are simpler: lighter control units and much larger matrix multiply units, with the same slow high-bandwidth memory and fast local memory. The largest differences are in networking, not in the chips; every GPU concept maps onto a TPU concept, as a table in the JAX book shows. The GPU's matrix multiply unit, the tensor core, corresponds to the TPU's MXU, and both are systolic arrays. One confusion: TPUs also call their processors tensor cores. A TPU has few, large matrix units where a GPU has many, small ones, so the GPU is more flexible; his batch-size sweep once stopped at 64 because the TPU would not take a smaller input. GPUs scale by adding SMs, the SIMT model makes them deceptively easy to program, and threads are light enough to be swapped whenever a warp stalls. Before the V100, researchers programmed shaders to multiply matrices; since then the dedicated unit has made the matrix product the privileged operation, running at more than ten times the speed of any other floating-point operation on the chip, which is why every compute-scaling architecture contains one.
**In this book:** [GPUs, TPUs and Kernels › 6. TPUs](../10-llm-internals/05-gpus-tpus-and-kernels.md#6-tpus).

### [22:37–30:09](https://www.youtube.com/watch?v=izZba4UA7iY&t=1357) Components scale at different rates

Compute throughput grows fastest, memory bandwidth slowly, and the interconnect between GPUs slower still. Early GPU programmers could ignore memory; the further right the plot goes, the wider the gap, so most optimizations are memory optimizations. The mental model to keep: massively parallel, compute growing faster than memory, everything must respect the memory hierarchy. Questions fill the rest: before the V100 there was no matrix unit, though the many ALUs still gave decent throughput; L2 is slower than L1 by distance and interconnect, and the TPU's equivalent is much faster by design. Does the gap change chip layouts? Yes: prefill-decode disaggregation, which began in the previous year, puts the matrix-heavy prefill on one chip and the memory-bound decoding on another, and one Chinese open model, StepFun 3, even splits attention and MLP layers across accelerators.
**In this book:** [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed) · [Resource Accounting › 5. Find the bottleneck: arithmetic intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#5-find-the-bottleneck-arithmetic-intensity).

### [30:09–34:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=1809) The plot, the roofline, and control divergence

The goal of the second part is the throughput plot: the size of two square matrices multiplied against the work done per second. Throughput rises with size, since more work keeps the hardware busy, but with strange dips. The roofline model predicts a diagonal part, where memory limits, and a flat part, where the matrix units are saturated and more work no longer helps. Efficient code sits on the flat part, so the task is to raise operational intensity, and six tricks do it. The first is different in kind and comes from SIMT. An if statement on a GPU is executed by every thread: one branch runs while the threads of the other wait, then the other way round. This control divergence leaves compute gaps, which is why GPU code multiplies by a mask instead of branching, for instance in a ReLU.
**In this book:** [GPUs, TPUs and Kernels › The core idea](../10-llm-internals/05-gpus-tpus-and-kernels.md#the-core-idea) · [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks).

### [34:00–38:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=2040) Low precision: a black art

Low-precision computation is where he sees NVIDIA investing most. A good part of the growth in throughput came from number formats, from float32 to bfloat16 to 8-bit integers: half the bits means half the bytes moved. A ReLU in float32 moves 8 bytes for one operation. In a matrix unit the formats are mixed: inputs are cast down before the product, the partial sums accumulate in full precision, and the result may be emitted in float32. The black art is deciding which operation takes which format, a softmax or an exponential perhaps float32, and it took years of slow empirical work to keep training stable while lowering precision. FP8 has no single canonical format: E4M3 with more mantissa and E5M2 with more exponent serve different places.
**In this book:** [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks) · [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [38:00–42:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=2280) MXFP8: block scaling and its price

In plain FP8 training every value shares one float32 scaling factor, needed because four exponent bits overflow and underflow quickly. But magnitudes differ across one matrix, so the MX formats use many scaling factors, one per block of elements. In MXFP8 the factors are themselves 8 bits in the E8M0 format, exponent only and therefore powers of two, the elements keep more mantissa, and one factor serves 32 elements. He asks the class to spot the flaw: the blocks of a transposed matrix are not the transposed blocks. Transposing now needs re-quantization, so training in MXFP8 keeps two copies of every quantized matrix. Only layers known to be safe are quantized. The saving on matrix products is 20 to 30%, not twofold, because quantization itself costs. To a question: the last layer is hard to quantize because it drives so much of the loss.
**In this book:** [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks) · [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [42:00–46:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=2520) MXFP4, and questions on quantization

MXFP4 fits on one slide: every value lies between −6 and 6, in blocks of sixteen 4-bit numbers with one FP8 scaling factor. One paper has trained in FP4; he has not heard of a serious large model trained with it in the wild, though the next generation probably will. In questions: anything can be quantized, but matrix products give the large throughput gains that make it worthwhile; the compute gain of a product is linear in the bits saved, diluted by the cost of quantizing and dequantizing; scaling factors are an implementation choice, a scan for the extreme value or running statistics, fitted at inference and not trained; structured sparsity has one clear success, mixture of experts, while its other gains have washed out against the loss of representational power; and small quantized models today come from training a larger model and quantizing it down, with some quantization-aware training and some post-training quantization, a science that industry teams still study.
**In this book:** [GPUs, TPUs and Kernels › What the practitioners say](../10-llm-internals/05-gpus-tpus-and-kernels.md#what-the-practitioners-say).

### [46:00–50:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=2760) Operator fusion

Think of a GPU as a factory: a memory warehouse, a compute workshop and a conveyor between them. Scale up the workshop and the conveyor is the limit, worse still when many operations each send their inputs and results across. Better one large factory that takes raw materials once and returns finished products once. This is operator fusion. For the sum of a squared sine and a squared cosine, the PyTorch graph has five operations, each reading from and writing to global memory. One kernel can read once, do everything inside the SM and write once. Simple chains like this are fused by compilers: torch.compile, or JAX's compiler. Advanced fusions need manual work.
**In this book:** [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks).

### [50:00–52:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=3000) Recomputation

Backpropagation stores the activations of the forward pass. Three stacked sigmoids give one read and three writes on the way forward and as many on the way back: eight memory accesses for almost no arithmetic. When computation is abundant and memory expensive, another graph wins: read the input, compute, write the output, and in the backward pass recompute the intermediate activations where they are needed. That is five accesses. The computation is the same; some extra arithmetic buys some memory.
**In this book:** [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks) · [Resource Accounting › 6. Count memory for training](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#6-count-memory-for-training).

### [52:00–58:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=3120) DRAM bursts, coalescing, and row-major reads

Global memory is DRAM, and DRAM delivers bursts: reading one position brings its neighbours almost for free, up to 128 bytes of one contiguous block. A memory access is coalesced when all the threads of a warp fall in the same burst. To a question on why: the cells form a grid, the amplifiers work a column at a time, and charging the column is the slow step, after which several readouts are cheap. This matters for matrices. In a row-major matrix, threads that move down a column touch a different burst window for every element and read almost the whole matrix to obtain one column. Threads that move along a row read whole blocks at once.
**In this book:** [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks).

### [58:00–62:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=3480) Tiling: reuse in shared memory

Tiling is the trick with the largest effect. Cut the data into tiles, load a tile into shared memory once, and read it there as often as needed. In an n × n matrix product every input element is read n times if the reads go to global memory. With tiles of size t each element is read n/t times from global memory and t times inside the tiles; in the limit of one tile, once. To a question: the limit is that fast memory is small and very expensive. Data and tensor parallelism across GPUs resemble tiling too. Every matrix product kernel in a library tiles underneath, though PyTorch is not perfect.
**In this book:** [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one).

### [62:00–66:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=3720) Tile sizes, padding, and a speed-up from a larger vocabulary

Tiles bring subtle problems. With tiles of 128, a 256 × 256 matrix is four perfect tiles; add one to the size and two thin, nearly empty tiles appear. Tile sizes are therefore tuned to the matrix sizes, the coalescing rule and the shared memory of the device; PyTorch's max-autotune option benchmarks tile sizes for fifteen minutes and finds real gains. If rows do not line up with the bursts, reading one tile takes twice the reads, so matrices are padded until the boundaries agree. His favourite strange example: in the nanoGPT speedrun, Andrej Karpathy raised the vocabulary size from 50,257 to 50,304 and gained 25%. The advice is not to think about tiles, unless writing kernels, but to think about matrix sizes: powers of two, divisible by 32.
**In this book:** [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one) · [GPUs, TPUs and Kernels › What the practitioners say](../10-llm-internals/05-gpus-tpus-and-kernels.md#what-the-practitioners-say).

### [66:00–72:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=3960) The plot explained: alignment and wave quantization

The opening plot is now readable. The upward slope is the roofline. Coloured by divisibility, the lines show that odd and barely even sizes have poor throughput, while sizes divisible by 16 or 32 carry no penalty: not because powers of two are magic, but because such sizes fill whole bursts. The periodic cliffs have another cause. With tiles of 256 by 128, a size of 1792 gives 98 tiles and 1793 gives 120. The A100 has 108 SMs, so 98 tiles run in one round and 120 leave 12 for a second round in which most of the GPU idles: wave quantization. Liang calls this GPU trivia and dislikes it, he says, and he loves it. In questions: why 108 SMs is a question for NVIDIA's chief executive; larger divisors bring no further benefit, it is a divisor property; more fast memory is barred by cost, proximity and power; and wafer-scale chips bring compilation problems he does not know.
**In this book:** [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed) · [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one).

### [72:00–76:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=4320) FlashAttention: tiled products and the online softmax

The finale turns the tricks into FlashAttention, one large improvement in attention that is all systems: from PyTorch's naive implementation to one cleverly fused kernel, with a dramatic drop in serving latency, most of it from fewer bytes moved out of high-bandwidth memory. The paper claims only tiling and recomputation. Attention is three matrix products and one softmax, and the products are tiled in the usual way. The difficulty is the softmax, a global operation that ties every tile together. The key observation is the online softmax. Instead of exponentiating everything after subtracting the largest score, keep a running maximum, replace it whenever a larger value arrives and correct what was accumulated so far, keep a running sum of exponentials, and divide by it at the end. Because it runs block by block, each tile can be processed without seeing the others.
**In this book:** [GPUs, TPUs and Kernels › 7. FlashAttention, the tricks together](../10-llm-internals/05-gpus-tpus-and-kernels.md#7-flashattention-the-tricks-together).

### [76:00–1:20:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=4560) Fusion, recomputation, and the lesson

The diagram from a later FlashAttention paper shows the pieces: the products and the exponentials are computed tile by tile in fast memory, the running sums are a very small amount of state kept in shared memory or registers, the multiplication by the values is tiled too, and the division comes at the very end. Fusion holds it together in one kernel, and in the backward pass the n × n attention matrix is not stored but recomputed tile by tile. His lessons: understand the hardware down to the bottom, so as not to copy rules such as multiples of 32 without knowing why; matrix products are the arithmetically dense core operations; and because compute outruns memory, data movement deserves as much thought as arithmetic, including in architecture design.
**In this book:** [GPUs, TPUs and Kernels › 7. FlashAttention, the tricks together](../10-llm-internals/05-gpus-tpus-and-kernels.md#7-flashattention-the-tricks-together) · [GPUs, TPUs and Kernels › Key takeaways](../10-llm-internals/05-gpus-tpus-and-kernels.md#key-takeaways).

## What to take away

- A GPU is many streaming multiprocessors next to a memory hierarchy; compute has grown much faster than memory, so nearly every optimization moves fewer bytes.
- Threads in a warp execute the same instruction, so branches cost; low precision halves the bytes each time a format loses half its bits, at the price of deciding which operation tolerates it.
- Operator fusion, recomputation, coalesced reads and tiling all cut traffic between global memory and the fast memory inside an SM.
- Matrix sizes divisible by 32 fill whole memory bursts, and a matrix that needs one more round of tiles than the chip has multiprocessors leaves most of it idle.
- FlashAttention is these tricks together: tiled products, an online softmax that needs no global pass, fusion into one kernel, and recomputation in the backward pass.

## Sources

- Tatsu Hashimoto and the course staff, "GPUs, TPUs", Stanford CS336 Language Modeling from Scratch, Spring 2026: [video](https://www.youtube.com/watch?v=izZba4UA7iY).
- Course page: <https://cs336.stanford.edu/>.
