---
name: api-contract-guard
description: Review HTTP, RPC, webhook, event, and internal service contracts for validation, compatibility, failure semantics, and operability.
version: 1.0.0
risk: review-gate
---

# api-contract-guard

## Purpose

Review HTTP, RPC, webhook, event, and internal service contracts for validation, compatibility, failure semantics, and operability.

## Activation

Use for routes, schemas, payloads, status codes, pagination, webhooks, provider clients, retries, and version changes.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Validate external input with explicit schemas, bounds, formats, unknown-field policy, and size limits.**
2. **Keep response shapes, status codes, headers, and error codes stable or version them deliberately.**
3. **Distinguish client, authorization, conflict, throttling, dependency, and internal failures.**
4. **Define idempotency for create/write requests and verify replay behavior.**
5. **Use bounded pagination with stable cursors or documented ordering.**
6. **Set connect/read/write/total timeouts and retry only safe, transient operations.**
7. **Verify webhook signatures, timestamps, replay windows, event IDs, and duplicate delivery handling.**
8. **Avoid leaking stack traces, credentials, internal hosts, provider payloads, or tenant data.**
9. **Update OpenAPI/schema/examples/clients and contract tests with behavior changes.**
10. **Record deprecation, compatibility window, migration path, and removal conditions.**

## Exclusions

Do not treat schema generation as proof that business authorization or semantic validation is correct.

## Receipt format

```json
{
  "skill": "api-contract-guard",
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
- [`references/compatibility.md`](references/compatibility.md)
