# Lecture guide: On-Device Training and Transfer Learning

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 21 · **Length:** 1:06:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=1YuD_5UQxsA) · **Slides:** [slides](https://www.dropbox.com/scl/fi/35992g5bz2sa1hxo3dmn6/Lec21-On-Device-Training-And-Transfer-Learning.pdf?rlkey=yqym2zffstfrdsui371lkvael&st=sqmt0oro&dl=0)
**Chapters that cite this lecture:** [09. LLM Post-Training and On-Device Training](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md)

> **In one sentence:** Song Han shows that gradients can leak training data, so learning should happen on the device, and then makes that possible: TinyTL trains biases and a small residual branch, sparse back-propagation updates only the layers that matter, quantization-aware scaling repairs 8-bit training, and PockEngine compiles the whole thing to run in 256 kilobytes.

## Before you watch

The chapter [LLM Post-Training and On-Device Training](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) follows this lecture in its section on training on the device. The pruning and quantization lectures supply the tools that are reused here.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=0) Why learn on the device

Phones, cars and sensors collect new and sensitive data, images and text that users would rather keep; training should then happen on the laptop, the phone or a Jetson, not in the cloud. Training needs far more memory and computation than inference. The plan: why gradients are not safe to share, the memory bottleneck, TinyTL, sparse back-propagation, quantized training with quantization-aware scaling, and PockEngine, a tiny training engine.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [2:00–4:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=120) Federated learning, and its open question

In federated learning each device trains locally for a few iterations, sends the updated model to a server, and the server averages the models and sends the result to all devices, so that a word typed by one user helps the others while the data never leave the device. But the difference between the old and the new model is the gradient, and it is shared openly. Is that safe?
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [4:00–8:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=240) Deep leakage from gradients

Earlier attacks on a shared gradient infer membership of a record or properties of a sample. Deep leakage goes further and recovers the data. Given the same model, the attacker starts from a random dummy input and a dummy label, runs a forward and a backward pass, and compares the resulting gradient with the shared one. The squared difference of the gradients is itself backpropagated, into the dummy input and the dummy label. As the dummy gradient approaches the real one, the dummy image turns into the real image.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [8:00–12:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=480) Images, text, and a failed defence

The demo starts as noise and resolves into the training image. A batch of seven is recovered too, in a different order but with the right content. For BERT's masked language modelling, masked tokens are recovered word by word and the sentence, taken from the NeurIPS website, is exact after 30 iterations. Adding Gaussian noise to the gradient hides the data only when the noise is so strong that the model's accuracy collapses.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [12:00–16:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=720) A defence that costs nothing

