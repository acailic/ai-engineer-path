# Lecture guide: Distributed Training (Part II)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 20 · **Length:** 1:00:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=lOVcPooetrM) · **Slides:** [slides](https://www.dropbox.com/scl/fi/c0w7j7dxduuf8ply7lzeb/Lec20-Distributed-Training-II.pdf?rlkey=ynh3yx4jf99nojklt0ki7zh0y&st=vxzkzdt4&dl=0)
**Chapters that cite this lecture:** [10. Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md)

> **In one sentence:** Song Han continues distributed training: combining parallelisms in 2D and 3D and choosing them automatically with Alpa, then attacking the two costs of communication, bandwidth with gradient compression (deep gradient compression, PowerSGD, 1-bit and ternary gradients) and latency with delayed gradient averaging.

## Before you watch

The chapter [Parallelism](../10-llm-internals/06-parallelism.md) covers the combinations of parallelism from Stanford's course, and [Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) summarizes this lecture. The previous lecture's four parallelisms and its communication primitives are assumed.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=0) Recap: four parallelisms, four trade-offs

The plan: hybrid and mixed parallelism, automatic parallelization, then two bottlenecks of distributed training, communication bandwidth, answered by gradient compression, and communication latency, answered by delayed updates. Data parallelism gives high utilization and low communication but high memory, which ZeRO and FSDP relieve by sharding. Pipeline parallelism gives low utilization, since a fast stage waits for a slow one, low memory and medium communication. Tensor parallelism gives high utilization and low memory but high communication, one exchange at each end of every attention and feed-forward block. Sequence parallelism splits tokens and needs communication inside attention, by Ulysses or by ring attention.
**In this book:** [Parallelism › 1. The vocabulary](../10-llm-internals/06-parallelism.md#1-the-vocabulary).

### [4:00–8:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=240) 2D parallelism

Methods combine. Four GPUs can run data parallelism on the outside and pipeline parallelism on the inside, or pipeline parallelism on the outside and tensor parallelism on the inside, each half of a weight matrix on one GPU. Sequence parallelism can also go two-dimensional. Ring attention alone is bound by the slowest link: about 50 gigabytes per second between nodes, against up to 900 within a node over NVLink. So run Ulysses, an all-to-all, inside each node and ring attention between nodes.
**In this book:** [Parallelism › 7. Putting it together](../10-llm-internals/06-parallelism.md#7-putting-it-together) · [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [8:00–12:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=480) 3D parallelism, and Alpa

In 3D parallelism, tensor parallelism, the most communication-heavy, stays inside a server; pipeline parallelism splits layers; and sharded data parallelism runs across servers. The design space is huge: each layer could be split by pipeline or by tensor, in several groupings. Alpa, a unified compiler for distributed training, searches it hierarchically. It first partitions layers into stages, the inter-operator choice, by dynamic programming, then decides each operator's intra-operator parallelism: replicate one matrix and split the other, or split both and sum the partial results by all-reduce. The cost model adds computation, communication and resharding between operators, and the result reaches higher throughput than the best manual systems, up to 64 GPUs.
**In this book:** [Parallelism › 7. Putting it together](../10-llm-internals/06-parallelism.md#7-putting-it-together) · [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [12:00–16:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=720) The communication problem

Computation is cheap and data movement expensive, and three trends make communication worse: synchronous training, the common practice, exchanges gradients after every iteration; larger models send larger gradients, as large as their weights; and more nodes mean more traffic. Scalability therefore differs by model: AlexNet, with 240 megabytes of weights and little computation, scales poorly on 200 nodes, Inception much better. Latency sets a floor: microseconds within a rack, about a millisecond within a data centre, some 100 milliseconds over wireless and across the world, up to seconds.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [16:00–20:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=960) Two ways to send less

In the parameter-server workflow the costly steps are pulling parameters and pushing gradients, the latter as large as the weights, from every node. Two remedies shrink the message. Gradient pruning sends only the largest gradients by magnitude and skips the zeros. Gradient quantization sends 32-bit gradients in 8 bits, eight times smaller.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [20:00–24:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=1200) Why early gradient pruning lost accuracy

Prune only the top k gradients and keep the rest in a local buffer until they grow past the threshold and are sent. This raised throughput years ago on small datasets but lost 1% accuracy on ResNet. The reason is momentum, used by nearly every optimizer: the velocity is the discounted previous velocity plus the current gradient, and the weights move by the velocity, not by the gradient. Feeding accumulated gradients into that rule gives a different update from ordinary momentum SGD, and the optimization drifts.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [24:00–28:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=1440) Momentum correction and warm-up

The remedy, momentum correction, accumulates the velocity rather than the gradient, so that the delayed update lands where ordinary momentum would have. Warm-up helps too, because early training changes the weights fast and stale gradients hurt most then: start with a small learning rate and raise it, and raise the sparsity gradually over the first few epochs so the optimizer can adapt.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [28:00–32:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=1680) Deep gradient compression: results

A vision baseline reaches 92.9%; pruning without accumulation does not converge; accumulation recovers most of the loss; adding momentum correction brings it to about 92.5%; warm-up alone helps; and all three together pass 93%. In language modelling accumulation alone costs about three points of word error rate, which momentum correction and gradient clipping, important for LSTMs, recover. Gradients can be pruned to 99.9% sparsity with the accuracy intact, shrinking them several hundred times, less than a thousand because sparse storage needs indices and biases are kept.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [32:00–36:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=1920) Denser every round, and PowerSGD

Elsewhere the same method shrinks a language model's gradient from 190 megabytes to half a megabyte and a speech model's from 480 to under 1. One problem remains with all-reduce: nodes hold different sparsity patterns, so summing them makes the result denser each iteration. Enforcing a common coarse pattern, or pruning again inside the ring, fixes it. PowerSGD avoids sparsity altogether: factor a gradient matrix into two low-rank factors, a 4 by 4 into 1 by 4 and 4 by 1, whose fixed shape changes nothing under all-reduce; it scales almost linearly with the number of workers.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [36:00–38:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=2160) What was learned about pruning gradients

The 2017 method combines local accumulation, momentum correction, gradient clipping and warm-up. Gradients tolerate far more pruning than weights, 99.9% against 90%, at no loss of accuracy; Han adds that 90% is already a high ratio for weights, whereas gradients, which are computed anew at every iteration, are far more redundant. Their sparsity does not survive all-reduce, which low-rank factors do.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [38:00–42:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=2280) Gradient quantization

After a break: fewer bits per gradient. 1-bit SGD sends one bit per value, its sign, with a 32-bit scale per column chosen to preserve the sum of absolute values; the quantization error is kept as a residual and added to the next gradient. Threshold quantization maps values to plus or minus a chosen threshold or to zero, with the same error accumulation, and needs the threshold picked by hand. TernGrad sends minus, zero or plus the tensor's maximum with probabilities proportional to each gradient's magnitude, so the expected quantized gradient equals the true one and no error accumulation is needed.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [42:00–46:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=2520) Latency, the harder bottleneck

Bandwidth yields to compression and to better hardware, from Ethernet at up to a gigabit per second through fibre to InfiniBand at 400 gigabits. Latency yields to nothing: light itself takes 162 milliseconds from Boston to Shanghai, and congestion adds more. In synchronous training every worker waits for communication before the next iteration. Han likens the fix to late days for homework: submit homework 2 and keep studying lecture 3 meanwhile.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [46:00–50:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=2760) Delayed gradient averaging

With delayed gradient averaging a worker starts the next iteration as soon as its own computation ends and applies the averaged gradient from d iterations ago, stale by a few steps; the study finds up to three steps safe. No gradient is dropped, only used late, and the course's fixed number of late days corresponds to a delay beyond which convergence fails. Moving the synchronization barrier forward hides communication entirely as long as it finishes before the barrier. The algorithm stores each iteration's local gradient, so that the update can use the fresh local gradient plus the delayed average minus the worker's own contribution from d steps ago.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [50:00–54:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=3000) Correcting for staleness

Without the correction, accuracy falls from 88% to 84% as the delay grows. With it, the stale average's share of the worker's own old gradient is subtracted and the fresh gradient added, and accuracy holds 4 to 5% higher. The delay stays small, ten or twenty iterations, over which the learning rate barely changes; asked whether a smaller learning rate is needed, Han answers that it must scale with the batch size, which grows with the number of nodes.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [54:00–58:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=3240) Speed-up, including on Raspberry Pis

The baseline, FedAvg with five local steps, merely trains with a five times larger batch. Accumulating ten iterations before sending gives a 1.5 times speed-up and twenty a 2 times one; adding delayed averaging gives 3 to 4 times, with accuracy intact on vision and language datasets, IID or not. On eight Raspberry Pis joined by plain Ethernet, the baseline reaches 3 to 4 times on eight nodes and delayed averaging 7 to 7.5 times.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [58:00–1:00:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=3480) Summary

Han recaps: hybrid and automatic parallelism; bandwidth answered by pruning and quantizing gradients; latency answered by delaying the update like a late day for homework. He then urges students to open-source their final projects, as the lab has done since 2018, which in his view keeps quality high and helps the community; the lab's GitHub organization shows the expected format, and project proposals are due soon.
**In this book:** nothing beyond this guide; nearest: [Parallelism › Key takeaways](../10-llm-internals/06-parallelism.md#key-takeaways).

## What to take away

- Combine parallelisms to match the hardware: tensor parallelism inside a server, data parallelism across servers, Ulysses inside a node and ring attention between nodes; Alpa can choose the plan.
- Synchronous training pays for bandwidth and latency at every iteration.
- Gradients tolerate extreme sparsity if the velocity, not the gradient, is accumulated and training is warmed up; low-rank factors survive all-reduce; a few bits per value suffice.
- Stale gradients a few iterations old still converge, provided the worker's own old contribution is removed.

## Sources

- Song Han, "Distributed Training (Part II)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=lOVcPooetrM).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
