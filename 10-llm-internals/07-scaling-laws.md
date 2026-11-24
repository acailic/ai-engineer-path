# 07. Scaling Laws

**Level:** Professional · **Reading time:** 16 min · **Exercise:** 60 min
**Prerequisites:** [Resource Accounting](02-resource-accounting-flops-memory-and-arithmetic-intensity.md), for the 6·N·D FLOP count, and [Transformer Architectures and Hyperparameters](03-transformer-architectures-and-hyperparameters.md), for aspect ratio.

> **In one sentence:** After this chapter you can fit a scaling law on small training runs, use it to choose model size, token count and batch size for a large run, and name the places where the method is fragile.

## Why this matters

A friend lends you 10,000 B200 GPUs for a month and asks for a good open model. Your training infrastructure works and your dataset is ready. Now: how many parameters, how many tokens, which learning rate, which batch size?

Tuning those on the real run is impossible. You get one shot, and it costs millions. So you need a way to make the decisions on runs that cost a thousand times less, and trust that the answers carry over. That is what a scaling law is for.

## The core idea

A **scaling law** is a simple formula that predicts a model's loss from a resource: data, parameters or compute. **Loss** is the model's error on held-out text, the number that training pushes down.

For data, the empirical finding is that loss falls as a power of the dataset size:

`L(n) = a · n^(−α) + c`

Here `n` is the number of tokens, `a` and `α` set the curve, and `c` is a floor the loss never passes. On a plot with logarithmic axes, a power law is a straight line. Tatsu Hashimoto's Lecture 9 opens with the history: the idea goes back to work at Bell Labs in 1993 on how error falls with dataset size ([4:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=240), [6:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=360)).

Where the line comes from is less settled. His example is estimating the mean of a set of numbers: the squared error of the average is `σ²/n`, which is a scaling law with slope −1. Classical models all give that slope. Neural networks give much shallower ones: the fitted exponents he shows are about −0.1, −0.3 and −0.1 ([16:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=960)). One mental model: estimating an arbitrary smooth function in d dimensions, without assumptions, gives an error of about `n^(−1/d)`, so a slope of −0.1 is what a non-parametric estimator in ten dimensions would show ([18:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=1080)). His own verdict on that argument is reserved. He does not know how much he buys it, and some of the evidence relies on estimators of intrinsic dimension ([20:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=1200)).

The analogy to a mean estimate breaks in one more place: the formula is an observation, not a guarantee. It can stop holding when conditions change.

## How it works, step by step

### 1. Write the budget

A training run's compute is `C = 6 · N · D`, where N is the parameter count and D is the number of training tokens. A fixed budget allows many pairs of N and D. The scaling question is which pair.

### 2. Pick a method for the trade-off

| Method | What you do | Chinchilla's answer | Main weakness |
|---|---|---|---|
| Lower envelope | Take the best loss reached at each compute level across all runs, then read off the model sizes | 67B | The envelope is hard to define |
| IsoFLOP | Fix a few budgets. At each, train several sizes and take the best | 63B | Many runs per budget |
| Parametric fit | Fit a formula for loss as a function of both N and D | Not given; its fitted exponents (0.46 and 0.54) differ slightly from the other two methods' (about 0.50 and 0.50) | Depends on the formula you assume, and on how you fit it |

An **IsoFLOP run** is a training run held to a fixed FLOP budget. To sweep it, double the data and halve the parameters, and so on. Hashimoto calls IsoFLOP easy and robust, probably his personal favorite: budgets spaced by factors of about three, a sweep of the parameter-to-data trade-off at each, then the minimum of each curve, or of a quadratic fitted to it ([64:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=3840)).

### 3. Fit, then extrapolate

With the best size found at several small budgets, fit a line through them and read off the size for the target budget. Do the same for loss. Lecture 9 gives the resulting rule of thumb from Chinchilla: about 20 tokens per parameter ([62:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=3720)), so a 70B model trains on about 1.4T tokens.

### 4. Carry the hyperparameters across scale

Two hyperparameters move with scale and matter most: batch size and learning rate.

