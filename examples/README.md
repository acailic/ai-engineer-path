# Examples

The complete listings from the chapters, saved as runnable files. Each one needs Python 3.10 or newer and nothing else: no packages, no API key, no network. They are identical to the listings in the chapters that explain them.

| File | Lines | From the chapter | What it is |
|---|---|---|---|
| [`minimal_agent.py`](minimal_agent.py) | 105 | [the anatomy of an agent](../02-building-agents/01-the-anatomy-of-an-agent.md) | A minimal agent loop with no framework and no network: a model behind an interface, a tool registry, a loop with a stop condition, and error handling. The model is a deterministic stub, so it runs without an API key. |
| [`agent_computer_interface.py`](agent_computer_interface.py) | 54 | [coding agents](../02-building-agents/07-coding-agents.md) | Three tools in the agent-computer-interface style (view, search, edit), each with one guardrail. The repository is a dictionary, so the file runs without a model or a disk. |
| [`eval_harness.py`](eval_harness.py) | 222 | [a minimal eval harness](../03-evaluation/02-a-minimal-eval-harness.md) | A minimal evaluation harness: dataset, task runner, grader, metrics (exact match, pass@k, pass^k) and a report. Ships with two deterministic stub models, so it runs without an API key. |
| [`eval_stats.py`](eval_stats.py) | 33 | [statistics for evals](../03-evaluation/05-statistics-for-evals.md) | Standard errors and a paired comparison, computed by hand and checked in code. |

Run any of them from this folder:

```bash
python3 minimal_agent.py
python3 agent_computer_interface.py
python3 eval_harness.py
python3 eval_stats.py
```

Some chapters show further short snippets that import one of these files (for example a CI gate that imports `eval_harness`). Save such a snippet in this folder under the name the chapter gives it.
