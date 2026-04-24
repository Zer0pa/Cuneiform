# Requirements: gnosis-cuneiform

Defined: 2026-04-23

## Primary Requirements

- [x] **DATA-01**: Preserve the cuneiform control-pack substrate and truth
      surfaces inside this scaffold.
- [x] **DATA-02**: Preserve the inherited failed governing gate as
      `NO_GO_GOVERNING_GATE_UNMET` with
      `governing_1nn_accuracy = 0.021916`.
- [x] **DATA-03**: Freeze the exact source-to-destination ledger for the first
      cuneiform-specific rerun slice. (`docs/PATH_REWRITE_LEDGER.md`, frozen 2026-04-24)
- [x] **DERV-01**: State that this lane owns cuneiform control/rerun material
      only, not generic benchmark methodology.
- [x] **DERV-02**: Define the minimal rerun contract and the fixtures or fetch
      records needed to execute it. (`docs/MINIMAL_SMOKE_TARGET.md`, admitted 2026-04-24; execution deferred to Phase 02)
- [x] **SIMU-01**: Extract or stub the minimal cuneiform rerun path without
      live-monorepo imports. (`code/cuneiform_control/smoke/run_manifest_validation.py`,
      stdlib-only; Phase 02, 2026-04-24)
- [x] **SIMU-02**: Emit checksums, manifest records, or fetch notes for every
      input used by the rerun. (`docs/evidence/ARTEFACT_CHECKSUMS.md`,
      `artefacts/smoke/manifest_validation_report.json`,
      `artefacts/smoke/hf_upload_verify.json`; Phase 02, 2026-04-24)
- [x] **VALD-01**: Reject public promotion while the failed scientific gate is
      unchanged.
- [x] **VALD-02**: Run the minimal rerun or manifest validation from repo
      custody. (Smoke executed 2026-04-24, verdict `PASS`,
      `artefacts/smoke/manifest_validation_report.json`)
- [x] **WRIT-01**: Update handover notes only after the source ledger and rerun
      target are frozen. (`06_handover/README.md` rewritten 2026-04-24 with
      Phase 02 evidence + HF revision + smoke-PASS posture; ARCHITECTURE,
      AUDITOR_PLAYBOOK, PUBLIC_AUDIT_LIMITS, RELEASING all updated in Phase 03.)

## Out Of Scope

| Topic | Reason |
|---|---|
| Public release | Failed gate blocks promotion. |
| Pixel or raw corpus release | Rights posture is unresolved. |
| Generic benchmark ownership | Belongs in `gnosis-morph-bench` or `gnosis-falsification-harness`. |
| Glyph descriptor framework | Belongs in `gnosis-glyph-engine` if earned later. |

## Traceability

| Requirement | Phase | Status |
|---|---|---|
| `DATA-01`, `DATA-02`, `DERV-01`, `VALD-01` | Phase 00 | Complete |
| `DATA-03`, `DERV-02` | Phase 01 | Complete (2026-04-24) |
| `SIMU-01`, `SIMU-02`, `VALD-02` | Phase 02 | Complete (2026-04-24) |
| `WRIT-01` | Phase 03 | Complete (2026-04-24) |
