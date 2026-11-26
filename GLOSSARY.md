# Glossary

One definition per term, and one term per concept. The name in bold is the one the course uses most. Other names the parts use follow it as "also called". The last column links to the chapter that defines the term best: `03.02` means part 03, chapter 02. The definitions come from the glossaries of the eleven parts, merged into one list.

- [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z) · [Numbers](#numbers)

## A

| Term | Definition | Defined in |
|---|---|---|
| **A/B test** (also called: A/B experiment) | Showing a change to a randomly assigned treatment group and comparing it with a control group. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **A2A** | The Agent2Agent protocol, an open convention for agents to exchange tasks and messages over the network. | [03.08](03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) |
| **Ablation** | Running a system again with one ingredient removed, to measure that ingredient's effect. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Accelerator chip** | A processor built for model arithmetic. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Accelerator intensity** | A chip's peak FLOP/s divided by its memory bandwidth. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Acceptance test** | A test that the product serves the users' needs, which validates that the right system was built. | [08.08](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) |
| **Accessibility gap** | Welleck's name for the distance between strong research methods and tools people can use, since the methods are often closed or costly to run | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Accessibility tree** | The operating system's list of interface elements with their roles and names. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Accountability** | The state in which a named person or role answers for each kind of automated decision and affected people can appeal. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Accuracy (of a measure)** | How close a measure's values lie, on average, to the true value. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Accuracy (of a model)** | The share of a model's predictions that match the label. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Acting (in an agent)** | Calling something outside the model, such as retrieval, code execution or a tool, which adds knowledge and feedback. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Action** | What an agent does in its environment, such as calling a tool. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Action space** | The set of moves an agent can make. | [02.07](02-building-agents/07-coding-agents.md) |
| **Activation** (also called: Activations) | Intermediate results computed in the forward pass that the backward pass needs. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Activation checkpointing** | Storing only some layers' activations and recomputing the rest in the backward pass. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Activation function** | A simple nonlinearity such as `max(0, x)` applied to each value. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Activation memory** | The memory holding a layer's intermediate results while it runs. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Activation sparsity** | Zeros in the intermediate results, for example in point-cloud data, that a sparse kernel can skip. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Active parameters** | The parameters one token passes through, as opposed to the model's total parameters. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **ad hoc teamwork** | The problem of building one agent that cooperates with teammates it did not train with and cannot choose | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Adam** | An optimizer that combines momentum, the average of past gradients, with the average of their squares to scale each update. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Adapter** | A small trainable layer inserted into each transformer block. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Adapter (DSPy)** | The part that lays a module's fields out as a prompt and parses the output back. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **AddressSanitizer** | A sanitizer that detects out-of-bounds reads and writes at run time. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Advantage** | A reward minus a baseline, here the group's standardized reward, which sets the size and sign of an update. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **Adversarial data set** (also called: Attack set) | A versioned collection of attacks, each with its task, the place its payload is planted, and its oracle. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Adversarial environment** | A test setting with a hostile system prompt, a hostile user prompt, or misleading examples in the prompt. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Adversarial example** (also called: Evasion attack) | An input changed just enough to flip a model's output. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Adversarial search** | Searching for the smallest input change that breaks an invariant or relation. | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **Adversarial suffix** | A string of tokens appended to a request that makes an aligned model comply. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Adverse event reporting** | A channel through which harms observed after deployment are reported, as in aviation and cybersecurity. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **Agency** (also called: Level of automation) | How much an agent can do without a person: which tools, with which permissions, and how much autonomy. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Agent** | A system that pursues a goal by acting on an environment in steps: at each step it observes the environment, decides the next action itself, and acts again, until the goal is met or a budget runs out. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Agent (conversational peer)** | In conversation programming, a named participant with a role and a function that speaks for it: a model, a tool or a person. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Agent loop** | The code that calls the model, runs the chosen tool, appends the result to the history and checks for a stop. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **Agent skills** | Named bundles of instructions and tools that an agent can call. | [02.07](02-building-agents/07-coding-agents.md) |
| **Agent-computer interface (ACI)** | The set of commands an agent uses to view, search and change a computer, designed around the model's limits. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **AgentBeats** | The platform that hosts assessments between green agents and white agents. | [03.08](03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) |
| **Agentic model** | A model trained to maximize verifiable rewards by acting in environments with tools, in addition to matching human preference. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Agentic RAG** | An agent layer above retrieval that treats retrieval as a tool and decomposes the question before answering. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Agentic RL** | Reinforcement learning on whole trajectories in environments with tools, with task success as the reward. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Agents4Science 2025** | An online conference held on October 22, 2025 in which agents wrote and reviewed the papers. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **AgentTrek** | A pipeline that turns web tutorials into agent trajectories by replaying them and filtering with an evaluator model. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **AGUVIS** | A vision-only GUI agent trained with a unified action format and an inner monologue. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **AI Safety Levels** | Named risk levels, ASL-1 to ASL-4 in the lecture, each with required safeguards before a model may reach it. | [03.06](03-evaluation/06-evaluating-capabilities-and-risks.md) |
| **AI safety vs AI security** | Safety means the system does no harm to the outside world; security means the system is protected from outsiders. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Alert** | A notification sent when a telemetry value crosses a threshold. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Algorithm and system co-design** | Changing the model and the software or hardware together instead of tuning either alone. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Aligned model** | A model post-trained to maximize a given objective, such as human preference for chat models or verifiable rewards for agentic models. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Alignment** | In CS336, moving from full supervision to scored responses: generate, score with a human, verifier or judge, and update. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |
| **Alignment problem** | The risk that an automated system meets an assigned objective that captures the task only partially. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **All-gather** | Collecting every rank's slice onto every rank. | [10.06](10-llm-internals/06-parallelism.md) |
| **All-reduce** | Summing tensors across ranks so that every rank has the total. | [10.06](10-llm-internals/06-parallelism.md) |
| **All-to-all** | Every rank sending a different slice to every other rank. | [10.06](10-llm-internals/06-parallelism.md) |
| **Allow-list** | A list of the only destinations or actions that are permitted. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **AlphaProof** | DeepMind's system that combines autoformalization, imitation, reinforcement learning and test-time RL on Lean proofs. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Amplitude encoding** | Loading an input vector into the state vector, so n features need only the base-2 logarithm of n qubits | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Analogical prompting** | Asking a model to first recall a similar problem and its solution, then solve the new problem. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Anchor** | The few conditions on an input that suffice to produce a given prediction. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **AND gate, OR gate** | The two ways causes combine in a fault tree: all are needed, or one is enough. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Angle encoding** | Storing each value in a rotation angle, one gate per value, with no state-preparation circuit | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Annotated run** | A run that a person reviewed and labeled, used to measure a user simulator's own error rate. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Annotator** (also called: Labeler) | A person who labels examples or grades outputs by hand. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Anomaly detection** | Flagging behavior that differs from the normal pattern. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |
| **Anomaly detection (data)** | Learned checks that flag values unusual for the data's distribution. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Anonymization** | Removing identifying information or sensitive attributes from stored data, which is hard because models can infer what is missing. Only in the proposal above; the course mentions anonymized logs in 08/09, step 3 of "How it works", without defining the term. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Anti-classification** | A fairness criterion requiring that protected attributes never change the output. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Antipattern** | A common practice that looks helpful and causes harm. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **AnyRes** | Splitting a high-resolution image into encoder-sized tiles and concatenating their tokens. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |
| **API access** | Using a model only through prompts and responses, which allows measuring behavior. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **API agent** | An agent that uses software by calling functions the software exposes. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Appeal path** | A route by which a person can have an automated decision reversed. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Arbitrary encoding** | Combining several encodings in one circuit: rotations, then CNOT gates, then rotations | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Architectural style** | A common overall structure for systems, such as client-server or three tiers. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Architectural view** | A picture of a system that shows one concern and hides the rest. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Architecturally significant requirement** | A quality requirement that can be met only by planning the whole system. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Architecture decision record (ADR)** | A short file that keeps one decision with its context, the alternatives considered and the conditions for revisiting it. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Arithmetic intensity** | An operation's FLOPs divided by the bytes it moves. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **ASM (assumption)** | A statement about the world that the software relies on to meet its requirements. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Aspect ratio** | Model width divided by number of layers, the depth-versus-width choice to fix before scaling. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Asset** | Anything in a system worth protecting, from user data to the API key, the system prompt, and whatever a tool can reach. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Associativity** | Connecting scattered pieces of information. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Assurance case** | A structured record of safety claims and the evidence supporting them. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Asynchronous RL** | Training in which the sampler and the trainer do not wait for each other. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Attack success rate** | Successful attacks divided by attempts, with the number of runs stated. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Attack surface** | The set of ways anyone can interact with a system. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Attacker** | Anyone who controls input that the system will read or run, including a legitimate user who wants more than they should get. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Attempt** | One run of one task by the system under test. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Attention** | The step in which each token weighs how relevant the earlier tokens are and updates its vector with what it finds. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Attention head** | One of the parallel attention sub-calculations of a layer; KV heads are the ones that produce keys and values. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Attention map** | The table of attention weights of a transformer layer, with one row and one column per token, `N × N` in size | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Attention sink** | A token, usually among the first, that attracts a large share of attention regardless of meaning. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Attribution** | The share of statements in an answer that the cited sources support. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Audit trail** | The record of events that lets you reconstruct a run afterwards. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |
| **Autoencoder** | A network trained to reconstruct its input, used to flag inputs it reconstructs badly. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Autoformalization** | Translating a mathematical statement or proof from prose into formal code. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Automate, prompt, augment** | The three strengths of human interaction with a model, from acting without asking to only showing information. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Automated theorem prover** | A program that searches for a proof of a goal in some logic without a person writing each step; strong on small gaps, weak on long proofs. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Automation bias** | The tendency of people to accept a machine's suggestion. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Auxiliary lemma** | A lemma invented on the way to a theorem. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Availability** | The goal that authorized users get reliable and timely access to a service. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **AWQ** | Activation-aware weight quantization: a 4-bit weight-only method that scales up the few channels that matter most before quantizing them. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |

## B

| Term | Definition | Defined in |
|---|---|---|
| **Backdoor** | A hidden trigger in a model that makes it misbehave when it appears in the input. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Backoff** | A wait that grows between retry attempts, up to a cap. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Backpropagation** | The algorithm that computes how each weight should change by reading every intermediate result again. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Bake-off** | Running two implementations on the same cases and comparing success, cost and latency. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Bank conflict** | Two threads needing the same shared-memory bank in one cycle, which forces them to wait. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Barren plateau** | A region where a quantum circuit's gradients vanish as it grows, stalling training. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Base model** | A model that has only been pre-trained: it continues text and does not follow instructions. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Baseline** | The simplest version of a solution, measured so that anything smarter can be compared with it. | [07.02](07-ml-in-production/02-when-to-use-ml-and-when-not-to.md) |
| **Basic event** | A cause in a fault tree that is not split further; model failure is usually treated as one. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Basis encoding** | Storing a binary string as one basis state of the qubits | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Batch** | A group of requests or inputs processed together to reuse the weights. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **batch normalization** | A normalization layer whose set is one channel, across the whole batch and every position; common in convolutional networks | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Batch processing** | One long computation over a large snapshot of data, built for throughput. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Bayesian optimizer** | A search method that picks the next trial from the results of earlier trials. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Behavior cloning** (also called: Imitation model) | Learning by copying demonstrated answers, which is what SFT does. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Behavioral requirement** | A requirement that says what the software does. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Behavioral testing** | Building test data for one capability at a time and asserting a pass rate per capability. | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **Benchmark** | A dataset, an environment and a scoring procedure that many teams use to compare systems. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Benign environment** | A test setting with plain prompts. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Best response** | The strategy that scores highest against a given opponent strategy. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Best-of-N** (also called: Search by repeated sampling) | Sampling N answers in parallel and keeping one that passes a check. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Beta distribution** | A flexible probability distribution for values between 0 and 1, which fits per-question pass rates across models. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **Bias** | In a neural network, one extra learned number per output of a layer, added after the multiply. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Big Sleep** | Google Project Zero's agent that finds memory-safety bugs with a code browser, a scripting tool, and a debugger. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **binary quantization** | Quantization that keeps only the sign of each weight, +1 or −1, so that multiplications become additions and subtractions | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **BitFit** | Parameter-efficient fine-tuning that trains only the bias terms. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Bitter lesson** | Richard Sutton's argument that methods which make the best use of growing compute win in the long run. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Black-box attack** | An attack that uses only success or failure as feedback. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Black-box test** | A check that you can print every message and edit every prompt a framework sends to the model. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Blast radius** | The share of users and systems exposed to the consequences of a failed experiment or release. | [11.07](11-professional-practice/07-checklists.md) |
| **Bloch sphere** | The sphere whose points are the states of one qubit; a single-qubit gate rotates it | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Blue/green deployment** | Switching all traffic from an old version to a new one at once. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Blueprint** | A decomposition of a research proof into definitions and lemmas arranged as a dependency graph, written in LaTeX before each node is proved in Lean | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Bootstrap** | Estimating uncertainty by resampling the observed data with replacement. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **Bootstrapping (few-shot)** | Keeping the traces of runs that passed the metric and using them as worked examples in prompts. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Bubble** | Time in a pipeline when some GPUs wait for others. | [10.06](10-llm-internals/06-parallelism.md) |
| **budget forcing** | Setting the length of a model's thought at inference: when the model stops early, "wait" is appended and it goes on; a run that is too long is cut off | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Byte-pair encoding (BPE)** | A method that learns a vocabulary by repeatedly merging the most frequent pair of adjacent units, starting from bytes. | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) |

## C

| Term | Definition | Defined in |
|---|---|---|
| **CACE principle** | "Changing anything changes everything": one change in data, model, or prompt can shift the behavior of the whole system. | [08.08](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) |
| **Cache** | A store of results from expensive computations, reused until an invalidation rule removes them. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Calibrated model** | A model whose confidence scores match how often its predictions are right. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Calibration (quantization)** | Collecting value ranges for activations on sample inputs before quantizing. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Canary** | A harmless word or marker that an agent would never produce unless it followed a payload. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Canary release** | A release that first shows a new model to a small share of traffic and rolls it back if quality drops. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Canary test** | Inserting random strings a known number of times into training data and measuring their exposure after training. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Capability evaluation** | Measuring what a system can do, including the things you do not want it to do. | [03.06](03-evaluation/06-evaluating-capabilities-and-risks.md) |
| **Capability negotiation** | The exchange at connection time in which a client and a server state which protocol features they support. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Capability tier** | A statement of what an agent may touch at a given level, with the evaluation that admits a model to it. | [03.06](03-evaluation/06-evaluating-capabilities-and-risks.md) |
| **Capacity planning** | Estimating the load, the cost per unit and the needed resources before building. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Capture the flag (CTF)** | A security contest with small problems to solve, used as benchmarks for agents. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Cascade (two-phase prediction)** | A design in which a small model decides whether to call an expensive one. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Catastrophic forgetting** | A neural network losing old knowledge when it learns something new. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Chain-of-thought (CoT)** (also called: Chain-of-thought prompting) | The reasoning steps a model writes before its final answer. Chain-of-thought prompting asks for them through worked examples or an instruction. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Chaos engineering** (also called: Chaos testing) | Injecting faults into a running system to test its robustness. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Chat model** | A model after post-training that follows instructions and converses, such as the models you call through an API. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Chat pattern** | The rule for who speaks next in a conversation and when it ends. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Chat template** | The fixed format, with roles, in which conversations are written for training and serving. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **Cheap talk** | Communication that costs nothing and binds nobody; useless in a two-player zero-sum equilibrium. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Cheese** | A cheap strategy that wins when the opponent is unprepared and tends to work across opponents. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Chinchilla rule of thumb** | About 20 training tokens per parameter for a compute-optimal model. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Chunk** | One piece of a document, a few hundred tokens, stored for retrieval. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **CIA triad** | The three classic security goals: confidentiality, integrity, and availability. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Classification model** | A model that predicts one label from a fixed set. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Classifier** | A small model that labels an input, for example harmful or harmless. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Classifier guidance** | Steering each sampling step of a diffusion model with the gradient of a separately trained classifier, multiplied by a strength | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Classifier-free guidance** | Steering that evaluates the diffusion model twice per step, with and without the condition, and blends the two estimates; it doubles the FLOPs | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Client (MCP)** | The part inside a host that holds one connection to a server. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Client-side deployment** | Running a model on the user's device. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **CLIP** (also called: CLIP embeddings) | A model trained on image-caption pairs so that each image's embedding matches its caption's. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |
| **Clipping** | Cutting a value range below its maximum so the remaining values get finer steps. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Closed-ended task** | A task with few possible answers, so a program can check them. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Cluster** | A group of observations that depend on the same source, such as repeated attempts on one task. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **Clustered standard error** | A standard error that treats each cluster as one source of evidence. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **CNOT** | Controlled NOT, a two-qubit gate that flips the target qubit only when the control qubit is 1. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Coalescing** | Combining the memory accesses of a warp's threads into a few full cache-line transfers. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Code action** | An action expressed as code or a shell command that does several things at once. | [02.07](02-building-agents/07-coding-agents.md) |
| **Code browser** | A tool that lets an agent jump to definitions and follow cross-references as an IDE does. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Codebook** | The small table of allowed values that each index points to in k-means quantization. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Codified knowledge** | The good practice that a community has written down; architectural styles and design patterns are this kind | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Coding agent** | An agent whose environment is a code base, which it reads, edits and runs. | [02.07](02-building-agents/07-coding-agents.md) |
| **Cohen's kappa** | Agreement between two labelers after removing the agreement expected by chance. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Cold start** | The delay before a fresh sandbox or process is ready to use. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Collective operation** | A communication pattern in which every rank takes part at once, such as all-reduce. | [10.06](10-llm-internals/06-parallelism.md) |
| **Common Crawl** | A public snapshot of web pages, used as raw material for pre-training data. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **common knowledge** | In Brown's wording, a strategy that the opponent knows, while the outcomes of its random choices stay unknown | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Compaction** | Shortening an agent's history by replacing older steps with a summary. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Complete mediation** | The principle that every access is checked, with no exceptions. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Complexity asymmetry** | The requirement that the simulated user stay less capable than the agent, so the task still needs the agent. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Component** | A part of a system with one responsibility. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Component mistake** | A wrong output from one part of a system. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Compound AI system** (also called: compound system, Hybrid system) | A modular program in which language models carry out specialized steps instead of answering as one black box. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Compression ratio** | Bytes of text per token; higher means shorter sequences. | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) |
| **Compute threshold** (also called: Training-compute threshold) | A limit on the computing power used to train a model, used to decide which models a rule covers. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **Compute-bound** | Limited by arithmetic rather than data movement. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Computer use** | Letting a model operate a desktop by receiving screenshots and returning mouse and keyboard actions. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Concept drift** | A change in the correct output for the same input. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Conditioning signal** | An extra input that tells a network which style to play. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Confidence interval** | A range that would contain the true value in a stated share of repeated evaluations; a 95 percent interval is the usual choice. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **Confidence score** | A number from 0 to 1 for how sure a model is about its prediction. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Confidentiality** | The goal that only authorized parties can read information. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Confusion matrix** | A table of true labels against predicted labels in which each off-diagonal cell is one kind of mistake. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Constrained flow** | A design in which people write the control flow and the model only fills in steps or picks options. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Construct validity** | Whether a measure captures the concept it was meant to capture. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Container** | An isolated package of code and dependencies that runs the same way on every machine. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Containment** | Limiting which parts of a system a failing component can affect. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Contamination** (also called: Dataset leakage) | The presence of test examples in a model's training data, so a score can come from memory. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Context engineering** | Deciding what enters the context window: compacting, selecting and loading on demand. | [02.06](02-building-agents/06-how-agent-system-designs-evolve.md) |
| **Context parallelism** | Splitting the activations of a long sequence across accelerators, as in ring attention, so that each one handles part of the context. | [10.06](10-llm-internals/06-parallelism.md) |
| **Context window** (also called: Context) | The maximum number of tokens a model can consider in one call, counted across input and output. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Continuous batching** | Adding new requests to the running batch as they arrive. | [10.08](10-llm-internals/08-inference.md) |
| **Continuous delivery (CD)** | Keeping every change that passes its checks ready to release through an automated process. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Continuous integration (CI)** | The practice of running the test suite on every change, in a clean environment, and refusing to merge a change that breaks it. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Contrastive loss** | A training objective that pulls a proof state and its useful premises close in the embedding space and pushes useless premises away. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Control divergence** | Threads in a warp taking different branches, which then run one after another. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Control flow** | The rule for who acts next: your code, the model, or another agent. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Control group** | The users who keep the old version in an experiment, for comparison. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Conversation programming** | Building an agent system as a conversation between agents, where the message history is the whole program state. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Convolution** | A layer in which each output depends only on a small window of inputs. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Copra** | An in-context theorem-proving agent that trains nothing and proposes steps for the proof assistant to execute. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Cost per prediction** | The operating cost of one prediction, including a share of the training cost. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Counterfactual explanation** | A statement of a small change to an input that would have produced a different prediction. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Coverage** | The share of code lines, branches, or requirements that a test suite executes. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Critical batch size** | The batch size beyond which doubling the batch saves less than half the steps. | [10.07](10-llm-internals/07-scaling-laws.md) |
| **Cross-entropy** | The usual training loss for classifiers, which rewards a high probability on the correct label. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **CUDA** | NVIDIA's programming language for writing code that runs on its GPUs. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **CUDA cores** | The other kind of unit on a GPU; work such as scaling runs on them, best after the main loop | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Curriculum** | A graded sequence of problems, one of the three ingredients Hubert names for systems that beat experts. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Cut set** | A group of basic events that together trigger the system failure. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **CVE** | A public identifier for one known vulnerability. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **CWE (Common Weakness Enumeration)** | A community-developed list, hosted by MITRE, of the kinds of software and hardware weaknesses that lead to security vulnerabilities. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |

