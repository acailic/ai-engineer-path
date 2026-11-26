# Lecture guide: TinyEngine and Parallel Processing

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 11 · **Length:** 1:12:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=wl1UEnIOVek) · **Slides:** [slides](https://www.dropbox.com/scl/fi/z1980bzepegz85ara200n/Lec11-TinyEngine.pdf?rlkey=5evtfesbourbo03nlhazmiy1r&st=ehihqr5t&dl=0)
**Chapters that cite this lecture:** [07. TinyML: Microcontrollers and TinyEngine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md)

> **In one sentence:** Song Han teaches how to make a network run fast on small devices by programming close to the hardware: loop optimization, SIMD, multithreading and CUDA, then function-preserving inference tricks (im2col, in-place depthwise convolution, memory layouts, Winograd), the basis of his TinyEngine library and of running a language model on a laptop.

## Before you watch

The chapter [TinyML: Microcontrollers and TinyEngine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) uses this lecture for its step on the inference engine; [GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md) teaches the CUDA model and tiling from another course. The lecture assumes a first course in computer architecture: caches, cache lines and branch prediction.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=0) TinyAI's constraints

TinyAI runs in phones, cars, robots and smart offices on very little. Han's table: a cloud GPU has 80 gigabytes of memory and about 2,000 TOPS, an Apple M2 Ultra 100 gigabytes and 30 TOPS, a phone 8 to 24 gigabytes, a microcontroller 300 kilobytes and a fraction of a TOPS, several orders of magnitude apart. The lecture matters for Lab 5, deploying a language model on a laptop.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Why this matters](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#why-this-matters).

### [2:00–4:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=120) Microcontroller against laptop, and the memory hierarchy

A MacBook Pro against a microcontroller: twenty CPU cores against one, 3 gigahertz against 200 megahertz, a GPU and a neural engine against none, caches of megabytes against kilobytes, 64 gigabytes against a few hundred kilobytes. There is no operating system, so the program manages memory itself. The memory hierarchy runs from registers through caches to memory and storage: capacity grows into terabytes and latency grows with it, so the rule is to stay in the cache.
**In this book:** [TinyML: Microcontrollers and TinyEngine › The core idea](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#the-core-idea) · [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [4:00–10:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=240) Loop reordering

Matrix multiplication is three nested loops, convolution six, so loop code decides speed; the aims are cache locality and few branches. In the naive i-j-k order, A is read along rows but B down columns, so the elements of B visited in succession sit in different cache lines. Swapping to i-k-j reads B along rows too. A student notices that C then suffers, since many partial sums are live at once instead of one element being finished at a time; the gain on B outweighs it. A change of a few lines cuts the time from 24,000 to about 2,000 milliseconds, 12 times, and the compilable code is posted.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine).

### [10:00–18:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=600) Loop tiling

When matrices are larger than the cache, cache misses are heavy. Tiling partitions a loop's iteration space into blocks small enough to fit: one extra loop bounds the working set of B by n times the tile size, a second makes it tile size squared, a third does the same for A, so that all three tiles are tile size squared and the tile size is chosen so they fit in the cache together, where data is reused without reloading. With two levels of cache, add another level of tiling: the square of the smaller tile fits L1, the product of the two tile sizes L2. Tiling brought 24,000 milliseconds down to 1,200, about 19 times.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine) · [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one).

### [18:00–22:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=1080) Loop unrolling

Each pass through a loop tests its bound, and a mispredicted branch flushes the pipeline. Unrolling copies the loop body several times, four in his example, so that no branch occurs inside the body: pointer arithmetic and loop tests fall four times over, while the code of the inner loop grows four times, the trade of binary size for speed. Measured, 24,000 milliseconds became 8,000. Students ask about dimensions that are not multiples of the factor, which need remainder code, though network dimensions are often powers of two, and about compilers: they already unroll, though not for every matrix dimension, especially tall, thin against short, fat ones.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine).

### [22:00–30:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=1320) SIMD programming

The instruction set is the contract between software and hardware: add, compare, jump, load, store. CISC processors such as x86 have many specialized instructions; RISC processors such as ARM and RISC-V use short ones, so one CISC add may take four RISC instructions. Neural networks are easy to parallelize, so one instruction can operate on several data: a 128-bit vector register holds four single-precision numbers, and one multiply handles four at once, which also spreads the cost of decoding an instruction over four operations. Han shows a dot product in x86 intrinsics, load, multiply and add on packed single-precision values with a step of four, and the ARM NEON equivalents on quadword vectors, then a matrix multiplication built from them.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine).

### [30:00–40:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=1800) Multithreading

Threads of one process share code, data and open files but keep their own registers, stack and program counter, and can run on different cores. They speed up work and keep the processor busy when a thread waits on I/O, which, with very many threads, is the principle of GPUs. With pthreads, matrix multiplication splits by rows: create the threads with a function to run, give each a start and end row from its thread ID, and join them all at the end. Four threads brought 24,000 milliseconds to 5,800, 4.1 times. OpenMP does the same with one directive, a pragma that makes the i loop parallel, with synchronization built in, and Han calls its code much cleaner than pthreads'.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine).

### [40:00–44:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=2400) The CUDA programming model