- **Batch size.** Up to a **critical batch size**, every extra example in a batch pays off in full: training is limited by gradient noise, and more examples reduce it. Past it, the limit is the bias of the local descent direction, so returns diminish ([42:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=2520)). Hashimoto's recipe for finding it: pick a target loss, sweep batch sizes, and record the steps and the examples each needs to get there. The critical batch size is the minimum examples divided by the minimum steps ([44:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=2640)). It grows as the target loss falls, once again as a power law, so a run that goes all the way to a low loss can use large batches ([46:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=2760)).
- **Learning rate.** Two strategies from Lecture 11:
  - **muP** (maximum update parametrization), a set of rules for scaling initialization and learning rates with width, so that the best learning rate stays the same at every size. MiniCPM (2024) used it and tuned on a ladder of models about 5× smaller than the target. The best learning rate sat near 0.01 at every size ([6:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=360)).
  - **Direct search**, the DeepSeek LLM approach: no muP. Grid-search learning rate and batch size at several scales, keep the runs within 0.25% of the best, and fit how the optimum moves. Hashimoto's summary: fix the compute, vary the two, and mark the lowest loss at each scale. The optimal batch size rises and the optimal learning rate falls with non-embedding FLOPs ([16:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=960)). His reservation: unless the grid sits in the right place, quantization error weakens the fit ([18:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=1080)).

### 5. Use a schedule that lets you reuse runs

The **WSD schedule** (warmup, stable, decay) holds the learning rate constant after a short warmup, then decays it over about 10% to 20% of training, down to roughly 10% of its peak. It replaces the usual cosine curve, which needs the total budget known in advance, so a run trained for 4 million sequences cannot be extended to 8 million without starting over ([10:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=600)). The payoff: run one long training, rewind checkpoints and decay each one, and you have a sweep over training length for a fraction of the cost.

### 6. Predict, then run

Write down the predicted loss before the big run starts. Lecture 2 opens with a 10²³-FLOP run that landed within 0.05 of its forecast. Lecture 1 makes the principle explicit: what matters is smoothness across scales and relative performance, not the absolute number ([Lecture 1, 54:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3240)).

## Worked example

The numbers below are invented, to show the procedure.

```python
import math

def fit_line(xs, ys):
    """Least-squares line y = a + b * x."""
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b

# IsoFLOP runs: (compute budget in FLOPs, parameters, final loss). Tokens = C / (6 N).
runs = [(1e19, 1e8, 3.30), (1e19, 2e8, 3.22), (1e19, 4e8, 3.25),
        (1e20, 2e8, 3.09), (1e20, 4e8, 3.04), (1e20, 8e8, 3.06),
        (1e21, 4e8, 2.96), (1e21, 8e8, 2.92), (1e21, 1.6e9, 2.94)]

best = {}
for C, N, loss in runs:
    if C not in best or loss < best[C][1]:
        best[C] = (N, loss)                 # best size and loss per budget

budgets = sorted(best)
a, b = fit_line([math.log10(C) for C in budgets], [best[C][1] for C in budgets])
predicted = a + b * math.log10(1e22)        # loss at ten times the largest budget
```

What to observe:

- The best size doubles with every 10× in budget: 200M, 400M, 800M parameters. So the target run wants about 1.6B.
- The slope `b` is −0.15. Each tenfold increase in compute buys about 0.15 less loss.
- `predicted` is 2.76, down from 2.92 at the largest budget you actually ran. That number is the forecast to write down before spending.
- Three points per budget is too few for a real fit. Real sweeps use more sizes and more budgets.

## What the practitioners say

Hashimoto frames scaling laws as a tool for engineering at scale. Tuning hyperparameters on big models is, in his slide, the old and unpleasant way. The new optimism is to tune small and extrapolate ([2:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=120)). He warns that inside large labs belief in scaling laws is nearly a creed, and that scaling laws can be tricky objects.

On what a law can answer, Lecture 9 goes beyond size. Scaling comparisons are how you decide between Transformers and LSTMs, or Adam and SGD: train both cheaply at several compute levels and compare the lines ([30:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=1800), [34:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=2040)). Depth matters up to a point: one layer is hopeless, more than one is surprisingly competitive, and in his plot more layers did better at every compute level. The aspect ratio, unlike the layer count, is scale invariant: its minimum sits near 100 units of width per layer at every model size ([36:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=2160)). And not all parameters behave alike. Embedding parameters do not follow the same curve ([36:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=2160)).

