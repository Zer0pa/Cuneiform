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
| Tagged remote release | Shipping a milestone tag to GitHub | Owner clears versioning/tag intent; evidence, docs, data posture, and no-go wording still agree |
| Public/lab visibility | Showing the repo as a live lab window or website-sync source | Front door must keep `NO_GO_GOVERNING_GATE_UNMET` adjacent to any smoke `PASS`; no rights-gated data is exposed |
| Product or scientific-success release | Claiming release-ready product status, cuneiform recovery, or repaired science | Not currently allowed; requires repaired governing gate and a real extracted rerun surface beyond manifest validation |

## Required Checks (every tag, internal or otherwise)

- Authority artefact is current and linked from `README.md`.
- `AUDITOR_PLAYBOOK.md` still points to the right evidence.
- `PUBLIC_AUDIT_LIMITS.md` still matches the public surface.
- `docs/ARCHITECTURE.md` reflects the actual repo structure.
- `docs/evidence/ARTEFACT_CHECKSUMS.md` pins are unchanged.
- The smoke report (`artefacts/smoke/manifest_validation_report.json`) verdict
  is `PASS` and the schema/manifest SHA-256s match the pins.
- HF dataset visibility is `private` and the recorded revision matches
  current custody registers.
- Licence references are correct for the release being published.
- Release notes and roadmap language do not overclaim.
- The release does not soften `NO_GO_GOVERNING_GATE_UNMET`.
- The Ops-Gates coupling audit is either green or explicitly blocked on the
  `OPS_GATES_READ_TOKEN` CI secret.

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

## Owner Inputs Still Required Before Any Product/Scientific Release

- `OWNER_DEFERRED_VERSIONING` policy
- `CHANGELOG_LOCATION_TBD`
- explicit public-vs-internal visibility decision for the GitHub repo setting
- explicit dataset/manifest redistribution ruling for derived artefacts
- `NO_PUBLIC_COMPATIBILITY_PROMISE_YET`
