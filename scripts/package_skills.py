#!/usr/bin/env python3
"""Zip each free skill for upload to the Claude apps or copying into Claude Code.

Each zip holds one folder named after the skill, with SKILL.md and any resource files.
The evals/ folder is left out: it's for testing the skill, not for running it.

Usage: python3 scripts/package_skills.py [out_dir]   (default: dist/)
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_PARTS = {"evals", "__pycache__"}


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    out.mkdir(parents=True, exist_ok=True)
    made = []
    for skill in sorted(p for p in (ROOT / "products").iterdir() if p.is_dir() and not p.name.startswith("_")):
        if not (skill / "SKILL.md").exists():
            continue
        dest = out / f"{skill.name}.zip"
        with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                rel = f.relative_to(skill)
                if f.is_file() and not SKIP_PARTS.intersection(rel.parts):
                    z.write(f, Path(skill.name) / rel)
        made.append(dest)
        print(dest.relative_to(out.parent) if out.parent in dest.parents else dest)
    if not made:
        print("no skills found", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
