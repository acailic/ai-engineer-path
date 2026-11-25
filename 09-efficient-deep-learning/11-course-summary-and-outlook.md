# 11. Course Summary and Outlook

**Level:** Foundation · **Reading time:** 12 min · **Exercise:** 20 min
**Prerequisites:** [Why Efficiency Matters](01-why-efficiency-matters.md) and the four compression chapters, [03](03-pruning-and-sparsity.md) to [06](06-knowledge-distillation.md)

> **In one sentence:** After this chapter you can place any efficiency technique on one map, know which topics the course itself left open, and have a routine for staying current.

## Why this matters

Six months from now a new number format or attention variant appears, with a paper that reports a large speed-up. Should you adopt it? The answer depends on three things you already have: a measurement of your own system, a map of which technique addresses which cost, and the habit of checking claims against your hardware.

This chapter compresses the part into that map and adds the routine.

## The core idea: one map, one procedure

Song Han names the through-line of MIT 6.5940 in his first lecture: **algorithm and system co-design** (Lecture 1, [62:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3720)). Change the model and the software or hardware together. Every chapter was one application of that idea:

| Goal | Technique | Chapter |
|---|---|---|
| Efficient inference | pruning and sparsity | [03](03-pruning-and-sparsity.md) |
| | quantization | [04](04-quantization.md) |
| | architecture search | [05](05-neural-architecture-search.md) |
| | knowledge distillation | [06](06-knowledge-distillation.md) |
| | TinyML on microcontrollers | [07](07-tinyml-microcontrollers-and-tinyengine.md) |
| | language model deployment | [08](08-efficient-llm-inference-and-deployment.md) |
| Efficient training | parameter-efficient and on-device training | [09](09-llm-post-training-and-on-device-training.md) |
| | distributed training | [10](10-efficient-vision-generative-models-and-distributed-training.md) |
| Application-specific work | vision transformers, generative models, point clouds | [10](10-efficient-vision-generative-models-and-distributed-training.md) |

The procedure that goes with the map:

1. **Measure.** Latency, memory, energy and quality, on the real hardware and the real workload.
2. **Name the bottleneck.** Weight bytes, activation memory, the KV cache, arithmetic, or communication.
3. **Pick the lever for that bottleneck** (table below).
4. **Apply the cheapest lever first.** Quantize before you retrain. Distill only when the others are not enough.
5. **Re-measure quality and cost.**
6. **Stop when the budget is met.**

| Bottleneck | Levers |
|---|---|
| Too many weight bytes | weight-only quantization, a hardware-supported sparsity pattern, a smaller distilled model |
| Too much activation memory | lower resolution, patch-based inference, in-place operations, a memory-aware architecture |
| KV cache too large | shared heads, paging, cache quantization, attention sinks and windows |
| Decode too slow for one user | 4-bit weights, speculative decoding |
| Arithmetic-bound at large batch | 8-bit weights and activations, fused attention kernels |
| Training does not fit | parameter-efficient fine-tuning, sharding, gradient compression |
| A device with kilobytes | search under the memory constraint, 8-bit everywhere, a code-generating engine |

## What the course treats as the frontier

This part follows the Fall 2024 edition of the course. Four things in the final lectures mark where it was heading:

- **Training everywhere.** Han's closing recap in Lecture 22 lists data, pipeline, tensor and sequence parallelism and FSDP ([2:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120)). The lecture before it ends with training on a microcontroller under 256 KB of memory.
- **Smaller number formats with hardware support.** Lecture 6 covers microscaling formats such as MX4 and the FP4 tensor cores that NVIDIA's Blackwell generation introduced (as of that lecture).
- **Long context and alternatives to attention.** Lecture 15 closes with state-space models that keep a fixed-size state instead of a growing cache.
- **Quantum machine learning.** The last two lectures were given by Hanrui Wang, who had just graduated from Han's lab and was joining UCLA (Lecture 22, [2:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120), [4:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=240)). Wang begins from the devices: IBM's Condor chip passed 1,000 qubits, the quantum counterpart of a bit ([6:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=360)), but noise is so large that a program can rarely use them all, so much current work goes into error correction, where many physical qubits stand for one logical qubit ([8:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=480)). Training has its own limits. Circuits cannot simply be stacked deeper: with many qubits and layers, the variance of the gradients falls exponentially. Wang names this **barren plateau** problem, the quantum cousin of vanishing gradients, as one of the open bottlenecks (Lecture 23, [38:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2280)). The old toolbox travels: his QuantumNAS searches circuit architectures with a noise-aware objective (Lecture 23, [60:00](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3600)).

### What the course leaves open

Han's summary slides (Lecture 22, slides 2 to 9) do not list open problems. They draw the course as one map: efficient inference, efficient training (distributed training, on-device learning, federated learning) and application-specific work on language, vision-language and diffusion models, with a system layer from electrical engineering, an algorithm layer from computer science and an application layer from AI. His opening remark gives the principle behind it: open up the whole stack and co-design across it, because that opens a much larger design space ([0:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=0)).

