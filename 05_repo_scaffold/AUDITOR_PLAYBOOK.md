# Auditor Playbook

## Goal

Use this file to verify what this control pack currently proves without reading
the full doc surface.

## Fast Path

1. Read the authority block in `README.md`.
2. Read `docs/ARCHITECTURE.md` to see where truth lives.
3. Open `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md`.
4. Read `PUBLIC_AUDIT_LIMITS.md` before making portfolio-level claims.
5. Check `SOURCE_BOUNDARY.md` and `DATA_POLICY.md` for pack limits.

## Claim Replay Map

| Claim | Evidence Path | Publicly Verifiable? | Caveat |
|---|---|---|---|
| The lane is control-only and not a sovereign promotion candidate | `README.md`, `SOVEREIGN_PRD.md`, `GOVERNANCE.md` | `YES` | This pack documents posture; it does not repair the source-lane science gate. |
| The inherited governing gate failed and remains failed | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` | `PARTIAL` | The summary is staged here; the full upstream artifact chain still lives in the monorepo source paths named there. |
| Source families and data boundaries are explicit | `SOURCE_BOUNDARY.md`, `DATA_POLICY.md`, `docs/CUNEIFORM_RERUN_GUIDE.md` | `YES` | No runnable extracted rerun exists in this scaffold yet. |

## Minimum Replay Steps

1. Confirm the README still calls the lane benchmark/control only.
2. Verify the failed P5 verdict and metrics appear in the staged authority
   artifact.
3. Check that `SOURCE_BOUNDARY.md` excludes generic methods that belong
   elsewhere.
4. Record any missing artifact or uncited upgrade as `UNKNOWN` or
   `UNVERIFIED`, not as closure.

## If You Find A Problem

- Use the evidence dispute issue template for claim/evidence disagreements.
- Use the bug template for reproducible implementation defects.
- Use `PUBLIC_AUDIT_LIMITS.md` if the disagreement is caused by unavailable
  private inputs rather than a public contradiction.
