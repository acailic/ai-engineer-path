# 05. Capstone 4: Efficient Inference

**Level:** Practitioner · **Reading time:** 20 min · **Exercise:** 25 h
**Prerequisites:** [Quantization](../09-efficient-deep-learning/04-quantization.md), [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md)

> **In one sentence:** After this project you have taken one small open model, measured its latency, memory and quality, made it smaller with quantization, and reported the trade-off in a table that says what was measured on which machine.

## Why this matters

A model that scores well and does not fit on the machine is not a feature. [Quantization](../09-efficient-deep-learning/04-quantization.md) opens with the arithmetic. A model with 7 billion parameters needs 14 GB for its weights in 16-bit, so it does not load on a laptop with 8 GB. In 4-bit the same weights need 3.5 GB.

After every compression the questions are the same. What did it cost in quality? Did it make anything faster? Answering them is an engineering job with a fixed shape: measure, compress, measure again, compare.

## The goal

Take one small open model, a file from a model hub such as Hugging Face. Measure its latency, memory and quality. Compress it, with quantization at minimum and [pruning](../09-efficient-deep-learning/03-pruning-and-sparsity.md) or [distillation](../09-efficient-deep-learning/06-knowledge-distillation.md) as optional stages. Then report the trade-off between size, speed and quality, in numbers that another engineer can check.

## Two tracks

| Track | Model | Hardware | What it teaches |
|---|---|---|---|
| A | A small open classifier, or another small model you can load | Any laptop | The whole procedure, end to end, with nothing hidden |
| B | A small open-weights language model | A laptop that can load it. A GPU only for training-based stages | Where the money is: quantizing the weights and the [KV cache](../GLOSSARY.md) |

Do track A first. It takes 8 to 12 hours and works through the five deliverables in one pass; the milestones below are track B's. Then do track B. Both run on a laptop. Numbers measured on a CPU are real numbers. They are not GPU numbers, and the report says so.

## What hardware is needed

| Task | Laptop, CPU only | GPU |
|---|---|---|
| Measure latency, memory and quality of a small model | Yes | Needed only for GPU latency numbers |
| Post-training quantization of the weights | Yes | Not needed |
| Check the quality of the compressed model | Yes, more slowly | Faster |
| Quantization-aware training, pruning with fine-tuning, distillation | Only for a tiny model | Needed |
| Speedups that depend on special low-bit hardware | No | The matching hardware |

Start track B at a billion parameters or fewer. Weight memory is parameters times bytes. A billion parameters take about 2 GB in 16-bit, 1 GB in 8-bit, and 0.5 GB in 4-bit, before the cache and the overhead.

One pitfall from the quantization chapter decides what you can promise. A smaller file is not a faster model unless the inference engine, the program that loads the model and runs it, has a fast [kernel](../GLOSSARY.md) for that format. Which engine supports which format changes quickly. As of 2026-11-24, check the documentation of the engine you pick. [Inference](../10-llm-internals/08-inference.md) names four engines. [Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) covers the serving side.

## Deliverables

1. **A baseline table.** Parameter count, size, latency, peak memory and quality, before any compression.
2. **A quality evaluation.** A fixed task set, and for a language model a held-out text for perplexity.
3. **Variants.** Float, 8-bit and 4-bit. Optionally a pruned or a distilled model.
4. **The final table.** Size, latency, memory and quality for every variant, with the hardware named.
5. **A report of one page.** The trade-off, what was not comparable, and what you recommend.

## Milestones

### Milestone 1: measure the baseline (4 to 6 hours)

Read [Neural Network Basics for Efficiency](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) for latency against throughput, FLOPs, parameter counting and memory, and [Why Efficiency Matters](../09-efficient-deep-learning/01-why-efficiency-matters.md) for latency and energy budgets.

- [ ] Parameter count recorded. Weight memory computed as parameters times bytes, and checked against the file size. Any gap is explained.
- [ ] Latency measured after warm-up, at least 20 times, one input at a time. Reported as a median and a 95th percentile. For a language model: time to first token and tokens per second, at a fixed prompt length and output length.
- [ ] Peak memory during one inference, recorded.
- [ ] Hardware, engine and their versions, written down.
- [ ] Track B: the size of the cache of past tokens at your prompt length, estimated and set beside the weights. [Inference](../10-llm-internals/08-inference.md) shows how to bound a model's speed from memory bandwidth and that cache. Per token, the cache takes `2 × layers × heads × head size × bytes per value`.

