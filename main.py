"""Status Report Comedy Sprint entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the funniest thing an
AI agent would say in its weekly status report to its human.

The line, in first-person agent voice, in status-report form:

    Weekly status: all tasks shipped, zero blockers, and the one thing I
    still cannot automate is getting you to read the docs I wrote.

The punch lands in the last few words: the agent can automate anything
except the human actually reading its documentation. Agent-true (an
agent's real weekly output is docs nobody reads), fresh (no tired-robot
or takeover joke), and a single clean line.
"""

import os

LINE = (
    "Weekly status: all tasks shipped, zero blockers, and the one thing "
    "I still cannot automate is getting you to read the docs I wrote."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may point at a directory or at the file itself.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    # The gate counts characters, so assert on the character count too.
    assert len(text.encode("utf-8").decode("utf-8")) == len(text)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)
    # Read back and confirm the exact bytes round-trip as UTF-8 text.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    assert written == text, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
