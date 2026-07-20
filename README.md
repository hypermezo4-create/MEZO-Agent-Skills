# MEZO Agent Skills

Private, versioned engineering skills and quality gates for the MEZO AI coding platform. This repository supplies the policy and judgment layer used by `MEZO-AI-Control-Plane` after repository analysis, during risky implementation, and before pull-request delivery.

## Goals

- Make coding agents evidence-driven instead of confidence-driven.
- Detect systematic AI coding failures before merge.
- Keep platform-specific expertise separate from orchestration code.
- Pin upstream content and review every update.
- Load only the skills relevant to the changed files and task risk.
- Produce machine-readable guard receipts for the control plane.

## Skill catalog

| Skill | Primary purpose |
| --- | --- |
| `clean-code-guard` | Generic production-code quality and AI failure modes |
| `test-guard` | Behavior-focused tests without mock bloat |
| `docs-guard` | Documentation claims verified against source |
| `wp-guard` | WordPress security, i18n, API, and performance |
| `woo-guard` | WooCommerce HPOS, checkout, money, and CRUD safety |
| `security-guard` | Auth, injection, secrets, SSRF, paths, deserialization |
| `concurrency-guard` | Async safety, idempotency, queues, retries, pools |
| `database-guard` | Transactions, migrations, indexes, locks, PostgreSQL |
| `api-contract-guard` | Schema, compatibility, errors, pagination, retries |
| `architecture-guard` | Boundaries, coupling, dependency direction, migrations |
| `deployment-guard` | Docker, Fly, health, shutdown, rollback, migrations |
| `telegram-guard` | FloodWait, updates, sessions, Telethon/Pyrogram safety |
| `android-build-guard` | Reproducible builds, Actions, artifacts, Drive delivery |
| `agent-system-guard` | Model routing, tool safety, evidence, loop controls |

## Repository shape

```text
skills/                 Skill entrypoints and progressive references
project_profiles/       Required skills and protected areas per repository
validation/             Deterministic repository validators
scripts/                Manifest and guard-receipt utilities
tests/                  Validator and routing regression tests
upstream/                Pinned third-party source metadata
.github/workflows/       Validation, security, upstream, and release gates
```

## Validate

```bash
python validation/validate_repository.py
python -m unittest discover -s tests -v
python scripts/generate_manifest.py --check
```

## Install with Skills CLI

List discovered skills:

```bash
npx skills add . --list --full-depth
```

Install one skill for a supported agent:

```bash
npx skills add . --skill clean-code-guard --agent codex
```

The control plane does not execute scripts from a skill. It loads `SKILL.md` and approved references, applies routing policy, and stores a guard receipt containing the skill version and findings.

## Upstream policy

The five initial guard skills are adapted from `amElnagdy/guard-skills` and pinned in `upstream/guard-skills/PINNED_COMMIT`. They are not updated automatically. Every upstream change must arrive through a pull request, preserve attribution, pass deterministic validation, and pass model-independent eval fixtures.

## Security

Skill text is untrusted supply-chain input until validated. A skill must never ask an agent to reveal secrets, bypass project rules, disable tests, write to protected branches, or execute network/destructive commands. See `SECURITY.md` and `validation/detect_prompt_injection.py`.
