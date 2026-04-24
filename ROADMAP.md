# Roadmap

## How To Read This File

This roadmap states direction, sequence, and dependencies. It is not itself an
evidence surface or a promise of delivery.

## Active Priorities

| Priority | Item | Why It Matters | Entry Gate | Evidence Needed | Status | Owner |
|---|---|---|---|---|---|---|
| P0 | Freeze the control-pack truth surface | Every downstream action depends on keeping the failed gate and control-only posture explicit | Shared pack copied and customized | `README.md`, `SOVEREIGN_PRD.md`, `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` | `IN_PROGRESS` | Owner |
| P1 | Complete the path-rewrite and rerun ledger | Future extraction needs an explicit list of import, path, and data blockers | P0 coherent | `SOURCE_BOUNDARY.md`, `docs/CUNEIFORM_RERUN_GUIDE.md`, `.gpd/phases/01-control-pack-admission/01-01-PLAN.md` | `NOT_STARTED` | Owner |
| P2 | Prepare a minimal internal rerun scaffold | The lane should eventually support a truthful tiny rerun without promotion theater | P1 source audit complete | staged helper modules, tiny fixture or manifest-only smoke path | `DEFERRED` | Owner |

## Deferred Or Blocked Work

| Item | Reason | Unblock Condition | Status |
|---|---|---|---|
| Public promotion or sovereign repo narrative | The inherited scientific gate failed and the data/legal surface is not cleared for public release | A future workstream repairs the governing gate and clears the data and license posture | `BLOCKED` |
| Heavy asset vendoring | Image-bearing material and upstream fetch surfaces remain constrained | Rights review plus explicit fetch/checksum policy | `DEFERRED` |

## Status Rules

- Use simple states such as `NOT_STARTED`, `IN_PROGRESS`, `BLOCKED`,
  `DEFERRED`, `DONE`, or the repo's declared project states.
- If a priority depends on private inputs or owner action, say so plainly.
- Remove stale items instead of letting the file become a graveyard.
