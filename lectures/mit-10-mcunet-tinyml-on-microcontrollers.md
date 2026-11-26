# Lecture guide: MCUNet: TinyML on Microcontrollers

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 10 · **Length:** 1:08:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=uR1KKhIhHEk) · **Slides:** [slides](https://www.dropbox.com/scl/fi/udgt7c6sw5wpvrbh7us2t/Lec10-MCUNet.pdf?rlkey=sryh8aiehv8792uk1ocu00icn&st=8v4oql2g&dl=0)
**Chapters that cite this lecture:** [05. Neural Architecture Search](../09-efficient-deep-learning/05-neural-architecture-search.md) · [07. TinyML: Microcontrollers and TinyEngine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md)

> **In one sentence:** Song Han presents MCUNet, the system-algorithm co-design that runs real neural networks on microcontrollers with a few hundred kilobytes of memory: TinyNAS finds a model that fits the flash and SRAM budgets, and per-patch inference tames the memory of the early layers.

## Before you watch

The chapter [TinyML: Microcontrollers and TinyEngine](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) follows this lecture step by step; [Neural Architecture Search](../09-efficient-deep-learning/05-neural-architecture-search.md) explains the once-for-all search that TinyNAS builds on. The memory arithmetic of the second lecture (parameters, activation sizes) is assumed.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=0) TinyML's promise

This lecture gathers pruning, quantization, distillation and architecture search into one system for microcontrollers. Today's AI is large: GPT-3 has 175 billion parameters, and its training is put at 355 GPU-years and over four million dollars. Han's wish is deep learning gone tiny, on the edge as well as in the cloud, so that images, text and voice need not leave the device: billions of IoT devices built on microcontrollers that cost a few dollars and sip power, running on renewable energy if need be. The uses are broad: smart homes, defect detection in manufacturing, personalized healthcare, precision agriculture.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Why this matters](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#why-this-matters).

### [4:00–6:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=240) The memory gap

The obstacle is memory. A cloud GPU offers 80 gigabytes and terabytes of storage; a phone a few gigabytes and hundreds of gigabytes; a microcontroller a few hundred kilobytes of SRAM for activations and about a megabyte of flash, four to five orders of magnitude less. Mobile AI is bounded by latency and energy; TinyML adds memory as a new constraint, and the same holds for today's language models: 175 billion parameters in FP16 take 340 gigabytes, more than one GPU holds.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Why this matters](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#why-this-matters).

### [6:00–10:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=360) Where tensors live, and how far off models are

Both weights and activations must shrink. Activations are read and written during inference and so live in SRAM, which is volatile; weights are only read and can live in flash, which keeps its contents without power. Typical parts: an Arduino Nano with 256 kilobytes of SRAM and a single megabyte of flash; the STM32F746 the course uses, 320 kilobytes and one megabyte. Flash use is roughly the model size, and SRAM use is the input plus output activation of the largest layer, since weights can be fetched piece by piece. The gap is stark: against a 320-kilobyte budget, ResNet-50's peak is 23 times too large and MobileNetV2's 22 times; quantization helps four times but leaves a factor of five.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 1. Budget the memory first](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-1-budget-the-memory-first).

### [10:00–14:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=600) Why both must fit, and co-design

MobileNetV2 cuts weights more than four times against ResNet-18, but its peak activation grows by 80%. MCUNet's aim is both: weights six times smaller than ResNet-18 at similar accuracy and a peak activation 3.4 times smaller than MobileNetV2's, because if either fails to fit, the model does not run. The method is system-algorithm co-design. One may fix the library and search the model, as ProxylessNAS does, or fix the model and build the library, as TVM does; MCUNet searches the model with TinyNAS, covered here, and builds the inference engine TinyEngine, covered in the next lecture.
**In this book:** [TinyML: Microcontrollers and TinyEngine › The core idea](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#the-core-idea) · [TinyML: Microcontrollers and TinyEngine › Step 1. Budget the memory first](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-1-budget-the-memory-first).

### [14:00–18:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=840) TinyNAS: a search space for microcontrollers

TinyNAS has two stages: first find a good search space, then search in it, like narrowing the forest before looking for a lost friend. A mobile search space does not transfer: a phone has gigabytes of memory, a microcontroller 320 kilobytes, so even its smallest network does not fit. Instead the mobile space is scaled down by resolution and by a width multiplier, and the question is by how much, since microcontrollers range from 256 to 512 kilobytes of SRAM.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 2. Pick a model for the chip](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-2-pick-a-model-for-the-chip).

