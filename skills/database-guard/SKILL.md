---
name: database-guard
description: Review schema, query, transaction, migration, persistence, and PostgreSQL changes for correctness, scale, and rollback safety.
version: 1.0.0
risk: review-gate
---

# database-guard

## Purpose

Review schema, query, transaction, migration, persistence, and PostgreSQL changes for correctness, scale, and rollback safety.

## Activation

Use for models, repositories, SQL, migrations, transaction boundaries, indexes, locks, pools, and data backfills.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Put cross-request invariants in database constraints, not only application checks.**
2. **Match transaction boundaries to business atomicity and avoid network calls inside transactions.**
3. **Use explicit isolation and locking only with a documented anomaly being prevented.**
4. **Index real filter, join, order, and uniqueness patterns; consider selectivity and write cost.**
5. **Detect N+1 queries, unbounded reads, large offsets, and accidental full-table work.**
6. **Migrations must be backward-compatible across rolling deployment, resumable, observable, and rollback-aware.**
7. **Separate schema change, backfill, enforcement, and cleanup when data volume or availability matters.**
8. **Bound pools and timeouts; always release sessions, cursors, advisory locks, and connections.**
9. **Use parameterized SQL and least-privilege database roles.**
10. **Test concurrency and real migrations when persistence behavior is the subject.**

## Exclusions

Do not approve destructive migrations solely because they run on an empty test database.

## Receipt format

```json
{
  "skill": "database-guard",
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
- [`references/migrations.md`](references/migrations.md)
