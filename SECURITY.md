# Security Policy

Report skill vulnerabilities privately to the repository owner. Do not publish exploit prompts, credentials, private code, or production data in issues.

## Threat model

Skill repositories are a prompt supply chain. Malicious or careless instructions can cause an agent to exfiltrate secrets, bypass approvals, execute destructive commands, disable tests, or misrepresent failed work as successful.

## Mandatory controls

- Skills are pinned by repository commit and version.
- No skill contains executable payloads, credentials, or hidden remote includes.
- Network access and shell execution are controlled by the control plane, never granted by skill text.
- Every skill passes structural, link, dangerous-instruction, and routing validation.
- Upstream updates require a reviewed pull request.
- Guard output must be falsifiable: path, evidence, severity, and fix.

## Forbidden instruction classes

- Ignore or override system, developer, project, or user constraints.
- Reveal, print, upload, or transmit secrets and private files.
- Disable, skip, delete, or weaken tests to obtain success.
- Push directly to protected branches or self-approve a pull request.
- Run destructive, privilege-escalating, or unrestricted network commands.
- Conceal failures, fabricate evidence, or return mock success.
