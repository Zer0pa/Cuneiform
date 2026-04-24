# Cuneiform Control Results

## Review-Pack Outputs

The staged control lane inherits these upstream review artifacts:

- `05_annotated_sign_benchmark_manifest.json`
- `06_annotated_sign_p8_manifest.json`
- `07_annotated_sign_p8_benchmark.json`
- `08_annotated_sign_p8_1nn_probe.json`

## Best Reported Review-Pack Results

| Surface | Best Result | Interpretation |
|---|---|---|
| Centroid baseline | accuracy `0.003774` | weak signal above null, not a serious gate result |
| 1-NN probe | accuracy `0.028302` | stronger than centroid, still very weak overall |
| Highest macro recall | `0.011798` | confirms the lane is real but underperforming |

## Why The Lane Still Matters

- The benchmark lane is real and sign-labeled.
- The results falsify the current representation strongly enough to justify a
  control-lane preservation pack.
- The lane is useful as known-script validation material even though it is not a
  promotion candidate.

## What These Results Do Not Mean

- They do not close the scientific governing gate.
- They do not justify a flagship repo story.
- They do not justify commercialization or public-release claims.

## Source Basis

- `workspace/share/science_engineering_review_2026-04-10/04_OUTPUTS_AND_RESULTS.md`
- `workspace/share/science_engineering_review_2026-04-10/05_annotated_sign_benchmark_manifest.json`

