#!/usr/bin/env python3
"""Parse every shipped Fairplay font and check its core tables.

Run locally with `python tests/validate_fonts.py`; CI runs the same script.
It fails loudly (non-zero exit) if any font is missing, unparseable, or lacks
the tables a usable variable font needs. Fonts are the product, so this is the
gate that keeps a broken binary from being tagged and released.
"""

from __future__ import annotations

import sys
from pathlib import Path

from fontTools.ttLib import TTFont

REPO_ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = REPO_ROOT / "fonts"
REQUIRED_TABLES = ("name", "cmap", "glyf", "head", "fvar")


def validate(path: Path) -> list[str]:
    """Return a list of problems for one font; empty means it passed."""
    problems: list[str] = []
    try:
        font = TTFont(path)
    except Exception as exc:  # noqa: BLE001 - report any parse failure verbatim
        return [f"could not parse: {exc}"]

    for table in REQUIRED_TABLES:
        if table not in font:
            problems.append(f"missing '{table}' table")

    if "name" in font and not font["name"].getDebugName(1):
        problems.append("empty family name (name ID 1)")

    if "fvar" in font and not font["fvar"].axes:
        problems.append("fvar table has no variation axes")

    if "maxp" in font and font["maxp"].numGlyphs < 2:
        problems.append("font has fewer than 2 glyphs")

    font.close()
    return problems


def main() -> int:
    fonts = sorted(FONT_DIR.rglob("*.ttf"))
    if not fonts:
        print(f"FAIL: no .ttf fonts found under {FONT_DIR}")
        return 1

    failed = False
    for path in fonts:
        rel = path.relative_to(REPO_ROOT)
        problems = validate(path)
        if problems:
            failed = True
            print(f"FAIL {rel}")
            for problem in problems:
                print(f"     - {problem}")
        else:
            font = TTFont(path)
            axes = ", ".join(a.axisTag for a in font["fvar"].axes)
            print(f"OK   {rel}  ({font['maxp'].numGlyphs} glyphs, axes: {axes})")
            font.close()

    if failed:
        print("\nFont validation failed.")
        return 1
    print(f"\nAll {len(fonts)} font(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
