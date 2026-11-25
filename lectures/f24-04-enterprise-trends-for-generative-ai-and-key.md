# Lecture guide: Enterprise trends for generative AI, and key components of building successful agents/applications

**Lecturer:** Burak Gokturk (Google) · **Course:** UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137), lecture 4 · **Length:** 1:04:00
**Video:** [watch on YouTube](https://www.youtube.com/watch?v=Sy1psHS3w3I) · **Slides:** [slides](https://rdi.berkeley.edu/llm-agents-mooc/slides/Burak_slides.pdf)
**Chapters that cite this lecture:** [07. Agents in the Enterprise](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md)

> **In one sentence:** Burak Gokturk describes what changed in the enterprise market for generative AI, and explains four techniques that turn a base model into a working application: tuning, distillation, grounding and function calling.

## Before you watch

Read [Agents in the Enterprise](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) first; it arranges the lecture as a procedure, from grounding to evaluation. You do not need any chapter of part 06.

## The lecture, part by part

### [0:00–5:23](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=0) How neural networks won

As a doctoral student the lecturer saw neural networks lose to support vector machines and expected them to vanish. Three changes reversed that: an architecture easy to run in parallel, training data created by hiding words in sentences and predicting them, and better chips with the transformer design. The public launch of ChatGPT in November 2022 convinced companies that the technology works.
**In this book:** nothing beyond this guide; nearest: [How Large Language Models Are Trained › Pre-training data](../01-foundations/02-how-large-language-models-are-trained.md#pre-training-data).

### [5:23–9:15](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=323) A decade of measured progress

Classical AI maps an input to a label; generative models run the other way, producing an image or speech from text. Two charts show the progress: image classification on ImageNet rose from 50.9 percent in 2011 to 90.88 percent, and the error rate for speech recognition on LibriSpeech fell from 13.25 percent in 2016 to 2.5 percent. The lecturer had expected this level after a hundred years, not fifteen.
**In this book:** nothing beyond this guide.

### [9:15–11:15](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=555) From base model to assistant

Supervised fine-tuning needs tens of thousands of expert answers. Preference tuning is cheaper: the model proposes several answers and a person marks each good or bad.
**In this book:** [From Base Model to Assistant: Post-Training › 1. Supervised fine-tuning: imitate good answers](../01-foundations/03-from-base-model-to-assistant-post-training.md#1-supervised-fine-tuning-imitate-good-answers) · [From Base Model to Assistant: Post-Training › 3. Preference tuning: reward models, RLHF and DPO](../01-foundations/03-from-base-model-to-assistant-post-training.md#3-preference-tuning-reward-models-rlhf-and-dpo).

### [11:15–15:57](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=675) A multimodal model and a long context

Gemini 1.5 accepts image, text, audio and video from the start, and its context reaches a million tokens in public preview, with trials up to ten million. The needle-in-a-haystack test hides one sentence, image or clip in a long input and checks that the model finds it: green for found, red for missed. An open research question is whether a model with a huge context will replace keyword or embedding search.
**In this book:** nothing beyond this guide; nearest: [Using LLMs: Tokens, Context and Sampling › The core idea](../01-foundations/04-using-llms-tokens-context-and-sampling.md#the-core-idea).

### [15:57–20:43](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=957) Enterprise trends: speed and access

Thousands of enterprises now ask to pilot each new feature. A base model is already trained, so a company starts in days, and any developer can build with it.
**In this book:** [Agents in the Enterprise › Gokturk: what companies ask for](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#gokturk-what-companies-ask-for).

### [20:43–23:48](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1243) Technical trends in the models

The next base model soon beats a domain-specific one. Sparse models run about a tenth of the paths of dense ones, and single-modality models are merging.
**In this book:** [Agents in the Enterprise › Gokturk: what companies ask for](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#gokturk-what-companies-ask-for).

### [23:48–26:14](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1428) Success factors: the platform

Companies ask for a broad set of models, customization with their own data, management in production, and choice at every level.
**In this book:** [Agents in the Enterprise › Gokturk: what companies ask for](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#gokturk-what-companies-ask-for).

### [26:14–28:01](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1574) Falling cost and latency

API prices fell about one and a half orders of magnitude, and latency fell with them, so more applications can use a model.
**In this book:** [Agents in the Enterprise › Gokturk: what companies ask for](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#gokturk-what-companies-ask-for).

### [28:01–30:46](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1681) Why models need search

A model is trained on the past, invents facts several percent of the time, and cannot name its source. Search returns citations, which gives an application authority.
**In this book:** [Agents in the Enterprise › Gokturk: what companies ask for](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#gokturk-what-companies-ask-for).

### [30:46–34:35](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=1846) One platform, choice at every level

Choice starts with the hardware, GPU or TPU. Model Garden gathers first-party, partner and open models in one place, with Agent Builder on top for customization.
**In this book:** [Agents in the Enterprise › The core idea](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#the-core-idea).

### [34:35–37:32](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2075) The four building blocks

Tuning adapts a base model to one use case, distillation makes a smaller model, and grounding ties answers to search. Function calling lets the model act.
**In this book:** [Agents in the Enterprise › The core idea](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#the-core-idea).

### [37:32–39:31](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2252) The range of tuning methods

The methods run from prompt design, which trains nothing, to full fine-tuning, which updates every weight. Prompt tuning sees little use in practice.
**In this book:** [Agents in the Enterprise › How it works, step by step: from notebook to workflow](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#how-it-works-step-by-step-from-notebook-to-workflow).

### [39:31–43:55](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2371) LoRA and parameter-efficient tuning

LoRA freezes the base model and learns a small added set of low-rank matrices, so only that addition is stored.
**In this book:** [Agents in the Enterprise › How it works, step by step: from notebook to workflow](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#how-it-works-step-by-step-from-notebook-to-workflow).

### [43:55–47:58](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2635) Distillation: teacher and student

A large teacher model labels the training data, and a small student learns to reproduce its answers. A higher temperature turns the teacher's outputs into soft labels.
**In this book:** [Agents in the Enterprise › How it works, step by step: from notebook to workflow](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#how-it-works-step-by-step-from-notebook-to-workflow).

### [47:58–55:01](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=2878) Grounding in practice

Three remedies help: retrieved context in the prompt, more factual models, and sources shown to the user. Because search has not become cheaper, an application decides when to call it.
**In this book:** [Agents in the Enterprise › Gokturk: what companies ask for](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#gokturk-what-companies-ask-for) · [Memory and Knowledge for Agents › C. Retrieval: the standard pipeline](../02-building-agents/04-memory-and-knowledge-for-agents.md#c-retrieval-the-standard-pipeline).

### [55:01–58:59](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=3301) Function calling in three steps

The developer defines functions, the model recognizes a request it cannot fulfil, and then picks the right function; the larger the library, the harder the choice.
**In this book:** [Tool Design and Function Calling › The core idea](../02-building-agents/02-tool-design-and-function-calling.md#the-core-idea).

### [58:59–1:04:00](https://www.youtube.com/watch?v=Sy1psHS3w3I&t=3539) Evaluation and conclusion

A side-by-side tool runs several models on one input and lets the largest model rate them. The closing advice: pair AI with another field, for creativity.
**In this book:** [Agents in the Enterprise › How it works, step by step: from notebook to workflow](../05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md#how-it-works-step-by-step-from-notebook-to-workflow) · [LLM-as-a-Judge and Rubrics › 4. Choose the setup](../03-evaluation/03-llm-as-a-judge-and-rubrics.md#4-choose-the-setup).

## What to take away

- Enterprises choose a platform, not a model: many models, customization, management in production.
- Adapt a model cheapest first: examples in the prompt, then parameter-efficient tuning such as LoRA.
- A model is trained on the past, invents facts and cannot cite; search grounds it.
- Function calling turns answers into actions.
- Evaluate each change automatically, with a large model as the rater.

## Sources

- Burak Gokturk, "Enterprise trends for generative AI, and key components of building successful agents/applications", UC Berkeley LLM Agents MOOC, Fall 2024 (CS 294-137): [video](https://www.youtube.com/watch?v=Sy1psHS3w3I).
- Slides: <https://rdi.berkeley.edu/llm-agents-mooc/slides/Burak_slides.pdf>.
- Course page: <https://rdi.berkeley.edu/llm-agents/f24>.
