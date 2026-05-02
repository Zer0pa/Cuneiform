# Gnosis Cuneiform

## What This Is

Gnosis negative-control control pack preserving cuneiform benchmark custody, failed-gate evidence, source/data boundaries, and a stdlib-only manifest-validation smoke.

`gnosis-cuneiform` is a Method Mechanics lane in the Gnosis portfolio. It keeps the cuneiform benchmark/control artefact chain inspectable without promoting the lane as a product, a decipherment result, or a repaired scientific gate.

The public posture is control-only: useful for audit and falsification, blocked for promotion, and explicit about Traditional-Knowledge, source-boundary, data-rights, and public-audit limits.

## Method Mechanics

| Mechanic | Current implementation | Authority |
|---|---|---|
| Control-pack role | Preserves the cuneiform benchmark truth surface as `MODULE_ONLY_CONTROL_PACK`; no sovereign product promotion. | `SOVEREIGN_PRD.md` |
| Governing falsification gate | Keeps `NO_GO_GOVERNING_GATE_UNMET` at `governing_1nn_accuracy = 0.021916`; P6/P7 diagnostics remain diagnostic-only. | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` |
| Source boundary | Admits only cuneiform-specific control/rerun material; shared geometry, transport, and generic evaluation kernels stay out of this repo. | `SOURCE_BOUNDARY.md` |
| Smoke target | Validates manifest custody and shape only: checksum, schema, five cross-field invariants, and preserved failed-gate fields. | `artefacts/smoke/manifest_validation_report.json` |
| Public audit boundary | Allows reviewers to verify the visible scaffold, pins, smoke report, and failed-gate posture; does not expose private HF bytes or rights-limited corpora. | `PUBLIC_AUDIT_LIMITS.md` |

## Key Metrics

| Metric | Value | Evidence |
|---|---|---|
| Governing gate | `NO_GO_GOVERNING_GATE_UNMET`; `governing_1nn_accuracy = 0.021916` | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` |
| Manifest smoke | `PASS`; 5/5 invariants OK, 0 schema errors, observed SHA matches pin | `artefacts/smoke/manifest_validation_report.json` |
| Hermetic tests | `pytest -q` -> 3 self-tests; smoke runner is stdlib-only with zero runtime dependencies | `tests/test_smoke_runner.py`, `pyproject.toml` |
| HF custody | 6/6 lane-pinned manifests verified against SHA-256 pins; AP heavy store remains private | `docs/HF_CUSTODY_REGISTER.md`, `artefacts/smoke/hf_upload_verify.json` |

## Repo Identity

| Field | Value |
|---|---|
| Identifier | `gnosis-cuneiform` |
| Repository | `https://github.com/Zer0pa/Cuneiform` |
| Portfolio / domain | Gnosis methodology; cuneiform negative-control/control-pack lane |
| Visibility | `PUBLIC` |
| Default branch | `main` |
| Authority source | `SOVEREIGN_PRD.md`; `.gpd/STATE.md`; `.gpd/DECISIONS.md` |
| License | Code: `Apache-2.0`; documentation/reports/written materials: `CC-BY-4.0`; data by rights class in `DATA_POLICY.md` |
| Last verified | 2026-05-02 GitHub main alignment pass |

## Readiness

| Field | Value |
|---|---|
| Verdict | `BLOCKED` |
| Posture | `HOLD_CONTROL_ONLY`; negative-control preservation |
| Checks | Hermetic tests pass; manifest smoke passes; HF custody pins verify; governing gate remains failed |
| Anchors | 6 display anchors |
| Authority | `SOVEREIGN_PRD.md`; `PUBLIC_AUDIT_LIMITS.md`; `.gpd/STATE.md` |
| Public surface | Lab window only; not a product release or scientific flagship |

### Honest Blocker

The inherited governing gate `NO_GO_GOVERNING_GATE_UNMET` remains failed at `governing_1nn_accuracy = 0.021916`. The smoke surface proves custody and shape only; it cannot repair the gate, clear image/corpus rights, or authorize public-release claims.

## What We Prove

- The cuneiform benchmark/control artefact chain is real and pinned. Six upstream manifests are recorded by SHA-256 in `docs/evidence/ARTEFACT_CHECKSUMS.md` and held under private HF custody recorded in `docs/HF_CUSTODY_REGISTER.md`.
- The inherited governing gate failed and remains failed: P5 closed `NO_GO_GOVERNING_GATE_UNMET` at `governing_1nn_accuracy = 0.021916`; P6 (`0.038176`) and P7 (`0.051826`) diagnostics are never promoted to gate closure.
- `SMOKE-01-MANIFEST-VALIDATION` runs and passes against the pinned upstream manifest with all 5 cross-field invariants holding and 0 schema errors.
- The smoke surface is stdlib-only, third-party-dependency-free, and reproducible on any Python >= 3.8 host without provisioning.

