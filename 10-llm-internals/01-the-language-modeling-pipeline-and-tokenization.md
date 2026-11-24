# 01. The Language Modeling Pipeline and Tokenization

**Level:** Practitioner · **Reading time:** 16 min · **Exercise:** 90 min

> **In one sentence:** After this chapter you can turn any string into token IDs with a byte-pair encoding tokenizer you wrote yourself, and you can name the five pieces that CS336 builds to get from raw text to a trained language model.

## Why this matters

You paste a 2,000-character email into a token-counting tool and it reports about 500 tokens. Price lists, context limits and speed are all quoted in tokens, never in characters. Then two odd things show up. The word "world" costs one token in the middle of a sentence and two at the start of one. The phrase `hello hello` is split in two different ways, once with a space glued to the word and once without.

The model never sees your text. It sees integers. So two questions come before any architecture or training math:

1. What are the units a language model actually reads, and how does text become them?
2. Where does that step sit in the work of building a language model from scratch?

This chapter answers both: first the map of the whole build, then tokenization from bytes to byte-pair encoding.

## The core idea

A language model reads a sequence of **tokens**, gives a probability to every possible next token, and, when you ask it to generate, picks one. A token is an integer between 0 and V−1, where V is the **vocabulary size**.

Text is not integers. A Python `str` is a sequence of Unicode characters, and the UTF-8 encoding turns each character into one to four **bytes**, each a number from 0 to 255. So you need a translator. A **tokenizer** is two functions: `encode` turns a string into a list of integers and `decode` turns them back. The one hard requirement is the round trip: `decode(encode(text)) == text`.

The analogy is the lexer in a compiler, which turns characters into tokens such as keywords and identifiers. The analogy breaks in two places. A lexer's token kinds are fixed by the language grammar, while a tokenizer's vocabulary is learned from a corpus. And a lexer throws whitespace away, while a tokenizer keeps it: the space before a word is part of a token.

Why translate at all, if bytes are already integers? Because of cost. The work a model does per token is roughly fixed, but attention, the mechanism that lets each token look at the others, costs more as sequences get longer. Lecture 1 puts it as "attention is quadratic in sequence length", meaning doubling the length roughly quadruples that part of the work. A modern tokenizer packs about 1,000 bytes into 250 tokens. That is four times less sequence for the model to process. Tokenization is an efficiency decision.

## How CS336 frames the whole pipeline

Stanford CS336, *Language Modeling from Scratch* (Spring 2026, taught by Percy Liang and Tatsunori Hashimoto), has one organizing idea: train the best model you can with a fixed budget of compute and memory. Every piece of the build is judged by that standard. The course splits into five units, each with one assignment:

| Unit | Question it answers | What students build |
|---|---|---|
| Basics | What are the atoms, the model and the training loop? | A tokenizer, a Transformer, a training loop; train on TinyStories and OpenWebText |
| Systems | How do you get the most out of GPUs? | A fused kernel in Triton, distributed training, faster inference |
| Scaling laws | How big should the model be for a given budget? | Fits that predict loss from small runs |
| Data | What do you train on? | Text extraction, quality filters, deduplication |
| Alignment | How do you make the model useful and safe? | Fine-tuning and reinforcement learning methods |

For the big picture of why pretraining, see [how large language models are trained](../01-foundations/02-how-large-language-models-are-trained.md). This part of the course follows the five units one chapter at a time.

## The design space of tokenizers

Four ways to choose the atoms are worth comparing. The measure that matters is the **compression ratio**: bytes per token. Higher is better for compute, because the sequence gets shorter.

| Scheme | Vocabulary size | Compression | Main problem |
|---|---|---|---|
| One token per Unicode character | About 150,000 | Low | Many characters are rare, so vocabulary slots are wasted |
| One token per byte | 256 | Very low | Sequences are far too long |
| One token per word | No fixed limit, in the millions | High | Rare words are learned badly; new words have no token |
| Byte-pair encoding (BPE) | You choose it | High | Adds a separate component with its own file to ship |