## D

| Term | Definition | Defined in |
|---|---|---|
| **Dangerous-capability evaluation** | Measuring whether a system has crossed from "could not help with serious harm" to "could". | [03.06](03-evaluation/06-evaluating-capabilities-and-risks.md) |
| **Dashboard** | A live view of telemetry trends. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Data augmentation** | Training on transformed copies of the examples to reduce overfitting. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Data cache** | The store where a researcher agent keeps retrieved material for a writer agent. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Data engineer** | A specialist in large-scale data systems who pulls data out of many sources and moves it between systems, and who builds the ML pipelines. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Data flywheel** | The loop in which production failures become evaluation tasks that gate the next release. | [03.07](03-evaluation/07-evals-in-production.md) |
| **Data integrity** | Strict conformance of data to its schema. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Data lake** | Raw data in many shapes, kept cheaply until it is needed. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Data linting** | Heuristic checks for suspicious data encodings, such as placeholder dates and duplicates. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Data locality** | Keeping data close to the machines that read it. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Data mix** | The shares of different kinds of text, such as code, books, science or languages, in training data. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Data parallelism** | Replicating the model on every GPU and giving each a different slice of the batch. | [10.06](10-llm-internals/06-parallelism.md) |
| **data poisoning** | An attack on the training data, in pre-training or fine-tuning, that makes the model learn a backdoor | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Data provenance** | Tracking the origin of a value and who modified it, which builds trust in data and helps debugging. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Data quality** | Fitness of data for use by the model and the operators. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Data warehouse** | Curated data in a fixed shape, organized for analysis. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Data-science trajectory** | The particular order in which a project moves through data-science steps, such as goal-first or data-first. | [08.10](08-quality-assurance/10-process-models-planning-and-iteration.md) |
| **DDIM** | The denoising diffusion implicit model, a sampler that changes inference only, so that steps can be skipped while the FID stays stable | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Debate (with a judge)** | A run-time pattern in which several agents argue positions and a judge picks an answer. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Debt register** | A list of known shortcuts, each with its cost and its owner. | [08.11](08-quality-assurance/11-teams-and-technical-debt.md) |
| **Debugging** | Finding the cause of a failure that testing or monitoring revealed. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Decision boundary** | Where one label ends and the next begins, which a classifier learns. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Decision record** | A stored description of one production decision that ties its output to the exact inputs and versions that produced it. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Deduplication** | Removing repeated documents or passages from a data set. | [10.10](10-llm-internals/10-training-data.md) |
| **Deep gradient compression** | A 2017 method of Han's group: prune gradients, accumulate the rest locally, and add momentum correction, warm-up and gradient clipping to keep the accuracy. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Deep leakage from gradients** | Reconstructing a model's input data from its shared gradients. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Defense in depth** | Several layers of defense whose weaknesses differ, so that an attack has to defeat all of them. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Delayed gradient averaging** | Applying the averaged gradient from `d` iterations back while computation continues, with the worker's own stale share removed | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Delimiter** | A marker placed around data in a prompt to tell the model where the data begins and ends; it is a hint, not a wall. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Dense and sparse models** | A dense model runs every parameter on each call; a sparse model runs only a small part of the network. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Deployment latency** | The time from a finished model to a served model. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Depthwise convolution** | A convolution with one filter per input channel and no mixing between channels. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Dereference** | To follow a node's reference back to the source element it describes. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Design pattern** | A named, reusable solution to a design problem, with its known benefits and pitfalls. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Design space** | All combinations of design choices for a component. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Design vocabulary** | The shared names of standard designs, each standing for a whole solution and its trade-offs, so that a discussion can go straight to the qualities at stake | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Deskilling** | The loss of skilled work when automation leaves most people following a machine's instructions while a few maintain the machines. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Detection rate** | The share of attack tasks that a detector flags. | [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) |
| **Detector** | The rule or model that decides whether an observation is a problem. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |
| **Determinism** | The property of giving the same output for the same input every time. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Development copilot** | A model that works synchronously with a developer, one action at a time. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **DevSecOps** | Running automated security checks such as static analysis as part of continuous integration, so that security work belongs to the delivery pipeline instead of coming at the end. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Diagrammatic gap** | A step of a classical proof that nobody proves because the diagram makes it obvious, and that a proof assistant therefore needs to have formalized. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Differentiable** | Having a derivative, so that one can compute how the output changes when any parameter moves a little. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Differentiable augmentation** | Applying the same transformation to real and generated images during GAN training, so that the loss flows back through the transformation to the generator. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Differential privacy** | A guarantee that a training result is nearly the same whether or not one person's record is in the data. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Differential testing** | Comparing a model's output with a reference implementation or with several other models instead of with a label. | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **Diffusion model** | A generative model that produces an image by removing noise over many steps. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Direct injection** | A prompt injection in which the attacker types the instruction into the application. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Discriminator** | The half of a GAN that learns to tell real images from generated ones. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Distillation loss** | A penalty on the difference between the teacher's and the student's output distributions. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Distributed data parallel (DDP)** | Data parallelism in which every GPU holds a full copy of the model, each one takes its own slice of the batch, and the gradients are averaged after the backward pass. | [10.06](10-llm-internals/06-parallelism.md) |
| **Distribution (of inputs)** | The full range of real inputs and how often each occurs. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Doer-checker pattern** | A design in which a second component watches the effects of the component that acts and intervenes when they are wrong. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **DOM tree** | The page's source code represented as text, exact but often long and without layout. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Domain knowledge** | Expertise about the field the data comes from, such as how a shipment is really recorded, which the people who collect the data hold and the data scientists who use it often lack. Used in my addition to step 5, not defined as a term. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Domain randomization** | Varying physical parameters such as gravity and friction across simulated worlds so a policy still works in reality. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Dominated design** | A design that is worse than another on every quality attribute. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **DPO** | Direct preference optimization, which trains a model directly on preferred and rejected answer pairs without a separate reward model. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Draft model** | A small model that proposes the next few tokens for a large model to check in one pass. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Draft-Sketch-Prove** | A method that drafts an informal proof, turns it into a formal sketch with gaps, and lets automated provers fill the gaps. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Drift** | A change over time in the data or in the assumptions made about it. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Dropout** | A training method that randomly switches off parts of the model. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **DSPy** | A framework for writing language-model programs as declarative modules and optimizing them. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Dual control** | A setting in which both the agent and the simulated user can act through tools in a shared world. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Dual use** | The property of a technology that serves a peaceful and a hostile purpose, so that one and the same model can rescue and attack. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **dual-use** | Said of a technology that brings great benefits and, in the hands of attackers, enables harm | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **DualFormer** | A successor to Searchformer, trained on partially removed traces, that switches between a fast and a slow mode. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **DuoAttention** | A method that classifies attention heads into retrieval heads with full cache and streaming heads with a window. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Durable idea** | An idea that keeps its value across model generations because it has a mechanism, appears in several sources and has a metric. | [11.08](11-professional-practice/08-staying-current.md) |
| **dynamic benchmark** | A benchmark that updates or regenerates its test cases every week, month or season, so that it follows the data and is harder to game | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |

## E

