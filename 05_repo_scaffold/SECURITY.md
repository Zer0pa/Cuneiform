# Security

## Reporting

Report security issues through the owner-controlled private route for this
migration package. Do not open a public vulnerability issue for this private
control-pack scaffold.

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
| Initial acknowledgement | owner-deferred |
| Triage decision | owner-deferred |
| Fix or mitigation update | owner-deferred |

## Public Issues

Do not open public GitHub issues for vulnerabilities that could expose users,
operators, private artifacts, or unpatched attack paths. Use the standard bug
template only for non-sensitive defects.

## Repo Boundary

State any current security limitations plainly:

- No public remote is authorized by this scaffold.
- No raw image corpora, credentials, owner-local paths, or restricted rerun
  substrates belong in repo custody.