His favorite method is IsoFLOP, which he calls easy and robust, with a recommendation: "isoflops is always a good default" ([76:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=4560)). On the Kaplan-versus-Chinchilla disagreement, which told teams to build much larger models on much less data, he is blunt. It shows that fitting "it's not just something where you like turn the crank and you get the answer" ([62:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=3720)). The cause, he says, is a sequence of small decisions. A replication paper, *Resolving Discrepancies of Compute-Optimal Scaling of Language Models*, started from the Kaplan settings and reached the Chinchilla result in three steps. Kaplan had excluded the output layer along with the embeddings when counting parameters. Its models were too small to converge during warm-up, which left the learning rates suboptimal. And it fixed one large batch size that hurt the smaller models ([68:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=4080), [70:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=4200)).

Lecture 11 turns to recipes that shipped. MiniCPM is his success case for muP: the best learning rate sits at the same value across model sizes, very clean in his experiments ([6:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=360)). He is skeptical of one MiniCPM claim, that models need far more tokens per parameter than Chinchilla found, and says it is unclear to him whether that is real ([14:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=840)). DeepSeek LLM (2024) is his other example, one of the more nicely executed scaling analyses in the open world ([16:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=960)). Its predicted losses for the two models it actually trained came out close to reality ([20:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=1200)). The slides add that Qwen 2.5, Kimi K2, Hunyuan, MiniMax-01 and StepFun all published fits of the same kind. StepFun's finding: loss is convex in learning rate and batch size, and the best batch depends mainly on data size.

His list of where muP breaks is practical. SwiGLU, unusual initializations, RMSNorm and changed optimizers all sit outside the theory, yet most of them work with muP in practice. Three fail: a learnable gain in RMSNorm, exotic optimizers such as Lion, and, the failure he finds most concerning, large decoupled weight decay. The slides put that weight decay at 0.1. muP still beats the standard parametrization, where the optimal learning rate shifts greatly as width grows ([74:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=4440)). His closing judgment on practice: it is "a lot more messy and a lot more unknown" than the clean lines suggest, and there is no silver bullet yet ([76:00](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=4560)).

Two limits come from Lecture 9's slides. Scaling laws can break if you apply them blindly, and they are lower bounds on what is achievable: a better recipe can beat the curve. A caveat from Lecture 1 applies to the 20-tokens-per-parameter rule: it ignores inference cost. A model that will be served to millions is worth training smaller and longer ([Lecture 1, 50:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3000)).

His strongest caution concerns transfer. Scaling-law lines for perplexity are clean and predictable, but transfer from perplexity to downstream tasks is a lot less certain than it seems. Post-training teams, he says, are handed a model with good perplexity and told the rest is their problem, although the trouble often started in pretraining ([52:00](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=3120)). Most points on scaling plots are single runs, which is another reason to keep a task set at every scale.

## Pitfalls

1. **Fitting on unconverged runs.** A run whose learning rate never decayed is not on the curve. Fix: use the same schedule shape at every scale, and WSD to get converged points cheaply.
2. **Changing the recipe between the small runs and the target.** The law describes one recipe. Fix: hold architecture, data and optimizer fixed, and scale hyperparameters by a rule.
3. **Assuming loss transfers to your task.** Perplexity curves are smooth. Downstream accuracy is not. Fix: keep a small task set at every scale.
4. **Comparing parameter counts that include embeddings.** Fix: fit on non-embedding parameters, or report both.
5. **Scaling the batch by habit.** Fix: set it from the target loss, as the critical batch size suggests, then confirm.
6. **Trusting one functional form.** Fix: fit with at least two of the three methods and compare.

## Try it

Take the worked example's script.

**Deliverable:** a notebook or script that reports the best size, the slope and the predicted loss for a target budget.

You are done when:

- Running it prints the three numbers above.
- You add a fourth budget (10²²) with three runs of your own invented losses that follow the trend, and the prediction changes by less than 0.02.
- You change one run's loss to break the trend and see how much the slope moves.
- A comment in the script states what you would check before trusting the prediction on real data.