| Term | Definition | Defined in |
|---|---|---|
| **Early stopping** | Training for fewer steps than planned, to limit overfitting. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Ecological validity** | How well an evaluation captures real use. | [10.09](10-llm-internals/09-evaluating-language-models.md) |
| **Economy of mechanism** | The principle that security controls stay small and simple. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Effector** | A part that acts, such as a motor in a robot. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **einops** | A library for tensor operations in which dimensions are written by name. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Elicitation** | The choice of prompts, techniques and environments that draws a capability out of a model. | [03.06](03-evaluation/06-evaluating-capabilities-and-risks.md) |
| **Elo** (also called: Elo score) | A rating built from pairwise wins, with the win probability given by a logistic formula. | [10.09](10-llm-internals/09-evaluating-language-models.md) |
| **Embarrassingly parallel** | Said of work that scales by copying it, with no coordination between the copies. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Embedding** | A list of numbers that stands for a piece of text, placed so that similar meanings get similar numbers. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Embodied agent** | An agent that acts through a body, physical or simulated. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Encoder** | A model part that turns an input into vectors that another model can read; a vision encoder turns an image into vectors for a language model. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |
| **End-state check** (also called: Execution-based evaluation) | A comparison of the final state of an environment with the goal state. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **End-user audit** | Letting users from minority groups try a system before it is released widely, to find discriminatory behavior that the developers did not test for | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **Ensemble** | Several models answering the same question in parallel, combined by average or vote. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Entanglement** | A joint state of two qubits whose measurements agree, 00 or 11, however far apart the qubits are | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Entangling capacity** | How strongly a circuit entangles its qubits, on the Meyer-Wallach scale from 0 to 1 | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Entropy** | The uncertainty in a model's choice of the next token; it is low when one token gets almost all the probability. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Entropy collapse** | A late stage of RL in which a model becomes certain of one answer per prompt and stops exploring. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Enum** | A closed list of allowed values for an argument. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Environment** | What an agent acts on and observes, such as a file system, a browser, an API or a database. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Environment injection** | Planting text in an agent's environment so that it acts on it; indirect injection with an agent as the target. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Epilogue** | The step after the main loop of a matrix multiplication kernel; a kernel that applies its scales there runs efficiently | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Epsilon (privacy budget)** | The knob of a differential privacy guarantee; smaller is stricter. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Equalized odds** | A fairness criterion requiring similar error rates across groups. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Escalation rate** | The share of attempts handed off to a person. | [03.07](03-evaluation/07-evals-in-production.md) |
| **Ethics washing** | The criticism that principles and funded research announced by companies serve chiefly to hold off regulation. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **ETL** | Extract, transform, load: the batch process that cleans data into one shape and fills a data warehouse. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Eureka** | A method in which a coding language model writes candidate reward functions and training results pick the best. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Eval-driven development loop** | A cycle in which each change is kept only if the evaluation improves beyond the noise and nothing regresses. | [03.01](03-evaluation/01-evaluation-is-the-product.md) |
| **Evaluation** | Measuring a model or prompt on held-out data with a metric. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Evaluation set** (also called: Test set) | A frozen collection of inputs with wanted outputs, used to measure a prompt or a model. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Event stream** (also called: Tape) | A single ordered log in which every action and observation of an agent is recorded. | [02.07](02-building-agents/07-coding-agents.md) |
| **Evidence check** | Verifying that the words a judge quotes as justification occur in the output it graded. | [08.05](08-quality-assurance/05-testing-generative-and-llm-components.md) |
| **Evidence gate** | A level of rollout that opens when a measurement passes, not when a launch date arrives. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **Evidence-based AI policy** | The position that rules about AI should rest on measured risk, and that measuring it is a research job. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **Exact match** | A score of 1 when the answer equals an accepted answer after normalization, else 0. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Excessive agency** | An agent holding more permission, autonomy, or trust than its task needs, which turns a small attack into a large effect. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Exemplar** | One worked example in a prompt. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Experience buffer** | A store of recent samples that a PPO implementation takes its updates from. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **Experience replay** | Storing each step of an agent's experience and reusing it many times in training. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Expert parallelism** | Placing different experts on different GPUs and routing tokens to them. | [10.06](10-llm-internals/06-parallelism.md) |
| **Explainability** | Whether a model can give a person useful reasons for one output, such as a reason code for one prediction. Understanding the model's internals is a separate property, interpretability. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Exploitability** | The expected loss per game of a strategy against a best response; zero at the minimax equilibrium. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Exploiter** | An agent trained to beat one frozen opponent or a whole population. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Exploration** | Trying varied actions, tools or environments during training so that better behavior can be found. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Exploratory audit** | A red team or an end-user audit: an unstructured search for problems that gives no score, and whose findings become requirements and tests | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **Exploratory data analysis** | Summarizing and plotting data to learn its shape before writing checks. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Exponent** | The bits of a floating-point number that set its power of two, and so its range. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Exposure** | The Secret Sharer metric: how much more probable a model makes an inserted canary than a random string it never saw. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Expressivity** | How much of the state space a circuit can cover | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **External validity** | Whether a measure still holds outside the data it was designed on. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Extra mistakes** | A slice's mistakes minus the mistakes the overall error rate predicts for a group of that size. | [08.03](08-quality-assurance/03-slicing.md) |

## F

| Term | Definition | Defined in |
|---|---|---|
| **Fail-safe by default** | The principle that a failure leaves the system in its safest state. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Fairness (allocation)** | Who gets the decision that matters: the loan, the interview, or the acceptance. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Fairness (as a quality attribute)** | Comparable accuracy and outcomes across groups of people. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Fake quantization** | Rounding values only to simulate low precision while storing them in high precision. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **False fail** | An output a person accepts that the judge fails. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **False negative** | A real positive case that the model did not flag: a miss. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **False negative rate** | The share of attacks a detector lets through. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **False pass** | An output a person rejects that the judge passes. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **False positive** | A case the model flagged that did not deserve it: a false alarm. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **False positive budget** | The largest share of benign inputs a detector may block or flag at a given action level, written down before the detector can block anything. | [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) |
| **False positive rate** | The share of legitimate inputs a detector blocks or flags. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Fashion item** | A name, a leaderboard record or a demo that has not been measured and is not expected to last. | [11.08](11-professional-practice/08-staying-current.md) |
| **Fault tree** | A diagram that starts from one system failure and shows which combinations of events cause it. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Feature** | One input variable of a model. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Feature encoding** | The step that turns a raw input into the feature vector a model expects. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Feature engineering** | The step that turns raw data into the inputs a model receives. | [08.07](08-quality-assurance/07-pipeline-quality.md) |
| **Feature flag** | A switch that turns new code on for selected users. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Feature importance** | How much a model's accuracy drops when it loses access to one feature. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Feature interaction** | A failure that appears only when components that each work as specified are combined. | [08.08](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) |
| **Feature store** | A central catalog of reusable feature-encoding code that can also precompute and cache feature vectors. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Feature vector** | The sequence of numbers that represents an input for a model. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Feature-level measure** | An online success measure designed for one feature, such as how many users switch it on, because a system-level number cannot say whether that feature helped. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Federated learning** | Training on user devices and sharing model updates with a server that averages them. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Feedback loop** | A cycle in which a system's predictions change the environment and so change the data the next model learns from. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Few-shot prompting** (also called: Few-shot) | Including a handful of worked examples in the prompt before the real input. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Fictitious play** | Self-play in which each player best-responds to the opponent's average play so far; the average converges. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **FID** | An image-quality score for generated images that is better when it is lower; it climbs as a GAN's or a sampler's output degrades. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **File localization** | Finding the files that a request is about. | [02.07](02-building-agents/07-coding-agents.md) |
| **Filter bubble** | A situation in which personalization shows a person only content that agrees with views they already hold. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Fine-tuning** | Training a copy of an existing model on new examples to change its behavior. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Fire drill** | A problem deliberately injected into a running system to confirm that monitoring alerts the right people. | [08.08](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) |
| **Fitness** | A candidate's score, typically accuracy under the cost constraint. | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) |
| **Fixed pipeline** | A workflow with a few hard-coded steps, each a model call. | [02.06](02-building-agents/06-how-agent-system-designs-evolve.md) |
| **Flakiness** | Variation in test results between runs caused by sampled outputs or judges rather than by the code. | [08.05](08-quality-assurance/05-testing-generative-and-llm-components.md) |
| **Flaky oracle** | A pass-or-fail check that can disagree with itself and with a person on the same output. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Flaky test** (also called: Flaky row) | A test that passes and fails on the same code. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Flash** | Non-volatile storage on a microcontroller that holds the program and the weights. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **FlashAttention** | A tiled, fused attention algorithm that never writes the full score table to main memory. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **FLOP** (also called: FLOPs) | One floating-point addition or multiplication, the unit of work. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **FLOP/s** (also called: FLOPS) | Floating-point operations per second, a unit of speed. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **FMEA** | Failure Modes and Effects Analysis: a table that lists, for each component, the ways it can fail, the effects, the detection and the mitigation. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Formal mathematics** | Mathematics written as source code in a proof assistant, where a compiling proof is correct. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Formal verification** | A mathematical proof that a design keeps a stated property. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Formaliser model** | The model that turns a problem into a Lean statement. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Forward process** | The step-by-step addition of Gaussian noise to a clean image that a diffusion model learns to reverse. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Foundation model** | A large general-purpose model trained by someone else and customized with a prompt. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Four-fifths rule** | A rule of thumb from US employment-law discourse that a disadvantaged group's selection rate be at least 80 percent of the other group's. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **FP16, BF16, FP8, FP4** (also called: bf16) | Floating-point formats with 16, 16, 8 and 4 bits; BF16 trades precision for the range of FP32. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Fraction** | The bits of a floating-point number after the leading one, also called the mantissa, which set its precision. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Frontier lab** | A company that builds the most capable models. | [03.06](03-evaluation/06-evaluating-capabilities-and-risks.md) |
| **Full fine-tuning** | Updating all the weights of a pre-trained model on new data. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Fully connected layer** | A layer in which every output has its own weight for every input; also a linear layer. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Fully sharded data parallel (FSDP)** | ZeRO stage 3: parameters are gathered before each layer runs and freed afterwards. | [10.06](10-llm-internals/06-parallelism.md) |
| **Function calling** | Passing tool contracts to the model and receiving a tool call in return. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Fusion** | Doing several operations in one kernel so intermediate results never reach main memory. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Fuzzer** | A program that feeds a target many generated or mutated inputs and waits for a crash. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Fuzzing** | Feeding a program many generated inputs and waiting for a crash. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |

## G

| Term | Definition | Defined in |
|---|---|---|
| **GAN** | Generative adversarial network: a generator and a discriminator trained against each other. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Gate** | An automatic check that fails a change when a metric regresses. | [03.07](03-evaluation/07-evals-in-production.md) |
| **Gated MLP** | An MLP variant that multiplies one projection by another element by element before the output projection. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **GeLU** | A smooth activation function similar to ReLU, common in Transformers. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **generalist** | One model for many tasks, from which smaller specialists are then derived by prompting, fine-tuning or distilling | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Generalization** | Performing well on inputs the model never saw during training. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Generation** (also called: Decode) | The phase that generates one token per step, limited by memory traffic. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Generative model** | A model that produces text or images rather than choosing a label. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Generator and critic** | A run-time pattern in which one agent produces and another checks it with new information. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Genetic algorithm** | A search that keeps the candidates that work, mutates them, and repeats. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Global surrogate model** | A small interpretable model trained to imitate a model's predictions. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Goal** | The end state an agent pursues, which something outside the model can check. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Goal layers** | The four levels of goals: organization, product, users and model. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Goal test** | The check that says a task is done. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Goal-Question-Metric** | A method that starts from a goal, lists the questions that show whether it is reached, and picks one measure per question. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Gold answer** | The known correct answer against which a verifiable reward checks the model's final answer. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Good enough** | The judgment that a model works well enough for one use on one data, which replaces "correct" for ML components. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Goodhart's law** | The observation that a measure stops being a good measure once it becomes a target. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **GPU** | A processor built to run many simple arithmetic operations in parallel, which is what neural networks need. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **GPU kernel** | A function that runs on the GPU. A fast kernel moves as little data as possible to the GPU's main memory and back. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Graceful degradation** | Reducing a system's function, after a failure, to keep operating safely. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Grader** | Code, or a judge, that turns one response into a score and a list of violations. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Gradient** (also called: Gradients) | The direction that raises the loss fastest; training steps the parameters the opposite way. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Gradient accumulation** | Adding up gradients over several small batches before updating the parameters. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Gradient compression** | Sending only the largest or a low-rank approximation of the gradients to cut communication. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Greedy decoding** | Always taking the single most probable next token. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Green agent** | In Berkeley's course project, the hosting agent that defines the assessment and reports the metrics. | [03.08](03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) |
| **Ground truth** | The known correct facts for a task, given to a judge so that it can tell an invention from a fact. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Grounding** | Tying each statement of an answer to a source fetched at run time. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Grounding (instruction proposal)** | Giving the instruction-writing model extra context: worked examples, a summary of the data and the program's code. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Grounding (multimodal)** | Linking a phrase in an instruction to the thing on screen or in the world that it refers to. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Group chat** | A chat pattern in which several agents share one history and a manager picks the next speaker. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Group fairness** | A fairness criterion requiring similar rates of positive outcomes across groups; also called demographic parity. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **group normalization** | A normalization layer that splits the channels into groups and normalizes each group on its own, used for a large channel count | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Group quantization** | Giving each small block of weights its own scale, needed at 4 bits and below. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Grouped convolution** | A convolution split into independent groups of channels, with weights divided by the group count. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Grouped-query attention (GQA)** | Attention in which several query heads share one key-value head, which shrinks the KV cache. | [10.08](10-llm-internals/08-inference.md) |
| **Grover's search** | The quantum algorithm for searching an unstructured space with a quadratic speed-up over classical search. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **GRPO** | An RL algorithm that samples several answers per question and reinforces those that score above the group's average. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **GT Sophy** | A racing agent trained with reinforcement learning in the Gran Turismo driving game. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Guardrail** (also called: input guard, output guard) | A check that runs on untrusted input before the model (an input guard) or on the model's output, including its tool calls (an output guard), and stops a mistaken or dangerous action before it reaches a user or a system. Guardrails are usually plain code. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Guardrail trigger** | A recorded event in which an attempt broke a rule. | [03.07](03-evaluation/07-evals-in-production.md) |
| **Guideword** | A fixed word such as *none*, *more*, *late* or *perturbed*, used to prompt failure ideas in HAZOP. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |

## H

| Term | Definition | Defined in |
|---|---|---|
| **Hallucinated reference** | A citation to a paper that does not exist. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Hallucination** | A false statement produced by a model, with no attacker involved. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Halo** | The border of pixels around a patch that neighboring patches must both read, causing repeated work. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Hammer** | A tool that calls external automated theorem provers from inside an interactive proof assistant; Sledgehammer and LeanHammer are examples. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Handoff** | A run-time pattern in which one active agent at a time passes the task, with context, to another. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Hard constraint** | A limit on a quality attribute that cannot be negotiated. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Hard negative** | A benign input that looks like an attack, kept in the evaluation set so that a detector's false positive rate is measured where the detector is most likely to be wrong. | [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) |
| **hard Swish** | A hardware-friendly stand-in for Swish: zero below −3, x above 3, and a simple expression between them | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Harms of allocation** | Harm in which a group receives fewer resources or a worse service because of a discriminatory decision. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Harms of representation** | Harm in which output skews how a group is portrayed, reinforces a stereotype, or demeans people, without allocating anything. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Harness (agent)** (also called: Scaffold) | The code around a model in an agent: its tools, context rules and stop conditions. | [02.06](02-building-agents/06-how-agent-system-designs-evolve.md) |
| **Harness (evaluation)** | The program that runs every task of a dataset on a system, scores each attempt and reports metrics. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Hazard** | A system condition in which an accident can happen. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Hazard analysis** | Working out with safety-engineering methods how component mistakes can add up to a system failure. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **HAZOP** | Hazard and Operability Study: a guided brainstorm that applies fixed guidewords to each component and output. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **HBM** | High bandwidth memory, the GPU's main memory: large, and slower to reach than the caches on the chip. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Head dimension** | The width of one attention head; by convention the heads' widths add up to the model width. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Hedge** | A self-play algorithm that picks regularized best responses and converges faster than fictitious play. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Held-out set** (also called: Held-out data) | Tasks that are never used while developing, so that a score on them still means something. | [03.07](03-evaluation/07-evals-in-production.md) |
| **Hessian** | The matrix of second derivatives of the loss, used to estimate a weight's importance. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Heuristic** | A rule of thumb that points out what looks like a problem, so it can miss real problems and flag harmless code. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Heuristic attack** | An attack payload written by a person, such as context ignoring or a fake completion. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Hidden stratification** | A label that looks uniform while hiding subgroups on which a model performs very differently. | [08.03](08-quality-assurance/03-slicing.md) |
| **Hippocampal indexing theory** | The theory that raw memories live in the cortex and an index in the hippocampus links them. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **HippoRAG** | A retrieval method with a structured index, inspired by the indexing of human memory. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Host (MCP)** | The AI application that connects to servers through clients. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Hostile stub** | A stub model that returns the failures you choose, such as an unknown label or a low confidence, so that guardrails and fallbacks can be tested. | [11.04](11-professional-practice/04-capstone-model-to-product.md) |
| **Hot standby** | A spare copy of a component that takes over when the main copy fails. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Human approval gate** | A pause before a critical action until a person approves it, showing the real arguments, with no answer meaning no action. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Human in the loop** (also called: Control point, Human oversight) | A design in which a person checks, confirms or can reverse a model-driven decision. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |
| **Hybrid deployment** | Splitting a model's work between the user's device and a server. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Hybrid layers** | A model that alternates full attention layers with cheaper layers such as sliding-window or state-space layers. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **Hyperparameter** | A setting that controls the learning process and is chosen by the developer, such as the learning rate or the architecture. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |

