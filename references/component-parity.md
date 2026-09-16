# Machine-Readable Component Parity

The repository describes cross-platform component parity with a structured contract and checks example sources for renderer-specific evidence.

`references/component-parity.json` defines the normalized contract for the primary interactive example used by all ten visual styles.

## Required normalized semantics

Every renderer must preserve:

`role → accessible name → state → responsive intent → target size → fallback`

Renderer-specific primitives are allowed. Semantic meaning is not.

## State normalization

The baseline action exposes `default`, `pressed`, and `disabled` state. Additional states such as loading, invalid, or expanded may be added when the component requires them, but must never replace the baseline semantics.

## Enforcement

`scripts/validate-component-parity.mjs` loads the manifest and checks each of the ten styles against renderer-specific evidence. A passing result means the implementation contains concrete signals for the same normalized contract; it does not claim pixel identity or runtime equivalence.

Before reading example sources, the validator requires all four supported renderer objects, non-empty lists of non-blank evidence strings, and boolean `true` for the responsive and fallback requirements. Missing renderers or malformed rule lists fail validation rather than silently skipping coverage.

Source evidence uses substring heuristics. A passing result does not prove that every control has an accessible name, that each baseline state works, or that a rendered target meets its minimum size. Confirm those behaviors in renderer-specific runtime tests and manual accessibility review.

Run `node --test scripts/validate-component-parity.test.mjs` to exercise the valid repository and invalid-manifest regression cases. CI runs this suite alongside the parity validator.

False positives should be corrected by improving the example or the manifest's evidence rules, not by weakening a required semantic field.