The character and byte schemes sit at opposite ends. The Lecture 1 notes call the character version "the worst of both worlds": a huge vocabulary and little compression. The byte version has a tiny vocabulary but, in the same notes, a "terrible" compression ratio.

Words look better. Each token means something, because people invented words. The cost is an open-ended vocabulary. A word seen three times in training teaches the model almost nothing. And a word that never appeared has to become a special `UNK` token, which the notes warn can distort **perplexity**, the model's average uncertainty about the next token (lower is better). Perplexity is counted per token, so two models with different tokenizers are not comparable on it.

## How it works, step by step

**Byte-pair encoding** learns the vocabulary from data. Common sequences of bytes become single tokens. Rare sequences stay split.

Training:

1. Encode the corpus with UTF-8. You now have a long list of integers, each from 0 to 255.
2. Count every pair of adjacent integers.
3. Take the most frequent pair. Assign it the next free ID (the first is 256). Record the merge.
4. Replace every occurrence of that pair in the list with the new ID.
5. Repeat from step 2 until you have the number of merges you want.

Encoding new text:

1. Encode the string as bytes.
2. Apply the recorded merges in the order they were learned, one merge at a time over the whole sequence.
3. Return the resulting IDs.

Decoding: each ID stands for a byte string (a raw byte for 0 to 255, the two merged strings joined for the rest). Join the byte strings and decode them as UTF-8.

Real tokenizers add three things, which is also what CS336's first assignment asks for beyond the basic version:

- **Pre-tokenization**: splitting text first with a regular expression, as the GPT-2 tokenizer does, so merges never cross a word or punctuation boundary.
- **Special tokens**: strings such as `<|endoftext|>` that mark document boundaries. The tokenizer must detect them and never split them.
- **Speed**: when encoding, loop only over the merges that can actually apply, not over all of them.

## Worked example

A complete byte-level BPE in plain Python:

```python
from collections import Counter

def merge(data, pair, new_id):
    """Replace every (pair[0], pair[1]) in `data` with `new_id`."""
    out, i = [], 0
    while i < len(data):
        if i < len(data) - 1 and (data[i], data[i + 1]) == pair:
            out.append(new_id)
            i += 2
        else:
            out.append(data[i])
            i += 1
    return out

def train_bpe(text, num_merges):
    """Learn `num_merges` merges. IDs 0-255 stay the raw bytes."""
    data, merges = list(text.encode("utf-8")), {}
    for i in range(num_merges):
        pairs = Counter(zip(data, data[1:]))
        if not pairs:
            break
        pair = max(pairs, key=pairs.get)   # most frequent adjacent pair
        merges[pair] = 256 + i
        data = merge(data, pair, 256 + i)
    return merges

def encode(text, merges):
    data = list(text.encode("utf-8"))
    for pair in sorted(merges, key=merges.get):   # in the order learned
        data = merge(data, pair, merges[pair])
    return data

def decode(ids, merges):
    vocab = {i: bytes([i]) for i in range(256)}
    for (left, right), new_id in merges.items():
        vocab[new_id] = vocab[left] + vocab[right]
    return b"".join(vocab[i] for i in ids).decode("utf-8")

corpus = ("the cat sat on the mat. the dog sat on the log. "
          "a cat and a dog sat on a mat. ") * 50
m = train_bpe(corpus, 30)
```

Run on this corpus, the first merges are `at`, `at `, `th`, `the`, `the `, ` the `, `sat `, `sat o`, `sat on`, `og`, ` a`, ` a `. Encoding four short strings gives:

| Input | Bytes | Tokens | Pieces |
|---|---|---|---|
| `the cat sat on a log` | 20 | 6 | `the `, `cat `, `sat on`, ` a `, `l`, `og` |
| `catalog` | 7 | 5 | `c`, `at`, `a`, `l`, `og` |
| `The cat` | 7 | 6 | `T`, `h`, `e`, ` `, `c`, `at` |
| `the cat sat on the mat.` | 23 | 3 | `the `, `cat sat on the `, `mat.` |

