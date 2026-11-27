# Lecture guide: LLM Post Training

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 14 · **Length:** 1:18:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=OCdwWfVoQ-Q) · **Slides:** [slides](https://www.dropbox.com/scl/fi/ed32dovpq8no4571xmkzs/Lec14-LLM-Post-training.pdf?rlkey=5re66ef6shk3tr3v31ey6hzzo&st=d9n9h7ql&dl=0)
**Chapters that cite this lecture:** [09. LLM Post-Training and On-Device Training](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) · [10. Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) · [12. Vision Transformers](../09-efficient-deep-learning/12-vision-transformers.md) · [12. Alignment and Multimodality](../10-llm-internals/12-alignment-and-multimodality.md)

> **In one sentence:** Song Han covers post-training: supervised fine-tuning, RLHF and DPO; parameter-efficient fine-tuning from BitFit and adapters to LoRA, QLoRA and BitDelta; vision-language models of both kinds, Flamingo-style cross-attention and tokens in, tokens out for PaLM-E and VILA; and prompting with retrieval.

## Before you watch

[From Base Model to Assistant: Post-Training](../01-foundations/03-from-base-model-to-assistant-post-training.md) covers SFT, RLHF and DPO in more detail, [LLM Post-Training and On-Device Training](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) the parameter-efficient methods, and [Prompting and In-Context Learning](../01-foundations/05-prompting-and-in-context-learning.md) the last part. The lecture assumes the transformer and its attention, and once refers back to in-flight batching from an earlier lecture.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=0) Supervised fine-tuning

A language model's life has three stages: collecting data, pre-training, which consumes the most compute, and post-training on a smaller dataset that teaches the task and aligns the model with what people prefer. The lecture covers post-training, multimodal models and prompting. Supervised fine-tuning, SFT, shows the model prompts with human answers and applies the loss only to the answer tokens. Han's examples come from Llama 2's data: a poem for the first ten elements of the periodic table, and a polite refusal to write a brutal roast. Asked how to log in, a pre-trained model gives a correct but dry answer; after SFT it answers like a friendly support agent, which is what helpfulness means where a metric cannot say.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers).

### [4:00–12:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=240) RLHF: reward model and reinforcement learning