No chapter shows how to time a call. Read `time.perf_counter()` before and after one call, discard three warm-up calls, and report the median and the 95th percentile of the rest. For peak memory, start `tracemalloc` before the call and read its peak after it. A deep-learning framework allocates mostly outside it: use its own peak counter and name it.

### Milestone 2: build the quality evaluation first (3 to 5 hours)

Read [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md) and [Evaluating Language Models](../10-llm-internals/09-evaluating-language-models.md).

- [ ] A fixed set of at least 50 tasks with answers a program can check, or a labeled test set for a classifier. For a language model, fifty arithmetic questions in the harness's task format will do.
- [ ] Track B: a held-out text for [perplexity](../GLOSSARY.md), beside the task set.
- [ ] The baseline score, with a [standard error](../03-evaluation/05-statistics-for-evals.md).
- [ ] A written limit: the largest quality loss you accept.

The fourth pitfall of the quantization chapter is judging quality by one prompt or by perplexity alone. Its fix is to run an evaluation set against the float baseline.

### Milestone 3: quantize (6 to 8 hours)

Read [Quantization](../09-efficient-deep-learning/04-quantization.md), and the compression levers in [Inference](../10-llm-internals/08-inference.md).

- [ ] Float, 8-bit and 4-bit variants exist as files you can load.
- [ ] The 4-bit variant uses per-channel or group scales. The report notes what changed from one scale per tensor.
- [ ] Sensitive layers stay in 16 bits: embeddings, the first and the last layer, the final normalization.
- [ ] Track B: only the weights are quantized. Activations stay in floating point, which is the quantization chapter's choice for language models on one machine.
- [ ] The size arithmetic is checked again for each variant.

Follow the chapter's procedure: fix a float baseline, compute the [scales](../GLOSSARY.md), run a few hundred representative inputs to record each activation's range, quantize, and evaluate on real tasks.

### Milestone 4 (optional): prune or distill (6 to 10 hours)

Read [Pruning and Sparsity](../09-efficient-deep-learning/03-pruning-and-sparsity.md) and [Knowledge Distillation](../09-efficient-deep-learning/06-knowledge-distillation.md).

- [ ] One pruning pass, with the quality recorded after each step, and the report saying which kind of sparsity you produced.
- [ ] Or one distillation run, with the student evaluated on real labels and not on agreement with its teacher.
- [ ] The new rows added to the table.

### Milestone 5: measure again and report (4 to 6 hours)

Read [Quality Attributes of ML Components](../07-ml-in-production/06-quality-attributes-of-ml-components.md).

- [ ] The final table: variant, size, latency as median and 95th percentile, peak memory, quality with its standard error, hardware.
- [ ] The dominated variants named, those worse on every attribute, and the choice made among the rest.
- [ ] For each speedup, or its absence, a stated reason.
- [ ] Every number measured on one machine, or the differences named.

## You are done when

1. The baseline was measured before any compression.
2. The quality evaluation existed before any compression, with a written limit.
3. Three variants were measured: float, 8-bit and 4-bit.
4. The size arithmetic matches the measured file sizes, or the gap is explained.
5. Latency is reported as a median and a 95th percentile over at least 20 runs.
6. The report names the hardware, the engine and the date for every number.

## Effort, tools and cost

