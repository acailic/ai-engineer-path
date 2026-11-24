# 07. TinyML: Microcontrollers and TinyEngine

**Level:** Practitioner · **Reading time:** 19 min · **Exercise:** 60 min
**Prerequisites:** [Neural Network Basics for Efficiency](02-neural-network-basics-for-efficiency.md), [Neural Architecture Search](05-neural-architecture-search.md)

> **In one sentence:** After this chapter you can check whether a model fits a microcontroller's flash and RAM before you compile anything, explain how patch-based inference and a small inference engine get it there, and name the code changes that make it run fast.

## Why this matters

A two-dollar sensor has to detect a person, a wake word or a machine fault, on a small battery, with no network. The chip is a **microcontroller** (MCU): one processor core, a few hundred kilobytes of memory, no operating system.

Han's number for the memory budget in his lecture is 320 KB. ResNet-50 does not fit, and neither do most models designed for phones (Lecture 10, [10:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=600)). You need to know how to build one that does.

## The core idea

**TinyML** is machine learning on devices with kilobytes of memory and milliwatt power budgets. A microcontroller has two kinds of memory, and they are separate budgets:

- **Flash** stores the program and the model weights. It keeps its content without power.
- **SRAM** is the working memory for values computed at run time. It is fast, small, and loses its content without power (Han, Lecture 10, [8:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=480)).

So a model fits when two conditions hold:

```
weight bytes ≤ flash          peak activation bytes ≤ SRAM
```

The second one is usually the problem. Han's contrast with a laptop (Lecture 11, [2:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=120)): one core against twenty, no GPU or neural engine, a few hundred kilobytes against tens of gigabytes. And, in his words, "there's no operating system, so you have to manage the memory by yourself".

The analogy for the whole approach is streaming a file instead of loading it: process the image piece by piece, keep only what the current piece needs in RAM. The analogy breaks on borders. Neighboring pieces depend on overlapping pixels, so some work is repeated.

## How it works, step by step

### Step 1: Budget the memory first

- **Weight bytes** = parameters × bytes per weight. An 8-bit model needs 1 byte per weight.
- **Peak activation** = the largest set of intermediate values alive at the same time, usually the input of a layer together with its output. Han's slides call this a simplified method to estimate memory usage (Lecture 10, slides 19 to 23).

Worked numbers. The first layer of MobileNetV2 at 224 × 224 pixels with 32 output channels produces 224 × 224 × 32 = 1,605,632 values. In 8-bit that is 1.5 MB, about six times the SRAM of a 256 KB chip. One layer, before anything else happens.

### Step 2: Pick a model for the chip

1. Quantize to 8-bit: weights and activations shrink four times against 32-bit floats.
2. Use depthwise-separable blocks, which need few weights.
3. Search the architecture under the memory constraint. Han's TinyNAS does this in two stages (Lecture 10, [18:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1080)): first scale the search space itself to the budget by resolution and width, then search inside it.

TinyNAS also evens out the memory profile. In the hand-designed MobileNetV2 that Han shows, the busiest layer needs 2.2 times the average; the searched model is flatter, so a larger model fits the same memory ([28:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1680)).

### Step 3: Patch-based inference

Convolutional networks are uneven. Early layers work per pixel on large maps. Later layers work per patch on small maps. The early layers set the peak.

**Patch-based inference** runs the early layers one patch of the image at a time. Peak memory then scales with the patch, not the image. The price is the **halo**: to compute a patch correctly, the engine must also read a border of pixels around it, and neighboring patches read the same border twice. Han's example: a 3 × 3 overlap of nine pixels ([38:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2280)). His MCUNetV2 reduces the price by moving the per-patch stage earlier in the network and searching the two together.

Worked numbers. Output patches of 24 × 24 pixels from a 3 × 3 convolution need an input of 24 + 3 − 1 = 26 pixels per side. That is 26 × 26 = 676 input pixels for 24 × 24 = 576 output pixels: 36% more input to read and compute.

The architecture the search found makes sense once you know this (Han, [44:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2640)): small kernels in the per-patch stage, to shrink the halo; a small expansion ratio in the middle, to cut peak memory; larger expansion later. His slides report visual wake words running under 32 KB of memory, and a double-digit accuracy gain in detection from MCUNet to MCUNetV2.

### Step 4: Run it with an inference engine

**TinyEngine** is the inference library that executes the model on the chip. MCUNet is the pairing of the search (TinyNAS) with this engine. Han separates two kinds of optimization (Lecture 11, [54:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=3240)). Pruning, quantization, search and distillation change the workload. The engine's techniques keep the mathematics identical and change only how fast it runs:

