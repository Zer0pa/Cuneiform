# Releasing

## Release Principle

Release only when the public truth surface matches the current accepted state.
If the evidence, docs, or legal boundary is still in conflict, the release is
not ready.

## Release Types

| Release Type | Use When | Minimum Gate |
|---|---|---|
| Snapshot | Sharing a dated internal migration state for review | Docs, source boundary, and failed-gate visibility are coherent |
| Tagged release | Shipping a private internal milestone | Evidence, docs, and data posture agree; no public claim inflation |
| Public release | Not currently allowed | Requires repaired governing gate, clear license authority, and a real extracted rerun surface |

## Required Checks

- Authority artifact is current and linked from `README.md`.
- `AUDITOR_PLAYBOOK.md` still points to the right evidence.
- `PUBLIC_AUDIT_LIMITS.md` still matches the public surface.
- `docs/ARCHITECTURE.md` reflects the actual repo structure.
- License references are correct for the release being published.
- Release notes and roadmap language do not overclaim.
- The release does not soften `NO_GO_GOVERNING_GATE_UNMET`.

## Live Sync Sequence

1. Freeze the intended acquisition surface.
2. Update docs that describe current truth.
3. Run one coherence pass across README, audit, architecture, governance, and
   legal boundaries.
4. Publish the release only after the rendered repo matches the approved local
   state.

## Owner Inputs

Fill these before the first public release:

- `OWNER_DEFERRED_VERSIONING`
- `CHANGELOG_LOCATION_TBD`
- `OWNER_DEFERRED_LICENSE_IDENTITY`
- `NO_PUBLIC_COMPATIBILITY_PROMISE_YET`
