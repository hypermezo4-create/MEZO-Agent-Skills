from __future__ import annotations

import sys
from pathlib import Path as _BootstrapPath
sys.path.insert(0, str(_BootstrapPath(__file__).resolve().parents[1]))

import argparse
import hashlib
import json
from pathlib import Path

from validation.common import ROOT, SKILLS, parse_frontmatter

OUTPUT = ROOT / "skills-manifest.json"


def build_manifest() -> dict[str, object]:
    skills: list[dict[str, object]] = []
    for directory in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        parsed = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        files = sorted(path for path in directory.rglob("*") if path.is_file())
        digest = hashlib.sha256()
        for file in files:
            digest.update(file.relative_to(ROOT).as_posix().encode())
            digest.update(b"\0")
            digest.update(file.read_bytes())
            digest.update(b"\0")
        skills.append({
            "name": parsed.values["name"],
            "version": parsed.values["version"],
            "description": parsed.values["description"],
            "sha256": digest.hexdigest(),
            "files": [file.relative_to(ROOT).as_posix() for file in files],
        })
    return {"schema_version": 1, "skills": skills}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build_manifest(), indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print("skills-manifest.json is stale; run scripts/generate_manifest.py")
            return 1
        print("skills-manifest.json is current")
        return 0
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
