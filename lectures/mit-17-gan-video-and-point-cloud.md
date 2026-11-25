# Lecture guide: GAN, Video, and Point Cloud

**Lecturer:** Song Han (MIT) · **Course:** MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024, lecture 17 · **Length:** 1:12:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=o_60Yhb79W8) · **Slides:** [slides](https://www.dropbox.com/scl/fi/6o45qs8xm20qhzkc192bv/Lec17-Efficient-GANs-Video-PointCloud.pdf?rlkey=71hrp50kjtl8zz8w7jntvbwn0&st=ywq378y5&dl=0)
**Chapters that cite this lecture:** [10. Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md)

> **In one sentence:** Song Han applies efficiency to three heavy but redundant workloads: GANs, compressed by GAN Compression, made elastic by AnyCost GAN and trainable on little data by differentiable augmentation; video, handled at 2D cost by the temporal shift module; and point clouds, processed by point-voxel and sparse point-voxel CNNs and fused with cameras in bird's-eye view.

## Before you watch

The chapter [Efficient Vision, Generative Models and Distributed Training](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) covers the GAN methods of the first half. The pruning, quantization and architecture-search lectures supply the tools that are reused here.

## The lecture, part by part

### [0:00–2:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=0) Plan

The lecture turns from general techniques to three applications that are both computationally heavy and full of redundancy: GANs with their 2D spatial redundancy, video with temporal redundancy between similar frames, and point clouds, where most of space is empty. The order: efficient GANs (GAN Compression, AnyCost GAN, differentiable augmentation), efficient video understanding with the temporal shift module, and efficient point-cloud understanding, ending with sensor fusion.
**In this book:** not needed (lecture introduction and plan of the lecture).

### [2:00–4:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=120) GANs, and why they need compression

A generative adversarial network trains two networks against each other: a generator that tries to pass its images off as real, and a discriminator that learns to tell real from fake, with one loss for each. At generation time only the generator runs, so that is the part to compress. An unconditional GAN maps random noise to an image; a conditional one conditions both networks on a label, a segmentation map or strokes, as in NVIDIA's GauGAN, which turns drawn strokes into landscapes and wants real-time speed. Generative models are heavy: MobileNet and ResNet-50 have 4 to 25 million parameters and under 4 GMACs, a BigGAN about 93 million parameters and 400 GMACs.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [4:00–8:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=240) GAN Compression

A large generator is shrunk by reducing its channels. Three losses train it: a reconstruction loss, pixel by pixel, so that a horse still turns into a zebra; a distillation loss on intermediate feature maps, with a projection where channel counts differ; and the original conditional GAN loss. As in Lab 3, a once-for-all supernetwork is trained by sampling channel counts, and an architecture search then picks the channels that fit the latency budget. The edges-to-shoes model shrinks 11 times and horse-to-zebra 21 times with comparable quality, and on a small mobile GPU horse-to-zebra rises from 12 to 40 frames per second.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [8:00–14:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=480) AnyCost GAN: elastic resolution

Image editing projects a photo into a latent space and turns knobs there, smile, hair, glasses, but generating each view is slow. Ray-tracing previewers answer with fewer samples; AnyCost GAN answers with a supernetwork: a small sub-network for quick previews and the full network for the final image, which should look the same. Resolution is made elastic first. StyleGAN shows its discriminator only the highest resolution, MSG-GAN all resolutions; AnyCost instead feeds a randomly sampled resolution at each step. It beats both in FID at low and high resolution, and its outputs change smoothly from 32 by 32 up to 1k.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [14:00–20:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=840) AnyCost GAN: elastic channels and a conditioned discriminator

Channel counts are sampled too. Outputs of different widths disagreeed, glasses vanished at half width, so a distillation loss keeps them alike. One discriminator also failed: its FID spiked for narrow generators, since a judge fit for a large generator gives a slim one poor feedback. The fix is a generator-conditioned discriminator: the generator's channels and resolution pass through a fully connected layer and modulate it. The FID then beats the baseline's, outputs are consistent across widths and resolutions, and computation falls from 100% to 19% with hardly visible loss.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [20:00–22:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=1200) Editing on a laptop

In a demo on a MacBook the original model takes 3.24 seconds per edit; the small sub-network answers almost instantly while the user adds a smile, a moustache, grey hair, and removes glasses with sliders, and the finalize button runs the full network once. The software is open source.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [22:00–26:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=1320) Why GANs fail on little data

Computation aside, GANs need data: FFHQ has 70,000 faces and ImageNet over a million images, and collection is slow and tangled in copyright. StyleGAN2 trained on 100 faces, 160 cats or 300 dogs produces poor images, and FID climbs steadily as the data shrinks to 20% and 10%. The diagnosis is the discriminator: with 20% of the data its training accuracy rises and its validation accuracy collapses. An overfitted discriminator gives the generator bad feedback, and the two are tightly coupled.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [26:00–30:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=1560) Differentiable augmentation

Augmenting only the real images, with colour jitter, shifts or cutout, makes the generator reproduce those artefacts. Augmenting real and fake images alike, but outside the graph, balances the artefacts and unbalances the training: the discriminator sees transformed images while the generator is trained without them. Differentiable augmentation applies the same transformations to both real and generated images, and to both networks, with gradients flowing through the transformation to the generator. FID then moves from 9 to 14 as data shrinks instead of 11 to 36, and StyleGAN2 with the method draws faces from 100 examples, cats from 160 and dogs from 300, with clean interpolations between scenes.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [30:00–34:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=1800) Video understanding with 2D networks

After a break, video, of which YouTube was said to receive 10 to the 5th hours a day. It needs temporal modelling: whether a hand moves left or right is known only from the sequence. Yet most pixels repeat from frame to frame. Early methods used 2D CNNs: sampling frames and averaging their scores; the two-stream network of the mid-2010s, with a spatial stream and a temporal stream over optical flow, which is slow to compute; and 2D CNNs with an LSTM fusing the outputs late, which loses low-level motion because each frame is encoded separately. 2D networks are efficient and reuse image pre-training but cannot model time.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [34:00–38:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=2040) 3D CNNs

C3D, from 2014, convolves over time as well as space and models low, middle and high-level motion jointly. I3D inflates 2D kernels pre-trained on ImageNet into 3D by repeating them along the time axis. The gain is joint modelling at every level; the cost is computation and a four-dimensional weight tensor. Han's question is whether a model can reach 3D accuracy at 2D cost.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [38:00–44:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=2280) The temporal shift module

TSM reaches 3D accuracy at 2D cost with an operation that has no arithmetic and no parameters: shifting. Part of each frame's channels is replaced by the same channels of the previous frame and part by those of the next, so a frame carries its neighbours' information, and the following 1 by 1 convolution mixes them across channels. The fraction shifted is a hyperparameter: too little brings no context, too much erases the present. Offline video understanding shifts in both directions and adds a residual connection that restores the current frame's lost channels. Online understanding, as in a car, shifts only from the past into the present and caches the shifted-out channels for the next frame, so each frame carries the whole history with diminishing weight. The implementation takes about five lines.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [44:00–48:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=2640) What TSM delivers

On Something-Something, a dataset of moving objects, TSM needs 3 times less computation than ECO and 6 times less than I3D at higher accuracy. On a 2019 embedded GPU, latency fell from 164 to 17 milliseconds per video, about 9 times, throughput rose from 6 to 77 videos per second, and accuracy improved from 41% to 43%. Watching only 10% or 40% of a video, TSM keeps its accuracy where baselines drop. In driving, a frame-by-frame detector flips a car into a tree; TSM remembers and stays stable. It runs above 20 frames per second on a phone's CPU and above 70 on a Jetson Nano GPU.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient generative models](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-generative-models).

### [48:00–52:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=2880) Scaling up, and looking inside

On the Summit supercomputer TSM doubles throughput and hardware utilization against a baseline: its batches are bound by compute, not by input and output, and its small weights communicate little, so it scales. One node took almost two days; 256 nodes took 14 minutes, 211 times faster, with the same accuracy and a batch size of 12,000, which needs a learning-rate schedule of its own. Dissecting the network, one channel responds to moving something away and another to pushing something left. The last demo navigates a map by hand gestures.
**In this book:** [Efficient Vision, Generative Models and Distributed Training › Distributed training basics](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#distributed-training-basics).

### [52:00–58:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=3120) Point clouds

From 2D to 3D: phones, cars and drones carry LiDAR, which returns a point cloud, points with x, y, z and an intensity. Where there is no object there are no points, so the data are extremely sparse, sometimes below 0.1% density, and stored irregularly, which GPUs dislike; and the models must run on headsets and cars. A voxel-based baseline divides space into a grid of cubes, whose memory grows with the cube of the resolution and still merges points that fall into one voxel, losing over 40% of them at practical memory. Its time goes to irregular memory access and dynamic kernels, and a DRAM access costs far more energy than an arithmetic operation.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [58:00–1:02:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=3480) Point-voxel CNN

PVCN has two branches. The voxel branch puts the points into a regular tensor, applies 3D convolution to aggregate neighbourhood information and gives each point the feature of its voxel; it is regular and has no irregular access. The point branch transforms each point's features on its own, as PointNet does, at full resolution. Together the voxel branch captures large surfaces, a tabletop, and the point branch thin structures, chair legs. PVCN is more than 7 times faster with higher accuracy and less memory, and an indoor segmentation demo drops from about 2 seconds to 1.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [1:02:00–1:06:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=3720) Sparse point-voxel CNN, and a 3D search

Voxelization itself loses detail. SPVCNN applies sparse convolution, computed only on non-empty voxels, so the voxel branch can run at higher resolution, while the point branch keeps small objects such as traffic signs and tree trunks. Under a latency budget, a 3D architecture search then finds the model: a once-for-all supernetwork with elastic channel counts and depth, a latency predictor that rejects candidates over budget, and an evolutionary search with mutation and crossover, which cut the search cost 17 times and lowered GPU latency and MACs.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

### [1:06:00–1:12:00](https://www.youtube.com/watch?v=o_60Yhb79W8&t=3960) BEVFusion, and a summary

Cars carry six cameras and LiDAR, and the sensors must meet in one space that every modality can enter without much loss and that suits detection and map segmentation alike. BEVFusion uses the bird's-eye view. Camera features are lifted into it by a view transformation, the critical operator, which the authors accelerated; LiDAR features are flattened along height, since no car stacks on another; the two are concatenated and encoded; and heads decode map segmentation and 3D boxes. A demo shows both on a drive. Han closes: GAN Compression, AnyCost GAN and differentiable augmentation; the temporal shift module; PVCN and SPVCNN. Diffusion models come next.
**In this book:** nothing beyond this guide; nearest: [Efficient Vision, Generative Models and Distributed Training › Efficient vision transformers](../09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md#efficient-vision-transformers).

## What to take away

- Only the generator of a GAN runs at inference, so compress it; one supernetwork can serve fast previews and a slow final image if its discriminator knows the generator's size.
- On small data the discriminator overfits; differentiable augmentation on real and fake images alike keeps its feedback honest.
- The temporal shift module buys 3D-CNN accuracy at 2D-CNN cost by moving data instead of computing.
- Point clouds are sparse and irregular: pair a regular voxel branch with a per-point branch, make the voxels sparse, and fuse sensors in bird's-eye view.

## Sources

- Song Han, "GAN, Video, and Point Cloud", MIT 6.5940 TinyML and Efficient Deep Learning Computing, Fall 2024: [video](https://www.youtube.com/watch?v=o_60Yhb79W8).
- Course page: <https://hanlab.mit.edu/courses/2024-fall-65940>.
