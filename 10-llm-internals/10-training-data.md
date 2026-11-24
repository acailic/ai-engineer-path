# 10. Training Data

**Level:** Practitioner · **Reading time:** 16 min · **Exercise:** 90 min

> **In one sentence:** After this chapter you can describe the pipeline that turns a web crawl into pretraining text, and build its three workhorses: a rule-based filter, an exact-duplicate remover and a near-duplicate detector.

## Why this matters

The Llama 3 paper describes the model's architecture in full and its training procedure in detail. About the data, in the lecturer's summary, it says only that training used a variety of sources and some processing. Two reasons explain the silence: data is the competitive advantage, and admitting what you trained on invites copyright claims ([0:00](https://www.youtube.com/watch?v=-qm0ln33G24&t=0)).

So the part that most decides what a model can do is the part least documented. And it is large. Lecture 13 ends on the scale of the reduction: going from about 200 trillion raw tokens to under three trillion ([80:00](https://www.youtube.com/watch?v=-qm0ln33G24&t=4800)).

## The core idea

**Data does not fall from the sky.** Every training set comes from a pipeline:

`live service → raw data → processed data`

The raw material is a web page, a PDF, or a repository. None of it is plain text, most of it is not worth training on, and much of it repeats. Four operations turn it into a training set:

1. **Transform**: extract text.
2. **Filter**: keep what looks good.
3. **Deduplicate**: remove repeats.
4. **Mix**: decide how much of each source to use.

The analogy is cooking for a crowd from a market's delivery. Wash, trim, throw out what is spoiled, then combine in proportion. The analogy breaks on one point. A cook knows good produce when she sees it. Here "good" has no definition. It exists only as a small sample of text you already trust, and every rule is a guess about what makes that sample different from the rest.

Training itself comes in stages, and data quality rises along them:

| Stage | Data | Purpose |
|---|---|---|
| Pretraining | Large amounts of raw web text | Broad knowledge |
| Mid-training | Smaller, higher-quality sets, long documents | Specific capabilities, long context |
| Post-training | Conversations, tasks with checkers | Following instructions, reasoning (Chapter 11) |

The lecturer notes that the lines are blurry and that some large models now ship only in their post-trained form ([2:00](https://www.youtube.com/watch?v=-qm0ln33G24&t=120)).

## How it works, step by step

### 1. Get raw data

"Trained on the whole Internet" is wrong twice. The web is a set of live servers, not a dataset. And much of it cannot be had: pages behind logins, apps that need clicks, sites that block bots, terms of service that forbid scraping.

| Source | How to get it | Figures quoted in Lecture 13 |
|---|---|---|
| Common Crawl | Download a crawl: WARC files hold raw HTML, WET files hold extracted text | Non-profit since 2007; the April 2026 crawl has 2.19 billion pages, 372 TB |
| Wikipedia | Periodic dumps | 67 million articles in 361 language editions |
| GitHub | Clone repositories with permissive licenses; metadata from GitHub Archive | 420 million repositories, 28 million public |
| arXiv | Bulk download; LaTeX source available | About 3 million submissions |
| Stack Exchange | Data dumps with votes and tags | Question-and-answer format close to instruction data |
| Books | Licensed or public-domain collections | Mixed legal status |

### 2. Transform

HTML to text means removing navigation, ads and menus, then linearizing what remains. It is lossy: a nested table has no good one-dimensional form. The tools are rule-based, such as trafilatura, resiliparse and jusText, because they must run on terabytes. The conversion tool you pick changes downstream accuracy, so look at its output.

### 3. Filter

Lecture 14 gives one shape for almost every filter. You have a small **target** set T of good text and a huge **raw** set R. Find the part of R that resembles T. Two ways to score a document:

- A generative model of T scores how likely the document is under it.
- A classifier estimates the probability that the document belongs to T.

Keep documents above a threshold. Some pipelines keep probabilistically, in proportion to the score.

| Filter | How it works | Example from the lectures |
|---|---|---|
| Hand rules | Regular expressions and counts | C4 kept lines ending in punctuation with five or more words, and dropped pages with fewer than three sentences: 1.4 trillion tokens down to 156 billion |
| Language | A fastText classifier for 176 languages | Dolma keeps pages with English probability of at least 0.5 |
| Quality | A classifier with positives from trusted sources and negatives from the crawl | DCLM used instruction data and simple explanations as positives and got 3.8 trillion tokens from a 240-trillion-token pool |
| Domain | Rules plus a model of the domain | OpenMathText kept math-like text; its 14.7 billion tokens trained models that beat others trained on 20 times more |
| Toxicity | A classifier on labeled comments | Dolma used the Jigsaw toxic-comments dataset |

No single threshold is right. The lecturer's rule at [16:00](https://www.youtube.com/watch?v=5sxHosTLPF8&t=960): a long training run tolerates lower-quality data, a short one wants the best only. Lecture 13's slides add that strong quality filters can throw away about 90% of the crawl.

### 4. Deduplicate

Duplicates come in two kinds. Exact copies come from mirror sites and forks. Near copies differ by a few words: licenses, boilerplate, template text. One product description appears 61,036 times in C4. Removing repeats trains more efficiently and reduces memorization.

**Exact duplicates.** Hash each document and keep one per hash. Use a fast hash such as MurmurHash, not a cryptographic one. C4 went finer, removing repeated three-sentence spans, with a warning: deleting a span from the middle can leave an incoherent document.

**Near duplicates.** Compare documents as sets of word sequences. The **Jaccard similarity** of two sets is their shared share:

`Jaccard(A, B) = |A ∩ B| / |A ∪ B|`

Comparing every pair is impossible at web scale. **MinHash** solves it: under a random hash function, the chance that the smallest hash of A equals the smallest hash of B is exactly their Jaccard similarity. A short signature of many such hashes stands in for the set.

**Locality-sensitive hashing** turns signatures into candidate pairs. Split n hash values into b bands of r values each. Two documents are candidates if they agree on every value of at least one band. For documents with similarity s, the probability of becoming candidates is:

`1 − (1 − s^r)^b`

The switch from unlikely to likely is sharp near `(1 / b)^(1 / r)`. Larger r makes it stricter, larger b looser. The lecture's example, 9,000 hashes in 20 bands of 450, catches only almost-identical documents.

### 5. Mix

Each source gets a weight. Three naive choices: set weights by intuition, sample uniformly, or sample in proportion to size. Two problems follow:

- Too much weight on a small source means repeating it many times. Lecture 14 shows 50 passes over high-quality data, which overfits.
- Optimizing for one kind of evaluation skews the mixture. Code benchmarks make you upweight code until other abilities suffer.

Two answers come from the lecture. A hard cap on passes per source, and **regression-based mixing**: try many mixtures on small models, fit mixture to loss, and optimize. One trap is specific to that method. A small model trained on few tokens does not repeat its sources, while the large run would. So downsample every source in the same proportion, which makes the small runs feel the same scarcity the large one will ([68:00](https://www.youtube.com/watch?v=5sxHosTLPF8&t=4080)).

### 6. Synthetic data

A strong model can write training data. In pretraining, Nemotron-CC has a model rephrase low-quality pages and generates tasks from good ones. After pretraining, whole datasets are synthetic: OpenThoughts has 1.2 million reasoning examples written by a 32B teacher. The lecturer's findings there: sampling 16 responses per prompt helped, filtering answers did not, and a stronger model was not the better teacher.

### 7. The legal layer

Almost everything online is copyrighted. Using it needs a license or a fair-use argument. As of the lecture, US courts had found training on lawfully obtained books to be fair use in two cases, and obtaining them by piracy to be unlawful in one, with a reported $1.5 billion settlement. The lecturer's summary is that the area is active and evolving, so treat this as a snapshot.

## Worked example

A miniature pipeline in plain Python:

```python
import hashlib, re

def looks_like_prose(text):
    """Simplified rule in the spirit of C4: most lines end a sentence and have 5+ words."""
    lines = [line for line in text.split("\n") if line.strip()]
    ok = [line for line in lines if line[-1] in ".!?" and len(line.split()) >= 5]
    return len(lines) >= 1 and len(ok) >= 0.5 * len(lines)

def exact_key(text):
    return hashlib.md5(text.strip().encode("utf-8")).hexdigest()

def shingles(text, k=5):
    """The set of k-word sequences; this is the 'set' that Jaccard compares."""
    words = re.findall(r"\w+", text.lower())
    return {" ".join(words[i:i + k]) for i in range(len(words) - k + 1)}

def signature(sh, n=64):
    return [min(hash((seed, s)) for s in sh) for seed in range(n)]   # MinHash

def buckets(sig, bands=16, rows=4):
    """LSH: one bucket key per band."""
    return {hash(tuple(sig[b * rows:(b + 1) * rows])) for b in range(bands)}

def jaccard(a, b):
    return len(a & b) / len(a | b)

docs = [
    "buy now click here\nbest prices\nno prescription needed",
    "The cat sat on the mat and watched the rain fall on the garden.",
    "The cat sat on the mat and watched the rain fall on the porch.",
    "The cat sat on the mat and watched the rain fall on the garden.",
]
kept = [d for d in docs if looks_like_prose(d)]           # filter: 3 documents
seen, unique = set(), []
for d in kept:                                            # exact dedup: 2 documents
    if exact_key(d) not in seen:
        seen.add(exact_key(d))
        unique.append(d)
sigs = [buckets(signature(shingles(d))) for d in unique]
jaccard(shingles(unique[0]), shingles(unique[1]))         # 0.818
bool(sigs[0] & sigs[1])                                   # True: candidates for near-duplicate review
```

What to observe:

- The filter drops the spam page: its lines end no sentence and are too short.
- Exact hashing removes the verbatim copy.
- The two remaining documents differ by one word and have a Jaccard similarity of 0.818. With 16 bands of 4 rows, the chance that they share a bucket is above 99%.
- Python's `hash` is randomized per process, so signatures differ between runs. The similarity estimate and the candidate decision do not.
- Nothing here is production code. It is the smallest thing that shows each step.

## What the practitioners say

The lecturer's thesis across both lectures is that data work never ended, it changed shape. Before, it was labeling. Now it is curation and cleaning. His reason that it will always be scarce: "Data has always been a bottleneck and always will be a bottleneck" ([0:00](https://www.youtube.com/watch?v=-qm0ln33G24&t=0)), because it is a long-tail problem that grows with human effort, unlike architecture and systems.

He is candid about the method's maturity. Where other parts of the course rest on first principles, "data processing is, right now at least, a lot just based on kind of vibes" ([80:00](https://www.youtube.com/watch?v=-qm0ln33G24&t=4800)). He suggests the data assignment as a place to look for better ways.

On filtering he calls language identification a fairly easy problem ([12:00](https://www.youtube.com/watch?v=5sxHosTLPF8&t=720)). On mixing, he compares the regression method to scaling laws: cheap small runs that stand in for an expensive large one. And his closing description of the work is that "it's very domain-specific and requires looking at concrete examples" ([84:00](https://www.youtube.com/watch?v=5sxHosTLPF8&t=5040)).

Lecture 13 also gives the history in datasets: WebText for GPT-2, C4 for T5, The Pile, MassiveText for Gopher, the Llama sets, RefinedWeb, FineWeb at 15 trillion tokens, Dolma at 3 trillion, and Nemotron-CC at 6.3 trillion. For scale, it notes that Llama 3 trained on 15 trillion tokens and Qwen3 on 36 trillion.

## Pitfalls

1. **Trusting the text extraction.** Fix: read samples of the extracted text and measure the error rate before processing terabytes.
2. **One quality threshold for every run.** Fix: loosen the filter for long runs, tighten it for short ones.
3. **Deleting duplicate spans blindly.** Fix: check that documents still read as wholes.
4. **Over-weighting a small source.** Fix: cap the number of passes over any source.
5. **Tuning the mixture on one kind of evaluation.** Fix: optimize against a broad set.
6. **Copying mixture results from small runs to large ones.** Fix: downsample sources proportionally in the small runs.
7. **Ignoring access rules.** Terms of service, robots files, licenses and personal data in the crawl all apply. Fix: decide the policy before downloading.

## Try it

Take the pipeline above and a real sample: one WET file from a Common Crawl crawl, or any folder of HTML pages you may use.

**Deliverable:** a script and a one-page report.

You are done when:

- The script reproduces the toy example: 3 documents after filtering, 2 after exact deduplication, similarity 0.818.
- On the real sample it reports the token count before and after each step, as percentages.
- You have read 20 rejected and 20 kept documents and list the three most common reasons for rejection.
- It prints a list of near-duplicate candidate pairs, and you have checked five by hand.

**Stretch:** add a fastText quality classifier trained on 1,000 documents you label yourself, and compare its choices with the rule-based filter.

## Key takeaways

- Training data comes from a pipeline: transform, filter, deduplicate, mix. The reduction is about two orders of magnitude.
- Every filter is "find raw text that resembles a small trusted sample". The right threshold depends on how long you train.
- Exact duplicates fall to hashing. Near duplicates fall to MinHash with locality-sensitive hashing, which needs time linear in the data.
- Mixing is a scaling problem: try mixtures small, then extrapolate, with a cap on repeats.
- The work is judgment-heavy and example-driven. Read the data.

## Self-check

1. What is the shared shape of most filters?
   - A. Rank pages by their URL length
   - B. Keep raw documents that resemble a small trusted sample
   - C. Remove every page longer than a limit
   - D. Keep only pages that appear in many crawls
2. What does MinHash give you?
   - A. A compression of each document with no loss
   - B. A signature whose collision chance equals the Jaccard similarity
   - C. A count of the words in a document
   - D. A sorted list of a document's rare words
3. In locality-sensitive hashing, what does increasing the number of rows per band do?
   - A. It makes matching stricter
   - B. It makes matching looser
   - C. It changes nothing
   - D. It removes the need for signatures
4. Why can a mixture tuned on small runs mislead a large run?
   - A. Small models cannot read code
   - B. Small runs do not repeat their sources, while the large run would
   - C. Large runs use a different tokenizer
   - D. Sources change their language over time
5. When is a strict quality filter least appropriate?
   - A. A short run on a small budget
   - B. A fine-tuning run on one task
   - C. A long run with compute to spare
   - D. A run that deduplicates first

<details><summary>Show answers</summary>

1. B. That is the target-versus-raw pattern from Lecture 14.
2. B. The smallest hash values agree with probability equal to the Jaccard similarity.
3. A. More rows per band means more values must match, so the threshold moves up.
4. B. Downsampling every source proportionally reproduces the scarcity in advance.
5. C. Long runs benefit from more, lower-quality data.

</details>

## Sources

- **Lecture:** Stanford CS336, "Lecture 13: Data (Sources, Datasets)", Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=-qm0ln33G24), used at [why data is secret](https://www.youtube.com/watch?v=-qm0ln33G24&t=0), [stages](https://www.youtube.com/watch?v=-qm0ln33G24&t=120), [closing](https://www.youtube.com/watch?v=-qm0ln33G24&t=4800)- **Lecture:** Stanford CS336, "Lecture 14: Data", Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=5sxHosTLPF8), used at [language ID](https://www.youtube.com/watch?v=5sxHosTLPF8&t=720), [thresholds](https://www.youtube.com/watch?v=5sxHosTLPF8&t=960), [simulated scarcity](https://www.youtube.com/watch?v=5sxHosTLPF8&t=4080), [closing](https://www.youtube.com/watch?v=5sxHosTLPF8&t=5040)
- **Reading:** Common Crawl: [commoncrawl.org](https://commoncrawl.org/)
- **Reading:** Colin Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (2019), the paper that introduced C4: [arXiv](https://arxiv.org/abs/1910.10683)
- **Reading:** Guilherme Penedo et al., "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale" (2024): [arXiv](https://arxiv.org/abs/2406.17557)
- **Reading:** Jeffrey Li et al., "DataComp-LM: In Search of the Next Generation of Training Sets for Language Models" (2024): [arXiv](https://arxiv.org/abs/2406.11794)

## Next

→ [Post-Training: SFT, RLHF and RLVR](11-post-training-sft-rlhf-and-rlvr.md), for the smallest and most valuable slice of the data: the examples that turn a base model into an assistant. The data side of evaluation is in [Evaluating Language Models](09-evaluating-language-models.md), and data scaling laws are in [Scaling Laws](07-scaling-laws.md).
