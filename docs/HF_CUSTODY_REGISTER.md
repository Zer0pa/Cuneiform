# Hugging Face Custody Register — `gnosis-cuneiform`

> **Closeout artefact (2026-04-24).** Required by the closeout brief. Records
> the exact HF custody state that was verifiable under the Zer0pa production
> HF token on 2026-04-24. Append-only: a new verification run appends a new
> section; it does not edit older entries.

## Spelling Convention

The cuneiform lane uses the British/international spelling **`artefact`**
throughout docs and HF dataset IDs. The closeout brief flagged that other
Gnosis workstreams may use the American spelling `artifact`. **For this lane,
the canonical HF repo ID is `<HF_ORG>/cuneiform-control-artefacts`** (with the
`e`). Any `artifact`-spelled references in other workstream docs should be
treated as pointers to this same dataset.

## Consuming GitHub Repo

`Zer0pa/Cuneiform` (INTERNAL, `main`). This repo references the HF dataset by
SHA-256 pin via:

- `docs/evidence/ARTEFACT_CHECKSUMS.md` (pinned SHA-256 per file)
- `artefacts/smoke/manifest_validation_report.json` (in-pod verified SHA-256)
- `artefacts/smoke/hf_upload_verify.json` (post-upload SHA-256 verify)

## Verification 1 — 2026-04-24 03:31 UTC (upload + immediate verify)

| Key | Value |
|---|---|
| Token scope | `Architect-Prime` user, org `Zer0pa` (write) |
| Repo ID | `Zer0pa/cuneiform-control-artefacts` |
| Repo type | `dataset` |
| Visibility | `private` |
| Revision (commit SHA) | `c64e22f671dcce1577233309fd3320258dbd2e09` |
| Last modified | `2026-04-24 03:31:58+00:00` |
| Files | `README.md`, `M-01…M-06_*.json`, `.gitattributes` |
| Post-upload verify | 6/6 SHA-256 match against pins |

Evidence: `artefacts/smoke/hf_upload_verify.json`.

## Verification 2 — 2026-04-24 (closeout re-verify under production token)

Re-run from the shared `<RUNPOD_HOST>` pod using `huggingface_hub 1.11.0`.

| Key | Value |
|---|---|
| Token user | `Architect-Prime` |
| Token org membership | `['Zer0pa']` |
| Repo exists | **Yes** — visible to the production token |
| Current revision | `c64e22f671dcce1577233309fd3320258dbd2e09` (unchanged) |
| Current visibility | `private` (unchanged) |
| Last modified | `2026-04-24 03:31:58+00:00` (unchanged) |
| SHA-256 verify | 6/6 OK against `docs/evidence/ARTEFACT_CHECKSUMS.md` pins |
| All verified | `true` |

## Verification 4 — 2026-04-26 (HF storage split per GNOSIS_HF_STORAGE_EXECUTION_BRIEF_2026-04-26)

Per `GNOSIS_HF_STORAGE_EXECUTION_BRIEF_2026-04-26.md` §1.2 (storage
economics), §3 (Gnosis routing), §4 (thresholds), §7.4 (Cuneiform
guidance). Heavy artefacts moved to canonical `Architect-Prime/*`
store; `Zer0pa/*` reduced to the lightweight discovery surface.

### Split decision (per §4 thresholds)

Three files on Zer0pa exceed the single-file threshold (> 1 MB):

| ID | Bytes | Threshold call |
|---|---:|---|
| M-01 | 9,280,260 | heavy (>1 MB) → AP canonical |
| M-02 | 9,280,260 | heavy (>1 MB; byte-identical to M-01) → AP canonical |
| M-03 | 27,684,873 | heavy (>1 MB; P6 diagnostic) → AP canonical |
| M-04 | 471,305 | lightweight (<1 MB; P6 review) → kept on Zer0pa as backup |
| M-05 | 1,880 | trivial (P7 probe) → kept on Zer0pa as backup |
| M-06 | 4,466 | trivial (review-pack index) → kept on Zer0pa as backup |

Total Zer0pa storage reduction: 46.73 MB → 0.486 MB (≈ 46.25 MB
returned to org private quota).

### `Architect-Prime/cuneiform-control-artefacts` — created

