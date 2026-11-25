# Lecture guide: Quantization (Part I)

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 5 · **Length:** 1:08:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=ymAzUz3qlIA) · **Slides:** [slides](https://www.dropbox.com/scl/fi/qc2s9opsa2mnqfithvwz1/Lec05-Quantization-I.pdf?rlkey=sizfzkdv85etnplz1nqgngeql&st=zr1y81q7&dl=0)
**Chapters that cite this lecture:** [04. Quantization](../09-efficient-deep-learning/04-quantization.md)

> **In one sentence:** Song Han teaches quantization: how integers and floats from FP32 down to FP4 are built, what quantization error is, and two methods in detail, k-means quantization with a codebook and linear quantization that turns a whole layer into integer arithmetic.

## Before you watch

The chapter [Quantization](../09-efficient-deep-learning/04-quantization.md) covers both lectures on quantization; this one corresponds to its sections on number formats and linear quantization. The arithmetic is worked on the slides, so pen and paper help for the two exercises and the matrix-multiplication derivation.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=0) Two ways to shrink a model

A model's size is its number of parameters times the bits per parameter. Pruning, the last two lectures, reduces the count; quantization reduces the bits, and gets two lectures. The plan: number formats (integers, FP32, FP16, FP4, INT8, INT4), the concept of quantization, then k-means and linear quantization today and binary and ternary quantization next time. The reasons: low-bit operations use far less energy than 32-bit ones, and every memory access costs hundreds of arithmetic operations, so fewer bits also mean less traffic.
**In this book:** [Quantization › The core idea](../09-efficient-deep-learning/04-quantization.md#the-core-idea).

### [2:00–4:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=120) Integers

An unsigned integer sums powers of two, one per bit. A naive signed version gives the top bit a negative weight, which leaves two encodings of zero; two's complement removes the duplicate by making the top bit worth minus 2 to the seven, for eight bits, while the rest stay positive.
**In this book:** [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [4:00–6:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=240) Fixed point and floating point

A fixed-point number puts a radix point inside the bits: integer bits above, fraction bits worth one half, one quarter and so on below. It is the same as an integer scaled by a power of two. For a larger range, the IEEE 754 32-bit float spends one bit on the sign, eight on the exponent and 23 on the fraction, also called the mantissa: minus one raised to the sign bit, times one plus the fraction, times two to the power of the stored exponent minus a bias of 127, that is two to the eight minus one, minus one.
**In this book:** [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [6:00–10:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=360) An example, and subnormal numbers

0.265625 is 1.0625 times two to the minus two, so the exponent field holds 125 and the fraction a single 1 in the fourth place. That form cannot express zero, so when the exponent field is all zeros the rule changes: the value is two raised to the power of one minus the bias, multiplied by the fraction. These are subnormal numbers, evenly spaced. The smallest positive one is two to the minus 149, the largest one minus two to the minus 23, times two to the minus 126, while the smallest normal number is two to the minus 126. Exponent fields of all ones encode plus and minus infinity, with fraction zero, or not-a-number otherwise, a wasteful case Han returns to for FP8.
**In this book:** [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [10:00–14:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=600) Fewer bits: FP16 and BF16

Han summarizes by the exponent field: neither all zeros nor all ones gives a normal number; all zeros gives zero or a subnormal; all ones gives infinity or not-a-number. Subnormals are evenly spaced and normals widen, so floats are good at large magnitudes. Formats keep shrinking. FP32 has 8 exponent and 23 fraction bits; FP16 has 5 and 10; BF16, introduced by Google, keeps FP32's 8 exponent bits and only 7 fraction bits, trading precision for the same range. When FP16 training diverges, BF16 is the usual remedy.
**In this book:** [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [14:00–20:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=840) Two exercises

The FP16 bias is two to the four minus one, or 15. A pattern with a negative sign, exponent 17 and fraction 0.75 decodes as minus 1.75 times 4, which is −7. The reverse: 2.5 is 1.25 times two to the first; in BF16 the exponent field is 1 + 127, or 128, and the fraction is 0.25, a 0 then a 1 followed by zeros.
**In this book:** [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [20:00–22:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=1200) FP8

NVIDIA's H100, the Hopper generation, brought FP8; Han notes that the chips were out of stock and even served as loan collateral, and that Blackwell brings FP4. With one sign bit, seven bits remain, and two layouts are common: E4M3, four exponent and three mantissa bits, with more precision and less range, and E5M2, five and two, with more range and less precision, which suits gradients in the backward pass.
**In this book:** [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [22:00–28:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=1320) Four ways to spend four bits

With four bits the allocation matters more. All mantissa and no exponent is INT4, the integers from −8 to 7, evenly spaced. E1M2 gives 0, 0.5, 1 and so on up to 3.5: INT4 scaled by one half, with one slot wasted on a second zero, so 15 distinct values. E2M1 reaches 0, 0.5, 1, 1.5, 2, 3, 4 and 6: a wider range, coarser steps. E3M0 is pure powers of two, up to 16 with a bias of three, the widest range and no precision in between.
**In this book:** [Quantization › 1. Know the number formats](../09-efficient-deep-learning/04-quantization.md#1-know-the-number-formats).

### [28:00–30:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=1680) What quantization is

Quantization constrains an input from a continuous range of values to a small number of discrete levels: a signal snapped to the nearest of a few levels, an image reduced to 16 colours. The gap between a value and its snapped version is the quantization error, which the methods try to minimize. The first method, k-means quantization, stores a codebook of allowed values and, per weight, only its index into that book.
**In this book:** [Quantization › The core idea](../09-efficient-deep-learning/04-quantization.md#the-core-idea).

### [30:00–36:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=1800) K-means quantization, by example

On a 4 by 4 weight matrix in FP32, values near 2, such as 2.09 and 1.92, get one colour, values near −1 another; each colour is a centroid. A weight is stored as the index of its centroid, two bits for four centroids, and reconstruction looks the index up; the difference from the original is the quantization error. Storage: 16 weights at 32 bits are 64 bytes; after quantization 16 two-bit indices are 4 bytes and the four-entry FP32 codebook 16 bytes, 20 bytes in all, 3.2 times smaller. In general, with n bits and M weights, far more than there are centroids, the size falls from 32M bits to about nM, a compression of 32 over n: 16 times at two bits, 8 times at four.
**In this book:** [Quantization › 2. Linear quantization: map reals to integers](../09-efficient-deep-learning/04-quantization.md#2-linear-quantization-map-reals-to-integers).

### [36:00–40:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=2160) Fine-tuning the codebook, and combining with pruning

To fine-tune, the gradient of each weight inherits the weight's colour; gradients of one colour are summed, and the sum, times the learning rate, is taken off that centroid, one stochastic-gradient step per centroid. Quantization alone keeps accuracy until the model shrinks to about a tenth, then drops quickly; pruning followed by quantization keeps it at a few percent of the size. Students ask why sum rather than average (many weights nudge one centroid; the learning rate absorbs the scale; try both) and which comes first: prune first, so that fewer weights need quantizing. The weight distribution after pruning peaks at zero and after quantization becomes a handful of spikes.
**In this book:** [Quantization › 2. Linear quantization: map reals to integers](../09-efficient-deep-learning/04-quantization.md#2-linear-quantization-map-reals-to-integers) · [Quantization › What the practitioners say](../09-efficient-deep-learning/04-quantization.md#what-the-practitioners-say).

### [40:00–44:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=2400) More questions

Quantization alone in preference to pruning? Han sees no case except hardware without a low-precision unit; coarse-grained pruning runs on any hardware, so combine the two. Can a weight change colour during fine-tuning? Yes, when an update moves it nearer another centroid; Lab 2 implements this. After a few iterations the centroids themselves shift slightly, as his before-and-after slides show.
**In this book:** [Quantization › 2. Linear quantization: map reals to integers](../09-efficient-deep-learning/04-quantization.md#2-linear-quantization-map-reals-to-integers).

### [44:00–48:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=2640) How many bits, Huffman coding, Deep Compression

In practice convolution layers keep accuracy down to 4 bits and fully connected layers to 2, and 4 bits suffice for today's language models. Deep Compression adds Huffman coding: since some centroids occur far more often than others, frequent ones get short codes and rare ones long ones. The pipeline prunes, quantizes with k-means and retrains the codebook, then encodes, and compresses networks 35 to 49 times, SqueezeNet included, from 4.8 megabytes to 0.47. The number of centroids is a hyperparameter, found where accuracy starts to fall. K-means saves storage but not computation, since indices are decoded and everything else runs in floating point; for a single user generating text, which is bound by memory, four times less memory than FP16 still helps greatly.
**In this book:** [Quantization › What the practitioners say](../09-efficient-deep-learning/04-quantization.md#what-the-practitioners-say).

### [48:00–54:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=2880) Linear quantization

After a break, linear quantization, the kind a phone most likely runs: integer weights and integer arithmetic, so both storage and computation shrink. The same 4 by 4 matrix becomes small integers, 2.09 as 1 and −0.98 as −2. Two parameters connect the two: a zero point and a scale, with the real value equal to the scale times the integer minus the zero point. The zero point lets zero be represented exactly; the scale maps the integer range, fixed by the bit width (−2 to 1 for two bits, −4 to 3 for three), onto the real range of the weights: the scale is r_max − r_min over q_max − q_min, 1.07 here, and the zero point is computed from it and rounded to an integer, −1 here. Reconstruction gives 2.14 and −1.07.
**In this book:** [Quantization › 2. Linear quantization: map reals to integers](../09-efficient-deep-learning/04-quantization.md#2-linear-quantization-map-reals-to-integers).

### [54:00–1:02:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=3240) Matrix multiplication with integers only

Han then derives integer-only matrix multiplication, to be implemented in Lab 2. Substitute scale times integer minus zero point for weights, activations and output in y = Wx and four terms appear. Multiplications run in n-bit integers and accumulation in 32 bits to avoid overflow. The ratio of scales s_w s_x over s_y, empirically between 0 and 1, splits into a power of two and a fixed-point factor between 0.5 and 1, so a fixed-point multiply and a shift replace floating point. Weights are roughly symmetric around zero, so their zero point can be set to zero and a term disappears. For the bias, its zero point is set to zero and its scale forced to equal s_w s_x, so the bias folds into a pre-computed integer. What remains at run time is integer multiply-accumulate; convolution follows the same derivation.
**In this book:** [Quantization › 2. Linear quantization: map reals to integers](../09-efficient-deep-learning/04-quantization.md#2-linear-quantization-map-reals-to-integers).

### [1:02:00–1:04:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=3720) The resulting pipeline

The computation graph: quantized weights and activations enter an integer convolution, accumulate in a 32-bit register, receive the bias, are scaled, and get the zero point added back to give a quantized output. Unlike k-means, this saves computation as well as storage. Asked about ReLU, Han answers that with a zero zero point half the integer range goes unused.
**In this book:** [Quantization › 2. Linear quantization: map reals to integers](../09-efficient-deep-learning/04-quantization.md#2-linear-quantization-map-reals-to-integers).

### [1:04:00–1:08:00](https://www.youtube.com/watch?v=ymAzUz3qlIA&t=3840) Results, and what comes next

Against floating point, 8-bit integer models sit consistently better on latency against accuracy for ResNet-50 and Inception v3. 8-bit quantization is mature, most hardware has integer units for it, and it is the standard way to compress and speed up networks on phones, microcontrollers and edge devices. Binary and ternary quantization follow in the next lecture. Han closes by reviewing the number formats and the two methods.
**In this book:** [Quantization › What the practitioners say](../09-efficient-deep-learning/04-quantization.md#what-the-practitioners-say).

## What to take away

- A model's size is parameters times bits: pruning cuts the first, quantization the second, and the two combine.
- In a float, exponent bits buy range and mantissa bits precision; FP8 and FP4 force a choice between the two.
- K-means quantization stores codebook indices and saves only memory; linear quantization with a scale and a zero point also saves computation.
- With weights and biases treated as symmetric and the scale ratio split into a shift and a fixed-point factor, a whole layer runs in integers.

## Sources

- Song Han, "Quantization (Part I)", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=ymAzUz3qlIA).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
