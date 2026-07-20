from __future__ import annotations

import sys
from pathlib import Path as _BootstrapPath
sys.path.insert(0, str(_BootstrapPath(__file__).resolve().parents[1]))

from validation.detect_prompt_injection import detect_prompt_injection
from validation.validate_links import validate_links
from validation.validate_routing import validate_routing
from validation.validate_structure import validate_structure


def main() -> int:
    checks = {
        "structure": validate_structure(),
        "links": validate_links(),
        "prompt-injection": detect_prompt_injection(),
        "routing": validate_routing(),
    }
    total = 0
    for name, errors in checks.items():
        if errors:
            print(f"[FAIL] {name}: {len(errors)}")
            for error in errors:
                print(f"  - {error}")
            total += len(errors)
        else:
            print(f"[PASS] {name}")
    if total:
        print(f"Validation failed with {total} error(s).")
        return 1
    print(f"Validation passed for {sum(1 for _ in __import__('pathlib').Path('skills').iterdir())} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