## What We Don't Claim

- We do not claim the failed governing gate is repaired. The smoke is custody-only by construction; it cannot move the gate.
- We do not claim cuneiform decipherment, substrate identification, or any positive scientific recovery on this corpus.
- We do not claim public-release readiness, flagship status, commercial readiness, or cross-domain superiority.
- We do not claim cleared image rights, rights-cleared corpus redistribution, or permission to expose private HF artefact bytes.
- We do not claim proprietary rights over cuneiform, its scripts, or the archaeological record.
- We do not claim that shared geometry, transport, or generic evaluation kernels belong in this repo.

## Verification Status

| Code | Check | Verdict |
|---|---|---|
| V-01 | Hermetic self-test: `pytest -q` returns 3 passing tests against bundled fixtures. | `PASS` |
| V-02 | Real-manifest smoke: checksum, schema, and 5/5 cross-field invariants pass. | `PASS` |
| V-03 | HF post-upload SHA verify: 6/6 admitted manifest pins match observed hashes. | `PASS` |
| V-04 | HF custody register: AP heavy store and Zer0pa lightweight surface remain private and token-verified. | `PASS` |
| V-05 | Operational-leak scan in CI blocks concrete IPs, raw SSH endpoints, local home paths, retired monorepo paths, and pod IDs. | `PASS` |
| V-06 | Governing science gate remains failed and cannot be repaired by this smoke. | `BLOCKED` |
| V-07 | Public redistribution of image-bearing corpora and some derived data remains rights-constrained. | `BLOCKED` |

## Proof Anchors

| Path | State |
|---|---|
| `SOVEREIGN_PRD.md` | VERIFIED |
| `SOURCE_BOUNDARY.md` | VERIFIED |
| `DATA_POLICY.md` | VERIFIED |
| `PUBLIC_AUDIT_LIMITS.md` | VERIFIED |
| `.gpd/DECISIONS.md` | VERIFIED |
| `artefacts/smoke/manifest_validation_report.json` | VERIFIED |

## Repo Shape

| Path | What Lives Here |
|---|---|
| `README.md`, `SOVEREIGN_PRD.md`, `AUDITOR_PLAYBOOK.md`, `AGENTS.md` | Front door, sovereign brief, reviewer entry, agent brief. |
| `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `GOVERNANCE.md`, `RELEASING.md`, `PUBLIC_AUDIT_LIMITS.md` | Source, data, governance, release, and public-audit boundaries. |
| `code/cuneiform_control/` | Stdlib-only smoke runner and JSON Schema. |
| `tests/` | Hermetic pytest-discovered self-tests for pass, invariant-fail, and checksum-fail paths. |
| `pyproject.toml` | Package manifest (`Private :: Do Not Upload`; zero runtime deps). |
| `artefacts/smoke/` | Deterministic smoke report and HF-upload-verify report. |
| `docs/evidence/` | Failed-gate evidence, control results, and SHA-256 pin register. |
| `docs/` | Architecture, ledgers, smoke target, HF custody, rerun guide, executor status, and support docs. |
| `docs/migration/` | Original migration-package brief, authority, source inventory, and handover history. |
| `.gpd/` | GPD state, decisions, roadmap, requirements, conventions, and four closed phases. |
| `.github/workflows/ci.yml` | Minimal CI: install, pytest, smoke help, operational-leak scan, clean-tree check. |
| `_internal/` | Agent-orchestration scaffolding; not reader-facing. |

## Traditional-Knowledge Acknowledgment

This repository works with material in cuneiform-bearing writing systems (Sumerian, Akkadian, Babylonian, and related). Zer0pa claims no proprietary right over cuneiform, its scripts, or the archaeological record.

This repository preserves a negative-control result as a first-class output; it does not claim a definitive decipherment of cuneiform or related scripts.

Good-faith inquiries from identified communities, governmental antiquity authorities, or institutional bodies may be sent to architects@zer0pa.ai.

## Data And Public Audit Boundaries

The data boundary is evidence, not boilerplate:

- Staged docs, PRD, handover surfaces, and derived benchmark summaries can be published as repo-local written material.
- Benchmark manifests and derived JSON outputs are `PUBLISH_WITH_REVIEW`; each file still needs provenance review before any remote promotion.
- Image previews and raw image-bearing corpora are `FETCH_EXTERNALLY_OR_INTERNAL_ONLY` until rights posture is cleared.
- Model weights and intermediate experimental checkpoints are `INTERNAL_ONLY` and are not needed for the current control-pack truth surface.
- A public audit can verify the source tree, path-rewrite ledger, checksum pins, smoke runner, smoke report, failed-gate posture, and docs coherence; it cannot verify private HF artefact bytes without access or infer private results from public prose.

## Licensing

This repository is part of the Zer0pa Gnosis Portfolio.

**Code** in this repository is licensed under the Apache License 2.0. See `LICENSE` for the full text. SPDX identifier: `Apache-2.0`.

**Documentation, reports, and written materials** are licensed under Creative Commons Attribution 4.0 International. SPDX identifier: `CC-BY-4.0`. Canonical terms: <https://creativecommons.org/licenses/by/4.0/>.

**Data and fixtures** are handled per dataset and artifact family. See `DATA_POLICY.md` for this repository's data boundary. The code license does not license raw corpora, image-bearing cultural-heritage assets, private HF artifacts, model weights, endpoint logs, or operational transcripts.

**Trademarks** - "Gnosis", "Zer0pa Gnosis", and distinctive sub-marks are trademarks of Zer0pa. Apache-2.0 and CC-BY-4.0 do not grant trademark rights. See `TRADEMARKS.md`.

Public visibility is a separate repository-setting action. The license files in this repo define the intended open-source/open-documentation terms for released Gnosis code and written materials; they do not publish rights-gated data.

## Quick Start

Verified end-to-end on 2026-04-25. Commands run from a fresh clone.

```bash
# 1. Install the smoke surface (zero third-party runtime deps; pytest pulled in for tests)
python3 -m venv /tmp/cuneiform-control
source /tmp/cuneiform-control/bin/activate
python -m pip install --upgrade pip
python -m pip install -e . pytest

