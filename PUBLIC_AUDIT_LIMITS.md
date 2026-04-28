# Public Audit Limits

## Purpose

This staged control pack can establish only what the visible artefact and
documentation surface support. It must not be read as proof of a repaired
cuneiform result or a public-ready standalone repo.

## What A Public Audit Can Now Establish (after Phase 03)

| Surface | What It Can Show |
|---|---|
| Source tree | The lane is intentionally framed as benchmark/control only and bounded by explicit source and data policies |
| Path-rewrite ledger | Exactly which upstream files are admitted and which are excluded; one ghost entry (`revert_phase2_common.py`) was audited and retired as `UPSTREAM_NOT_PRESENT` |
| Pinned checksums | 6 manifest SHA-256 pins + 5 source-script pins; reproducible from any compliant copy of those files |
| Smoke runner | A stdlib-only Python 3.8+ runner is present and self-tested against bundled fixtures |
| Smoke report | `verdict: PASS` with explicit cross-field invariants and the observed-vs-pinned SHA-256 |
| Failed-gate posture | The inherited P5 gate failed and the pack preserves that failure across docs, smoke report, code package, and HF dataset card |
| Docs coherence | Whether the public truth surface is internally consistent across README / PRD / ARCHITECTURE / RELEASING |

## What A Public Audit Still Cannot Establish

| Missing Input | Why It Matters |
|---|---|
| Repaired governing gate | No artefact in this lane proves the failed metric has improved. The smoke is custody-only by construction. |
| HF artefact contents | The HF dataset is `private`. A non-Zer0pa account sees only the SHA-256 pins, not the bytes. |
| Full upstream cuneiform corpora and image-bearing assets | Some sources remain fetch-only or rights-constrained. |
| Dataset and corpus redistribution | Apache-2.0 for code and CC-BY-4.0 for docs do not license private HF artefacts, derived manifests, model checkpoints, or rights-constrained source corpora. |
| Future gate-repair evidence | No document here proves that the failed governing metric will be repaired. |

## Rules For Interpreting This Repo

- Do not infer private results from public prose.
- Do not turn roadmap intent into proof.
- Do not use portfolio-level language unless this repo evidences it directly.
- Treat `UNKNOWN`, `UNVERIFIED`, `INFERRED`, `UPSTREAM_NOT_PRESENT`, and
  data-specific owner-deferred rulings as real states, not as placeholders to
  gloss over.
- A smoke `PASS` is a custody claim, not a science claim.
- An Ops-Gates audit `PASS` is an operational-hygiene claim, not a science
  claim.

## Disputes

If a public statement appears to outrun the evidence surface, open an evidence
dispute and cite the exact file, line, and missing artefact path. SHA-256
mismatches must be raised as disputes — they are never silently corrected.
