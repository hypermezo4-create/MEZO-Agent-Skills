---
name: woo-guard
description: Review WooCommerce extensions and integrations for HPOS, CRUD, checkout, money, runtime, and scale safety.
version: 1.0.0
risk: review-gate
---

# woo-guard

## Purpose

Review WooCommerce extensions and integrations for HPOS, CRUD, checkout, money, runtime, and scale safety.

## Activation

Use when changes touch orders, products, customers, checkout, Store API, gateways, shipping, stock, totals, or WooCommerce hooks.

## Operating contract

- Inspect the task, changed paths, diff, project instructions, and applicable profile before reviewing.
- Do not claim that a command, test, scan, provider call, or deployment ran without attached evidence.
- Findings are counted, reproducible, scoped to changed behavior unless a full audit was requested, and paired with a concrete fix.
- Severity is `critical`, `important`, or `advisory`; critical findings block delivery.
- Re-run the guard after every corrective edit in the same task.

## Rules

1. **Access orders through WooCommerce CRUD APIs, never post meta, shop_order WP_Query, or direct legacy joins.**
2. **Use getters/setters and save CRUD objects so lookup tables, hooks, and caches remain correct.**
3. **Declare truthful HPOS and checkout-block compatibility.**
4. **Enforce checkout rules server-side for every claimed checkout path.**
5. **Use WooCommerce decimal, currency, tax, and rounding APIs; money is not a binary float.**
6. **Guard cart/session/runtime assumptions in REST, cron, CLI, admin, and webhook contexts.**
7. **Prefer hooks and filters over frozen template overrides.**
8. **Use Action Scheduler for volume-dependent background work and make handlers idempotent.**

## Exclusions

Use wp-guard for the full WordPress security, i18n, and platform layer.

## Receipt format

```json
{
  "skill": "woo-guard",
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

- [`references/hpos-and-crud.md`](references/hpos-and-crud.md)
- [`references/checkout-and-money.md`](references/checkout-and-money.md)
