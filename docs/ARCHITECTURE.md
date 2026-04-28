# Architecture

## Purpose

This file explains where technical truth lives in the repo. It is an index of
components, authority artefacts, and boundaries — not a marketing deck.

## System Snapshot (2026-04-28, post-license and Ops-Gates adoption wave)

| Layer | What Lives Here | Source Of Truth |
|---|---|---|
| Public docs | Front-door control-pack posture, governance, handover | `README.md`, `SOVEREIGN_PRD.md`, `_internal/MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `_internal/TODO.md`, `docs/migration/06_handover/README.md` |
| Code package | Minimal extracted surface for manifest validation; stdlib-only | `code/cuneiform_control/__init__.py`, `code/cuneiform_control/schemas/benchmark_manifest.schema.json`, `code/cuneiform_control/smoke/run_manifest_validation.py`, `pyproject.toml` |
| Smoke evidence | Deterministic JSON reports from `SMOKE-01-MANIFEST-VALIDATION` | `artefacts/smoke/manifest_validation_report.json`, `artefacts/smoke/hf_upload_verify.json` |
| Pinned custody | SHA-256 pins for 6 manifests + 5 source scripts; one `UPSTREAM_NOT_PRESENT` entry | `docs/evidence/ARTEFACT_CHECKSUMS.md` |
| Path-rewrite ledger | Frozen source-to-destination mapping with admit/exclude rules | `docs/PATH_REWRITE_LEDGER.md`, `docs/MINIMAL_SMOKE_TARGET.md`, `docs/HF_DATASET_PLAN.md` |
| Failed-gate evidence | Phase 2 status + control results + benchmark-pack contract | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`, `docs/evidence/CUNEIFORM_CONTROL_RESULTS.md`, `docs/family/CUNEIFORM_BENCHMARK_PACK_CONTRACT.md` |
| Remote artefact custody | HF private custody for manifests, workspace backups, and checkpoints | `Architect-Prime/cuneiform-control-artefacts` revision `3ed3f0d40585b9afa9366d7748f7d8228de1bf25`; `Zer0pa/cuneiform-control-artefacts` remains a private lightweight discovery surface for M-04..M-06 |
| Operational hygiene gate | Ops-Gates coupling audit over Python surfaces | `.github/workflows/ci.yml` consumes `Gnosis-Ops-Gates` `coupling_audit.py` pinned at `54ed0a7` |
| Owner-held / private | Full upstream corpora, image-bearing assets, monorepo helper imports | See `DATA_POLICY.md` and `SOURCE_BOUNDARY.md` |

## Component Map

| Component | Responsibility | Inputs | Outputs | Notes |
|---|---|---|---|---|
| Control-pack front door | State current lane truth and prevent overclaiming | corrected workstream docs, staged authority summaries | README and governance surface | Keeps benchmark/control posture explicit |
| Source boundary layer | Freeze what belongs to this lane and what must stay elsewhere | cuneiform scripts, artefacts, review-pack | `SOURCE_BOUNDARY.md`, `PATH_REWRITE_LEDGER.md`, `CUNEIFORM_RERUN_GUIDE.md` | Excludes generic methods that belong in other lanes |
| Evidence layer | Preserve the failed gate and selected control results | upstream phase + review artefacts | staged evidence + checksum pins + smoke reports | Summaries do not replace upstream artefact custody |
| Smoke layer | Prove manifest custody and shape without computing scientific metrics | pinned manifest, JSON schema | deterministic JSON report | Stdlib-only; cannot move the failed gate by construction |
| HF artefact custody | Hold derived JSON manifests with pinned SHA-256s | staged manifests | private HF dataset revision + dataset card | Visibility hard-locked to `private` |

## Authority Artefacts

| Artefact | Path | Why It Matters | Public? |
|---|---|---|---|
| Phase 2 gate status | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` | Keeps the failed governing verdict visible inside the scaffold | `PARTIAL` |
| Control results summary | `docs/evidence/CUNEIFORM_CONTROL_RESULTS.md` | Shows why the lane remains useful as control material despite failure | `PARTIAL` |
| Benchmark pack contract | `docs/family/CUNEIFORM_BENCHMARK_PACK_CONTRACT.md` | Defines the bounded control-pack surface for future extraction | `YES` |
| Path-rewrite ledger | `docs/PATH_REWRITE_LEDGER.md` | Frozen source-to-destination map; admits/excludes; one ghost entry retired | `YES` |
| Smoke target spec | `docs/MINIMAL_SMOKE_TARGET.md` | Names `SMOKE-01-MANIFEST-VALIDATION` and the explicit non-goals | `YES` |
| Artefact checksum pins | `docs/evidence/ARTEFACT_CHECKSUMS.md` | SHA-256 pins for 6 manifests + 5 sources + 1 `UPSTREAM_NOT_PRESENT` | `YES` |
| Smoke report | `artefacts/smoke/manifest_validation_report.json` | Verdict `PASS`, all invariants OK, sha256 matches pin | `YES` |
| HF upload verify | `artefacts/smoke/hf_upload_verify.json` | Post-upload SHA-256 verify of all 6 manifests against pins | `YES` |

## Truth Surface Boundaries

- `README.md` is the front door and routes outward.
- `AUDITOR_PLAYBOOK.md` is the shortest outsider replay path.
- `PUBLIC_AUDIT_LIMITS.md` bounds what a public clone can prove (still tight
  while the gate is failed).
- `code/README.md` documents the smoke surface.
- `pyproject.toml` is the minimum extracted package contract.
- `docs/LEGAL_BOUNDARIES.md` summarizes legal constraints but does not replace
  `LICENSE`, `NOTICE`, `TRADEMARKS.md`, or `DATA_POLICY.md`.

## Known Gaps Closed in Phase 02–03

- ~~No extracted installable code root or smoke test exists yet inside this
  scaffold.~~ → `code/cuneiform_control/` package + `pyproject.toml` + smoke
  runner ship in this scaffold.
- ~~No truthful minimal rerun surface exists.~~ →
  `SMOKE-01-MANIFEST-VALIDATION` runs and PASSes against the real upstream
  manifest with pinned SHA-256.

## Known Gaps Still Open

- The failed governing gate is unrepaired (and not in this lane's scope).
- Image-bearing data and some upstream fetch surfaces remain rights-limited.
- Derived manifests, model checkpoints, and private HF artefacts remain governed
  by `DATA_POLICY.md`; code/docs licensing does not publish those bytes.
- `revert_phase2_common.py` was inherited as a reference but is
  `UPSTREAM_NOT_PRESENT` on the pod; recorded as `S-06`, not blocking.
- `check_repo_truth` from Ops-Gates is not adopted yet; Ops-Gates lacks a
  Cuneiform/control-pack profile, so using it now would require fake paths.