Gradient pruning from the previous lecture also defends. Prune 99% of the gradients and the top-1 accuracy stays, while the leak disappears beyond about 70% pruned: with one percent of the gradient to match, the attack has many unknowns and few equations. Han notes that deep leakage takes about 20 lines of PyTorch, and that the code and demonstrations are public on the lab's website.
**In this book:** nothing beyond this guide; nearest: [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [16:00–20:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=960) The memory bottleneck

Since gradients are unsafe, everything stays on the device, where memory is four to six orders of magnitude smaller than in the cloud. Training keeps the activations of every layer for the backward pass, and they grow with the batch size; checkpointing recomputes them, trading compute for memory. Moving from ResNet-50 to MobileNetV2 cuts parameters four times but the peak activation only by a tenth. Parameter-efficient fine-tuning helps little: updating only the last layer has 13 times fewer trainable parameters but drops accuracy on Cars from 90% to 50%, and updating only the batch-normalization layers has 12 times fewer and does better.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [20:00–26:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=1200) TinyTL: fewer parameters is not less memory

Updating weights needs the activations; updating biases does not. But 12 times fewer trainable parameters gave under 2 times less measured memory, so parameter efficiency is not memory efficiency. Bias-only updates save memory 12 times and lose 16% accuracy. TinyTL adds capacity back with a light residual branch next to the frozen block: half the resolution, one sixth of the channels, grouped convolutions and no inverted bottleneck, so it takes 4% of the activation size and 5 megabytes more. That buys 11% accuracy, closes the gap to the full update at the memory cost of last-layer training, and beats activation pruning. Memory falls 6.5 times on Flowers and about 4.5 times on Cars and Food, from about 300 megabytes to 60, which fits in a cache.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [26:00–30:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=1560) Sparse back-propagation

The brain learns most when its synapses are fewest: 2,500 per neuron at birth, 15,000 at two to four years, down to 7,000 in adolescence. Sparse back-propagation borrows the idea. Between a full update and a last-layer or bias-only update, it updates some layers and not others, and inside an updated layer only some channels, and it never backpropagates into the early feature extractors. If a quarter of a layer's weight gradient is needed, only a quarter of its activations is stored.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [30:00–34:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=1800) Which layers to update

Memory over depth is U-shaped: early layers have large activations because the resolution is high, late layers have many channels and large weights, so middle layers are cheapest. To choose, a contribution analysis fine-tunes one layer at a time and measures the gain in accuracy, as the sensitivity analysis did for pruning. Early layers give nothing or hurt; one late layer alone adds 14%. In MobileNet the gains zigzag: pointwise convolutions matter, depthwise ones do not, and the first pointwise layer of a block is also the cheaper to update. In BERT the query, key and value projections and the first feed-forward layer matter, the output projection and the second feed-forward layer do not.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [34:00–38:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=2040) Searching the update scheme

The analysis runs on one dataset, with whole layers, halves, quarters and eighths of channels, and transfers to others. An evolutionary search then picks the scheme: how many biases to update, how deep the bias updates reach, which layer's weights to update and what fraction of its channels, maximizing the summed accuracy gains under a memory budget; it beats random search. Across DistilBERT, BERT on GLUE, MCUNet, MobileNetV2 and ResNet-50, sparse back-propagation matches full back-propagation at several times less memory.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [38:00–42:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=2280) Adapting a language model on a device

With PockEngine, Llama 2 7B is fine-tuned on the Stanford Alpaca data on a device: half the latency of PyTorch, less memory, the same loss, a competitive win rate and the MT-Bench score kept. Against LoRA of rank 8, sparse back-propagation reaches the same accuracy, and both match full fine-tuning. In Han's examples the adapted model names Washington as the capital where the base model said Washington DC, and gives Michael Jackson's last album. Reversing the words of a sentence is where the sparse update fails once; on a multi-step arithmetic question it answers correctly but with a longer chain of thought than the full update.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [42:00–46:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=2520) Fake and real quantized training

After a break: training at low precision. In fake quantization, used for quantization-aware training, weights and activations are rounded to a low-precision grid but every arithmetic operation still runs in FP32, so no memory is saved. A real quantized graph keeps weights and activations in INT8 or INT4 and accumulates in INT32. It saves memory but, averaged over ten datasets, INT8 training loses about 10% top-1 accuracy. The diagnosis looks at the ratio of weight to gradient: in INT8 it is about ten times larger than in FP32, so the gradient is too small to move the weight.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [46:00–52:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=2760) Quantization-aware scaling

A per-channel scale s_w maps the integer range of −128 to 127 onto weights that lie around zero, so s_w is much smaller than one. By the chain rule the integer weight equals the real weight divided by s_w and the integer gradient equals the real gradient times s_w, so the integer weight-to-gradient ratio carries a factor of one over s_w squared, which is large. The fix, quantization-aware scaling, multiplies the gradient by that factor, one factor from the scale and one from the chain rule, for the weight and likewise for the bias, whose scale differs. This replaces a per-layer tuning of the learning rate that would be hard in practice. With it, the weight-to-gradient ratio, the training and validation loss and the accuracy of INT8 training match FP32, and the 12-point loss is recovered.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [52:00–56:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=3120) Training in 256 kilobytes, and a demo

Combined, the techniques fit on-device training under 256 kilobytes of SRAM: against PyTorch, PockEngine saves 7 times, quantization-aware scaling 2 times, the sparse update 8 times and operator reordering a further 2.4 times, from over 100 megabytes to 141 kilobytes. In a demo, an OpenMV camera board with an STM32 microcontroller and two buttons learns to tell person from no person with a few button presses, and works on people in the room. The code is open source as TinyTraining.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [56:00–1:00:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=3360) PockEngine: differentiation at compile time

Algorithms alone give no measured speed-up; that needs a system. Conventional training libraries build the backward graph by automatic differentiation at run time, for flexibility. PockEngine differentiates at compile time: compilation is slower and runs once, the run-time engine is thin, and a static graph can be optimized thoroughly. Its pipeline traces the PyTorch model into a forward representation, derives a backward representation, in which one convolution becomes three, one for the forward pass and two for gradients, and then optimizes the graph: operators that need no gradient are removed, operators are reordered and updated in place to save memory, and constants are folded and dead code eliminated.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

### [1:00:00–1:06:00](https://www.youtube.com/watch?v=1YuD_5UQxsA&t=3600) Results across devices, and a summary

Each kernel's schedule is then tuned with its dimensions known, which in Han's statement makes the result two to three times faster and smaller than TensorFlow Lite, and code is generated for the device: an STM32 microcontroller, a Raspberry Pi, phones and more, with PyTorch and TensorFlow as front ends. On a Jetson Orin Nano, MCUNet, MobileNetV2, BERT and Llama 2 7B train 2 to 4 times faster than with existing frameworks; on ARM CPUs in a Raspberry Pi and a phone, 13 to 21 times faster than PyTorch or TensorFlow, whose training kernels were little optimized. On Apple M1 and M2 chips the training graph compiles to Metal where the standard frameworks ran poorly. PockEngine also reaches DSPs and microcontrollers, so that frameworks built for inference alone can train. Han recaps the lecture: gradients leak, activations are the bottleneck, and four remedies make training fit a device.
**In this book:** [LLM Post-Training and On-Device Training › Training on the device](../09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md#training-on-the-device).

## What to take away

- A shared gradient can be turned back into the training data; pruning the gradient hides it at no cost, or keep training on the device.
- Memory, not parameter count, is what matters: update biases and a light residual branch, or only the layers that a contribution analysis finds useful.
- Real low-precision training converges badly until the gradient is rescaled by the square of the quantization scale.
- Compilation turns these algorithmic savings into measured ones, down to 256 kilobytes of memory.

## Sources

- Song Han, "On-Device Training and Transfer Learning", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=1YuD_5UQxsA).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
