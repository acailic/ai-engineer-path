# Lecture guide: Distributed Training (Part I)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 19 · **Length:** 1:10:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=LcOM-nZdqxw) · **Slides:** [slides](https://www.dropbox.com/scl/fi/85ud2gzrtyllgeqgpv9gs/Lec19-Distributed-Training-I.pdf?rlkey=80t52w3peqqf8oanpc6ojmvnf&st=jn4yxsjy&dl=0)
**Chapters that cite this lecture:** [10. Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md)

> **In one sentence:** Song Han opens distributed training: why many GPUs are needed, the four ways to split work (data, pipeline, tensor and sequence parallelism), how gradients are aggregated without a central server (ring and recursive-halving all-reduce), how ZeRO and FSDP shard training state to fit large models, and how sequence parallelism handles long contexts.

## Before you watch

The chapter [Parallelism](../10-llm-internals/06-parallelism.md) teaches the same methods from Stanford's course, and [Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) summarizes this lecture. The lecture reviews the earlier inference techniques only by name and uses the transformer's attention and MLP blocks without introducing them, so the transformer lecture is the one to read first.

## The lecture, part by part

### [0:00–1:24](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=0) Plan

The course turns from inference to training. The first half accelerated inference with general techniques, pruning, quantization, architecture search and distillation, and domain-specific ones; the next lectures make training faster: data parallelism with its sharded variants ZeRO and FSDP, pipeline parallelism, tensor parallelism, and sequence parallelism.
**In this book:** not needed (lecture introduction and plan of the lecture).

### [1:24–5:10](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=84) Why distribute