### [18:00–22:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1080) Choosing the search space by FLOPs under a memory budget

Given memory and storage limits, the method picks a subspace with two knobs, resolution and width multiplier, and leaves kernel sizes, expansion ratios and the number of blocks per stage to the later search. To choose without training, it analyzes each candidate space's distribution of FLOPs among models that satisfy the constraints. One space holds only models above 41 million FLOPs, another above 28 million; the top fifth reach 50 million in the first and 32 million in the second. Since computation is cheap and memory expensive, the space that fits more arithmetic under the same memory is judged better, and it was: 78.7% best accuracy against 74%.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 2. Pick a model for the chip](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-2-pick-a-model-for-the-chip) · [Neural Architecture Search › Step 2. Define the search space](../09-efficient-deep-learning/05-neural-architecture-search.md#step-2-define-the-search-space).

### [22:00–26:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1320) Flash, SRAM, width and resolution

Han poses two questions about the optimized spaces, with flash from 512 kilobytes to 2 megabytes on one axis and SRAM from 192 kilobytes to 512 kilobytes on the other. More flash with the same SRAM means more weights fit, so the width multiplier rises from about 0.4, and the resolution falls, since channels times resolution squared must stay within the SRAM. More SRAM with the same flash means the weights stay the same, so the width stays and the resolution rises. The figure ties flash and SRAM to weights and activations and to channels and resolution.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 2. Pick a model for the chip](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-2-pick-a-model-for-the-chip).

### [26:00–28:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1560) Searching inside the space

With the space fixed, the search itself uses the once-for-all approach from the previous lecture: train one supernetwork, sample sub-networks nested inside it and fine-tune them jointly, so that one training yields many models. Lab 3, released today, practises this.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 2. Pick a model for the chip](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-2-pick-a-model-for-the-chip).

### [28:00–30:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1680) What the search found

The searched model uses memory more evenly. In hand-designed MobileNetV2 the peak memory of a block is 2.2 times the average, and the peak alone sets the requirement; TinyNAS yields a flatter profile, so a larger model fits the same memory. Against MobileNetV2, Han reports MCUNet 2.4 times faster in latency with a peak SRAM 3.7 times smaller at higher accuracy.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 2. Pick a model for the chip](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-2-pick-a-model-for-the-chip).

### [30:00–32:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1800) The imbalance: early layers overflow

Plotting SRAM use per block explains why models fail. The first five stages, at high resolution, need 500 to 1400 kilobytes, far above a 256-kilobyte limit, with layer 2 8 times over; from layer 5 on everything fits. Reducing the memory of the early stages would reduce the whole.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 3. Patch-based inference](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-3-patch-based-inference).

### [32:00–36:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1920) Per-patch inference

Conventional inference computes a layer's whole output before the next layer starts. Per-patch inference computes one patch of the image through the early layers at a time, like cutting a too-large pizza into slices; the later layers, on small feature maps, run over the whole image. The ceiling on savings is the number of patches, never reached because the last layers still need the whole map. The peak fell from 1372 to 172 kilobytes, under the limit. In measurement, four patches gave about 3 times where 4 was the bound; nine patches, 4.9 times, down to 64 kilobytes.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 3. Patch-based inference](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-3-patch-based-inference).

### [36:00–38:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2160) The cost: halos

The first cost named is latency: patches run one after another and limit parallelism, though microcontrollers have little of it. The other cost is recomputation. A 3 by 3 convolution with stride 2 gives each output pixel a 5 by 5 receptive field, so neighbouring patches share a border, a halo, and the overlap grows with every earlier layer; for MobileNetV2 it costs about 10% more computation.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 3. Patch-based inference](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-3-patch-based-inference).

### [38:00–42:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2280) Redistribution, and a joint search

Two remedies. Apply per-patch inference only to the early stages, where memory is tight, and per-layer inference later. Then shrink the halo by moving receptive field out of the per-patch stage: replace a 3 by 3 convolution with a 1 by 1, remove a 3 by 3 layer, and add one 3 by 3 layer in a later stage so that the total receptive field is unchanged. The MACs return to the original count and accuracy holds. Finally, architecture and inference schedule are searched together: layers, channels, kernels and resolution on one side, whether to use patches, their size and how many layers on the other.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 3. Patch-based inference](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-3-patch-based-inference).