| Key | Value |
|---|---|
| Token user | `Architect-Prime` |
| Token org membership | `['Zer0pa']` |
| Repo created | 2026-04-26 |
| Repo type | `dataset` |
| Visibility | `private` (hard-locked: brief §1.3 — never make AP Gnosis repo public) |
| Initial revision | `03ad7397dc12be58289481ff8a209349c6ed9042` |
| Last modified | `2026-04-26 19:26:39+00:00` |
| Files on AP | `README.md`, `M-01..M-06`, `.gitattributes` (8 files) |
| Total bytes | ~46.7 MB |
| Post-upload SHA-256 verify | 6/6 OK against `docs/evidence/ARTEFACT_CHECKSUMS.md` pins |

### `Zer0pa/cuneiform-control-artefacts` — reduced to lightweight surface

| Key | Value |
|---|---|
| Previous revision | `1d26b9168eb7ac5a765e8a869f03501840d16347` (post HF lane brief card rewrite) |
| New revision | `e08e1694c337a8298d92c058b416053b04f239f6` (post storage split) |
| Last modified | `2026-04-26 19:28:01+00:00` |
| Visibility | `private` (unchanged) |
| Files remaining | `README.md` (lightweight card), `M-04`, `M-05`, `M-06`, `.gitattributes` (5 files) |
| Total bytes | 485,992 (0.486 MB) |
| Files removed | `M-01`, `M-02`, `M-03` (the three >1 MB files) |
| SHA-256 verify (M-04..M-06) | 3/3 OK at new revision |

### Routing model (now in effect for cuneiform lane)

| Use case | Source |
|---|---|
| Quick review / discovery / SHA pin lookup | `Zer0pa/cuneiform-control-artefacts` (lightweight) |
| Re-hash of M-04..M-06 | `Zer0pa/cuneiform-control-artefacts` |
| Re-hash of M-01..M-03 (heavy) | `Architect-Prime/cuneiform-control-artefacts` (canonical) |
| Smoke runner real-manifest replay (full M-01) | `Architect-Prime/cuneiform-control-artefacts` |

### Non-negotiables honoured

- No public licence implication on either side (Gnosis non-negotiable).
- `Architect-Prime/cuneiform-control-artefacts` will not be made public
  (brief §1.3 hard rule).
- No model weights, no pixel data, no operational endpoints uploaded
  anywhere.
- No deletion of pinned scientific provenance — bytes preserved at AP.
- No new naming under deprecated `Cipher` (brief §1.1).

## Verification 3 — 2026-04-26 (HF lane brief execution)

Per `HF_LANE_EXECUTION_BRIEF_2026-04-26.md` (Gnosis family rules, §4.4).
Re-run under the production HF token from local macOS using
`huggingface_hub 1.8.0` (pod offline at execution time).

| Key | Value |
|---|---|
| Token user | `Architect-Prime` |
| Token org membership | `['Zer0pa']` |
| Repo exists | **Yes** — visible to the production token |
| Current revision | `1d26b9168eb7ac5a765e8a869f03501840d16347` (**new**: card rewrite) |
| Previous revision | `c64e22f671dcce1577233309fd3320258dbd2e09` |
| Current visibility | `private` (unchanged) |
| Last modified | `2026-04-26 18:32:34+00:00` |
| SHA-256 verify (manifests M-01..M-06) | 6/6 OK against pinned values (unchanged from V1/V2) |
| All verified | `true` |
| Card change | `README.md` rewritten to HF lane brief §5 template (Gnosis-family posture; no SAL; no public-licence implication; mirrors root `NOTICE.md`); **manifest payloads untouched** |
| Pin commit on GitHub source | `bdca3f8` (`repo: replace interim notices with canonical Phase 1 text`) — recorded in the new card's "Source" section |

### HF lane discovery (executed 2026-04-26)

- `Zer0pa` namespace (datasets, all `private`):
  `cuneiform-control-artefacts` (this repo) plus 14 unrelated lane
  datasets (ZPE-XR, Zer0paShip, glyph-engine, gnosis-indus,
  gnosis-morph-bench (×2), kv-3d, research-brain, knowledge-graph,
  ship-hull-designs, image-codec, imc-benchmark/canonical, taste-restart).
- `Zer0pa` namespace (models): `gnosis-indus-models` (private) — not in
  cuneiform scope.
- `Architect-Prime` namespace cuneiform-related repos: **none found**.
  No drift to clean up.

### HF lane decision (per Gnosis family rules)

| Question | Answer |
|---|---|
| Public/private | **Private.** No change. |
| Migrate from another namespace | **No.** Already canonical. |
| Create new HF repo(s) | **No.** Existing surface is sufficient. |
| Push additional artefacts | **No.** No new manifests admitted by ledger. |
| Card update | **Yes** — done in this verification (rev `1d26b91…`). |
| Architect-Prime cleanup | **N/A.** No drift exists. |

