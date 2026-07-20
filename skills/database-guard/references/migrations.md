# Migrations

Prefer expand/migrate/contract. Avoid table rewrites and long locks. Make backfills chunked, resumable, idempotent, rate-limited, and separately deployable.
