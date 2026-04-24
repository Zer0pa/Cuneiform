# Gnosis Cuneiform

> Internal control-module pack for the cuneiform benchmark/control lane.
> **INTERNAL** visibility; public promotion blocked by
> `NO_GO_GOVERNING_GATE_UNMET`.

## What This Repo Is

`gnosis-cuneiform` preserves the cuneiform control/benchmark artefact chain,
the failed governing gate, the source boundary, and the rerun contract without
pretending this lane is a sovereign external product or a successful scientific
flagship.

## Current Authority

| Item | Current Truth |
|---|---|
| Product lane | `MODULE_ONLY_CONTROL_PACK` |
| Repo URL | `https://github.com/Zer0pa/Cuneiform` |
| Default branch | `main` |
| Visibility | `INTERNAL` (Zer0pa org) |
| Licence | `OWNER_DEFERRED` — see `PRIVATE_INTERNAL_LICENSE_NOTICE.md` |
| Acquisition surface | Internal git remote + Hugging Face (see `docs/HF_CUSTODY_REGISTER.md`) |
| Governing verdict | `NO_GO_GOVERNING_GATE_UNMET` |
| Governing metric | `governing_1nn_accuracy = 0.021916` |
| Evidence status | `PARTIAL` |
| Primary contact | `OWNER_DEFERRED` |

## What We Prove Now

- A real cuneiform benchmark/control artefact chain exists and is worth keeping
  as validation material.
- The inherited governing gate failed: P5 closed `NO_GO_GOVERNING_GATE_UNMET`
  at `governing_1nn_accuracy = 0.021916`, and later P6/P7 diagnostics do not
  undo that result.
- A **minimal stdlib-only installable smoke surface** ships in this repo
  (`cuneiform_control`, entry point `cuneiform-smoke`). It validates manifest
  **custody, shape, and cross-field invariants** against pinned SHA-256s.
- `SMOKE-01-MANIFEST-VALIDATION` runs and passes against the pinned upstream
  manifest (6 SHA-256 pins, 5 cross-field invariants). See
  `artefacts/smoke/manifest_validation_report.json`.
- The smoke is custody-only by construction: it **does not repair** the failed
  governing gate, **does not** change `governing_1nn_accuracy`, and **does
  not** promote any P6/P7 diagnostic into gate closure.

## What We Do Not Claim

- This lane is not a flagship, a sovereign external repo candidate, or a
  current product thesis.
- The pack does not claim a repaired scientific gate, positive decipherment,
  or cross-domain superiority.
- The pack is not public-release ready and does not carry cleared image
  rights.

## Repository Layout (flattened 2026-04-24)

| Path | What Lives Here |
|---|---|
| `README.md`, `SOVEREIGN_PRD.md`, `AUDITOR_PLAYBOOK.md`, `AGENTS.md` | Front-door truth, reviewer entry points, agent brief |
| `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `GOVERNANCE.md`, `RELEASING.md` | Policy surfaces |
| `LICENSE_PLACEHOLDER.md`, `PRIVATE_INTERNAL_LICENSE_NOTICE.md` | Licence posture (currently `OWNER_DEFERRED`) |
| `code/cuneiform_control/` | Stdlib-only smoke runner + conservative JSON Schema |
| `tests/` | Hermetic pytest-discovered self-test for the smoke runner |
| `pyproject.toml` | Package manifest (no third-party deps; `Private :: Do Not Upload`) |
| `artefacts/smoke/` | Deterministic smoke-report JSONs (`PASS`) |
| `docs/` | Architecture, path-rewrite ledger, smoke-target spec, HF custody register, rerun guide |
| `docs/evidence/` | Failed-gate evidence, artefact checksum pins, control results |
| `docs/migration/` | Original migration-package brief, authority notes, source inventory, handover (preserved as transfer history) |
| `.gpd/` | GPD phase pack (`PROJECT.md`, `STATE.md`, phases, requirements, roadmap) |
| `.github/` | Issue templates, PR template |

## Read Next

| Need | File |
|---|---|
| **Reviewer landing page** | `docs/EXECUTOR_STATUS_REPORT.md` |
| Sovereign brief for the lane | `SOVEREIGN_PRD.md` |
| Failed-gate summary | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` |
| Fast audit path | `AUDITOR_PLAYBOOK.md` |
| Architecture and truth map | `docs/ARCHITECTURE.md` |
| HF custody (token-verified) | `docs/HF_CUSTODY_REGISTER.md` |
| Source ownership and exclusions | `SOURCE_BOUNDARY.md`, `docs/PATH_REWRITE_LEDGER.md` |
| Data and release limits | `DATA_POLICY.md`, `PUBLIC_AUDIT_LIMITS.md` |
| Smoke target spec | `docs/MINIMAL_SMOKE_TARGET.md` |
| Current state | `.gpd/STATE.md` |
| Immediate residual work | `TODO.md` |

## Quickstart (verified 2026-04-24)

```bash
python3 -m venv /tmp/cuneiform-control
source /tmp/cuneiform-control/bin/activate
python -m pip install --upgrade pip
python -m pip install -e . pytest
pytest -q
cuneiform-smoke --help
```

A successful `pytest -q` run shows **3 passed** (hermetic self-test against
bundled fixtures). `cuneiform-smoke --help` documents the real-manifest
replay flags (`--manifest`, `--schema`, `--checksum`, `--report`,
`--manifest-label`, `--schema-label`).

A `PASS` verdict from the runner proves manifest custody and shape against
the pinned SHA-256. It **does not** repair `NO_GO_GOVERNING_GATE_UNMET`.

## Current Gaps

- Full upstream extraction of cuneiform helper modules (`benchmark_common.py`,
  `bench_tokenizer.py`, `probe_1nn.py`, and P6/P7 diagnostic scripts) remains
  deferred per `docs/PATH_REWRITE_LEDGER.md`. The smoke is a custody-only
  surface, not a full rerun.
- Image-bearing sources and some upstream datasets remain rights-constrained
  or fetch-only; pixel-bearing data is never vendored.
- **Public release remains blocked** by image/data rights posture and the
  unresolved licence decision (`OWNER_DEFERRED`). No remote git tag push and
  no public visibility change until the owner rules.
- `NO_GO_GOVERNING_GATE_UNMET` and `governing_1nn_accuracy = 0.021916` remain
  the scientific truth. Repairing that gate is **not** in scope for this lane;
  it is external work for a separate workstream.
