# Governance

## Scope

This document defines how the repo states truth, promotes claims, handles
disputes, and decides release readiness.

## Truth Hierarchy

1. The active PRD and declared authority metric govern internal execution.
2. Accepted artifacts and evidence paths govern promoted technical claims.
3. Public docs summarize current truth; they do not override artifacts.
4. Issues and discussions can raise questions, but they do not redefine truth.

## Status Vocabulary

| Token | Meaning |
|---|---|
| `VERIFIED` | Backed by current evidence in this repo |
| `PARTIAL` | Some evidence exists, but the claim is bounded |
| `UNKNOWN` | No evidence surface exists yet |
| `UNVERIFIED` | Claimed or proposed, but not closed |
| `INFERRED` | Reasonable interpretation, not direct proof |
| `OWNER_DEFERRED` | Requires owner-supplied input before closure |

If the repo uses a Commercial Readiness `Verdict` field, use only:
`STAGED`, `PASS`, `PARTIAL`, `BLOCKED`, `FAIL`, or `INCONCLUSIVE`.

## Decision Rights

| Topic | Authority | Notes |
|---|---|---|
| PRD amendments | Owner | Threshold or posture changes must be explicit |
| Promoted public claims | Owner | No proxy-only closure and no control-lane upgrades without new evidence |
| Release approval | Owner | Must satisfy `RELEASING.md` and preserve the failed gate if unchanged |
| Legal statements | Owner | Must match the final license text and the current data posture |

## Claim Discipline

- One canonical authority block lives in `README.md`.
- Supporting docs deepen or bound the truth; they do not duplicate it blindly.
- Repo docs may inherit structure from another Zer0pa repo, never its facts.
- When two truth surfaces differ intentionally, state why explicitly.

## Dispute Handling

1. Point to the exact statement under dispute.
2. Point to the missing or conflicting evidence path.
3. Classify the issue as contradiction, ambiguity, missing artifact, or stale
   public surface.
4. Repair the evidence or downgrade the claim. Do not rewrite prose to hide the
   contradiction.
