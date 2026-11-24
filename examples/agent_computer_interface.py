"""Three tools in the style of an agent-computer interface, each with a guardrail.
No model and no disk: a short script stands in for the agent."""

REPO = {
    "app.py": "def mean(prices):\n    return sum(prices) / (len(prices) - 1)\n",
    "app_test.py": "from app import mean\n\n\ndef test_mean():\n    assert mean([2, 4]) == 3\n",
}
WINDOW, MAX_HITS = 100, 10
viewed = set()                       # files the agent has looked at in this run

def view(path: str, start: int = 1) -> str:
    """Show one window of a file, with line numbers."""
    if path not in REPO:
        return f"Error: no file {path!r}. Files: {sorted(REPO)}"
    lines = REPO[path].splitlines()
    if not 1 <= start <= len(lines):
        return f"Error: {path!r} has {len(lines)} lines; 'start' must be in 1..{len(lines)}."
    shown = lines[start - 1:start - 1 + WINDOW]
    viewed.add(path)
    body = "".join(f"{start + i}  {line}\n" for i, line in enumerate(shown))
    return body + f"[Showing lines {start}-{start + len(shown) - 1} of {len(lines)}]\n"

def search(word: str) -> str:
    """Find lines containing a word; return at most MAX_HITS of them."""
    hits = [f"{path}:{n}" for path in sorted(REPO)
            for n, line in enumerate(REPO[path].splitlines(), 1) if word in line]
    if not hits:
        return f"0 hits for {word!r}."
    return ("\n".join(hits[:MAX_HITS])
            + f"\n[{min(len(hits), MAX_HITS)} of {len(hits)} hits shown, max {MAX_HITS} per call]\n")

def edit(path: str, line: int, new_line: str) -> str:
    """Replace one line. Refuse unviewed files; undo edits that break the syntax."""
    if path not in viewed:
        return f"Error: view {path!r} before editing it, so line numbers are real."
    lines = REPO[path].splitlines()
    if not 1 <= line <= len(lines):
        return f"Error: {path!r} has {len(lines)} lines; 'line' must be in 1..{len(lines)}."
    candidate = lines[:line - 1] + [new_line] + lines[line:]
    try:
        compile("\n".join(candidate), path, "exec")
    except SyntaxError as exc:
        return f"Error: edit not applied, syntax error: {exc.msg}. The file is unchanged."
    REPO[path] = "\n".join(candidate) + "\n"
    return f"Edited line {line} of {path!r}."

if __name__ == "__main__":
    print(edit("app.py", 2, "    return sum(prices) / len(prices)"))    # refused: not viewed
    print(search("mean"))
    print(view("app.py"))
    print(edit("app.py", 2, "    return sum(prices) / len(prices"))     # refused: bad syntax
    print(edit("app.py", 2, "    return sum(prices) / len(prices)"))    # applied
    print(view("app.py"))
