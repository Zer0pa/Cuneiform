# Minimal Smoke Target — Phase 01 Freeze

> **Phase 01 artifact.** Names the single smallest repo-local check that will
> prove the cuneiform-control rerun contract is not narrative-only. Phase 02
> has now executed this target; current reports live at
> `artefacts/smoke/manifest_validation_report.json` and
> `artefacts/smoke/hf_upload_verify.json`.

## Freeze metadata

| Key | Value |
|---|---|
| Frozen on | 2026-04-24 |
| Phase | 01 Plan 01 |
| Status | `EXECUTED_PHASE_02_PASS` |
| Governing verdict (unchanged) | `NO_GO_GOVERNING_GATE_UNMET` |

## Candidates Considered

| # | Candidate | Pros | Cons | Decision |
|---|---|---|---|---|
| 1 | Re-run the full 1-NN probe (`probe_annotated_sign_tokenizer_1nn.py`) | Reproduces the governing metric end-to-end | Requires pixel-bearing input custody + tokenizer + full helper family; cannot run today; risks narrativizing P5 as "passing" during dev loop | **REJECTED** — oversized for Phase 02 smoke; belongs to Phase 03+ if ever earned |
| 2 | Rerun the P8 diagnostic (`benchmark_annotated_sign_p8.py`) | Already runnable upstream | Re-runs a **diagnostic** gate (P6); pack must not substitute diagnostics for P5 | **REJECTED** — violates the "no P6/P7 narration into pass" invariant |
| 3 | JSON-schema + checksum validation of the frozen `annotated_sign_benchmark_manifest.json` | No pixels, no rerun, no new numbers; verifies custody of the inherited frozen artefact and the label/sign contract | Narrow scope — proves manifest-custody only, not rerun correctness | **ADMITTED** |
| 4 | Fetch-and-checksum smoke over the review-pack JSON set (`05_`, `06_`, `07_`, `08_`) | Extends (3); catches silent asset drift | Slightly larger target; still no rerun of failing gate | **ADMITTED AS EXTENSION** — runs immediately after (3) |

## Admitted Smoke Target

**Target ID:** `SMOKE-01-MANIFEST-VALIDATION`

**One-line description:** Validate that the frozen cuneiform annotated-sign
benchmark manifest is present, checksum-matches its recorded SHA-256, conforms
to a pinned JSON schema, and preserves the label/sign class count on record at
Phase 2 close.

### Inputs

| Input | Custody | How obtained in Phase 02 |
|---|---|---|
| `annotated_sign_benchmark_manifest.json` | `PUBLISH_WITH_REVIEW` per `DATA_POLICY.md` | Held in private HF custody; checksum pin recorded in `docs/evidence/ARTEFACT_CHECKSUMS.md` |
| JSON schema | in-tree | `code/cuneiform_control/schemas/benchmark_manifest.schema.json` |
| Expected label/sign class count | from `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` | static expectation record |

### Pass Condition (what counts as smoke-passing, and what it does NOT mean)

A smoke PASS means **all** of:

1. The manifest is fetched by checksum and the SHA-256 matches the pinned value.
2. The JSON parses without error.
3. The parsed manifest validates against the pinned schema.
4. The sign/class vocabulary and label count match the Phase 2 gate record.
5. A deterministic smoke report is emitted to
   `artefacts/smoke/manifest_validation_report.json` with the inputs, the
   checksums, the schema hash, the expected-vs-observed vocabulary summary,
   and the verdict `PASS`.

A smoke PASS **does not** mean:

- the failed governing gate has been repaired,
- `governing_1nn_accuracy` has changed from `0.021916`,
- any public-promotion criterion has been met,
- pixel-bearing assets have been cleared for redistribution.

Any of the above still require fresh scientific evidence, not a smoke success.

### Fail Modes And Required Response

| Fail mode | Required response |
|---|---|
| SHA-256 mismatch | Refuse to promote; open a blocker; do **not** overwrite the pinned checksum. |
| Schema violation | Record the violation in the smoke report; leave the frozen governing verdict intact; open a task to amend the schema or the upstream manifest, not the gate. |
| Vocabulary drift | Record as an **evidence divergence**, not as a gate change. Blocks promotion until reconciled. |
| Fetch unavailable | `BLOCKED_FETCH`; execution deferred until HF custody is populated. |

### Explicit Non-Goals

- No centroid / 1-NN / transport accuracy is computed.
- No pixel data is read.
- No monorepo helper is imported.
- No P6 or P7 diagnostic is executed.

### Why This Target Passes Phase 01

1. It is the **smallest** check that distinguishes a real control pack from a
   narrative one.
2. It proves custody without vendoring rights-constrained data.
3. It cannot accidentally narrate `NO_GO_GOVERNING_GATE_UNMET` into a pass — by
   construction it computes no scientific metric.
4. It exposes the `CUNEIFORM_SPECIFIC` vs `SHARED_METHOD` boundary (only a
   tiny manifest-validation module is admitted) before any heavier extraction.

## Phase 02 Preconditions (satisfied 2026-04-24)

- HF dataset `Zer0pa/cuneiform-control-artefacts` created and populated.
- `docs/evidence/ARTEFACT_CHECKSUMS.md` authored with SHA-256s.
- `code/cuneiform_control/schemas/benchmark_manifest.schema.json` authored.
- `code/cuneiform_control/smoke/run_manifest_validation.py` extracted per the
  path-rewrite ledger.

## Phase 02 Explicitly Forbidden

- Re-running the failed governing probe and narrating any result as a pass.
- Uploading pixel-bearing corpora to HF or GitHub.
- Copying any `SHARED_METHOD` code from group (B) of the path-rewrite ledger
  into this repo.
