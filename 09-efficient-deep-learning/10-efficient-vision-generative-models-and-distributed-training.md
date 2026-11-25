# 10. Efficient Vision, Generative Models and Distributed Training

**Level:** Practitioner · **Reading time:** 15 min · **Exercise:** 30 min
**Prerequisites:** [Neural Network Basics for Efficiency](02-neural-network-basics-for-efficiency.md), [Efficient LLM Inference and Deployment](08-efficient-llm-inference-and-deployment.md) for the cost of attention

> **In one sentence:** After this chapter you can name the standard efficiency move for vision transformers, for generative models and for training across many machines, and estimate what each one saves.

## Why this matters

The techniques so far were introduced on classifiers and language models. They reappear in three more places, each with its own dominant cost:

- a segmentation model on a drone, where attention over millions of pixels is the problem;
- an image generator, where the problem is running a large network dozens of times per image;
- a training job that does not fit on one GPU.

This is a survey: one dominant cost and one standard move for each.

## Efficient vision transformers

A **vision transformer** (ViT) cuts an image into patches, treats each patch as a token, and runs a standard transformer encoder over them (Han's Lecture 16, slides 4 to 11). Han's slides note that it is weaker than a convolutional network on small datasets and stronger with large-scale pre-training.

The cost problem is attention. With `N` patches, the attention table has `N²` entries per head.

- 224 × 224 image, 16 × 16 patches: 196 tokens, 38,416 entries.
- 1,024 × 1,024 image, same patches: 4,096 tokens, 16.8 million entries.

An image 4.6 times larger on each side costs 21 times more tokens and 436 times more attention. Han makes the same point when he raises resolution in the lecture: tokens grow with the square of the resolution and attention with the square of the token count, so a vision transformer's computation grows with the fourth power, much faster than a convolutional network's ([8:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=480)). His example of the gain is segmentation on a Jetson Orin at FP16 and batch size one: from 1.6 to 21 frames per second at the same accuracy.

| Move | Idea | What you pay |
|---|---|---|
| Window attention | each patch attends only inside a local window; cost grows linearly with image size. Han's example uses 7 × 7 windows, so each holds a fixed number of tokens ([10:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=600)) | long-range relations need several layers |
| Shifted or balanced windows | let neighboring windows exchange information; equal-size groups are hardware-friendly, and on a Jetson Orin they run faster than other transformer models and even than convolutional ones (Han, [16:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=960)) | bookkeeping |
| Linear attention | change the order of multiplication, as in `(A × B) × C = A × (B × C)`, so the cost is linear in `N` (Han, [18:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1080)) | on its own, a large accuracy drop: it cannot produce the sharp, local attention of softmax. Han's fix adds a small convolution branch, which costs little, restores the accuracy and gives about 5.8 times the speed with higher accuracy on segmentation on a mobile chip ([20:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1200)) |
| Sparse windows | prune unimportant windows; his SparseViT keeps the first layer dense and later layers sparser, because a pruned token cannot recover, and finds the per-layer sparsity by evolutionary search ([28:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1680)) | a search for which windows |

His EfficientViT results cover segmentation on Cityscapes, super-resolution and Segment Anything, which is where [Chapter 01](01-why-efficiency-matters.md) got its 182 images per second example. He reports latency on an Orin, an edge chip serving one user, and throughput on an A100, a cloud chip serving many ([24:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1440)).

One more finding is relevant to efficiency. In his lecture on post-training, Han reports for the VILA vision-language model that the original image resolution matters more than the number of tokens (Lecture 14, [54:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3240)). More tokens are not automatically better, and they are never cheap.

## Efficient generative models

A **generative model** produces images, video or 3D content instead of a label.

| Family | Why it is expensive | Standard moves |
|---|---|---|
| GAN | two networks; the generator runs per pixel | prune the generator; one generator at several sizes |
| Diffusion | a large network runs once per denoising step, dozens of steps per image | fewer steps, fewer tokens, cheaper attention, skip unchanged regions |
| Autoregressive image models | one network pass per visual token | predict many tokens per step |

A **GAN** has a generator and a discriminator, which learns to tell real images from generated ones (Han, Lecture 17, [2:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=120)). Only the generator runs at inference, so that is the part to compress (same block). His GAN Compression result cut a CycleGAN model from 56.8 to 3.5 billion MACs and raised its speed from 12.1 to 40 frames per second (Lecture 17, [8:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=480), on a Jetson Xavier GPU, the device named on his Lecture 1 slide). Anycost GANs train one generator that runs at several resolutions and channel widths, the once-for-all idea from [Chapter 05](05-neural-architecture-search.md). Han's finding: one discriminator cannot give useful feedback to every sub-generator, so it is conditioned on the generator's configuration ([16:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=960)).

A **diffusion model** learns to remove noise step by step. Starting from pure noise, it produces an image after many steps. Total cost = steps × cost per step. Han's Lecture 18 covers four ways to reduce it:

1. **Fewer steps.** Deterministic samplers (DDIM) and progressive distillation.
2. **Fewer tokens per step.** Latent diffusion runs in a compressed space. Han's deep compression autoencoder shrinks an image 64 times instead of the usual 8, so a model diffuses 64 tokens where it used to diffuse about 4,000 ([40:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=2400)).
3. **Cheaper attention.** His Sana model uses linear attention in the diffusion transformer.
4. **Skip work.** When editing part of an image, SIGE recomputes only the edited region: Han's demo changes 3% of the pixels and runs more than 4 times faster at the same quality ([60:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=3600)). Quantization needs another recipe. Weight-only quantization speeds up a language model, which is bound by memory bandwidth, but a diffusion model is bound by compute, so Han says weights and activations must both go to 4 bits for a measured speed-up (same block).

Worked numbers: 50 steps on 16,384 tokens is 819,200 token-steps per image. 20 steps on 256 tokens is 5,120. That is 160 times less work, before any change to the network itself.

Han's remark on conditioning techniques applies to the whole family: each technique added for quality adds computation ([30:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=1800)).

For video, his Temporal Shift Module moves part of the channels from one frame to the next. It adds temporal modeling to a 2D network with no multiplies at all (Lecture 17, [42:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=2520)).

## Distributed training basics

Two reasons to train on several machines: the data is too large for one, or the model does not fit. Han's motivating figure: on a single GPU, the training of GPT-3 would take 355 years (Lecture 19, [2:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=120)). His practical reason is the developer's time: a job of 10 GPU-days on one GPU takes about 40 minutes on 1,024 GPUs.

| Parallelism | What is split | Memory per GPU | Communication |
|---|---|---|---|
| Data | the data; every GPU holds a full model | unchanged | gradients each step |
| Pipeline | the layers, in stages | reduced | activations between stages |
| Tensor | each weight matrix | reduced | heavy; keep inside one machine |
| Sequence | the tokens | reduced | activations and attention across machines |

**Data parallelism** in Han's five steps (Lecture 19, slides 34 to 41): replicate the model to each GPU, split the data, compute gradients, aggregate them, update. The aggregation uses **all-reduce**, an operation in which every GPU ends up with the sum; his slides compare a naive version with a ring ([26:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=1560)).

Data parallelism saves time and no memory. For memory, ZeRO and its implementation FSDP shard, stage by stage, the optimizer state, the gradients and the weights across GPUs ([38:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2280)). On Han's slide, with 64 GPUs, the first stage leaves 4.2 bytes per parameter and fits 19 billion parameters on one 80 GB GPU; the last, which also shards the weights, fits about 320 billion ([36:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2160)). Worked numbers for the 7-billion-parameter model from [Chapter 09](09-llm-post-training-and-on-device-training.md): 112 GB before activations on one GPU, about 14 GB per GPU on eight.

Large runs combine the methods into 3D parallelism: tensor parallelism stays inside one server because it is the most communication-heavy, pipeline parallelism splits the layers, and sharded data parallelism runs across servers (Lecture 20, [8:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=480)). Alpa searches the partitioning automatically, first between operators, then within them ([12:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=720)).

Communication is the remaining bottleneck: computation is cheap, data movement is expensive, and synchronous training exchanges gradients after every iteration (Lecture 20, [12:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=720)). To send fewer bytes, prune small gradients and keep them locally until they grow past a threshold. An early version lost 1% accuracy on ResNet; Han traces that to momentum, the optimizer's running average of past gradients, so his deep gradient compression accumulates momentum rather than raw gradients ([20:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=1200)). Latency is harder: his slides are titled "High Network Latency Slows Distributed Training" and show delayed gradient averaging as the remedy (Lecture 20, slides 19 to 22).

The details are in [parallelism](../10-llm-internals/06-parallelism.md).

## Pitfalls

1. **Counting only the linear layers in a high-resolution transformer.** Fix: include the `N²` attention term.
2. **Comparing diffusion models by cost per step.** Fix: multiply by the number of steps and the token count.
3. **Using data parallelism to fit a large model.** Fix: shard with FSDP or split the model.
4. **Tensor parallelism across a slow link.** Fix: keep it inside one machine; use pipeline parallelism between machines.
5. **Dropping small gradients without momentum correction.** Fix: accumulate velocity, not raw gradients, as Han's deep gradient compression slides show.

## Try it

Build a cost sheet with one line per family.

1. A vision transformer at two resolutions: token count and attention entries.
2. A diffusion model: steps × tokens per step, for the original and for a compressed latent space.
3. A 7-billion-parameter training run: memory per GPU with 8-way FSDP.

**You are done when** every number has its formula next to it.

**Stretch:** verify the two vision transformer numbers in three lines of Python.

## Key takeaways

- Vision transformers: attention cost grows with the square of the token count. Windows, linear attention and sparsity make it linear.
- Diffusion: cost is steps times tokens. Cut both.
- Data parallelism saves time, not memory. ZeRO and FSDP shard memory.
- Communication bytes can be compressed. Latency is the hard limit.
- Fewer MACs is never the whole story; measure latency on the target.

## Self-check

1. Doubling an image's side length multiplies the number of tokens by 4. What happens to the attention cost?
2. A diffusion model needs 50 steps on 16,384 tokens. Give two independent ways to cut its cost.
3. Which parallelism leaves memory per GPU unchanged?
4. What do ZeRO and FSDP shard across GPUs?
5. Why is tensor parallelism usually kept inside one machine?

<details><summary>Show answers</summary>

1. It grows by 16 times, since attention is proportional to tokens squared.
2. Fewer sampling steps, and fewer tokens per step by working in a more compressed latent space.
3. Data parallelism, because every GPU holds a full copy of the model.
4. The optimizer state, the gradients and the weights.
5. Because it needs heavy communication for every layer, and links between machines are slower.

</details>

## Sources

- **Lecture:** Song Han, "Lecture 16: Vision Transformer", MIT 6.5940 TinyML and Efficient Deep Learning Computing (Fall 2024): [video](https://www.youtube.com/watch?v=v0jYDgaVzlk), used at [resolution cost](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=480), [balanced windows](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=960), [linear attention](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1080), [sparse windows](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1680)
- **Lecture:** Song Han, "Lecture 17: Efficient GAN, Video, and Point Cloud", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=o_60Yhb79W8), used at [GANs](https://www.youtube.com/watch?v=o_60Yhb79W8&t=120), [temporal shift](https://www.youtube.com/watch?v=o_60Yhb79W8&t=2520)
- **Lecture:** Song Han, "Lecture 18: Diffusion Model", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=LXrqmQrscf0), used at [cost of conditioning](https://www.youtube.com/watch?v=LXrqmQrscf0&t=1800), [compression autoencoder](https://www.youtube.com/watch?v=LXrqmQrscf0&t=2400)
- **Lecture:** Song Han, "Lecture 19: Distributed Training (Part I)", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=LcOM-nZdqxw), used at [motivation](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=120), [all-reduce](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=1560), [ZeRO and FSDP](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2280)
- **Lecture:** Song Han, "Lecture 20: Distributed Training (Part II)", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=lOVcPooetrM), used at [3D parallelism](https://www.youtube.com/watch?v=lOVcPooetrM&t=480), [automatic partitioning](https://www.youtube.com/watch?v=lOVcPooetrM&t=720)
- **Lecture:** Song Han, "Lecture 14: LLM Post-Training", MIT 6.5940 (Fall 2024): [resolution versus tokens](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3240)
- **Reading:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, et al., "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale" (ICLR 2021): [arXiv](https://arxiv.org/abs/2010.11929)
- **Reading:** Robin Rombach, Andreas Blattmann, Dominik Lorenz, et al., "High-Resolution Image Synthesis with Latent Diffusion Models" (CVPR 2022): [arXiv](https://arxiv.org/abs/2112.10752)
- **Reading:** Jiaming Song, Chenlin Meng, Stefano Ermon, "Denoising Diffusion Implicit Models" (ICLR 2021): [arXiv](https://arxiv.org/abs/2010.02502)
- **Reading:** Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, Yuxiong He, "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models" (SC 2020): [arXiv](https://arxiv.org/abs/1910.02054)
- **Reading:** Yanan Li, Ji Lin, Song Han, "TSM: Temporal Shift Module for Efficient Video Understanding" (CVPR 2019): [arXiv](https://arxiv.org/abs/1811.08383)

## Next

→ [Course Summary and Outlook](11-course-summary-and-outlook.md): what the course treats as the frontier, and how to keep track of it.
