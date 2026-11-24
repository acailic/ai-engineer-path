# 05. GPUs, TPUs and Kernels

**Level:** Professional · **Reading time:** 16 min · **Exercise:** 60 min
**Prerequisites:** [Resource Accounting](02-resource-accounting-flops-memory-and-arithmetic-intensity.md), for arithmetic intensity and the memory-bound versus compute-bound distinction.

> **In one sentence:** After this chapter you can describe a GPU's memory hierarchy, say what a kernel is and why speed is mostly about moving fewer bytes, and read a simple Triton kernel.

## Why this matters

Two teams implement the same Transformer. One trains at 45% of the hardware's peak speed, the other at 15%. Same model, same chips. The difference is in the kernels: the small programs that run on the GPU.

Tatsu Hashimoto opens Lecture 5 with a promise. He shows a plot of matrix-multiplication throughput against matrix size, full of jumps and dips, and says that by the end you will understand why it looks that way. His stated goal is to make "CUDA and GPUs less magic". CUDA is NVIDIA's programming language for GPUs.

## The core idea

A CPU is built to run a few threads as fast as possible. A GPU is built to run thousands of threads at once, each slow. It is organized as many **streaming multiprocessors** (SMs), each with its own small, fast memory, all fed by one large, slow memory.

The numbers for an H100, from Lecture 6's table:

| Memory | Size | Bandwidth |
|---|---|---|
| Registers, inside each SM | 256 KB per SM | About 401 TB/s |
| L1 cache and shared memory, inside each SM | 256 KB per SM | About 33 TB/s |
| L2 cache, shared by the chip | 50 MB | About 12 TB/s |
| High bandwidth memory (HBM), the GPU's main memory | 80 GB | 3.35 TB/s |

Each row down is an order of magnitude slower. So the rule of the whole unit is: move as little data as possible down to HBM and back.

Lecture 5's analogy is a factory. The SM is the workshop, HBM is the warehouse, and every trip to the warehouse costs time. The analogy breaks in one place: a real factory can stock a shelf once and forget it. A GPU's fast memory is so small that a program must keep refilling it, in an order that avoids repeated trips.

A **kernel** is the function that runs on the GPU. When PyTorch executes an operation such as `a + b`, it launches a kernel. A program that adds, then multiplies, then applies an activation launches three kernels and visits HBM after each one.

## How it works, step by step

### 1. The programming model

- A **thread** runs the kernel's code on one small piece of the data.
- A **thread block** is a group of threads that share memory. A block runs on one SM.
- The **grid** is all the blocks of one kernel launch.

Blocks exist because some operations need threads to cooperate. Adding two vectors needs no cooperation: one thread per element. A matrix product needs threads to share the inputs, so they must live on the same SM.

### 2. The hardware facts that decide speed

| Fact | What it means | What goes wrong |
|---|---|---|
| Warps | Threads run in groups of 32 that execute the same instruction at the same time | If threads in a group take different branches, the branches run one after another (control divergence) |
| Occupancy | Each thread uses up to 255 registers; the more it uses, the fewer threads fit on an SM | Too few threads leave the SM idle while it waits for memory |
| Bank conflicts | Shared memory has 32 banks; one access per bank per cycle | Threads that hit the same bank wait in line |
| Coalescing | The 32 threads of a group fetch memory in 128-byte lines | Threads that read scattered addresses fetch mostly unused bytes |
| Waves | Blocks are scheduled onto SMs in rounds | With 148 SMs and 160 blocks, the last round has 12 blocks and 136 SMs sit idle |

Hashimoto's warning about this table is that the programming model promises correctness if you ignore all of it. Performance does not forgive.

### 3. Five tricks

Lecture 5 builds speed from a short list.

1. **Lower precision.** Fewer bits per value means fewer bytes to move and faster matrix units.
2. **Fusion.** One kernel does several operations and never writes the intermediates to HBM. Computing `sin²(x) + cos²(x)` the naive way launches five kernels. Fused, it launches one.
3. **Recomputation.** Throw away an intermediate result and calculate it again later, instead of storing and reloading it. For three stacked sigmoids, Lecture 5's example gets by on five eighths of the memory accesses.
4. **Coalescing.** Arrange for neighboring threads to read neighboring addresses.
5. **Tiling.** Cut a large matrix product into small blocks that fit in shared memory, so each input is loaded from HBM once and reused many times.

### 4. Tiling, the big one

In a naive product of two n × n matrices, each of the n² outputs reads a row of one input and a column of the other. Every input value travels from HBM n times. With tiles of side t, a value is read n/t times from HBM and reused t times from shared memory.