Five things to observe:

1. Frequency drives everything. `at` merges first because it is the most common pair.
2. Spaces stick to words. `the ` and ` the ` are different tokens, which is the `hello hello` effect from the start of the chapter.
3. Nothing is unknown. `catalog` never appears in the corpus, so it falls back into pieces the model has seen.
4. Capital letters are different bytes. `The` breaks apart completely.
5. Merged phrases appear, such as `cat sat on the `. The corpus is one tiny paragraph repeated, so merges run across word boundaries. Pre-tokenization prevents this, and so does diverse training text.

The round trip `decode(encode(corpus)) == corpus` holds.

## What the practitioners say

Percy Liang opens the course with a claim about what a small-scale course can teach. He sorts knowledge into three kinds: mechanics (how things work), mindset (squeezing the hardware, taking scaling seriously) and intuitions (which data and modeling choices work). The first two transfer to frontier models. Intuitions only partly do, because small models behave differently: in an old plot he shows, the share of FLOPs spent in the MLP layers is about 44% at small scale and about 80% at 175B parameters ([6:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=360)).

His organizing lens is efficiency, and he applies it to every unit, including data: "We don't want to waste time updating gradients on a bunch of redundant bad data" ([64:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3840)). With a fixed compute budget, time spent on bad data is time not spent on good data.

His advice for someone with an application has three steps, in order: prompt a model, fine-tune a model, and only as a last resort pretrain your own, because pretraining "is a pain and it's also expensive". He adds that watching lectures is not enough: "you learn really by doing the assignments" ([22:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=1320)).

On tokenization itself, the Lecture 1 notes ([65:06](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3906)) make four points:

- Growing the vocabulary raises the compression ratio, but it also makes the model's use of the vocabulary sparser.
- BPE was introduced by Philip Gage in 1994 for data compression, later adapted to neural machine translation, and then used by GPT-2.
- BPE is a data-driven heuristic that works well. Character, byte and word tokenization are all "highly suboptimal".
- The long-term goal is a tokenizer-free model that reads bytes directly. Such models are promising but, in his words at the time, have not been scaled to the frontier.

Liang closes with two properties any replacement must have ([78:00](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=4680)): the model should operate on chunks, not on raw units, which matters even more for video or DNA than for text, and chunks should vary in size, so that more model capacity goes to the interesting parts of the input.

## Pitfalls

1. **Treating a token as a word.** English averages roughly four bytes per token with a modern tokenizer, but punctuation, code and other languages differ. Fix: measure with the tokenizer you will ship.
2. **Cleaning text before tokenizing.** Stripping leading spaces or lowercasing changes the token IDs. Fix: tokenize exactly what the model will see.
3. **Training BPE on a small or repetitive corpus.** Merges cross word boundaries and become phrases. Fix: train on representative text and add pre-tokenization.
4. **A slow `encode`.** Applying every merge to the whole sequence for every input wastes time. Fix: consider only the merges that can apply, as the assignment asks.
5. **Decoding bytes token by token.** One emoji is four bytes that may land in four tokens. Decoding each one alone raises a UTF-8 error. Fix: join all bytes first, as `decode` above does.
6. **Reusing IDs across models.** Every tokenizer has its own vocabulary. Token 257 here is `th`; in another model it is something else.
7. **Comparing perplexity across tokenizers.** Fewer, longer tokens mean less uncertainty per token. Fix: compare models only on the same tokenizer, or convert to a per-byte measure.

## Try it

Save the code above as `bpe.py` and use a real text file of at least 1 MB as the corpus.

**Deliverable:** a script that trains on 90% of the file and reports results on the other 10%.

You are done when:

- The round trip holds on the held-out text, including at least one line with non-ASCII characters.
- A word absent from the training split still encodes without any unknown-token marker.
- You report the compression ratio on held-out text for 50, 500 and 5,000 merges, and it is lower than on the training text.
- Encoding the held-out text takes under five seconds.

