# Lecture guide: Transformer and LLM

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 12 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=EV6xb4xY708) · **Slides:** [slides](https://www.dropbox.com/scl/fi/4o87goykb0aoyopps02t4/Lec12-Transformers-and-LLM.pdf?rlkey=k97sdf3ls3xxz4fgvte6px279&dl=0)
**Chapters that cite this lecture:** [08. Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md)

> **In one sentence:** Song Han builds the transformer from its parts (tokens, attention, feed-forward layers, normalization, positional encoding), covers the variants that define modern open models (decoder-only blocks, rotary position, grouped-query attention, SwiGLU), sizes the KV cache, and ends with scaling, emergent abilities and the Llama family.

## Before you watch

The chapter [Transformer Architectures and Hyperparameters](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md) covers the same architecture from Stanford's course, and [Efficient LLM Inference and Deployment](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) uses this lecture for the KV cache. Little beyond matrix multiplication and the softmax is assumed.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=0) What language models now do

A new chapter which, he says, is the course's most exciting, with much that is modern. Han prompted ChatGPT, launched in late 2022, to write a syllabus for this course, and it did; Google Translate, GitHub Copilot and GPT-4V, which solves a geometry problem from a figure, follow. In one example a rider asks how to lower a bike seat, sends photos, and the model explains the quick-release lever, then identifies the bolt on his own bike and picks the right tool by reading the manual and the toolbox together. Serving and training such models is expensive, and long conversations, or video with hundreds of tokens per frame, make the KV cache grow linearly. This lecture explains the workload before the next one accelerates it.
**In this book:** [Efficient LLM Inference and Deployment › What the practitioners say](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#what-the-practitioners-say).

### [4:00–12:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=240) Before transformers

Language tasks divide into discriminative ones, which classify a given sentence (sentiment, entailment), and generative ones, which produce new tokens (modelling, translation, summarization). Recurrent networks kept a fixed working memory, constant in size but poor at long dependencies, and their step-by-step dependence limited parallel training. Convolutions over a window of three tokens see little context unless stacked. Bidirectional recurrent networks served as encoders, unidirectional ones as decoders. The deep problem: language has no locality, since an early word may relate to a much later one, and relating two distant tokens took as many steps as the distance between them.
**In this book:** [Transformer Architectures and Hyperparameters › How it works, step by step › 2. Attention and position](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#2-attention-and-position).

### [12:00–16:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=720) Tokens and embeddings

The transformer block has these parts: tokenizer, embedding, attention, feed-forward layer, layer norm, residual connection, positional encoding and a final linear head. A token is a piece of a word: a 110-word paragraph becomes 162 tokens. One-hot encoding over a vocabulary of 100,000 stores mostly zeros; an embedding gives each token a dense vector, learned end to end for the task, after early methods such as Word2Vec and GloVe.
**In this book:** [The Language Modeling Pipeline and Tokenization › The core idea](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#the-core-idea).

### [16:00–20:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=960) Attention as retrieval

Attention lets every token interact with every other, through an n by n matrix. The input is projected to query, key and value; query times the transpose of key gives the scores; a mask, possibly causal, and a softmax make each row sum to one; the result weights a sum of the values. Han's analogy is a video search: the query is the typed text, the key the title and description, the value the video. Scores are divided by a scale tied to the hidden size, 4k in a 7-billion-parameter model, and the cost grows with n squared. In a translation example the map is mostly diagonal, reversed where word order differs; the correspondences are learned, not rule-based.
**In this book:** [Transformer Architectures and Hyperparameters › 2. Attention and position](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#2-attention-and-position) · [Neural Network Basics for Efficiency › 3. Attention, in one paragraph](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#3-attention-in-one-paragraph).

### [20:00–24:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=1200) Several heads, two masks

One head models one kind of relation; several heads, each with its own projections, capture different semantics, some nearly diagonal, some vertical, and their outputs are concatenated and projected. A global mask lets every token see every token. A causal mask is a lower triangle: a token sees itself and everything before it, never the future.
**In this book:** [Transformer Architectures and Hyperparameters › 2. Attention and position](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#2-attention-and-position).

### [24:00–26:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=1440) The feed-forward layer

Attention mixes tokens but adds no elementwise nonlinearity, so a feed-forward layer models each token on its own: two matrix multiplications, from d to 4d and back to d, with ReLU or GELU between, an inverted bottleneck that adds capacity. The 7-billion-parameter model has a hidden size of about 4k and 32 heads; a 175-billion one about 12k.
**In this book:** [Transformer Architectures and Hyperparameters › 3. The MLP and gating](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#3-the-mlp-and-gating).

### [26:00–30:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=1560) Layer normalization, before or after

Layer norm normalizes across the feature dimension rather than the batch, with a learned scale and bias. Han urges attention to these two parameters: few in number, they can absorb scaling operations, as in SmoothQuant or rotations, since multiplication is linear. Post-norm places the norm after the attention; pre-norm before it, outside the residual branch. Pre-norm is now the more popular choice, for training stability and because it folds into the prologue of a matrix multiplication in one kernel.
**In this book:** [Transformer Architectures and Hyperparameters › 1. Normalization](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#1-normalization).

### [30:00–32:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=1800) Residuals and absolute positions

Residual connections carry each sub-block's input forward. Convolution is translation invariant, but in language position matters, and neither attention nor the feed-forward layer knows the order of tokens. Absolute positional encoding adds to each embedding a pattern that depends only on its position: sinusoids whose frequency varies with the dimension, fast in some dimensions and almost flat in others, so every position and dimension has a unique value.
**In this book:** [Transformer Architectures and Hyperparameters › 2. Attention and position](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#2-attention-and-position).

### [32:00–34:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=1920) The whole block, and its cost

Assembled, the block reads tokens, embeds them with position information, mixes them with multi-head attention, models each with the feed-forward layer, and ends with a linear head. On translation it reached a higher BLEU score than earlier models at two to three orders of magnitude less training cost.
**In this book:** [Transformer Architectures and Hyperparameters › The core idea](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#the-core-idea).

### [34:00–38:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=2040) Encoder-decoder and encoder-only models

After a break, design variants. The original transformer was an encoder-decoder: the encoder reads the source sentence and the decoder generates the answer token by token, as in translation, semantic similarity and summarization. BERT is encoder-only, with two pre-training objectives: masked language modelling, hiding about 15% of the tokens and predicting them with access to both neighbours, and next-sentence prediction, now rarely used. Its mask is full, and the pre-trained model is fine-tuned for each downstream task.
**In this book:** [Transformer Architectures and Hyperparameters › How it works, step by step › 5. Three families: encoder-decoder, encoder-only, decoder-only](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#5-three-families-encoder-decoder-encoder-only-decoder-only).

### [38:00–40:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=2280) Decoder-only models

GPT, a generative pre-trained transformer, is decoder-only: trained to predict the next word, with a causal mask because a token may attend only to what precedes it. Such models can be fine-tuned for tasks or, when large enough, solve tasks from a description or a few examples without fine-tuning.
**In this book:** [Prompting and In-Context Learning › The core idea](../01-foundations/05-prompting-and-in-context-learning.md#the-core-idea) · [Transformer Architectures and Hyperparameters › The core idea](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#the-core-idea).

### [40:00–44:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=2400) Relative positions, and ALiBi

Absolute encoding changes the input embeddings, so position flows through the whole network. Relative encoding changes only the attention scores, by a bias or by modifying queries and keys, because the scores depend only on those. Its advantage is extrapolation: a model trained on short sequences can be tested on a whole book or film. Attention with linear biases, ALiBi, adds to each score a term that depends on the distance between the query's and the key's positions, multiplied by a strength that is set by hand.
**In this book:** [Transformer Architectures and Hyperparameters › 2. Attention and position](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#2-attention-and-position).

### [44:00–50:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=2640) Rotary position embedding

Rotary position embedding, harder but widely used, as in Llama. The embedding is split into two halves that form pairs of coordinates, and each pair is rotated in the plane by an angle proportional to the token's position. The base of 10,000 makes the rotations small per dimension index; a full turn would make distant tokens indistinguishable. When a rotated query is multiplied by a rotated key, the result depends only on the difference of their positions, which is why the encoding is relative. Asked for the intuition, Han answers that the same word at position 1 and at position 10 is rotated by different angles.
**In this book:** [Transformer Architectures and Hyperparameters › 2. Attention and position](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#2-attention-and-position).

### [50:00–54:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=3000) Stretching the context window

Rotary embedding extends the context window by interpolation. To double the window, halve the angle: rotate by mθ over 2. Positions that would fall beyond the range seen in training are compressed into it, with more points interpolated in between. Context lengths have grown from 2k in the first Llama to 4k in Llama 2.
**In this book:** [Transformer Architectures and Hyperparameters › 4. The hyperparameters that matter](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#4-the-hyperparameters-that-matter).

### [54:00–58:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=3240) The KV cache, and its size

To attend to earlier tokens, their keys and values are needed; recomputing them for every new token wastes work, so they are cached, and only the new token's key and value are computed. The cache grows with the sequence. Its size per token is 2, for key and value, times the bytes, times layers, heads and head dimension, times the batch. For Llama 2's 7-billion model that is half a megabyte; for 13 billion, 40 layers and 40 heads, 0.8 megabytes; for 70 billion, 80 layers and 64 heads, 2.5 megabytes.
**In this book:** [Inference › 1. Count one decoding step](../10-llm-internals/08-inference.md#1-count-one-decoding-step) · [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [58:00–1:00:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=3480) How large the cache becomes

For the 70-billion model, 512 tokens take over a gigabyte of cache, 4,000 tokens, about a paper, 10 gigabytes. Sixteen users reading a paper each need 160 gigabytes: two 80-gigabyte GPUs just for the cache. Unlike the model, which stays fixed, the cache grows with batch and length and can exceed the model's own size.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache).

### [1:00:00–1:04:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=3600) Multi-query and grouped-query attention

The remedy shares keys and values. Multi-query attention keeps many query heads but one key and one value head, shrinking the cache most but losing much capacity. Grouped-query attention, GQA, lets a group of query heads, typically eight, share one key and value head. Han likens the three to standard, depthwise and grouped convolution: a trade of capacity against cost. With grouped-query attention the 70-billion model's cache fell from 328 gigabytes to under 80, fitting a single H100 node; at large model sizes its accuracy matches full multi-head attention, he says, whereas multi-query sometimes loses a little.
**In this book:** [Efficient LLM Inference and Deployment › 3. Shrink the KV cache](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#3-shrink-the-kv-cache) · [Inference › 3. Shrink the KV cache](../10-llm-internals/08-inference.md#3-shrink-the-kv-cache).

### [1:04:00–1:06:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=3840) SwiGLU

The last change replaces the feed-forward layer with a gated linear unit. SwiGLU has three matrix multiplications of size 8d over 3, which together match the old 4d twice over, an elementwise gate between two of their results, and the Swish activation. The first two multiplications can be fused into one kernel, and the results are good.
**In this book:** [Transformer Architectures and Hyperparameters › 3. The MLP and gating](../10-llm-internals/03-transformer-architectures-and-hyperparameters.md#3-the-mlp-and-gating).

### [1:06:00–1:10:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=3960) Scale, emergent abilities, and in-context learning

Models keep growing because scale unlocks abilities. On modified arithmetic, where every result is one more than usual, or on unscrambling words, accuracy stays near zero until training compute passes a threshold, then jumps. GPT-3 scaled up GPT-2 and became a few-shot learner. Fine-tuning needs gradient updates for each task; zero-shot learning gives only a description of the task, few-shot learning a few examples, with no updates. For the 175-billion model accuracy rises with the number of examples in the context; small models gain nothing from more examples.
**In this book:** [Scaling Laws › The core idea](../10-llm-internals/07-scaling-laws.md#the-core-idea) · [Prompting and In-Context Learning › The core idea](../01-foundations/05-prompting-and-in-context-learning.md#the-core-idea).

### [1:10:00–1:18:00](https://www.youtube.com/watch?v=EV6xb4xY708&t=4200) Open models, from OPT to Llama 3

Open models caught up from 2022. Meta's OPT came in sizes from 125 million to 175 billion with ReLU, pre-norm and a decoder-only design. Llama added SwiGLU and rotary embedding; its 7-billion model has 32 layers, a 2k context, a 4k hidden size and 32 heads. Llama 2 extended the context to 4k, doubled the training tokens to 2 trillion, added grouped-query attention and a chat version aligned by supervised fine-tuning. Llama 3 trained on 15 trillion tokens, from 1.8 trillion, with 50 times the FLOPs; its flagship has 405 billion parameters, an 8k context and a long-context variant, and it was tuned by supervised fine-tuning, rejection sampling and direct preference optimization. Mistral 7B beat Llama 2's 34-billion model with sliding-window attention, later dropped. The Chinchilla rule says data must grow with parameters; Llama models train on far more tokens than that, spending more on training so that inference costs less and a model of the same size is more accurate.
**In this book:** [Attention Alternatives and Mixture of Experts › 2. Mix local and global layers](../10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md#2-mix-local-and-global-layers) · [Scaling Laws › 2. Pick a method for the trade-off](../10-llm-internals/07-scaling-laws.md#2-pick-a-method-for-the-trade-off) · [Efficient LLM Inference and Deployment › What the practitioners say](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#what-the-practitioners-say).

## What to take away

- A transformer block is attention, which relates tokens, a feed-forward layer, which models each token, normalization and residuals, plus positional information.
- Relative positional information, as in rotary embedding, touches only the attention scores and extrapolates to longer contexts by interpolation.
- The KV cache grows with sequence length and batch and can cost more memory than the model; grouped-query attention cuts it several times at almost no loss.
- Scale unlocks abilities such as in-context learning, and the open Llama line packages all of these choices.

## Sources

- Song Han, "Transformer and LLM", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=EV6xb4xY708).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
