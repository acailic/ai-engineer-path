# Lecture guide: Knowledge Distillation

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 9 · **Length:** 1:00:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=Ubj3QXv4rjw) · **Slides:** [slides](https://www.dropbox.com/scl/fi/fjgnue7z3mi1ynxbd0y5k/Lec09-Knowledge-Distillation.pdf?rlkey=cup1qhlpx3vx0nrs7wuwj6m0d&st=jzhogqwp&dl=0)
**Chapters that cite this lecture:** [06. Knowledge Distillation](../09-efficient-deep-learning/06-knowledge-distillation.md)

> **In one sentence:** Song Han teaches knowledge distillation, training a small student to match a large teacher: what to match and at what temperature, how to distill without a trained teacher, how the idea extends from classifiers to detectors, GANs and language models, and why tiny models need network augmentation rather than data augmentation.

## Before you watch

The chapter [Knowledge Distillation](../09-efficient-deep-learning/06-knowledge-distillation.md) follows this lecture section by section. Nothing beyond the loss functions of a classifier (softmax, cross-entropy, KL divergence) is assumed.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=0) Why distill

Knowledge distillation follows pruning, quantization and architecture search as a fourth way to efficient models. Memory is scarce everywhere: cloud GPUs have 80 or 100 gigabytes or so, microcontrollers a couple of hundred kilobytes. So ResNets and ViTs run in the cloud while MCUNet and MobileNetV2-tiny run on tiny devices, and the question is how to train the small ones to approach the large ones. Even in the cloud it matters, since language models keep growing.
**In this book:** [Knowledge Distillation › Why this matters](../09-efficient-deep-learning/06-knowledge-distillation.md#why-this-matters).

### [2:00–4:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=120) Teacher, student, and a second loss

Distilling a 70-billion-parameter model into a 7-billion one would cut the memory traffic for the weights ten times. A large teacher and a small student receive the same input; say Llama 2 70B and a 7B model. Trained alone their accuracies differ greatly, 82% against 52% in his example. When training the student, its usual classification loss is joined by a distillation loss between the teacher's logits and the student's, so that the student learns to match the teacher.
**In this book:** [Knowledge Distillation › The core idea](../09-efficient-deep-learning/06-knowledge-distillation.md#the-core-idea).

### [4:00–6:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=240) What the cross-entropy misses

Given a cat, a teacher's logits for cat and dog might be 5 and 1, which after the softmax are 98% and 1.7%; the student's 3 and 2 become 73% and 26%. Both classify correctly, so the cross-entropy loss against the label is zero, yet the teacher is far more certain. Matching the predicted probabilities supplies exactly the signal that the label does not.
**In this book:** [Knowledge Distillation › The core idea](../09-efficient-deep-learning/06-knowledge-distillation.md#the-core-idea).

### [6:00–8:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=360) Temperature

The softmax turns logits into probabilities, exponentiating each and dividing by the sum. A temperature T divides the logits before that step: T = 1 is the usual case, and a higher temperature smooths the distribution, turning 98% and 1.7% into something like 60% and 40%. The goal of distillation is to align the class probabilities of teacher and student.
**In this book:** [Knowledge Distillation › 1. The loss](../09-efficient-deep-learning/06-knowledge-distillation.md#1-the-loss).

### [8:00–12:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=480) What to match: outputs and weights

Many tensors can be matched. Output logits: a cross-entropy between the two distributions or a plain squared difference. Intermediate weights: the teacher's tensors are larger than the student's, so a learned projection, a 1 by 1 convolution or fully connected layer, maps the student's smaller tensor to the teacher's size, and the match is made after it; a student suggests low-rank approximation, another option Han notes.
**In this book:** [Knowledge Distillation › 3. What to match](../09-efficient-deep-learning/06-knowledge-distillation.md#3-what-to-match).

### [12:00–16:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=720) Features and gradients

Intermediate features: teacher and student should resemble each other layer by layer, not only at the output. Gradients: backpropagation computes both weight gradients and activation gradients, so the latter can be matched instead. Han backpropagates to the input: the resulting map, the derivative of the loss with respect to each pixel, is large where a small change would alter the decision, as on the nose and eyes in his picture. Since teacher and student share the input, these maps have the same size and compare directly; networks of one family that both score above 70% have similar maps, and a weaker one, at 62%, has a different map.
**In this book:** [Knowledge Distillation › 3. What to match](../09-efficient-deep-learning/06-knowledge-distillation.md#3-what-to-match).

### [16:00–20:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=960) Sparsity and relations inside the network

Sparsity patterns can be matched too: after a ReLU, the set of neurons that stay active. Relational knowledge goes one step further and matches two tensors at once. A teacher with 32 layers and a student with 14 layers both have three stages; within a stage, the relation between a module's input and its output can be summarized, after reducing the spatial dimension, as a matrix of input channels by output channels, whatever the counts, and that relation is matched.
**In this book:** nothing beyond this guide; nearest: [Knowledge Distillation › 3. What to match](../09-efficient-deep-learning/06-knowledge-distillation.md#3-what-to-match).

### [20:00–22:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=1200) Relations across samples

The same idea applies across inputs. For three pictures of birds, ordinary distillation matches each teacher embedding to its student embedding independently. Relational distillation also matches the geometry between samples: if the second teacher embedding lies to the right of the first, so should the second student embedding. With n samples there are n × (n − 1) / 2 pairwise distances to compare. Han suggests trying this when compressing language or vision-language models.
**In this book:** nothing beyond this guide; nearest: [Knowledge Distillation › 3. What to match](../09-efficient-deep-learning/06-knowledge-distillation.md#3-what-to-match).

### [22:00–27:30](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=1320) Born-Again Networks

All of this presumes a trained teacher, and training a 70-billion-parameter teacher is expensive. Self-distillation avoids it. Born-Again Networks iterates: step 0 trains a network with the classification loss alone; each later step trains a network of the same architecture with the classification loss plus a distillation loss from the previous step; and because all steps share an architecture, their predictions can be ensembled at the end.
**In this book:** [Knowledge Distillation › 4. No teacher needed: self and online distillation](../09-efficient-deep-learning/06-knowledge-distillation.md#4-no-teacher-needed-self-and-online-distillation).

### [27:30–30:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=1650) Online distillation: deep mutual learning

Online distillation trains teacher and student together from scratch. In deep mutual learning two networks of the same size sit side by side: while one is trained, with its cross-entropy loss against the labels, the other serves as teacher through the KL-divergence distillation term; then the roles swap. Neither needs pre-training, and neither needs to be larger. On CIFAR-10 and CIFAR-100 both networks improve over independent training.
**In this book:** [Knowledge Distillation › 4. No teacher needed: self and online distillation](../09-efficient-deep-learning/06-knowledge-distillation.md#4-no-teacher-needed-self-and-online-distillation).

### [30:00–32:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=1800) Be your own teacher

A combined scheme, Be Your Own Teacher, keeps one copy of weights instead of two, which halves the GPU memory. The deeper layers of a network supervise its shallower layers, on the reasoning that later predictions are more reliable.
**In this book:** [Knowledge Distillation › 4. No teacher needed: self and online distillation](../09-efficient-deep-learning/06-knowledge-distillation.md#4-no-teacher-needed-self-and-online-distillation).

### [32:00–36:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=1920) Object detection

First, a side effect of Be Your Own Teacher: the intermediate classifiers sometimes beat the baseline on their own, so inference may exit early once confidence is high enough. Then, after a break, distillation for other tasks. Object detection predicts a class and a location. Features are matched with a 1 by 1 convolution to align shapes, and the classification loss is weighted so that foreground must match closely while background may differ. For the bounding box, the distillation loss applies only when the student's error exceeds the teacher's by a margin; a teacher that is no better than the student should not teach.
**In this book:** [Knowledge Distillation › 5. Beyond classification](../09-efficient-deep-learning/06-knowledge-distillation.md#5-beyond-classification).

### [36:00–38:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=2160) Localization distillation

Box regression can be turned into classification: divide each axis into bins, six on each axis for 36 classes in his example, and treat the bin holding the predicted coordinate as its class. Cross-entropy then supervises the location, and the teacher's distribution over bins can be distilled like any class distribution.
**In this book:** [Knowledge Distillation › 5. Beyond classification](../09-efficient-deep-learning/06-knowledge-distillation.md#5-beyond-classification).

### [38:00–44:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=2280) Segmentation and GAN compression

For semantic segmentation, a label per pixel, a discriminator is added: the student must produce embeddings that the discriminator cannot tell from the teacher's. GAN Compression distills image-to-image models with three losses, on intermediate features, on reconstruction and on a conditional GAN term. On a small mobile GPU the horse-to-zebra model went from 56.8 to 3.5 GFLOPs, from 12 to 40 frames per second, with a better FID, 53 against 61.5; an edges-to-shoes model on a Jetson Nano rose from 1.6 to 3.9 frames per second, enough to make drawing interactive.
**In this book:** nothing beyond this guide; nearest: [Knowledge Distillation › 5. Beyond classification](../09-efficient-deep-learning/06-knowledge-distillation.md#5-beyond-classification).

### [44:00–48:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=2640) Language models

For transformers, distillation can also match the N by N attention maps: with attention transfer the student's maps resemble the teacher's, without it they do not. Han then sketches a pipeline for compressing large language models that combines pruning with distillation: the student is a pruned copy of the teacher, chosen by ranking the importance of components, then retrained with the full model as teacher; the pipeline around it also uses synthetic pre-training data and instruction data generated in part by a 400-billion-parameter Llama model. He reports students trained with far fewer tokens than training from scratch at comparable accuracy.
**In this book:** nothing beyond this guide; nearest: [Knowledge Distillation › 5. Beyond classification](../09-efficient-deep-learning/06-knowledge-distillation.md#5-beyond-classification).

### [48:00–51:35](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=2880) Regularization that helps large models hurts small ones

To improve small models in another way, consider data augmentation and dropout. Cutout removes part of an image, mixup adds two images pixel by pixel and averages their labels, AutoAugment searches policies; dropout zeroes random neurons, and variants remove channels or blocks. For ResNet-50 these lift accuracy from 76.5% toward 78%. For tiny models every one of them lowered accuracy, and the more was added, the lower it went.
**In this book:** [Knowledge Distillation › 6. Tiny models need different regularization](../09-efficient-deep-learning/06-knowledge-distillation.md#6-tiny-models-need-different-regularization).

### [51:35–56:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=3095) Network augmentation

Han's reading: large models overfit and need more data or dropout; tiny models underfit, lacking capacity. So instead of augmenting the data, augment the model during training. Network augmentation wraps the small model in a larger one, wider by a few channels or deeper, whose inner part shares the small model's weights; its loss adds extra supervision to the small model's own, and different widths are sampled at different steps. The deployed model is still the small one, and its accuracy rose; for large models the method did not help, as expected. It combines with distillation, and it transferred better than training four times longer.
**In this book:** [Knowledge Distillation › 6. Tiny models need different regularization](../09-efficient-deep-learning/06-knowledge-distillation.md#6-tiny-models-need-different-regularization).

### [56:00–1:00:00](https://www.youtube.com/watch?v=Ubj3QXv4rjw&t=3360) Detection, and a summary

Network augmentation also raised detection accuracy on VOC and COCO at the same computation. Its limit is that it was tried on vision tasks before ChatGPT; Han invites students to try it on small language models. He sums up: distillation needs a teacher and a student, though self and online variants remove the separate teacher; outputs, features, weights or gradients can be matched; and the method extends to detection, segmentation, GANs and language. The next lecture is MCUNet, co-design for microcontrollers.
**In this book:** [Knowledge Distillation › 6. Tiny models need different regularization](../09-efficient-deep-learning/06-knowledge-distillation.md#6-tiny-models-need-different-regularization) · [Knowledge Distillation › What the practitioners say](../09-efficient-deep-learning/06-knowledge-distillation.md#what-the-practitioners-say).

## What to take away

- Distillation adds the teacher's confidence to the labels: match softened probabilities, and optionally features, weights, gradients or relations.
- A separate trained teacher is optional: networks of one size can teach each other, or deeper layers can teach shallower ones.
- Distillation adapts to any task with a signal to match, from boxes to attention maps.
- Large models overfit and tiny models underfit: augment data for the first, augment the network for the second.

## Sources

- Song Han, "Knowledge Distillation", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=Ubj3QXv4rjw).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