| Technique | What it does | What it saves |
|---|---|---|
| Loop reordering | visits matrix entries in an order that reuses what is in cache | memory traffic |
| Loop tiling | works on small blocks that fit in cache | memory traffic |
| Loop unrolling | repeats the loop body in code instead of looping | branch overhead; costs binary size |
| SIMD | one instruction handles several values at once | instructions |
| Im2col | turns convolution into matrix multiplication | uses the fastest kernel |
| In-place depthwise convolution | writes the output over the input | peak memory |
| Layout choice | channels-last for 1 × 1 layers, channels-first for depthwise | cache misses |
| Winograd convolution | transforms a 3 × 3 convolution to use fewer multiplications | arithmetic |

His rule for the memory hierarchy is the one from [Chapter 02](02-neural-network-basics-for-efficiency.md): registers, then cache, then memory, then storage. Each step out is slower, so stay in cache.

### Step 5: Plan memory like a compiler plans registers

The engine knows every tensor's size and lifetime before the program runs. It can give a buffer to a new tensor as soon as the old one is dead, instead of allocating a fresh one. The analogy is register allocation. The difference: buffers have different sizes, so the order of reuse decides the peak, and the planner searches for the order with the lowest maximum.

## Worked example

A memory estimator for a small network, in pure Python. It applies the two budgets from this chapter.

```python
def layer(c_in, c_out, k, size, stride=1, groups=1):
    """One 8-bit convolution. Returns (weight bytes, output size, input+output bytes)."""
    out = (size - k) // stride + 1
    weights = k * k * (c_in // groups) * c_out + c_out
    return weights, out, (c_in * size * size) + (c_out * out * out)

def whole_image(layers, c_in, size):
    weights, peak = 0, 0
    for c_out, k, stride, groups in layers:
        w, out, live = layer(c_in, c_out, k, size, stride, groups)
        weights, peak, c_in, size = weights + w, max(peak, live), c_out, out
    return weights, peak

def first_layer_per_patch(c_in, c_out, k, patch):
    """The same first layer, computed one output patch at a time."""
    tile = patch + k - 1                     # input region a patch needs, halo included
    weights, _, live = layer(c_in, c_out, k, tile)
    return weights, live

# (output channels, kernel, stride, groups), starting from a 96x96 RGB image
layers = [(16, 3, 2, 1), (32, 3, 1, 16), (32, 1, 1, 1), (64, 3, 2, 32), (64, 1, 1, 1)]

w, p = whole_image(layers, 3, 96)
print(f"whole image:    weights {w / 1024:5.1f} KB, peak SRAM {p / 1024:6.1f} KB")
_, p1 = first_layer_per_patch(3, 16, 3, 24)
print(f"first layer in 24x24 patches: peak SRAM {p1 / 1024:.1f} KB")
```

What to observe:

- Weights are about 6.5 KB. Flash is not the constraint here.
- Peak SRAM is about 127 KB. It comes from the 1 × 1 layer, where the input map and the output map are both alive. That single layer uses half the RAM of a 256 KB chip.
- Computing the first layer in 24 × 24 patches lowers its footprint from about 62 KB to 11 KB.
- The estimate is an upper bound. An engine that writes the 1 × 1 output in place would need less.

## What the practitioners say

- Han's motivation for TinyML is reach: billions of microcontroller-based devices that cost a few dollars and draw little power, which keeps data local instead of sending it to the cloud. He lists smart homes, defect detection in manufacturing, personalized healthcare and precision agriculture (Lecture 10, [2:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=120)).
- The applications on his slides go beyond images: visual wake words, tiny object detection with a larger input resolution, keyword spotting on audio, and anomaly detection. For the last one an **autoencoder**, a network trained to reconstruct its input, flags samples it reconstructs badly: error is low on normal data and high on anomalies ([60:00](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=3600)). The demo hardware is an Arduino Nano 33 BLE Sense watching a fan.
- On the engine side, his matrix multiplication example with four threads ran 4.1 times faster, and he prefers OpenMP's one-line directive over manual threads for readability (Lecture 11, [38:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=2280)). Those matter on laptops, not on a single-core microcontroller.
- The same toolkit scales up: his lab's final lab quantizes a language model to 4 bits and runs it on a laptop with the TinyChat engine ([70:00](https://www.youtube.com/watch?v=wl1UEnIOVek&t=4200)).

## Pitfalls

