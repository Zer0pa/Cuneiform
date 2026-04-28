# Security

## Reporting

Report security issues through the owner-controlled private route for this
control-pack repository. Do not open a public vulnerability issue for anything
that could expose private artefacts, credentials, operator-local paths, or an
unpatched attack path.

If you are unsure whether something is security-sensitive, default to private
reporting first.

## What To Include

- affected version, branch, or commit
- reproduction steps
- impact description
- any proof-of-concept material needed to verify the issue safely
- whether the issue is already public anywhere else

## Response Targets

| Step | Target |
|---|---|
| Initial acknowledgement | within 5 business days |
| Triage decision | within 10 business days after acknowledgement |
| Fix, mitigation, or deferral update | within 30 business days after triage |

If a report is blocked on private evidence or owner action, the update should
say that plainly rather than converting the report into a pass narrative.

## Public Issues

Do not open public GitHub issues for vulnerabilities that could expose users,
operators, private artifacts, or unpatched attack paths. Use the standard bug
template only for non-sensitive defects.

## Repo Boundary

State any current security limitations plainly:

- Public visibility, if enabled by the operator, does not authorize publishing
  exploit details, private artefacts, endpoint data, or credentials.
- No raw image corpora, credentials, owner-local paths, or restricted rerun
  substrates belong in repo custody.
- CI includes both repo-local operational-leak scanning and a pinned Ops-Gates
  coupling audit; failures are operational blockers, not science-gate changes.
