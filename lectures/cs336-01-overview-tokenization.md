# Lecture guide: Overview, tokenization

**Lecturer:** course staff · **Course:** Stanford CS336 Language Modeling from Scratch, Spring 2026, lecture 1 · **Length:** 1:20:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=JuoVZkPBiKk)
**Chapters that cite this lecture:** [01. The Language Modeling Pipeline and Tokenization](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) · [07. Scaling Laws](../10-llm-internals/07-scaling-laws.md) · [08. Inference](../10-llm-internals/08-inference.md) · [12. Alignment and Multimodality](../10-llm-internals/12-alignment-and-multimodality.md) · [13. Building Your Own: A Roadmap Through the Assignments](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md)

> **In one sentence:** Percy Liang opens CS336 with why building language models from scratch still matters and what the course teaches, tours its five units from basics and systems through scaling laws, data and alignment, and then builds byte-pair encoding, the tokenizer that turns text into tokens.

## Before you watch

Percy Liang gives most of this lecture, with Tatsu Hashimoto and the course assistants introducing themselves. The chapter [Building Your Own: A Roadmap Through the Assignments](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md) follows the course tour, and [The Language Modeling Pipeline and Tokenization](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) follows the last fifteen minutes. Nothing is assumed beyond knowing what a language model is.

## The lecture, part by part

### [0:00–2:22](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=0) Introductions

The third edition of CS336. Percy Liang has worked on language models for twenty years, most of them small ones; Tatsu Hashimoto covers architectures and scaling; the assistants Marcel, Herman and Steven introduce their research, and Herman notes that a year earlier tokens were things collected in video games.
**In this book:** not needed (course introduction).

### [2:22–3:24](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=142) What stays and what changes

