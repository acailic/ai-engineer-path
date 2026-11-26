# Part 09: Efficient Deep Learning and Edge AI

Make a model smaller, faster and cheaper, and run it on a laptop, a phone or a microcontroller.

This part follows **MIT 6.5940, TinyML and Efficient Deep Learning Computing, Fall 2024 edition** (Song Han), with the lecture videos on the [EfficientML.ai](https://efficientml.ai) site. Each chapter cites the moments it uses. Numbers reported in the lectures are from Fall 2024 and are marked as such; model names, formats and hardware move fast, so date anything you reuse.

## What you can do afterwards

- Estimate a model's memory, latency and energy on paper before running it.
- Prune, quantize and distill a model, and know what each step costs in accuracy.
- Choose a serving setup for a language model: precision, batching, KV cache and decoding tricks.
- Check whether a model fits a microcontroller, and get it there.
- Decide between pruning, quantization, search and distillation for a given budget.

## Chapters

| # | Chapter | Level | Min | What it covers |
|---|---|---|---|---|
| 01 | [Why Efficiency Matters](01-why-efficiency-matters.md) | Foundation | 10 | the four resources a model burns, and where they can be saved |
| 02 | [Neural Network Basics for Efficiency](02-neural-network-basics-for-efficiency.md) | Foundation | 18 | counting parameters, operations and memory; latency versus throughput |
| 03 | [Pruning and Sparsity](03-pruning-and-sparsity.md) | Practitioner | 20 | removing weights so that quality survives and hardware notices |
| 04 | [Quantization](04-quantization.md) | Practitioner | 22 | number formats, linear quantization, post-training quantization, quantization-aware training |
| 05 | [Neural Architecture Search](05-neural-architecture-search.md) | Practitioner | 15 | search spaces, search algorithms, hardware awareness, once-for-all networks |
| 06 | [Knowledge Distillation](06-knowledge-distillation.md) | Practitioner | 18 | teacher and student training, what to match, self-distillation |
| 07 | [TinyML: Microcontrollers and TinyEngine](07-tinyml-microcontrollers-and-tinyengine.md) | Practitioner | 19 | flash and SRAM budgets, patch-based inference, inference engines |
| 08 | [Efficient LLM Inference and Deployment](08-efficient-llm-inference-and-deployment.md) | Practitioner | 24 | prefill and decode, KV cache, attention, batching, speculative decoding, long context |
| 09 | [LLM Post-Training and On-Device Training](09-llm-post-training-and-on-device-training.md) | Practitioner | 15 | parameter-efficient fine-tuning, quantized training, training on the device |
| 10 | [Efficient Vision, Generative Models and Distributed Training](10-efficient-vision-generative-models-and-distributed-training.md) | Practitioner | 15 | vision transformers, GANs and diffusion, parallelism across machines |
| 11 | [Course Summary and Outlook](11-course-summary-and-outlook.md) | Foundation | 12 | one map of the whole part, the course's open topics, a routine for staying current |

"Min" is reading time. Each chapter header also gives the time for its exercise.

## How to read this part

- **Compression route:** 01, 02, 03, 04, 06. Start here if you have a model that must shrink.
- **Language model serving route:** 02, 04, 08, then 09. Start here if you deploy language models.
- **Edge route:** 02, 05, 07, then 09. Start here if you target phones or microcontrollers.

Chapter 02 is the only real prerequisite for everything else: it defines the counts and the latency-versus-throughput reasoning the later chapters rely on.

## Related parts

- [How large language models are trained](../01-foundations/02-how-large-language-models-are-trained.md) gives the training picture this part assumes.
- [Transformer architectures](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md), [parallelism](../10-llm-internals/06-parallelism.md) and [scaling laws](../10-llm-internals/07-scaling-laws.md) go deeper on the model internals that this part only summarizes.
- [Deploying a model](../07-ml-in-production/07-deploying-a-model.md) covers the production architecture around an efficient model.
- [A minimal eval harness](../03-evaluation/02-a-minimal-eval-harness.md): every compression step needs it to measure the quality loss.

## Lecture guides for this part

Each guide maps one lecture from its first minute to its last and says where this book teaches each piece. Where no chapter teaches a part of the lecture, the guide explains it itself; the table counts those parts.

| Lecture | Lecturer | Length | Parts no chapter teaches | Guide |
|---|---|---|---|---|
| Introduction | Song Han (MIT) | 1:06:00 | 0 of 17 | [open guide](../lectures/mit-01-introduction.md) |
| Transformer and LLM | Song Han (MIT) | 1:18:00 | 2 of 20 | [open guide](../lectures/mit-12-transformer-and-llm.md) |
| Efficient LLM Deployment | Song Han (MIT) | 1:18:00 | 0 of 20 | [open guide](../lectures/mit-13-efficient-llm-deployment.md) |
| LLM Post Training | Song Han (MIT) | 1:18:00 | 1 of 17 | [open guide](../lectures/mit-14-llm-post-training.md) |
| Long Context LLM | Song Han (MIT) | 1:14:00 | 0 of 19 | [open guide](../lectures/mit-15-long-context-llm.md) |
| Basics of Deep Learning | Song Han (MIT) | 52:00 | 1 of 17 | [open guide](../lectures/mit-02-basics-of-deep-learning.md) |
| Distributed Training (Part I) | Song Han (MIT) | 1:10:00 | 2 of 17 | [open guide](../lectures/mit-19-distributed-training-part-i.md) |
| Distributed Training (Part II) | Song Han (MIT) | 1:00:00 | 2 of 16 | [open guide](../lectures/mit-20-distributed-training-part-ii.md) |
| On-Device Training and Transfer Learning | Song Han (MIT) | 1:06:00 | 0 of 16 | [open guide](../lectures/mit-21-on-device-training-and-transfer-learning.md) |
| Pruning and Sparsity (Part I) | Song Han (MIT) | 58:00 | 0 of 15 | [open guide](../lectures/mit-03-pruning-and-sparsity-part-i.md) |
| Pruning and Sparsity (Part II) | Song Han (MIT) | 1:10:00 | 1 of 19 | [open guide](../lectures/mit-04-pruning-and-sparsity-part-ii.md) |
| Quantization (Part I) | Song Han (MIT) | 1:08:00 | 0 of 17 | [open guide](../lectures/mit-05-quantization-part-i.md) |
| Quantization (Part II) | Song Han (MIT) | 1:10:00 | 0 of 19 | [open guide](../lectures/mit-06-quantization-part-ii.md) |
| Neural Architecture Search (Part I) | Song Han (MIT) | 1:08:00 | 0 of 19 | [open guide](../lectures/mit-07-neural-architecture-search-part-i.md) |
| Neural Architecture Search (Part II) | Song Han (MIT) | 1:18:00 | 0 of 19 | [open guide](../lectures/mit-08-neural-architecture-search-part-ii.md) |
| Knowledge Distillation | Song Han (MIT) | 1:00:00 | 2 of 18 | [open guide](../lectures/mit-09-knowledge-distillation.md) |
| MCUNet: TinyML on Microcontrollers | Song Han (MIT) | 1:08:00 | 1 of 18 | [open guide](../lectures/mit-10-mcunet-tinyml-on-microcontrollers.md) |
| TinyEngine and Parallel Processing | Song Han (MIT) | 1:12:00 | 0 of 15 | [open guide](../lectures/mit-11-tinyengine-and-parallel-processing.md) |
| Course Summary + Quantum Machine Learning I | Song Han (MIT) | 1:24:00 | 1 of 19 | [open guide](../lectures/mit-22-course-summary-quantum-machine-learning-i.md) |
| Vision Transformer | Song Han (MIT) | 1:02:00 | 1 of 18 | [open guide](../lectures/mit-16-vision-transformer.md) |
| GAN, Video, and Point Cloud | Song Han (MIT) | 1:12:00 | 5 of 17 | [open guide](../lectures/mit-17-gan-video-and-point-cloud.md) |
| Diffusion Model | Song Han (MIT) | 1:12:00 | 5 of 18 | [open guide](../lectures/mit-18-diffusion-model.md) |
| Quantum Machine Learning II | Song Han (MIT) | 1:14:00 | 2 of 20 | [open guide](../lectures/mit-23-quantum-machine-learning-ii.md) |

## Going further

The original course has five hands-on labs, in order: pruning, quantization, architecture search, language model compression, and deploying a quantized language model on your own laptop. They are published on the course site. The exercises in these chapters are smaller versions of the same ideas and need only Python and NumPy.