Scores such as BLEU are not enough for creativity, truthfulness or usefulness, so reinforcement learning from human feedback lets a model optimize for such subjective, human-defined qualities, a crucial step behind ChatGPT. Three stages. First SFT, as above. Second, comparison data: for a prompt such as explaining the moon landing to a six-year-old, people rank several answers, in Han's example the story of people going to the moon first and the one about the space race last. A reward model is trained on these pairs so that the preferred answer scores higher by as wide a margin as possible. Third, the policy generates answers, the reward model scores them, and PPO updates the policy. The objective has two terms and needs three models: the reward term, and a penalty keeping the tuned model close to a frozen reference so it does not drift or overfit the reward model.
**In this book:** [From Base Model to Assistant: Post-Training › 2. Why imitation is not enough](../01-foundations/03-from-base-model-to-assistant-post-training.md#2-why-imitation-is-not-enough) · [From Base Model to Assistant: Post-Training › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [12:00–16:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=720) DPO: one model, one loss

That is complicated, and direct preference optimization, DPO, removes the reinforcement learning: no reward model, no separate phases, a single loss like SFT's. Each example holds a prompt, a preferred answer and a rejected one: asked about Shanghai, a city in China against a place that does not exist. The reference model's probabilities are computed once in advance; the tuned model's log probability of the preferred answer, relative to the reference, is raised, and that of the rejected answer lowered, so their difference grows.
**In this book:** [From Base Model to Assistant: Post-Training › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [16:00–20:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=960) Parameter-efficient fine-tuning: bias, side branch, adapter

Full fine-tuning stores gradients and optimizer states for every parameter. Parameter-efficient methods train few. BitFit trains only the bias terms, which needs no stored activations: BERT-base has 110 million parameters but only 0.1 million biases, a thousand times fewer, competitive on small and medium data and worse on large. TinyTL, an earlier method of Han's group, adds a light residual branch and learns only the difference from the frozen network, keeping activations small. Adapters insert small bottleneck modules, two feed-forward layers, into each transformer block: a few trainable parameters per task, so that a thousand tasks take 14 gigabytes instead of 14 petabytes of copies of a 7-billion model, with accuracy close to full tuning. The cost is latency, since the model grows deeper.
**In this book:** [LLM Post-Training and On-Device Training › How it works: the PEFT menu](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#how-it-works-the-peft-menu).

### [20:00–26:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=1200) Prompt and prefix tuning

Can a model be tuned with no extra parameters? Prompt tuning learns a continuous prompt, prepended to the input, for each task. One 11-billion model then serves many tasks, and requests from different tasks share a batch because they all look like prompt plus input, where separate per-task models could not be batched. For large models it approaches full fine-tuning. Prefix tuning puts tunable prompts in every layer instead of only the input and scores noticeably better. The catch: longer inputs mean a larger KV cache and more latency.
**In this book:** [LLM Post-Training and On-Device Training › How it works: the PEFT menu](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#how-it-works-the-peft-menu).

### [26:00–30:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=1560) LoRA

LoRA adds a low-rank side branch next to a frozen weight: one matrix projects the dimension d down to a small rank r, another projects back. The first starts from a Gaussian, the second at zero, so training begins exactly at the pre-trained model. Because there is no nonlinearity in the branch, its product can be added to the main weight at inference, leaving zero extra latency, the same residual idea as TinyTL. Han shows the community's LoRA add-ons for diffusion models: an ink-scenery style, a detail enhancer, a model that draws sushi rolls shaped like huskies.
**In this book:** [LLM Post-Training and On-Device Training › LoRA, step by step](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#lora-step-by-step).

### [30:00–34:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=1800) QLoRA

QLoRA also quantizes the frozen backbone to 4 bits, 3.5 gigabytes instead of 14 for a 7-billion model, while the adapters stay 16-bit. It introduces a 4-bit NormalFloat format whose codebook values are fixed quantiles of a normal distribution, unevenly spaced but precomputed, so no learning is needed; double quantization, which quantizes the scaling constants too; and paged optimizer states, moved to the CPU when not needed. Fine-tuning then fits in about 20 to 26 gigabytes, within reach of entry-level GPUs.
**In this book:** [LLM Post-Training and On-Device Training › LoRA, step by step](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#lora-step-by-step) · [LLM Post-Training and On-Device Training › How it works: the PEFT menu](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#how-it-works-the-peft-menu).

### [34:00–40:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=2040) BitDelta

Fine-tuning adds little to a well-trained model, so the change should compress well. BitDelta quantizes the difference between a fine-tuned model and its base to one bit per weight, multiplied by one 16-bit scale per tensor. Many fine-tuned models then share one base, each adding a one-bit delta, where separate copies would need 16 bits for every weight. The scale starts as the mean of the difference and is refined by distillation on about 800 samples, about 10 minutes for a 7-billion model. Compression is 10 to 15 times, nearer 16 for larger models; a fused binary kernel keeps latency low; and a demo serves six models fine-tuned from Mistral 7B at once, useful when many tenants share a base.
**In this book:** [LLM Post-Training and On-Device Training › What the practitioners say](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#what-the-practitioners-say).

### [40:00–48:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=2400) Vision-language models through cross-attention

After a break, multimodal models, in two styles. Flamingo keeps the language model frozen and injects images through cross-attention. A vision encoder turns an image into tokens, and a perceiver resampler reduces a variable number of them to a fixed count: in Han's example 27 image tokens are concatenated with 5 learned queries, attention gives a 5 by 32 map, and the output is 5 tokens whatever the input length. In each layer the queries come from the text and the keys and values from these visual tokens, with a tanh gate initialized to zero, so the model starts as a pure language model and learns how much vision to admit. It learns in context, a chinchilla and a shiba demonstrated and a flamingo named; holds a dialogue about two teddy bears using a computer on the moon; and recognizes Chicago from its aquarium and Tokyo from its tower.
**In this book:** [Alignment and Multimodality › How it works, step by step › 3. The standard recipe: encoder, projector, language model](../10-llm-internals/12-alignment-and-multimodality.md#3-the-standard-recipe-encoder-projector-language-model).

### [48:00–54:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=2880) Tokens in, tokens out: PaLM-E and VILA

The second style treats image and text tokens alike. PaLM-E, an embodied model that led to RT-2, takes images, video, action and audio as tokens and outputs language or control signals: one uniform model, token in, token out. VILA, Han's group's model, passes an image through a vision transformer, projects the result into the language model's space, concatenates it with text tokens, and trains in three stages: align the projector, pre-train, then supervised fine-tuning. Its lessons: freezing the language model gives acceptable zero-shot results but unfreezing it is what yields in-context learning; interleaved image-text data matters more than image-text pairs alone; and blending text-only instruction data into fine-tuning protects text ability and also helps the visual tasks: MMLU rises from 40 to 50 and VQA from 69 to 72.
**In this book:** [Alignment and Multimodality › 3. The standard recipe: encoder, projector, language model](../10-llm-internals/12-alignment-and-multimodality.md#3-the-standard-recipe-encoder-projector-language-model).

### [54:00–58:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3240) What VILA does

Image resolution counts for more than how many tokens the image becomes. Demos show VILA counting animals in context, naming companies from their logos, reasoning step by step that two beers at 6 dollars cost 12 by reading a menu, advising a driver behind a truck shedding a flying chair, comparing Arctic ice in 1984 and 2012, and seeing that CPR is practised on a mannequin. The model is open source with an online demo.
**In this book:** [Alignment and Multimodality › 3. The standard recipe: encoder, projector, language model](../10-llm-internals/12-alignment-and-multimodality.md#3-the-standard-recipe-encoder-projector-language-model).

### [58:00–1:00:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3480) High resolution

Large images need more resolution. InternVL matches an image to predefined aspect ratios, resizes, cuts it into tiles of 448 by 448, and adds a downsampled thumbnail of the whole; an 800 by 1300 image becomes six tiles plus one. OCR and text tasks keep improving with more tiles, while knowledge and reasoning peak at six and decline after. CogAgent combines the styles: a low-resolution encoder's tokens are concatenated with the text, and a high-resolution encoder's features enter through cross-attention as keys and values.
**In this book:** [Alignment and Multimodality › 4. Resolution](../10-llm-internals/12-alignment-and-multimodality.md#4-resolution).

### [1:00:00–1:06:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3600) One model for understanding and generation

Can one model both understand and generate images? Generation needs discrete visual tokens, a lookup table for images as words have, aligned with text so that one pipeline predicts the next token of either. VILA-U trains a unified vision tower with two losses: reconstruction, so that a residual quantizer with several codebooks and a decoder can rebuild the image, and image-text contrast, so that visual and text tokens share a space. Discrete tokens gave double-digit gains on image and video understanding over earlier discrete methods and matched continuous-token models; a demo generates images from prompts.
**In this book:** [Alignment and Multimodality › 6. Generation](../10-llm-internals/12-alignment-and-multimodality.md#6-generation).

### [1:06:00–1:08:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=3960) Zero-shot and few-shot prompting

Prompt engineering makes one foundation model serve many tasks. Zero-shot prompting states the task in the prompt; six generators are replaced by six prompts. Few-shot prompting demonstrates the task with examples, as with reviews labelled in a binary format, after which the model labels a new review the same way.
**In this book:** [Prompting and In-Context Learning › 1. Start with zero-shot](../01-foundations/05-prompting-and-in-context-learning.md#1-start-with-zero-shot) · [Prompting and In-Context Learning › 2. Add exemplars when format or judgment is off](../01-foundations/05-prompting-and-in-context-learning.md#2-add-exemplars-when-format-or-judgment-is-off).

### [1:08:00–1:10:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=4080) Tips for examples, and chain of thought

Two rules for examples: give each class about as many, birds and fish alike, and keep the format identical across them. Chain-of-thought prompting supplies the intermediate steps: the tennis-ball problem solved in words teaches the model to reason through the cafeteria problem and answer 9 instead of 27.
**In this book:** [Prompting and In-Context Learning › 2. Add exemplars when format or judgment is off](../01-foundations/05-prompting-and-in-context-learning.md#2-add-exemplars-when-format-or-judgment-is-off) · [Reasoning in LLMs: From Chain-of-Thought to Search › The core idea](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#the-core-idea).

### [1:10:00–1:14:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=4200) Prompting in practice

A short phrase, "let's think step by step", often suffices, though Han notes that this method is already incorporated in models these days. He demonstrates: a syllabus request returns a semester's plan, so he asks for a one-hour lecture and gets five headings, and pasting the outlines of earlier lectures improves the result. Image prompts gain detail with each added phrase. A famous trick, asking the model to play a grandmother who reads activation keys as a bedtime story, once bypassed a refusal; it has since been patched.
**In this book:** [Prompting and In-Context Learning › 7. Engineer the prompt like code](../01-foundations/05-prompting-and-in-context-learning.md#7-engineer-the-prompt-like-code).

### [1:14:00–1:18:00](https://www.youtube.com/watch?v=OCdwWfVoQ-Q&t=4440) Retrieval-augmented generation

Knowledge can live outside the parameters. Retrieval-augmented generation keeps documents in a database, retrieves those relevant to a question and appends them to the prompt: asked what protects the digestive system, the model answers from a retrieved passage about gastric acid. It fixes staleness: the database, not the model, is updated, as with the CEO of Twitter after a knowledge cutoff. Its parts are an embedding model, ranked on the MTEB benchmark; a retriever; a re-ranker scoring relevance; and the language model. The course assistant shown earlier is built this way, over Han's slides and lecture videos.
**In this book:** [LlamaIndex: Building a Knowledge Assistant › The core idea](../05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md#the-core-idea).

## What to take away

- SFT imitates good answers; RLHF and DPO add preferences, DPO with one model and one loss.
- Train few parameters: BitFit, adapters, prompt and prefix tuning, and LoRA, which folds into the weights and costs no latency; QLoRA and BitDelta cut memory further.
- Vision-language models either inject vision by cross-attention with a gate (Flamingo) or tokenize everything (PaLM-E, VILA); unfreeze the language model and blend in text data.
- Prompting rests on zero-shot instructions, balanced examples and chain of thought, with retrieval for fresh knowledge.

## Sources

- Song Han, "LLM Post Training", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=OCdwWfVoQ-Q).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