1. **Checking the model file and forgetting RAM.** Fix: estimate peak activation per layer before compiling.
2. **Equating fewer MACs with faster.** Depthwise layers move a lot of data per multiply. Fix: measure on the chip.
3. **Feeding a high-resolution image into the first layers.** Fix: lower the resolution, stride early, or use patch-based inference.
4. **Relying on dynamic memory allocation.** Fix: let the engine allocate static buffers at build time.
5. **Leaving activations in 32-bit floats.** Fix: quantize activations as well as weights.
6. **Measuring the model alone.** Fix: time and power-measure the sensor pipeline too; capture and preprocessing often dominate.

## Try it

Estimate, then measure.

1. Pick a board and write down its flash and SRAM sizes.
2. Quantize a small image or keyword model to 8-bit.
3. Compile it with a TinyML inference framework and its documentation.
4. Record flash used, peak RAM, latency per inference, and energy if your board can measure it.
5. Compare the two memory numbers with your own estimate from the functions above.

**You are done when** you have a table with estimate and measurement for flash, RAM and latency, and one sentence explaining any gap larger than 20%.

**Stretch:** lower the input resolution step by step until accuracy falls below your limit, and plot latency and accuracy against resolution.

## Key takeaways

- A microcontroller has two budgets: flash for weights, SRAM for activations. SRAM is usually the binding one.
- Quantize to 8-bit and search the architecture under the memory constraint.
- Early layers set the peak. Patch-based inference cuts it, at the price of a halo of repeated work.
- The engine keeps the math fixed and changes the speed: loop order, tiling, layouts, in-place operations.
- Weights are small on these devices. Count the activations.

## Self-check

1. A chip has 512 KB of flash and 256 KB of SRAM. A model has 180 KB of weights and a 300 KB peak activation. Does it fit?
2. Why do the first layers of a convolutional network set the memory peak?
3. What does patch-based inference cost?
4. Which of these change the model's output: pruning, loop unrolling, a change of memory layout, Winograd convolution?
5. Why does in-place depthwise convolution lower peak memory?
6. Why does a model with fewer MACs sometimes run slower on a microcontroller?

<details><summary>Show answers</summary>

1. No. The weights fit the flash, but the activations exceed the SRAM.
2. They work at full image resolution, so their activation maps are the largest in the network.
3. Repeated computation along patch borders, because neighboring patches need overlapping input pixels.
4. Only pruning. The other three compute the same result faster or with less memory.
5. The output is written over the input buffer, so the two never have to exist at the same time.
6. Because speed there depends on moving data, not on the number of multiplies.

</details>

## Sources

- **Lecture:** Song Han, "Lecture 10: MCUNet and TinyML", MIT 6.5940 TinyML and Efficient Deep Learning Computing (Fall 2024): [video](https://www.youtube.com/watch?v=uR1KKhIhHEk), used at [motivation](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=120), [flash and SRAM](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=480), [TinyNAS](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1080), [memory profile](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=1680), [halo](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2280), [searched design](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=2640), [anomaly detection](https://www.youtube.com/watch?v=uR1KKhIhHEk&t=3600)
- **Lecture:** Song Han, "Lecture 11: TinyEngine and Parallel Processing", MIT 6.5940 (Fall 2024): [video](https://www.youtube.com/watch?v=wl1UEnIOVek), used at [microcontroller versus laptop](https://www.youtube.com/watch?v=wl1UEnIOVek&t=120), [function-preserving optimizations](https://www.youtube.com/watch?v=wl1UEnIOVek&t=3240), [multithreading](https://www.youtube.com/watch?v=wl1UEnIOVek&t=2280), [deploying on a laptop](https://www.youtube.com/watch?v=wl1UEnIOVek&t=4200)
- **Reading:** Ji Lin, Wei-Ming Chen, Yuanyao Lin, et al., "MCUNet: Tiny Deep Learning on IoT Devices" (NeurIPS 2020): [arXiv](https://arxiv.org/abs/2007.10319)
- **Reading:** Ji Lin, Wei-Ming Chen, Han Cai, et al., "MCUNetV2: Memory-Efficient Patch-based Inference for Tiny Deep Learning" (2021): [arXiv](https://arxiv.org/abs/2110.15352)

## Next

→ [Efficient LLM Inference and Deployment](08-efficient-llm-inference-and-deployment.md), the same memory-bound reasoning applied to language models, or on to [On-Device Training](09-llm-post-training-and-on-device-training.md) to make the tiny model learn on the chip.