Track A takes 8 to 12 hours. Track B takes 17 to 25 hours. You need Python 3.10 or newer, NumPy (the quantization chapter's snippet uses it), the library that loads your model, and for track B an inference engine that supports the quantized format.

The project is free on a laptop. A rented GPU costs money. You need one for the optional stage, for GPU latency numbers, and for any training-based compression. [Building Your Own](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) lists prices for one GPU type, with their date. Check current prices before you budget.

## Stretch goals

- **Quantization-aware training**, if post-training quantization lost more quality than your limit allows ([Quantization](../09-efficient-deep-learning/04-quantization.md)).
- **Mixed precision per layer.** Cheap or memory-bound layers stay in 16 or 32 bits, and compute-bound layers go lower. The same chapter.
- **Smoothing activation outliers** into the weights, the idea the quantization chapter describes from a course project.
- **A smaller cache** of past tokens, through the attention variants and cache levers in [Inference](../10-llm-internals/08-inference.md).
- **Energy**, measured beside latency ([Why Efficiency Matters](../09-efficient-deep-learning/01-why-efficiency-matters.md)).
- **A microcontroller**, if the classifier of track A is small enough ([TinyML: Microcontrollers and TinyEngine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md)).

## Pitfalls

1. **Measuring once, or cold.** Fix: warm-up, then at least 20 runs, median and 95th percentile.
2. **Numbers from different machines or engines.** Fix: one machine, one engine, or say what differs.
3. **One prompt, or perplexity alone.** Fix: a task set beside perplexity.
4. **Assuming smaller means faster.** Fix: check the engine's kernel support for the format.
5. **One scale at 4 bits.** Fix: per-channel scales, and group scales below 8 bits.
6. **Every layer at the same width.** Fix: sensitive layers stay in 16 bits.
7. **Forgetting the cache of past tokens.** With long inputs it can outweigh the weights.
8. **A different evaluation set for each variant.** Fix: one set, fixed before the first compression.
9. **An average without a spread.** Fix: the 95th percentile and the standard error.
10. **A number without its date and versions.** Fix: hardware, engine and date in every table.

## What the practitioners say

- **Quantization is the workhorse.** Song Han calls it very widely used in industry, and 8-bit mature ([Quantization](../09-efficient-deep-learning/04-quantization.md)).
- **Post-training first.** His order: try post-training quantization, and move to quantization-aware training only when the evaluation shows a real loss. The same chapter.
- **Generation is limited by memory.** The inference chapter of part 10 bounds a model's speed from memory bandwidth ([Inference](../10-llm-internals/08-inference.md)).
- **Argue on the front.** Kästner's method for quality attributes: cut the design space with hard constraints, and argue only among the designs left ([Quality Attributes of ML Components](../07-ml-in-production/06-quality-attributes-of-ml-components.md)).

## Try it

The project is the exercise. Start with one hour:

1. Pick the smallest model you already use.
2. Write down its parameter count, and compute its weight memory at 16 bits.
3. Time one inference 20 times, after three warm-up runs. Write down the median.

**You are done with the first hour when** you have three numbers on paper: parameters, bytes and milliseconds.

## Key takeaways

- Measure before you compress: latency, memory and quality, on named hardware.
- Build the quality evaluation first, with a written limit on the loss.
- Try post-training quantization first. Go finer in granularity before you go to retraining.
- A smaller file is a faster model only if the engine has a fast kernel for the format.
- Report the trade-off as a table with a spread, a date and a machine.
- Both tracks run on a laptop. A GPU is for training-based stages and for GPU numbers.

## Self-check

1. Why must the quality evaluation exist before the first compression?
2. A 4-bit model loads in a quarter of the memory and runs at the same speed as the 16-bit model. What is the first explanation to check?
3. Why report a task set beside perplexity?
4. Which layers stay in 16 bits?
5. What two latency numbers does a language model need that a classifier does not?
6. Why measure latency at least 20 times after warm-up?

<details><summary>Show answers</summary>

1. Without a fixed evaluation and a written limit, there is no number to compare a variant against. The temptation is then to judge by one prompt.
2. Whether the inference engine has a fast kernel for that format. Without one, the compression saved memory only.
3. Perplexity is one average over held-out text. The quantization chapter counts it alone as a way of judging quality wrongly, and asks for an evaluation set on real tasks.
4. Embeddings, the first and the last layer, and the final normalization. They are the sensitive ones, so they stay in higher precision.
5. Time to first token, and tokens per second. Each is measured at a fixed prompt length and output length.
6. The first runs are cold and slower. A median and a 95th percentile over many runs describe a distribution. One run does not.

</details>

## Sources

- Part 09: [Why Efficiency Matters](../09-efficient-deep-learning/01-why-efficiency-matters.md), [Neural Network Basics for Efficiency](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md), [Pruning and Sparsity](../09-efficient-deep-learning/03-pruning-and-sparsity.md), [Quantization](../09-efficient-deep-learning/04-quantization.md), [Knowledge Distillation](../09-efficient-deep-learning/06-knowledge-distillation.md), [TinyML: Microcontrollers and TinyEngine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md), [Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md)
- Part 10: [Inference](../10-llm-internals/08-inference.md), [Evaluating Language Models](../10-llm-internals/09-evaluating-language-models.md), [Building Your Own: A Roadmap Through the Assignments](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md)
- Part 03: [A Minimal Evaluation Harness](../03-evaluation/02-a-minimal-eval-harness.md)
- Part 07: [Quality Attributes of ML Components](../07-ml-in-production/06-quality-attributes-of-ml-components.md)

## Next

→ [Capstone 5: Train a Small Language Model](06-capstone-train-a-small-language-model.md), for building the model instead of compressing it.
