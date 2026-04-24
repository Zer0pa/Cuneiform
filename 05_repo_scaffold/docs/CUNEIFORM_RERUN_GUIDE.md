# Cuneiform Rerun Guide

## Current Status (post-Phase-03)

`SMOKE_AVAILABLE; FULL_RERUN_BLOCKED_BY_GATE`

This scaffold ships a runnable manifest-validation smoke. It does **not**
ship — and intentionally will never ship in this lane — a rerun of the failed
governing 1NN probe.

## What Runs Today

```bash
# From the scaffold root:
pip install -e .

# Or, without install:
python -m cuneiform_control.smoke.run_manifest_validation \
  --manifest /path/to/annotated_sign_benchmark_manifest.json \
  --schema   code/cuneiform_control/schemas/benchmark_manifest.schema.json \
  --checksum e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24 \
  --report   artefacts/smoke/replay_report.json

# Self-test against bundled fixtures:
python -m unittest tests.test_smoke_runner -v
```

A PASS proves manifest custody and shape against pinned SHA-256s and the
shipped JSON schema. A PASS does **not** repair
`NO_GO_GOVERNING_GATE_UNMET`.

## Frozen Upstream Inputs (pinned in `docs/evidence/ARTEFACT_CHECKSUMS.md`)

| ID | File | SHA-256 |
|---|---|---|
| `M-01` | `annotated_sign_benchmark_manifest.json` | `e4d85a…3daa24` |
| `M-02` | `05_annotated_sign_benchmark_manifest.json` | `e4d85a…3daa24` |
| `M-03` | `06_annotated_sign_p8_manifest.json` (P6 diagnostic) | `05fc85…b574` |
| `M-04` | `07_annotated_sign_p8_benchmark.json` (P6 diagnostic) | `5fd933…aeba` |
| `M-05` | `08_annotated_sign_p8_1nn_probe.json` (P7 diagnostic) | `c89657…590a` |
| `M-06` | `09_REVIEW_PACK_MANIFEST.json` | `7163ea…4aa9` |
| `S-01..S-05` | cuneiform-specific scripts | see ledger |

HF custody: `Zer0pa/cuneiform-control-artefacts` revision
`c64e22f671dcce1577233309fd3320258dbd2e09` (private).

## What A Future Minimal Rerun (in a different lane) Must Preserve

1. The frozen benchmark manifest and label contract (`schema_version: 1`).
2. The distinction between the failed P5 gate and the P6/P7 diagnostic
   branches — diagnostics never substitute for P5 closure.
3. Deterministic report emission into a repo-local artefact path.
4. No hidden dependence on the live monorepo or undeclared data.
5. Reproducible SHA-256 pins on every input.

## Known Blockers For A Full Scientific Rerun

- The cuneiform helper imports still assume the live monorepo (Phase 01–03
  did not authorize their extraction).
- Image-bearing assets remain fetch-only or rights-constrained.
- The governing gate is failed; a rerun without a credible repair path would
  reproduce the failure and risk being narrated otherwise.

## Next Truthful Step (only if owner clears scope)

Open a separate workstream (not this one) to repair the governing gate. If
that succeeds, this control pack becomes the validation reference; any rerun
work belongs in the new workstream, not here.
