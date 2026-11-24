# Part 10: LLM Internals

How a language model is built end to end, following Stanford CS336, *Language Modeling from Scratch* (Spring 2026, Percy Liang and Tatsunori Hashimoto). The course teaches by having students build everything. These chapters explain the same material for someone who is reading rather than enrolled.

The thread through all thirteen chapters is one idea from Lecture 1: train the best model you can with a fixed budget of compute and memory, and judge every design choice by it.

## Who this is for

A software engineer with no machine-learning background who wants to understand what is under the API: why text is split into tokens, why one operation is slow and another fast, how big a model to train for a given budget, where the training data comes from, and what turns a base model into an assistant.

## Chapters

| # | Chapter | Level | Min | What it covers |
|---|---|---|---|---|
| 01 | [The Language Modeling Pipeline and Tokenization](01-the-language-modeling-pipeline-and-tokenization.md) | Practitioner | 16 | The course map; bytes, words and byte-pair encoding |
| 02 | [Resource Accounting: FLOPs, Memory and Arithmetic Intensity](02-resource-accounting-flops-memory-and-arithmetic-intensity.md) | Practitioner | 15 | Estimating time and memory; compute-bound versus memory-bound |
| 03 | [Transformer Architectures and Hyperparameters](03-transformer-architectures-and-hyperparameters.md) | Practitioner | 16 | What modern Transformers agree on; the numbers that matter |
| 04 | [Attention Alternatives and Mixture of Experts](04-attention-alternatives-and-mixture-of-experts.md) | Professional | 15 | Cheaper attention for long context; MoE layers |
| 05 | [GPUs, TPUs and Kernels](05-gpus-tpus-and-kernels.md) | Professional | 16 | Memory hierarchy, kernels, Triton, FlashAttention |
| 06 | [Parallelism](06-parallelism.md) | Professional | 15 | Data, pipeline and tensor parallelism; sharding |
| 07 | [Scaling Laws](07-scaling-laws.md) | Professional | 16 | Fitting and using them; muP; WSD schedules |
| 08 | [Inference](08-inference.md) | Practitioner | 15 | Why generation is memory-bound; KV cache; serving |
| 09 | [Evaluating Language Models](09-evaluating-language-models.md) | Practitioner | 14 | Choosing an evaluation; contamination and validity |
| 10 | [Training Data](10-training-data.md) | Practitioner | 16 | Sources, filtering, deduplication, mixing |
| 11 | [Post-Training: SFT, RLHF and RLVR](11-post-training-sft-rlhf-and-rlvr.md) | Professional | 17 | Imitation and reinforcement; GRPO |
| 12 | [Alignment and Multimodality](12-alignment-and-multimodality.md) | Professional | 14 | What alignment means here; images as tokens |
| 13 | [Building Your Own: A Roadmap Through the Assignments](13-building-your-own-a-roadmap-through-the-assignments.md) | Practitioner | 14 | The five assignments, order, compute, traps |

## Three ways to read

- **The full build.** Read 01 to 13 in order. Each chapter assumes the two or three before it.
- **You build on top of models.** Read 01, 02, 03, 08, 09 and 11. That explains tokens, why speed is about memory, how to read a benchmark score, and what post-training changes.
- **You care about performance.** Read 02, then 05, 06 and 08, with 04 for the architecture side.

## How it connects to the rest of the course

- The big picture of pretraining is in [how large language models are trained](../01-foundations/02-how-large-language-models-are-trained.md). This part goes one level down.
- Quantization and deployment have their own treatment in [efficient deep learning](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md). Chapter 08 covers only what the CS336 lecture does.
- Chapter 09 explains how a research lab evaluates models. For evaluating an application, start with [evaluation is the product](../03-evaluation/01-evaluation-is-the-product.md).
- Chapter 11 assumes the overview in [from base model to assistant](../01-foundations/03-from-base-model-to-assistant-post-training.md).

## A note on sources

Each chapter is built on one or two CS336 lectures and cites them with timestamps. Statements from a lecturer are attributed and dated: model names, prices and court cases are as reported in the Spring 2026 lectures. Where a chapter goes beyond what the lecture covers, the text says so. Code examples are plain Python and were run before being included, except where a snippet is labeled as illustrative.
