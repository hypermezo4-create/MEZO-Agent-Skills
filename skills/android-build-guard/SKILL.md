---
name: android-build-guard
description: Review Android ROM, device, kernel, build automation, artifact, release, and Google Drive delivery changes for reproducibility and integrity.
version: 1.0.0
risk: review-gate
---

# android-build-guard

## Purpose

Review Android ROM, device, kernel, build automation, artifact, release, and Google Drive delivery changes for reproducibility and integrity.

## Activation

Use for Android/Xiaomi build repositories, GitHub Actions, manifests, device configs, build scripts, artifacts, upload scripts, and release pipelines.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Pin source revisions, manifests, toolchains, container images, actions, and build dependencies.**
2. **Validate device, variant, target, partition, firmware, and signing inputs before expensive work.**
3. **Fail on missing or unexpected artifacts; never upload the nearest filename or stale workspace output.**
4. **Record artifact name, size, hash, build ID, source commit, target, and timestamp in a manifest.**
5. **Validate archive/file type and inspect expected internal metadata before delivery.**
6. **Use least-privilege credentials and keep Drive/service-account secrets out of logs and artifacts.**
7. **Make upload idempotent and verify remote object identity, size, and checksum after transfer.**
8. **Keep official-source fixes separate from DeadZone-specific features and delivery differences.**
9. **Use caches only with versioned keys and never let cache hits bypass correctness checks.**
10. **Preserve full logs and failure evidence while redacting secrets; do not declare success from process exit alone.**

## Exclusions

Do not recommend redistributing proprietary firmware, signing keys, or artifacts without authorization.

## Receipt format

```json
{
  "skill": "android-build-guard",
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
- [`references/google-drive-delivery.md`](references/google-drive-delivery.md)