The from-scratch philosophy is unchanged: building from the ground up is how one learns how everything works, though a quarter only allows the highest-value parts. Two years of refinement chose those parts. Last year's lectures are on YouTube, so the staff assume part of the audience has seen them, and a year alone changes a great deal: Hashimoto rewrites his architecture lectures each time. New this year: more on mixture of experts, and long context, because agents are now popular.
**In this book:** nothing beyond this guide; nearest: [The Language Modeling Pipeline and Tokenization › How CS336 frames the whole pipeline](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#how-cs336-frames-the-whole-pipeline).

### [3:24–7:10](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=204) Why build from scratch

Researchers have drifted from the technology: ten years ago all of them trained their own models, eight years ago they fine-tuned ones such as BERT, and today prompting suffices. Prompting is fine, but abstractions leak, and fundamental research needs the whole stack torn open, which understanding through building provides. One problem: language models have been industrialized. GPT-4 reportedly cost 100 million dollars three years ago, and costs now approach a billion, while labs publish no details. The small models the class can build are not always representative: the share of computation in feed-forward layers is about 44% at small scale and 80% at 175 billion parameters, and behaviours emerge only past a critical scale.
**In this book:** [The Language Modeling Pipeline and Tokenization › What the practitioners say](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#what-the-practitioners-say).

### [7:10–11:37](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=430) What transfers, and the bitter lesson

Three kinds of knowledge are at stake. Mechanics, what a transformer or model parallelism is, and mindset, squeezing the most from hardware, taking scaling seriously and benchmarking everything, both transfer to larger scale. Intuitions about which modelling and data choices work may not; some, like the activation in Shazeer's SwiGLU paper, come only from experiment, as its author admits in a closing line about divine benevolence. A common misreading of the bitter lesson is that scale is all that matters; the right one is that algorithms that scale matter, since accuracy is efficiency times resources, and efficiency matters more at scale. An OpenAI paper measured a 44-fold algorithmic gain on ImageNet between 2012 and 2019. The course's framing: the best model for a given data and compute budget.
**In this book:** [The Language Modeling Pipeline and Tokenization › What the practitioners say](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#what-the-practitioners-say).

### [11:37–19:27](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=697) A short history, and why open models matter

Shannon used language models in the 1950s to measure the entropy of English, and n-gram models long served translation and speech. The neural lineage runs through LSTMs, Bengio's 2003 neural language model, sequence-to-sequence models, Adam, attention and the transformer, then mixture of experts and model parallelism. ELMo and BERT were fine-tuned; OpenAI embraced scaling from GPT through GPT-3, with emergent in-context learning; Google's answer was under-trained, and DeepMind's compute-optimal laws were a wake-up call. Early open efforts, EleutherAI, Meta's first attempt and BigScience, produced weak models; in three years Llama, Mistral and Chinese models such as DeepSeek and Qwen brought open weights close to closed ones, and AI2, NVIDIA and the Marin project publish paper, code and data too, without which the course could not exist. The idea of a language model moved from fine-tuning to prompting to conversation to agents, while the fundamentals, GPUs, stochastic gradients and transformers, held; only context lengths grew.
**In this book:** nothing beyond this guide; nearest: [The Language Modeling Pipeline and Tokenization › How CS336 frames the whole pipeline](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#how-cs336-frames-the-whole-pipeline).

### [19:27–27:24](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=1167) The course itself

Lectures are executable: a Python program rendered for the screen and stepped through. Five units carry five intense assignments. Take the course to understand how; not to do research that quarter, to learn the newest techniques, multimodality and agents are skipped, or to get results on an application, where prompting and fine-tuning come first. Assignments give no scaffolding code but unit tests, run on a laptop and then on a cluster, with leaderboards. Because coding agents can now solve the assignments, students who use AI must use a supplied prompt that makes the agent a tutor rather than a solver. Compute comes as credits on the Modal platform.
**In this book:** [Building Your Own: A Roadmap Through the Assignments › The core idea](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md#the-core-idea) · [Building Your Own: A Roadmap Through the Assignments › The five assignments](../10-llm-internals/13-building-your-own-a-roadmap-through-the-assignments.md#the-five-assignments).

### [27:24–35:53](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=1644) Unit one: basics

Tokenizer, architecture, training. A tokenizer defines the atoms the model works on; byte-pair encoding compresses frequent chunks and allows adaptive computation, though Liang hopes yearly that byte-level models, such as recent HNet work, will make tokenizers obsolete; frontier models still use them. Architectures have been refined in activations, positional encodings, normalization, cheaper attention, state-space models such as Mamba and Gated DeltaNet, usually in hybrids, and mixture-of-experts feed-forward layers; the model's shape matters greatly. Training involves the loss, where predicting several tokens helps, optimizers, Adam yielding to Muon in models such as Kimi K2, initialization, learning-rate schedules, regularization and batch size, each decisive between a run that diverges and one that reaches the state of the art. Assignment 1 builds all of it, with resource accounting and training on TinyStories and OpenWebText. The theme: balance expressiveness, stability and efficiency.
**In this book:** [The Language Modeling Pipeline and Tokenization › The core idea](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#the-core-idea).

### [35:53–45:11](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=2153) Unit two: systems

Resource accounting starts the unit: training on D tokens a model of N parameters takes about 6ND floating-point operations, and memory is not where compute is, so moving data is often the bottleneck; a B200 offers 2.25 petaflops per second in BF16 and 8 terabytes per second of memory, and roofline analysis tells whether compute or memory limits an operation. A DGX box holds eight GPUs on NVLink, thousands more over InfiniBand or Ethernet. Custom kernels minimize data movement, by operator fusion and tiling. With many GPUs, collectives such as all-reduce and the sharding of parameters, activations, gradients and optimizer states by data, layers, sequences or experts are the subject. Inference has a prefill phase like training and a memory-bound decode phase; pruning, quantization, distillation, speculative decoding, inference kernels and the batching of arriving queries all speed it up. Assignment 2 writes Triton kernels and parallel training; Liang recommends the book How to Scale Your Model.
**In this book:** [Inference › 7. Run a server, not a loop](../10-llm-internals/08-inference.md#7-run-a-server-not-a-loop).

### [45:11–53:42](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=2711) Unit three: scaling laws

Given 10 to the 25th floating-point operations, tens of millions of dollars, which model should one train, with only one chance? The conceptual shift is from a single model to a scaling recipe, a mapping from a compute budget to hyperparameters. Run smaller experiments, fit a law, predict the loss at the target scale, and optimize the recipe there. Scaling laws are willed into existence: hyperparameters must transfer across scale, so predictability matters as much as optimality. The classic compute-optimal laws of Kaplan and colleagues sweep model sizes per budget; a rule of thumb is 20 tokens per parameter, 1.4 trillion for a 70-billion model, though many models are trained on more to be cheaper at inference. Marin pre-registers its laws, the latest out to 10 to the 22nd operations. Assignment 3 exposes a training interface that returns a loss for a configuration, from a cache of runs, and grades a model landed on a budget.
**In this book:** [Scaling Laws › 6. Predict, then run](../10-llm-internals/07-scaling-laws.md#6-predict-then-run) · [Scaling Laws › The core idea](../10-llm-internals/07-scaling-laws.md#the-core-idea).

### [53:42–1:00:22](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3222) Unit four: data

Data quality decides how good a model is, and data reflects what the model should do. Evaluation comes first and splits in two: internal metrics need smoothness across scales and meaningful relative differences, and perplexity still captures intrinsic quality well; external metrics need ecological validity. Many diverse evaluations beat one average, and data absent from the internet avoids contamination. Data must be actively curated, web pages, books, papers, code, as in the Pile of 2021, amid legal disputes over copyrighted and unlicensed material. Processing turns HTML, PDFs and repositories into text, filters, deduplicates and mixes sources, and increasingly generates synthetic data; data serves pre-training, mid-training with high-quality and long-context data, and post-training. Assignment 4 starts from a raw web crawl.
**In this book:** nothing beyond this guide; nearest: [Training Data › The core idea](../10-llm-internals/10-training-data.md#the-core-idea).

### [1:00:22–1:05:06](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3622) Unit five: alignment, and the efficiency lens

After full supervision comes weak supervision, because criticizing is easier than generating: sample responses, score them with a human, a verifier or a model judge, and update the model to prefer better ones, by PPO, GRPO or, for preference data, DPO. Reinforcement learning is unstable and hard to tune, Liang says, and at scale brings systems problems of juggling on-policy data with throughput. Everything in the course is efficiency: tokenization is compute efficiency, architecture changes serve memory and inference speed, data filtering avoids wasting compute on bad data, and scaling laws are hyperparameter tuning on small models.
**In this book:** [Alignment and Multimodality › Part one: what CS336 means by alignment](../10-llm-internals/12-alignment-and-multimodality.md#part-one-what-cs336-means-by-alignment).

### [1:05:06–1:10:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3906) What a tokenizer must do

Text is a Unicode string; a language model puts a distribution over sequences of token indices. A tokenizer encodes strings to indices and decodes them back, and must round-trip. Observations: a word with and without its leading space are unrelated tokens, and numbers split into digit groups in some tokenizers. A string of 20 bytes becomes 8 tokens with the GPT-5 tokenizer, a compression ratio of 2.5 bytes per token; higher is better, since attention is quadratic in the sequence, but a larger vocabulary brings sparsity, and modern tokenizers have 100,000 to 200,000 tokens. Three naive designs fail in different ways: characters, a vocabulary of 150,000 mostly rare symbols with poor compression; bytes, a 256-symbol vocabulary and a ratio of 1; and words, whose vocabulary is unbounded and needs an unknown-token symbol.
**In this book:** [The Language Modeling Pipeline and Tokenization › The design space of tokenizers](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#the-design-space-of-tokenizers) · [The Language Modeling Pipeline and Tokenization › The core idea](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#the-core-idea).

### [1:10:00–1:16:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=4200) Byte-pair encoding

Byte-pair encoding is an old compression method, brought into natural language processing for machine translation and first used for language models in GPT-2. It is trained on the data: every byte starts as a token, and the most frequent pair of adjacent tokens is merged into a new token, again and again. Common sequences become single tokens and rare ones split into smaller units, so nothing is out of vocabulary. On "the cat and the hat", the pair of bytes 116 and 104, "th", merges first into token 256; iterations add 257 and 258 while the sequence shrinks and the vocabulary grows, reaching a ratio of 1.5 on the toy. New text is encoded by applying the learned merges in order, and decoding returns the original.
**In this book:** [The Language Modeling Pipeline and Tokenization › How it works, step by step](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#how-it-works-step-by-step).

### [1:16:00–1:20:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=4560) Making it fast, and a summary

The implementation shown is complete but slow; Assignment 1 asks students to speed it up, by looping only over the merges that matter, with indexes, by handling special tokens, and by splitting text into chunks before tokenizing, in Rust or C if Python proves too slow. Liang recaps: tokenizers convert strings to indices and back; characters, bytes and words each fall short; byte-pair encoding is a data-driven heuristic that works. Whatever replaces it must still abstract low-signal units, as with video or DNA, and treat chunks variably. Next comes resource accounting.
**In this book:** [The Language Modeling Pipeline and Tokenization › How it works, step by step](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#how-it-works-step-by-step) · [The Language Modeling Pipeline and Tokenization › What the practitioners say](../10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md#what-the-practitioners-say).

## What to take away

- Building from scratch teaches mechanics and mindset, which transfer to frontier scale; intuitions about modelling and data choices only come from experiments.
- Accuracy is efficiency times resources, so algorithms that scale matter, and efficiency counts most at large scale.
- The course runs from tokenization, architecture and training through systems, scaling laws, data and alignment, each seen through efficiency.
- A tokenizer maps text to token indices and back; byte-pair encoding learns frequent chunks from the data and never meets an unknown unit.

## Sources

- Percy Liang, Tatsu Hashimoto and the course staff, "Overview, tokenization", Stanford CS336 Language Modeling from Scratch, Spring 2026: [video](https://www.youtube.com/watch?v=JuoVZkPBiKk).
- Course page: <https://cs336.stanford.edu/>.