## Files Under Custody (post-2026-04-26 split)

| ID | Filename | SHA-256 (pinned) | Bytes | Rights class | Diagnostic-only? | Hosted on |
|---|---|---|---|---|---|---|
| `M-01` | `M-01_annotated_sign_benchmark_manifest.json` | `e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24` | 9,280,260 | `PUBLISH_WITH_REVIEW` | no | **Architect-Prime** (canonical) |
| `M-02` | `M-02_05_annotated_sign_benchmark_manifest.json` | `e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24` | 9,280,260 | `PUBLISH_WITH_REVIEW` | no (byte-identical to M-01) | **Architect-Prime** (canonical) |
| `M-03` | `M-03_06_annotated_sign_p8_manifest.json` | `05fc8505df0b408d8044d6beb39c96adef53370e81c280a84779c543fd90b574` | 27,684,873 | `PUBLISH_WITH_REVIEW` | **yes — P8/P6** | **Architect-Prime** (canonical) |
| `M-04` | `M-04_07_annotated_sign_p8_benchmark.json` | `5fd933bcf706387c58ac5bccbdd434362901ec1d77f057e532440776005baeba` | 471,305 | `PUBLISH_WITH_REVIEW` | **yes — P6** | both (Zer0pa lightweight + AP canonical) |
| `M-05` | `M-05_08_annotated_sign_p8_1nn_probe.json` | `c896572754d24442c90cce81e750d05e4af4707119ca5b8e7f077ce2879a590a` | 1,880 | `PUBLISH_WITH_REVIEW` | **yes — P7** | both (Zer0pa lightweight + AP canonical) |
| `M-06` | `M-06_09_REVIEW_PACK_MANIFEST.json` | `7163eae78448b73bd924f508575b2d1de1df4b94c6e39e14d669ae85f82a4aa9` | 4,466 | `PUBLISH_WITH_REVIEW` | no | both (Zer0pa lightweight + AP canonical) |

GitHub cross-reference for all six pins: `docs/evidence/ARTEFACT_CHECKSUMS.md`.

## Files Forbidden Under Custody

Never upload:

- any pixel-bearing corpora (rights unresolved);
- any model weights or intermediate checkpoints (`INTERNAL_ONLY`);
- any upstream helper source not admitted by `docs/PATH_REWRITE_LEDGER.md`;
- anything that would downgrade the failed-gate posture in the dataset card.

## Closeout-Brief Discrepancy (resolved)

The central closeout brief (`GNOSIS_REPO_CLOSEOUT_BRIEF_2026-04-24.md`,
"Hugging Face State And Housekeeping") noted that the HF repo
`Zer0pa/cuneiform-control-artefacts` was **not** visible to the reviewer's
token. Under the **production** token (`Architect-Prime`, org `Zer0pa`)
probed here on 2026-04-24, the repo **is** visible, is `private`, and matches
the 6 pinned SHA-256s.

Working hypothesis for the reviewer's negative result:

- Most likely: the reviewer's token snapshot pre-dates repo creation
  (this dataset was created at 2026-04-24 03:31:58 UTC; any reviewer run
  before that timestamp would see `NOT_EXISTS`).
- Alternative: reviewer's token had read-only scope with different org
  membership visibility. Confirmed in this register that the production
  token has both membership and access.

A reviewer can reproduce the positive result by running the exact script in
`docs/EXECUTOR_STATUS_REPORT.md` §"Replay" on the shared pod under a
Zer0pa-org-scoped HF token.

## Open Items For Owner / Legal

- Whether to align lane spellings across Gnosis (`artifact` vs `artefact`)
  before a public release. Default position: keep `artefact` here; update
  cross-lane pointers in whichever lane owns the public index.
- Whether to publish a dataset-card changelog (currently embedded in README).
- Licence ruling for the manifest files themselves (they are **derived**
  from upstream rights-constrained corpora; licence of the derivation is
  not automatically clear).

## Update Protocol

1. Any new verification run appends a new **Verification N** section above;
   it does not edit prior ones.
2. A SHA-256 mismatch opens an **evidence dispute** — never a silent re-pin.
3. Visibility change from `private` requires an owner ruling recorded in
   `RELEASING.md` before it happens.
4. If the revision SHA changes on HF (a new dataset commit), the new
   revision is recorded here **and** re-pinned into the
   `artefacts/smoke/hf_upload_verify.json` of that run — old revisions stay
   as history.
