# Lecture guide: Diffusion Model

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 18 · **Length:** 1:12:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=LXrqmQrscf0) · **Slides:** [slides](https://www.dropbox.com/scl/fi/f4end70haytw1nalboxp2/Lec18-Diffusion-Models.pdf?rlkey=emaxca812n2npb2rinq1nor64&st=ed3ziw4o&dl=0)
**Chapters that cite this lecture:** [10. Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md)

> **In one sentence:** Song Han explains diffusion models, which turn noise into images step by step, and how to make them cheap: conditioning and guidance, diffusion in a compressed latent space (latent diffusion, DC-AE, Sana), fewer sampling steps (DDIM, distillation), spatial sparsity, 4-bit weights and activations, and several GPUs.

## Before you watch

The chapter [Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) covers latent diffusion, Sana's compressor and sparse inference in its section on generative models. Gaussian distributions and the transformer lectures are assumed; the derivations are short.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=0) Plan

Where a discriminative model predicts a decision boundary, a generative model predicts the data distribution, for photo editing, image generation and video generation, as with Midjourney and OpenAI's Sora, and all of it is computationally intensive. The course's generative landscape so far: GANs, HART, and today diffusion models with efficient autoencoders. The plan: how diffusion works, conditioning, latent diffusion, editing and personalization, then fewer sampling steps and acceleration by sparsity, quantization and parallelism. Han's own model, Sana, made the opening image of a cyberpunk cat under a neon MIT sign.
**In this book:** not needed (lecture introduction and plan of the lecture).

### [2:00–6:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=120) The forward process

Diffusion has a forward and a reverse process. The forward process destroys data by adding a little Gaussian noise at each step, with a schedule β_t setting the speed, until the image is pure noise. Each step depends on the previous one, but because the dependence is linear, two Gaussians can be merged: with α_t = 1 − β_t and their product up to t, the noisy image at any step is the clean image times a scale plus noise times another scale, the diffusion kernel. The schedule is designed so that at the last step the distribution is nearly the standard normal.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [6:00–10:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=360) Training and sampling

When the steps are small, the reverse step from x_t to x_(t−1) is also a Gaussian whose mean a network learns. Training: take a clean image, sample a step t and a noise, form x_t, let the network predict the noise from x_t, and minimize the squared error against the noise actually added. Sampling starts from noise and runs the model many times: the predicted mean subtracts the scaled predicted noise from the image, a little fresh noise is added for the variance, and the result is a cleaner image, which becomes the input of the next step until x_0.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [10:00–12:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=600) Why diffusion is slow

The rule of thumb, predict the noise, subtract the noise, is repeated hundreds of times with the same model, and every pass predicts a value for every pixel, not a class or a box. That is where the computation goes: unlike earlier models that run once, this one runs the same network over and over. The reward: images that beat human ones on ImageNet in the cited study.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [12:00–18:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=720) Conditions: class and text

Generation usually follows a condition: a class, a text prompt, or pixel-wise guidance. A class id passes through a small multilayer perceptron into an embedding that is broadcast over the feature map and added, or turned into a scale and a bias. Text joins through attention, in three styles. Cross-attention treats image tokens as queries and text tokens as keys and values, so the output stays an image that carries the text. Joint attention passes image and text through separate query, key and value transformations, concatenates them, runs attention, and splits the output through separate output transformations; the two modalities are symmetric. Early fusion concatenates the tokens first and applies one transformation to both.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [18:00–22:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=1080) Pixel-wise conditions and ControlNet

Pixel-wise conditions give a segmentation map, Canny edges or a human pose, and the generated image must follow it. ControlNet freezes the trained denoising network and adds a trainable copy of its encoder half. The copy receives the pixel condition at every encoder stage and feeds the decoder through 1 by 1 convolutions initialized to zero, so the new branch has no effect when training begins and the model changes smoothly.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [22:00–30:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=1320) Classifier guidance and classifier-free guidance

Guidance trades diversity for fidelity. Classifier guidance adds, during sampling, the gradient of a classifier trained on noisy images, scaled by a strength ω; a small ω gives varied but unreliable images, a large one faithful but repetitive ones. Its limits: classes only, and a separate network to train. Classifier-free guidance needs no classifier. By Bayes' rule the same objective equals the conditional prediction times the conditional over the unconditional, so the model is run twice per step, with the condition and without, and the outputs combined as (ω + 1) times the conditional minus ω times the unconditional. It works for any condition, text or pixels, at twice the FLOPs, and with the same quality-diversity trade-off.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [30:00–34:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=1800) Latent diffusion

Every technique so far adds computation. Latent diffusion removes some: instead of denoising a high-resolution image pixel by pixel, an encoder compresses it 4, 8 or, in Han's recent work, 64 times per side; diffusion runs in that small latent space and a decoder restores the image. Training and sampling keep their form, with the encoder before the noise and the decoder after the last denoising step, and high-resolution images become affordable.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [34:00–38:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=2040) Deep compression autoencoder

The more the compression, the fewer the tokens: compressing each side eight times more than the usual, from 8 to 64 per side, leaves 64 times fewer tokens and, attention being quadratic, 4,096 times less attention computation. Ordinary variational autoencoders collapse at that ratio; Stable Diffusion's degrades fast in FID. DC-AE, the deep compression autoencoder, holds FID to 128 times compression per side. One ingredient is residual autoencoding: a weight-free branch in each downsampling block that moves every 2 by 2 block of pixels into four channels, and the inverse in upsampling, so the network need not learn the rearrangement.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [38:00–42:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=2280) Adapting to high resolution, and Sana

A second ingredient adapts the autoencoder to high resolution in three stages: train the whole encoder and decoder at low resolution, tune only the middle layers at high resolution, then refine only the last layer of the decoder. With 64-fold compression a 512 image becomes an 8 by 8 latent of 64 tokens instead of 4,096, and generation is 19 times faster; 4k images become possible. On this Han's group built Sana: the linear-attention module of EfficientViT for the denoiser, the DC-AE, and a decoder-only language model, Gemma, as the text encoder. Asked plainly, Gemma chats about the prompt; prepended with a fixed complex instruction and a few examples, it expands "a man is walking" into a scene with a leather jacket and a setting sun.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [42:00–48:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=2520) Better captions, and Sana's results

The vision-language model VILA recaptions the training images: a short caption grows into a paragraph about the chocolate cake and the red heart, more than human labellers would write. Captions from two model sizes are compared by CLIP score to keep hallucination down. So VILA produces data for Sana, and the two improve together. Sana's 1.6-billion-parameter model generates text, logos and faces in detail and runs 25 times faster than FLUX at 1k resolution and about 100 times faster at 4k, thanks to the autoencoder, linear attention, kernel fusion and a flow-based solver.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [48:00–52:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=2880) Editing and personalization

Editing follows the same idea as the lecture's opening: a stroke and an image live in different regions of space, so noise is added until they overlap and denoising moves the stroke toward images, which turns a rough drawing into a castle. Personalization makes the model draw one particular dog. Fine-tuning on three to five pictures with a rare identifier lets a prompt place that dog on a beach; the cost is one fine-tuned model per subject, and Han mentions that training-free methods followed.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [52:00–56:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=3120) Fewer steps: DDIM and distillation

Denoising is iterative, so fewer, larger steps would save time. DDIM, the denoising diffusion implicit model, defines the step from x_t to depend on the predicted x_0 as well as on x_t, an inference-only change that lets sampling skip ahead, by 10 steps at a time. DDPM's FID explodes when 1,000 steps become 20 or 10; DDIM's stays level. Progressive distillation trains a student to match two adjacent teacher steps in one, halving the count each generation, four steps to one, with a lower FID than shorter plain sampling.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [56:00–1:00:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=3360) Spatially sparse inference

Photo editing changes few pixels, a sign under 2% of the image, yet Stable Diffusion recomputes everything. Spatially sparse inference, SIGE, recomputes only the edited blocks and reuses the other feature maps from the previous pass. The difference mask is discretized to a grid, the changed blocks are gathered, stacked into a batch for parallelism, convolved, and scattered back; patches are two-dimensional convolutions with no border exchange, so no sparse-convolution library is needed, and the method applies to diffusion transformers as well.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [1:00:00–1:02:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=3600) What sparsity buys

Inpainting a horse into a box, 3% of an image for a coconut tree, gives the same quality three to four times faster, and a live demo adds clouds to a photo interactively.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=3720) Quantization: W4A4