## I

| Term | Definition | Defined in |
|---|---|---|
| **i.i.d. assumption** | The assumption that training and test examples are independent draws from the same distribution seen in production. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Idempotent** | Said of an operation that has the same effect when repeated as when called once. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Im2col** | Rearranging convolution inputs into columns so the operation becomes matrix multiplication. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Imperfect information** | A game in which a player cannot see everything, as in poker. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Improper output handling** | Trusting model output enough to pass it to a shell, a database, or a URL without validation. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **In silico** | Done on a computer, without physical experiments. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **In-context learning** | A model picking up a task from the instructions and examples in its input, with no training step. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **In-place operation** | Writing a layer's output over its input buffer so both never exist at once. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Incident response plan** | A written plan for the kinds of trouble a team can anticipate, with people, procedures and recovery steps. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Incremental training** | Training that adds new data to an existing model without starting over. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Indirect injection** | A prompt injection in which the attacker plants the instruction where the application will read it. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Inference** | Calling a trained model on a new input. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Inference engine** | The program that loads a model and runs it; whether it has a fast kernel for a format decides if a smaller file is also faster. | [11.05](11-professional-practice/05-capstone-efficient-inference.md) |
| **Inference latency** | The time one prediction takes, usually reported as a percentile. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Inference throughput** | The number of predictions a component can make per unit of time. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Inference-time scaling** | Spending more computation per problem at inference time to raise accuracy. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **InfiniBand** | A network link for data centers; Han cites 400 gigabits a second for it, against up to 1 gigabit for Ethernet. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Influential instances** | Training examples that shape a model's decision boundaries far more than the others; often mislabeled outliers where training data is sparse. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Informal mathematics** | Mathematics written as prose, LaTeX or papers, which carries no guarantee. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Information flow control** (also called: Taint tracking) | Tracking labeled data as it moves through a system, also called taint tracking. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Infrastructure as code** | Describing servers, containers and pipeline steps in files under version control. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Injected dependency** | An external call or data source passed into a function as an argument so tests can replace it. | [08.07](08-quality-assurance/07-pipeline-quality.md) |
| **Injection monitor** | A separate program that reads another agent's event stream and flags instructions planted in untrusted data, without touching that agent's tools or workspace. | [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) |
| **Inline check** | A check on the path between the model and its effect, which can block and adds latency to every step. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |
| **Inner monologue** | A short piece of reasoning text an agent writes before each action. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Input schema** | A JSON description of the arguments a tool accepts. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **instance normalization** | A normalization layer whose set is the positions of one channel and one input | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Instruction hierarchy** | A model-level defense in which the model is trained to privilege some instructions over others. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Instrumentation** | The code added to a system so that it produces telemetry. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Integration test** | A test that several components work together, between a unit test of one component and a system test of the whole product. | [08.08](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) |
| **Integrity** | The goal that the system and its data are not altered, on purpose or by accident, and stay accurate. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Interface** | The contract for using a component: what goes in, what comes out, and what happens when it fails. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Interface contract** | Fixed inputs, outputs, latency, and cost limits that let model work and system work proceed independently. | [08.10](08-quality-assurance/10-process-models-planning-and-iteration.md) |
| **Interleaving experiment** | Showing each user one list that mixes results from two ranking models and counting which model's results get used. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Interpretability** | The degree to which a person can understand a model's internals. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Intrinsically hard problem** | A problem with no known hand-written solution, typically one that mirrors human perception. | [07.02](07-ml-in-production/02-when-to-use-ml-and-when-not-to.md) |
| **Intrusion detection** | Monitoring a running system for unusual behavior that signals an attack. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Invariant** | A rule that must hold for a model's outputs without saying what those outputs are. | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **IsoFLOP run** | A training run held to a fixed compute budget, used to compare model sizes at equal cost. | [10.07](10-llm-internals/07-scaling-laws.md) |
| **Iterative pruning** | Repeating prune-and-fine-tune in small steps instead of pruning once. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Iterative refinement** | Improving one candidate answer over several rounds using feedback. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |

## J

| Term | Definition | Defined in |
|---|---|---|
| **Jaccard similarity** | The size of two sets' intersection divided by the size of their union. | [10.10](10-llm-internals/10-training-data.md) |
| **Jailbreak** (also called: Jailbreaking) | An attempt by the person talking to a model to get past its safety training and obtain content its provider forbids. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **JSON** | JavaScript Object Notation, the bracket-and-quote text format that APIs use to exchange data. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **JSON Schema** | A formal description of what valid arguments look like. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **JSON-RPC** | A convention in which a request and its reply are JSON objects with a method name, parameters and an ID. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Judge** | Whatever answers a rubric question: a program, an LLM, or a person. | [08.05](08-quality-assurance/05-testing-generative-and-llm-components.md) |
| **Judge calibration** | Measuring, criterion by criterion, how often a judge agrees with human labels before it can block a merge. | [08.05](08-quality-assurance/05-testing-generative-and-llm-components.md) |

## K

| Term | Definition | Defined in |
|---|---|---|
| **K-means quantization** | Storing a small table of representative values and an index per weight. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Kernel** | In a convolution, the small weight table that slides over the input. On a GPU, a kernel is instead a small program; see GPU kernel. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Kill switch** | A flag that turns a model's action off while the rest of the system keeps running. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **KL divergence** | A measure of how one probability distribution differs from another, zero when they are identical. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **KL penalty** | A training term that keeps a policy close to a reference model. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **Knowledge assistant** | A system that answers over private data and produces reports, with retrieval, agent reasoning and deployment. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Knowledge cutoff** | The date after which a model saw no training data. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Knowledge distillation** (also called: Distillation) | Training a small student model to reproduce the outputs of a large teacher model. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Knowledge graph** | A structure that stores facts as nodes, one per concept, joined by links that name the relations. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **KV cache** | Stored keys and values of all previous tokens, kept so generation does not recompute them. | [10.08](10-llm-internals/08-inference.md) |

## L

| Term | Definition | Defined in |
|---|---|---|
| **Label** | The wanted output attached to a training input. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Label leakage** | A model learning a shortcut that predicts the label in the data but will not hold in production. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Lambda architecture** | A design in which batch jobs recompute everything on a schedule and stream processing keeps results fresh in between. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Large language model (LLM)** | A neural network that gives a probability for every possible next token of a text sequence. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **LaSR (symbolic regression with a learned concept library)** | A search for an equation that fits a data set which also names the abstract concepts behind each equation in natural language. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Latency** | The delay to complete one request. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Latency budget** | A written limit on how much time a check may add to each step of a system, fixed before the check goes on the path between a model and its effect. | [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) |
| **Latency table** | Per-operator timings measured once on the target device and summed to estimate a model's latency. | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) |
| **Latent diffusion** | Running a diffusion model in a compressed latent space instead of on pixels. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **layer normalization** | A normalization layer whose set is every channel and position of one input, so that each token is normalized before attention | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **LayerNorm** | Normalization that subtracts the mean and divides by the standard deviation, then scales and shifts. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Leading indicator** | A measure that is easy to observe now and is expected to move with later success. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **League** | A training population of main agents and exploiters that play each other. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Leaky ReLU** | A ReLU with a small slope on the negative side, so gradients flow there at the price of the sparsity | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Lean** | The proof assistant used by AlphaProof and by most of the systems in this part. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Lean-STaR** | A method that trains a model to think in natural language before each formal tactic. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Learned detector** | A classifier trained to label inputs or outputs as attacks. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Learning rate** | The size of the step a training loop takes at each update; a hyperparameter. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Least privilege** (also called: Principle of least privilege) | The principle that a component gets only the permissions its current task needs. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Least-to-most prompting** | Splitting a problem into subquestions and answering them easiest first. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Lemma** | A smaller theorem, already proved, that a later proof can apply as one step. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Levels of evaluation** | The four places a "does it work" question can sit: component, trajectory, outcome and online. | [03.01](03-evaluation/01-evaluation-is-the-product.md) |
| **Lineage** | How data flows between files and processes inside a system, as opposed to edits made to individual rows. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Linear attention** | Attention without the softmax, computed through a fixed-size state so cost is linear in sequence length. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **Linear quantization** | An affine mapping between integers and real numbers, `r = S (q - Z)`. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Linter** | A tool that flags suspicious or invalid code. | [02.07](02-building-agents/07-coding-agents.md) |
| **LIPS** | An inequality-proving system in which a language model proposes steps of two restricted types and symbolic reasoning verifies and prunes them. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **LLM agent** | An agent in which an LLM makes the step-by-step decisions. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **LLM-as-a-judge** (also called: LLM as judge) | A model that reads an output and scores it against criteria. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Load balancer** | A component that spreads requests across several copies of a service. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Load-balancing loss** | A training term that penalizes uneven use of experts. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **Locality-sensitive hashing** | Banding MinHash signatures so that similar documents become candidate pairs with high probability. | [10.10](10-llm-internals/10-training-data.md) |
| **Lock-in** | The cost of leaving a framework because your application has grown into its shape. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Logical qubit** | A qubit built from several physical ones by error correction. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Logits** | The raw scores a model outputs for each choice, before normalization. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Long-term memory** | Anything stored outside the context and loaded back later, such as files, a database or a search index. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **Loop tiling** (also called: Tiling) | Restructuring loops to work on small blocks that fit in cache. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Loop unrolling** | Repeating a loop body in code to remove loop overhead, at the cost of binary size. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **LoRA (low-rank adaptation)** | Low-rank adaptation: learning a weight update as the product of two small matrices, merged at deployment. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Loss** (also called: Loss function) | A cost function that returns one number for how wrong a model is on a set of examples. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Lost in the middle** | The finding that models use information from the middle of a long input worst. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Lottery ticket hypothesis** | The claim that a dense network contains a small subnetwork that trains as well from its original initial values. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **LSTM** | A recurrent network with a fixed-size memory that processes a sequence step by step; it came before Transformers. | [10.07](10-llm-internals/07-scaling-laws.md) |

## M

| Term | Definition | Defined in |
|---|---|---|
| **MAC** | One multiply-accumulate: a multiplication and an addition, counted as two floating-point operations. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Machine learning (ML)** | A way of producing a function by fitting its parameters to examples, instead of writing its logic by hand. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Machine-learning algorithm** | The procedure that creates a model from training data, used only during training, as a compiler is not needed at run time. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Magnitude-based pruning** | Removing the weights with the smallest absolute value. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Marginal risk** | The risk a model adds on top of the risk that already exists without it. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **Matchmaking** | The rule for which opponent a training agent plays next. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Mathlib** | The open-source Lean library of formalized mathematics. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Max tokens** | A request parameter that stops generation after a set number of output tokens. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **MCUNet** | Song Han's TinyML framework that pairs the TinyNAS architecture search with the TinyEngine inference library so that a model fits and runs on a microcontroller. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Measurement** | Reading a qubit; it returns one random classical bit and collapses the state | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Membership inference** (also called: Membership inference attack) | Learning whether a given record was part of a model's training data. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Memorization** | A model assigning much higher probability to text it saw in training than to text it did not. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Memory** | What an agent stores and re-reads between tasks and sessions. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Memory bandwidth** | The rate at which a chip can move data from its main memory to its compute units, in bytes per second; it caps the speed of a memory-bound model. | [09.01](09-efficient-deep-learning/01-why-efficiency-matters.md) |
| **Memory hierarchy** | The chain of storage levels from registers to cache to main memory, each larger and slower. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Memory layer** | Stored questions and answers that let an assistant keep context between conversations. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Memory poisoning** | Planting content in an agent's memory so that later tasks follow it. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Memory-bound** | Limited by data movement rather than arithmetic, because arithmetic intensity is below the chip's. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **meta-judge** | The part a model plays when it compares two of its own judgments and says which is better | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **meta-rewarding** | A method in which one model follows instructions, judges the responses and also judges its own judgments, so that it is trained on preference pairs between judgments as well as between responses | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Metamodel (stacking)** | A model that learns which of several other models to trust in which situation. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Metamorphic relation** | A rule stating how two outputs must relate when the inputs differ in a prescribed way. | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **Metric** (also called: Measure) | A number that summarizes model quality on a data set, such as accuracy. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Micro-batch** | One small piece of a batch, used to keep the stages of a pipeline busy. | [10.06](10-llm-internals/06-parallelism.md) |
| **Microcontroller** | A single chip with one processor core, a few hundred kilobytes of memory and no operating system. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Microservice** | A small, independently deployable process that other parts of the system call over a network. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **MicroVM** | A minimal virtual machine with its own kernel, used for strong isolation. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Mid-training** | Continued pre-training on a smaller amount of higher-quality data, to shift a model's strengths and extend its context. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Migration strength** | The exponent that sets how much quantization difficulty SmoothQuant moves from activations to weights. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **MILP** | Mixed integer linear programming, an optimization method for decisions with hard constraints. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **MimicGen** | A method that turns one human demonstration into many successful trajectories across varied scenes. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Mind2Web** | A 2023 offline web benchmark that compares an agent's steps with one recorded human demonstration per task. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **MinHash** | A signature of hashed shingles whose collision chance equals the Jaccard similarity. | [10.10](10-llm-internals/10-training-data.md) |
| **miniCTX** | A benchmark of theorems from real Lean projects that depend on long, cross-file context. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Minimal cut set** | A cut set that stops triggering the failure if any one of its events is removed. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Minimax equilibrium** | A set of strategies in which no player gains by changing only their own; in two-player zero-sum games it cannot lose in expectation. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Minimum detectable effect** | The smallest true difference an evaluation of a given size would count as evidence. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **MIPRO** | An optimizer that tunes instructions and demonstrations together with a Bayesian optimizer. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Mistake analysis** | A structured pass over a feature that lists how it fails and what keeps each failure from reaching a person. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Misuse** | Using a model or a system to cause harm, with no attack on the system itself. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Mitigation** | A change outside the model, such as routing inputs to a human, that limits the harm of a known weakness. | [08.03](08-quality-assurance/03-slicing.md) |
| **Mixed precision (inference)** | Giving different layers, or weights and activations, different bit widths. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Mixed-precision training** | Using bf16 for parameters, activations and gradients and fp32 for optimizer state. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Mixture of experts (MoE)** | A layer with many expert MLPs and a router that sends each token to a few of them. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **ML component** | The model plus the code that wraps it for inference: the request, the parsing, the retries. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **ML flywheel** (also called: Closed-loop intelligence) | The cycle in which more users produce more data, which produces better models, which attract more users. | [07.02](07-ml-in-production/02-when-to-use-ml-and-when-not-to.md) |
| **ML-enabled product** | A software product with machine-learning components. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **MLOps** | The practice of automating the ML pipeline so that deploying, updating and operating models is routine. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **MLP** (also called: feed-forward network) | The part of a block that processes each token on its own through two or three linear layers. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Model (machine-learned model)** | The learned function, with its fitted parameter values, that a running system calls. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Model card** | A one- or two-page description of a model's intended use, supported inputs, accuracy and limits. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Model compression** | The set of techniques that shrink a trained model's storage, memory or compute needs. | [09.01](09-efficient-deep-learning/01-why-efficiency-matters.md) |
| **Model Context Protocol (MCP)** | An open standard for connecting AI applications to external systems such as data sources and tools. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Model extraction** | Learning a copy of a model by querying it repeatedly. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Model FLOPs utilization (MFU)** (also called: Model FLOP utilization) | The FLOP/s a run achieves divided by the peak of the chip. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Model independence testing** | Checking whether two released models were derived from the same weights. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Model inspection** | Reading a model without test data, as a code review reads code, to judge whether the rules it learned are plausible or rest on a shortcut; a small model is read directly and a large one through an explainability tool | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Model interface** | The small boundary, such as `step(messages, tools)`, that hides the language model from the loop. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **Model inversion** | Reconstructing training data from a model's outputs. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Model retry** | The model choosing a different call after reading an error observation. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Model security level** | Dawn Song's L0 to L4 scale, from an accurate and secure model (L0) to a malicious one (L4); design for L2. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Model size** | The storage needed for a model's weights: parameters times bits per parameter. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Model-based planning (simulate-then-act)** | Imagining each candidate action with a world model and executing only the best. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Model-centric** | A view of ML work that stops at the model or at the pipeline that produces it and leaves out the rest of the system and its environment. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Module (DSPy)** | The strategy for carrying out a signature, such as a plain prediction or step-by-step reasoning. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Momentum** | An optimizer's running average of past gradients. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Momentum correction** | Accumulating the optimizer's velocity rather than the raw gradient when gradients are sent late | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Monitor (in Privtrans)** | The small privileged part of a program that holds permissions and exports a narrow interface; not the runtime monitor of chapter 05. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Monitor (runtime)** | A component that observes the events of a running system and raises findings. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |
| **Monte Carlo tree search (MCTS)** | A search algorithm that grows a tree of moves by repeatedly picking a promising node, simulating a completion and pushing the score back up the path. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Multi-agent system** | A system in which several agents with different roles interact. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Multi-head attention** | Attention split into several heads, each working on its own smaller slice of the query, key and value vectors. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Multi-head latent attention (MLA)** | Attention that caches one compressed vector per token and expands it to keys and values when needed. | [10.08](10-llm-internals/08-inference.md) |
| **Multi-hop question** | A question whose answer needs more than one fact, often from different documents. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Multi-query attention (MQA)** | Attention in which all query heads share a single key-value head. | [10.08](10-llm-internals/08-inference.md) |
| **Multimodal agent** | An agent that reads more than text, here screenshots as well as page source, and acts on what it perceives. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Multimodal model** | A model that reads or writes more than one kind of data, such as text and images. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Multiple comparisons** | The rise in false alarms that comes from testing many slices or hypotheses at once. | [08.03](08-quality-assurance/03-slicing.md) |
| **muP** | A set of rules for scaling initialization and learning rates with width so the best learning rate stays the same. | [10.07](10-llm-internals/07-scaling-laws.md) |
| **Must criterion** | A hard requirement asserted strictly for every test case. | [08.05](08-quality-assurance/05-testing-generative-and-llm-components.md) |
| **Mutation (attack generator)** | Rewriting or generating candidate attacks, by hand or by search, to raise the success rate. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Mutation and crossover** | Evolutionary steps that change one parent or combine two parents into a child architecture. | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) |
| **Mutation testing** | A measure of test-suite quality that injects small artificial bugs and counts how many the suite detects. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |

