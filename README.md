# Gnosis Cuneiform

> This is a live window into the Zer0pa lab. None of the work in this repo is
> a product release, decipherment claim, or scientific success claim. This lane
> is useful as a negative-control/control-pack surface because the failed gate
> is preserved rather than hidden. Always read the smoke `PASS` together with
> the sovereign blocker: `NO_GO_GOVERNING_GATE_UNMET`.

## Licensing

This repository is part of the Zer0pa Gnosis Portfolio.

**Code** in this repository is licensed under the Apache License 2.0. See
`LICENSE` for the full text. SPDX identifier: `Apache-2.0`.

**Documentation, reports, and written materials** are licensed under Creative
Commons Attribution 4.0 International. SPDX identifier: `CC-BY-4.0`. Canonical
terms: <https://creativecommons.org/licenses/by/4.0/>.

**Data and fixtures** are handled per dataset and artifact family. See
`DATA_POLICY.md` for this repository's data boundary. The code license does not
license raw corpora, image-bearing cultural-heritage assets, private HF
artifacts, model weights, endpoint logs, or operational transcripts.

**Trademarks** - "Gnosis", "Zer0pa Gnosis", and distinctive sub-marks are
trademarks of Zer0pa. Apache-2.0 and CC-BY-4.0 do not grant trademark rights.
See `TRADEMARKS.md`.

Public visibility is a separate repository-setting action. The license files in
this repo define the intended open-source/open-documentation terms for released
Gnosis code and written materials; they do not publish rights-gated data.


## Traditional-Knowledge Acknowledgment

This repository works with material in cuneiform-bearing writing systems
(Sumerian, Akkadian, Babylonian, and related). Zer0pa claims no proprietary
right over cuneiform, its scripts, or the archaeological record.

This repository preserves a negative-control result as a first-class output; it
does not claim a definitive decipherment of cuneiform or related scripts.

Good-faith inquiries from identified communities, governmental antiquity
authorities, or institutional bodies may be sent to architects@zer0pa.ai.

## What This Is

`gnosis-cuneiform` is a **negative-control / control-pack repository** inside
the Gnosis methods portfolio. It preserves the cuneiform benchmark/control
artefact chain, the failed governing gate, the source boundary, and the rerun
contract without pretending the lane is a public product or a successful
scientific flagship. It ships a stdlib-only **manifest-validation smoke
surface** so the custody and shape of pinned inherited artefacts are
mechanically checkable from a fresh checkout.

**Headline metric:** `pytest -q` → **3 passed in 0.04s**; 5/5 cross-field
invariants hold on real-manifest smoke (`artefacts/smoke/manifest_validation_report.json`);
6/6 SHA-256 pinned upstream manifest custody verified against
`Architect-Prime/cuneiform-control-artefacts` (token-verified 2026-04-27,
`docs/HF_CUSTODY_REGISTER.md` Verification 5). CI also consumes the internal
`gnosis-ops-gates` coupling audit so operational-leak hygiene is checked by
the portfolio gate bundle, not only by repo-local prose.

**Honest blocker:** The inherited governing gate `NO_GO_GOVERNING_GATE_UNMET`
failed at `governing_1nn_accuracy = 0.021916` and remains failed. This lane
preserves the negative result as a first-class output; repairing the gate is
out of scope for this lane (see `## Upcoming Workstreams`).

## What We Prove

- The cuneiform benchmark/control artefact chain is real and pinned. Six
  upstream manifests are recorded by SHA-256 in
  `docs/evidence/ARTEFACT_CHECKSUMS.md` and held under HF custody at a pinned
  revision (`docs/HF_CUSTODY_REGISTER.md`).
- The inherited governing gate **failed and remains failed**: P5 closed
  `NO_GO_GOVERNING_GATE_UNMET` at `governing_1nn_accuracy = 0.021916`. P6
  (`0.038176`) and P7 (`0.051826`) diagnostics are diagnostic-only and never
  promoted to gate closure.
- `SMOKE-01-MANIFEST-VALIDATION` runs and passes against the pinned upstream
  manifest with all 5 cross-field invariants holding and 0 schema errors. See
  `artefacts/smoke/manifest_validation_report.json`.
