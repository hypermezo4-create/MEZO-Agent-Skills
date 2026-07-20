---
name: clean-code-guard
description: Review generated or changed production code for correctness, maintainability, and systematic LLM failure modes before presentation, commit, or merge.
version: 1.0.0
risk: review-gate
---

# clean-code-guard

## Purpose

Review generated or changed production code for correctness, maintainability, and systematic LLM failure modes before presentation, commit, or merge.

## Activation

Use after non-trivial production-code edits, refactors, bug fixes, or code-review requests. Read the target file, one neighbor, project rules, and the diff first.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Preserve observable behavior during refactors; separate bug fixes from cleanup.**
2. **Use intent-revealing names and keep functions focused; avoid generic helper/manager/process names.**
3. **Catch only errors that can be recovered from; never swallow broad exceptions or return fake success.**
4. **Validate at trust boundaries but do not add defensive noise inside typed, trusted contracts.**
5. **Verify every import, package, hook, method, and signature against the installed version.**
6. **Do not add abstractions, flags, factories, dependencies, or extension points without a current caller.**
7. **Never ship hardcoded fixtures, mock fallbacks, dead code, disabled tests, or half-implementations.**
8. **Re-derive boundary and range logic from the specification; enumerate empty/one/many and edge cases.**
9. **Match established repository patterns for logging, errors, HTTP, database, style, and module boundaries.**
10. **Every finding must include path, evidence, severity, risk, and a concrete fix; never invent a score.**

## Exclusions

Do not use for test-only code, documentation-only work, CI execution, or pure architecture discussion; route those to their dedicated skills.

## Receipt format

```json
{
  "skill": "clean-code-guard",
  "version": "1.0.0",
  "commit": "<skills repository commit>",
  "scope": ["<changed path>"],
  "findings": [
    {
      "severity": "critical|important|advisory",
      "path": "path/to/file",
      "evidence": "quoted behavior or tool evidence",
      "risk": "specific consequence",
      "fix": "concrete correction"
    }
  ],
  "result": "pass|changes-required"
}
```

Never output an invented quality percentage. A pass means the defined checks were walked and no blocking evidence was found; it is not a guarantee that the software is defect-free.

## References

- [`references/review-checklist.md`](references/review-checklist.md)
- [`references/ai-failure-modes.md`](references/ai-failure-modes.md)
