# Workstream GPD Init Checklist

Use this checklist to confirm the copied starter pack has been specialized into
truthful `gnosis-cuneiform` control-pack state.

## Copy And Boundaries

- [x] Copy the shared GPD pack into the workstream root.
- [x] Confirm the workstream write scope and ownership boundary.
- [x] Confirm the sovereign PRD for the control pack.
- [x] Confirm the failed gate and source-boundary anchors that actually apply.

## Replace Placeholders

- [x] Replace every inherited starter placeholder token.
- [x] Remove inherited claims, metrics, statuses, or artefact paths that are
      not true for this workstream.
- [x] Convert unresolved execution gaps into explicit blocked state.

## Initialize Core Truth Surfaces

- [x] Fill `.gpd/PROJECT.md`.
- [x] Fill `.gpd/REQUIREMENTS.md`.
- [x] Fill `.gpd/ROADMAP.md`.
- [x] Fill `.gpd/STATE.md`.
- [x] Fill `.gpd/CONVENTIONS.md`.
- [x] Fill `.gpd/config.json`.
- [x] Fill `.gpd/state.json`.

## Freeze The First Governing Gate

- [x] Name `control_truth_preserved` and the inherited failed metric.
- [x] Name the failed source verdict as the comparator boundary.
- [x] Name the required deliverables and artefact paths.
- [x] Name the destructive checks that block promotion drift.
- [x] Name the stop-and-rethink conditions.

## Bootstrap The Phase Surface

- [x] Customize `.gpd/phases/00-workstream-bootstrap/00-CONTEXT.md`.
- [x] Customize `.gpd/phases/00-workstream-bootstrap/00-RESEARCH.md`.
- [x] Customize `.gpd/phases/00-workstream-bootstrap/00-VERIFICATION.md`.
- [x] Customize `.gpd/phases/00-workstream-bootstrap/00-01-PLAN.md`.
- [x] Execute the bootstrap plan before opening Phase 01.
- [x] Write `.gpd/phases/00-workstream-bootstrap/00-01-SUMMARY.md`.

## Phase 01 Close (2026-04-24)

- [x] Path-rewrite ledger frozen — `docs/PATH_REWRITE_LEDGER.md`.
- [x] Minimal smoke target admitted — `docs/MINIMAL_SMOKE_TARGET.md`.
- [x] HF dataset plan named — `docs/HF_DATASET_PLAN.md`.
- [x] Phase 01 summary — `.gpd/phases/01-control-boundary-and-rerun-ledger/01-01-SUMMARY.md`.
- [x] Governing verdict unchanged.

## Phase 02 Close (2026-04-24)

- [x] Pinned SHA-256s — `docs/evidence/ARTEFACT_CHECKSUMS.md` (6 manifests + 5 sources + 1 `UPSTREAM_NOT_PRESENT`).
- [x] Conservative JSON Schema shipped — `code/cuneiform_control/schemas/benchmark_manifest.schema.json`.
- [x] Stdlib-only smoke runner shipped — `code/cuneiform_control/smoke/run_manifest_validation.py`.
- [x] Smoke executed on pod against real manifest, verdict `PASS`.
- [x] Smoke report — `artefacts/smoke/manifest_validation_report.json`.
- [x] HF dataset created (private) and post-upload SHA-256 verified.
- [x] HF revision recorded — `c64e22f671dcce1577233309fd3320258dbd2e09`.
- [x] Path-rewrite ledger amended — `S-06` `revert_phase2_common.py` recorded as `UPSTREAM_NOT_PRESENT`; `S-05` `probe_annotated_sign_p8_1nn.py` added.
- [x] Phase 02 summary — `.gpd/phases/02-minimal-rerun-or-manifest-smoke/02-01-SUMMARY.md`.
- [x] Governing verdict unchanged.

## Phase 03 Close (2026-04-24)

- [x] `pyproject.toml` shipped (no third-party deps; `cuneiform-smoke` entry point).
- [x] Hermetic self-test shipped — `tests/test_smoke_runner.py` (3/3 pass on host).
- [x] Bundled fixtures — `tests/fixtures/manifest_min_pass.json`, `manifest_min_fail_invariant.json`.
- [x] Handover doc rewritten — `06_handover/README.md`.
- [x] `docs/ARCHITECTURE.md` updated to register the now-real package, smoke, evidence, and HF custody.
- [x] `AUDITOR_PLAYBOOK.md` updated with Fast Path + Replay command.
- [x] `PUBLIC_AUDIT_LIMITS.md` updated; smoke is custody-only by construction.
- [x] `RELEASING.md` updated with `v0.1.0-internal` tag rule.
- [x] `docs/CUNEIFORM_RERUN_GUIDE.md` updated — status `SMOKE_AVAILABLE; FULL_RERUN_BLOCKED_BY_GATE`.
- [x] `TODO.md` reflects PRD-complete state.
- [x] `04_evidence_manifest/README.md` registers Phase 02–03 artefacts.
- [x] Phase 03 summary — `.gpd/phases/03-control-pack-handover/03-01-SUMMARY.md`.
- [x] Governing verdict unchanged across all phases.

## Coherence Checks

- [x] `PROJECT.md`, `REQUIREMENTS.md`, and `ROADMAP.md` agree on phase names
      and gates.
- [x] `STATE.md` and `state.json` agree on current phase, status, and blockers.
- [x] `CONVENTIONS.md` matches real terminology and reporting rules.
- [x] The startup prompt still matches the workstream root and PRD path.
- [x] Smoke report `governing_verdict` field matches `state.json`
      `governing_source_verdict`.
- [x] HF dataset card `governing_verdict` line matches `state.json`.
- [x] Tag `v0.1.0-internal` is annotated and **not** pushed to remote.

## Ready To Hand To An Autonomous Agent

- [x] The workstream can be read without parent-repo tribal knowledge.
- [x] The workstream can be executed without interim reporting.
- [x] A blocker-only escalation path is defined.
- [x] The active Phase 01 plan exists before coding starts.
- [x] PRD complete; no further phases scheduled in this lane.