**Stretch:** replace the discrete minimum with a quadratic fit in log-size for each budget, as the Chinchilla IsoFLOP method does.

## Key takeaways

- Loss falls as a power law in data, parameters and compute. On log-log axes that is a straight line you can fit and extend.
- Fix a compute budget, sweep model size at a few smaller budgets, take the best, and extrapolate. IsoFLOP is the default method.
- Chinchilla's answer was about 20 tokens per parameter for compute-optimal training. Inference cost argues for smaller models trained longer.
- Batch size and learning rate must be carried across scale by a rule: critical batch size, muP or a direct search.
- The WSD schedule makes converged checkpoints cheap. Predictability matters as much as optimality, and no method is a silver bullet.

## Self-check

1. What is an IsoFLOP run?
   - A. A training run held to a fixed FLOP budget
   - B. A run that doubles its budget every step
   - C. A run with the learning rate fixed to one value
   - D. A run that measures FLOPs but not loss
2. Which statement best captures the Chinchilla result?
   - A. Loss depends on parameters only
   - B. Parameters and data should grow together, about 20 tokens per parameter
   - C. Data should grow ten times faster than parameters
   - D. Compute has no effect on loss
3. Why does muP help when tuning a large model?
   - A. It removes the need for a learning-rate schedule
   - B. It makes the best learning rate stable across model widths
   - C. It increases the critical batch size
   - D. It lowers the loss floor in the scaling law
4. What does the WSD schedule let you do cheaply?
   - A. Compare architectures at equal FLOPs
   - B. Recover converged checkpoints at many training lengths from one run
   - C. Skip warmup on the largest model
   - D. Deduplicate the training data
5. A team fits a law on runs whose learning rate never decayed. What is the risk?
   - A. The fitted slope reflects unfinished runs, so the forecast is off
   - B. The FLOP count of each run is wrong by a factor of 6
   - C. The tokenizer changes between runs
   - D. Nothing, decay does not affect final loss

<details><summary>Show answers</summary>

1. A. Each run spends the same compute, so only the size and data split changes.
2. B. Their fits put similar exponents on parameters and data.
3. B. MiniCPM's best learning rate was the same across sizes.
4. B. Rewind to a checkpoint and run the short decay phase.
5. A. The follow-up paper Hashimoto cites found this in the Kaplan runs.

</details>

## Sources

- **Lecture:** Tatsu Hashimoto, "Lecture 9: Scaling Laws", Stanford CS336 Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=Q15rhEWZPQ4), used at [motivation](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=120), [parameter kinds](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=2160), [three methods](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=3720), [IsoFLOP](https://www.youtube.com/watch?v=Q15rhEWZPQ4&t=4560)
- **Lecture:** Tatsu Hashimoto, "Lecture 11: Scaling Laws", Stanford CS336 Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=vTfEyOyzV9E), used at [MiniCPM and muP](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=360), [skepticism](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=840), [DeepSeek](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=960), [no silver bullet](https://www.youtube.com/watch?v=vTfEyOyzV9E&t=4560)
- **Lecture:** Percy Liang, "Lecture 1: Overview, Tokenization" (scaling-laws unit): [video](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=2711)
- **Reading:** Jared Kaplan et al., "Scaling Laws for Neural Language Models" (2020): [arXiv](https://arxiv.org/abs/2001.08361)
- **Reading:** Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models" (2022): [arXiv](https://arxiv.org/abs/2203.15556)
- **Reading:** Greg Yang et al., "Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer" (2022): [arXiv](https://arxiv.org/abs/2203.03466)
- **Reading:** Shengyu Hu et al., "MiniCPM" (2024): [arXiv](https://arxiv.org/abs/2404.06395)
- **Reading:** DeepSeek-AI, "DeepSeek LLM: Scaling Open-Source Language Models with Longtermism" (2024): [arXiv](https://arxiv.org/abs/2401.02954)

## Next

→ [Inference](08-inference.md), the other half of the cost equation: what a trained model spends every time it generates. For the mixture-of-experts twist on parameter scaling, see [Attention Alternatives and Mixture of Experts](04-attention-alternatives-and-mixture-of-experts.md).
