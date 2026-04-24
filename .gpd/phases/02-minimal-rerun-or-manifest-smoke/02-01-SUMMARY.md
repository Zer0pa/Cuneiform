# Phase 02 Plan 01 — Summary

## Close

Phase 02 `02-minimal-rerun-or-manifest-smoke` closed on 2026-04-24 under the
autonomous execution policy. Smoke verdict: **PASS**. Governing verdict
**unchanged**.

## What Was Produced

| Artefact | Purpose | Status |
|---|---|---|
| `docs/evidence/ARTEFACT_CHECKSUMS.md` | Pinned SHA-256 for 6 manifests + 5 source scripts; recorded `S-06` `revert_phase2_common.py` as `UPSTREAM_NOT_PRESENT`; recorded manifest invariants. | Frozen |
| `code/cuneiform_control/__init__.py` | Package marker; pins governing verdict + metric. | Created |
| `code/cuneiform_control/schemas/benchmark_manifest.schema.json` | Conservative JSON Schema for the manifest. | Created |
| `code/cuneiform_control/smoke/run_manifest_validation.py` | `SMOKE-01-MANIFEST-VALIDATION` runner; stdlib-only; SHA + schema + cross-field invariants; deterministic JSON report. | Executable |
| `artefacts/smoke/manifest_validation_report.json` | Deterministic smoke report (`PASS`, all invariants OK, sha256 matches pin). | Emitted from pod |
| `artefacts/smoke/hf_upload_verify.json` | Post-upload SHA-256 verify report; HF revision recorded. | Created |
| HF dataset `<HF_ORG>/cuneiform-control-artefacts` | Private; 6 manifests + dataset card; revision `c64e22f671dcce1577233309fd3320258dbd2e09`. | Created + populated |
| `docs/PATH_REWRITE_LEDGER.md` | Amended: `revert_phase2_common.py` retired (`UPSTREAM_NOT_PRESENT`); `probe_annotated_sign_p8_1nn.py` added as P7 diagnostic; SHA pins cross-referenced. | Amended |
| `code/README.md` | Documents the smoke surface. | Updated |
| `.gpd/REQUIREMENTS.md` | `SIMU-01`, `SIMU-02`, `VALD-02` complete. | Updated |
| `.gpd/ROADMAP.md`, `STATE.md`, `state.json` | Phase 03 active; Phase 02 close recorded with HF revision. | Updated |

## Smoke Execution Evidence

```
Smoke runner:    code/cuneiform_control/smoke/run_manifest_validation.py
Manifest:        <MONOREPO>/workspace/artifacts/cuneiform/annotated_sign_benchmark_manifest.json
Manifest bytes:  9,280,260
SHA-256 pinned:  e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24
SHA-256 obs:     e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24  (MATCH)
Schema SHA-256:  8f86ba76580a42d9f1b10914d7bff762cf3177ca37d7c7c9c6f409814a3ea181
Schema errors:   0
Invariants:      5/5 pass
  - summary.available_sign_record_count == len(sign_records): 7462 == 7462
  - summary.downloaded_tablet_count == len(tablets):           72   == 72
  - summary.missing_tablet_count == len(missing_tablets_preview): 9 == 9
  - summary.annotated_tablet_count == downloaded + missing:    81  == 72+9
  - schema_version == 1:                                       1   == 1
Verdict:         PASS
Exit code:       0
```

## HF Upload Evidence

```
Repo:           <HF_ORG>/cuneiform-control-artefacts (dataset, private)
Revision:       c64e22f671dcce1577233309fd3320258dbd2e09
URL:            https://huggingface.co/datasets/<HF_ORG>/cuneiform-control-artefacts/tree/c64e22f671dcce1577233309fd3320258dbd2e09
Files:          M-01..M-06 + README.md + .gitattributes
Post-upload SHA-256 verify: 6/6 OK against pinned values
```
(Full token-verified HF state lives in `docs/HF_CUSTODY_REGISTER.md`.)

## Governing-Gate Delta

