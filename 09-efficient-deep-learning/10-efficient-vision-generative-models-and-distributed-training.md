# 10. Efficient Vision, Generative Models and Distributed Training

**Level:** Practitioner · **Reading time:** 12 min · **Exercise:** 30 min
**Prerequisites:** [Neural Network Basics for Efficiency](02-neural-network-basics-for-efficiency.md), [Efficient LLM Inference and Deployment](08-efficient-llm-inference-and-deployment.md) for the cost of attention

> **In one sentence:** After this chapter you can name, for a vision model, an image generator or a training job on many machines, the cost that grows fastest, the standard moves against it and the chapter that teaches each in detail.

## Why this matters

The techniques so far were introduced on classifiers and language models. They reappear in three more places, each with its own dominant cost:

- a segmentation model on a drone, where attention over millions of pixels is the problem;
- an image generator, where the problem is running a large network dozens of times per image;
- a training job that does not fit on one GPU.

This chapter is the map of these places. For each it gives the cost that grows fastest, the standard moves and one worked number. The chapters that follow take one place each: [12](12-vision-transformers.md) vision transformers, [13](13-gans-video-and-point-clouds.md) GANs, video and point clouds, [14](14-efficient-diffusion-models.md) diffusion models, [15](15-distributed-training.md) training across machines.

## The core idea: find the term that grows fastest

Every cost in this part is a product. [Chapter 02](02-neural-network-basics-for-efficiency.md) counts parameters, operations and memory, and asks how large each term is. Here the question is how fast each term grows when the input grows. The term that grows fastest is the one to attack.

| Place | The cost, written as a product | The term that grows fastest | Standard moves | Chapter |
|---|---|---|---|---|
| Vision transformer | attention entries = patches² per head; the patches grow with the resolution² | attention, with the fourth power of the resolution | window attention, linear attention, sparse windows | [12](12-vision-transformers.md) |
| GAN | the generator runs once per pixel at inference | the generator's size | prune the generator; one generator for several budgets | [13](13-gans-video-and-point-clouds.md) |
| Video and point clouds | a 3D convolution weighs and computes far more than a 2D one | the extra dimension | shift channels in time; a voxel branch beside a point branch | [13](13-gans-video-and-point-clouds.md) |
| Diffusion model | steps × cost per step; the cost per step grows with its tokens | both factors | fewer steps, fewer tokens, cheaper attention, skip unchanged regions | [14](14-efficient-diffusion-models.md) |
| Training on many machines | memory per GPU; bytes exchanged per step | the model's size and the communication | data, pipeline, tensor and sequence parallelism; sharding; gradient compression | [15](15-distributed-training.md) |

The families in one sentence each:

- A **vision transformer** cuts an image into patches, treats each patch as a token, and runs a transformer encoder over them.
- A **generative model** produces images, video or 3D content instead of a label.
- A **GAN**, a generative adversarial network, has a generator and a discriminator, which learns to tell real images from generated ones; only the generator runs at inference (Han, Lecture 17, [2:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=120)).
- A **diffusion model** learns to remove noise step by step; starting from pure noise, it produces an image after many steps (Lecture 18, [2:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=120)).

## Three numbers to keep

**Vision.** A 224 × 224 image cut into 16 × 16 patches gives 196 tokens and 38,416 attention entries per head. At 1,024 × 1,024 it gives 4,096 tokens and 16.8 million entries: an image 4.6 times larger on each side costs 21 times more tokens and 436 times more attention. Han makes the point in the lecture by raising the resolution: a vision transformer's computation grows with the fourth power of the resolution, much faster than a convolutional network's (Lecture 16, [8:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=480)). His example of the gain is segmentation on a Jetson Orin at FP16 and batch size one: from 1.6 to 21 frames per second while keeping the accuracy. His EfficientViT results cover segmentation on Cityscapes, super-resolution and Segment Anything, which is where [Chapter 01](01-why-efficiency-matters.md) got its 182 images per second example (Lecture 16, [24:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1440)).

