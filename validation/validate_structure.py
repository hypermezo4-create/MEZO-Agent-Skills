from __future__ import annotations

from pathlib import Path
import re

from validation.common import SKILLS, parse_frontmatter

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def validate_structure() -> list[str]:
    errors: list[str] = []
    if not SKILLS.exists():
        return ["skills directory is missing"]
    for directory in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        version_file = directory / "VERSION"
        agent_file = directory / "agents" / "openai.yaml"
        for required in (skill_file, version_file, agent_file):
            if not required.is_file():
                errors.append(f"{required.relative_to(SKILLS.parent)} is missing")
        if not skill_file.is_file():
            continue
        try:
            parsed = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{skill_file.relative_to(SKILLS.parent)}: {exc}")
            continue
        for key in ("name", "description", "version", "risk"):
            if not parsed.values.get(key):
                errors.append(f"{skill_file.relative_to(SKILLS.parent)}: missing {key}")
        name = parsed.values.get("name", "")
        if name != directory.name or not NAME.fullmatch(name):
            errors.append(f"{directory.name}: frontmatter name mismatch or invalid")
        version = parsed.values.get("version", "")
        file_version = version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else ""
        if version != file_version or not SEMVER.fullmatch(version):
            errors.append(f"{directory.name}: invalid or mismatched semantic version")
        if len(parsed.values.get("description", "")) < 40:
            errors.append(f"{directory.name}: description is too short")
        if "## Receipt format" not in parsed.body:
            errors.append(f"{directory.name}: missing receipt contract")
    return errors
