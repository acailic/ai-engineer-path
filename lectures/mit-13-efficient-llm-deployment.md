# Lecture guide: Efficient LLM Deployment

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 13 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=sTz2tXG1T0c) · **Slides:** [slides](https://www.dropbox.com/scl/fi/aa5ea0hrc68cn3fh18nan/Lec13-LLM-Deployment.pdf?rlkey=gzq9yiddx4bnh14bxomtfmcoj&dl=0)
**Chapters that cite this lecture:** [08. Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md)

> **In one sentence:** Song Han shows how to deploy language models cheaply: SmoothQuant and AWQ, the quantization methods of his group, QServe, which combines them, three kinds of sparsity, and the serving techniques of modern inference libraries, paged attention, FlashAttention, speculative decoding and continuous batching.

## Before you watch

The chapter [Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) follows this lecture almost section by section, and [Quantization](../09-efficient-deep-learning/04-quantization.md) explains SmoothQuant. The two quantization lectures and the transformer lecture's KV cache arithmetic are assumed.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=0) Plan

The agenda in three parts: quantization, from 8-bit weights and activations to weight-only quantization to QServe, which quantizes both; sparsity of weights, contextual sparsity and attention sparsity; and system support, with paged attention, FlashAttention, speculative decoding and batching. Inference is getting very important, he says, and the scaling of inference time is crucial, so efficiency matters, and AWQ and a laptop deployment are the subjects of Labs 4 and 5.
**In this book:** [Efficient LLM Inference and Deployment › How it works: count first](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#how-it-works-count-first).

### [2:00–4:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=120) Why old quantization fails on language models

Techniques that work on convolutional networks lose accuracy on large language models: in a plot that runs from 1.3 to 175 billion parameters, only the small models hold up. The cause is outliers: a few activation channels, three of 5,000 in Han's plot, hold very large values for every token. Quantizing the tensor to the outliers' range clamps all the other values to zero. Weights, by contrast, are flat and easy to quantize; activations are the problem.
**In this book:** [Quantization › Outliers in language models: the SmoothQuant idea](../09-efficient-deep-learning/04-quantization.md#outliers-in-language-models-the-smoothquant-idea) · [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [4:00–10:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=240) SmoothQuant: moving the difficulty

Matrix multiplication is linear, so difficulty can move between activations and weights: scale an activation channel by 0.1 and its weight channel by 10 and the product is unchanged. SmoothQuant equalizes the two with one scale per channel. On a toy example, the largest absolute activation per column and the largest weight per row give a scale equal to the square root of their ratio: 16 over 1 gives 4, 9 over 1 gives 3. Activations are divided by the scale, weights multiplied, so 16 times 1 becomes 4 times 4 and the outlier of 16 becomes 4. The scaling is absorbed by the preceding layer when the model is compiled; at run time two integer matrices multiply with no overhead.
**In this book:** [Quantization › Outliers in language models: the SmoothQuant idea](../09-efficient-deep-learning/04-quantization.md#outliers-in-language-models-the-smoothquant-idea).

### [10:00–16:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=600) The migration strength, and what it saves

How far to push is a knob: activations to the power α and weights to the power 1 − α, where pushing everything to either side hurts accuracy and the middle, α = 0.5, the square root, is the sweet spot. Integrated into FasterTransformer, the compute-heavy multiplications run in INT8 while layer norms, softmax and residual paths stay in FP16. A 175-billion-parameter model then needs 4 GPUs instead of 8 and runs faster for the saved communication; a 530-billion model fits on 8 GPUs instead of 16, a single node. The method also holds accuracy on Llama.
**In this book:** [Quantization › Outliers in language models: the SmoothQuant idea](../09-efficient-deep-learning/04-quantization.md#outliers-in-language-models-the-smoothquant-idea) · [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [16:00–20:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=960) AWQ: the case for 4-bit weights

AWQ, activation-aware weight-only quantization, targets a single user on a device. At batch size one matrix multiplication becomes matrix-vector, the same weights are fetched for far less reuse, and compute intensity falls; the generation stage dominates and is bound by memory bandwidth. On the roofline a 4-bit weight with 16-bit arithmetic beats FP16 and INT8 at low batch, though it peaks at the same throughput. Weight memory dwarfs activation memory, over a thousand times in the feed-forward layers, so only the weights are quantized, to 4 bits.
**In this book:** [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations) · [Inference › 1. Count one decoding step](../10-llm-internals/08-inference.md#1-count-one-decoding-step).

### [20:00–24:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=1200) A few salient channels

Rounding weights to 3 bits wrecks perplexity, a measure of how well a model predicts text, lower being better. Keeping just 1% of the channels in FP16 greatly improves it. Which 1%? Not the largest weights: selection by activation magnitude does far better, because a weight error is amplified by the activation it multiplies, and outlier channels amplify it most. Keeping a few channels in another precision would force mixed precision on the whole tensor, which complicates the engine.
**In this book:** [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [24:00–28:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=1440) Protect a channel by scaling it

The salient channels can be protected without mixed precision, by the idea of SmoothQuant: multiply them by a scale and divide the activations by it. Perplexity fell from 43 to about 14 with a scale of 2; a scale of 4 was slightly worse. Scaling one channel by 2 effectively gives it one more bit, since 0.5 and 1, which both round to 1, become 1 and 2. The error analysis agrees: the rounding error scales as one over the scale, while the quantization step, set by the largest value, stays fixed unless the scale grows so large that it moves that maximum.
**In this book:** [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations) · [Quantization › Outliers in language models: the SmoothQuant idea](../09-efficient-deep-learning/04-quantization.md#outliers-in-language-models-the-smoothquant-idea).

### [28:00–34:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=1680) The AWQ recipe, and how it generalizes

The scale for each channel is its average activation magnitude raised to a power α between 0 and 1, searched to keep the scaled product close to the original. The reciprocal folds into the preceding layer norm; the weight scaling is done offline; neither costs run time. No backpropagation is needed, only a calibration set, 64 sequences suffice, and it generalizes: calibrated on one corpus it loses little on PubMed or Enron emails, where a regression-based method loses two to four points of perplexity. It holds up across Llama and Llama 2 from 7 to 70 billion parameters and for vision-language models, as in a live VILA demo describing a soccer video from a single GPU.
**In this book:** [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [34:00–38:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=2040) TinyChat: running 4-bit weights

TinyChat is Han's inference engine: low-level code under a Python interface, for CPUs and GPUs from cloud to edge. Computers address bytes, so two 4-bit weights share a byte; TinyChat stores them interleaved, so that a mask with 0x0F and a shift by four unpack a vector of weights in two operations, about 20% faster on ARM NEON. It also fuses whole operations into single kernels, the attention from query-key product through softmax to the value multiplication, and the matrix multiplications, since each kernel launch is costly.
**In this book:** nothing beyond this guide; nearest: [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [38:00–44:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=2280) What AWQ delivers

On desktop, laptop and mobile GPUs, 4-bit AWQ models run about three times faster than FP16, and some that overflowed a laptop's 8 gigabytes now fit. A 3D-printed computer built around a Jetson Orin Nano with about 7 gigabytes runs Llama 2 7B at 3.5 gigabytes of weights, with privacy and no internet; a vision-language model on a MacBook's M1 chip, on the CPU alone, answers questions about a painting, and one laptop demo shows 25 milliseconds per token. By the time of the lecture AWQ had passed six million downloads and was used by NVIDIA's TensorRT-LLM, among others.
**In this book:** [Efficient LLM Inference and Deployment › What the practitioners say](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#what-the-practitioners-say).

### [44:00–48:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=2640) Combining the two: QServe

After a break: the two methods serve different regimes. SmoothQuant gives W8A8, 8-bit weights, activations and cache, which suits cloud serving at large batch and lifts the roofline. AWQ gives W4A16, which wins at low batch and halves the memory. QServe aims at the best of both, W4A8 with a 4-bit cache, good at small and large batch. Earlier 4-bit attempts ran at half the throughput of TensorRT's W8A8 and lost accuracy, for lack of a good engine.
**In this book:** [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [48:00–52:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=2880) Where dequantization belongs

Han dissects quantized matrix multiplication on a GPU. TensorRT's INT8 kernel keeps the main loop in the tensor core and scales in the epilogue, on CUDA cores, which is efficient. A W4A4 kernel that rescales partial sums in FP16 inside the loop is slow: partial sums take more registers than inputs. AWQ converts 4-bit weights to FP16 inputs once and multiplies in FP16. QServe converts 4-bit weights to 8-bit integers and multiplies in INT8, scaling in the epilogue. The lesson: dequantize outside the main loop and never dequantize partial sums.
**In this book:** nothing beyond this guide; nearest: [Efficient LLM Inference and Deployment › 1. Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [52:00–56:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=3120) A 4-bit cache, and the order of operations

The KV cache is hard to bring to 4 bits: values are smooth, but keys after rotary embedding have outlier channels. Smooth attention applies the same trick as SmoothQuant between queries and keys, pushing all difficulty into the queries, which are few and stay in FP16. A second detail: converting 4-bit integers to signed 8-bit by subtracting the zero point first lets the carry overflow into the next value, so multiply by the scale first and subtract after. QServe reaches low perplexity at W4A8 with a 4-bit cache and higher throughput on A100 and L40S GPUs.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [56:00–1:00:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=3360) Pruning weights and activations

Sparsity follows. Wanda prunes weights by weight magnitude times activation magnitude rather than by weight alone, and beats magnitude pruning. Pruning activations statically hurts; contextual sparsity instead finds a small, input-dependent set of useless attention heads and feed-forward dimensions, predicted from the previous layer, and keeps accuracy at high reduction while DejaVu turns it into speed-up. Mixture of experts is contextual sparsity too: a router sends each token to a few experts. An expert's capacity, tokens per batch divided by experts and multiplied by a capacity factor such as 1.5, bounds how many tokens it takes.
**In this book:** [Efficient LLM Inference and Deployment › What the practitioners say](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#what-the-practitioners-say) · [Attention Alternatives and Mixture of Experts › 6. Mixture of experts](../10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md#6-mixture-of-experts).

### [1:00:00–1:02:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=3600) Routing, and sparse attention

Routing can be decided per token, each picking its experts, or per expert, each picking its tokens. In attention, SpAtten prunes tokens and heads: a sentence of 11 tokens shrinks to 2, "film perfect", and still reads as positive. A token's importance is its cumulative attention score; tokens such as "I" and the final period receive little and go. H2O applies the same measure, made causal, to prune the KV cache.
**In this book:** [Efficient LLM Inference and Deployment › 2. Attention without the N × N matrix](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#2-attention-without-the-n--n-matrix) · [Attention Alternatives and Mixture of Experts › 5. Sparse attention](../10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md#5-sparse-attention).

### [1:02:00–1:04:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=3720) Serving metrics

Time to first token is the wait before a response begins, decisive for interaction. Time per output token sets the pace of generation; 100 milliseconds per token gives 10 tokens per second, roughly the threshold below which a model feels slow. Total latency is the first plus the second times the number of tokens. Throughput counts tokens per second over all requests. The system aims to shorten the first, quicken the second and raise throughput, and the last trades against the second. Output length, input length and model size predict cost, though size is not proportional: a 70-billion model has about twice the latency of a 13-billion one.
**In this book:** [Efficient LLM Inference and Deployment › 7. Metrics and serving choices](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#7-metrics-and-serving-choices).

### [1:04:00–1:08:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=3840) PagedAttention

Caches are allocated for sequences of unknown length, which wastes memory three ways: reserved space never used, reservation for tokens not yet generated, and gaps between requests of different sizes. Operating systems solved such fragmentation with paging, and PagedAttention does the same: the cache lives in fixed-size blocks, and a block table maps each request's logical blocks to physical ones, so that new blocks are added as tokens appear. Requests interleave in memory without fragmentation, and requests that share a prompt share its blocks by pointing at the same physical block.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [1:08:00–1:10:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=4080) FlashAttention

The n by n attention matrix need never be stored. FlashAttention tiles the computation, as in the parallel-processing lecture, multiplying query by key and immediately by value for each tile, and fuses the two multiplications into one kernel. Against PyTorch it is far faster, with or without the causal mask, and FlashAttention-2 faster still.
**In this book:** [Efficient LLM Inference and Deployment › 2. Attention without the N × N matrix](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#2-attention-without-the-n--n-matrix).

### [1:10:00–1:12:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=4200) Speculative decoding

At small batch, generating a token is bound by memory bandwidth, so verifying several tokens costs about as much as one. A small draft model generates K tokens one after another; the large model checks all K in one batched pass; wrong tokens are regenerated from the first rejection. Accepted, rejected and corrected tokens make up the trace, and the result is 2 to 3 times faster with outputs identical to the large model's.
**In this book:** [Efficient LLM Inference and Deployment › 4. Speculative decoding: several tokens per step](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#4-speculative-decoding-several-tokens-per-step).

### [1:12:00–1:18:00](https://www.youtube.com/watch?v=sTz2tXG1T0c&t=4320) Batching, and where it all lives

Running several requests together fills the GPU. Static batching waits for a full batch, fine for overnight jobs, slow for live ones. Dynamic batching runs when the batch is full or a timer expires, like a bus that leaves full or on schedule, and suits work of uniform length. Continuous batching, also called in-flight, works at the granularity of a single token: as soon as one request ends, its place is given to a new one, as passengers getting off free seats. TensorRT-LLM bundles these techniques with those of the last lecture; tensor and pipeline parallelism come in a later lecture.
**In this book:** [Efficient LLM Inference and Deployment › 5. Batch the requests](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#5-batch-the-requests) · [Inference › 2. Batch requests, up to a point](../10-llm-internals/08-inference.md#2-batch-requests-up-to-a-point).

## What to take away

- Activation outliers break naive quantization of language models; per-channel scaling that moves difficulty between activations and weights is the idea behind both SmoothQuant and AWQ.
- For a single user, weights bound speed: 4-bit weights with 16-bit arithmetic triple the speed; for many users, quantize everything to 8 bits and keep dequantization out of the inner loop.
- Sparsity in weights, activations, attention and the cache can be guided by activations and attention scores.
- Serving speed rests on paged caches, fused attention kernels, speculative decoding and continuous batching.

## Sources

- Song Han, "Efficient LLM Deployment", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=sTz2tXG1T0c).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