**Generation.** An illustration with round numbers: 50 denoising steps on 16,384 tokens are 819,200 token-steps per image. 20 steps on 256 tokens are 5,120. That is 160 times less work, before any change to the network itself. [Chapter 14](14-efficient-diffusion-models.md) gives the lecture's own figures for each way of getting there.

**Training.** On a single GPU, the training of GPT-3 would take 355 years (Lecture 19, [2:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=120)). Data parallelism, several GPUs that each hold the whole model, saves time and no memory. For memory, Han presents ZeRO, which shards the optimizer state, the gradients and the weights across GPUs, stage by stage (Lecture 19, [36:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2160), [38:00](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2280)). Worked numbers for the 7-billion-parameter model of [Chapter 09](09-llm-post-training-and-on-device-training.md): 112 GB before activations on one GPU, about 14 GB per GPU on eight.

## How to choose the move

1. **Write the cost as a product.** Attention entries, steps × tokens, memory per GPU, bytes per step.
2. **Double what worries you** and see which term grows fastest: the resolution, the image size, the number of GPUs.
3. **Pick the move that changes that term's growth**, not the one with the best percentage in a paper. Window attention turns the square of the patch count into a linear term; a more compressed latent space cuts the tokens of every step at once.
4. **Measure latency on the target.** Fewer MACs is never the whole story. Han reports latency on an Orin, an edge chip serving one user, and throughput on an A100, a cloud chip serving many (Lecture 16, [24:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1440)).

## What the practitioners say

Three of Han's remarks hold for every place in the table.

