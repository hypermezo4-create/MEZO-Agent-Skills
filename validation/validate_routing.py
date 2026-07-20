from __future__ import annotations

import re

from validation.common import ROOT, SKILLS


def validate_routing() -> list[str]:
    errors: list[str] = []
    known = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    for file in [ROOT / "skill-routing.yaml", *sorted((ROOT / "project_profiles").glob("*.yaml"))]:
        text = file.read_text(encoding="utf-8")
        referenced = set(re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)*-guard\b", text))
        for skill in sorted(referenced - known):
            errors.append(f"{file.relative_to(ROOT)}: unknown skill {skill}")
    required = {"clean-code-guard", "security-guard", "test-guard", "deployment-guard"}
    routing_text = (ROOT / "skill-routing.yaml").read_text(encoding="utf-8")
    for skill in sorted(required):
        if skill not in routing_text:
            errors.append(f"skill-routing.yaml: required skill is not routed: {skill}")
    return errors
