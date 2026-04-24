# Code

The `cuneiform_control` Python package is the minimum extracted surface for the
cuneiform control pack. It does **not** repair the inherited failed governing
gate (`NO_GO_GOVERNING_GATE_UNMET`).

## Layout

| Path | Purpose |
|---|---|
| `cuneiform_control/__init__.py` | Package marker; pins `__governing_verdict__` and `__governing_1nn_accuracy__`. |
| `cuneiform_control/schemas/benchmark_manifest.schema.json` | Conservative JSON Schema for the `annotated_sign_benchmark_manifest.json` artefact. |
| `cuneiform_control/smoke/run_manifest_validation.py` | `SMOKE-01-MANIFEST-VALIDATION` runner. Validates SHA-256, schema, and cross-field invariants. Stdlib-only. |

## Run the smoke

```bash
python3 code/cuneiform_control/smoke/run_manifest_validation.py \
  --manifest /path/to/annotated_sign_benchmark_manifest.json \
  --schema   code/cuneiform_control/schemas/benchmark_manifest.schema.json \
  --checksum e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24 \
  --report   artefacts/smoke/manifest_validation_report.json
```

A `PASS` verdict means: SHA-256 matches the pin, JSON parses, structure
conforms to the schema, and cross-field invariants hold. A `PASS` **does not**
mean the failed governing gate has been repaired.

## What is intentionally absent

- No code that reruns the failed governing 1NN probe.
- No code that promotes P6 or P7 diagnostic outputs as gate closure.
- No image-bearing or pixel-loading code.
- No external dependencies — stdlib only, on purpose.
