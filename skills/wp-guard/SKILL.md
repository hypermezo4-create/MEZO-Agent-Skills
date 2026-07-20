---
name: wp-guard
description: Review WordPress plugins, themes, blocks, REST, AJAX, shortcode, query, and WP-CLI changes for shipping safety.
version: 1.0.0
risk: review-gate
---

# wp-guard

## Purpose

Review WordPress plugins, themes, blocks, REST, AJAX, shortcode, query, and WP-CLI changes for shipping safety.

## Activation

Use when changed code touches WordPress hooks, request data, output, REST/AJAX, WP_Query, wpdb, assets, cron, or public names.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Escape output late with context-correct functions and sanitize request data early after unslashing.**
2. **Every state change requires both capability authorization and intent verification such as a nonce.**
3. **Prepare every variable SQL query and prefer core query/data APIs.**
4. **Use WordPress HTTP, enqueue, redirect, filesystem, scheduling, options, and transient APIs instead of custom plumbing.**
5. **Verify every hook and function in supported versions and register it at the correct lifecycle point.**
6. **Prefix or namespace public functions, classes, options, meta keys, handles, actions, and REST namespaces.**
7. **Make every user-facing string translation-ready with a literal text domain.**
8. **Avoid unbounded queries, query-in-loop patterns, unconditional assets, and uncached expensive work.**

## Exclusions

Use woo-guard alongside for WooCommerce-specific order, product, money, checkout, or HPOS logic.

## Receipt format

```json
{
  "skill": "wp-guard",
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

- [`references/security.md`](references/security.md)
- [`references/performance.md`](references/performance.md)
