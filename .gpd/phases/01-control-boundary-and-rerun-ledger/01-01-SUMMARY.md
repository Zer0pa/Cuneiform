# Phase 01 Plan 01 — Summary

## Close

Phase 01 `01-control-boundary-and-rerun-ledger` closed on 2026-04-24 under the
autonomous execution policy. The governing gate did **not** change.

## What Was Produced

| Artifact | Purpose | Status |
|---|---|---|
| `docs/PATH_REWRITE_LEDGER.md` | Freezes the source-to-destination mapping for cuneiform-specific code and derived artefacts; names exclusions for shared-method code. | Frozen (append-only) |
| `docs/MINIMAL_SMOKE_TARGET.md` | Admits `SMOKE-01-MANIFEST-VALIDATION` as the single smallest rerun-contract proof. | Admitted; execution deferred to Phase 02 |
| `.gpd/REQUIREMENTS.md` | Marks `DATA-03` and `DERV-02` complete with artefact references. | Updated |
| `.gpd/ROADMAP.md` | Marks Phase 01 complete; Phase 02 active next. | Updated |
| `.gpd/STATE.md`, `.gpd/state.json` | Advanced to Phase 02; previous-phase close recorded. | Updated |
| `TODO.md` | Now-list refreshed to Phase 02 actions; "Must Stay Blocked" list preserved. | Updated |
| `docs/migration/04_evidence_manifest/README.md` | Registers Phase 01 artefacts with their custody class. | Updated |
| Git remote | `https://github.com/Zer0pa/Cuneiform` (INTERNAL, `main`) wired from current workstream root. | Live |
| `UNIVERSAL_STARTUP_PROMPT.md` | Path drift (old monorepo-absolute path) repaired. | Updated |
| Closeout pass (2026-04-24) | Repo flattened (former `05_repo_scaffold/*` → root; migration folders → `docs/migration/`); operational paths scrubbed. | Applied |

## Governing-Gate Delta

| Metric | Before | After | Delta |
|---|---|---|---|
| Governing verdict | `NO_GO_GOVERNING_GATE_UNMET` | `NO_GO_GOVERNING_GATE_UNMET` | `unchanged` |
| `governing_1nn_accuracy` | `0.021916` | `0.021916` | `unchanged` |
| P6 diagnostic accuracy | `0.038176` | `0.038176` | `unchanged; remains diagnostic-only` |
| P7 diagnostic accuracy | `0.051826` | `0.051826` | `unchanged; remains diagnostic-only` |
| Promotion posture | blocked | blocked | `unchanged` |

This is the correct outcome. Phase 01 is a boundary phase; it does not compute
new scientific numbers.

## Pass-Condition Check

Phase 01 pass condition (`01-01-PLAN.md`):

> A fresh agent can identify source, destination, input custody, first smoke
> target, and the reason public promotion remains blocked.

| Criterion | Evidence | Status |
|---|---|---|
| Source identified | `PATH_REWRITE_LEDGER.md` §A | Pass |
| Destination identified | `PATH_REWRITE_LEDGER.md` §A (column: Destination in this repo) | Pass |
| Input custody identified | `PATH_REWRITE_LEDGER.md` §C–§E + `DATA_POLICY.md` references | Pass |
| First smoke target identified | `MINIMAL_SMOKE_TARGET.md` (`SMOKE-01-MANIFEST-VALIDATION`) | Pass |
| Reason promotion remains blocked | `CUNEIFORM_PHASE2_GATE_STATUS.md` + governing-gate delta above | Pass |

**Phase 01 gate: PASS.** Governing verdict remains `NO_GO_GOVERNING_GATE_UNMET`
by design — this phase was never authorized to repair it.

## Executive Decisions Made Autonomously

Per `AUTONOMOUS_EXECUTION_POLICY.md` executive-mandate clause:

1. **Rename `revert_phase2_common` → `rerun_phase2_common`** on extraction.
   Reason: `revert_` misrepresents the code's rerun role; the rename closes a
   future narration risk.
2. **Retain P6/P7 diagnostic scripts with a `_diagnostic` destination suffix.**
   Reason: keeps them extractable without losing the anti-narration signal.
3. **Default HF dataset visibility to `private` (INTERNAL)** pending owner
   ruling. Reason: `DATA_POLICY.md` tags derived manifests `PUBLISH_WITH_REVIEW`;
   the lane verdict blocks public promotion; `private` is the only safe default.
4. **Retire the upstream `scripts/cuneiform/` prefix on destination.** Reason:
   the destination is a package (`cuneiform_control`), not a loose script
   folder; preserving the prefix would re-inherit a monorepo coupling.
5. **Admit `SMOKE-01-MANIFEST-VALIDATION` over a full-probe rerun.** Reason:
   rerunning the probe without cleared pixel custody risks narrativizing the
   failed gate; manifest-validation proves custody without touching scientific
   claims.
6. **Set repo default branch to `main` and visibility to `INTERNAL`.** Reason:
   matches scaffold README and GitHub metadata; INTERNAL is mandatory while the
   governing gate is failed.

## What Was Explicitly Not Done

- No code was extracted into `code/`. Phase 02 owns extraction.
- No manifest was uploaded to HF. Checksums must be pinned in Phase 02 first.
- No pixel-bearing asset was touched. Rights posture is unresolved.
- No rerun of the failing governing probe. That would narrate P5 into a pass.
- No P6/P7 diagnostic was re-executed or promoted. They remain diagnostic-only.
- No public-release surface was created.

## Open Blockers Carried Forward

1. Public promotion — blocked by `NO_GO_GOVERNING_GATE_UNMET`.
2. Image/pixel redistribution — blocked by unresolved rights.
3. Licence text — `OWNER_DEFERRED` in `README.md`; needs decision before any
   public surface is ever considered.

## Next Phase Entry

Phase 02 entry is `.gpd/phases/02-minimal-rerun-or-manifest-smoke/02-01-PLAN.md`
(to be authored as the first act of Phase 02 execution).