| Metric | Before | After | Delta |
|---|---|---|---|
| Governing verdict | `NO_GO_GOVERNING_GATE_UNMET` | `NO_GO_GOVERNING_GATE_UNMET` | `unchanged` |
| `governing_1nn_accuracy` | `0.021916` | `0.021916` | `unchanged` |
| P6 diagnostic accuracy | `0.038176` | `0.038176` | `unchanged; remains diagnostic-only` |
| P7 diagnostic accuracy | `0.051826` | `0.051826` | `unchanged; remains diagnostic-only` |
| Promotion posture | blocked | blocked | `unchanged` |

This is the correct outcome. The smoke proves manifest custody and shape, not
scientific recovery. By construction it cannot move the gate.

## Pass-Condition Check

Phase 02 pass condition (`02-01-PLAN.md`):

> Smoke report exists, contains verdict `PASS`, all six pinned checksums match,
> schema validation succeeds, cross-field invariants hold, and HF revision is
> recorded. Governing verdict remains `NO_GO_GOVERNING_GATE_UNMET`.

| Criterion | Evidence | Status |
|---|---|---|
| Smoke report exists, verdict `PASS` | `artefacts/smoke/manifest_validation_report.json` | Pass |
| 6 pinned checksums match | `artefacts/smoke/hf_upload_verify.json` `all_verified: true` | Pass |
| Schema validation succeeds | `schema_errors: []` in smoke report | Pass |
| Cross-field invariants hold | `5/5` invariants OK | Pass |
| HF revision recorded | `c64e22f671dcce1577233309fd3320258dbd2e09` in HF report | Pass |
| Governing verdict unchanged | Both reports carry `NO_GO_GOVERNING_GATE_UNMET` | Pass |

**Phase 02 gate: PASS.** Governing verdict remains
`NO_GO_GOVERNING_GATE_UNMET` by design.

## Executive Decisions Made Autonomously

1. **Stdlib-only smoke runner.** Refused to add `jsonschema` (or any third-party
   dep). Reason: the smoke must be runnable on any Python 3.8+ host without
   provisioning; the schema subset needed is small enough to inline.
2. **`revert_phase2_common.py` retired as `UPSTREAM_NOT_PRESENT`.** Reason: pod
   audit found no such file under `scripts/cuneiform/`. Removing speculative
   entries from the ledger is required by the truth contract.
3. **`probe_annotated_sign_p8_1nn.py` added as P7 diagnostic.** Reason: pod
   audit confirmed it exists; the inherited `SOURCE_BOUNDARY.md` reference to
   `corrected_structural_benchmark.py` was speculative and could not be
   verified — it is replaced by the verified file with `_diagnostic` suffix.
4. **HF filenames carry `M-NN_` prefix.** Reason: collisions otherwise (M-01
   and M-02 share content); the prefix gives the dataset a deterministic
   ordering keyed to `ARTEFACT_CHECKSUMS.md`.
5. **HF dataset card includes `governing_verdict` block.** Reason: any
   downstream consumer must see the failed-gate posture before any data
   download.
6. **HF visibility hard-locked to `private`.** Reason: `DATA_POLICY.md`
   `PUBLISH_WITH_REVIEW` for derived JSON + `NO_GO_GOVERNING_GATE_UNMET` block.
7. **Smoke runner reports both pinned and observed SHA-256.** Reason: an
   evidence run must be reproducible; recording both lets a fresh agent verify
   the pin still applies in a future re-run.

## What Was Explicitly Not Done

- The failed governing 1NN probe was **not** rerun.
- No P6/P7 diagnostic was promoted as gate closure (both kept the
  `diagnostic_only` flag in the dataset card and the upload report).
- No pixel-bearing source was uploaded to HF.
- No code from Path-Rewrite-Ledger group (B) `SHARED_METHOD` was touched.
- Public visibility was not granted on either GH or HF.

## Open Blockers Carried Forward

1. Public promotion — still blocked by `NO_GO_GOVERNING_GATE_UNMET`.
2. Image/pixel redistribution — still blocked by unresolved rights.
3. Licence text — `OWNER_DEFERRED`. Required ruling before any public surface.
4. `S-06` `revert_phase2_common.py` — file may exist under a different name
   upstream; not a Phase-02 blocker, but flagged for owner if a rerun ever
   needs the rollback semantics that filename suggested.

## Next Phase Entry

`.gpd/phases/03-control-pack-handover/03-01-PLAN.md` is being authored as the
first act of Phase 03.
