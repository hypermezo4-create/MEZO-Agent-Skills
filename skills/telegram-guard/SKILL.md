---
name: telegram-guard
description: Review Telegram bot and account-client code for update handling, FloodWait, sessions, concurrency, privacy, and reliable delivery.
version: 1.0.0
risk: review-gate
---

# telegram-guard

## Purpose

Review Telegram bot and account-client code for update handling, FloodWait, sessions, concurrency, privacy, and reliable delivery.

## Activation

Use for Bot API, Telethon, Pyrogram, session listeners, code capture, handlers, callbacks, storage groups, retries, and account management.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Deduplicate updates and messages with stable IDs before side effects; Telegram can redeliver or reconnect.**
2. **Keep handlers fast; enqueue expensive work and acknowledge callbacks promptly.**
3. **Respect FloodWait/Retry-After exactly, centralize rate limits, and prevent concurrent retry storms.**
4. **Bound per-account and global concurrency; isolate noisy users and accounts.**
5. **Protect session files, string sessions, phone numbers, login codes, hashes, and API credentials as secrets.**
6. **Never log login codes, session material, message bodies, or private identifiers without explicit redaction policy.**
7. **Persist listener checkpoints and delivery state so restarts do not lose or duplicate work.**
8. **Make code capture event-driven where possible; avoid aggressive polling and broad scans that create lag.**
9. **Separate capture time, processing time, queue delay, send time, and provider delay in metrics.**
10. **Handle revoked sessions, authorization changes, disconnected clients, migrations, and graceful shutdown explicitly.**

## Exclusions

Do not advise bypassing Telegram limits, account protections, consent, or platform terms.

## Receipt format

```json
{
  "skill": "telegram-guard",
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
- [`references/latency.md`](references/latency.md)