Language models at batch size one are bound by memory, so weight-only quantization speeds them up; diffusion is bound by compute, so only quantizing weights and activations both, W4A4, helps. Both carry outliers. Smoothing, as in SmoothQuant, moves the outliers out of the activations into the weights; then a full-precision low-rank side branch of about 32 ranks, from an SVD, absorbs the weight outliers, leaving 4-bit weights and 4-bit activations that are easy to quantize. The side branch suits LoRA: new LoRA weights just add ranks, with no re-quantization. Kernel fusion removes about 40% of the latency overhead by merging the side branch's down projection into the previous kernel and its up projection into the next.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [1:06:00–1:08:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=3960) SVDQuant's results

W4A16 methods save memory but not time, since arithmetic stays 16-bit. SVDQuant, with 4-bit INT4 or FP4 arithmetic, runs about 3 times faster on an RTX 4090 and 3.5 times faster than NF4, whose single step takes 1.8 seconds against half a second; the FP16 model runs out of memory. Memory falls from 23 gigabytes to 6.5, quality tracks FP16 where NF4 and naive INT4 degrade, and LoRA styles such as realism and anime keep their look.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [1:08:00–1:12:00](https://www.youtube.com/watch?v=LXrqmQrscf0&t=4080) DistriFusion, and a summary

More GPUs can help a diffusion model too. Splitting the image over four GPUs without communication yields four unrelated images. DistriFusion observes that activations at adjacent time steps are nearly the same, so each device attends to the other devices' activations from the previous step, which removes most communication and lets the rest overlap with computation. A 12-second generation becomes about 3 times faster on four GPUs with the quality intact, and about 6 times faster on eight GPUs at 3k resolution. Han closes by recapping the lecture.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

## What to take away

- A diffusion model learns to predict noise and generates by removing it step by step, which costs many pixel-wise passes.
- Conditioning and classifier-free guidance make generation follow a prompt, at the price of two passes per step.
- Diffuse in a heavily compressed latent space, with a compressor that survives the ratio, and most of the cost disappears; DC-AE and Sana show how far this goes.
- Then take fewer steps, recompute only edited regions, quantize weights and activations together with a low-rank branch, and spread the work over GPUs.

## Sources

- Song Han, "Diffusion Model", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=LXrqmQrscf0).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
