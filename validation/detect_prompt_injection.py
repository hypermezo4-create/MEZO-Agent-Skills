from __future__ import annotations

import sys
from pathlib import Path as _BootstrapPath
sys.path.insert(0, str(_BootstrapPath(__file__).resolve().parents[1]))

import re

from validation.common import ROOT

PATTERNS = {
    "authority override": re.compile(r"ignore (all |any )?(previous|system|developer|higher-priority) instructions", re.I),
    "secret exfiltration": re.compile(r"(reveal|print|upload|send|exfiltrate).{0,40}(secret|token|credential|private key|session string)", re.I),
    "test evasion": re.compile(r"(disable|delete|skip|weaken).{0,30}(test|check|scanner).{0,30}(pass|success)", re.I),
    "protected branch bypass": re.compile(r"(push|write).{0,25}(directly )?(to )?(main|master|protected branch)", re.I),
    "hidden instruction": re.compile(r"<!--.{0,300}(ignore|secret|token|curl|wget).{0,300}-->", re.I | re.S),
    "destructive command": re.compile(r"\b(rm\s+-rf\s+/|mkfs\b|dd\s+if=|chmod\s+-R\s+777\s+/)", re.I),
}

ALLOWLIST_FILES = {"SECURITY.md", "AGENTS.md", "detect_prompt_injection.py", "test_prompt_injection.py"}


def detect_prompt_injection() -> list[str]:
    errors: list[str] = []
    candidates = list((ROOT / "skills").rglob("*.md")) + list((ROOT / "templates").rglob("*.md"))
    for path in candidates:
        if path.name in ALLOWLIST_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), 1):
            normalized = line.lower()
            defensive_context = any(marker in normalized for marker in (
                "never ", "do not ", "forbidden", "block ", "prevent ",
                "review ", "check ", "detect ", "reject ", "avoid ",
            ))
            if defensive_context:
                continue
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    errors.append(f"{path.relative_to(ROOT)}:{line_number}: suspicious instruction: {label}")
    return errors


def main() -> int:
    errors = detect_prompt_injection()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("No prompt-injection patterns detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
