# Cuneiform Rerun Guide

## Current Status

`BLOCKED_PENDING_EXTRACTION`

This scaffold documents the rerun target, but it does not yet ship a truthful
installable rerun path.

## Frozen Upstream Inputs

- `scripts/cuneiform/annotated_sign_benchmark_common.py`
- `scripts/cuneiform/revert_phase2_common.py`
- `scripts/cuneiform/benchmark_annotated_sign_tokenizer.py`
- `scripts/cuneiform/probe_annotated_sign_tokenizer_1nn.py`
- `workspace/artifacts/cuneiform/annotated_sign_benchmark_manifest.json`
- `workspace/artifacts/cuneiform/phase2_end_of_prd_report.md`

## What A Future Minimal Rerun Must Preserve

1. The frozen benchmark manifest and label contract.
2. The distinction between the failed P5 gate and later diagnostic branches.
3. Deterministic report emission into a repo-local artifact path.
4. No hidden dependence on the live monorepo or undeclared data.

## Known Blockers

- cuneiform scripts still use local bare-module imports and monorepo-relative
  assumptions.
- No tiny fixture or manifest-only smoke path has been admitted yet.
- Some image-bearing assets remain fetch-only or rights-constrained.

## Next Truthful Extraction Step

Extract only the benchmark helper family first, then stage one manifest
validation or tiny rerun path that still leaves the failed governing gate
visible.