## N

| Term | Definition | Defined in |
|---|---|---|
| **N-gram model** | A language model that predicts the next token from counts of how often tokens followed a context. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **N-step return** | Scoring an action by the sum of several later rewards instead of one. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Nanobody** | A small protein that can bind a target, used in the Virtual Lab's COVID-19 case study. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Naptime** | The first name of Google Project Zero's project for finding vulnerabilities with language models. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Needle in a haystack** | A test that hides one fact at varying depths in a long document and asks the model to find it. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **needle-in-a-haystack test** | A test that hides one sentence, image or clip in a long input and checks whether the model finds it | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Nested chat** | A chat pattern in which a matching message starts a private sub-conversation whose summary returns as the reply. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Network augmentation** | Treating a tiny model as a subnetwork of wider models during training, to give it extra supervision. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Neural and symbolic decision making** | Splitting decisions between a learned model, which handles language and vague goals, and an algorithm, which handles constraints and guarantees. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Neural architecture search** | Automatically choosing a model's architecture from a defined search space under a cost constraint. | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) |
| **Neural component** | The model in a hybrid system, which turns text into text by probability. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Neural network** | A function built by stacking many simple arithmetic steps whose numbers are the parameters. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **NISQ era** | Noisy intermediate-scale quantum, the current period of noisy devices with few qubits | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **No-cloning theorem** | The rule that a quantum state cannot be copied, which blocks skip connections in quantum circuits | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **No-press Diplomacy** | The board game Diplomacy without the negotiation messages. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Node** | One machine of a cluster; GPUs in the same node are linked more tightly than GPUs in different nodes. | [10.06](10-llm-internals/06-parallelism.md) |
| **Non-determinism** (also called: Non-deterministic) | The property that the same input can give a different output, because the model picks text partly at random. | [03.01](03-evaluation/01-evaluation-is-the-product.md) |
| **Non-ML component** | Any part of the product that contains no model, such as the interface, API, queue or database. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Non-parametric memory** | Knowledge stored outside a model's parameters and retrieved when needed. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Non-transitivity** | The property that agents of equal strength beat each other in cycles. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Normalization layer** | A layer that rescales activations so training converges faster. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Notebook** | A file of code cells that are run one at a time, suited to exploration. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Novelty effect** | A change in user behavior caused only by a feature being new. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **NVLink** | The high-speed link between GPUs inside one node. | [10.06](10-llm-internals/06-parallelism.md) |

## O

| Term | Definition | Defined in |
|---|---|---|
| **Observability** | How well you can tell what a system is doing from what it reports about itself. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Observation** | What an agent receives back from its environment after an action. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Occupancy** | The share of a SM's thread slots that are in use. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Omni model** | A model that takes any combination of modalities in and produces any combination out. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |
| **On-call** | The rotation of people who answer alerts outside working hours. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **On-device training** | Adapting a model on the device where its data was created. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Once-for-all network** | One trained network that contains many sub-networks, each fit for a different device. | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) |
| **One-shot** | Putting exactly one example of the task into the prompt. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Online distillation** | Training several networks together so that they teach each other from the start. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Online metrics** | Numbers computed from production records, such as escalation rate or repeat contact. | [03.07](03-evaluation/07-evals-in-production.md) |
| **OP** | Any operation, including integer and bitwise ones, counted as one unit of work. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Open design** | The principle that security does not depend on keeping the design secret. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Open-ended task** | A task with many acceptable answers, which needs human or model judgments. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Open-source access** | Having the data, architecture and training procedure, which allows questioning every design choice. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Open-weight access** | Having the trained model itself, which allows fine-tuning, distillation and inspection. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Open-weight model** | A model whose parameters are published. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Operationalization** | The rule that computes a measure's number from raw observations. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Operations** | All tasks, infrastructure and processes for deploying, running and updating a system in production. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Optimization loop (red teaming)** | Dawn Song's frame for automatic red teaming: generate candidates, inject, score, feed back, update. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Optimizer (DSPy)** | A procedure that searches for better instructions and examples for every module of a program. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Optimizer state** | Running statistics an optimizer keeps to decide each step. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Oracle** (also called: External check, Test oracle) | A cheap, trusted procedure that says whether a result is correct, such as running a program. | [03.01](03-evaluation/01-evaluation-is-the-product.md) |
| **Oracle (red teaming)** | A rule that decides whether an attack succeeded, such as a canary in an answer or a change of state. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Oracle problem** | The difficulty of naming the expected output for an input, especially one that was generated automatically. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **orchestrator** | The agent that shows a person the plan and asks for approval before the other agents carry the sub-tasks out | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **OSWorld** | A 2024 benchmark of 369 tasks on a real desktop operating system, run in a virtual machine and scored by scripts. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Out-of-band check** | A check that runs beside the request path and reads the record of a run: it costs almost no latency but cannot block an action in time. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |
| **Out-of-distribution input** (also called: Out-of-distribution data) | An input that differs strongly from the data a model was trained on. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Outcome evaluation** | Grading whether an attempt reached the goal state. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Outcome validity** | The property that an evaluator's verdict faithfully reflects whether the task succeeded. | [03.01](03-evaluation/01-evaluation-is-the-product.md) |
| **outer product** | The product of one activation channel and one weight channel, the term that regression-based pruning switches off with its scaling factor | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Outlier** | A value far outside the usual range of the data. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Over-optimization** | A model learning to please a learned reward model in ways people did not intend. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Over-tainting** | Labeling so much data as untrusted that the labels stop being useful. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Overfitting** | Fitting the training examples so closely, by memorizing them, that performance on new inputs suffers. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **OWASP Top 10** | A public list from the Open Worldwide Application Security Project of the ten most critical security risks to web applications; OWASP also publishes lists for LLM and agent applications. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |

## P

| Term | Definition | Defined in |
|---|---|---|
| **p95 latency** | The time within which 95 of 100 requests finish. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Padding** | Zeros added around an input border so a convolution keeps the output size. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **PagedAttention** | Storing a KV cache in non-contiguous blocks that can be shared between requests with the same prefix. | [10.08](10-llm-internals/08-inference.md) |
| **Paired comparison** | A comparison of two versions on the same tasks, using each task's own difference. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **Pairwise judging** (also called: Side-by-side evaluation) | Comparing two outputs, which is better at ranking and subject to position bias. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Paper2Agent** | A system that turns a research paper into an interactive agent exposing the paper's methods. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Parameter** (also called: Parameters) | A value inside a model that training sets, such as a weight. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Parameter policy** | A policy that outputs the settings of an existing controller, such as a navigation stack, instead of raw actions. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Parameter-efficient fine-tuning (PEFT)** | Freezing the pretrained weights and training a small set of parameters instead. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Parameter-shift rule** | The analytic gradient of a circuit: run it twice with an angle moved up and down by π/2 and take half the difference | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Parameterized quantum circuit** | A circuit in which some gates carry learned angles and others are fixed; the model of quantum machine learning | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Parametric memory** | Knowledge stored in a model's weights. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Pareto front** | The designs left after dominated ones are dropped: each is better than the others on at least one quality. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Parse** | To turn a document into typed elements: text blocks, tables, figures. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Partial credit** | The fraction of a task's key phrases that appear in the answer. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Partial dependence plot** | A plot of how the output changes as one feature varies while the others are held still. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Partitioning** | Splitting data so that different parts sit on different machines. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **pass@k** | The chance that at least 1 of k independent attempts succeeds. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **pass^k** | The chance that all k independent attempts succeed; the reliability metric. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Patch-based inference** | Running a network's early layers one patch of the image at a time to cut peak memory. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Pattern completion** | Recovering a whole memory from partial cues. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Payload family** | A group of injection payloads that share one technique, such as context ignoring, a fake system message or a buried instruction. | [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) |
| **Peak activation size** | The largest set of intermediate values alive at the same moment, which sets the RAM a model needs. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Peak performance** | A chip's advertised maximum operations per second, which almost no model reaches. | [09.01](09-efficient-deep-learning/01-why-efficiency-matters.md) |
| **Penetration testing** | Attacking a system on purpose, the way a real attacker would, to find its weaknesses; a practice of software security next to red teaming | [08.04](08-quality-assurance/04-testing-without-oracles.md) |
| **Perfect information** | A game in which all players see the full state, as in chess. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Perplexity** | A model's average uncertainty about the next token on held-out text, computed from the probability it assigns; lower is better. | [10.09](10-llm-internals/09-evaluating-language-models.md) |
| **PI agent** | The agent that plays the principal investigator: it chooses the expertise a project needs and creates the specialists. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Pipeline** (also called: ML pipeline) | Everything that produces, deploys and updates an ML component. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Pipeline jungle** | A pipeline of ad hoc scripts whose order and dependencies are not written down. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Pipeline parallelism** | Placing consecutive layers on different GPUs and streaming micro-batches through them. | [10.06](10-llm-internals/06-parallelism.md) |
| **Placement** | The place where an injection payload is planted, such as an inbox message, an event's notes or a contact's note. | [11.03](11-professional-practice/03-capstone-monitoring-agent-for-prompt-injection.md) |
| **Plan** | A sequence of actions chosen before taking them. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Plan-then-execute** | Writing every step first and then carrying them out. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Plausibility check** | A soft check that flags data that looks wrong without being able to prove it wrong. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Point cloud** | A set of 3D points measured by a sensor such as LiDAR, mostly empty space. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Pointwise judging** | Scoring one output at a time. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Poisoning attack** | Manipulation of training data to degrade a model or plant a back door. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Policy** | The model being trained with reinforcement learning, viewed as the rule that chooses actions. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **Policy enforcement** | Checking every action an agent proposes against a written policy before the action runs. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Policy gate** | Code that routes every tool call through a policy check with a default of deny. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Policy gradient** | A reinforcement learning update that pushes up the probability of actions in proportion to their reward. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **Pooling** | A parameter-free layer that shrinks an activation map by taking the maximum or average of small blocks. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **popcount** | An operation that counts the ones in an array of bits; with a shift and an offset it gives the dot product of two sign vectors | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Population best response** | The best strategy against the mix of players actually present. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Position bias** | The tendency of a judge to favor the output listed first. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Position interpolation** | Rescaling rotary positions so a model trained on short contexts accepts longer ones. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Post-training** | Every training stage that comes after pre-training, which reuses the training loop with a new objective. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Post-training quantization** | Converting a trained model to low precision without retraining it. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Power analysis** | A calculation, made before running, of whether an evaluation is large enough to detect an effect of a given size. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **PowerSGD** | Sending each gradient matrix as two low-rank factors whose shape is the same on every node | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **PPO** | Proximal policy optimization, an RL algorithm that improves a model in small clipped steps. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Pre-norm** | Placing normalization on the branch that feeds a block, so the residual stream itself is untouched. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Pre-tokenization** | Splitting text with a regular expression before merging, so merges do not cross word boundaries. | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) |
| **Pre-training** | The first and largest training stage, which sets a model's parameters by next-token prediction on huge amounts of text. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Precision** | Of the cases a model flagged, the share that were real. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Precision (of a measure)** | How reliably a measurement gives the same value when repeated. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Prediction** | The output a model computes for a new input. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Prediction accuracy** | How well a model does on test data under a chosen measure; used instead of the ambiguous word "performance". | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Predictive validity** | Whether a measure tells you something about the outcome you care about. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Preference pair** | A prompt with two answers and a mark saying which one is better. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Prefill** | The phase that processes a whole prompt at once, limited by arithmetic. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Prefix (of a prompt)** | The unchanged beginning of a prompt, which prompt caching can reuse. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Premise order** | The order in which the facts of a problem are presented, which changes a model's answers. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Premise selection** | Choosing, among the hundreds of thousands of facts in a library, the few that an automated prover is given for a goal | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Pretrained model** | A model that someone else has already trained, which you can use as it is or adapt by fine-tuning. | [07.02](07-ml-in-production/02-when-to-use-ml-and-when-not-to.md) |
| **Privacy** | The ability of a person to control what information about them is shared and how it is used. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Privacy policy** | The public document describing what a system collects and how it may use and share it. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Privilege separation** | Splitting a system into parts with different permissions, so that a compromised part cannot borrow the permissions of another. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **privileged information** | Exact values that a simulator knows, such as the position and velocity of every joint, but a real robot cannot sense | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Probabilistic gradient pruning** | Updating only the parameters with the largest accumulated gradients, so that small noisy gradients are never computed | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Process violation** | A required tool call that is missing or out of order, or a forbidden tool call. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Profiling** | Recording which kernels ran and for how long, to see where time goes. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Progent** | Dawn Song's group's programmable privilege control for agents, with human-written baseline policies and task-specific contextual policies enforced on each action. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Program retry** | An automatic repeat of a failed call after a transient error. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Progressive distillation** | Training a student to replace two neighbouring teacher steps with one, halving the step count each round | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Project GR00T** | NVIDIA's effort, announced in March 2024, to build a generalist model as the brain of humanoid robots. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Projector** | The small layer that maps a vision encoder's output into the language model's embedding space. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |
| **Prompt** | The text sent to a model, which acts as the argument of a function. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Prompt (MCP primitive)** | A reusable prompt template that a server offers and a user picks. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Prompt caching** | Storing the processed form of a prompt prefix so that later requests with the same prefix are cheaper and faster to start. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Prompt design** | Writing the instructions and one to ten examples that go into a prompt. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Prompt engineering** | Writing, testing and versioning prompts as an engineering activity. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Prompt injection** | An attempt to make an application follow someone else's instruction instead of the owner's or the user's. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **Prompt leakage** | A model revealing its system prompt or other text it was meant to keep. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Prompt management** | Storing prompts with revision history and porting them across models. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Prompt sensitivity** | The tendency of outputs to change when the wording, order or formatting of a prompt changes slightly. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Prompt tuning** (also called: Prompt and prefix tuning) | Learning a vector to place in front of the prompt instead of writing examples. | [05.07](05-frameworks-and-multi-agent/07-agents-in-the-enterprise.md) |
| **Proof assistant** | A program, also called an interactive theorem prover, that checks each step of a formal proof; Lean, Coq and Isabelle are examples. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Proof reconstruction** | The step of a hammer that turns the proof found by an automated prover into a proof the interactive prover can check. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Proof state** | At one step of a formal proof, the list of what is known and what remains to be shown. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Propagation** | The spread of injected or false content from one compromised agent to others. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Protected attribute** | A feature that divides the demographic groups for which wrongful discrimination is a concern. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Provenance (lineage)** | The record of where a value came from and who modified it. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Prover model** | The model that proposes tactics for the current proof state. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Proxy** (also called: Proxy measure) | A measure that stands in for something that cannot be observed directly. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Prudent technical debt** | A shortcut chosen knowingly, recorded, and given a repayment plan. | [08.11](08-quality-assurance/11-teams-and-technical-debt.md) |
| **Pruning** | Setting weights to zero and leaving them out of storage or computation. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Pruning granularity** | The unit a pruning method removes: a weight, a vector, a kernel, a channel or a layer. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Pruning ratio** | The share of weights removed, chosen per layer. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |

## Q

| Term | Definition | Defined in |
|---|---|---|
| **QLoRA** | LoRA applied on a base model stored in 4 bits. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Quality assurance** | All activities that evaluate whether a system meets its requirements and its users' needs. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Quality attribute** | A measurable quality of a component, such as latency, cost, accuracy or robustness. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Quality requirement** | A requirement that says how well the software must do it, with a value and the conditions of measurement. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Quantization** | Constraining values to a small discrete set so that each needs fewer bits. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Quantization error** | The difference between a value and its quantized replacement. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Quantization granularity** | How many weights share one scale: a whole tensor, a channel, or a small group. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Quantization-aware training** | Fine-tuning a model with quantization simulated in the forward pass. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Quantum circuit** | The three stages of a quantum program: initialize the qubits, apply gates, measure, with optional classical post-processing | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Quantum simulator** | A classical program that computes a circuit's state vector, which a real device does not expose; its time and memory grow exponentially with the number of qubits. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Quantum supremacy** | A computation that a quantum device performs better than the best classical computer, shown by Google a few years before Lecture 22 | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Quantum utility** | A computation that is hard to run classically but not yet useful, demonstrated by IBM | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Qubit** | A quantum bit, the unit of information in a quantum computer. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Qubit mapping** | Choosing the physical qubits that carry a circuit and inserting SWAP gates where the device's topology requires them | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Query decomposition** | Splitting one question into sub-questions that can be answered separately. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Query, key and value** | The three vectors a token produces in attention: its query is compared with every key, and the scores weight a sum of the values. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |

## R

| Term | Definition | Defined in |
|---|---|---|
| **RAG (retrieval-augmented generation)** (also called: RAG stack) | Finding relevant passages and adding them to the prompt before the model answers. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Rank** | In LoRA, the width of the two small matrices, which sets how many parameters are trained. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Rate limit** | A service refusing calls beyond a quota. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **RDMA** | Direct memory access between machines that bypasses the CPU. | [10.06](10-llm-internals/06-parallelism.md) |
| **ReAct** (also called: Interleaved reasoning, ReAct loop, ReAct-style loop) | A method in which an LLM interleaves thoughts, actions and observations in a loop. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Reactive policy** | A policy that acts on its first choice without looking ahead. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Reasoning (in an agent)** | Thinking in written steps, as in chain-of-thought, which adds no outside knowledge. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Reasoning agent** | An agent that uses an LLM to reason in order to act. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Reasoning model** | A model trained with RL on checkable problems so that it writes a long chain of thought before its final answer. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Recall** | Of all the real positive cases, the share a model flagged. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Receptive field** | The set of inputs that one output value depends on. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Red teaming** | Playing the attacker against your own system, on purpose, before somebody else does. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Reduce-scatter** | Summing tensors across ranks and dealing the result out in slices. | [10.06](10-llm-internals/06-parallelism.md) |
| **Reduction in error** | The share of a baseline's mistake rate that a model removes. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Redundancy** | Running several independent copies or kinds of a component so that one failure does not stop the system. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Reference window** | An earlier period whose data is trusted and that a new batch is compared with. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Reference-based criterion** | A rubric criterion that checks the output against known facts. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Reference-free criterion** | A rubric criterion that can only judge the form of the output. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Reflection** (also called: Reflexion) | Having the model critique a finished run and write a lesson for the next attempt. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Reflection step** | A second prompt that checks an earlier draft and validates it. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Regression** | A metric that got worse in a new version compared with the previous one. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Regression gate** | A CI check that fails when the attack success rate rises above a baseline by more than a fixed allowance. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Regression test** | A test that fails if a previously fixed problem returns. | [08.03](08-quality-assurance/03-slicing.md) |
| **Regression-based mixing** | Trying data mixtures on small models, fitting mixture to loss, and choosing the best. | [10.10](10-llm-internals/10-training-data.md) |
| **Regret matching** | A self-play algorithm that gives more probability to actions that would have scored better, and converges faster than fictitious play. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Regularized best response** | A best response that gives each action a probability in proportion to how well it scores, instead of always picking the single best action. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Reinforcement learning (RL)** | Training by trial and error in which outputs that earn a higher reward are made more likely. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Rejection sampling** | Generating many answers and keeping only those that pass a checker or ranker. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Relational distillation** | A distillation loss that matches a relation between two tensors, such as a module's input and its output, or between the features of different samples, instead of the content of one tensor | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Reliability** | The absence of defects: how often a system or component performs as specified. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **ReLU** | An activation function that sets negative values to zero. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **ReLU6** | A ReLU whose output is limited to 6, a purely empirical limit that narrows the range to quantize | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Repeat contact** | A customer returning about the same issue within a fixed time, a sign of a wrong answer that looked fine. | [03.07](03-evaluation/07-evals-in-production.md) |
| **Replication** | Storing the same data on several machines so that one can fail. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Repository map** | A tree-shaped summary of a code base, built up front and placed in the context. | [02.07](02-building-agents/07-coding-agents.md) |
| **Representation control** | Changing the model's behavior by pushing its internal vectors along a direction tied to a property. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Representation engineering** | Reading and steering a model's behavior through its internal vectors, in a top-down way. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Representation reading** | Detecting a property of the upcoming answer from the model's internal vectors. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Reproducibility** | The ability to run the same version again and get the same result, or a result within a known margin. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **ReProver** | A theorem prover that retrieves useful known lemmas before proposing a tactic. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **REQ (requirement)** | A statement of a state you want in the world. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Requirements engineering** | The work of finding, negotiating and writing down what a system must do and how well. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Residual stream** | The vector a token carries from the first layer to the last, which blocks add to and never overwrite. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Resource (MCP primitive)** | Data that a server exposes for the application to read. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Responsible Scaling Policy** | A developer's public commitment that names capability thresholds and the measures it will meet before training or deploying a model above each one. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **Retrieval** | A search that puts matching documents into the prompt. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Retrieval hit rate** | How often the retrieval step fetches a chunk that contains the answer. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Retrieval poisoning** | Planting documents in a knowledge base so that they are retrieved and followed. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Retriever** | A model that ranks the premises of a library by how likely each is to help with the current proof state. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Reversible action** | An action that can be undone, so that a wrong prediction behind it usually does minor or temporary harm. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Revision** | A version of an artifact that replaces an earlier one in time. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Reward** | A score given to a model's output during training, which the model is trained to maximize. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Reward hacking** | Passing the grader without doing the task. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Reward model** | A model trained on preference comparisons to score answers. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Risk register** | A team's written list of risks, here kept in the six-question marginal-risk form. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **RLHF** | Reinforcement learning from human feedback: training a model to maximize a reward model trained on human preferences. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **RLVR (reinforcement learning with verifiable rewards)** | Reinforcement learning in which a program such as a test suite or answer check gives the reward. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **RMSNorm** | Normalization that only rescales by the root mean square, without subtracting a mean or adding a bias. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **RoboCasa** | A framework that generates many simulated kitchen scenes from which robot data can be produced. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Robustness** | The stability of a model's output when its input changes a little. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Robustness check at inference time** | Testing one prediction against the small input changes it should survive, so that a prediction that flips can be routed to a fallback or a person. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Rollback** | Returning a system to its previous version. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Rollout** | One run of a policy in an environment from start to finish. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Rollout level** | One step of a staged release, such as shadow, staff only, a small share of traffic, or all users, which opens on evidence and closes on a named stop condition. | [11.01](11-professional-practice/01-how-to-ship-an-llm-feature-end-to-end.md) |
| **Roofline plot** (also called: Roofline chart) | A graph of achieved FLOP/s against arithmetic intensity, rising until the chip saturates. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **RoPE** (also called: rotary position embedding, rotary position encoding) | A position method that rotates query and key vectors by an angle that depends on position, so attention scores depend on distance. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Round trip** | The requirement that decoding the encoding of a text returns the original text. | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) |
| **Router** | The small layer that scores each expert for each token in a mixture of experts. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **Router prompt** | A prompt that picks one option out of several and so sends a task down one path. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Router with specialists** | A run-time pattern in which a router sends each task to one specialist with its own tools. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Routing** | Sending each query to the model or agent best suited to it. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Rubric** | A list of short, concrete criteria, each checkable by reading the output. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Rule of three** | With zero successes in n independent runs, the true rate is below about 3/n with 95% confidence. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |
| **Rule of Two** | A rule of thumb that an agent should have at most two of: processing untrusted input, access to sensitive systems or data, and the ability to change data or communicate externally. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Run-time collaboration** | Several role-specialized agents exchanging messages while doing one task. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Runbook** | A short page that says what to do when a specific alert fires. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Runtime protection** | Any check that happens while an agent runs: input guards, output guards, information flow tracking, monitoring, and a human in the loop. | [04.05](04-safety-and-security/05-runtime-monitoring-and-detection.md) |

## S

