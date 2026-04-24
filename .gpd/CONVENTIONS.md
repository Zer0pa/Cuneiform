# Conventions

- Workspace root: the repository root of a fresh checkout of
  `Zer0pa/Cuneiform`.
- Authority metric: `control_truth_preserved`.
- Governing source verdict: `NO_GO_GOVERNING_GATE_UNMET`.
- Governing metric value to preserve: `governing_1nn_accuracy = 0.021916`.
- Public posture: blocked/private control pack until the failed gate changes on
  evidence.
- Data rule: derived summaries and manifests first; no raw image-bearing corpus
  release without rights clearance.
- Boundary rule: cuneiform-specific rerun/control code may enter this lane;
  generic benchmark logic stays in methods workstreams.
- Reporting rule: no interim reporting unless a phase cannot be resolved from
  repo-local and source-repo evidence.
- Path scrubbing rule: operational paths and endpoints in authored docs are
  parameterized with symbolic placeholders (`<LOCAL_MONOREPO_ROOT>`,
  `<RUNPOD_HOST>`, `<HF_ORG>`, `<POD_ID>`, `<RUNPOD_CONTAINER>`). Scientific
  provenance (SHA-256s, filenames, metric values, HF revisions, git commit
  hashes) is never scrubbed.
