---
name: docs-guard
description: Verify that technical documentation, examples, configuration, changelogs, and docstrings make only source-backed claims.
version: 1.0.0
risk: review-gate
---

# docs-guard

## Purpose

Verify that technical documentation, examples, configuration, changelogs, and docstrings make only source-backed claims.

## Activation

Use after docs or documented behavior changes and for documentation review requests.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Every referenced symbol, command, flag, endpoint, environment key, path, and version must exist.**
2. **Every code sample must resolve imports, match signatures, avoid real credentials, and work from a clean state.**
3. **Document actual implemented behavior; flag disagreements between code and specs.**
4. **Remove performance, compatibility, scale, and production-readiness claims without repository evidence.**
5. **Update every documentation surface affected by renamed or changed behavior.**
6. **Remove filler, signature-paraphrasing docstrings, superlatives, TODO stubs, and copied upstream prose.**
7. **Examples must include real failure behavior and recovery where relevant.**
8. **Validate internal links, anchors, prerequisites, and version ranges.**

## Exclusions

Do not use for marketing copy, visual documentation theming, or production-code quality review.

## Receipt format

```json
{
  "skill": "docs-guard",
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

- [`references/verification.md`](references/verification.md)
- [`references/code-samples.md`](references/code-samples.md)