# 2. Hermetic self-test against bundled fixtures (3 cases, < 1 second)
pytest -q

# 3. Confirm the console entry point works
cuneiform-smoke --help

# 4. Operational-leak scan: runs in CI; reproduce locally by re-running the
#    `Operational-leak scan` step from `.github/workflows/ci.yml`.

# 5. Real-manifest replay (only with a locally-held pinned manifest copy):
cuneiform-smoke \
  --manifest /path/to/annotated_sign_benchmark_manifest.json \
  --schema   code/cuneiform_control/schemas/benchmark_manifest.schema.json \
  --checksum e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24 \
  --manifest-label "<MONOREPO>/workspace/artifacts/cuneiform/annotated_sign_benchmark_manifest.json" \
  --report /tmp/replay_report.json
```

A `PASS` verdict from step 5 proves manifest custody and shape against the pinned SHA-256. It does not repair `NO_GO_GOVERNING_GATE_UNMET`.

## Current Gaps

- Full upstream extraction of cuneiform helper modules (`benchmark_common.py`, `bench_tokenizer.py`, `probe_1nn.py`, P6/P7 diagnostics) remains deferred per `docs/PATH_REWRITE_LEDGER.md`. The smoke is custody-only, not a full rerun.
- `revert_phase2_common.py` is `UPSTREAM_NOT_PRESENT` (`S-06`); it is flagged in the checksum register, not hidden or silently resolved.
- Image-bearing sources and some upstream datasets remain rights-constrained or fetch-only; pixel-bearing data is never vendored.
- `NO_GO_GOVERNING_GATE_UNMET` remains the sovereign scientific truth. Repairing it is out of scope for this lane and is external work for a separate workstream, likely `gnosis-glyph-engine` or `gnosis-falsification-harness`.

## Upcoming Workstreams

### Active Engineering

- Smoke surface tightening if new schema variants are contributed. Preserve the stdlib-only constraint.

### Research-Deferred - Investigation Underway

- None currently. If upstream changes substrate-discrimination methodology, revisit whether P6/P7 diagnostics graduate from diagnostic-only to gate candidates.

### Operations / External Dependency

- P5 governing-gate repair is owned by a separate workstream. This lane preserves the negative result; it does not initiate gate repair.
- Rights clearance for image-bearing corpus redistribution remains unresolved; no action here until upstream rights review completes.

### Zero-Base Scientific Thinking - GPD Research and Planning Pending

- None currently scheduled. A new milestone in this lane opens only if a separate workstream produces gate-repair evidence that warrants revisiting the governing verdict.
