# Lecture guide: Kernels, Triton

**Lecturer:** course staff · **Course:** Stanford CS336 Language Modeling from Scratch, Spring 2026, lecture 6 · **Length:** 1:28:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=xnDHaNUvHBg)
**Chapters that cite this lecture:** [05. GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md)

> **In one sentence:** Percy Liang turns the GPU model of the previous lecture into practice: where the clean programming model meets the hardware, how to benchmark and profile before writing a kernel, how to write kernels in Triton, and how tiling makes a matrix product fast.

## Before you watch

Watch the previous lecture first: this one starts from its picture of a GPU and its six tricks. The lecture is live-coded and walks through four kernels of increasing difficulty, an activation, a softmax over a row, a sum over a row longer than a block, and a tiled matrix product, which together are the ingredients of FlashAttention in the assignment. The chapter [GPUs, TPUs and Kernels](../10-llm-internals/05-gpus-tpus-and-kernels.md) keeps the code patterns in its section on Triton.

## The lecture, part by part

### [0:00–3:18](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=0) The picture of a GPU

A GPU is memory plus a chip. Across the A100, H100 and B200 generations a chip has on the order of 100 to 200 streaming multiprocessors, and that number has barely changed. Inside an SM, a B200 has 65,000 registers, 256 KB in all, also stable, and an L1 cache that is the same memory as shared memory, of which only shared memory is under the programmer's control. An L2 cache serves the whole chip, and the high bandwidth memory is large and growing. Bandwidth runs the other way from size: registers fastest, then L1, then L2, then high bandwidth memory, which at 8 terabytes per second is still not slow in absolute terms. The hierarchy to keep in mind: large memory is slow, far and big; fast memory is local to the SM, fast and small.
**In this book:** [GPUs, TPUs and Kernels › The core idea](../10-llm-internals/05-gpus-tpus-and-kernels.md#the-core-idea).

### [3:18–7:15](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=198) Threads, thread blocks and grids

A thread runs one piece of code over one small share of the data. Threads are organized into thread blocks, also called cooperative thread arrays, and blocks form a grid; launching a kernel launches a grid. Some details are hidden: H100s and B200s have clusters of blocks that share memory across a block, and the B200 has a tensor memory for its tensor cores. Why blocks at all? For elementwise operations such as GELU, one thread per element would suffice. For operations in which threads must communicate, a softmax or a matrix product, it would not, unless every thread paid for reads and writes to high bandwidth memory. A block is a set of threads that share the memory of one SM: it is scheduled there, reads from high bandwidth memory, computes, possibly through shared memory, and writes back. Triton, the main way kernels are written in this course, thinks natively in blocks.
**In this book:** [GPUs, TPUs and Kernels › 1. The programming model](../10-llm-internals/05-gpus-tpus-and-kernels.md#1-the-programming-model).

### [7:15–11:09](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=435) The model is simple; the hardware decides the speed

The programming model is a clean abstraction, enough for correctness: defining blocks and what each thread does is like writing Python. Speed, the whole reason to write kernels, depends strongly on the hardware, and five examples follow. The first is the warp. The threads of a block are grouped into warps of 32, so a block of 64 threads has two warps, and all threads of a warp execute the same instruction in lockstep. Control divergence arises when threads of one warp need different branches: first one branch runs, then the other, so branching is to be avoided. The useful side: an SM runs many warps at once, and its warp scheduler switches between them at no cost, unlike a CPU. When one warp waits for a read from high bandwidth memory, which can take a hundred cycles, another runs.
**In this book:** [GPUs, TPUs and Kernels › 1. The programming model](../10-llm-internals/05-gpus-tpus-and-kernels.md#1-the-programming-model).

### [11:09–14:21](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=669) Occupancy and registers

Each thread may use at most 255 registers, and an SM has a fixed number, so threads that use many registers leave room for few threads: lower occupancy. That is not necessarily bad, since fewer threads that each do more work can be better. Thread coarsening does exactly that, for instance eight elements per thread instead of one. The arithmetic on an example: a block of 128 threads at 160 registers each needs about 20,000 registers, so at most three such blocks fit on a B200 SM with its 65,000 registers. Three blocks are 12 warps, against a maximum of 64: an occupancy of 18%, because each thread is heavy on registers. Memory constrains compute.
**In this book:** [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [14:21–16:51](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=861) Bank conflicts

Shared memory is split into 32 banks, each four bytes wide, and in one clock cycle each bank serves at most one thread. Threads that hit the same bank wait in turn: a bank conflict. The worst case is 32 threads reading the first column of a matrix at once, a 32-way conflict. Reading rows would avoid it, but a matrix product reads along the rows of its first matrix and down the columns of its second, and transposes happen, so the order is not always free to choose. The remedy, which he does not develop, is swizzling, an arrangement of shared memory that avoids conflicts.
**In this book:** nothing beyond this guide; nearest: [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [16:51–19:05](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=1011) Coalescing, and the last wave

When the 32 threads of a warp read high bandwidth memory, the reads are combined into one transaction of 32 to 128 bytes, a cache line. With full coalescing all the threads read the same line; reading down a column fetches many lines of which little is used. It feels like a bank conflict but is a different constraint: that one is about shared memory, this one about high bandwidth memory. The last consideration is block occupancy. Blocks are scheduled on a finite number of SMs, 148 in his example: 160 blocks run as 148, then the remaining 12 while most SMs idle. So the number of blocks should divide the number of SMs. In sum: high bandwidth memory is global, shared memory belongs to a block, registers to a thread, and the hardware details decide performance; many are outside the programmer's control, so it is messier than the model.
**In this book:** [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks) · [GPUs, TPUs and Kernels › 2. The hardware facts that decide speed](../10-llm-internals/05-gpus-tpus-and-kernels.md#2-the-hardware-facts-that-decide-speed).

### [19:05–24:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=1145) A question on sharing an SM, then the recipe: measure, change, measure

Can two blocks share an SM? Only if a block leaves something to share; one that uses most of the SM's tensor cores gains nothing from company. The underlying problem is unevenness, since a block must stay together, and the remedy is to choose block sizes that leave no tail. Then the philosophy of the rest: benchmark and profile, change the code, and benchmark and profile again. Measure before writing any kernel. Benchmarking answers how long, an end-to-end number; it does not say where the time goes, but it is what one cares about, and as a single number it shows how time scales with the dimension. A tool exists, but the class builds one from scratch to show the pitfalls, on the operation of multiplying two random square matrices, starting from the naive start timer, run, stop timer.
**In this book:** [GPUs, TPUs and Kernels › What the practitioners say](../10-llm-internals/05-gpus-tpus-and-kernels.md#what-the-practitioners-say).

### [24:00–28:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=1440) Benchmarking pitfalls, and profiling

Always warm up first, because some code is compiled lazily and a kernel is run many times. Time more than once, since runs vary. The proper way is with CUDA events: record a start event, compute, record an end event, then synchronize, because the GPU runs asynchronously, and only then read the time; take the average, or the whole distribution if it matters. Scaling the matrices up shows the expected cubic growth, with a floor: up to nearly 2000 dimensions the time is almost constant, because these GPUs are built for large products and a 2 × 2 product wastes them. Profiling says where the time goes, and, less obviously, what happens under the hood. The assignment uses Nsight; in class the built-in PyTorch profiler suffices. Adding two tensors turns out to call one kernel with a long name.
**In this book:** [GPUs, TPUs and Kernels › What the practitioners say](../10-llm-internals/05-gpus-tpus-and-kernels.md#what-the-practitioners-say) · [GPUs, TPUs and Kernels › Try it](../10-llm-internals/05-gpus-tpus-and-kernels.md#try-it).

### [28:00–32:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=1680) Reading kernel names, and three GELU implementations

A matrix product calls a different kernel for every shape, and the names say how they are built: CUTLASS is NVIDIA's linear algebra library, SM100 marks the Blackwell architecture, then comes the precision, then the tile shape, 64 by 64 by 16 against 32 by 32 by 16 for another size. Two lessons: which kernels run is visible, and it depends on the dimensions. The case study is GELU, usually computed in its tanh approximation. Three implementations give the same answer: the equation written out in PyTorch, the built-in function, and the same expression after torch.compile, which turns any PyTorch function into another function. The naive one is several times slower, the built-in is fastest, the compiled one close behind.
**In this book:** [GPUs, TPUs and Kernels › What the practitioners say](../10-llm-internals/05-gpus-tpus-and-kernels.md#what-the-practitioners-say).

### [32:00–36:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=1920) What the profiler shows

The profile of the naive GELU lists many kernels, binary operations, a unary one, an addition, a hyperbolic tangent: each primitive of the computation graph is a kernel that reads from high bandwidth memory and writes back, and the next kernel reads it again. The built-in version is one kernel that someone wrote because people use GELU; nothing is magical. The compiled version is also one kernel, and a Triton kernel at that: the compiler read the graph and wrote the fused kernel itself. That is the whole difference: no fusion, many round trips, against one read and one write per element. To a question, no, the Triton kernel is not faster than the built-in here; the numbers change from year to year and with the hardware, and none of these is heavily tuned.
**In this book:** [GPUs, TPUs and Kernels › What the practitioners say](../10-llm-internals/05-gpus-tpus-and-kernels.md#what-the-practitioners-say) · [GPUs, TPUs and Kernels › 3. Six tricks](../10-llm-internals/05-gpus-tpus-and-kernels.md#3-six-tricks).

### [36:00–39:57](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=2160) CUDA against Triton

CUDA, developed by NVIDIA, was for years the way to write kernels. Its mental model is what each thread does, identified by an index: close to the hardware and fine-grained. The cost is bookkeeping: threads of a block that communicate must synchronize, read together, compute, write together. For elementwise work CUDA is fine; for complex operations the abstraction of Triton, developed at OpenAI and now standard, helps. In Triton one specifies what a thread block does: load data into shared memory, operate on it, write it back. It sits between thinking about single elements and thinking, as in PyTorch, about whole matrices. It is powerful enough for this course, though not for every feature of the latest hardware.
**In this book:** [GPUs, TPUs and Kernels › 5. Triton](../10-llm-internals/05-gpus-tpus-and-kernels.md#5-triton).

### [39:57–46:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=2397) A first Triton kernel: GELU

Take a vector of 8,000 elements. Triton is no longer functional: the output tensor is allocated explicitly for the kernel to write into, and inputs arrive as pointers. The vector is too big for one SM, so it is cut into blocks of 1,024 elements, eight of them, and the launch specifies a grid with that many blocks; the kernel receives the two pointers, how many elements there are and how large a block is. The kernel body has a fixed shape. Wake up and ask who I am: the program ID numbers the block. Find the data: the start is the ID times the block size, and the offsets are the start plus the range from zero to the block size. Mask the last block where the tensor ends. Load from the input pointer plus the offsets, compute, store at the output pointer plus the offsets. In questions: for elementwise work CUDA looks the same and is even simpler, since it works per element, where this is the vectorized form; whether tensor cores are used is not under the programmer's control.
**In this book:** [GPUs, TPUs and Kernels › 5. Triton](../10-llm-internals/05-gpus-tpus-and-kernels.md#5-triton).

### [46:00–50:39](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=2760) What a load really does

What happens when the load statement runs? In a sense it is a lie: the GPU does not execute this code. It specifies the computation, and the compiler turns it into PTX. Conceptually the pointer is a location in high bandwidth memory, the offsets pick a range of locations, and the load returns their contents, which end up in a register or in shared memory. On blocking: a load stalls for some cycles, but the SM runs several warps, so the scheduler runs another warp meanwhile and returns when the data has arrived. Every kernel in the lecture has this form: inputs and outputs, wake up, find the index, read, compute, write back.
**In this book:** [GPUs, TPUs and Kernels › 5. Triton](../10-llm-internals/05-gpus-tpus-and-kernels.md#5-triton).

### [50:39–58:05](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=3039) PTX: what one thread executes

PTX is the intermediate assembly language the Triton compiler emits. He shows it for the flavor. It is written per thread, the block having been compiled away. A load instruction moves data from global memory into registers, named with R for integers and F for floating point; moves and multiplications by constants follow; a store instruction writes back to global memory. The code shows thread coarsening: each thread handles eight elements, a decision the compiler took because the work per thread was light. The code is compiled once, and a thread tells itself apart through the block index and the thread index passed to it. Much is left unspecified, such as which SM runs what; that is hardware-controlled. Some people do write PTX by hand, which he does not recommend while compilers are as mature as NVIDIA's. He does not know why an SM has four warp schedulers. The plan for the rest: a softmax whose row fits in a block, one whose row does not, then a matrix product, the ingredients of FlashAttention.
**In this book:** [GPUs, TPUs and Kernels › 5. Triton](../10-llm-internals/05-gpus-tpus-and-kernels.md#5-triton).

### [58:05–62:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=3485) Softmax when a row fits in a block

Softmax exponentiates and normalizes each row of a matrix. The naive PyTorch version computes each row's maximum for numerical stability, subtracts it, exponentiates, sums and divides. Each step is a kernel that reads and writes high bandwidth memory: five reads of the whole matrix and three writes, where far fewer are needed. The Triton version makes each row a block, because rows do not interact and blocks share no memory. The block size is the number of columns, rounded to a power of two for luck; there is one block per row; the pointers and the strides are passed in. Masked positions are filled with negative infinity, which acts as zero, and the rest is the naive computation: maximum, subtract, exponentiate, sum, divide, store. When everything fits in a block, Triton is nearly plain PyTorch. To a question: a softmax down a column only needs the strides changed.
**In this book:** nothing beyond this guide; nearest: [GPUs, TPUs and Kernels › 5. Triton](../10-llm-internals/05-gpus-tpus-and-kernels.md#5-triton).

### [62:00–72:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=3720) A row longer than a block: tiles

A row of 4,000 columns does not fit a block of 1,024. The row is broken into four tiles, each thread iterates over the tiles and keeps an accumulator, and the accumulators are summed at the end. He switches to a row sum, which is easier to follow: with tiles of four columns, four threads add the elements at their position in each tile, 3 plus 5 plus 5 in one, and the four accumulators are then summed into the row's total. In the code the loop moves the start by one block size at a time, loads each tile and adds it to the accumulator, which lives in a register or in shared memory as the compiler decides. The for loop inside the block is what a row longer than a block requires. The difference from the GELU kernel matters: there each piece was an independent block, here the block is the whole row and the pieces are tiles, so the code stops looking like PyTorch.
**In this book:** [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one).

### [72:00–76:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=4320) Matrix multiplication: naive and idealized

The finale is the matrix product, optimized to death and fundamental, followed here by a ReLU, as in a linear layer. The naive kernel computes one output element at a time: for each of the K positions read from both inputs, multiply, accumulate, write. It is correct and reads from high bandwidth memory once per multiply-add, so its arithmetic intensity is a constant. The reads are redundant: neighbouring output elements need the same row. The idealized kernel loads both whole matrices into shared memory and then computes, which brings the reads down to quadratic and the arithmetic intensity to order n. Its problem is that real matrices do not fit in shared memory.
**In this book:** [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one) · [Resource Accounting › 5. Find the bottleneck: arithmetic intensity](../10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md#5-find-the-bottleneck-arithmetic-intensity).

### [76:00–80:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=4560) Tiling: naive globally, idealized locally

Tiling is the classic answer: fit as much into shared memory as fits. Globally it looks like the naive kernel, locally like the idealized one. Each tile of the output is a thread block. The block sweeps along the row tiles of the first matrix and the column tiles of the second, loads each pair into shared memory, multiplies them and adds the result to a partial sum, and writes its output tile once at the end. The arithmetic intensity rises to the order of the tile size, short of order n but good for large tiles. A bonus: since the kernel writes the output anyway, an elementwise activation costs nothing extra before the write. That is kernel fusion. The code needs strides: a tensor is stored linearly, and the strides map a row and a column to one index, four positions per row and one per column in his example, flipped for a transpose.
**In this book:** [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one).

### [80:00–1:28:00](https://www.youtube.com/watch?v=xnDHaNUvHBg&t=4800) The tiled kernel, and the lesson

The tiled kernel wakes up on one output tile, works out which rows of the first matrix and which columns of the second it needs, sets up an accumulator and loops: load the two small tiles, take their product, which in shared memory reads like a matrix product in PyTorch, advance. An optional nonlinearity is applied before the single write. The summary: the programmer controls PyTorch, Triton or PTX, and even PTX does not control everything, because SMs, banks, memory and registers are finite, and a model must fit their constraints; hence benchmarking and profiling. Thinking in thread blocks is easier than in threads, since synchronization and shared memory need no thought: read, do something, write back. The examples climbed from elementwise to a reduction over a row, a reduction across tiles, and the tiled matrix product. The next lecture covers several GPUs. Asked about alternatives to Triton, he says that every language has an inductive bias, and that Triton was built by people who train transformers, so transformer kernels come easily; PTX is the extreme, and other libraries and domain-specific languages, Thunder Kittens among them, give different trade-offs.
**In this book:** [GPUs, TPUs and Kernels › 4. Tiling, the big one](../10-llm-internals/05-gpus-tpus-and-kernels.md#4-tiling-the-big-one) · [GPUs, TPUs and Kernels › Key takeaways](../10-llm-internals/05-gpus-tpus-and-kernels.md#key-takeaways).

## What to take away

- The programming model, threads in blocks in a grid, is enough for correctness; warps, register limits, bank conflicts, coalescing and the last wave of blocks decide the speed.
- Benchmark with warm-up, CUDA events and synchronization, and profile before writing a kernel; the kernel names show which library and tile shape PyTorch chose.
- torch.compile fuses an expression into one Triton kernel, which is why it beats the naive version; a hand-written kernel can still be faster.
- A Triton kernel has one shape: find the block, compute the offsets, mask the tail, load, compute, store; data larger than a block needs a loop over tiles.
- A matrix product goes from constant arithmetic intensity to the order of the tile size by loading tiles into shared memory, and an activation can ride along before the write.

## Sources

- Percy Liang and the course staff, "Kernels, Triton", Stanford CS336 Language Modeling from Scratch, Spring 2026: [video](https://www.youtube.com/watch?v=xnDHaNUvHBg).
- Course page: <https://cs336.stanford.edu/>.