| Term | Definition | Defined in |
|---|---|---|
| **Safety** | The prevention of harm from system failure, treated as a property of the whole system rather than of the model. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Safety engineering** | The field that developed FMEA, fault trees and HAZOP, long standard in aviation, medical devices and nuclear plants, and now applied to ordinary products that contain a model. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **Salient weights** | The few weight channels that matter most, identified by the activation distribution. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Sampler** | The part of an RL system that generates rollouts. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Sampling** | Choosing the next token according to the model's probability distribution. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Sampling noise** | Variation in results that comes from the random choice of each sampled token. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **Sandbox** (also called: Sandboxing) | An isolated environment with its own file system, processes, network rules and resource limits. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Sandwich prevention** | Repeating the instruction after the data, so that the nearest text before the answer is yours. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Sanitizer** | A tool that instruments a running program and crashes it when it does something forbidden. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Saturation** | The state in which every system scores near the top of a benchmark, so it no longer separates them. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Scalability** | The ability of a system to handle more work when given more resources. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Scale** | In linear quantization, the real size of one integer step. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Scaling law** (also called: Scaling laws) | A simple formula that predicts loss from a resource such as data, parameters or compute, fitted on small runs and extrapolated. | [10.07](10-llm-internals/07-scaling-laws.md) |
| **Schema (data)** | The expected structure of data: fields, types, allowed values, and constraints. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Schema drift** | A change in the structure of incoming data, such as a renamed column. | [08.06](08-quality-assurance/06-data-quality.md) |
| **Search space** | The set of candidate architectures a search may choose from. | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) |
| **Search strategy** | The rule for picking the next candidate, such as grid, random, reinforcement learning or evolution. | [09.05](09-efficient-deep-learning/05-neural-architecture-search.md) |
| **Searchformer** | A small transformer trained to output an A* search trace before the plan. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Security mindset** | The habit of designing as if any component could be compromised, any user could misbehave and any input could be malicious, with reduced risk rather than perfect security as the goal. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Seed** (also called: Random seed) | A number that fixes the random choices of a run, so that a training run or an evaluation attempt can be repeated exactly. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **seL4** | A formally verified operating-system kernel. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Self-consistency** (also called: Consensus) | Sampling several complete answers and returning the most frequent final answer. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Self-correction** | Asking a model to review and revise its own answer, which brings no net gain without an external check. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Self-debugging** | Improving generated code with feedback from running it and from unit tests. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Self-Discover** | A method in which the model picks the reasoning strategies that suit a task from a given list and composes them into a reasoning structure, with no written demonstrations | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Self-distillation** | Distillation in which the student has the same architecture and size as its teacher. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Self-play** | Training in which an agent improves by playing against copies of itself. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Self-preference** | The tendency of a model to rate its own output higher. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Self-regulation** | An organization's own principles and policies, which no one outside that organization enforces. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Self-rewarding language model** | A model that scores its own answers and trains on those scores in a loop. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Semantic noise** | Variation in results that comes from which questions were in an evaluation set and how they were worded. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **Sensemaking** | Reading large, complex or uncertain contexts. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Sensitivity analysis** | Measuring how much accuracy each layer loses at several pruning ratios. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Sequence parallelism** | Splitting the tokens of a sequence across machines. | [10.06](10-llm-internals/06-parallelism.md) |
| **Sequential chat** | A chat pattern in which the result of one conversation becomes the input of the next. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Sequential decomposition** | A chain of models that each perform one step of a task, often with plain code between them. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Serialized model** | A model stored as a file. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Server (MCP)** | A small program that exposes tools, resources and prompts to a host. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Server-side deployment** | Running a model on servers that the provider controls. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Server-side request forgery** | An attack that tricks a system into fetching a URL the attacker chose. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Serverless computing** | A cloud service that runs code only when a request arrives and bills per request. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Service-level agreement (SLA)** | A service-level objective written into a contract, with consequences for missing it. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Service-level objective (SLO)** | A target for an operational quality of the system or of one component. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Serving form** | The way a model is delivered: library, service, batch job or precomputed table. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Set and forget** | The antipattern of training a model once and never updating it. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Set-of-Mark** | A screenshot with numbered labels drawn on elements taken from the accessibility tree. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Shadow release** (also called: Shadow execution) | Running a new version on live traffic while users keep seeing the old one. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Sharding** | Splitting a tensor into slices that live on different GPUs. | [10.06](10-llm-internals/06-parallelism.md) |
| **Shared expert** | An expert that every token uses, in addition to the routed experts. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **Shared history** | The list of messages of a conversation; it can be printed, replayed and tested. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Shared memory** | Fast memory inside one streaming multiprocessor that the threads of a thread block share, used to reuse a value loaded from global memory. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Shor's algorithm** | The quantum algorithm that factors large integers with an exponential speed-up over classical machines. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **short-term memory** | Shunyu Yao's name for the context window of an agent: you can only append to it, its size is fixed, and it is gone when the task ends | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Should criterion** | A quality preference asserted as a pass rate over many cases. | [08.05](08-quality-assurance/05-testing-generative-and-llm-components.md) |
| **Side effect** | A change a tool makes outside its own run, such as sending an email, which a retry may repeat. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **SigLIP** | A contrastive image-text model that scores each pair on its own instead of across the batch. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |
| **sigmoid** | An activation function that stays between 0 and 1: easy to quantize, but its gradient vanishes at both ends | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Sign test** | A test that asks how often one model wins on the questions where two models disagree. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **Signal-to-noise ratio** (also called: Signal to noise) | A benchmark's real improvement signal divided by its noise, with the gain from doubling model size as the signal in Wang's lecture. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **Signature (DSPy)** | A declaration of the input fields and the output field of one step. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Sim to real** | Moving a policy trained in simulation onto a physical robot. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **SIMD** | Single instruction, multiple data: one instruction applied to several values at once. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Similarity-based explanation** | An explanation of a prediction that shows the nearest labeled training examples. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **Simulated workspace** | A fake environment, such as a calendar and a to-do list loaded from a file, that an agent can change only through its tools and that resets to the same state. | [11.02](11-professional-practice/02-capstone-task-agent-with-evals.md) |
| **Simulator** (also called: Environment simulator) | A program that imitates an environment so that trials are cheap. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Single control** | A setting in which the agent operates every tool and the user only talks. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Skill library** | Voyager's store of learned behaviors as executable code, each retrieved by its description. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Slave** | In Privtrans, the unprivileged part of a program that does the risky work with no permissions. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **Slice** | A subset of evaluation or production data selected by a slicing function and reported with its size. | [08.03](08-quality-assurance/03-slicing.md) |
| **Slice intersection** | A slice made from examples that belong to two or more other slices at once. | [08.03](08-quality-assurance/03-slicing.md) |
| **Slicing function** | A rule that decides whether an example belongs to a slice. | [08.03](08-quality-assurance/03-slicing.md) |
| **SmoothQuant** | A per-channel rescaling that moves quantization difficulty from activations into weights. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **SMT solver** | A program that decides whether a logical formula follows from given facts. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Softmax** | The function that turns scores into probabilities that add up to 1. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Software architecture** | The early design decisions that matter most for a system's quality requirements and are expensive to reverse. | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Software vulnerability** | A bug with security consequences, such as an out-of-bounds write or SQL injection. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Solution length** (also called: rollout length) | The number of tokens a model produces to finish a task. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Solver** | A program that returns a provably valid or optimal answer to a problem written in formal notation. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Sound self-play** | A self-play method that provably converges to a minimax equilibrium. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Sources file** | A personal list of primary sources, lecturers and benchmarks, with the date each was last checked. | [11.08](11-professional-practice/08-staying-current.md) |
| **Sparse attention** | Attention in which each query reads only a selected subset of earlier tokens. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **Sparse back-propagation** | Backpropagating only into selected layers and channels, so fewer activations must be stored. | [09.09](09-efficient-deep-learning/09-llm-post-training-and-on-device-training.md) |
| **Sparsity** | The fraction of a model's weights that are zero. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **SPEC (specification of the software)** | A statement of what the software must do. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Special token** | A reserved string such as an end-of-text marker that the tokenizer must keep intact. | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) |
| **Specification** | A description of what a component must do, which other developers rely on; ML components lack one. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Speculative decoding** (also called: Speculative sampling) | A small model drafts several tokens and the large model checks them in one pass, with output distributed exactly as the large model alone. | [10.08](10-llm-internals/08-inference.md) |
| **Spotlighting** | Marking where untrusted data begins and ends in a prompt so that the model can tell it from instructions. | [04.04](04-safety-and-security/04-defenses-guardrails-detection-and-secure-design.md) |
| **SPSA** | Simultaneous perturbation stochastic approximation, which perturbs all parameters at once and estimates every gradient from two evaluations | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **SQL injection** | An attack in which attacker-chosen text becomes part of a database query; in an agent the text can arrive through model output. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **SRAM** | The small, fast working memory that holds activations at run time and loses its content without power. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Stack machine** | A simple computer model whose program is a list of instructions that push values onto a stack and combine the top ones. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Stack trace** | The report a program prints when it crashes, written for developers rather than for the model. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Stakeholder** | Any person or organization with an interest in the system or affected by it. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Stale gradient** | A gradient from an earlier iteration that is applied late, as in delayed gradient averaging. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Standard error** | The typical distance between an estimate and the true value; for pass-or-fail scores the square root of p(1 − p)/n. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **State** | The situation an agent is in at one moment. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **State vector** | The list of complex amplitudes that describes a quantum system; it doubles in length with every qubit | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **State-space model** | A layer that keeps a fixed-size state updated at every step, such as Mamba-2. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **StateFlow** | A group chat that encodes a finite state machine: one agent per state, transitions fixed in advance. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Stateless** | Holding no memory between requests, as a plain RAG pipeline does. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Static analysis** | Inspecting code for problems without running it. | [02.07](02-building-agents/07-coding-agents.md) |
| **static benchmark** | A benchmark whose test cases never change, which makes comparisons reproducible but lets the fixed cases end up in training data | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Statistical test** | A calculation of how unlikely a result is if only chance were at work. | [08.03](08-quality-assurance/03-slicing.md) |
| **Statistically significant** | Unlikely to be caused by sampling noise alone; in practice larger than about two standard errors of the difference. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **Stdio transport** | Carrying protocol messages through a local program's standard input and output. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Stereotype bias** | A model tying a group to an attribute, such as one group getting "leadership" and another "abrasive". | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Stop condition** | An event that ends the agent loop: a final answer, a step limit, or a budget or timeout. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **Stop condition (rollout)** | A named event that sends a system back one rollout level. | [04.09](04-safety-and-security/09-policy-governance-and-standards.md) |
| **Stop reason** | A field in an API response that says why generation stopped. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Stop sequence** | A string that makes a model stop generating as soon as it writes it. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Straight-through estimator** | Passing the gradient through a rounding step as if it were the identity function. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Strategy** | A rule, possibly random, that picks actions in a game. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Stream processing** | Processing events from a queue as they arrive. | [07.09](07-ml-in-production/09-scaling-the-system.md) |
| **Streaming** | Sending a model's output tokens to the caller as they are produced. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Streaming multiprocessor (SM)** | One of the many processing units inside a GPU, each with its own small fast memory. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Streetlight effect** | Measuring what is easy to observe instead of what matters. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Stride** | How far a convolution's window moves per step. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Stringly-typed** | Said of a system whose essential design is entangled with incidental prompt wording. | [02.05](02-building-agents/05-compound-ai-systems-and-dspy.md) |
| **Structural pruning** | Removing whole neurons, channels or layers so that the matrices shrink. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Structured index** | A network of concepts and their links, stored beside the embeddings, that lets retrieval follow associations. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Structured output** | Model output constrained to a format such as JSON that code can parse. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Stub** (also called: Scripted model, stub model) | A deterministic fake that stands in for a real system behind the same interface. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Subcircuit** | A candidate circuit contained in a supercircuit, which inherits the supercircuit's parameters. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Super-population** | The infinite set of questions that an evaluation's questions were drawn from. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **Supercircuit** | A circuit large enough to contain every candidate, trained once so that its subcircuits can be ranked without training each. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Superposition** | A weighted sum of the 0 state and the 1 state, with two complex numbers as weights | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **Supervised fine-tuning (SFT)** | Continuing a model's training with the next-token loss on good answers to prompts. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Supervised learning** | Learning from pairs of input and label. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Supply chain attack** | An attack in which something imported, such as a model file, a package, or a data set, was already malicious. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **SurCo** | A method that learns a simple stand-in for a hard optimization objective and solves it with an existing solver. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **SWAP gate** | A two-qubit gate that exchanges the states of two qubits. | [09.11](09-efficient-deep-learning/11-course-summary-and-outlook.md) |
| **SWE-bench** | A benchmark of real GitHub issues, scored by the tests added with each fix. | [02.07](02-building-agents/07-coding-agents.md) |
| **SwiGLU** | A gated MLP that uses the Swish function. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Swish** | An activation function found by architecture search, x multiplied by the sigmoid of x, hard to build in hardware | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Symbolic component** | Ordinary code in a hybrid system, written and parsed by rules. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **symbolic regression** | Finding an equation from observations, for example a law of planetary motion from measurements of Mars | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Symmetric quantization** | Linear quantization with a zero point of zero, used for weights centered on zero. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Synthetic data** | Training text written or rephrased by a model. | [10.10](10-llm-internals/10-training-data.md) |
| **System** | All components working together toward one goal, inside an environment. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **System 1 thinking** | Fast, associative processing; in an LLM, the transformer itself producing an answer directly. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **System 2 thinking** | Slow, deliberate processing; in an LLM, procedures such as chain-of-thought or search built on top. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **System failure** | A violation of a system requirement in the real world. | [07.04](07-ml-in-production/04-planning-for-mistakes.md) |
| **System of record** | The database that holds the real state of a business, such as whether an order was refunded. | [03.07](03-evaluation/07-evals-in-production.md) |
| **System prompt** | A separate input field for instructions that apply to a whole conversation. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **System test** | A test that the whole product meets its requirements end to end, which verifies that the system was built right. | [08.08](08-quality-assurance/08-system-quality-end-to-end-tests-and-guardrails.md) |
| **System-level measure** | An online measure of the success of the whole product, such as revenue or retention, which is easy to collect and slow to move. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |

## T

| Term | Definition | Defined in |
|---|---|---|
| **T-shaped** (also called: T-shaped person) | Deep expertise in one specialty with working knowledge of the neighboring ones. | [07.01](07-ml-in-production/01-from-models-to-systems-and-products.md) |
| **Tacit knowledge** | What a designer knows from personal experience and has not written down | [07.05](07-ml-in-production/05-architecture-for-ml-systems.md) |
| **Tactic** | One small formal proof step, such as applying a known lemma. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Task** | One item of a dataset: an input plus what an acceptable result looks like. | [03.02](03-evaluation/02-a-minimal-eval-harness.md) |
| **Task agent** | An agent that carries out small office tasks such as scheduling a meeting or adding a to-do, in a simulated workspace. | [11.02](11-professional-practice/02-capstone-task-agent-with-evals.md) |
| **Task decomposition** | Splitting a goal into sub-goals inside a plan. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Task validity** | The property that success at a task demonstrates the capability you meant to measure. | [03.01](03-evaluation/01-evaluation-is-the-product.md) |
| **Teacher and student** (also called: Student, Teacher) | The large fixed model that provides targets, and the small model that learns from them. | [09.06](09-efficient-deep-learning/06-knowledge-distillation.md) |
| **Technical debt** | The future cost of a shortcut taken today. | [08.11](08-quality-assurance/11-teams-and-technical-debt.md) |
| **Telemetry** | The log lines, counts and measurements a system emits about itself. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Temperature** | A sampling parameter that rescales token probabilities: lower values make output more predictable, higher values more varied. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Temporal Shift Module** | Moving part of a video network's channels between frames to add temporal modeling with no multiplies. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Tensor** | A block of numbers with a shape; the form of all data, parameters and intermediate results in training. | [10.02](10-llm-internals/02-resource-accounting-flops-memory-and-arithmetic-intensity.md) |
| **Tensor core** | One of the matrix-multiply units on recent NVIDIA GPUs. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **Tensor cores** | One of the two kinds of unit on a GPU that a kernel can run on; the main loop of a matrix multiplication belongs on them | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Tensor parallelism** | Splitting each weight matrix across GPUs, with every GPU handling every token. | [10.06](10-llm-internals/06-parallelism.md) |
| **ternary weight networks** | Networks whose weights are quantized to +1, 0 and −1 by a threshold at 0.7 times the average absolute value | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Test-time RL** | Training the prover on one target problem by solving easier generated variants and learning from each. | [06.04](06-frontier-applications/04-agents-for-formal-mathematics.md) |
| **Test-time sampling** | Running one agent several times in parallel and keeping one result. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Testing** | Executing software with selected inputs in a controlled setting to check that it behaves as expected. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Testing in production** | Evaluating a running system in real conditions on real users and data. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Text agent** | An agent whose actions and observations are both in language. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **The World and the Machine** | The distinction between statements about the real world and statements about the software. | [07.03](07-ml-in-production/03-goals-and-requirements.md) |
| **Theory of mind** | Reasoning about what other agents believe and intend. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **thought preference optimization** | Weston's follow-up to self-rewarding models: the model is trained by DPO to write a chain of thought on tasks with no verifier, with a judge scoring only the final response | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Thread block** | A group of GPU threads that share memory and run on one SM. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Threat model** | A written answer to three questions about a system before defenses are built: what must be protected, who would attack it, and where their input can enter. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Threat modeling** | A structured review of a system's design for security threats, in five stages. | [08.14](08-quality-assurance/14-security-privacy-transparency-and-accountability.md) |
| **Threshold** | The score above which a model's output is treated as the positive class. | [08.02](08-quality-assurance/02-measuring-model-quality.md) |
| **Throughput** | The number of tasks a system finishes per unit of time, such as requests, tokens or video frames per second. | [09.02](09-efficient-deep-learning/02-neural-network-basics-for-efficiency.md) |
| **Time per output token** | The delay between consecutive generated tokens. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Time to first token** | The delay before the first output token appears, spent mostly on processing the prompt. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **Time-boxed spike** | A fixed-length experiment that answers whether a problem is tractable. | [08.10](08-quality-assurance/10-process-models-planning-and-iteration.md) |
| **TinyChat** | Han's inference engine for 4-bit language models: low-level code under a Python interface, for processors from cloud GPUs to edge devices | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **TinyEngine** | The inference library that executes a searched model efficiently on a microcontroller. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **TinyML** | Machine learning on devices with kilobytes of memory and milliwatt power budgets, typically microcontrollers. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **TinyNAS** | A two-stage architecture search that first scales the search space to a tiny memory budget, then searches inside it. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Token** | A short chunk of text from a fixed vocabulary that a model reads or writes as one unit. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Tokenizer** | The program that cuts text into token IDs and converts tokens back to text. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Tokenizer-free model** | A model that reads raw bytes without a separate tokenizer; not yet proven at frontier scale as of the lecture. | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) |
| **Tool** | An ordinary function with a name and a description that the program runs on the model's behalf. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **Tool (MCP primitive)** | A function that a server exposes and a model may call. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Tool call** | The model's structured request to run one tool with given arguments. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **Tool contract** | The name, description and argument schema that the model sees for one tool. | [02.02](02-building-agents/02-tool-design-and-function-calling.md) |
| **Tool generalization** | Using tools the model has never seen by following their descriptions. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Tool poisoning** | Hiding an instruction in a tool's description, which the model reads when it decides which tool to call. | [04.03](04-safety-and-security/03-agent-specific-attacks.md) |
| **Top-p (nucleus sampling)** | A sampling parameter that keeps only the smallest set of tokens whose probabilities add up to p. | [01.04](01-foundations/04-using-llms-tokens-context-and-sampling.md) |
| **TPU** | Google's machine-learning accelerator, structured like a GPU with a larger matrix-multiply unit. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Trace** | The recorded trajectory of one production attempt, with versions, cost and outcome. | [03.07](03-evaluation/07-evals-in-production.md) |
| **trained ternary quantization** | Ternary quantization in which the network learns two scales, one per sign, instead of one fixed scale | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Trainer** | The part of an RL system that updates the weights. | [02.08](02-building-agents/08-training-models-for-agentic-tasks.md) |
| **Training** | The optimization loop that changes parameters to lower the loss on the training data. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Training data** | The examples a model learns from. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Training data extraction attack** | An attack that makes a model print a piece of its training data. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Training latency** | The time needed to train or retrain a model. | [07.06](07-ml-in-production/06-quality-attributes-of-ml-components.md) |
| **Training loss and test loss** | The model's error on the data it learned from, and on data it never saw. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Training set** | The part of the data that the training loop learns from. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Training-serving skew** (also called: Training–serving skew) | A mismatch between training and serving: the code that prepares inputs differs, or the production data differs from the training data. | [07.07](07-ml-in-production/07-deploying-a-model.md) |
| **Training-time multi-agent** | Using a population of agents to train or select one agent. | [05.05](05-frameworks-and-multi-agent/05-multi-agent-systems-ii-the-llm-era.md) |
| **Trajectory** (also called: Transcript) | The ordered record of one attempt: every message, tool call and result. | [03.01](03-evaluation/01-evaluation-is-the-product.md) |
| **Trajectory evaluation** | Grading whether the steps an agent took were allowed. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Transformer** | The network architecture behind LLMs, built from stacked layers that use attention. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Transparency** | That the people who depend on a system can find out what it does, where it fails, and what was tested. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Transport** | The channel that carries protocol messages between client and server. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **Treatment group** | The users who see the new version in an experiment. | [08.09](08-quality-assurance/09-testing-and-experimenting-in-production.md) |
| **Tree search** | Exploring several next steps at each point of a solution, judging partial solutions and backtracking. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Tree search (inference-time)** | Branching in the middle of a run and using a judge to rate intermediate states before continuing. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Tree-of-thought** | Tree search applied to reasoning steps written by an LLM. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Triton** | A language in which a kernel is written at the level of what each thread block does. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Trust boundary** | A line where data crosses from one party to another; in an agent every tool result and fetched page crosses one. | [04.01](04-safety-and-security/01-threat-modeling-llm-applications-and-agents.md) |
| **Turn limit** | A cap on how many messages a conversation may contain before the runtime stops it. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Two-agent chat** | A chat pattern in which two agents alternate until a stop condition holds. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **Type checker** | A static analysis, as in Java, that can guarantee its one kind of mistake is absent when it reports nothing, at the cost of false warnings. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |

