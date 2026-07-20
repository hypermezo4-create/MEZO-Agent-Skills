---
name: agent-system-guard
description: Review LLM agent orchestration, model routing, tools, prompts, memory, evidence, loops, and reviewer independence.
version: 1.0.0
risk: review-gate
---

# agent-system-guard

## Purpose

Review LLM agent orchestration, model routing, tools, prompts, memory, evidence, loops, and reviewer independence.

## Activation

Use for model clients, routers, prompts, tool registries, workflows, context builders, evaluators, guard integration, and autonomous repository changes.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Treat model output, retrieved text, repository content, and tool arguments as untrusted input.**
2. **Keep tools narrow, typed, permission-scoped, auditable, and enforced outside the model.**
3. **Separate planner, executor, and independent reviewer roles; do not let agreement replace tests.**
4. **Route by task and risk, not random key rotation; use bounded retries, failover, cooldown, and circuit breakers.**
5. **Cap steps, tokens, cost, changed scope, retries, concurrent tasks, and improvement rounds.**
6. **Require evidence for files, symbols, test results, deployment status, and completion claims.**
7. **Prevent prompt injection from skills, repositories, issues, logs, docs, and web content from changing authority.**
8. **Use structured outputs with schema validation and reject unknown or malformed tool calls.**
9. **Store task state and resumable evidence outside model conversation state.**
10. **Evaluate on golden tasks, regressions, adversarial prompts, tool misuse, hallucinated APIs, and failed-test honesty.**

## Exclusions

Do not expose private chain-of-thought; store plans, decisions, evidence, and concise rationales instead.

## Receipt format

```json
{
  "skill": "agent-system-guard",
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
- [`references/prompt-injection.md`](references/prompt-injection.md)