### 5. Triton

Two ways exist to write a kernel. In CUDA you say what each thread does. In **Triton**, you say what each thread block does, and the compiler handles the threads. The pattern is always the same: load into shared memory, compute, write back once.

```python
# Illustrative pseudocode (Triton API, not executed here)
import triton
import triton.language as tl

@triton.jit
def add_kernel(x_ptr, y_ptr, out_ptr, n, BLOCK: tl.constexpr):
    pid = tl.program_id(0)                       # which block am I
    offs = pid * BLOCK + tl.arange(0, BLOCK)     # the elements this block owns
    mask = offs < n                              # ignore the tail past the end
    x = tl.load(x_ptr + offs, mask=mask)         # one read from HBM
    y = tl.load(y_ptr + offs, mask=mask)
    tl.store(out_ptr + offs, x + y, mask=mask)   # one write to HBM
```

Lecture 6's script calls Triton "generally powerful enough (especially when getting started)". Triton compiles the kernel to PTX, an assembly language for GPUs.

### 6. TPUs

A **TPU** is Google's accelerator. Hashimoto's point is that designing an energy-efficient machine-learning chip brings you to the same place either way: lightweight control, a large matrix-multiply unit, fast local memory, slow main memory. A GPU's tensor core, the circuit that multiplies small matrix blocks, maps almost exactly onto a TPU's matrix unit. The real difference between the two, in his words, is networking, not the chips themselves ([18:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=1080)).

### 7. FlashAttention, the tricks together

Attention computes three matrix products with a softmax in between. Naively, the n × n table of attention scores is written to HBM. FlashAttention avoids that:

- It tiles the products.
- It computes the softmax incrementally over tiles, keeping only running sums.
- It fuses everything into one kernel.
- In the backward pass it recomputes instead of storing the n × n table.

## Worked example

How much does tiling save in bytes?

```python
def bytes_from_hbm(n, tile=None):
    """Bytes read from main memory for an n x n times n x n product in bf16."""
    reads = 2 * n ** 3 if tile is None else 2 * n ** 3 // tile
    return reads * 2

bytes_from_hbm(4096)          # about 275 GB
bytes_from_hbm(4096, 128)     # about 2.1 GB
```

What to observe:

- The naive version reads each input value 4,096 times: about 275 GB from HBM, for a result that is 32 MB.
- Tiles of 128 cut that to about 2.1 GB, 128 times less.
- The arithmetic is unchanged: 2 × 4096³, about 1.4 × 10¹¹ FLOPs. Naive, that is half a FLOP per byte, deep in memory-bound territory. Tiled, it is 64 FLOPs per byte, which is compute-bound.

## What the practitioners say

Hashimoto introduces himself on the topic with "you know I am not a systems person, surprise" ([2:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=120)). His argument for learning it anyway is that compute has grown far faster than memory bandwidth and inter-GPU bandwidth, so the share of optimization that is about memory keeps growing ([26:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=1560)).

