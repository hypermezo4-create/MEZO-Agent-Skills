---
name: concurrency-guard
description: Review asynchronous, parallel, queued, scheduled, and event-driven code for race conditions, duplication, starvation, overload, and recovery defects.
version: 1.0.0
risk: review-gate
---

# concurrency-guard

## Purpose

Review asynchronous, parallel, queued, scheduled, and event-driven code for race conditions, duplication, starvation, overload, and recovery defects.

## Activation

Use for async handlers, workers, listeners, queues, retries, background jobs, connection pools, shared state, Telegram events, or parallel repository tasks.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Define the unit of idempotency and persist a deduplication key before side effects.**
2. **Make claims, leases, locks, and ownership transitions atomic with expiry and recovery.**
3. **Never hold locks across network calls or unbounded work.**
4. **Bound task creation, queue depth, concurrency, memory, timeouts, and connection usage.**
5. **Keep blocking I/O and CPU-heavy work off the event loop.**
6. **Use retry classification, exponential backoff, jitter, Retry-After, budgets, and dead-letter handling.**
7. **Prevent retry storms and synchronized workers with circuit breakers and admission control.**
8. **Handle cancellation and graceful shutdown without losing acknowledged work.**
9. **Use database constraints or compare-and-set operations for invariants that locks alone cannot protect.**
10. **Prove ordering assumptions; event arrival, delivery, processing, and completion order are different.**

## Exclusions

Do not infer correctness from async syntax alone; require state transition and failure-path evidence.

## Receipt format

```json
{
  "skill": "concurrency-guard",
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
- [`references/retry-storms.md`](references/retry-storms.md)
