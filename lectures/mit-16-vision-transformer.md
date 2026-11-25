# Lecture guide: Vision Transformer

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 16 · **Length:** 1:02:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=v0jYDgaVzlk) · **Slides:** [slides](https://www.dropbox.com/scl/fi/lr3jlbzoa1du3og22wbiw/Lec16-Vision-Transformers.pdf?rlkey=6ejlatw4kpfzxgxg7zx2a6zo2&st=7btq6r53&dl=0)
**Chapters that cite this lecture:** [10. Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md)

> **In one sentence:** Song Han turns transformers to images: how patches become tokens, why high resolution is expensive, and three ways to make it affordable (window attention, EfficientViT's linear attention with a convolution branch, SparseViT's pruned windows), then self-supervised pre-training and HART, an autoregressive image generator that runs interactively on a laptop.

## Before you watch

The chapter [Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) follows the first half of the lecture in its section on efficient vision transformers. The transformer lecture is assumed; nothing else.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=0) Plan, and a Halloween demo

On Halloween the class plays with a live demo, hart.mit.edu, that generates a pumpkin image in a few seconds on an A6000 GPU in the basement. The agenda: the basics of vision transformers, three ways to accelerate them (window attention, linear attention, sparse attention), self-supervised learning without labels, and autoregressive image generation, the method behind the demo.
**In this book:** not needed (lecture introduction and plan of the lecture).

### [2:00–4:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=120) Images as tokens

Text splits into tokens easily; an image is cut into patches. A 96 by 96 image with patches of 32 by 32 gives 9 tokens. Each patch, 3,072 numbers, is flattened and projected to 768; in practice one convolution with kernel 32, stride 32, no padding, 3 input channels and 768 outputs does both. Positional encodings are added, since otherwise the model could not tell where a patch came from, and a standard transformer encoder follows.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [4:00–6:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=240) Sizes, and ViT against CNNs

ViT-Base, ViT-Large and ViT-Huge differ in size; ViT-Large has 24 layers, a hidden size of 1,024, a feed-forward size of 4,096, 16 heads and about 300 million parameters. A suffix such as /16 names the patch size, and larger patches give a coarser model. With little training data a vision transformer loses to a convolutional network; pre-trained on very large data it overtakes one, so it scales better.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [6:00–8:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=360) Why high resolution matters

Many tasks need dense prediction at high resolution: medical image segmentation, where the boundary of a tumour matters; super-resolution, accelerated from 16 to 41 frames per second in his demo and used in NVIDIA's DLSS for games; and autonomous driving, where a cyclist is invisible at low resolution and visible at high, with a large gain in segmentation quality.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [8:00–10:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=480) The price of resolution, and Segment Anything

No free lunch: from 1k to 2k resolution a vision transformer's computation grows far faster than a convolutional network's. The number of tokens grows with the square of the resolution and attention with the square of the token count, so the cost grows with the fourth power. EfficientViT makes a slow segmentation model run several times faster at the same accuracy on a Jetson Orin. High resolution also serves augmented reality, which segments what the wearer looks at, as in Segment Anything: a ViT image encoder takes most of the time, and prompts, a point, a box or a mask, combine with its embedding to predict the mask; the model handles ambiguity and labels more data for itself.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [10:00–14:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=600) Window attention and shifted windows

Instead of letting every patch attend to every patch, window attention restricts it to windows, 7 by 7 patches in Han's example. Each window holds a fixed number of tokens, so the cost grows linearly with the image. The flaw is isolation: tokens in neighbouring windows never meet. The next layer shifts the windows by half a window, so that tokens near an edge attend to the neighbouring window, and repetition connects everything. The Swin Transformer beats ViT accuracy on ImageNet, detection and segmentation.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [14:00–16:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=840) Sparse windows

Not all windows earn their compute. In point clouds 99.9% of voxels are empty, and images have empty background too. SparseViT attends only to windows that contain something. Grouping by equal windows leaves groups of 1, 2 or 3 tokens, so fast groups wait for slow ones; grouping by equal size, a fixed number of non-empty tokens per group, balances the work. On a Jetson Orin the result runs faster than other transformers and than convolution models.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [16:00–20:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=960) Linear attention, and what it loses