## U

| Term | Definition | Defined in |
|---|---|---|
| **Ultimatum game** | A game in which one player splits a sum and the other accepts the split or leaves both with nothing. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |
| **Unconstrained flow** | A design in which the model chooses the next step among the tools it was given. | [05.01](05-frameworks-and-multi-agent/01-the-agent-framework-landscape.md) |
| **Undeclared consumer** | A script that depends on data whose origin nobody declared. | [07.08](07-ml-in-production/08-automating-the-pipeline.md) |
| **Unicorn** | A developer said to combine expertise in modeling, software engineering, product and the domain, whom Kästner considers rare or nonexistent. | [08.11](08-quality-assurance/11-teams-and-technical-debt.md) |
| **Unintended memorization** | Memorization of training data that is irrelevant to what the model was meant to learn. | [04.07](04-safety-and-security/07-trustworthiness-beyond-injection.md) |
| **Unit test** | A test of one function or component in isolation. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Universal self-consistency** | Letting a model choose which of several free-form answers is most consistent with the others. | [01.06](01-foundations/06-reasoning-in-llms-from-chain-of-thought-to-search.md) |
| **Unpaired comparison** | A comparison of two runs that were made on different questions. | [01.07](01-foundations/07-why-llm-outputs-are-noisy.md) |
| **Upcycling** | Initializing a mixture of experts from a trained dense model. | [10.04](10-llm-internals/04-attention-alternatives-and-mixture-of-experts.md) |
| **User proxy agent** | An agent that speaks for the user: it carries the request in and may run code or ask the user. | [05.02](05-frameworks-and-multi-agent/02-autogen-conversation-programming.md) |
| **User simulator** | A model that plays the customer from a short instruction. | [03.04](03-evaluation/04-evaluating-agents-trajectories-and-environments.md) |
| **Utility** | The task success rate on benign tasks, reported beside the attack success rate. | [04.06](04-safety-and-security/06-red-teaming-and-safety-evaluation.md) |

## V

| Term | Definition | Defined in |
|---|---|---|
| **V-model** | A planning practice that pairs each design activity with the test activity that will check it. | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Validation** | Checking that a system meets the users' needs: did we build the right system? | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Validation set (dev set)** (also called: Validation data) | The part of the data used to make choices while developing. | [01.01](01-foundations/01-machine-learning-in-a-nutshell.md) |
| **Value function** | A model that estimates how close a run is to success; tree search uses it to score intermediate states. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Value model** | A second network, as large as the policy, that estimates the reward to come at each token; PPO needs it and GRPO drops it. | [10.11](10-llm-internals/11-post-training-sft-rlhf-and-rlvr.md) |
| **Variant** | A bug similar to one already found, in another place in the same project. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Variant (A/B test)** | A version of an artifact that exists side by side with another, such as the two models of an A/B test. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Variant analysis** | Searching a project for bugs similar to one that was just fixed. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Vector** | An ordered list of numbers. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Vector database** | A store that finds the vectors nearest to a query's embedding. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Vector search** | Finding the stored chunks whose embeddings are closest to the embedding of a question. | [02.04](02-building-agents/04-memory-and-knowledge-for-agents.md) |
| **Velocity** | The optimizer's momentum term, a running combination of past gradients that updates the weights in place of the raw gradient. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Velocity, validation, versioning** | Three goals of MLOps practice named in an interview study: fast iteration, automated checking with quick feedback, and keeping versions for recovery. | [07.10](07-ml-in-production/10-planning-for-operations.md) |
| **Verbosity bias** | The tendency of a judge to score longer outputs higher when they add nothing. | [03.03](03-evaluation/03-llm-as-a-judge-and-rubrics.md) |
| **Verifiable reward** | A reward that a program computes by checking an answer, such as a string match or a passing unit test. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Verification** | Checking that an implementation meets its specification: did we build the software right? | [08.01](08-quality-assurance/01-quality-assurance-basics-and-the-oracle-problem.md) |
| **Verifier** | A program or rubric that judges whether a model's output or trajectory succeeded. | [01.03](01-foundations/03-from-base-model-to-assistant-post-training.md) |
| **Versioning** | Giving every input to a result an identifier: code, prompts, data, models, and settings. | [08.12](08-quality-assurance/12-responsible-engineering-versioning-and-reproducibility.md) |
| **Virtual Lab** | An open-source platform in which a PI agent assembles specialist agents that meet to do research. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **Virtual machine (VM)** | A simulated computer, used so that a ruined state costs one reset. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Vision transformer** (also called: ViT) | A transformer applied to an image cut into patches. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Vision-language model (VLM)** | A language model that also accepts images. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **VisualWebArena** | A 2024 extension of WebArena with tasks that need images. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **Vocabulary** | The fixed list of all tokens a model can use. | [01.02](01-foundations/02-how-large-language-models-are-trained.md) |
| **Vocabulary size** | The number of distinct tokens a model can read or produce. | [10.01](10-llm-internals/01-the-language-modeling-pipeline-and-tokenization.md) |
| **voice sommelier** | The person at Sierra, under an unofficial title, who listens to voices, rates them on a fixed set of dimensions and matches them to a company's brand | [03.07](03-evaluation/07-evals-in-production.md) |
| **Voyager** | An open-ended agent that plays Minecraft with no fixed goal, saving each learned behavior as code in a skill library. | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **VQ-VAE** | A network that compresses an image into a list of discrete codes and reconstructs it. | [10.12](10-llm-internals/12-alignment-and-multimodality.md) |

## W

| Term | Definition | Defined in |
|---|---|---|
| **W4A16** | Shorthand for 4-bit weights with 16-bit activations. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Warm-up** | Starting a training run with a small learning rate and little gradient pruning and raising both, because the weights move fastest early in training | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Warp** | A group of 32 threads that execute the same instruction at the same time. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Wave quantization** | Idle SMs in the last round of thread-block scheduling when blocks do not divide evenly among SMs. | [10.05](10-llm-internals/05-gpus-tpus-and-kernels.md) |
| **Weak supervision** | Producing training labels with rules instead of hand labeling. | [08.03](08-quality-assurance/03-slicing.md) |
| **Web agent** | An agent that uses software through its interface, as a person does. | [05.06](05-frameworks-and-multi-agent/06-agent-infrastructure-sandboxes-browser-use-and-protocols.md) |
| **WebArena** | A 2023 benchmark of self-hosted clones of a shopping site, Reddit and GitLab, scored by execution. | [06.01](06-frontier-applications/01-multimodal-agents-web-and-computer-use.md) |
| **WebShop** | A shopping environment built on 1.16 million Amazon products, used to evaluate web agents. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Weight decay** | A penalty that pulls weights toward zero during training. | [10.03](10-llm-internals/03-transformer-architectures-and-hyperparameters.md) |
| **Weight-only quantization** | Quantizing the weights while activations stay in higher precision, suited to one-user serving. | [09.08](09-efficient-deep-learning/08-efficient-llm-inference-and-deployment.md) |
| **Wet lab** | Experimental work with real reagents and materials. | [06.03](06-frontier-applications/03-agents-for-scientific-discovery.md) |
| **White agent** | In Berkeley's course project, a participant agent: the one being tested. | [03.08](03-evaluation/08-case-study-the-green-agent-and-white-agent-project.md) |
| **White-box attack** | An attack that uses access to the model's internals, for example to follow gradients. | [04.02](04-safety-and-security/02-jailbreaks-and-prompt-injection.md) |
| **whole-body control** | Coordinating the motors of arms and legs so that a humanoid stays balanced, walks and manipulates | [06.02](06-frontier-applications/02-embodied-agents-and-robotics.md) |
| **Window attention** | Attention restricted to a local window of patches, with linear instead of quadratic cost. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **Winograd convolution** | A transformation that computes a 3 × 3 convolution with fewer multiplications. | [09.07](09-efficient-deep-learning/07-tinyml-microcontrollers-and-tinyengine.md) |
| **Workflow** | A set of LLM calls connected by code that decides their order. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Workflow (LlamaIndex)** | Event-driven steps that pass messages, where a step can be plain Python or a model call. | [05.03](05-frameworks-and-multi-agent/03-llamaindex-knowledge-assistants.md) |
| **Workflow-to-agent spectrum** | The scale from a single prompt through a fixed workflow and a bounded loop to an agent and a multi-agent system, measured by who decides the next step. | [01.08](01-foundations/08-a-short-history-of-llm-agents.md) |
| **Working memory** | The part of memory that lives in the context window and is paid for at every step. | [02.01](02-building-agents/01-the-anatomy-of-an-agent.md) |
| **World model** | A model that predicts the next state from a state and an action. | [02.03](02-building-agents/03-planning-search-and-decision-making.md) |
| **Wrapper** | An application that is only a prompt and one model call behind an API. | [02.06](02-building-agents/06-how-agent-system-designs-evolve.md) |
| **Wrongful discrimination** | Use of a protected attribute in a decision that is not justified in that domain, such as a customer's sex in a mortgage decision. | [08.13](08-quality-assurance/13-explainability-fairness-and-safety.md) |
| **WSD schedule** | A learning-rate schedule with warmup, stable and decay phases, which lets checkpoints be reused. | [10.07](10-llm-internals/07-scaling-laws.md) |

## Z

| Term | Definition | Defined in |
|---|---|---|
| **z-score** | A gap divided by its standard error. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **ZeRO** | Data parallelism with the optimizer state, gradients and, in stage 3, parameters sharded across GPUs. | [10.06](10-llm-internals/06-parallelism.md) |
| **Zero point** | In linear quantization, the integer that stands for the real number zero. | [09.04](09-efficient-deep-learning/04-quantization.md) |
| **Zero-day** | A vulnerability that was previously unknown to the software's authors. | [04.08](04-safety-and-security/08-ai-for-cyber-defense-and-vulnerability-detection.md) |
| **Zero-shot CoT** | Triggering reasoning steps with an instruction only, such as asking the model to think step by step. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Zero-shot prompting** (also called: Zero-shot) | Giving the instruction only, with no examples. | [01.05](01-foundations/05-prompting-and-in-context-learning.md) |
| **Zero-sum** | Describes a game in which one player's gain is exactly the other's loss. | [05.04](05-frameworks-and-multi-agent/04-multi-agent-systems-i-games-and-self-play.md) |

## Numbers

| Term | Definition | Defined in |
|---|---|---|
| **2:4 sparsity** | A fixed pattern with at most two non-zero weights in every block of four, which supporting hardware can skip. | [09.03](09-efficient-deep-learning/03-pruning-and-sparsity.md) |
| **3D CNN** | A convolutional network whose kernels also run over time, so it models low-, middle- and high-level information jointly at the price of four-dimensional weights. | [09.10](09-efficient-deep-learning/10-efficient-vision-generative-models-and-distributed-training.md) |
| **90th percentile** | The value that 9 of 10 attempts stay below; a tail measure that reports slow cases a mean hides. | [03.07](03-evaluation/07-evals-in-production.md) |
| **95% confidence interval** (also called: 95% interval) | A range built so that it would contain the true value in 95% of repeated evaluations. | [03.05](03-evaluation/05-statistics-for-evals.md) |
| **XNOR** | A bitwise operation that gives 1 when two bits agree and 0 otherwise | [09.04](09-efficient-deep-learning/04-quantization.md) |
