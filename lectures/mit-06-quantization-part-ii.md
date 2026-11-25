# Lecture guide: Quantization (Part II)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 6 · **Length:** 1:10:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=wrcgWm_nUeE) · **Slides:** [slides](https://www.dropbox.com/scl/fi/qt970xoje5d1btek4a8cl/Lec06-Quantization-II.pdf?rlkey=lalxz5ed2hez0olwu4e4gokbj&st=f1oof15v&dl=0)
**Chapters that cite this lecture:** [04. Quantization](../09-efficient-deep-learning/04-quantization.md)

> **In one sentence:** Song Han continues quantization: how the choice of scale granularity, range clipping and rounding makes post-training quantization work, how quantization-aware training recovers accuracy, and what binary, ternary and mixed-precision quantization add.

## Before you watch

The chapter [Quantization](../09-efficient-deep-learning/04-quantization.md) covers this lecture in its sections on post-training quantization, quantization-aware training and mixed precision. The first quantization lecture's scale and zero point are assumed; the binary and ternary part needs only the idea of bitwise XNOR.

## The lecture, part by part

### [0:00–4:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=0) Recap and plan

Quantization matters as much in the vision era as in the era of large language models, on phones, edge devices and in the cloud, and Han reports a shortage of engineers who know it. Today's plan: post-training quantization, quantization-aware training, binary and ternary quantization, and automatic mixed precision. Recapping: k-means quantization stores a codebook and 2-bit or 4-bit indices but computes in floating point, which saves storage only, still valuable for language-model inference one request at a time, where weights are the memory bottleneck; linear quantization represents weights and activations as integers with a zero point and a scale and computes in integer arithmetic.
**In this book:** [Quantization › Why this matters](../09-efficient-deep-learning/04-quantization.md#why-this-matters) · [Quantization › The core idea](../09-efficient-deep-learning/04-quantization.md#the-core-idea).

### [4:00–6:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=240) Three knobs, and granularity

Linear quantization rests on three choices, and the lecture takes them in turn: granularity, the range of values to keep, and rounding (is 1.5 rounded to 1, to 2, or at random?). As in pruning, granularity ranges from one scale for a whole tensor to one per channel and, going below 4 bits, to group quantization: per-vector scaling and the MX data types.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [6:00–8:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=360) Why one scale per tensor is not enough

One scale for the whole tensor works well for large models but degrades small ones. Plotted by channel, the ranges differ widely; a few outliers, weights far larger or smaller than the rest, force one scale on very different channels and waste the representable range. The remedy is a scale per channel.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [8:00–14:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=480) Per tensor against per channel, on the same matrix

With 2 bits and symmetric quantization, per-tensor uses the largest absolute value in the matrix, 2.12, as the scale, so 2.09 becomes 1 and −0.98 becomes 0; the reconstruction error is 2.28. Per channel takes each row's largest absolute value instead: 2.09, 2.12, 1.92 and so on, so the reconstruction is more varied and the error smaller. One entry shows the difference: −1.03 divided by 2.12 is below one half and rounds to 0, while divided by 1.92 it exceeds one half and becomes −1. The price is one more value to store per channel.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [14:00–16:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=840) Why groups: Blackwell and FP4

Lower precision needs more accurate representation and more flexibility, so the group shrinks further. The occasion is NVIDIA's Blackwell generation, far faster than Hopper, with a new FP4 tensor core: Han's slide rates FP16 and BF16 at 4.5 petaflops, INT8 and FP8 at 9, and FP4 at 18. To keep FP4 models accurate, Blackwell introduces micro tensor scaling, which is what group quantization provides: a fine-grained scale per small group.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [16:00–20:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=960) Two levels of scale

Per-vector scaled quantization gives each sub-vector its own scale on top of a global one. The global scale is a floating-point number, expensive but stored once per tensor; the per-vector scale is a cheap integer stored for every few weights; the two multiply together. With 4-bit weights and a 4-bit scale per 16 elements, the scale costs a quarter bit per weight: an effective width of 4.25 bits.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [20:00–24:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=1200) A hierarchy of scales, and the MX formats

The scales form levels: level zero per channel in FP16, negligible when a model has thousands of channels; level one per group of 16 in INT4. The MX formats go further and share exponent bits. MX4 stores each value as a sign bit and two mantissa bits, shares one exponent bit between two values and an 8-bit exponent between 16: three bits plus one half plus one half make four. MX6 has four mantissa bits, giving six, and MX9 seven, giving nine. These are the representations that make fine-grained low precision usable.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization) · [Quantization › What the practitioners say](../09-efficient-deep-learning/04-quantization.md#what-the-practitioners-say).

### [24:00–26:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=1440) Where the range comes from

The range of activations changes with the input, and the scale depends on it, so statistics must be gathered before deployment. A model trained in-house can track its minimum and maximum during training with an exponential moving average, whose discount factor says how much the latest batches count; a factor of one ignores all history. Most models are downloaded already trained, with no access to the training run, so a calibration set of images or text is run instead and its range is assumed representative.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [26:00–30:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=1560) Clipping the range

Even on a calibration set the true minimum and maximum are usually the wrong choice. Activations have a long tail of rare extreme values; keeping them spends most of the levels on empty space. Clipping the range inward gives finer steps for the bulk of values at the cost of flattening the few outliers onto the edge. For a Laplacian distribution the optimum has a closed form; real activations rarely follow one, so in practice the range is chosen to minimize the KL divergence, a measure of information lost, between the distributions before and after quantization.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [30:00–36:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=1800) Choosing the range by KL divergence

Han illustrates with activations spread from 0 to 400 but mostly below 40. Clipping the maximum near 50 merges the tail into one bin; a larger maximum represents the tail better but widens the step for the many small values. The range that minimizes the KL divergence balances the two, and for AlexNet, ResNet-152 and GoogLeNet the chosen ranges all sit below the largest observed value. NVIDIA's OCTAV finds the range automatically: mean squared error against the clipping threshold is convex, too small or too large both hurt, and with it accuracy stays close to FP32. A student's question closes the section: the bit width is fixed first, 16 levels for 4 bits, and the range is then chosen to lose as little information as possible.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [36:00–40:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=2160) Rounding

Round-to-nearest is conventional and not optimal, because weights are correlated: the best rounding for each weight alone is not the best for the tensor. Randomness helps, as it did for pruning: rounding 0.5 up or down at random. AdaRound goes further and learns a perturbation between 0 and 1, produced by a rectified sigmoid from a tensor the size of the weights and pushed toward 0 or 1 by a regularizer; the perturbation is added and the result rounded. Han sums up: zero point, granularity from per tensor to groups, MX formats, range clipping and rounding.
**In this book:** [Quantization › 3. Post-training quantization](../09-efficient-deep-learning/04-quantization.md#3-post-training-quantization).

### [40:00–42:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=2400) Not enough for small models

With these techniques large models such as GoogLeNet and ResNet keep their accuracy, but small ones such as MobileNet still lose 1 to 2% even after everything, which is too much. The answer is fine-tuning: quantization-aware training, QAT. For k-means models that meant updating the centroids; for linear quantization it is more involved.
**In this book:** [Quantization › 4. Quantization-aware training](../09-efficient-deep-learning/04-quantization.md#4-quantization-aware-training).

### [42:00–46:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=2520) Quantization-aware training

During training a full-precision copy of the weights is kept in the background, FP32 or FP16, so that very small gradient updates accumulate without being lost. In the forward pass the weights are quantized for the computation and the activations are quantized too, so that each layer sees the values it will see after deployment; the quantized values still sit in floating-point registers, hence the name fake, or simulated, quantization. Once training ends the full-precision copy is discarded. Backward is the hard part: rounding is a staircase whose gradient is zero everywhere, so nothing could be learned. The straight-through estimator simply lets the gradient pass through the rounding node as if it were the identity.
**In this book:** [Quantization › 4. Quantization-aware training](../09-efficient-deep-learning/04-quantization.md#4-quantization-aware-training).

### [46:00–48:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=2760) What QAT buys

On Han's slide quantization-aware training lifts a model whose post-training accuracy was nearly nothing, 0.1%, to 70%, and another from 59% to 70%; for models already robust, such as some NAS and MobileNet models, the gain is marginal. Large language models are too costly to train this way often, so for them the goal is post-training quantization that needs no fine-tuning, covered later in the course.
**In this book:** [Quantization › 4. Quantization-aware training](../09-efficient-deep-learning/04-quantization.md#4-quantization-aware-training).

### [48:00–52:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=2880) Binary weights

Binary quantization keeps only the sign: a positive weight becomes +1 and a negative one −1. Multiplications disappear, leaving additions and subtractions; weights take 32 times less memory and the arithmetic roughly halves. Deterministic binarization by the sign function degrades accuracy heavily, and stochastic binarization, which flips values near zero at random, needs a hardware random-number generator. On the familiar 4 by 4 matrix, signs alone cost 21 points of accuracy with an error of 9.28; multiplying by a scale equal to the mean absolute value, 1.05 here, leaves accuracy 0.2% above the baseline.
**In this book:** nothing beyond this guide; nearest: [Quantization › What each option costs and when to choose it](../09-efficient-deep-learning/04-quantization.md#what-each-option-costs-and-when-to-choose-it).

### [52:00–58:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=3120) Binary weights and activations: XNOR and popcount

Binarizing the activations too turns a dot product into bitwise operations. The XNOR of two bits is 1 when they agree and 0 otherwise, so counting the ones gives the number of agreeing pairs; the dot product equals twice that count minus n. A popcount and a shift replace multiply and add, both cheap in hardware: 32 times less memory and roughly 58 times less computation by his estimate. XNOR-Net improves accuracy, yet with both weights and activations binarized the loss remains visible; his group published an FPGA implementation that uses only these two operations.
**In this book:** nothing beyond this guide; nearest: [Quantization › What each option costs and when to choose it](../09-efficient-deep-learning/04-quantization.md#what-each-option-costs-and-when-to-choose-it).

### [58:00–1:02:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=3480) Ternary weights

Adding zero to +1 and −1 gives ternary weight networks. A threshold Δ, set empirically at 0.7 times the mean absolute value (0.73 here), splits weights into positive, zero and negative; a scale that preserves the sum of absolute values follows. Accuracy rises from 60% for binary to 65%, short of 69% at full precision. Trained ternary quantization replaces the fixed scale with two learned ones, for the positive and the negative side, and comes closer still.
**In this book:** nothing beyond this guide; nearest: [Quantization › What each option costs and when to choose it](../09-efficient-deep-learning/04-quantization.md#what-each-option-costs-and-when-to-choose-it).

### [1:02:00–1:04:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=3720) Lower is not always better

Han places the methods on one line: floating-point weights and arithmetic; k-means, integer indices with a floating-point codebook; linear quantization, integers for both weights and arithmetic, today the most used; and binary and ternary weights with bitwise operations. Lower is not always better. About 4 bits is the usual sweet spot, because memory footprint shrinks linearly with precision while the work of low-level operations shrinks faster, and memory, the expensive part, shrinks more slowly. Pushing one knob to an extreme brings diminishing returns; pruning, quantization, distillation and architecture search should be used together.
**In this book:** nothing beyond this guide; nearest: [Quantization › What each option costs and when to choose it](../09-efficient-deep-learning/04-quantization.md#what-each-option-costs-and-when-to-choose-it).

### [1:04:00–1:10:00](https://www.youtube.com/watch?v=wrcgWm_nUeE&t=3840) Mixed precision, and a summary

As with pruning, layers differ in sensitivity, so each can have its own bit width. With 1 to 8 bits for weights and for activations across n layers the space holds 64 to the n designs. HAQ, hardware-aware automated quantization, searches it with an actor-critic agent that receives measured latency and energy from the hardware as reward. Rules of thumb: cheap or memory-bound layers can stay in FP16 or FP32, compute-bound layers should go lower if they are not sensitive. The result beats uniform precision on latency against accuracy, and the same search can target model size, latency or energy. Han closes by reviewing the lecture; the next one covers architecture search, and Lab 2 is released.
**In this book:** [Quantization › 5. Mixed precision](../09-efficient-deep-learning/04-quantization.md#5-mixed-precision).

## What to take away

- One scale per tensor wastes range on outliers; per-channel scales, and below 4 bits per-group scales such as the MX formats, buy accuracy back at a small storage cost.
- Choose the range by clipping a calibration set so that as little information as possible is lost, and do not assume round-to-nearest is best.
- When post-training quantization falls short, fine-tune with fake quantization and the straight-through estimator.
- Binary and ternary weights trade accuracy for bitwise arithmetic; about 4 bits is the usual sweet spot, and the right width differs by layer.

## Sources

- Song Han, "Quantization (Part II)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=wrcgWm_nUeE).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
