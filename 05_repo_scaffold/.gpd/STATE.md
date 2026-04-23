# Research State

## Current Position

Current phase: `02`
Current phase name: Minimal Rerun Or Manifest Smoke
Status: `HOLD_CONTROL_ONLY`
Last activity: 2026-04-24

Progress: 55%

## Phase 01 Close (2026-04-24)

Phase 01 `01-control-boundary-and-rerun-ledger` is complete.

- Path-rewrite ledger frozen: `docs/PATH_REWRITE_LEDGER.md`.
- Minimal smoke target admitted: `docs/MINIMAL_SMOKE_TARGET.md`
  (`SMOKE-01-MANIFEST-VALIDATION`).
- Phase summary: `.gpd/phases/01-control-boundary-and-rerun-ledger/01-01-SUMMARY.md`.
- Governing verdict `NO_GO_GOVERNING_GATE_UNMET` **unchanged**; governing
  metric `governing_1nn_accuracy = 0.021916` **unchanged**.
- Repo remote wired: `https://github.com/Zer0pa/Cuneiform` (INTERNAL, `main`).

## Active Work (Phase 02)

- Execute `SMOKE-01-MANIFEST-VALIDATION` per the admitted spec.
- Create HF dataset `Zer0pa/cuneiform-control-artefacts` and populate with the
  pinned manifests.
- Author `code/cuneiform_control/schemas/benchmark_manifest.schema.json`.
- Extract the minimum helper module per the path-rewrite ledger (group A only).
- Emit the deterministic smoke report with verdict, checksums, and schema hash.

## Open Questions

- Exact SHA-256 of the current `annotated_sign_benchmark_manifest.json` — to be
  recorded in `docs/evidence/ARTEFACT_CHECKSUMS.md` as Phase 02 opens.
- Whether HF dataset visibility is `private` or `public` for INTERNAL custody —
  default to `private` pending owner ruling.

## Blockers

- Public promotion remains blocked by `NO_GO_GOVERNING_GATE_UNMET`.
- Raw image and corpus redistribution remains blocked by unresolved rights.
- Phase 02 smoke execution is **not** blocked; it proceeds on Phase 02 entry.

## Resume

Resume from `.gpd/phases/02-minimal-rerun-or-manifest-smoke/02-01-PLAN.md`
(to be authored at Phase 02 entry).