- The smoke surface is stdlib-only, third-party-dependency-free, and
  reproducible on any Python ≥ 3.8 host without provisioning.

## What We Don't Claim

- We do not claim the failed governing gate is repaired. The smoke is
  custody-only by construction; it cannot move the gate.
- We do not claim cuneiform decipherment, substrate identification, or any
  positive scientific recovery on this corpus.
- We do not claim public-release readiness, flagship status, or
  cross-domain superiority.
- We do not claim cleared image rights or rights-cleared corpus
  redistribution.

## Tests and Verification

| Surface | Result | Source |
|---|---|---|
| Hermetic self-test | `pytest -q` → **3 passed** in 0.04s | `tests/test_smoke_runner.py` |
| Real-manifest smoke (pod, scrubbed label) | verdict `PASS`, observed SHA matches pinned `e4d85a…3daa24`, 5/5 invariants OK, 0 schema errors | `artefacts/smoke/manifest_validation_report.json` |
| HF post-upload SHA verify | 6/6 OK against pinned values | `artefacts/smoke/hf_upload_verify.json` |
| HF custody (token-verified, latest 2026-04-27) | canonical heavy store on `Architect-Prime/cuneiform-control-artefacts` (private, rev `3ed3f0d4…`, 519 MB total: 6 manifests + orchestrator-added workspace tarballs + tokenizer checkpoints); 6/6 lane SHA + 1 round-trip orchestrator-added SHA verified | `docs/HF_CUSTODY_REGISTER.md` Verification 5 |
| Local Mac inventory (2026-04-27) | 1.4 MB tree; 82 git-tracked + 0 local-only value-bearing files; lane is mac-loss recoverable | `docs/HF_CUSTODY_REGISTER.md` Verification 5 |
| Operational-leak scan | 0 hits for forbidden operational patterns (concrete RunPod IPs, raw SSH endpoints, local home paths, retired monorepo paths, pod IDs) | `Operational-leak scan` step in `.github/workflows/ci.yml` |
| Ops-Gates coupling audit | internal `Gnosis-Ops-Gates` `coupling_audit.py` pinned at `54ed0a7`; scans `code tests` without fetching HF/private artefacts | `.github/workflows/ci.yml` |
| GitHub Actions | minimal repo CI on `main` (this commit) | `.github/workflows/ci.yml` |

## Commercial Readiness

| Field | Value |
|---|---|
| **Verdict** | `STAGED` |
| **Posture** | `negative_control_preservation` |

This lane is website-syncable only as a negative-control/control-pack surface,
not as a product release or proof of cuneiform recovery. The negative result
(`NO_GO_GOVERNING_GATE_UNMET`) is a first-class scientific output. Commercial
readiness in the traditional sense is not the goal of this lane.

## Proof Anchors

| Need | File |
|---|---|
| Reviewer landing page | `docs/EXECUTOR_STATUS_REPORT.md` |
| Sovereign brief | `SOVEREIGN_PRD.md` |
| Failed-gate evidence | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` |
| Control-results summary | `docs/evidence/CUNEIFORM_CONTROL_RESULTS.md` |
| Pinned SHA-256 register | `docs/evidence/ARTEFACT_CHECKSUMS.md` |
| Smoke validation report | `artefacts/smoke/manifest_validation_report.json` |
| HF upload verify | `artefacts/smoke/hf_upload_verify.json` |
| HF custody register | `docs/HF_CUSTODY_REGISTER.md` |
| Path-rewrite ledger | `docs/PATH_REWRITE_LEDGER.md` |
| Smoke target spec | `docs/MINIMAL_SMOKE_TARGET.md` |
| Architecture / truth map | `docs/ARCHITECTURE.md` |
| Auditor playbook | `AUDITOR_PLAYBOOK.md` |
| Public audit limits | `PUBLIC_AUDIT_LIMITS.md` |
| Current state | `.gpd/STATE.md` |

## Repo Shape

| Path | What Lives Here |
|---|---|
| `NOTICE` | Apache-2.0 code license plus CC-BY-4.0 documentation posture. |
| `README.md`, `SOVEREIGN_PRD.md`, `AUDITOR_PLAYBOOK.md`, `AGENTS.md` | Front door, sovereign brief, reviewer entry, agent brief. |
| `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `GOVERNANCE.md`, `RELEASING.md`, `PUBLIC_AUDIT_LIMITS.md` | Policy surfaces. |
| `code/cuneiform_control/` | Stdlib-only smoke runner + JSON Schema. |
| `tests/` | Hermetic pytest-discovered self-test (3 cases). |
| `pyproject.toml` | Package manifest (`Private :: Do Not Upload`; zero runtime deps). |
| `artefacts/smoke/` | Deterministic smoke and HF-upload-verify reports. |
| `docs/` | Architecture, ledgers, smoke spec, HF custody, rerun guide, executor status. |
| `docs/evidence/` | Failed-gate evidence, control results, SHA-256 pin register. |
| `docs/migration/` | Original migration-package brief, authority, source inventory, handover (preserved as transfer history). |
| `.gpd/` | GPD phase pack: project, requirements, roadmap, state, four closed phases (00–03). |
| `.github/workflows/ci.yml` | Minimal repo CI: install + pytest + smoke help + Ops-Gates coupling audit + operational-leak scan. |
| `_internal/` | Agent-orchestration scaffolding (AUTONOMOUS_EXECUTION_POLICY, GPD_BOOTSTRAP_GUIDE, STARTUP_PROMPT, TEMPLATE_USAGE, WORKSTREAM_GPD_INIT_CHECKLIST, MIGRATION_PLAN, TODO). Not reader-facing. |

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

