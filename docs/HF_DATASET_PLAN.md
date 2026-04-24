# Hugging Face Dataset Plan — `Zer0pa/cuneiform-control-artefacts`

> **Phase 01 staging artefact.** This file names the HF dataset and its custody
> rules. It does **not** create or upload the dataset — that is a Phase 02 act
> gated on checksum pins and provenance review.

## Identity

| Key | Value |
|---|---|
| Intended ID | `Zer0pa/cuneiform-control-artefacts` |
| Visibility | `private` (default; can be downgraded to wider access only after the governing gate changes on evidence, which this pack cannot deliver) |
| Owner | `Zer0pa HF Storage` |
| Creation date | **NOT YET CREATED** — creation is a Phase 02 act |

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
6. **Licence posture** — `OWNER_DEFERRED`; gating public reuse.

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
