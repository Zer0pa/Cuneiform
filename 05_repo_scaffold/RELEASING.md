# Releasing

## Release Principle

Release only when the public truth surface matches the current accepted state.
If the evidence, docs, or legal boundary is still in conflict, the release is
not ready.

## Release Types

| Release Type | Use When | Minimum Gate |
|---|---|---|
| Snapshot | Sharing a dated internal migration state for review | Docs, source boundary, and failed-gate visibility are coherent |
| Internal tag (e.g. `v0.1.0-internal`) | Shipping a private internal milestone (Phase 03 close) | Evidence, docs, and data posture agree; smoke `PASS` recorded; HF custody pinned; tag is **annotated and local** — not pushed |
| Tagged remote release | Shipping a milestone tag to GitHub | Owner clears licence posture (currently `OWNER_DEFERRED`) AND the failed gate is unchanged → still `INTERNAL`-org visibility only |
| Public release | Not currently allowed | Requires repaired governing gate, clear licence authority, AND a real extracted rerun surface that goes beyond manifest validation |

## Required Checks (every tag, internal or otherwise)

- Authority artefact is current and linked from `README.md`.
- `AUDITOR_PLAYBOOK.md` still points to the right evidence.
- `PUBLIC_AUDIT_LIMITS.md` still matches the public surface.
- `docs/ARCHITECTURE.md` reflects the actual repo structure.
- `docs/evidence/ARTEFACT_CHECKSUMS.md` pins are unchanged.
- The smoke report (`artefacts/smoke/manifest_validation_report.json`) verdict
  is `PASS` and the schema/manifest SHA-256s match the pins.
- HF dataset visibility is `private` and the recorded revision matches
  `state.json`.
- Licence references are correct for the release being published.
- Release notes and roadmap language do not overclaim.
- The release does not soften `NO_GO_GOVERNING_GATE_UNMET`.

## Live Sync Sequence

1. Freeze the intended acquisition surface.
2. Update docs that describe current truth.
3. Run one coherence pass across README, audit, architecture, governance, and
   legal boundaries.
4. Re-run `SMOKE-01-MANIFEST-VALIDATION` against the recorded manifest path —
   it must still return `PASS` with matching SHA-256.
5. Publish the release only after the rendered repo matches the approved local
   state.

## v0.1.0-internal (Phase 03 close)

Tag spec:

| Field | Value |
|---|---|
| Tag name | `v0.1.0-internal` |
| Type | annotated |
| Pushed to remote | **NO** — local-only until owner clears licence + visibility decisions |
| Tag message | "Control-pack v0.1.0 internal — Phase 03 close. Smoke PASS; governing verdict NO_GO_GOVERNING_GATE_UNMET unchanged." |
| Required artefacts in tree | `artefacts/smoke/manifest_validation_report.json`, `artefacts/smoke/hf_upload_verify.json`, `docs/evidence/ARTEFACT_CHECKSUMS.md`, `code/cuneiform_control/`, `pyproject.toml` |

## Owner Inputs Still Required Before Any Public Release

- `OWNER_DEFERRED_VERSIONING` policy
- `CHANGELOG_LOCATION_TBD`
- `OWNER_DEFERRED_LICENSE_IDENTITY` — until set, **all release types public or
  external are forbidden**
- `NO_PUBLIC_COMPATIBILITY_PROMISE_YET`