### [42:00–46:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2520) Results, and what the searched model looks like

Put together, MCUNetV2 runs visual wake words, person or no person, in about 30 kilobytes of SRAM at 90% accuracy: four times less memory than before, or 4% more accuracy at the same memory. MCUNetV2 also improves ImageNet-level classification over MCUNet and MobileNetV2 with the same 256 or 320 kilobytes of SRAM, and object detection improves by double digits. Dissecting the searched network shows sensible choices: small kernels in the per-patch stage, to shrink the halo; a small expansion ratio in the middle stages, to lower peak memory; a large expansion late, when resolution is small; and an input resolution of 160 instead of 128, which helps resolution-sensitive tasks such as detecting a distant person.
**In this book:** [TinyML: Microcontrollers and TinyEngine › Step 3. Patch-based inference](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#step-3-patch-based-inference) · [TinyML: Microcontrollers and TinyEngine › What the practitioners say](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#what-the-practitioners-say).

### [46:00–52:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2760) Vision applications

Applications begin with image classification: sorting fruit by colour is trivial, but MCUNet was the first to pass 70% on ImageNet on a commercial microcontroller, where MobileNetV2 reached 53%. Microcontrollers differ in memory; a once-for-all network trained once specializes to each. Visual wake words, person or no person, can gate a heavier recognition model and save battery and privacy. Object detection needs resolution, and accuracy falls sharply as resolution drops; per-patch inference allows more of it, and in a mask-detection demo it finds people that the per-layer model missed.
**In this book:** [TinyML: Microcontrollers and TinyEngine › What the practitioners say](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#what-the-practitioners-say).

### [52:00–56:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=3120) Training on the device, and audio

A microcontroller can also learn on the device: with two buttons labelling orange and banana, backpropagation runs locally, gradients, activations and weights all inside the memory, until the two are told apart; the training techniques come later in the course. For audio, tasks such as keyword spotting turn into vision problems by writing the signal as a two-dimensional spectrogram, time against frequency. Convolutions beat fully connected layers there, because neighbouring times and frequencies are related, and MCUNet improves the accuracy-latency frontier on the Speech Commands dataset.
**In this book:** [TinyML: Microcontrollers and TinyEngine › What the practitioners say](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#what-the-practitioners-say) · [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [56:00–1:02:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=3360) Time series and anomaly detection

Anomaly detection serves manufacturing, surveillance and healthcare: tell a flawed capsule or nut from a sound one. Han notes a new alternative: his group's visual language model VILA, with 7 billion parameters, answers that a nut is abnormal because it has a hole. The established tiny method is the autoencoder. An encoder compresses the input into a low-dimensional code and a decoder reconstructs the input from it; training minimizes the reconstruction error. Inputs like the training data reconstruct well, unlike ones do not, so a large error flags an anomaly. In a demo, a microcontroller with 256 kilobytes of SRAM, one megabyte of flash and a 64-megahertz clock lights a yellow lamp when a fan is poked or shaken. Han then summarizes the lecture.
**In this book:** [TinyML: Microcontrollers and TinyEngine › What the practitioners say](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#what-the-practitioners-say).

### [1:02:00–1:08:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=3720) A course assistant built with retrieval

Last, a demo of a web assistant built for the course. It embeds the lecture slides, notes and videos, retrieves the relevant ones for a question, and passes question plus material to a large language model, the retrieval-augmented pattern. Answers link to the matching lecture video and textbook section, and the assistant writes quizzes on request, about pruning for instance. Asked how per-patch inference handles an object larger than a patch, it gives a general answer about splitting the image; Han judges it too general, since halos and receptive-field redistribution are the specifics, and suggests building such an assistant as a final project.
**In this book:** nothing beyond this guide; nearest: [TinyML: Microcontrollers and TinyEngine › What the practitioners say](../09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md#what-the-practitioners-say).

## What to take away

- On a microcontroller, weights live in flash and activations in SRAM; both must fit, and the peak activation of the largest layer sets the SRAM need.
- TinyNAS first picks a search space by how much computation its models fit under the memory budget, then searches inside it.
- Per-patch inference cuts peak memory several times; its halo costs about a tenth more computation, which moving receptive field to later layers removes.
- TinyML brings ImageNet-level classification, detection, audio and anomaly detection to devices with a few hundred kilobytes.

## Sources

- Song Han, "MCUNet: TinyML on Microcontrollers", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=uR1KKhIhHEk).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
