# Lecture guide: Introduction

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 1 · **Length:** 1:06:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=U7EPZv8Kh9w) · **Slides:** [slides](https://www.dropbox.com/scl/fi/h3ggav4eopxsitqxzf6t2/Lec01-Introduction.pdf?rlkey=hzbpsha72p5e3ed4mdvcgcda5&st=pz5u977e&dl=0)
**Chapters that cite this lecture:** [01. Why Efficiency Matters](../09-efficient-deep-learning/01-why-efficiency-matters.md) · [02. Neural Network Basics for Efficiency](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) · [04. Quantization](../09-efficient-deep-learning/04-quantization.md) · [11. Course Summary and Outlook](../09-efficient-deep-learning/11-course-summary-and-outlook.md)

> **In one sentence:** Song Han opens MIT 6.5940 with the gap between growing models and finite hardware, a tour of what efficient techniques buy in vision, language and multimodal work, the hardware trends behind them, and the plan of the course.

## Before you watch

The chapter [Why Efficiency Matters](../09-efficient-deep-learning/01-why-efficiency-matters.md) carries the argument of the first minutes and a table of the results quoted in the lecture. The lecture is a tour: each topic returns later in the course, and the lecturer presents it as an overview, a taste of what is to come, so it asks for little more than knowing what a neural network is.

## The lecture, part by part

### [0:00–3:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=0) The lecturer and the course

Song Han opens the third run of MIT's course on efficient deep learning computing, which has grown from 30 students to more than 200. He trained at Tsinghua and at Stanford with Bill Dally, where his Deep Compression paper laid foundations for network compression and acceleration; he co-founded a startup making efficient AI chips and, at MIT, a startup on model optimization. His group's AWQ, a quantization method for large language models, won a best-paper award at MLSys and has more than six million downloads. The course has five hands-on assignments, built from what those startups learned.
**In this book:** not needed (lecturer's introduction and course organization).

### [3:00–5:20](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=180) Supply and demand

Why efficiency? A chart of supply and demand: in red the size of language models, from the 0.05 billion parameters of the first transformer to 1.5 billion for GPT-2 and a trillion for recent models; in green the memory of GPUs. The gap widens every year and drives up the price of training and serving. The course teaches compression techniques that shrink a model's size, memory and computation, so that one trains a model, compresses it and only then deploys it; publications on compression and sparsity are rising fast.
**In this book:** [Why Efficiency Matters › The gap that keeps widening](../09-efficient-deep-learning/01-why-efficiency-matters.md#the-gap-that-keeps-widening).

### [5:20–8:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=320) Vision: accuracy costs computation

The lecture surveys three workloads, vision first. On ImageNet the error rate fell sharply in 2012, the year AlexNet appeared, and later passed human level; big data, compute and algorithms drove it. No free lunch: on a chart of accuracy against multiply-accumulate operations (MACs, explained in the next lecture), higher accuracy sits to the right, and larger circles mark larger models. The course's aim is to push the frontier toward the upper-left corner, with less computation and equal or better accuracy, by techniques such as architecture search. Efficient models also run on the phone: photo tagging, people recognition and pose estimation stay on the device, so no data goes to the cloud.
**In this book:** [Why Efficiency Matters › How it works: where efficiency is won](../09-efficient-deep-learning/01-why-efficiency-matters.md#how-it-works-where-efficiency-is-won).

### [8:00–12:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=480) TinyML and training on the device

Models can shrink further, onto microcontrollers that cost a few dollars; the inference library must then be efficient enough for detection as well as classification. A pandemic-era demo detects masked and unmasked faces on a microcontroller with 256 kilobytes of memory. The course also covers on-device training, so that a system adapts to new sensor data locally for privacy, lower cost, customization and lifelong learning. Training costs far more than inference, since intermediate activations must be kept, gradients computed and backpropagation run. A project two years old, training on the device under 256 kilobytes, cut the memory from a few hundred megabytes to 141 kilobytes with quantization-aware scaling, sparse updates and a small training engine. In the demo a camera module learns to tell person from no person from two buttons, with no network at all.
**In this book:** [Neural Network Basics for Efficiency › 5. Counting memory](../09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md#5-counting-memory) · [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [12:00–14:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=720) Segment anything, faster

Meta's Segment Anything segments an object from a point prompt but is computationally heavy; earlier deployments extracted features offline and ran only the head in the browser. EfficientViT-SAM raises throughput 48 times on an A100 GPU with higher accuracy on his chart: the same hardware runs at 182 images per second instead of 11.
**In this book:** [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say) · [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [14:00–18:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=840) Generative models and two ways to make them cheaper

Generative models create images from text, at heavy cost: training Stable Diffusion took 150,000 GPU hours on 256 A100s, about 600,000 dollars, and generating video costs several times more per diffusion step; compute also grows with the square of the resolution. GAN Compression cuts the computation of image-to-image translation by 9 to 21 times, from about 12 to 40 frames per second. Once-for-All trains one network that contains many sub-networks: photo editing is previewed with a small sub-network and the large one runs once at the end, so a smile or younger look appears almost instantly, with computation down to 19% at hardly visible loss of quality.
**In this book:** [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say) · [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models) · [Neural Architecture Search › Step 6. Train once for many devices: once-for-all](../09-efficient-deep-learning/05-neural-architecture-search.md#step-6-train-once-for-many-devices-once-for-all).

### [18:00–25:30](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=1080) Sparse updates, parallel generation, 3D

For inpainting, adding a horse or a coconut tree to a photo, earlier methods regenerated every pixel; updating only the changed region cuts the time from 369 to 95 milliseconds. Generating large images on four GPUs naively yields four unrelated pictures, because the GPUs do not talk; overlapping communication with computation, passing stale inputs to the next step, makes generation about three times faster at the same quality. Personalization methods blend people in one image without training. The same need appears in hand-drawn sketches rendered on a tablet, in 3D generation from one image or from text, in video generation such as Sora, and in 3D vision: autonomous cars must process LiDAR point clouds, and projects from his group raise 3D perception from 5 to 47 frames per second and fuse six cameras with one LiDAR for mapless segmentation and detection on a mobile GPU.
**In this book:** [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say) · [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [25:30–28:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=1530) Language: capacity limits, and prompting

When ChatGPT launched, demand forced a limit of 50 messages every three hours. Copilot suggests code from a comment; a machine-translation model was compressed from 176 megabytes to 9 megabytes with its BLEU score kept, small enough for a phone. Large language models add zero-shot learning, where a task is described in the prompt and no model is trained for it, and few-shot learning, where a few examples are placed in the prompt; neither uses gradients or fine-tuning.
**In this book:** [Prompting and In-Context Learning › The core idea](../01-foundations/05-prompting-and-in-context-learning.md#the-core-idea) · [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say).

### [28:00–34:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=1680) The price of accuracy, chain of thought, and redundancy

These abilities are costly: a chart of zero-, one- and few-shot accuracy against model size, from 13 billion to 175 billion parameters, rises slowly, so each point of accuracy takes many more parameters and GPUs. Chain-of-thought prompting is the next emergent ability. Asked how many tennis balls Roger has after buying two cans of three, a model answers 11; asked how many of 23 eggs remain after 20 are used and 6 bought, it answers 27. Shown the first problem with the reasoning spelled out, it reasons through the second and answers 9. Accuracy on GSM8K, school maths problems, likewise needs very large models, and his lab's server, bought with 200 gigabit InfiniBand, was outdated the day it arrived. Language also carries redundancy to exploit: a review sentence can be trimmed to two words and still read as positive, and his group's SpAtten drops tokens that attend weakly to others.
**In this book:** [Reasoning in LLMs: From Chain-of-Thought to Search › The core idea](../01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md#the-core-idea) · [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say).

### [34:00–38:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=2040) Language models on the edge

Running language models locally, on laptops, in cars and robots, removes latency, network dependence and the need to send private data to the cloud. Two labs show how: quantization from 16-bit to 8-bit with SmoothQuant and to 4-bit with AWQ, activation-aware weight-only quantization. SmoothQuant began as a course project two years earlier. Its idea: activations contain outliers, large values that are hard to quantize; because matrix multiplication is linear, the scaling can be moved between weights and activations so that both are smooth and the full range is used. A further lab builds an efficient inference library, which demands real systems knowledge: C, pointers, single-instruction-multiple-data instructions, caches, locality and multi-threading. The group's TinyChat runs a 7-billion-parameter model on a very small mobile GPU inside a 3D-printed computer, and a 13-billion-parameter model on a Jetson Orin; 4-bit quantization raises its speed from 40 to 50 tokens per second to 166.
**In this book:** [Quantization › Outliers in language models: the SmoothQuant idea](../09-efficient-deep-learning/04-quantization.md#outliers-in-language-models-the-smoothquant-idea) · [Why Efficiency Matters › Worked example: a one-line budget](../09-efficient-deep-learning/01-why-efficiency-matters.md#worked-example-a-one-line-budget) · [Efficient LLM Inference and Deployment › Quantization: weight-only or weights and activations](../09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md#1-quantization-weight-only-or-weights-and-activations).

### [38:00–42:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=2280) Multimodal models

Multimodal models project image, language, audio, video and action into one space; the challenge is aligning the representations. LLaVA describes an image in words; quantized to 4 bits with naive rounding it misreads a meme, while with AWQ it describes it correctly. His group's VILA turns an image into visual tokens with a vision transformer and concatenates them with text tokens: everything can be tokenized. The course covers how such models are trained, arguing that data and training recipe matter more than architecture: visual instruction tuning alone is not enough, image-text pairs alone are not enough, interleaved images and text are needed, and the blending proportions matter.
**In this book:** [Quantization › What the practitioners say](../09-efficient-deep-learning/04-quantization.md#what-the-practitioners-say).

### [42:00–48:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=2520) What a visual language model can do, and what action costs

Videos need long contexts, since each frame takes about 200 tokens, and the course covers long-context techniques that avoid a cache growing linearly. VILA answers questions about a video, predicts what happens next, as with a blender full of strawberries, which he calls a world model, and learns a task from examples without being told it: shown pairs of city images and names, it names the next city. It can also locate a photo he took on a trip. Running such a model on a laptop is extra credit in the last lab. Actions are another output: told to bring rice chips from a jar, a model plans opening the jar, taking a chip out, placing it and closing it, though at only three updates per second, because of the computational cost and because images travel over the internet to a workstation. The costs add up elsewhere too: AlphaGo used 1,920 CPUs and 280 GPUs, and AlphaFold trained on 16 TPUv3s for a few weeks.
**In this book:** [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say).

### [48:00–50:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=2880) Three pillars and hardware trends

The second half turns to the three pillars, algorithm, hardware and data, with hardware as the driving force. The philosophy is full-stack design: the algorithm sets the demand for computing, the system supplies it, and the course closes the gap from both sides. Trends: processor frequency and single-core performance have plateaued and Moore's law is slowing, while the counts of cores and transistors keep rising, so parallel and specialized computing are the way forward. Precision keeps falling, from FP32 to FP16, INT8, FP8 and now FP4 in the newest GPUs.
**In this book:** [Why Efficiency Matters › How it works: where efficiency is won](../09-efficient-deep-learning/01-why-efficiency-matters.md#how-it-works-where-efficiency-is-won) · [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [50:00–54:45](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3000) Hardware progress, and its limits

A slide from his advisor shows single-chip inference performance improving 300 times in eight years: from scalar FP32 to FP16 and then INT8 tensor cores in the V100, to structured sparsity in the A100. Software takes a growing share of design cost at advanced nodes, and with generative models changing daily, programmability matters; the course therefore uses existing hardware well rather than designing new chips. From P100 to B100 GPUs gained about 100 times in operations per second, and memory bandwidth more than doubled from H100 to B100, since computation is cheap and data movement expensive. Power is the new bottleneck: A100s draw 400 watts, H100s and B100s 700, and a node needs about 10,000 watts, so cooling rather than space limits a data centre. A lab tour later in the course will show the server room.
**In this book:** [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say).

### [54:45–59:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3285) Memory, from cloud to microcontroller

Memory grows more slowly than compute: 80 gigabytes on A100 and H100, 192 on B100. At the edge, phone chips draw about 10 watts and reach some 50 trillion operations per second with 8 to 16 gigabytes; Apple's Neural Engine is rated at 35. Peak numbers do not translate directly into speed: data movement, memory bandwidth and utilization all matter. Mobile GPUs such as the Jetson Orin, used in many electric cars, deliver a few hundred trillion operations per second at about 60 watts with 64 gigabytes. Microcontrollers for smart-home devices run on a few hundred milliwatts with a few hundred kilobytes of SRAM and sometimes no DRAM. The gap between tens of gigabytes and hundreds of kilobytes is what smaller models must close. The goal of TinyML, as he sums it up: fewer operations, a smaller carbon footprint, less engineering effort, and training that runs automatically on less data.
**In this book:** [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say).

### [59:00–1:02:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3540) Prerequisites, and the three sections of the course

Prerequisites are enforced this year: computation structures, because the later labs need cache, locality, parallelism, pipelining and comfortable C with multi-threading, and an introduction to machine learning, since labs use PyTorch. The content has three sections: efficient inference (pruning, quantization, architecture search, distillation); efficient training (gradient compression, on-device training, federated learning, and data, model, pipeline and sequence parallelism); and application-specific optimization, above all transformers and language models, then diffusion models, video and point clouds. The key concept throughout is algorithm and system co-design, drawing on electrical engineering, computer science and AI.
**In this book:** [Why Efficiency Matters › What the practitioners say](../09-efficient-deep-learning/01-why-efficiency-matters.md#what-the-practitioners-say) · [Course Summary and Outlook › The core idea: one map, one procedure](../09-efficient-deep-learning/11-course-summary-and-outlook.md#the-core-idea-one-map-one-procedure).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=U7EPZv8Kh9w&t=3720) Labs, grading and rules

Five labs: pruning, quantization, architecture search and language-model compression on Google Colab, and a final one on each student's own laptop, with at least 8 gigabytes of memory, written in C. Each lab is 15% of the grade; an open-ended final project in groups of three or four is 25%, plus about 4% for participation. Six late days are allowed per semester without penalty.
**In this book:** not needed (course logistics).

## What to take away

- Model sizes grow far faster than GPU memory; the course's answer is to compress a trained model before deploying it, and to design algorithm and system together.
- Efficiency is what puts models on phones, microcontrollers and laptops, and it makes training on the device possible.
- Hardware gains come from parallelism, specialization and lower precision, while memory and power are the limits.
- Han's syllabus has three parts: efficient inference, efficient training and application-specific optimization.

## Sources

- Song Han, "Introduction", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=U7EPZv8Kh9w).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
