from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


@dataclass(frozen=True)
class Frontmatter:
    values: dict[str, str]
    body: str


def parse_frontmatter(text: str) -> Frontmatter:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML-style frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter is not terminated")
    raw = text[4:end]
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return Frontmatter(values=values, body=text[end + 5 :])


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
