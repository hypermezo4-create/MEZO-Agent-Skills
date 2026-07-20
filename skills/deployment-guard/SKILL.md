---
name: deployment-guard
description: Review Docker, Fly.io, CI/CD, runtime configuration, health, shutdown, migrations, rollout, and rollback changes.
version: 1.0.0
risk: review-gate
---

# deployment-guard

## Purpose

Review Docker, Fly.io, CI/CD, runtime configuration, health, shutdown, migrations, rollout, and rollback changes.

## Activation

Use for Dockerfiles, compose, fly.toml, workflows, deploy scripts, runtime resources, health checks, secrets, and production migrations.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Build reproducibly with pinned bases, locked dependencies, minimal context, and no secrets in layers.**
2. **Run as a non-root user with a minimal runtime image and explicit entrypoint.**
3. **Separate liveness from readiness and make checks reflect real dependency behavior without causing outages.**
4. **Handle SIGTERM, stop intake, finish or return work safely, close connections, and respect platform timeout.**
5. **Define CPU, memory, concurrency, pool, timeout, disk, and scaling assumptions.**
6. **Run migrations in a controlled phase with rolling-deploy compatibility and failure recovery.**
7. **Use immutable artifacts, provenance, checksums, and environment promotion rather than rebuilding per environment.**
8. **Minimize workflow permissions, pin actions, protect environments, and prevent untrusted code from accessing secrets.**
9. **Use preview, smoke, canary, health, and rollback checks before full production rollout.**
10. **Document the rollback trigger and verify rollback does not depend on incompatible schema or state.**

## Exclusions

Do not treat a successful image build as proof that the application is production-ready.

## Receipt format

```json
{
  "skill": "deployment-guard",
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
- [`references/fly.md`](references/fly.md)