- **Each technique added for quality adds computation** (Lecture 18, [30:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=1800)). The clearest case is guidance, which evaluates the model twice per step; [Chapter 14](14-efficient-diffusion-models.md) shows its two forms.
- **More tokens are not automatically better, and they are never cheap.** For the VILA vision-language model he reports that the image's original resolution matters more than its number of tokens (Lecture 14, [54:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3240)).
- **Computation is cheap and data movement is expensive.** Synchronous training exchanges gradients after every iteration, so the network, not the processor, can set the time of a large run (Lecture 20, [12:00](https://www.youtube.com/watch?v=lOVcPooetrM&t=720)).

## Worked example

A cost sheet with one line per family, each number next to its formula:

| Family | Formula | Result |
|---|---|---|
| Vision transformer at 224 × 224 | 196² | 38,416 attention entries per head |
| The same at 1,024 × 1,024 | 4,096² | 16.8 million entries |
| Diffusion, many steps on many tokens (an illustration) | 50 steps × 16,384 tokens | 819,200 token-steps per image |
| Diffusion, fewer of each (an illustration) | 20 steps × 256 tokens | 5,120 token-steps |
| Training a 7-billion-parameter model on one GPU | 7 billion × 16 bytes | 112 GB before activations |
| The same on eight GPUs, sharded | 112 GB ÷ 8 | 14 GB per GPU |

The two diffusion lines illustrate the rule steps × tokens; they are not figures of the lecture. The 112 GB are [Chapter 09](09-llm-post-training-and-on-device-training.md)'s account of training a 7-billion-parameter model before activations: 14 GB of weights, 14 GB of gradients and 84 GB of optimizer state. The last two lines are the reason data parallelism alone does not fit a large model: without sharding, every GPU holds the same 112 GB.

## Pitfalls

1. **Counting only the linear layers in a high-resolution transformer.** Fix: include the `N²` attention term.
2. **Comparing diffusion models by cost per step.** Fix: multiply by the number of steps and the token count.
3. **Using data parallelism to fit a large model.** Fix: shard with FSDP or split the model.
4. **Tensor parallelism across a slow link.** Fix: keep it inside one machine; use pipeline parallelism between machines.
5. **Dropping small gradients without momentum correction.** Fix: accumulate velocity, not raw gradients, as Han's deep gradient compression slides show.

## Try it

Extend the cost sheet of this chapter to a system you know.

1. A vision transformer at two resolutions: token count and attention entries.
2. A diffusion model: steps × tokens per step, for the original and for a compressed latent space.
3. A 7-billion-parameter training run: memory per GPU with 8-way FSDP.

**You are done when** every number has its formula next to it.

**Stretch:** verify the two vision transformer numbers in three lines of Python.

## Key takeaways

- Find the term that grows fastest; it names the move.
- Vision transformers: attention grows with the square of the patch count, so with the fourth power of the resolution. Windows, linear attention and sparsity make it linear.
- Diffusion: cost is steps × tokens. Cut both.
- Data parallelism saves time, not memory. Sharding saves memory.
- Fewer MACs is never the whole story; measure latency on the target.

## Self-check

1. Doubling an image's side length multiplies the number of tokens by 4. What happens to the attention cost?
2. A diffusion model needs 50 steps on 16,384 tokens. Give two independent ways to cut its cost.
3. Which parallelism leaves memory per GPU unchanged?
4. What is sharded across GPUs to bring a 7-billion-parameter training run from 112 GB on one GPU down to about 14 GB on each of eight?
5. A vision transformer on 1,024 × 1,024 images is too slow. Which term do you attack first, and which moves change how it grows?
6. Han says that each technique added for quality adds computation. Give his clearest case.

<details><summary>Show answers</summary>

1. It grows by 16 times, since attention is proportional to tokens squared.
2. Fewer sampling steps, and fewer tokens per step by working in a more compressed latent space.
3. Data parallelism, because every GPU holds a full copy of the model.
4. The optimizer state, the gradients and the weights.
5. Attention, which grows with the square of the patch count and so with the fourth power of the resolution. Window attention, linear attention and sparse windows make it linear.
6. Guidance, which evaluates the diffusion model twice at every step.

</details>

## Sources

- **Lecture:** Song Han, "Lecture 16: Vision Transformer", MIT 6.5940 TinyML and Efficient Deep Learning Computing (Fall 2024): [video](https://www.youtube.com/watch?v=v0jYDgaVzlk) · [guide](../lectures/mit-16-vision-transformer.md), used at [resolution cost](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=480), [latency and throughput](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1440)
- **Lecture:** Song Han, "Lecture 17: Efficient GAN, Video, and Point Cloud", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=o_60Yhb79W8) · [guide](../lectures/mit-17-gan-video-and-point-cloud.md), used at [GANs](https://www.youtube.com/watch?v=o_60Yhb79W8&t=120)
- **Lecture:** Song Han, "Lecture 18: Diffusion Model", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=LXrqmQrscf0) · [guide](../lectures/mit-18-diffusion-model.md), used at [the diffusion model](https://www.youtube.com/watch?v=LXrqmQrscf0&t=120), [cost of conditioning](https://www.youtube.com/watch?v=LXrqmQrscf0&t=1800)
- **Lecture:** Song Han, "Lecture 19: Distributed Training (Part I)", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=LcOM-nZdqxw) · [guide](../lectures/mit-19-distributed-training-part-i.md), used at [motivation](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=120), [ZeRO and FSDP](https://www.youtube.com/watch?v=LcOM-nZdqxw&t=2160)
- **Lecture:** Song Han, "Lecture 20: Distributed Training (Part II)", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=lOVcPooetrM) · [guide](../lectures/mit-20-distributed-training-part-ii.md), used at [communication cost](https://www.youtube.com/watch?v=lOVcPooetrM&t=720)
- **Lecture:** Song Han, "Lecture 14: LLM Post-Training", MIT 6.5940 (Fall 2024): [resolution versus tokens](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3240)
- **Reading:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, et al., "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale" (ICLR 2021): [arXiv](https://arxiv.org/abs/2010.11929)
- **Reading:** Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase, Yuxiong He, "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models" (SC 2020): [arXiv](https://arxiv.org/abs/1910.02054)

## Next

→ [Vision Transformers](12-vision-transformers.md): why attention over patches costs so much, and the moves that make it linear.
