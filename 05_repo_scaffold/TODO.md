# TODO

## Now

PRD-level work is **complete** as of 2026-04-24. There is no scheduled "Now"
work in this lane. Any new work requires a new milestone gated on a
gate-repair event in a separate workstream.

## Done — PRD Closed (2026-04-24)

- [x] Phase 00 — Truth-Surface Bootstrap.
- [x] Phase 01 — Path-rewrite ledger + minimal smoke target frozen.
- [x] Phase 02 — `SMOKE-01-MANIFEST-VALIDATION` executed against the real
      upstream manifest; verdict `PASS`; HF dataset created and verified.
- [x] Phase 03 — Control-pack handover; `pyproject.toml` ships; self-test
      3/3 pass; all front-door truth surfaces updated.

## Stays Blocked Forever (until external evidence)

- [ ] Public promotion while `NO_GO_GOVERNING_GATE_UNMET` remains unchanged.
- [ ] Any repo narrative that upgrades the lane beyond benchmark/control use.
- [ ] Heavy asset vendoring without explicit rights clearance.
- [ ] Re-running the failed governing probe and narrating any result as a pass.
- [ ] Promoting P6 or P7 diagnostic numbers as substitute gate closure.
- [ ] Pushing the `v0.1.0-internal` git tag to the remote.
- [ ] Setting the HF dataset visibility to anything other than `private`.

## If A Future Workstream Repairs The Gate

- [ ] Open a new milestone (`/gpd:new-milestone`) here.
- [ ] Re-run `SMOKE-01-MANIFEST-VALIDATION` against the new manifest before
      claiming any change.
- [ ] Update `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` with the new
      verdict — never silently overwrite.
- [ ] Re-evaluate `RELEASING.md` constraints with the owner.