# 4. Operational-leak scan — runs in CI; reproduce locally by re-running the
#    `Operational-leak scan` step from `.github/workflows/ci.yml`. No concrete
#    IPs, raw SSH endpoints, local home paths, retired monorepo paths, or
#    pod IDs are permitted in tracked files (the workflow itself is excluded
#    because it legitimately defines those patterns).

# 5. Real-manifest replay (only with a locally-held pinned manifest copy):
cuneiform-smoke \
  --manifest /path/to/annotated_sign_benchmark_manifest.json \
  --schema   code/cuneiform_control/schemas/benchmark_manifest.schema.json \
  --checksum e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24 \
  --manifest-label "<MONOREPO>/workspace/artifacts/cuneiform/annotated_sign_benchmark_manifest.json" \
  --report /tmp/replay_report.json
```

A `PASS` verdict from step 5 proves manifest custody and shape against the
pinned SHA-256. It **does not** repair `NO_GO_GOVERNING_GATE_UNMET`.

## Current Gaps

- Full upstream extraction of cuneiform helper modules
  (`benchmark_common.py`, `bench_tokenizer.py`, `probe_1nn.py`, P6/P7
  diagnostics) remains deferred per `docs/PATH_REWRITE_LEDGER.md`. The smoke
  is custody-only, not a full rerun.
- `revert_phase2_common.py` is `UPSTREAM_NOT_PRESENT` (`S-06`); flagged in
  the checksum register, not a blocker for this lane.
- Image-bearing sources and some upstream datasets remain rights-constrained
  or fetch-only; pixel-bearing data is never vendored.
- `NO_GO_GOVERNING_GATE_UNMET` remains the sovereign scientific truth.
  Repairing it is **out of scope** for this lane and is external work for a
  separate workstream (likely `gnosis-glyph-engine` or
  `gnosis-falsification-harness`).

## Upcoming Workstreams

### Active Engineering

- Smoke surface tightening if new schema variants are contributed (the
  stdlib-only constraint is a feature, not a bug — preserve it).

### Research-Deferred — Investigation Underway

- None currently. If upstream changes substrate-discrimination methodology,
  revisit whether P6/P7 diagnostics graduate from diagnostic-only to gate
  candidates.

### Operations / External Dependency

- **P5 governing-gate repair** is owned by a separate workstream (likely
  `gnosis-glyph-engine` or `gnosis-falsification-harness`). This lane
  preserves the negative result; it does not initiate gate repair.
- **Rights clearance** for image-bearing corpus redistribution remains
  unresolved; no action here until upstream rights review completes.

### Zero-Base Scientific Thinking — GPD Research and Planning Pending

- None currently scheduled. A new milestone in this lane opens only if a
  separate workstream produces gate-repair evidence that warrants revisiting
  the governing verdict.
