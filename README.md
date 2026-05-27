# Cuneiform

> Product-page mirror for `/gnosis/Gnosis-Cuneiform/`.
> Live public repo: [Zer0pa/Cuneiform](https://github.com/Zer0pa/Cuneiform).
> GitHub Markdown cannot reproduce the website typography, CSS, JavaScript, scroll behavior, or live bento layout; this README translates the product page into GitHub-safe Markdown evidence blocks.

## 0. Install / Developer Commands

The product page is the positioning authority. This section is the only retained developer-surface material from the previous root README.

```bash
# 1. Install the smoke surface (zero third-party runtime deps; pytest pulled in for tests)
python -m pip install --upgrade pip
python -m pip install -e . pytest
pytest -q
```

## Product Page Mirror

**Product-page title:** Gnosis-Cuneiform · Evidenced-negative control pack · Zer0pa

**Product-page description:** Gnosis-Cuneiform · negative-control pack · governing 1NN classifier below target at 0.021916 (NO_GO_GOVERNING_GATE_UNMET) · stdlib-only manifest smoke 5/5 invariants PASS · SHA-pinned upstream artefact · no decipherment claimed · PyPI cuneiform-control v0.1.0 · Apache-2.0

### Hero Translation

> 00 · GNOSIS-CUNEIFORM · COMPUTATIONAL MORPHOLOGYRESEARCH-READY · P5 NO-GO Five thousand years of writing, searchable by its shape. Cuneiform morphology, kept honest · Gnosis-Cuneiform · PyPI cuneiform-control v0.1.0 · github.com/Zer0pa/Cuneiform Cuneiform is one of the oldest writing systems on earth — five thousand years of pressed marks in clay. Gnosis-Cuneiform measures the geometry of those signs so archives, classrooms, and museums can look across collections by shape. The first attempt at a governing classifier scored 0.021916 against a 0.6 target, and the score stays on the record. This page is shape infrastructure, not a reading claim, and the image-bearing corpora stay outside the public pack.

## Positioning

| Field | Value |
| --- | --- |
| Section | gnosis |
| Product route | /gnosis/Gnosis-Cuneiform/ |
| Live public repository | https://github.com/Zer0pa/Cuneiform |
| Repo identity used here | Cuneiform |
| Website display identity | Cuneiform |
| Verdict | STAGED |
| Posture | negative_control_preservation |
| Headline metric | pytest -q → 3 passed in 0.04s; 5/5 cross-field invariants holding on real-manifest smoke; 6/6 SHA-256 pinned upstream manifests verified. |
| Honest blocker | The inherited governing gate NO_GO_GOVERNING_GATE_UNMET failed at governing_1nn_accuracy = 0.021916 and remains failed. This lane preserves the negative result as a first-class output. |
| Mechanics asset from product page |  |

## Key Metrics

| Metric | Value | Baseline |
| --- | --- | --- |
| Governing gate | `NO_GO_GOVERNING_GATE_UNMET`; `governing_1nn_accuracy = 0.021916` | `docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md` |
| Manifest smoke | `PASS`; 5/5 invariants OK, 0 schema errors, observed SHA matches pin | `artefacts/smoke/manifest_validation_report.json` |
| Hermetic tests | `pytest -q` -> 3 self-tests; smoke runner is stdlib-only with zero runtime dependencies | `tests/test_smoke_runner.py`, `pyproject.toml` |
| HF custody | 6/6 lane-pinned manifests verified against SHA-256 pins; AP heavy store remains private | `docs/HF_CUSTODY_REGISTER.md`, `artefacts/smoke/hf_upload_verify.json` |

## Proof Anchors

| Path | State |
| --- | --- |
| docs/EXECUTOR_STATUS_REPORT.md | Reviewer landing page |
| SOVEREIGN_PRD.md | Sovereign brief |
| docs/evidence/CUNEIFORM_PHASE2_GATE_STATUS.md | Failed-gate evidence |
| docs/evidence/CUNEIFORM_CONTROL_RESULTS.md | Control-results summary |
| docs/evidence/ARTEFACT_CHECKSUMS.md | Pinned SHA-256 register |
| artefacts/smoke/manifest_validation_report.json | Smoke validation report |
| artefacts/smoke/hf_upload_verify.json | HF upload verify |
| docs/HF_CUSTODY_REGISTER.md | HF custody register |
| docs/PATH_REWRITE_LEDGER.md | Path-rewrite ledger |
| docs/MINIMAL_SMOKE_TARGET.md | Smoke target spec |
| docs/ARCHITECTURE.md | Architecture / truth map |
| AUDITOR_PLAYBOOK.md | Auditor playbook |
| PUBLIC_AUDIT_LIMITS.md | Public audit limits |
| .gpd/STATE.md | Current state |

## What We Prove

- The cuneiform benchmark/control artefact chain is real and pinned. Six upstream manifests are recorded by SHA-256 in `docs/evidence/ARTEFACT_CHECKSUMS.md` and held under private HF custody recorded in `docs/HF_CUSTODY_REGISTER.md`.
- The inherited governing gate failed and remains failed: P5 closed `NO_GO_GOVERNING_GATE_UNMET` at `governing_1nn_accuracy = 0.021916`; P6 (`0.038176`) and P7 (`0.051826`) diagnostics are never promoted to gate closure.
- `SMOKE-01-MANIFEST-VALIDATION` runs and passes against the pinned upstream manifest with all 5 cross-field invariants holding and 0 schema errors.
- The smoke surface is stdlib-only, third-party-dependency-free, and reproducible on any Python >= 3.8 host without provisioning.

## What We Do Not Claim

- We do not claim the failed governing gate is repaired. The smoke is custody-only by construction; it cannot move the gate.
- We do not claim cuneiform decipherment, substrate identification, or any positive scientific recovery on this corpus.
- We do not claim public-release readiness, flagship status, commercial readiness, or cross-domain superiority.
- We do not claim cleared image rights, rights-cleared corpus redistribution, or permission to expose private HF artefact bytes.
- We do not claim proprietary rights over cuneiform, its scripts, or the archaeological record.
- We do not claim that shared geometry, transport, or generic evaluation kernels belong in this repo.

## Blockers / Failures

> The inherited governing gate NO_GO_GOVERNING_GATE_UNMET failed at governing_1nn_accuracy = 0.021916 and remains failed. This lane preserves the negative result as a first-class output.

## Verification Surface

| Code | Check | Verdict |
| --- | --- | --- |
| V-01 | Hermetic self-test: `pytest -q` returns 3 passing tests against bundled fixtures. | PASS |
| V-02 | Real-manifest smoke: checksum, schema, and 5/5 cross-field invariants pass. | PASS |
| V-03 | HF post-upload SHA verify: 6/6 admitted manifest pins match observed hashes. | PASS |
| V-04 | HF custody register: AP heavy store and Zer0pa lightweight surface remain private and token-verified. | PASS |
| V-05 | Operational-leak scan in CI blocks concrete IPs, raw SSH endpoints, local home paths, retired monorepo paths, and pod IDs. | PASS |
| V-06 | Governing science gate remains failed and cannot be repaired by this smoke. | STAGED |
| V-07 | Public redistribution of image-bearing corpora and some derived data remains rights-constrained. | STAGED |

## License

| Field | Value |
| --- | --- |
| License | Apache-2.0+CC-BY-4.0 |
| Authority source | README.md |

## Upcoming Workstreams

| Category | Summary |
| --- | --- |
| Active Engineering | Continue current authority-packet refinement on Gnosis-Cuneiform; surface new receipts as they land. |
| Operations / External Dependency | Maintain CI gates and license-resolver synchronization with Zer0pa/ZPE-License-Commercial. |

## Related Repos

No related repos are declared on the product page frontmatter.

<details>
<summary>Full Visible Product-Page Bento Translation</summary>

This section preserves the product page cells as Markdown text blocks. It intentionally omits shared site navigation, footer chrome, CSS, and scripts.

### Bento Cell 1

> 00 · GNOSIS-CUNEIFORM · COMPUTATIONAL MORPHOLOGYRESEARCH-READY · P5 NO-GO Five thousand years of writing, searchable by its shape. Cuneiform morphology, kept honest · Gnosis-Cuneiform · PyPI cuneiform-control v0.1.0 · github.com/Zer0pa/Cuneiform Cuneiform is one of the oldest writing systems on earth — five thousand years of pressed marks in clay. Gnosis-Cuneiform measures the geometry of those signs so archives, classrooms, and museums can look across collections by shape. The first attempt at a governing classifier scored 0.021916 against a 0.6 target, and the score stays on the record. This page is shape infrastructure, not a reading claim, and the image-bearing corpora stay outside the public pack.

### Bento Cell 2

> 01 · THE GAPSUCCESS-ONLY RECORD Experts catalogue cuneiform sign by sign. Cross-collection search still begins from human memory.

### Bento Cell 3

> 02 · MARKETSADJACENT FORECASTS Cultural heritage digitization'30 · $8.1B Research data management'30 · $6.7B Scholarly infrastructure'30 · $5.3B Digital humanities'30 · $3.2B AI for archaeology'30 · $1.4B source: adjacent research-infrastructure and heritage categories. Sign-shape search is one underbuilt workflow inside them, not a commercial reading service.

### Bento Cell 4

> 03 · VALUE $8.1B Heritage digitization '30; cross-collection sign-shape search is one underbuilt workflow inside that spend.

### Bento Cell 5

> 04 · INSIGHT A cuneiform sign's geometry is a measurable signal.

### Bento Cell 6

> 05.1 · CURRENT TECHMEMORY-BOUND CATALOGUES Digitised tablets become images and catalogue entries. A scholar asking which signs look like this wedge pattern still walks between collections, emails curators, and stitches the answer together from human recall and PDF appendices.

### Bento Cell 7

> 05.2 · OUR TECHPUBLIC CONTROL PACK The cuneiform-control package on PyPI carries the morphology boundary in public: shape metrics, manifest checks, source policy, and the below-target classifier score recorded plainly at 0.021916. Anyone can install it, replay the manifest, and inspect the result without releasing image-bearing corpora or claiming text recovery.

### Bento Cell 8

> 05.3 · BENCHMARKSPHASE-2 RESULT STATUS P5 1NN check0.021916NO-GO Manifest5/5PASS Schema0errors PyPIv0.1.0 P50.021916 · NO-GO P6 diagnostic0.038176 Manifest5/5 PASS Verdict: Governing classifier below target · manifest passes against the SHA-pinned upstream tablet artefact.

### Bento Cell 9

> 06 · MEASUREMENTPHASE-2 RESULT LEDGER One classifier score against one chosen target.

### Bento Cell 10

> 06.1 · RESULT LEDGER · PHASE-2 STATUS P5 · governing 1NN0.021916 · NO-GO P6 · diagnostic0.038176 P70.051826 Manifest5/5 PASS Phase 2 governing score 0.021916 against a 0.6 target. P6 and P7 diagnostics report alongside but do not repair the result. Manifest passes 5/5 against the SHA-pinned 9.28 MB upstream tablet artefact.

### Bento Cell 11

> 07 · KEY METRICSPACK STATUS

### Bento Cell 12

> 07.1 · GOVERNING 1NN CHECK 0.021916 Governing classifier · below 0.6 target, kept public

### Bento Cell 13

> 07.2 · MANIFEST INVARIANTS 5/5 Manifest invariants pass · stdlib-only smoke runner

### Bento Cell 14

> 07.3 · P6 DIAGNOSTIC 0.038176 Diagnostic score only · does not repair the governing result

### Bento Cell 15

> 07.4 · PYPI CONTROL PACK v0.1.0 cuneiform-control on PyPI · Apache-2.0, live 2026-05-04

### Bento Cell 16

> 07.5 · MANIFEST SHA-256 e4d85a…3daa24 9.28 MB upstream artefact · SHA-pinned, verified

### Bento Cell 17

> 08 · DETERMINISMREPLAYABLE PACKET The public packet preserves the same measured boundary.

### Bento Cell 18

> 08.1 · WHAT REPLAYS EXACTLYSHA-PINNED MANIFEST Across two fresh installs, the Phase 2 score (0.021916) hashes identically. The pack validates 5 cross-field invariants with 0 schema errors against the SHA-pinned 9.28 MB artefact, stdlib-only on any Python 3.8+ host. This is not scientific proof of text recovery: the smoke does not re-run the governing 1NN. It proves the public control pack still matches the recorded morphology boundary, byte for byte, so the failed result cannot quietly drift over time.

### Bento Cell 19

> 08.2 · HONEST BLOCKER Honest Blocker · Manifest validation only: the smoke proves shape, not science. It does not repair the classifier result, recover cuneiform text, or release image-bearing corpora. Raw bytes remain private; Traditional-Knowledge protocols, museum image rights, and public-review limits apply. RELEASING.md and .gpd/STATE.md release-state drift pending.

### Bento Cell 20

> 09 ANCIENT SIGNS WITH A SEARCHABLE SHAPE.

### Bento Cell 21

> 09.1 · THIS LAB'S AMBITION The ambition is applied infrastructure for the cuneiform world: measure the geometry of a sign once, then let it travel into catalogue lookup, cross-collection comparison, classroom teaching, and museum metadata — without ever claiming text recovery or releasing image-bearing tablets the field has agreed to protect.

### Bento Cell 22

> 09.2 · WHAT THIS IS Shape-search infrastructure is public, the manifest passes, and the failed classifier score stays on the record.

### Bento Cell 23

> 09.3 · WHAT IT IS NOT The governing classifier missed its 0.6 target. Image-bearing corpora and release-state drift stay outside the pack.

### Bento Cell 24

> 09.4 · ARCHIVES · NEAR-TERM (12–24 MO) Tablet archives gain shape lookup A researcher chasing a wedge pattern across the British Museum, the Louvre, and CDLI no longer relies on memory and email. Sign geometry becomes a queryable field across catalogues, and the answer arrives before the trip is booked.

### Bento Cell 25

> 09.5 · TEACHING · NEAR-TERM (12–24 MO) Cuneiform classrooms see sign families A graduate seminar can group signs by visible form before any language claim enters the room. Students see how wedges relate to wedges, building intuition for variation across scribes, periods, and regions instead of memorising tables.

### Bento Cell 26

> 09.6 · CATALOGUING · MID-TERM (24–48 MO) Museums describe signs by geometry Curators add measured shape descriptors to tablet records alongside provenance and period. Discovery improves for the next generation of scholarship, and the metadata stays honest about what was photographed versus what was read.

### Bento Cell 27

> 09.7 · METHOD · MID-TERM (24–48 MO) Heritage AI keeps its discipline A loud public no-go score makes premature decipherment claims harder to publish unchallenged. Funders, reviewers, and journalists gain a reference for what restraint looks like when an early model misses the threshold its own authors chose.

### Bento Cell 28

> 09.8 · METHOD · PARADIGM (48 MO+) Failed science becomes shared memory Heritage scholarship gains a habit of preserving negative results with the same care as positive ones. A century from now, the next attempt on cuneiform morphology starts from a known floor, not from a forgotten draft, and the field learns faster because of it.

</details>

---

Source mapping: product route `/gnosis/Gnosis-Cuneiform/` -> live public repo `Zer0pa/Cuneiform`. README generated from product-page authority plus retained install/dev commands only.
