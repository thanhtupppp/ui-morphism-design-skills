# Accessibility Parity Contract

## Purpose

Accessibility behavior is part of cross-platform parity. A renderer may change visual treatment, but users must still be able to identify focus, state, relationships, errors, and available actions without relying on color, blur, shadow, glow, transparency, texture, or animation.

## Canonical checks

For every style implementation seed:

- Web CSS exposes a visible `:focus-visible` treatment, a `forced-colors: active` fallback, and reduced-motion behavior.
- Translucent or atmospheric styles provide a reduced-transparency or opaque-surface path when the effect is intentionally removed.
- React uses native semantic interactive elements where available and exposes state through native attributes/props or explicit semantic state markers.
- Flutter uses native interaction controls with platform semantics preserved; primary controls target at least 48 logical px.
- React Native uses native interaction primitives with `accessibilityRole` and/or `accessibilityState`; primary controls target at least 48 px.
- Form fields have an associated visible label or an equivalent accessible naming mechanism; validation state is not conveyed by color alone.
- Loading, disabled, selected, pressed, and error states remain distinguishable when decorative effects are disabled.

## Non-regression rule

Removing an advanced effect must not remove the semantic cue it was decorating. A fallback is valid only when role, name, state, content order, focus visibility, and target size remain understandable.

## Verification record

Every changed example should retain a short `Verification:` note covering focus, state semantics, target size, and the relevant fallback or reduced-effect path.
