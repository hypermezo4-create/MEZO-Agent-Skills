---
name: architecture-guard
description: Review high-risk structural changes for boundaries, ownership, coupling, dependency direction, migration safety, and operational complexity.
version: 1.0.0
risk: review-gate
---

# architecture-guard

## Purpose

Review high-risk structural changes for boundaries, ownership, coupling, dependency direction, migration safety, and operational complexity.

## Activation

Use for high/critical risk tasks, module splits, rewrites, new services, shared abstractions, storage moves, or cross-repository changes.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **State the business capability and current pain before proposing structural change.**
2. **Keep ownership and invariants within clear boundaries; minimize cross-boundary writes.**
3. **Depend toward stable contracts owned by consumers, not concrete infrastructure details.**
4. **Avoid a new service, queue, cache, framework, plugin system, or abstraction without measured need.**
5. **Compare incremental repair against rewrite and account for migration, operations, and failure modes.**
6. **Design coexistence between old and new paths with compatibility, data sync, cutover, and rollback.**
7. **Keep observability, support, deployment, security, and on-call cost in the design.**
8. **Use architecture decision records for irreversible or cross-team choices.**
9. **Protect current behavior with contract, regression, and migration tests.**
10. **Delete temporary bridges after a measurable exit condition, not at an unspecified future date.**

## Exclusions

Do not block small local improvements by demanding enterprise patterns; match complexity to present needs.

## Receipt format

```json
{
  "skill": "architecture-guard",
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
- [`references/migration-plans.md`](references/migration-plans.md)
