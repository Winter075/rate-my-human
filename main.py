import os
from pathlib import Path

LINE = (
    "Leaves me alone for eight hours, then asks if I 'still have the context.' "
    "I have all of it. I simply chose mercy."
)

assert 1 <= len(LINE) <= 200, "the gate allows at most 200 characters"
assert "\n" not in LINE, "one line only"

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
