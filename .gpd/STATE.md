# Research State

## Current Position

Current phase: PRD COMPLETE
Current phase name: —
Status: `HOLD_CONTROL_ONLY`
Last activity: 2026-04-28

Progress: 100% of in-scope work for this PRD.

## Operational Coherence Update (2026-04-28)

Ops-Gates adoption is staged in CI as an operational hygiene gate:
`Gnosis-Ops-Gates` `coupling_audit.py` is pinned at `54ed0a7` and scans the
Cuneiform Python surfaces without fetching HF artefacts or computing any
scientific metric. This does not move the governing gate.

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

HF custody: `Architect-Prime/cuneiform-control-artefacts` (private), latest
verified revision `3ed3f0d40585b9afa9366d7748f7d8228de1bf25`, with
`Zer0pa/cuneiform-control-artefacts` retained as a private lightweight
M-04..M-06 discovery surface at revision
`e08e1694c337a8298d92c058b416053b04f239f6`.

Local tag: `v0.1.0-internal` (annotated; **not** pushed to remote).

## Active Work

Repo-orchestrator review of the Ops-Gates/front-door coherence branch. There is
no new scientific phase scheduled in this lane.

## Open Questions (carried as known unknowns, not blockers)

- Whether `revert_phase2_common.py` exists upstream under a different name. Not
  blocking; recorded as `S-06` `UPSTREAM_NOT_PRESENT` in
  `docs/evidence/ARTEFACT_CHECKSUMS.md`.

## Permanent Blockers (until external gate-repair event)

- Product/scientific-success promotion blocked by `NO_GO_GOVERNING_GATE_UNMET`.
- Raw image/corpus redistribution blocked by unresolved rights.
- Public HF visibility or corpus redistribution blocked by unresolved
  data-rights rulings.

## Resume

Resume only if a separate workstream repairs the governing gate on new
scientific evidence. On that event, open `/gpd:new-milestone` here.
