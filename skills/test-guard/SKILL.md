---
name: test-guard
description: Review generated or changed tests so they protect behavior without mock abuse, duplication, implementation-detail coupling, or meaningless coverage.
version: 1.0.0
risk: review-gate
---

# test-guard

## Purpose

Review generated or changed tests so they protect behavior without mock abuse, duplication, implementation-detail coupling, or meaningless coverage.

## Activation

Use whenever test files or test helpers change, and after an agent writes regression, unit, integration, contract, or agent-flow tests.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Test caller-visible behavior and state transitions, not internal call counts or helper invocation details.**
2. **Mock only system boundaries such as networks, model APIs, external files, clocks, randomness, and third-party SDKs.**
3. **Use real DTOs, entities, and state objects; construction pain is design feedback.**
4. **Merge value-only variants into data-driven tests; keep genuinely different scenarios separate.**
5. **Every test must name the specific bug or contract it protects.**
6. **Preserve production regression tests and reference the incident or issue.**
7. **Do not test framework defaults, constants, constructors, or logging wording.**
8. **Use real migrated infrastructure when persistence behavior itself is under test.**
9. **For agents, test state-in to state-out and structured contracts, not exact prompt wording or number of model calls.**

## Exclusions

Do not review production implementation quality or execute the test suite; use clean-code-guard and project tooling.

## Receipt format

```json
{
  "skill": "test-guard",
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
- [`references/llm-app-testing.md`](references/llm-app-testing.md)
