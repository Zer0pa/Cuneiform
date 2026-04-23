# Evidence Manifest

Evidence surfaces are staged under `../05_repo_scaffold/docs/evidence/` and
`../05_repo_scaffold/docs/` (for Phase 01 ledgers). Derived JSON manifests are
routed to Hugging Face (`Zer0pa/cuneiform-control-artefacts`, private) rather
than vendored into git.

Required preserved truths:

- failed cuneiform gate stays visible,
- P6/P7 diagnostics do not become pass narratives,
- future reruns must name source, input custody, and smoke evidence.

## Custody Classes

- `PUBLISH_NOW` — in-tree text authored for this pack.
- `PUBLISH_WITH_REVIEW` — small derived JSON; routed through HF with checksum
  pins; not vendored in git.
- `FETCH_EXTERNALLY_OR_INTERNAL_ONLY` — image/pixel-bearing; never vendored.
- `INTERNAL_ONLY` — model weights, checkpoints; not admitted here.

## Phase 00 Artefacts

| Artefact | Custody | Path |
|---|---|---|
| Sovereign PRD | `PUBLISH_NOW` | `05_repo_scaffold/SOVEREIGN_PRD.md` |
| Source boundary | `PUBLISH_NOW` | `05_repo_scaffold/SOURCE_BOUNDARY.md` |
| Data policy | `PUBLISH_NOW` | `05_repo_scaffold/DATA_POLICY.md` |
| Failed-gate status | `PUBLISH_NOW` | `05_repo_scaffold/docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` |
| Control results | `PUBLISH_NOW` | `05_repo_scaffold/docs/evidence/CUNEIFORM_CONTROL_RESULTS.md` |
| Benchmark pack contract | `PUBLISH_NOW` | `05_repo_scaffold/docs/family/CUNEIFORM_BENCHMARK_PACK_CONTRACT.md` |

## Phase 01 Artefacts (closed 2026-04-24)

| Artefact | Custody | Path |
|---|---|---|
| Path-rewrite ledger | `PUBLISH_NOW` | `05_repo_scaffold/docs/PATH_REWRITE_LEDGER.md` |
| Minimal smoke target | `PUBLISH_NOW` | `05_repo_scaffold/docs/MINIMAL_SMOKE_TARGET.md` |
| Phase 01 summary | `PUBLISH_NOW` | `05_repo_scaffold/.gpd/phases/01-control-boundary-and-rerun-ledger/01-01-SUMMARY.md` |

## Phase 02 Pending Artefacts

| Artefact | Custody | Target location |
|---|---|---|
| Phase 02 plan | `PUBLISH_NOW` | `05_repo_scaffold/.gpd/phases/02-minimal-rerun-or-manifest-smoke/02-01-PLAN.md` |
| Artefact checksum pins | `PUBLISH_NOW` | `05_repo_scaffold/docs/evidence/ARTEFACT_CHECKSUMS.md` |
| Benchmark manifest JSON schema | `PUBLISH_NOW` | `05_repo_scaffold/code/cuneiform_control/schemas/benchmark_manifest.schema.json` |
| `annotated_sign_benchmark_manifest.json` | `PUBLISH_WITH_REVIEW` | HF `Zer0pa/cuneiform-control-artefacts` (private) |
| `05_…08_` review-pack JSON | `PUBLISH_WITH_REVIEW` | HF `Zer0pa/cuneiform-control-artefacts` (private) |
| Smoke validation report | `PUBLISH_NOW` | `05_repo_scaffold/artefacts/smoke/manifest_validation_report.json` |

## Governing-Gate Register (read-only for narrative purposes)

| Metric | Value | Source |
|---|---|---|
| Governing verdict | `NO_GO_GOVERNING_GATE_UNMET` | `CUNEIFORM_PHASE2_GATE_STATUS.md` |
| `governing_1nn_accuracy` | `0.021916` | P5 of upstream cuneiform artefact chain |
| P6 diagnostic best | `0.038176` | `CUNEIFORM_PHASE2_GATE_STATUS.md` (diagnostic-only) |
| P7 diagnostic best | `0.051826` | `CUNEIFORM_PHASE2_GATE_STATUS.md` (diagnostic-only) |

Only a genuinely new scientific run (not in scope for this pack) may update
these values.
