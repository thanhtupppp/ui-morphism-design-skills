# Machine-Readable Component Parity

The repository treats cross-platform component parity as a structured contract, not a keyword convention.

`references/component-parity.json` defines the normalized contract for the primary interactive example used by all ten visual styles.

## Required normalized semantics

Every renderer must preserve:

`role → accessible name → state → responsive intent → target size → fallback`

Renderer-specific primitives are allowed. Semantic meaning is not.

## State normalization

The baseline action exposes `default`, `pressed`, and `disabled` state. Additional states such as loading, invalid, or expanded may be added when the component requires them, but must never replace the baseline semantics.

## Enforcement

`scripts/validate-component-parity.mjs` loads the manifest and checks each of the ten styles against renderer-specific evidence. A passing result means the implementation contains concrete signals for the same normalized contract; it does not claim pixel identity or runtime equivalence.

False positives should be corrected by improving the example or the manifest's evidence rules, not by weakening a required semantic field.