Higher accuracy costs more computation. GPT-3 took about 3 million GPU hours to train, 355 years on a single GPU, so that a researcher would spend a month per epoch. A job of 10 GPU-days shrinks to minutes on 1,024 GPUs. Han's lab did this in 2019 on the Summit supercomputer, with V100 GPUs and 200 gigabit InfiniBand, now 400: a video model using the Temporal Shift Module, trained on 660 hours of video, needed 49 hours on one node and 14 minutes on 1,536 GPUs, 211 times faster against a theoretical 256, with the accuracy well maintained.
**In this book:** [Parallelism › Why this matters](../10-llm-internals/06-parallelism.md#why-this-matters) · [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [5:10–10:34](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=310) Four ways to split

Data parallelism splits the data and keeps a full copy of the model on every GPU. Pipeline parallelism splits the model by layers, each GPU holding some layers, and shares the data. Tensor parallelism splits within a layer, each GPU holding part of each weight matrix, for example two 4k by 2k halves of a 4k by 4k matrix, and shares the data. Sequence parallelism splits a long sequence, one chapter per GPU, with the whole model on each GPU. This part is new this year, he says, because sequences keep growing: an hour of 1080p video easily exceeds a hundred million tokens.
**In this book:** [Parallelism › 1. The vocabulary](../10-llm-internals/06-parallelism.md#1-the-vocabulary).

### [10:34–15:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=634) Data parallelism with a parameter server

A centralized design, no longer common. A parameter server holds the model; each worker pulls a copy, takes an equal random share of the data, computes a local gradient on it, which differs from the others because the data differ, and pushes it; the server applies the sum and the workers pull again. Compared with single-GPU training, each iteration gains two synchronization steps, pulling the weights and pushing the gradients, and synchronization is not free.
**In this book:** [Parallelism › 2. Data parallelism](../10-llm-internals/06-parallelism.md#2-data-parallelism).

### [15:00–20:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=900) Communication primitives

Send and receive move data from one node to one node. Scatter sends different pieces of a tensor to many nodes; broadcast sends the same copy to all. Gather collects data from many nodes into one; reduce gathers and then applies an operation such as a sum or a maximum. All-reduce and all-gather do the same for every receiver at once, many to many. The parameter server replicates the model by broadcast.
**In this book:** [Parallelism › 1. The vocabulary](../10-llm-internals/06-parallelism.md#1-the-vocabulary).

### [20:00–26:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=1200) The server's bottleneck, and the ring

The server collects the gradients by reduce, since it sums them. Each worker pays O(1) bandwidth to pull or push, but the server serves n workers, so its bandwidth grows with n and limits scale. All-reduce removes the server. A sequential version gathers and sums on each node in turn: time O(n) and bandwidth O(n) on every node. The ring version has every node pass its data to its neighbour; after n − 1 steps every node holds the full sum. Time is still O(n), but each node talks only to two neighbours, bandwidth O(1).
**In this book:** [Parallelism › 2. Data parallelism](../10-llm-internals/06-parallelism.md#2-data-parallelism).

### [26:00–31:25](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=1560) Parallel and recursive-halving all-reduce

Running all reductions at once gives O(1) time and O(n²) total bandwidth, too much. Recursive halving, also called the butterfly all-reduce, combines the virtues. With eight nodes, each first exchanges with its neighbour at offset 1, then at offset 2, then at offset 4; after log n cycles, three here, every node has every contribution. Han's lab uses this rather than a central server.
**In this book:** nothing beyond this guide; nearest: [Parallelism › 2. Data parallelism](../10-llm-internals/06-parallelism.md#2-data-parallelism).

### [31:25–36:50](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=1885) Where training memory goes, and ZeRO-1 and ZeRO-2

After a break: GPT-3's weights alone take 350 gigabytes in FP16, against 80 on one GPU. Training one parameter in mixed precision takes 16 bytes: 2 for the weight, 2 for the gradient, and 12 for optimizer state, an FP32 master copy plus first and second moments of 4 bytes each. An 80-gigabyte GPU then trains only a 5-billion-parameter model, activations aside. Data parallelism keeps n copies of all this. ZeRO, the zero-redundancy optimizer, shards them: stage 1 shards the optimizer state, so with 64 GPUs each parameter costs 4.2 bytes per GPU and 19 billion fit; stage 2 shards the gradients too, 2.2 bytes and 36 billion.
**In this book:** [Parallelism › 3. Shard the state: ZeRO and FSDP](../10-llm-internals/06-parallelism.md#3-shard-the-state-zero-and-fsdp) · [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [36:50–38:48](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2210) ZeRO-3 and FSDP

Stage 3 shards the weights as well, one n-th on each GPU; a parameter then takes 0.25 bytes per GPU and 320 billion parameters fit in 80 gigabytes. This is how large language models are usually trained; PyTorch implements it as FSDP, fully sharded data parallel, and Han calls it safe for models below about 70 billion parameters.
**In this book:** [Parallelism › 3. Shard the state: ZeRO and FSDP](../10-llm-internals/06-parallelism.md#3-shard-the-state-zero-and-fsdp) · [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [38:48–42:52](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2328) Pipeline parallelism

Layers go to different GPUs. Language models suit this because their blocks are identical, so every stage takes the same time, and GPT-3's 350 gigabytes of weights spread over 8 GPUs leave under 44 gigabytes each. Processing one batch naively leaves most GPUs idle most of the time, a utilization of 25%, full of bubbles. Splitting the batch into micro-batches lets the first GPU start the next while the second works on the first, and utilization rises to 57%, 2.5 times. The lesson: split training finely.
**In this book:** [Parallelism › 4. Pipeline parallelism](../10-llm-internals/06-parallelism.md#4-pipeline-parallelism).

### [42:52–48:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2572) Tensor parallelism: the MLP block

Tensor parallelism splits within a layer, as in Megatron-LM. Since communication is expensive, the aim is to communicate only at the start and the end. In the MLP, the first weight matrix is split by columns, the second by rows. The input is broadcast to two GPUs, each computes half of the first product with no communication, each multiplies its half by its rows of the second matrix, and the two partial results are summed by one all-reduce.
**In this book:** [Parallelism › 5. Tensor parallelism](../10-llm-internals/06-parallelism.md#5-tensor-parallelism).

### [48:00–53:08](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2880) Tensor parallelism: the attention block

The query, key and value projections are split by columns, which is to say by attention heads: each GPU holds whole heads and computes their attention independently, with no communication. The output projection is split by rows, each GPU multiplies its own attention output by its rows, and one all-reduce sums the two partial results. Again communication happens only in a broadcast at the start and an all-reduce at the end, which is why transformers scale so easily across GPUs; Han calls it a fine case of algorithm and system co-design.
**In this book:** [Parallelism › 5. Tensor parallelism](../10-llm-internals/06-parallelism.md#5-tensor-parallelism).

### [53:08–56:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=3188) Why sequence parallelism

Long contexts matter for documents, financial reports and legal texts, for video, and for robot trajectories, and they take a lot of GPU memory to train. In sequence parallelism each GPU holds the whole model but one part of the sequence, say one chapter of 10k tokens. Each GPU then holds only the queries, keys and values of its own part, while attention must relate every part to every other; computed without communication, chapter 1 would never see chapter 2.
**In this book:** [Parallelism › 6. The rest](../10-llm-internals/06-parallelism.md#6-the-rest).

### [56:00–1:03:30](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=3360) DeepSpeed Ulysses

The first solution, DeepSpeed Ulysses, re-partitions inside attention. After the query, key and value projections, an all-to-all communication switches from splitting by sequence to splitting by heads: everything of head 1 moves to GPU 1, of head 2 to GPU 2, and so on. Each GPU then computes full attention for its heads over the whole sequence, and a second all-to-all restores the split. Why not split by heads from the start? Because the query, key and value projections must be computed first. The limits are heavy communication and a maximum parallelism equal to the number of heads.
**In this book:** [Parallelism › 6. The rest](../10-llm-internals/06-parallelism.md#6-the-rest).

### [1:03:30–1:06:30](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=3810) Ring attention

The second solution recalls the ring all-reduce. Each GPU keeps its own block as queries and passes the key and value blocks around the ring: in the first cycle its queries attend to the next block, in the next cycle to the one after, until the grid of query blocks against key blocks is filled. Ring attention works for training and inference and is not limited by the number of heads.
**In this book:** [Parallelism › 6. The rest](../10-llm-internals/06-parallelism.md#6-the-rest).

### [1:06:30–1:07:27](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=3990) Two dimensions at once

The two methods can be combined into a 2D parallelism that exploits the hardware: the eight GPUs within a node have a higher communication bandwidth than nodes have between them, so Ulysses runs inside the node and ring attention runs between nodes. It follows the rule of thumb he stated earlier in the lecture, minimize communication and maximize utilization. The paper is open source.
**In this book:** nothing beyond this guide; nearest: [Parallelism › 7. Putting it together](../10-llm-internals/06-parallelism.md#7-putting-it-together).

### [1:07:27–1:10:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=4047) Summary, and the final project

Han recaps: data and sequence parallelism split the data, pipeline and tensor parallelism split the model, all-reduce has a ring form and a logarithmic one, ZeRO and FSDP are probably the most popular distributed training technique in PyTorch. The final project uses the NeurIPS template: abstract, motivation, prior methods, your method and results compared with the state of the art; the proposal is the same without results.
**In this book:** [Parallelism › Key takeaways](../10-llm-internals/06-parallelism.md#key-takeaways).

## What to take away

- Training large models takes many GPUs; the four ways to split are by data, by layers, within layers, and along the sequence.
- All-reduce replaces a central parameter server; ring all-reduce keeps bandwidth constant per node and recursive halving finishes in log n steps.
- Each parameter costs 16 bytes to train; ZeRO shards the optimizer state, then gradients, then weights, and FSDP implements the last stage.
- Tensor parallelism suits transformers because communication is needed only before and after each block; long sequences need Ulysses, ring attention or both.

## Sources

- Song Han, "Distributed Training (Part I)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=LcOM-nZdqxw).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
