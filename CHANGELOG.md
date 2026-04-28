# Changelog — gnosis-cuneiform

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [Unreleased]

## [0.1.0-refresh] — 2026-04-28

### Added

- Live-window banner at top of README (Zer0pa lab posture: useful now,
  improving continuously).
- `## Commercial Readiness` section in README with `STAGED` verdict cell and
  `negative_control_preservation` posture row.
- `## Upcoming Workstreams` section in README with 4-category taxonomy.
- Headline-first defensible metric and honest-blocker line in `## What This Is`.
- `CHANGELOG.md` (this file).
- `CITATION.cff` (entity attribution for Zer0pa Architects).
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1).
- `_internal/` subdirectory for agent-orchestration scaffolding files
  (AUTONOMOUS_EXECUTION_POLICY, GPD_BOOTSTRAP_GUIDE, STARTUP_PROMPT,
  TEMPLATE_USAGE, UNIVERSAL_STARTUP_PROMPT, WORKSTREAM_GPD_INIT_CHECKLIST,
  MIGRATION_PLAN, TODO).
- `Private :: Do Not Upload` classifier added to `pyproject.toml`.

### Changed

- Repo description updated to public-truth single-line (dropped "Private" prefix).
- GitHub topics filled (11 topics: gnosis, zer0pa, cuneiform, negative-control,
  falsification, methods, provenance, manifest-validation, python, methodology,
  no-decipherment-claim).
- Scaffolding files relocated from repo root to `_internal/`.

### Preserved (unchanged by this wave)

- `## Traditional-Knowledge Acknowledgment` — verbatim, no modification.
- All HF anchors (`Architect-Prime/cuneiform-control-artefacts`) — intact.
- `NO_GO_GOVERNING_GATE_UNMET` evidence chain — intact.
- `pyproject.toml` `Private :: Do Not Upload` classifier — added per design intent.
- All proof artifacts in `artefacts/` and `docs/evidence/`.

---

## [0.1.0-internal] — 2026-04-24

### Added

- PRD-complete: four phases closed (00 Truth-Surface Bootstrap, 01 Control
  Boundary And Rerun Ledger, 02 Minimal Rerun Or Manifest Smoke, 03 Control-Pack
  Handover).
- `SMOKE-01-MANIFEST-VALIDATION` executed; verdict `PASS`; SHA-256 pinned.
- HF dataset created and verified (`Architect-Prime/cuneiform-control-artefacts`).
- Hermetic self-test: 3/3 pass.
- All front-door truth surfaces (README, AUDITOR_PLAYBOOK, SOVEREIGN_PRD,
  docs/evidence/).
- Repo flattened; operational paths scrubbed; HF custody recorded.
