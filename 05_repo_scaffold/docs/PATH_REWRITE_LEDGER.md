# Path-Rewrite Ledger — Phase 01 Freeze

> **Phase 01 artifact.** Freezes the exact cuneiform-specific source-to-destination
> mapping for the first rerun slice. This ledger is append-only once frozen. It
> does not authorize extraction, publication, or a rerun — it only records the
> boundary so a fresh agent can see exactly what belongs where.

## Freeze metadata

| Key | Value |
|---|---|
| Frozen on | 2026-04-24 |
| Frozen by | autonomous executor under `AUTONOMOUS_EXECUTION_POLICY.md` |
| Governing verdict (unchanged) | `NO_GO_GOVERNING_GATE_UNMET` |
| Governing metric (unchanged) | `governing_1nn_accuracy = 0.021916` |
| Authority metric | `control_truth_preserved` |
| Repo | `https://github.com/Zer0pa/Cuneiform` (INTERNAL) |

## Legend

| Label | Meaning |
|---|---|
| `CUNEIFORM_SPECIFIC` | Logic is only meaningful for the cuneiform control lane — admit into this scaffold under `code/`. |
| `SHARED_METHOD` | Logic is generic benchmark/transport machinery — **excluded**; belongs in `gnosis-morph-bench` or `gnosis-glyph-engine`. |
| `DERIVED_ARTEFACT` | Output of a prior run, not source — staged under `docs/evidence/` (summaries only) or Hugging Face (manifests and JSON). |
| `REVIEW_PACK` | Frozen review/audit document set — referenced, not vendored. |
| `FETCH_EXTERNALLY` | Large or rights-constrained asset — never vendored; fetched via checksum manifest. |

## Source-to-Destination Ledger

### A. Cuneiform-specific scripts (admitted, extraction deferred to Phase 02)

| Upstream source | Classification | Destination in this repo | Phase that extracts | Custody note |
|---|---|---|---|---|
| `scripts/cuneiform/annotated_sign_benchmark_common.py` | `CUNEIFORM_SPECIFIC` | `code/cuneiform_control/benchmark_common.py` | Phase 02 | strip monorepo helper imports; re-root as a package module |
| `scripts/cuneiform/revert_phase2_common.py` | `CUNEIFORM_SPECIFIC` | `code/cuneiform_control/rerun_phase2_common.py` | Phase 02 | rename retires the imperative `revert_` prefix; semantics preserved |
| `scripts/cuneiform/benchmark_annotated_sign_tokenizer.py` | `CUNEIFORM_SPECIFIC` | `code/cuneiform_control/bench_tokenizer.py` | Phase 02 | entry point for tokenizer benchmark rerun |
| `scripts/cuneiform/probe_annotated_sign_tokenizer_1nn.py` | `CUNEIFORM_SPECIFIC` | `code/cuneiform_control/probe_1nn.py` | Phase 02 | produces the frozen governing metric `governing_1nn_accuracy` |
| `scripts/cuneiform/benchmark_annotated_sign_p8.py` | `CUNEIFORM_SPECIFIC` (diagnostic) | `code/cuneiform_control/bench_p8_diagnostic.py` | Phase 02 | P6 diagnostic only — **never** promoted as gate closure |
| `scripts/cuneiform/corrected_structural_benchmark.py` | `CUNEIFORM_SPECIFIC` (diagnostic) | `code/cuneiform_control/bench_structural_diagnostic.py` | Phase 02 | P7 diagnostic only — **never** promoted as gate closure |

### B. Shared-method candidates (excluded from this lane)

| Upstream source (probable location) | Why excluded | Target lane |
|---|---|---|
| generic 1-NN / centroid probes (any non-cuneiform-specific distance or reducer code) | generic evaluation kernel | `gnosis-morph-bench` |
| geometric / transport kernels (any reusable descriptor, alignment, or transport code) | reusable representation logic | `gnosis-glyph-engine` |
| generic fetch/checksum helpers | cross-cutting infrastructure | portfolio-shared tooling |
| Indus-specific label, catalogue, or decipherment material | wrong script family | `gnosis-indus-*` (if earned later) |

Exclusion is enforced by the extraction rule in `SOURCE_BOUNDARY.md`: if the same
code could govern another lane, **default to exclusion** until ownership is
settled.