After a break: CUDA, which Han motivates by the previous day's Nobel prizes for work that relied on GPUs, including Hinton's. NVIDIA introduced CUDA in 2006 as a C-like language for general-purpose GPU computing. Threads form two levels: a grid of thread blocks, each of many threads, with identifiers of up to three dimensions. In his example a 2 by 3 grid of blocks with 3 by 4 threads each launches 72 threads with one line of code; each thread derives its position from its block's identifier and its own, and adds the element at that position.
**In this book:** [GPUs, TPUs and Kernels › 1. The programming model](../10-llm-internals/05-gpus-tpus-and-kernels.md#1-the-programming-model).

### [44:00–49:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=2640) CUDA memory, and why launches are fused

The host, the CPU, and the device, the GPU, have separate address spaces: allocate on the device, copy to and from the host, and never dereference a device address from the host. Inside a kernel three spaces are visible: global memory, open to all threads; shared memory, private to a block; and local memory, private to a thread. A CUDA matrix multiplication on an old 2080 Ti spends 6 milliseconds in the kernel and about 200 in total against 24,000 on the CPU. The gap shows that launching a kernel is expensive, so do as much as possible per launch: kernel fusion folds the operations before and after a matrix multiplication, such as the activation function, into one kernel.
**In this book:** [GPUs, TPUs and Kernels › 1. The programming model](../10-llm-internals/05-gpus-tpus-and-kernels.md#1-the-programming-model).

### [49:00–54:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=2940) A tiled kernel, and tensor cores

The CUDA kernel tiles the matrices: each block loads its tiles of A and B into shared memory, the threads wait for the loads, multiply and write their part of C. Tensor cores, built for deep learning, finish a small matrix multiplication per cycle, 4 by 4 by 4 on Turing and 4 by 8 by 4 on Ampere, and gain further at lower precision; on an H100 Han shows them reaching some 60 times the throughput of CUDA cores, with the gap widening as matrices grow. Programs call them through matrix-multiply-accumulate intrinsics of fixed size, 16 by 8 by 16 in his example, and compose larger products by calling the intrinsic per tile, in any order.
**In this book:** [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one).

### [54:00–58:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=3240) Function-preserving optimizations: im2col

Pruning, quantization, search and distillation change the network. The remaining techniques keep the mathematics and change only the implementation. Matrix multiplication is a basic building block; convolution is six loops. Im2col turns convolution into matrix multiplication by laying every receptive field out as a row of a matrix, which then multiplies the matrix of flattened kernels: simple, and a very common technique, at the price of duplicating overlapping input elements in memory. Implicit GEMM computes the same thing on the original tensors without materializing the copy.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine).

### [58:00–1:00:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=3480) In-place depthwise convolution

Depthwise convolution, common in MobileNet-style blocks, processes each channel on its own. A naive implementation keeps input and output, twice C times H times W. As in the MCUNetV2 paper, each channel can be computed into one small constant buffer and written back over its own input, so the memory needed is C plus 1 times H times W.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 5. Plan memory like a compiler plans registers](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-5-plan-memory-like-a-compiler-plans-registers).

### [1:00:00–1:04:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=3600) Memory layout: NHWC or NCHW

Since data movement is very costly, the order of axes in memory matters. A pointwise, 1 by 1, convolution combines all channels of one pixel, so it wants channels adjacent: the NHWC layout, with the channel innermost, gives contiguous access, whereas under NCHW the accesses are discontinuous. Depthwise convolution works within one channel across pixels and wants the opposite, NCHW. Pointwise and depthwise convolution thus prefer different layouts; Han replays an animation of both access patterns to show how much the sequence of accesses matters for locality and memory footprint.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine).

### [1:04:00–1:08:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=3840) Winograd convolution

Winograd convolution cuts multiplications while preserving the result. A 3 by 3 kernel over a 4 by 4 input produces four outputs at 9 multiplications each, 36 per channel. Assuming the transformations are free, the input becomes 4 by 4, the filter is transformed too, and 16 elementwise products replace 36, 2.25 times fewer. The transformations are almost free: the input and output matrices contain only 0, 1 and −1, and the filter matrix adds one half, a one-bit shift. Han cites the paper that proves equality and encourages students to prototype it.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 4. Run it with an inference engine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-4-run-it-with-an-inference-engine).

### [1:08:00–1:12:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=4080) TinyEngine, and the labs

Combined, these techniques let his open-source TinyEngine run a language model on a laptop. Its TinyChatEngine runs Llama 2 at 7 and 13 billion parameters and Llama 3 with quantization, and TinyEngine also drives the object-detection, person-detection and visual-wake-word demos of the previous lecture; Lab 5 students may read the TinyChatEngine repository, a complete language-model inference engine. Labs 4 and 5 quantize a model to 4 bits with AWQ and run a local chatbot. Han recaps: microcontroller constraints, loop optimization, SIMD, multithreading and CUDA, and the inference optimizations.
**In this book:** [TinyML: Microcontrollers and TinyEngine › What the practitioners say](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#what-the-practitioners-say).

## What to take away

- Matrix multiplication's loops decide speed: reorder them for locality, tile them for the cache, unroll them to remove branches.
- One instruction can process four numbers (SIMD), several threads can split the rows (pthreads or OpenMP), and very many threads with tiled shared memory run on a GPU.
- Kernel launches are expensive, so fuse operations; tensor cores multiply small matrices per cycle.
- Implementation alone buys speed without changing the model: im2col, in-place depthwise convolution, the right memory layout and Winograd.

## Sources

- Song Han, "TinyEngine and Parallel Processing", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=wl1UEnIOVek).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
