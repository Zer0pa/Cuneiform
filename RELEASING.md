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
| **Custody-only public release** (e.g. `v0.1.0` on PyPI as `cuneiform-control`) | Shipping the manifest-validation control pack publicly while the scientific gate remains failed | Apache-2.0 (code) / CC-BY-4.0 (docs) declared; smoke `PASS` recorded; HF custody pinned; release notes and PyPI summary explicitly preserve `NO_GO_GOVERNING_GATE_UNMET`; **no decipherment claimed**; no image-bearing source corpora redistributed |
| Scientifically-repaired public release | Promoting the lane beyond custody-only | **Not currently allowed.** Requires repaired governing gate on new scientific evidence, AND a real extracted rerun surface that goes beyond manifest validation |

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

## v0.1.0-internal (Phase 03 close, historical)

Tag spec:

| Field | Value |
|---|---|
| Tag name | `v0.1.0-internal` |
| Type | annotated, local-only |
| Tag message | "Control-pack v0.1.0 internal — Phase 03 close. Smoke PASS; governing verdict NO_GO_GOVERNING_GATE_UNMET unchanged." |
| Status | Historical staging tag; superseded by the public custody-only release `v0.1.0` (below) |

## v0.1.0 (Custody-only public release, 2026-05-04)

Release spec — what was actually shipped:

| Field | Value |
|---|---|
| Tag name | `v0.1.0` |
| Type | annotated, pushed to `origin/main` |
| GitHub release | `https://github.com/Zer0pa/Cuneiform/releases/tag/v0.1.0` (published 2026-05-04T01:44:58Z) |
| PyPI | `cuneiform-control` 0.1.0 (Apache-2.0, Trusted Publishing via `.github/workflows/publish.yml`) |
| PyPI summary (verbatim) | "Control-pack manifest validation for the cuneiform benchmark lane. Stdlib-only. **Does not repair the failed governing gate.**" |
| Required artefacts in tree | `artefacts/smoke/manifest_validation_report.json`, `artefacts/smoke/hf_upload_verify.json`, `docs/evidence/ARTEFACT_CHECKSUMS.md`, `code/cuneiform_control/`, `pyproject.toml` |
| Failed-gate boundary preserved | `NO_GO_GOVERNING_GATE_UNMET` carried verbatim into release notes, PyPI summary, README, and `.gpd/STATE.md`; no decipherment claimed; no image-bearing source corpora redistributed |
| Scope discipline | Custody and shape only. The release proves the manifest chain replays bit-identically; it does **not** repair the scientific gate, decipher cuneiform, or unblock private corpus rights |

## Owner Inputs Resolved Before v0.1.0 Custody-only Release

- ✅ Licence: Apache-2.0 (code) + CC-BY-4.0 (docs) — declared in `LICENSE`, `pyproject.toml`, `CITATION.cff`, `.zenodo.json`, README; `Private :: Do Not Upload` classifier removed (`3d29caa`)
- ✅ Versioning: SemVer; v0.1.0 first public custody-only release
- ✅ Changelog location: GitHub releases page + repo `CHANGELOG.md`
- ✅ Compatibility promise: bounded — Python ≥ 3.8, stdlib-only smoke runner; manifest format pinned by `artefacts/smoke/manifest_validation_report.json`

## Owner Inputs Still Required Before Any Scientifically-Repaired Release

- Repaired governing gate on new scientific evidence (`NO_GO_GOVERNING_GATE_UNMET` cleared)
- Extracted rerun surface beyond manifest validation
- Image/corpus rights resolution for any redistributable raw-data surface
