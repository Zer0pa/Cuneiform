# Gnosis Cuneiform

> Negative-control/control-pack lane. Website-sync posture: staged/WIP, useful as a no-go truth surface, not a cuneiform recovery claim.

## What This Is

`gnosis-cuneiform` is a negative-control/control-pack repo inside the Gnosis methods portfolio. It preserves the cuneiform benchmark/control artifact chain, the failed governing gate, the source boundary, and the rerun contract. It is **not** a product release, decipherment claim, substrate-identification claim, or scientific success claim.

Headline metric: `pytest -q` passes with **3 tests**, real-manifest smoke holds **5/5 cross-field invariants**, and **6/6 upstream manifest SHA-256 pins** are verified in private HF custody. The sovereign scientific truth remains `NO_GO_GOVERNING_GATE_UNMET` at `governing_1nn_accuracy = 0.021916`.

Honest blocker: the failed governing gate remains failed. The smoke surface proves custody and manifest shape; it does not repair the no-go result. Image-bearing sources and some upstream datasets remain rights-constrained or fetch-only.

| Field | Value |
|-------|-------|
| Architecture | NEGATIVE_CONTROL_STREAM |
| Encoding | CUNEIFORM_MANIFEST_SMOKE_V1 |

## Key Metrics

| Metric | Value | Baseline |
|---|---:|---|
| PYTEST_PASS | 3 passed | pytest |
| MANIFEST_INVARIANTS | 5/5 | smoke |
| HF_SHA_VERIFY | 6/6 | custody |
| GOVERNING_1NN_ACCURACY | 0.021916 | no-go |

> Source: `tests/test_smoke_runner.py`, `artefacts/smoke/manifest_validation_report.json`, `artefacts/smoke/hf_upload_verify.json`, `docs/evidence/ARTEFACT_CHECKSUMS.md`, and `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`.

## What We Prove

- The cuneiform benchmark/control artifact chain is real and pinned by SHA-256.
- The inherited governing gate failed and remains failed: P5 closed `NO_GO_GOVERNING_GATE_UNMET` at `governing_1nn_accuracy = 0.021916`.
- `SMOKE-01-MANIFEST-VALIDATION` passes against the pinned upstream manifest with all 5 cross-field invariants holding and 0 schema errors.
- The smoke surface is stdlib-only, third-party-dependency-free, and reproducible on any Python >= 3.8 host.

## What We Don't Claim

- We do not claim the failed governing gate is repaired.
- We do not claim cuneiform decipherment, substrate identification, or positive scientific recovery on this corpus.
- We do not claim flagship status or cross-domain superiority.
- We do not claim cleared image rights or rights-cleared corpus redistribution.

## Commercial Readiness

| Field | Value |
|-------|-------|
| Verdict | STAGED |
| Commit SHA | c56dba6f2694 |
| Source | docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md |

`STAGED` means the control-pack truth surface is useful and reproducible. It does not mean the no-go result is repaired, and it does not clear image-bearing data rights.

## Tests and Verification

| Code | Check | Verdict |
|---|---|---|
| V_01 | `pytest -q` | PASS |
| V_02 | real-manifest smoke validation | PASS |
| V_03 | HF SHA-256 custody verification | PASS |
| V_04 | Ops-Gates coupling/operational-leak checks | PASS |

## Proof Anchors

| Path | State |
|---|---|
| `SOVEREIGN_PRD.md` | VERIFIED |
| `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` | VERIFIED |
| `docs/evidence/CUNEIFORM_CONTROL_RESULTS.md` | VERIFIED |
| `docs/evidence/ARTEFACT_CHECKSUMS.md` | VERIFIED |
| `artefacts/smoke/manifest_validation_report.json` | VERIFIED |
| `artefacts/smoke/hf_upload_verify.json` | VERIFIED |
| `docs/HF_CUSTODY_REGISTER.md` | VERIFIED |
| `docs/PATH_REWRITE_LEDGER.md` | VERIFIED |
| `AUDITOR_PLAYBOOK.md` | VERIFIED |

## Repo Shape

| Field | Value |
|---|---|
| Package | `cuneiform_control` |
| Source | `code/cuneiform_control/` |
| Tests | `tests/` |
| Evidence | `docs/evidence/`, `artefacts/smoke/`, `.gpd/` |
| Custody | `docs/HF_CUSTODY_REGISTER.md` |
| Legal/Data | `LICENSE`, `NOTICE`, `DATA_POLICY.md`, `docs/LEGAL_BOUNDARIES.md` |

## Quick Start

```bash
git clone https://github.com/Zer0pa/Cuneiform.git
cd Cuneiform
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e . pytest
pytest -q
cuneiform-smoke --help
```

A `PASS` verdict from a real-manifest replay proves manifest custody and shape against the pinned SHA-256. It does **not** repair `NO_GO_GOVERNING_GATE_UNMET`.

## Upcoming Workstreams

> This section captures the active lane priorities — what the next agent or contributor picks up, and what investors should expect. Cadence is continuous, not milestoned.

- **Smoke surface tightening** — Active Engineering. Preserve the stdlib-only smoke surface while adding schema variants only when new manifests justify them.
- **P5 governing-gate repair** — Operations / External Dependency. Owned by a separate workstream; this lane preserves the negative result.
- **Image-bearing rights clearance** — Operations / External Dependency. No pixel-bearing corpus redistribution until upstream rights review completes.
- **Gate-repair reassessment** — Zero-Base Scientific Thinking — GPD Research and Planning Pending. Open a new milestone only if separate evidence warrants revisiting the no-go verdict.

## Licensing

This repository is part of the Zer0pa Gnosis Portfolio.

**Code** in this repository is licensed under the Apache License 2.0. See `LICENSE`. SPDX identifier: `Apache-2.0`.

**Documentation, reports, and written materials** are licensed under Creative Commons Attribution 4.0 International. SPDX identifier: `CC-BY-4.0`.

**Data, fixtures, corpora, image-bearing cultural-heritage assets, private HF artifacts, model weights, endpoint logs, and operational transcripts** are not licensed by the code or documentation licenses. Their boundary is governed by `DATA_POLICY.md`, artifact-specific notices, and any future owner admission record.

**Trademarks** - "Gnosis", "Zer0pa Gnosis", and distinctive sub-marks are trademarks of Zer0pa. Apache-2.0 and CC-BY-4.0 do not grant trademark rights. See `TRADEMARKS.md`.

Public visibility is a separate repository-setting action. These license files define the open code/docs posture; they do not publish rights-gated data.


## Traditional-Knowledge Acknowledgment

This repository works with material in cuneiform-bearing writing systems (Sumerian, Akkadian, Babylonian, and related). Zer0pa claims no proprietary right over cuneiform, its scripts, or the archaeological record.

This repository preserves a negative-control result as a first-class output; it does not claim a definitive decipherment of cuneiform or related scripts.

Good-faith inquiries from identified communities, governmental antiquity authorities, or institutional bodies may be sent to architects@zer0pa.ai.
