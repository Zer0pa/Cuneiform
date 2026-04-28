# Hugging Face Dataset Plan — historical Phase 01 plan

> **Phase 01 staging artefact.** This file names the HF dataset and its custody
> rules. Phase 02 and later custody work has now executed; current authority is
> `docs/HF_CUSTODY_REGISTER.md` plus `docs/evidence/ARTEFACT_CHECKSUMS.md`.
> This file is retained as planning history, not current HF state.

## Current State As Of 2026-04-28

| Surface | State |
|---|---|
| Canonical heavy/private store | `Architect-Prime/cuneiform-control-artefacts`, private, latest verified revision `3ed3f0d40585b9afa9366d7748f7d8228de1bf25` |
| Lightweight private discovery surface | `Zer0pa/cuneiform-control-artefacts`, private, revision `e08e1694c337a8298d92c058b416053b04f239f6`, M-04..M-06 only |
| Source of truth | `docs/HF_CUSTODY_REGISTER.md` Verification 5 |
| Governing verdict | `NO_GO_GOVERNING_GATE_UNMET`; unchanged by HF custody |

## Identity

| Key | Value |
|---|---|
| Original intended ID | `Zer0pa/cuneiform-control-artefacts` |
| Actual canonical heavy store | `Architect-Prime/cuneiform-control-artefacts` |
| Visibility | `private`; do not widen for this lane |
| Owner | Zer0pa / Architect-Prime private custody |
| Creation date | Created during Phase 02; later split and mirrored per HF custody register |

## Scope

Admitted families (per `PATH_REWRITE_LEDGER.md` §C):

- `annotated_sign_benchmark_manifest.json`
- `05_annotated_sign_benchmark_manifest.json` (review-pack copy)
- `06_annotated_sign_p8_manifest.json` (diagnostic-only; must carry a
  `diagnostic_only: true` tag in the dataset card)
- `07_annotated_sign_p8_benchmark.json` (diagnostic-only; same tag)
- `08_annotated_sign_p8_1nn_probe.json` (diagnostic-only; same tag)

Forbidden families (never upload):

- pixel-bearing corpora (rights unresolved)
- model weights, checkpoints
- heavy substrate dumps
- any file from path-ledger group (B) `SHARED_METHOD`

## Dataset-Card Required Sections

1. **Governing verdict** — `NO_GO_GOVERNING_GATE_UNMET`; `governing_1nn_accuracy = 0.021916`.
2. **Custody class** — `PUBLISH_WITH_REVIEW`.
3. **Diagnostic-only labelling** — every P6/P7 artefact tagged so a consumer
   cannot read them as gate closure.
4. **Checksum table** — SHA-256 per file, cross-referenced to
   `docs/evidence/ARTEFACT_CHECKSUMS.md`.
5. **Linkback** — URL of this repo and of the failed-gate evidence page.
6. **Licence posture** — code/docs licensing does not grant rights to private
   HF artefacts, derived manifests, model checkpoints, or image-bearing source
   corpora.

## Phase 02 Entry Procedure

1. Compute SHA-256 for each admitted file from a known-good source path.
2. Commit `docs/evidence/ARTEFACT_CHECKSUMS.md` with the pins.
3. Create the HF dataset as **private**.
4. Upload files; verify post-upload SHA-256 matches the pinned value.
5. Populate the dataset card with the six required sections.
6. Record the dataset revision hash in the Phase 02 smoke report.

## Forbidden Under Any Circumstance

- Changing a published checksum after it has been pinned.
- Publishing the dataset to `public` while `NO_GO_GOVERNING_GATE_UNMET` stands.
- Removing the diagnostic-only tag from P6/P7 artefacts.
- Bundling pixel-bearing or rights-constrained sources.
