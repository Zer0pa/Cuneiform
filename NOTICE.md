# Notice

This is a **private internal repository** owned by Zer0pa. It is not published,
not licensed for third-party use, and not authorized for external mirroring or
redistribution.

## Posture

| Item | Value |
|---|---|
| Visibility | `INTERNAL` (`https://github.com/Zer0pa/Cuneiform`) |
| Licence | `OWNER_DEFERRED` — no public licence is granted |
| Rights reservation | All rights reserved, Zer0pa, 2026 |
| Default branch | `main` |
| Public release | Forbidden until Zer0pa legal rules and the failed governing gate is repaired by an external workstream |

## No Licence Granted

No permissive, source-available, commercial, or research-redistribution licence
is granted by this repository's existence or by any file inside it. The absence
of a `LICENSE` file at root is intentional. The presence of historical files
named `PRIVATE_INTERNAL_LICENSE_NOTICE.md` or any prior `LICENSE_PLACEHOLDER.md`
is **not** a grant.

## Permitted Use

- Internal use, review, and audit by authorized Zer0pa GitHub-org members.
- Internal evidence reproduction by Zer0pa-authorized reviewers.
- Execution of the stdlib-only smoke runner against locally-held inputs within
  authorized compute boundaries.

## Forbidden Until Zer0pa Legal Rules

- Redistribution in any form (source, binary, derived).
- Public hosting or mirroring.
- Inclusion in third-party packages, datasets, or training corpora.
- Pushing the `v0.1.0-internal` git tag to any public or external surface.
- Changing the Hugging Face dataset
  `<HF_ORG>/cuneiform-control-artefacts` visibility from `private`.

## Third-Party Provenance

The repository references — by SHA-256 pin, without vendoring — upstream
cuneiform benchmark and diagnostic artefacts. Those carry their own upstream
rights posture which has not been independently cleared. Any future Zer0pa
licence decision must reconcile this repo with that upstream rights posture.
See `docs/HF_CUSTODY_REGISTER.md` and `docs/evidence/ARTEFACT_CHECKSUMS.md`.

## Reference

`PRIVATE_INTERNAL_LICENSE_NOTICE.md` (kept while the central front-door work
is in progress) carries the longer-form internal licence detail. The
repo-agent review treats this `NOTICE.md` as the root legal posture.

## Removal

When Zer0pa legal selects the canonical licence matrix, this notice is
replaced by the appropriate `LICENSE` file and a changelog entry. Until then,
this notice stands.

— Zer0pa, 2026-04-25
