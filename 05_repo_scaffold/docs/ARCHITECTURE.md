# Architecture

## Purpose

This file explains where technical truth lives in the repo. It is an index of
components, authority artifacts, and boundaries, not a marketing deck.

## System Snapshot

| Layer | What Lives Here | Source Of Truth |
|---|---|---|
| Public docs | Front-door control-pack posture, governance, and handover surfaces | `README.md`, `SOVEREIGN_PRD.md`, `MIGRATION_PLAN.md`, `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `TODO.md` |
| Code or runtime | Planned future rerun surface only; no extracted code package is admitted yet | `code/README.md`, `docs/CUNEIFORM_RERUN_GUIDE.md` |
| Evidence artifacts | Failed-gate summary, result summary, and contract docs | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`, `docs/evidence/CUNEIFORM_CONTROL_RESULTS.md`, `docs/family/CUNEIFORM_BENCHMARK_PACK_CONTRACT.md` |
| Owner-held or private context | Full upstream corpora, image-bearing assets, and monorepo-only rerun state | See `DATA_POLICY.md` and `SOURCE_BOUNDARY.md` |

## Component Map

| Component | Responsibility | Inputs | Outputs | Notes |
|---|---|---|---|---|
| Control-pack front door | State current lane truth and prevent overclaiming | corrected workstream docs, staged authority summaries | README and governance surface | Must keep benchmark/control posture explicit |
| Source boundary layer | Freeze what belongs to this lane and what must stay elsewhere | cuneiform scripts, artifacts, review-pack sources | `SOURCE_BOUNDARY.md`, rerun guide | Excludes generic methods that belong in other lanes |
| Evidence layer | Preserve the failed gate and selected control results | upstream phase and review artifacts | staged evidence summaries | Summaries do not replace upstream artifact custody |
| Future rerun layer | Define what a truthful minimal extraction would need | source files, fetch rules, data rights | migration plan and future extraction tasks | Currently blocked by code and data coupling |

## Authority Artifacts

| Artifact | Path | Why It Matters | Public? |
|---|---|---|---|
| Phase 2 gate status | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` | Keeps the failed governing verdict visible inside the scaffold | `PARTIAL` |
| Control results summary | `docs/evidence/CUNEIFORM_CONTROL_RESULTS.md` | Shows why the lane remains useful as control material despite failure | `PARTIAL` |
| Benchmark pack contract | `docs/family/CUNEIFORM_BENCHMARK_PACK_CONTRACT.md` | Defines the bounded control-pack surface for future extraction | `YES` |

## Truth Surface Boundaries

- `README.md` is the front door and routes outward.
- `AUDITOR_PLAYBOOK.md` is the shortest outsider replay path.
- `PUBLIC_AUDIT_LIMITS.md` bounds what a public clone can prove.
- `code/README.md` owns package and interface details.
- `docs/LEGAL_BOUNDARIES.md` summarizes legal constraints but does not replace
  the license.

## Known Gaps

- No extracted installable code root or smoke test exists yet inside this
  scaffold.
- Some upstream image-bearing data and fetch surfaces remain rights-limited or
  monorepo-coupled.
