# Source Boundary

## Lane Role

`gnosis-cuneiform` is the cuneiform benchmark/control lane. Its boundary is the
domain-specific control material needed to preserve and later rerun the
cuneiform benchmark truth.

## In-Scope Source Families

### Upstream scripts to preserve or audit first

- `scripts/cuneiform/annotated_sign_benchmark_common.py`
- `scripts/cuneiform/benchmark_annotated_sign_tokenizer.py`
- `scripts/cuneiform/probe_annotated_sign_tokenizer_1nn.py`
- `scripts/cuneiform/benchmark_annotated_sign_p8.py`
- `scripts/cuneiform/probe_annotated_sign_p8_1nn.py`

Retired inherited references:

- `scripts/cuneiform/revert_phase2_common.py` is `UPSTREAM_NOT_PRESENT`
  (`S-06`) per `docs/evidence/ARTEFACT_CHECKSUMS.md`.
- `scripts/cuneiform/corrected_structural_benchmark.py` was a speculative
  inherited reference; `docs/PATH_REWRITE_LEDGER.md` replaced it with the
  pod-verified P7 diagnostic probe above.

### Upstream artifacts and review packs

- `workspace/artifacts/cuneiform/`
- `workspace/share/science_engineering_review_2026-04-10/`

## Explicit Exclusions

- reusable geometry and transport kernels that belong in
  `gnosis-glyph-engine`
- generic evaluation kernels that belong in `gnosis-morph-bench`
- Indus-specific catalogue or decipherment material
- heavy corpora and image-bearing asset dumps not admitted by `DATA_POLICY.md`

## Current Coupling Risks

- cuneiform scripts use local helper imports that assume the live monorepo
- some artifact paths and fetch scripts still assume upstream workspace layout
- only the manifest-validation package root is isolated; full scientific rerun
  helpers remain deferred and must not be copied in as generic shared methods

## Extraction Rule

Only copy a source family into this scaffold when its role is clearly
cuneiform-specific control or rerun logic. If the same code could govern another
lane, default to exclusion until ownership is settled.
