# Artefact Checksum Pins

> **Phase 02 artefact.** Pinned 2026-04-24 from upstream pod (endpoint held in
> Zer0pa's internal operations registry) paths under `<MONOREPO>/`. These pins
> are append-only. A pin may **never** be silently changed; if a checksum
> drifts, open a blocker and record the divergence as evidence.

## Pinning Procedure

1. Source paths are on the shared pod under `<MONOREPO>/` (see closeout brief
   for the canonical operational registry).
2. SHA-256 computed via `sha256sum` on the pod.
3. Files are not vendored into git; they are routed to HF (private) and
   re-verified post-upload. **Two-tier hosting (post-2026-04-26 split):**
   - `Architect-Prime/cuneiform-control-artefacts` (canonical heavy store):
     all 6 manifests M-01..M-06 (private; never made public).
   - `Zer0pa/cuneiform-control-artefacts` (lightweight discovery surface):
     M-04, M-05, M-06 only (M-01..M-03 removed; they are >1 MB and live
     canonically on Architect-Prime per
     `GNOSIS_HF_STORAGE_EXECUTION_BRIEF_2026-04-26.md` §4 thresholds).
   See `docs/HF_CUSTODY_REGISTER.md` for the token-verified HF state and
   the full split rationale.

## Pinned Manifests (admitted under `DATA_POLICY` `PUBLISH_WITH_REVIEW`)

| ID | SHA-256 | Bytes | Upstream path | Diagnostic-only? | HF host |
|---|---|---|---|---|---|
| `M-01` | `e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24` | 9,280,260 | `workspace/artifacts/cuneiform/annotated_sign_benchmark_manifest.json` | no — primary benchmark manifest (P5 input substrate) | AP canonical |
| `M-02` | `e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24` | 9,280,260 | `workspace/share/science_engineering_review_2026-04-10/05_annotated_sign_benchmark_manifest.json` | no — review-pack copy of `M-01` (byte-identical) | AP canonical |
| `M-03` | `05fc8505df0b408d8044d6beb39c96adef53370e81c280a84779c543fd90b574` | 27,684,873 | `workspace/share/science_engineering_review_2026-04-10/06_annotated_sign_p8_manifest.json` | yes — P8 / P6 diagnostic | AP canonical |
| `M-04` | `5fd933bcf706387c58ac5bccbdd434362901ec1d77f057e532440776005baeba` | 471,305 | `workspace/share/science_engineering_review_2026-04-10/07_annotated_sign_p8_benchmark.json` | yes — P6 diagnostic benchmark output | both |
| `M-05` | `c896572754d24442c90cce81e750d05e4af4707119ca5b8e7f077ce2879a590a` | 1,880 | `workspace/share/science_engineering_review_2026-04-10/08_annotated_sign_p8_1nn_probe.json` | yes — P7 diagnostic probe output | both |
| `M-06` | `7163eae78448b73bd924f508575b2d1de1df4b94c6e39e14d669ae85f82a4aa9` | 4,466 | `workspace/share/science_engineering_review_2026-04-10/09_REVIEW_PACK_MANIFEST.json` | no — review-pack index | both |

`AP canonical` = `Architect-Prime/cuneiform-control-artefacts` (private,
revision `03ad7397dc12be58289481ff8a209349c6ed9042`).
`both` = canonical on AP **and** lightweight backup on
`Zer0pa/cuneiform-control-artefacts` (private, revision
`e08e1694c337a8298d92c058b416053b04f239f6`).

## Pinned Source Scripts (referenced; extraction deferred per ledger)

| ID | SHA-256 | Bytes | Upstream path | Status |
|---|---|---|---|---|
| `S-01` | `815bcc885ed75e4dd37b5d2b3f7e7e50c7da428d3e9085f9bff86d1ca7a98ff5` | 19,033 | `scripts/cuneiform/annotated_sign_benchmark_common.py` | admitted; extraction Phase 02+ |
| `S-02` | `d032f0ec1a1e4e9fe8a8624a626df836bf8fe94251b95f1cbfa8fbf446d57d4b` | 3,999 | `scripts/cuneiform/benchmark_annotated_sign_tokenizer.py` | admitted; extraction Phase 02+ |
| `S-03` | `1f1b0d0f3440d2467647e049abda95472ab0696afd5d4d7d372887e1769ece17` | 3,855 | `scripts/cuneiform/probe_annotated_sign_tokenizer_1nn.py` | admitted; extraction deferred — produces failed governing metric |
| `S-04` | `170948f5dbb577daac387f8f666b84100e13729779255af29a0a3c3110b3a88e` | 10,682 | `scripts/cuneiform/benchmark_annotated_sign_p8.py` | admitted; **diagnostic-only** |
| `S-05` | `b7d3276dad4a7c0204ebbc5705add1c8d2b608385ff5922b287f8fb6c89c2392` | 7,669 | `scripts/cuneiform/probe_annotated_sign_p8_1nn.py` | admitted; **diagnostic-only** |
| `S-06` | `UPSTREAM_NOT_PRESENT` | — | `scripts/cuneiform/revert_phase2_common.py` | **NOT FOUND** on upstream pod (2026-04-24); see Path-Rewrite Ledger amendment |

## Manifest Invariants (extracted from `M-01` for smoke checks)

| Invariant | Expected | Source field |
|---|---|---|
| `schema_version` | `1` | top level |
| `len(sign_records)` | `7462` | `summary.available_sign_record_count` |
| `len(tablets)` | `72` | `summary.downloaded_tablet_count` |
| `len(missing_tablets_preview)` | `9` | `summary.missing_tablet_count` |
| `summary.annotated_tablet_count` | `81` | derived (= 72 downloaded + 9 missing) |
| `summary.available_sign_record_count` | `7462` | independent count |
| `summary.train_label_count` | `256` | independent count |
| `summary.test_label_count` | `219` | independent count |
| `summary.overlap_label_count` | `199` | independent count |

## Forbidden Mutations

- A pinned SHA-256 may not be edited. New evidence requires a new ID.
- A diagnostic-only flag may not be removed.
- An `UPSTREAM_NOT_PRESENT` entry may not be quietly resolved by inventing a
  path; resolution requires a new pod-verified path or removal from scope.
