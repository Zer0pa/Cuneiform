# TODO

## Now (Phase 02: Minimal Rerun Or Manifest Smoke)

- [ ] Author `.gpd/phases/02-minimal-rerun-or-manifest-smoke/02-01-PLAN.md`.
- [ ] Create HF dataset `Zer0pa/cuneiform-control-artefacts` (private) and upload
      the pinned manifests per `DATA_POLICY.md` `PUBLISH_WITH_REVIEW`.
- [ ] Author `docs/evidence/ARTEFACT_CHECKSUMS.md` with SHA-256 pins.
- [ ] Author `code/cuneiform_control/schemas/benchmark_manifest.schema.json`.
- [ ] Extract the minimum helper module per Path-Rewrite Ledger group A into
      `code/cuneiform_control/` (strip monorepo imports).
- [ ] Execute `SMOKE-01-MANIFEST-VALIDATION` and emit the deterministic report.

## Phase 01 Closed (2026-04-24)

- [x] Freeze a complete path-rewrite ledger — `docs/PATH_REWRITE_LEDGER.md`.
- [x] Decide which derived benchmark manifests are safe to stage beyond summary
      docs — covered by the Ledger §C (HF with `PUBLISH_WITH_REVIEW` custody).
- [x] Define one truthful minimal rerun target — `docs/MINIMAL_SMOKE_TARGET.md`
      `SMOKE-01-MANIFEST-VALIDATION`.

## Later

- [ ] After Phase 02 smoke passes, extend with fetch-and-checksum smoke over
      the `05_…08_` review-pack JSON set (listed as smoke-candidate #4).
- [ ] Reassess control-lane packaging only after the underlying science gate is
      repaired on evidence in a separate workstream.

## Must Stay Blocked

- [ ] Public promotion while `NO_GO_GOVERNING_GATE_UNMET` remains unchanged.
- [ ] Any repo narrative that upgrades the lane beyond benchmark/control use.
- [ ] Heavy asset vendoring without explicit rights clearance.
- [ ] Re-running the failed governing probe and narrating any result as a pass.
- [ ] Promoting P6 or P7 diagnostic numbers as substitute gate closure.