### C. Derived artefacts (summaries in-tree; JSON to HF)

| Upstream artefact | Classification | Destination | Custody |
|---|---|---|---|
| `workspace/artifacts/cuneiform/annotated_sign_benchmark_manifest.json` | `DERIVED_ARTEFACT` | HF dataset `Zer0pa/cuneiform-control-artefacts` (staged; upload deferred to Phase 02 smoke) | `PUBLISH_WITH_REVIEW` per `DATA_POLICY.md` |
| `workspace/artifacts/cuneiform/phase2_end_of_prd_report.md` | `DERIVED_ARTEFACT` | `docs/evidence/phase2_end_of_prd_report.md` (text only) | `PUBLISH_NOW` as derived text |
| `05_annotated_sign_benchmark_manifest.json` (review pack) | `DERIVED_ARTEFACT` | HF dataset staged; referenced via checksum in `MINIMAL_SMOKE_TARGET.md` | `PUBLISH_WITH_REVIEW` |
| `06_annotated_sign_p8_manifest.json` | `DERIVED_ARTEFACT` | HF dataset staged | `PUBLISH_WITH_REVIEW` |
| `07_annotated_sign_p8_benchmark.json` | `DERIVED_ARTEFACT` (P6) | HF dataset staged; diagnostic-only label required | `PUBLISH_WITH_REVIEW` |
| `08_annotated_sign_p8_1nn_probe.json` | `DERIVED_ARTEFACT` (P7) | HF dataset staged; diagnostic-only label required | `PUBLISH_WITH_REVIEW` |

### D. Review pack (referenced, not vendored)

| Upstream path | Classification | Destination |
|---|---|---|
| `workspace/share/science_engineering_review_2026-04-10/04_OUTPUTS_AND_RESULTS.md` | `REVIEW_PACK` | referenced in `docs/evidence/CUNEIFORM_CONTROL_RESULTS.md` — not copied |
| `workspace/share/science_engineering_review_2026-04-10/` (remainder) | `REVIEW_PACK` | referenced, not vendored |

### E. Raw data (fetch-only, forever until rights clear)

| Family | Classification | Destination |
|---|---|---|
| image-bearing corpora (all) | `FETCH_EXTERNALLY` | never vendored; fetch/checksum manifest only |
| model weights, intermediate checkpoints | `INTERNAL_ONLY` | not admitted to this repo |
| heavy rerun substrates | `FETCH_EXTERNALLY` | never vendored |

## Custody Invariants

1. No file listed under (A) is copied into `code/` before Phase 02 Plan 01
   approves the extraction with its import-rewrite diff.
2. No file listed under (C) is uploaded to HF before `MINIMAL_SMOKE_TARGET.md`
   admits it by SHA-256.
3. No file listed under (D) or (E) is vendored under any circumstance permitted
   by this ledger.
4. Any extraction that needs code from group (B) is a **blocker**, not a task.
   Raise it against the owning lane.

## Decision Log

| Decision | Rationale |
|---|---|
| Rename `revert_phase2_common` → `rerun_phase2_common` | `revert_` suggests rollback semantics that do not match the code's role as a rerun helper; rename makes the control-pack intent explicit. |
| Keep P6 and P7 scripts with `_diagnostic` suffix | Extraction is permitted, but the suffix enforces the invariant that these are never substituted for the failed P5 governing gate. |
| HF staging rather than in-tree JSON | `DATA_POLICY.md` tags derived manifests `PUBLISH_WITH_REVIEW`; HF with checksum records respects that without blocking future reruns. |
| Repo visibility `INTERNAL` | Matches the PRD: public promotion is blocked while `NO_GO_GOVERNING_GATE_UNMET` stands. |
| Default branch `main` | Matches scaffold README and GitHub repo metadata. |
| Retire `scripts/cuneiform/` path prefix on destination | The destination is a package, not a loose script folder; the monorepo-relative prefix is a coupling the pack should not inherit. |

## What This Ledger Does Not Do

- It does not close `DATA-03` without `MINIMAL_SMOKE_TARGET.md`.
- It does not admit any code into the repo — Phase 01 is boundary-only.
- It does not rerun, modify, or narrate the failed governing gate.
- It does not authorize public promotion.