**Stretch:** add pre-tokenization with a regular expression that keeps letters, digits, spaces and punctuation apart. Compare the first 30 merges with and without it.

## Key takeaways

- A language model reads integers. The tokenizer converts between strings and token IDs and must round-trip exactly.
- Tokenization exists for efficiency: fewer tokens means a shorter sequence and less attention work.
- Byte-pair encoding starts from bytes and repeatedly merges the most frequent adjacent pair. Common chunks become one token and anything unseen falls back to bytes.
- CS336 treats every part of the build, tokenization included, as a question of efficiency under a fixed budget.
- The course teaches mechanics and mindset; intuitions from small models only partly carry over.

## Self-check

1. What must every tokenizer guarantee?
   - A. The most frequent words map to the lowest IDs
   - B. Encoding and decoding return the original string
   - C. Every input string uses fewer tokens than bytes
   - D. The vocabulary stays below 65,536 entries
2. Why are raw bytes a poor choice for a Transformer in CS336's view?
   - A. Bytes cannot represent text that is not English
   - B. GPUs refuse to multiply integer matrices efficiently
   - C. Long sequences make the attention cost grow too quickly
   - D. Byte sequences cannot be decoded without loss
3. In BPE training, what picks the next merge?
   - A. The pair of adjacent tokens that occurs most often
   - B. The pair whose tokens have the smallest IDs
   - C. The longest word in the current vocabulary
   - D. The pair whose merge shortens the text least
4. You train byte-level BPE with 1,000 merges. How many token IDs exist?
   - A. 1,000
   - B. 256
   - C. 1,256
   - D. 512
5. Why does `The cat` split into more tokens than `the cat` in the example?
   - A. Capital letters are encoded as two bytes each
   - B. No merge was learned for the byte sequences of that variant
   - C. The tokenizer rejects words at the start of a string
   - D. The encoder sorts tokens before merging

<details><summary>Show answers</summary>

1. B. The round trip `decode(encode(text)) == text` is the one hard requirement.
2. C. Attention cost grows about quadratically with sequence length, and bytes make sequences long.
3. A. Each round merges the most frequent adjacent pair in the current sequence.
4. C. The 256 raw byte IDs plus 1,000 merged IDs.
5. B. `T` and `t` are different bytes, so the merges learned for `the` never apply to `The`.

</details>

## Sources

- **Lecture:** Percy Liang, "Lecture 1: Overview, Tokenization", Stanford CS336 Language Modeling from Scratch (Spring 2026): [video](https://www.youtube.com/watch?v=JuoVZkPBiKk), used at [three kinds of knowledge](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=360), [learn by doing](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=1320), [efficiency lens](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3840), [tokenization notes](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=3906), [what replaces tokenization](https://www.youtube.com/watch?v=JuoVZkPBiKk&t=4680)
- **Course:** Stanford CS336, [course page](https://cs336.stanford.edu/)
- **Reading:** Philip Gage, "A New Algorithm for Data Compression" (1994), where BPE was introduced
- **Reading:** Rico Sennrich, Barry Haddow and Alexandra Birch, "Neural Machine Translation of Rare Words with Subword Units" (2016): [arXiv](https://arxiv.org/abs/1508.07909)
- **Reading:** Andrej Karpathy, "Let's build the GPT Tokenizer" (2024), the video the lecture notes recommend: [video](https://www.youtube.com/watch?v=zduSFxRajkE) <!-- VERIFY: video ID taken from memory, not checked -->

## Next

→ [Resource Accounting: FLOPs, Memory and Arithmetic Intensity](02-resource-accounting-flops-memory-and-arithmetic-intensity.md), because the efficiency argument for tokenization only makes sense once you can count what a model spends. When you are ready for the model itself, continue with [Transformer Architectures and Hyperparameters](03-transformer-architectures-and-hyperparameters.md), and see [Building Your Own](13-building-your-own-a-roadmap-through-the-assignments.md) for how the tokenizer fits into the first assignment.
