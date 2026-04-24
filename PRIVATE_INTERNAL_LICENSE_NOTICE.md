# Private Internal License Notice

**Status:** `OWNER_DEFERRED`. No public licence is granted.

## Scope

This notice applies to everything in the `Zer0pa/Cuneiform` repository:

- code under `code/` and `tests/`,
- all documentation (`README.md`, `SOVEREIGN_PRD.md`, `docs/`, `docs/migration/`),
- evidence artefacts (`artefacts/`, `docs/evidence/`),
- the GPD pack (`.gpd/`),
- the inherited benchmark/control material referenced here by SHA-256 pin.

## Grant

**No public or third-party licence is granted** unless and until a licence file
is explicitly added to this repository by Zer0pa. The presence of
`LICENSE_PLACEHOLDER.md` is **not** a grant.

The current rights reservation is: all rights reserved, Zer0pa, 2026.

## Permitted Use

- Internal use by Zer0pa org members with authorised GitHub `Zer0pa/Cuneiform`
  access.
- Internal review, audit, and evidence reproduction by Zer0pa-authorised
  reviewers.
- Execution of the stdlib-only smoke runner against a locally-held copy of the
  pinned manifest, within authorised compute boundaries.

## Forbidden Use Until A Licence Is Chosen

- Redistribution in any form (source, binary, derived).
- Public hosting or mirroring.
- Inclusion in third-party packages, datasets, or training corpora.
- Pushing the `v0.1.0-internal` git tag to any public or external surface.
- Changing the Hugging Face dataset `<HF_ORG>/cuneiform-control-artefacts`
  visibility from `private`.
- Publishing any derived metric, benchmark, or result to external venues under
  attribution to this repo without a signed agreement.

## Third-Party Provenance

The repository references — by SHA-256 pin, without vendoring — upstream
cuneiform benchmark and diagnostic artefacts. These artefacts carry their own
upstream rights posture which has not been independently cleared. Any future
licence decision must reconcile this repo's licence with the upstream rights.

## Legal / Commercial Questions Reserved For Zer0pa Legal

See `docs/LEGAL_BOUNDARIES.md` and the closeout brief for the full list of
open legal questions (code licence, docs licence, dataset licence, model-weight
distribution, third-party provenance, trademark, internal systems).

## Removal

When Zer0pa legal chooses a licence matrix, this notice will be replaced by
the appropriate `LICENSE` file and a short changelog entry. Until then, this
notice stands.

— Zer0pa, 2026-04-24
