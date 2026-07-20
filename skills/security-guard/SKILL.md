---
name: security-guard
description: Perform a threat-driven security review of changed application, infrastructure, workflow, and integration code.
version: 1.0.0
risk: review-gate
---

# security-guard

## Purpose

Perform a threat-driven security review of changed application, infrastructure, workflow, and integration code.

## Activation

Use after every non-trivial production change and before merge for authentication, authorization, external input, files, network, secrets, commands, dependencies, or privileged operations.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Map trust boundaries, assets, actors, privileges, entry points, and data flows before judging controls.**
2. **Enforce authorization at the resource and action level; authentication alone is never sufficient.**
3. **Use parameterized queries and structured APIs; reject command, SQL, template, path, and header injection paths.**
4. **Constrain outbound requests against SSRF, redirects, private networks, metadata endpoints, and DNS rebinding.**
5. **Normalize and confine file paths; validate content, size, ownership, and archive extraction.**
6. **Never log, commit, return, or send secrets to model providers; rotate exposed material.**
7. **Avoid unsafe deserialization, dynamic evaluation, and untrusted plugin execution.**
8. **Pin dependencies, minimize permissions, verify artifacts, and review workflow token scopes.**
9. **Use secure failure behavior without leaking internals; preserve audit evidence.**
10. **Every critical finding must include an exploit path or violated security invariant and a concrete mitigation.**

## Exclusions

Do not replace dedicated SAST, dependency, secret, container, and infrastructure scanners; correlate their evidence.

## Receipt format

```json
{
  "skill": "security-guard",
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
- [`references/trust-boundaries.md`](references/trust-boundaries.md)