Softmax attention computes query times key for every pair of tokens, cost quadratic in their number, even if the softmax is replaced by a ReLU. Matrix multiplication is associative, so computing key times value first, a d by d result, and then multiplying by the query costs on the order of n times d squared, linear in n. But the attention maps go flat: the dog's eyes and the cat's nose, sharply attended before, receive weak attention everywhere, so local detail and multi-scale information are lost, and accuracy drops.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers) · [Attention Alternatives and Mixture of Experts › 3. Linear attention](../10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md#3-linear-attention).

### [20:00–22:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1200) A convolution branch restores the local detail

EfficientViT gives the model what linear attention lacks. A convolution branch, cheaply a depthwise convolution followed by a 1 by 1 grouped convolution, extracts local features while the linear attention handles the global ones; the spatial and channel modelling are decoupled, and the branch sits inside the feed-forward layer. Little computation is added, and the accuracy is recovered and slightly improved.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [22:00–24:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1320) What EfficientViT delivers

Segmentation speeds up 5.8 times on a mobile chip, 2.8 times on a Jetson Orin and 1.7 times on an A100, each with higher accuracy. Super-resolution from 512 to 1k gains quality and speed: on a driving dataset 50 milliseconds fall to 2.8, and on faces SwinIR gives 4.7 images per second against 70. For Segment Anything, with box or point prompts, throughput rises from 11 to 182 images per second at the same quality. Latency is measured on the Orin because an edge device serves one user, and throughput on the A100 because the cloud serves many.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [24:00–30:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1440) SparseViT: pruning windows in driving images

For a driving scene, half the resolution with all pixels loses detail; the same budget spent on full resolution with a quarter of the pixels keeps it. SparseViT prunes windows by their L2 activation magnitude, keeps the important ones, people and cars, sorted by importance, and prunes later layers harder, since a pruned token cannot return. A model trained dense is fine-tuned on sampled sparsity patterns, and an evolutionary search chooses the sparsity of each layer under a latency budget, where random search does not improve. The model is 1.5 times faster at 256 and 224 resolution for 3D detection and 2D segmentation, and its masks keep the foreground and drop the background.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [30:00–34:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=1800) Self-supervised learning: contrastive learning

Labels are expensive, and vision transformers want large data. After a break, two ways to learn without labels. Contrastive learning feeds two views of a cat through an image encoder and pulls their embeddings together while pushing the embedding of a dog away. From random initialization larger models do worse; with self-supervised pre-training larger models do better and beat their supervised counterparts. The multimodal version, CLIP, encodes paired text and images so that matching pairs score high on the diagonal of a similarity matrix; at inference an image is compared with a vocabulary of prompts and the best match chosen, which gives zero-shot classification without any training examples per class.
**In this book:** [Alignment and Multimodality › 1. CLIP: learning what images mean from their captions](../10-llm-internals/12-alignment-and-multimodality.md#1-clip-learning-what-images-mean-from-their-captions).

### [34:00–38:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=2040) Masked image modelling

Masked image modelling borrows from BERT's masked language model, which hides a word and predicts it. Patches are masked, the visible ones pass through a heavy encoder, and a light decoder reconstructs the whole image, 25 tokens from 8 in his example. Objects reappear from few pixels: a bus, a dog, a clock. The best mask ratio is 70 to 75%, against 15% for BERT, which tells Han that images carry less information per token than language and tolerate more masking. The accuracy is higher than the supervised baseline.
**In this book:** nothing beyond this guide; nearest: [Alignment and Multimodality › 1. CLIP: learning what images mean from their captions](../10-llm-internals/12-alignment-and-multimodality.md#1-clip-learning-what-images-mean-from-their-captions).

### [38:00–42:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=2280) From understanding to generation

So far the models were discriminative. An autoregressive transformer generates tokens one after another, so it can generate visual tokens too, and multimodal language models benefit, as in the Chameleon report, whose models output images natively as discrete tokens. HART, the hybrid autoregressive transformer built by the course's teaching assistant, is faster than diffusion models, which need many denoising steps: about 2 images per second against 0.2 for SDXL, PixArt-α, Playground and SD3.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [42:00–46:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=2520) Orders of generation, and discrete tokens

Tokens can be generated in raster order, one patch at a time, in random order, or several at once; generating one token at a time is bound by memory, since each token passes through all the weights. Language has a finite vocabulary and a cross-entropy loss; pixels are continuous. The bridge is a vector quantizer with a codebook, an encoder and a decoder that turn patches into discrete tokens, the idea of Deep Compression's centroid lookup applied to vectors rather than single numbers.
**In this book:** [Alignment and Multimodality › 6. Generation](../10-llm-internals/12-alignment-and-multimodality.md#6-generation).

### [46:00–50:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=2760) Next-scale prediction

VAR changes the order: generate one token for the whole image, then 2 by 2, then 4 by 4 and so on, from the coarse picture to fine detail. All tokens of a scale are produced together, with a block-shaped attention mask, so generation is no longer bound by memory. Quality still falls short of the reference, for instance in the eyes: a discrete tokenizer cannot represent continuous images exactly.
**In this book:** [Alignment and Multimodality › 6. Generation](../10-llm-internals/12-alignment-and-multimodality.md#6-generation).

### [50:00–56:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=3000) HART: discrete tokens plus a residual

HART has one decoder for continuous and discrete tokens, trained on samples of both. The difference between them, the residual, holds the fine detail that discrete tokens miss, and a very small diffusion model of 30 to 40 million parameters learns it. A text prompt becomes language-model tokens placed before the image tokens; the residual diffusion models the gap between the sum of the predicted tokens across scales and the final image, and the two are added. Discrete tokens carry the big picture, residual tokens the eyes and hair.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [56:00–1:02:00](https://www.youtube.com/watch?v=v0jYDgaVzlk&t=3360) Results, a laptop demo, and a summary

HART matches the diffusion models' quality on Han's prompts and runs at interactive speed on a laptop with a mobile 4090 GPU: steampunk makeup, an astronaut on a horse, a holographic crystal cat, each in about a second, with no internet. He recaps: images are tokens; attention grows with resolution, and windows, linear attention and sparse windows tame it; self-supervised learning removes the need for labels; and token-in, token-out models generate too. Diffusion models are the next lecture; the code of EfficientViT and HART is open source.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

## What to take away

- An image is a sequence of patch tokens; because tokens grow with the square of resolution, attention's cost grows with the fourth power.
- Windows, linear attention and sparse windows make vision transformers affordable; a convolution branch supplies the local detail linear attention lacks.
- Contrastive learning and masked image modelling pre-train without labels, and images tolerate far more masking than text.
- Discrete visual tokens let one autoregressive model generate images; HART adds a tiny diffusion model for the residual detail.

## Sources

- Song Han, "Vision Transformer", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=v0jYDgaVzlk).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
