# Contributing

1. Create a task branch.
2. Add or edit one focused skill at a time.
3. Put the activation scope and exclusions in frontmatter.
4. Add a positive fixture and an adversarial fixture under `evals/` for new behavior.
5. Run all validation commands from the README.
6. Regenerate `skills-manifest.json`.
7. Describe the risk, evidence, compatibility impact, and rollback in the pull request.

A new blocking rule needs a reproducible failure pattern. A stylistic preference without correctness, security, performance, operability, or maintenance impact does not belong in a guard.
