# Roadmap

## How To Read This File

This roadmap states direction, sequence, and dependencies. It is not an
evidence surface or a promise of delivery. Cuneiform remains a
negative-control/control-pack lane: the governing no-go result is preserved,
not repaired.

## Current State

| Field | Value |
|---|---|
| Repo posture | `HOLD_CONTROL_ONLY` |
| Commercial Readiness verdict | `STAGED` |
| Posture row | `negative_control_preservation` |
| Sovereign gate | `NO_GO_GOVERNING_GATE_UNMET` |
| Governing metric | `governing_1nn_accuracy = 0.021916` |
| Current package scope | manifest-validation smoke only |
| Ops hygiene gate | Ops-Gates coupling audit adopted in CI, pending repo-orchestrator review |

## Maintenance Priorities

| Priority | Item | Why It Matters | Evidence Needed | Status | Owner |
|---|---|---|---|---|---|
| P0 | Keep no-go/control truth inseparable from smoke `PASS` | Website and repo summaries must not narrate custody success as science success | `README.md`, `AUDITOR_PLAYBOOK.md`, `PUBLIC_AUDIT_LIMITS.md` | `IN_PROGRESS` | Repo orchestrator |
| P1 | Keep Ops-Gates load-bearing in CI | Cuneiform should consume shared operational-leak gates, not rely only on local prose | `.github/workflows/ci.yml`, green branch CI, `OPS_GATES_READ_TOKEN` present | `IN_PROGRESS` | Repo orchestrator |
| P2 | Keep HF custody routing current | Reviewers need the AP canonical store and Zer0pa lightweight split, not the pre-split revision only | `docs/HF_CUSTODY_REGISTER.md`, `docs/evidence/ARTEFACT_CHECKSUMS.md` | `DONE` | Lane |

## Deferred Or Blocked Work

| Item | Reason | Unblock Condition | Status |
|---|---|---|---|
| Product/scientific-success release | The inherited scientific gate failed | Separate workstream repairs the governing gate on evidence | `BLOCKED` |
| Full scientific rerun extraction | Current package deliberately validates manifest custody only | New milestone with source ownership and data plan | `DEFERRED` |
| Heavy asset vendoring or public HF visibility | Image-bearing material and some upstream data remain constrained | Explicit rights review plus fetch/checksum policy | `DEFERRED` |
| Ops-Gates `check_repo_truth` adoption | Current profiles are for the parent monorepo or Ops-Gates itself | Add a Cuneiform/control-pack profile or config-driven path ledger in Ops-Gates | `DEFERRED` |

## Status Rules

- Treat `NO_GO_GOVERNING_GATE_UNMET` as sovereign until new evidence changes
  it.
- Do not promote P6/P7 diagnostics as substitutes for P5 gate closure.
- A smoke `PASS` is custody-only.
- An Ops-Gates audit `PASS` is operational hygiene only.
