"""Write the one-line rubber-band review to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The line is fixed at build time; the program just emits it
byte-identically so the grader's two runs agree.
"""

import os

LINE = "Five stars: the rubber band held my papers together for five years, then snapped on a Tuesday for no reason and was replaced by an identical rubber band."

if not LINE.strip():
    raise ValueError("entry line must not be empty or only whitespace")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
try:
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
except OSError as exc:
    raise SystemExit(f"failed to write entry.txt: {exc}") from exc
