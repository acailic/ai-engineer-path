"""A minimal agent in plain Python: a model behind an interface, a tool
registry, a loop with a stop condition, and error handling.
No framework and no network: the model is a deterministic stub."""

import json
from dataclasses import dataclass


# ---------- 1. Tools: a function plus the text the model sees ----------
@dataclass(frozen=True)
class Tool:
    name: str
    description: str        # the model reads this: it is a prompt
    parameters: dict        # JSON Schema describing the arguments
    fn: object              # the Python function to call

    def run(self, arguments: dict) -> str:
        """Call the function. Always returns text; never raises."""
        missing = [k for k in self.parameters.get("required", []) if k not in arguments]
        if missing:
            return "Error: missing required arguments %s." % missing
        try:
            return str(self.fn(**arguments))
        except Exception as exc:                 # tool errors go back to the model
            return "Error: %s: %s" % (type(exc).__name__, exc)


def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float) -> float:
    return a / b


TOOLS = [
    Tool("add", "Add two numbers.",
         {"type": "object", "required": ["a", "b"]}, add),
    Tool("divide", "Divide a by b.",
         {"type": "object", "required": ["a", "b"]}, divide),
]


# ---------- 2. The model: the loop sees only this interface ----------
class Model:
    """Messages in, one decision out. A decision is either
    {"type": "tool_call", "name": ..., "arguments": {...}}
    {"type": "final", "text": ...}
    A real adapter implements step() on top of a chat API."""

    def step(self, messages: list, tools: list) -> dict:
        raise NotImplementedError


class ScriptedModel(Model):
    """Deterministic stand-in for an LLM: replays a fixed list of decisions."""

    def __init__(self, script: list):
        self.script, self.i = script, 0

    def step(self, messages: list, tools: list) -> dict:
        decision = self.script[min(self.i, len(self.script) - 1)]
        self.i += 1
        return decision


# ---------- 3. The agent loop ----------
def run_agent(model: Model, tools: list, task: str,
              max_steps: int = 8, log=print) -> str:
    registry = {tool.name: tool for tool in tools}
    messages = [{"role": "system", "content": "Solve the task with the tools available."},
                {"role": "user", "content": task}]
    for _ in range(max_steps):
        decision = model.step(messages, tools)              # 1. ask for the next decision
        messages.append({"role": "assistant", "content": json.dumps(decision)})
        if decision.get("type") == "final":                 # 2. stop condition: model is done
            return decision["text"]
        if decision.get("type") != "tool_call":             # 3. malformed output: report it
            result = "Error: reply with a tool call or a final answer."
        else:
            tool = registry.get(decision.get("name"))       # 4. look the tool up
            if tool is None:
                result = "Error: unknown tool %r. Known tools: %s" % (
                    decision.get("name"), sorted(registry))
            else:
                result = tool.run(decision.get("arguments", {}))   # 5. errors become text
        log("model -> %s" % json.dumps(decision))
        log("loop  -> %s" % result)
        messages.append({"role": "tool", "content": result})      # 6. show it to the model
    return "Stopped: step limit reached before a final answer."


if __name__ == "__main__":
    script = [
        {"type": "tool_call", "name": "divide", "arguments": {"a": 10, "b": 0}},    # tool error
        {"type": "tool_call", "name": "multiply", "arguments": {"a": 10, "b": 2}},  # unknown
        {"type": "tool_call", "name": "add", "arguments": {"a": 10}},               # bad args
        {"type": "oops"},                                                          # malformed
        {"type": "tool_call", "name": "add", "arguments": {"a": 10, "b": 5}},       # works
        {"type": "final", "text": "10 divided by 0 is undefined; 10 + 5 = 15."},
    ]
    print(run_agent(ScriptedModel(script), TOOLS, "Add 10 and 5."))
    print("---")
    stuck = [{"type": "tool_call", "name": "divide", "arguments": {"a": 10, "b": 0}}]
    print(run_agent(ScriptedModel(stuck), TOOLS, "Divide 10 by 0.", max_steps=3))