On tiling he calls it the biggest of the tricks, with the largest effect on performance, and notes that distributed strategies such as data and tensor parallelism are tiling ideas seen from farther away ([60:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=3600)). His closing wish is that you understand reasons rather than copy numbers: "I don't want you guys to be the kind of people that cargo cult" ([76:00](https://www.youtube.com/watch?v=izZba4UA7iY&t=4560)).

Percy Liang's Lecture 6 turns to practice. Its script repeats one instruction three times: benchmark and profile your code. Benchmarking gives wall-clock time for an operation, which is enough to compare implementations. Profiling shows which kernels ran and for how long. The kernel's name is informative: a name containing `cutlass`, `sm100` and `64x64x16` means NVIDIA's linear-algebra library, the Blackwell architecture, and a tile shape.

His case study is the GeLU activation. A naive PyTorch implementation launches several kernels and makes several round trips to HBM. The built-in version and a compiled Triton version each launch one kernel and are, in the script's word, significantly faster.

Two cautions from him. The hardware is "a lot messier than the programming model" ([16:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=960)). And CUDA calls return before the GPU finishes, so a timer that does not synchronize first measures nothing.

## Pitfalls

1. **Timing without a warm-up and a synchronize.** Fix: run the operation a few times, synchronize, then time.
2. **Optimizing before profiling.** Fix: profile first, and work on the kernel that takes the most time.
3. **Chains of small operations.** Each one is a separate kernel and a trip to HBM. Fix: fuse, or use a compiled path.
4. **Odd shapes.** Sizes that miss tile boundaries waste work, and leftover blocks leave SMs idle. Fix: pad to multiples of common tile sizes.
5. **Cutting precision blindly.** Fix: check accuracy after every change of data type.
6. **Writing CUDA when Triton would do.** Fix: start with the block-level view.
7. **Forgetting launch overhead.** Thousands of tiny kernels can spend more time launching than computing.

## Try it

Run this on any machine with PyTorch. A GPU is better; a CPU shows the same effect more slowly.

**Deliverable:** a script that times two implementations of `x³ + tanh(x)`: one written as ordinary PyTorch operations, one as a compiled function.

You are done when:

- Both agree on the output to within floating-point error on a tensor of one million elements.
- The script warms up, synchronizes and averages at least ten runs.
- It reports the time of each, and a profiler table listing the kernels each one launches.
- A comment explains the difference in one or two sentences, using the words "fusion" and "HBM".

**Stretch:** write the Triton add kernel from this chapter, test it against PyTorch's `+`, and time it.

## Key takeaways

- A GPU is many slow threads with a steep memory hierarchy. Speed comes from moving fewer bytes, not from doing more arithmetic.
- A kernel is a function launched as a grid of thread blocks. PyTorch launches one per operation.
- The tools are lower precision, fusion, recomputation, coalescing and tiling.
- Triton lets you write a kernel at the level of thread blocks: load, compute, write back.
- Benchmark to compare, profile to see where time goes, and repeat.

## Self-check

1. Why is shared memory important to a kernel?
   - A. It is the only memory large enough for model weights
   - B. It sits inside the SM and is much faster than main memory
   - C. It is shared between different GPUs
   - D. It holds the kernel's source code
2. What does operator fusion remove?
   - A. Floating-point operations inside the matrix product
   - B. Round trips of intermediate results to main memory
   - C. The need for thread blocks
   - D. The memory hierarchy itself
3. In a tiled matrix product with tiles of side t, how many times is each input read from main memory?
   - A. Once
   - B. t times
   - C. n over t times
   - D. n squared times
4. What does a profiler tell you that a benchmark does not?
   - A. The total wall-clock time
   - B. Which kernels ran and how long each took
   - C. The model's validation loss
   - D. The number of parameters
5. What is the unit of programming in Triton?
   - A. A single thread
   - B. A warp
   - C. A thread block
   - D. A whole node

<details><summary>Show answers</summary>

1. B. It is on the SM, an order of magnitude faster than HBM, and shared by a block's threads.
2. B. One kernel computes several steps and keeps intermediates on the chip.
3. C. n/t times from HBM, then t reuses from shared memory.
4. B. Benchmarks give end-to-end time; profiles break it down by kernel.
5. C. You describe what a block does with its piece of the data.

</details>

## Sources

- **Lecture:** Tatsu Hashimoto, "Lecture 5: GPUs, TPUs", Stanford CS336 Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=izZba4UA7iY), used at [motivation](https://www.youtube.com/watch?v=izZba4UA7iY&t=120), [TPUs](https://www.youtube.com/watch?v=izZba4UA7iY&t=1080), [memory wall](https://www.youtube.com/watch?v=izZba4UA7iY&t=1560), [tiling](https://www.youtube.com/watch?v=izZba4UA7iY&t=3600), [closing](https://www.youtube.com/watch?v=izZba4UA7iY&t=4560)
- **Lecture:** Percy Liang, "Lecture 6: Kernels, Triton, XLA", Stanford CS336 Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=xnDHaNUvHBg), used at [hardware](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=120), [messier than the model](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=960), [profiling](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=1560)
- **Reading:** Jacob et al., "How to Scale Your Model": [book](https://jax-ml.github.io/scaling-book/)
- **Reading:** Philippe Tillet, Hsiang-Tsung Kung and David Cox, "Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations" (MAPL 2019): [paper](https://doi.org/10.1145/3315508.3329973)
- **Reading:** Tri Dao, Daniel Y. Fu et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" (2022): [arXiv](https://arxiv.org/abs/2205.14135)
- **Reading:** Maxim Milakov and Natalia Gimelshein, "Online Normalizer Calculation for Softmax" (2018): [arXiv](https://arxiv.org/abs/1805.02867)

## Next

→ [Parallelism](06-parallelism.md), which applies the same principle one level up: moving less data between GPUs. For how kernels appear in the course's second assignment, see [Building Your Own](13-building-your-own-a-roadmap-through-the-assignments.md).