The open questions he states are questions he hands to the class. Of quantum machine learning he asks what it is founded on and "how far away are we from quantum machine learning" ([2:00](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120)). Earlier in the course he leaves two concrete suggestions: trying network augmentation on small language models (Lecture 9), and fitting language models in on-chip memory with many small chips, which he says startups have since done (Lecture 4, [44:00](https://www.youtube.com/watch?v=upaZrpXkELc&t=2640)).

## How to keep track of it

This routine is this repository's own suggestion, not course content.

| What to watch | Where | How often | What to do with it |
|---|---|---|---|
| Benchmark results (MLPerf) | published result tables | each release | read which techniques the fast submissions used |
| The course's own materials | [efficientml.ai](https://efficientml.ai) and its lab code | each new offering | redo one lab |
| Research papers | arXiv, systems conferences such as MLSys | skim weekly | read one paper a month in depth |
| Hardware announcements | chip-makers' documentation | when released | check which formats and sparse patterns are supported |
| Inference engine release notes | the engine you use | monthly | test one new feature against your baseline |

The habit that matters most is the last row of the table above: test what you use against your baseline, and reproduce one number a month. A speed-up you have reproduced on your own hardware is knowledge. A speed-up you have read is a rumor.

## Pitfalls

1. **Chasing every new paper without a measurement problem.** Fix: start from your own bottleneck table.
2. **Adopting a format your engine does not implement.** Fix: check kernel support before promising a speed-up.
3. **Comparing numbers from different hardware and batch sizes.** Fix: compare only like with like, or measure yourself.
4. **Skipping the quality measurement.** Fix: pair every speed number with an evaluation result.
5. **Treating Fall 2024 numbers as current.** Fix: date every figure you reuse.

## Try it

Write a one-page efficiency review of a system you know.

1. Fill in the bottleneck table with measured numbers.
2. Choose one or two levers and write the saving you expect.
3. Find one technique published in the last twelve months that applies, with its source and date.

**You are done when** every claim has a date and a source, and every lever is tied to a measured bottleneck.

**Stretch:** reproduce the technique's headline number on your own hardware and report the gap.

## Key takeaways

- The map has three rows: efficient inference, efficient training, application-specific work.
- The procedure has one rule: measure, name the bottleneck, pick the lever for it, re-measure.
- The course's final topics were distributed and on-device training, low-bit formats, long context, and quantum machine learning.
- Everything here is dated Fall 2024. Re-check before relying on it.
- Reproduce one result a month to stay current in practice, not in theory.

## Self-check

1. A model is too slow for one user on a laptop, and profiling shows memory is the limit. Which lever comes first?
2. Why does quantization come before distillation in the procedure?
3. Name two topics from the course's final lectures.
4. A paper reports a 3 times speed-up on hardware you do not own. What do you do before using the number?
5. What is a barren plateau?

<details><summary>Show answers</summary>

1. Weight-only quantization to 4 bits, since weight traffic is the limit and no retraining is needed.
2. Because quantization needs no training run and no data, and distillation costs a full training run.
3. Any two of: distributed and on-device training, low-bit formats, long-context attention and state-space models, quantum machine learning.
4. Check the hardware and batch size, check that your engine supports the method, and measure it yourself if it matters.
5. A region where the gradients of a quantum circuit become vanishingly small as the circuit grows, which makes training stall.

</details>

## Sources

- **Lecture:** Song Han, "Lecture 22: Course Summary + Quantum Machine Learning (Part I)", MIT 6.5940 TinyML and Efficient Deep Learning Computing (Fall 2024): [video](https://www.youtube.com/watch?v=svjjD2uthhQ) · [guide](../lectures/mit-22-course-summary-quantum-machine-learning-i.md), used at [closing recap](https://www.youtube.com/watch?v=svjjD2uthhQ&t=120)
- **Lecture:** Song Han, "Lecture 23: Quantum Machine Learning (Part II)", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=ZDk-GsyInt8) · [guide](../lectures/mit-23-quantum-machine-learning-ii.md), used at [barren plateaus](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=2280), [architecture search for circuits](https://www.youtube.com/watch?v=ZDk-GsyInt8&t=3600)
- **Lecture:** Song Han, "Lecture 1: Introduction", MIT 6.5940 (Fall 2024): [algorithm and system co-design](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3720)
- **Reading:** EfficientML.ai course site, slides, videos and labs: [efficientml.ai](https://efficientml.ai)
- **Reading:** Hanrui Wang, Yongshan Ding, Jiaqi Gu, et al., "QuantumNAS: Noise-Adaptive Search for Robust Quantum Circuits" (HPCA 2022): [arXiv](https://arxiv.org/abs/2107.10845)

## Next

→ Two directions. For the architecture underneath all of this, [transformer architectures](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md). For putting a compressed model into production, [deploying a model](../07-ml-in-production/07-deploying-a-model.md).
