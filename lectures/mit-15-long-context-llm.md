# Lecture guide: Long Context LLM

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 15 · **Length:** 1:14:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=kgTWKjbnrBA) · **Slides:** [slides](https://www.dropbox.com/scl/fi/aorbruqhmbu3cpqtnbuyo/Lec15-Long-Context-LLM.pdf?rlkey=i7d5urg0m4mm96wc82nx76lgs&st=nssefmxf&dl=0)
**Chapters that cite this lecture:** [08. Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md)

> **In one sentence:** Song Han teaches long-context language models: cheap fine-tuning with LongLoRA, how to evaluate them (lost in the middle, needle in a haystack, LongBench), and three ways to make long inference affordable, StreamingLLM with attention sinks, DuoAttention with its two kinds of heads, and Quest with query-aware sparse pages, ending with state-space models.

## Before you watch

The chapter [Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) covers most of these techniques in its sections on the KV cache and long context. The transformer lecture's rotary embedding and KV cache arithmetic are assumed.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=0) Plan

Long documents, long videos and multimodal models need long contexts, and memory is what limits them. The plan: context extension with rotary embedding, LongLoRA for training, evaluation of long-context models, three efficient attention mechanisms for inference, StreamingLLM, DuoAttention and query-aware sparsity, and, if time allows, state-space models.
**In this book:** not needed (lecture introduction and plan of the lecture).

### [2:00–3:41](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=120) Extending the context window

Rotary embedding pairs the dimensions of a vector, treats each pair as a point in the plane and rotates it by an angle proportional to the token's position; the inner product of two such vectors depends only on the difference of positions. To double the window from 2k to 4k, do not extrapolate: halve the angle, twice as many positions in the same range, and fine-tune afterwards. Fine-tuning on long contexts is expensive.
**In this book:** [Transformer Architectures and Hyperparameters › 2. Attention and position](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#2-attention-and-position).

### [3:41–9:24](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=221) LongLoRA: shifted sparse attention

Fed about 30k tokens of a Harry Potter book and asked for its message, a 4k-context Llama 2 answers poorly, and the earlier LongLlama training used 128 TPU v3 chips. LongLoRA fine-tunes 7-billion and 70-billion models to a 32k context on one node of eight A100 GPUs. Attention is the bottleneck, since its cost grows with the square of length. During training, tokens are grouped and attend only within their group; on half the heads the groups are shifted by half a group, so that neighbouring groups overlap and information passes between them, more with every layer. At inference the model uses full attention.
**In this book:** [Efficient LLM Inference and Deployment › 6. Long context: extend, then verify](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#6-long-context-extend-then-verify).

### [9:24–12:09](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=564) Enhanced LoRA, and how the shift is implemented

The second ingredient trains more than the low-rank branches: the input embeddings and the normalization layers too, while leaving the attention and output projections untouched. A student's question clarifies that the shift lets tokens, not heads, exchange information. In code the heads are split in two halves; one half keeps the groups, the other is rolled by half a group before grouping, and attention runs within each group.
**In this book:** [Efficient LLM Inference and Deployment › 6. Long context: extend, then verify](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#6-long-context-extend-then-verify).

### [12:09–14:03](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=729) How LongLoRA performs

Trained with shifted sparse attention, the model's perplexity matches full attention's, whereas plain LoRA rises steeply as context grows. Memory tells the same story: full attention runs out at 32k tokens, plain LoRA reaches 64k at a high perplexity, and LongLoRA reaches 64k with the lowest training time. Ablations favour the shifted pattern over block, dilated or streaming patterns, and perplexity is lowest when training is sparse and testing full.
**In this book:** [Efficient LLM Inference and Deployment › 6. Long context: extend, then verify](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#6-long-context-extend-then-verify).

### [14:03–16:42](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=843) Enhanced LoRA, and passkey retrieval

Normalization layers hold 0.004% of a model's parameters and embeddings 2%, so tuning them costs little. Plain LoRA trails full fine-tuning by about three points of perplexity however high its rank; adding normalization recovers one point, and normalization plus embeddings closes the gap at rank 8, where plain LoRA fails even at rank 256. On passkey retrieval, a number hidden in filler text and asked for at the end, Llama 2 7B collapses beyond its 4k context; LongLoRA holds to 32k and past 40k with the position extension.
**In this book:** [Efficient LLM Inference and Deployment › 6. Long context: extend, then verify](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#6-long-context-extend-then-verify).

### [16:42–20:58](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=1002) Evaluating long context

The lost-in-the-middle effect: models answer well when the relevant information sits at the start or the end of a context and poorly when it sits in the middle. Fluent output and good perplexity do not prove memory, so harder tests are needed. Needle in a haystack hides a statement in documents of growing length and at various depths and asks for it at the end; the plot is green at full accuracy, yellow at half and red at none. Up to 20k everything is green; from 73k the middle turns red while both ends hold; at 128k even three quarters of the way down retrieval is 65%. LongBench uses real tasks, question answering, summarization and few-shot learning, in English and Chinese, with automatic metrics. Its finding: position scaling helps long-context understanding, while context compression and retrieval help less than models designed for long context.
**In this book:** [Efficient LLM Inference and Deployment › 6. Long context: extend, then verify](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#6-long-context-extend-then-verify).

### [20:58–23:42](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=1258) The cache problem, recapped

The KV cache grows linearly: batch size times layers times heads times head size times length, for keys and values, times the bytes. A 70-billion model needs 2.5 megabytes per token; one 512-token request takes a gigabyte, and 16 requests of 4k tokens take 160 gigabytes, two A100 GPUs, sometimes more than the model itself. Three techniques follow: StreamingLLM and attention sinks, DuoAttention, and Quest.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [23:42–29:07](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=1422) StreamingLLM and attention sinks

Streaming use, an endless dialogue, needs constant memory. The original transformer keeps good perplexity until it passes its 4k training length, then collapses, and its memory grows without bound. Window attention keeps memory flat but collapses as soon as the first token leaves the window. Sliding windows with recomputation keep perplexity low at a quadratic cost. The clue is that the first token receives enormous attention in every layer: softmax forces the scores to sum to one, so tokens that need nothing dump their attention on the first token, the only one visible to all. Han's group had seen this in 2021 in SpAtten, without an explanation, in GPT-2 sentences.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [29:07–34:00](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=1747) Position, not meaning

Is the first token important for what it means or where it sits? Replacing four sink tokens with four meaningless line breaks restores perplexity just as well, so it is the position. StreamingLLM therefore keeps the keys and values of the sink tokens for ever, adds a sliding window of recent tokens, and numbers positions by their place in the cache rather than in the text. With PagedAttention this is as simple as pinning the first page. Perplexity stays flat to 4 million tokens, memory is constant, and the speed-up over recomputation grows with length.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [34:00–38:00](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=2040) How many sinks, and what StreamingLLM cannot do

Four sinks are the sweet spot; eight add little. Prompted by a question, Han shows a single learnable sink token at the start of training samples doing the same job, improving perplexity from 18.49 to 18.01. Sinks appear elsewhere: in vision transformers on background pixels and in BERT on separator tokens. But streaming is not long context: asked to recall content further back than the window, a cache of 2,048 plus four tokens fails at a distance of 2,300.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [38:00–40:52](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=2280) DuoAttention: the problem

Long videos and high-resolution images make million-token contexts ordinary: a 224 by 224 image is 256 tokens, and an hour of video at one frame per second about a million. Llama 3 8B decodes up to about 500k tokens within 80 gigabytes; a million tokens would need 137 gigabytes for the cache, and decoding time grows with length. Earlier compression methods, H2O, StreamingLLM and TOVA, damage long-context ability. DuoAttention halves memory, 78 to 49 gigabytes, halves prefill time, 4,000 to 2,000 seconds, and halves the 864 milliseconds per decoded token.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [40:52–45:20](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=2452) Two kinds of heads

Attention maps reveal two kinds of head. Retrieval heads attend to anywhere earlier in the sequence: asked for the best fruit after "the best fruit is orange", they look back at those words. Streaming heads attend only to recent tokens and the first token, the StreamingLLM pattern. Pruning retrieval heads destroys accuracy; pruning streaming heads changes nothing; random pruning lies between. DuoAttention gives retrieval heads a full cache and streaming heads a tiny constant one, the sinks and the most recent tokens.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [45:20–52:16](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=2720) Learning which heads are which

Each head gets a trainable gate α that blends its full attention with its streaming attention, which uses a mask shaped like the Greek letter lambda: recent tokens and sinks. The model is trained to match the output of full attention, with a regularizer pushing the gates down. Only the gates are trained, 32 by 32 for Llama 2 7B, a few hours on eight A100 GPUs, on passkey retrieval texts. At inference a threshold on each gate decides its kind. Decoding then keeps two caches and concatenates the heads' outputs; prefill processes the sequence in chunks, so streaming heads cost time linear in length and memory of constant size.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [52:16–55:14](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=3136) DuoAttention's results

About half the heads turn out to be streaming heads, with a negligible cache. On needle in a haystack and LongBench, DuoAttention stays as green as full attention where H2O, StreamingLLM, TOVA and FastGen fail; a quarter of the heads suffice as retrieval heads for Llama 2 and half for Llama 3, which uses grouped-query attention. Short-context benchmarks such as MBPP, MMLU and MT-Bench hold at half the cache budget. Memory falls 2 times for multi-head models and 1.6 for grouped-query ones, context grows from 500k to a million tokens, prefill latency drops 1.7 times. With 4-bit weights and cache 1.8 million tokens fit on one A100, and with QServe's 4-bit cache 3.3 million, about three hours of video.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [55:14–58:53](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=3314) Quest: sparsity that follows the query

The KV cache is naturally sparse: in SpAtten's example sentence, "video" and "game" receive heavy attention and "I" and "the" almost none. Dense attention keeps everything and costs memory. StreamingLLM and H2O are query-agnostic: once evicted, a token never returns. Quest makes the pattern depend on the token being decoded: in "A is B, C is D, … A is", the token B matters little until the last moment, then decisively, so what was pruned can come back.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache) · [Attention Alternatives and Mixture of Experts › 5. Sparse attention](../10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md#5-sparse-attention).

### [58:53–62:00](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=3533) How Quest estimates a page

Quest keeps the whole cache in memory and saves data movement instead: unimportant pages are simply not fetched. Scoring every key against the query would cost the very computation it tries to avoid, so each page keeps two summary keys, the smallest and the largest value in each channel across its tokens. The query is multiplied elementwise by both, the larger of the two products is taken per channel, and the sum is the page's importance. A token inserted into the cache updates the summaries; a query scores every page this way, and only the top pages are loaded.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [62:00–66:01](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=3720) Quest's results

On passkey retrieval Quest stays near perfect down to small token budgets where H2O and StreamingLLM manage about 1%. With a 100k context and a budget of 4k tokens accuracy is 100%, with 2k still 100%, with 1k 96% and with 256 88%. Language-modeling perplexity tracks the full cache, and a 2k budget on a 32k-context LongBench task matches the full cache. Attention latency falls 1.7 to 4 times as length grows at fixed budget; the largest overhead is estimating criticality, which can be shared across query tokens or across layers. End to end, Han reports 2.2 times at 32k length with a 2k budget, and the method works with 4-bit weights.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [66:01–1:14:00](https://www.youtube.com/watch?v=kgTWKjbnrBA&t=3961) Beyond transformers: state-space models

A state-space model replaces attention's communication between tokens with a recurrent update, like an RNN without nonlinearity: a matrix A moves the hidden state forward, B maps the input into it, C maps it to the output. With constant A, B and C the recurrence unrolls into a convolution. Mamba makes them selective, functions of the input, so that a token such as "hamburger" in "I want to order a hamburger" gets more weight; then the convolution form is lost, and training relies on a parallel scan, the trick that computes prefix sums in parallel on hardware. Hybrid models stack Mamba layers, attention layers and mixture-of-experts layers, some found by architecture search; Jamba fits 256k tokens on a single 80-gigabyte GPU. Their advantage is a fixed-size state instead of a growing cache. Han closes by recapping the lecture.
**In this book:** [Attention Alternatives and Mixture of Experts › 4. Add a state that can forget: Mamba-2 and Gated DeltaNet](../10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md#4-add-a-state-that-can-forget-mamba-2-and-gated-deltanet) · [Efficient LLM Inference and Deployment › What the practitioners say](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#what-the-practitioners-say).

## What to take away

- LongLoRA fine-tunes cheaply by training with shifted sparse attention and full attention at test time, and by also tuning the small normalization and embedding parameters.
- Judge long-context models with needle in a haystack or LongBench, not perplexity; models forget the middle.
- Attention sinks make constant-memory streaming possible; DuoAttention keeps a full cache only for retrieval heads; Quest loads only pages that matter for the current query.
- State-space models such as Mamba keep a fixed-size state, and hybrids mix them with attention.

## Sources

- Song Han, "Long Context LLM", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=kgTWKjbnrBA).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
