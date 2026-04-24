# Handover (migration-pack copy)

> **Migration artefact.** The canonical handover lives at the repository root
> via `README.md` and `docs/EXECUTOR_STATUS_REPORT.md`. Paths below resolve
> relative to the new repo root.

> **State at 2026-04-24.** Phases 00–03 closed; Closeout pass (2026-04-24)
> flattened the repo root and scrubbed operational path/endpoint leaks.

## Read Order For A Fresh Agent

1. `../../../README.md`
2. `../../../SOVEREIGN_PRD.md`
3. `../../../SOURCE_BOUNDARY.md`
4. `../../../DATA_POLICY.md`
5. `../../evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`
6. `../../PATH_REWRITE_LEDGER.md`
7. `../../MINIMAL_SMOKE_TARGET.md`
8. `../../evidence/ARTEFACT_CHECKSUMS.md`
9. `../../../artefacts/smoke/manifest_validation_report.json`
10. `../../../artefacts/smoke/hf_upload_verify.json`
11. `../../HF_CUSTODY_REGISTER.md`
12. `../../../.gpd/STATE.md`

## Current Truth (UNCHANGED through all phases)

| Item | Value |
|---|---|
| Lane class | `MODULE_ONLY_CONTROL_PACK` |
| Governing verdict | `NO_GO_GOVERNING_GATE_UNMET` |
| Governing metric | `governing_1nn_accuracy = 0.021916` |
| Repo | `https://github.com/Zer0pa/Cuneiform` (INTERNAL, `main`) |
| HF dataset | `<HF_ORG>/cuneiform-control-artefacts` (private, see `HF_CUSTODY_REGISTER.md`) |
| Smoke verdict (`SMOKE-01-MANIFEST-VALIDATION`) | `PASS` (executed 2026-04-24) |
| Public release | **FORBIDDEN** until governing gate repaired on new evidence |

## Do Not

- Public-promote this lane.
- Push the `v0.1.0-internal` tag to GitHub or to any public surface.
- Set the HF dataset visibility to anything other than `private`.
- Re-run the failed governing 1NN probe and report any number from this lane.

## Resume Path

If you need to do anything more here, start at `../../../.gpd/STATE.md`. There
are no unscheduled phases. Any new work is a new milestone
(`/gpd:new-milestone`) gated on a gate-repair event in a separate workstream.
