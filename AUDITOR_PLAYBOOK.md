# Auditor Playbook

Last reviewed: 2026-04-28 against the post-license, post-Ops-Gates adoption
candidate branch. The governing no-go result is unchanged.

## Goal

Verify what this control pack currently proves without reading the full doc
surface.

## Fast Path (≤ 10 minutes)

1. Read the authority block in `README.md`.
2. Read `docs/ARCHITECTURE.md` for the truth map.
3. Open `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` — confirm verdict
   `NO_GO_GOVERNING_GATE_UNMET` and `governing_1nn_accuracy = 0.021916`.
4. Open `docs/evidence/ARTEFACT_CHECKSUMS.md` — note the 6 pinned SHA-256s.
5. Open `artefacts/smoke/manifest_validation_report.json` — confirm
   `verdict: "PASS"`, `manifest_sha256_pinned == manifest_sha256`,
   `schema_errors: []`, all 5 invariants `ok: true`.
6. Open `artefacts/smoke/hf_upload_verify.json` — confirm
   `all_verified: true` and `private: true`.
7. Confirm CI includes both the repo-local operational leak scan and the
   Ops-Gates `coupling_audit.py` job pinned at `54ed0a7`.
8. Read `PUBLIC_AUDIT_LIMITS.md` before making any portfolio-level claim.

## Replay The Smoke Locally (≤ 60 seconds)

```bash
# From the scaffold root, with any compliant manifest at hand:
pip install -e .
python -m cuneiform_control.smoke.run_manifest_validation \
  --manifest /path/to/annotated_sign_benchmark_manifest.json \
  --schema   code/cuneiform_control/schemas/benchmark_manifest.schema.json \
  --checksum e4d85abf3bfa6901a6b20f7c612f1113e77ef9173ca42e00c9867b88b23daa24 \
  --report   /tmp/replay_report.json
# Or run the bundled fixture self-test:
python -m unittest tests.test_smoke_runner -v
```

A `PASS` exit code (`0`) and a matching observed SHA-256 prove that the pack's
smoke is real and reproducible. A `PASS` does **not** prove the failed
governing gate has been repaired.

## Claim Replay Map

| Claim | Evidence Path | Publicly Verifiable? | Caveat |
|---|---|---|---|
| The lane is control-only and not a sovereign promotion candidate | `README.md`, `SOVEREIGN_PRD.md`, `GOVERNANCE.md` | `YES` | Posture only; does not repair the science gate. |
| The inherited governing gate failed and remains failed | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`, smoke report `governing_verdict` field | `YES` | Smoke cannot move this gate by construction. |
| Source families and data boundaries are explicit | `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `docs/PATH_REWRITE_LEDGER.md` | `YES` | One ghost entry (`S-06`) retired during Phase 02 audit. |
| Manifest custody is pinned and verifiable | `docs/evidence/ARTEFACT_CHECKSUMS.md`, `artefacts/smoke/manifest_validation_report.json` | `YES` | Pins were verified on a known-good upstream pod 2026-04-24. |
| HF custody exists and matches the pins | `docs/HF_CUSTODY_REGISTER.md` Verification 5; AP revision `3ed3f0d4…`; lightweight Zer0pa surface `e08e1694…` | `INTERNAL_ONLY` | Datasets are `private`; only authorized accounts can fetch. |
| A bounded, stdlib-only smoke runner exists | `code/cuneiform_control/smoke/run_manifest_validation.py`, `tests/test_smoke_runner.py` | `YES` | No third-party deps, no pixel handling, no rerun of failing probe. |
| Ops-Gates is load-bearing for operational hygiene | `.github/workflows/ci.yml`; `Gnosis-Ops-Gates` `coupling_audit.py` pinned at `54ed0a7` | `YES` if CI secret is present | This is an ops hygiene gate only; it cannot move the science gate. |

## Minimum Replay Steps

1. Confirm the README still calls the lane benchmark/control only.
2. Verify the failed P5 verdict and metrics appear in the staged authority
   artefact AND in the smoke report's `governing_verdict` field.
3. Run the bundled fixture self-test (`python -m unittest tests.test_smoke_runner`).
4. Check that `SOURCE_BOUNDARY.md` + `PATH_REWRITE_LEDGER.md` together exclude
   the generic-methods code that belongs elsewhere.
5. Run `python3 ../Gnosis-Ops-Gates/code/tools/coupling_audit.py code tests`
   from a sibling checkout if reviewing locally.
6. Record any missing artefact or uncited upgrade as `UNKNOWN` or
   `UNVERIFIED`, not as closure.

## If You Find A Problem

- Use the evidence-dispute issue template for claim/evidence disagreements.
- Use the bug template for reproducible implementation defects.
- Use `PUBLIC_AUDIT_LIMITS.md` if the disagreement is caused by unavailable
  private inputs rather than a public contradiction.
- A SHA-256 mismatch is a **blocker**, not a fix-in-place: open an evidence
  dispute and record the divergence; do not edit the pin.
