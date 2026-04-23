# Code README

## Scope

This file describes the code-facing surface for the control pack. No installable
package has been extracted yet; the current code surface is still upstream and
documented here so future extraction work has a frozen boundary.

## Layout

| Path | Purpose |
|---|---|
| `scripts/cuneiform/annotated_sign_benchmark_common.py` | Benchmark helper logic that belongs to the cuneiform control lane |
| `scripts/cuneiform/revert_phase2_common.py` | Phase 2 rerun helpers and shared cuneiform benchmark utilities |
| `scripts/cuneiform/benchmark_annotated_sign_tokenizer.py` and related probes | Candidate future rerun entry points once extracted cleanly |

## Build Or Run

```bash
# BLOCKED_PENDING_EXTRACTION
# No truthful install or smoke command exists inside this scaffold yet.
```

## Interface Surface

| Interface | Path | Input | Output | Stability |
|---|---|---|---|---|
| Benchmark manifest helpers | `scripts/cuneiform/annotated_sign_benchmark_common.py` | normalized sign records and labels | benchmark-ready tables and manifests | `EXPERIMENTAL_UPSTREAM` |
| Phase 2 rerun utilities | `scripts/cuneiform/revert_phase2_common.py` | frozen benchmark inputs and route settings | rerun outputs and summaries | `EXPERIMENTAL_UPSTREAM` |
| Probe and benchmark scripts | `scripts/cuneiform/benchmark_annotated_sign_tokenizer.py`, `scripts/cuneiform/probe_annotated_sign_tokenizer_1nn.py` | cuneiform feature manifests and labels | benchmark and probe JSON/Markdown outputs | `EXPERIMENTAL_UPSTREAM` |

## Artifact Outputs

| Artifact | Produced By | Path | Used By |
|---|---|---|---|
| Annotated sign benchmark manifest | upstream cuneiform data/build scripts | `workspace/artifacts/cuneiform/annotated_sign_benchmark_manifest.json` | control pack, future reruns |
| Phase 2 gate and diagnostics | Phase 2 control-lane execution | `workspace/artifacts/cuneiform/phase2_end_of_prd_report.md` and related JSON outputs | staged evidence summaries and future extraction work |

## Known Boundaries

- The current code still assumes upstream monorepo layout and helper imports.
- This scaffold does not yet contain admitted code; it documents the future
  extraction boundary only.
