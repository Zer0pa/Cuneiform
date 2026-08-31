# Research State

## Current Position

Current phase: PRD COMPLETE
Current phase name: —
Status: `HOLD_CONTROL_ONLY`
Last activity: 2026-04-24

Progress: 100% of in-scope work for this PRD.

## PRD Close (2026-04-24)

All four phases closed. Governing verdict **unchanged** through every phase.

| Phase | Status | Closed | Summary |
|---|---|---|---|
| 00 Truth-Surface Bootstrap | Complete | 2026-04-23 | `.gpd/phases/00-workstream-bootstrap/00-01-SUMMARY.md` |
| 01 Control Boundary And Rerun Ledger | Complete | 2026-04-24 | `.gpd/phases/01-control-boundary-and-rerun-ledger/01-01-SUMMARY.md` |
| 02 Minimal Rerun Or Manifest Smoke | Complete | 2026-04-24 | `.gpd/phases/02-minimal-rerun-or-manifest-smoke/02-01-SUMMARY.md` |
| 03 Control-Pack Handover | Complete | 2026-04-24 | `.gpd/phases/03-control-pack-handover/03-01-SUMMARY.md` |

Smoke verdict: `SMOKE-01-MANIFEST-VALIDATION` = **PASS** against the real
upstream manifest (SHA-256 `e4d85a…3daa24`, 9,280,260 bytes).

HF custody: `Zer0pa/cuneiform-control-artefacts` (private), revision
`c64e22f671dcce1577233309fd3320258dbd2e09`.

Local staging tag: `v0.1.0-internal` (annotated, local-only; historical Phase
03 close marker).

Public custody-only release: **`v0.1.0`** (annotated, pushed to `origin/main`
on 2026-05-04T01:34:04Z, GitHub release published 2026-05-04T01:44:58Z, PyPI
`cuneiform-control` 0.1.0 Apache-2.0 live via Trusted Publishing). The release
preserves `NO_GO_GOVERNING_GATE_UNMET` verbatim in release notes, PyPI summary,
and README. See `RELEASING.md` § "v0.1.0 (Custody-only public release)" for the
full release spec.

## Active Work

None. There is no next-phase work scheduled in this lane.

## Open Questions (carried as known unknowns, not blockers)

- Whether `revert_phase2_common.py` exists upstream under a different name. Not
  blocking; recorded as `S-06` `UPSTREAM_NOT_PRESENT` in
  `docs/evidence/ARTEFACT_CHECKSUMS.md`.

## Permanent Blockers (until external gate-repair event)

- Scientifically-repaired public promotion remains blocked by
  `NO_GO_GOVERNING_GATE_UNMET`. The custody-only public release `v0.1.0`
  (live since 2026-05-04) is bounded to manifest validation; it does not
  promote the lane scientifically and explicitly preserves the failed gate.
- Raw image/corpus redistribution blocked by unresolved rights.
- Licence: Apache-2.0 (code) + CC-BY-4.0 (docs) declared and consistent across
  `LICENSE`, `pyproject.toml`, `CITATION.cff`, `.zenodo.json`, and README.
  Custody-only public release executed under this licence posture; any
  scientifically-repaired release remains gated on new scientific evidence.

## Resume

Resume only if a separate workstream repairs the governing gate on new
scientific evidence. On that event, open `/gpd:new-milestone` here.
