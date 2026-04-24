# AGENTS

Workstream root: this repository root (repo `Zer0pa/Cuneiform`, `main` branch).

## Mission

Maintain this repo as the truthful control-module pack for `gnosis-cuneiform`.
This lane is benchmark/control only. The inherited failed governing gate is
sovereign and must remain visible in every promoted surface.

## Read First

1. `README.md`
2. `SOVEREIGN_PRD.md`
3. `SOURCE_BOUNDARY.md`
4. `DATA_POLICY.md`
5. `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`
6. `.gpd/PROJECT.md`
7. `.gpd/REQUIREMENTS.md`
8. `.gpd/ROADMAP.md`
9. `.gpd/STATE.md`
10. the active phase plan under `.gpd/phases/`

## Hard Rules

- The top acceptance gate is sovereign.
- `NO_GO_GOVERNING_GATE_UNMET` stays explicit.
- P6 and P7 diagnostics do not substitute for the failed P5 gate.
- Do not position this lane as a flagship, product wedge, or public-ready repo.
- Do not absorb generic methods that belong in `gnosis-glyph-engine` or
  `gnosis-morph-bench`.
- Do not revert unrelated work from other agents.
- Keep contradictions visible until evidence changes them.
- Keep docs and handover artefacts aligned with the real gate state.

## Coding Commandments

- Avoid deep nesting.
- Avoid code duplication.
- Do not use naming that only you understand.
- Use dependency injection where it meaningfully decouples components.
- Use interfaces where they make the boundary clearer.
- Keep functions scoped to one responsibility where practical.
