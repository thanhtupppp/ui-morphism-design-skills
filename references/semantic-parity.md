# Semantic Parity Contract

## Purpose

A style is cross-platform only when its examples preserve the same semantic anatomy, interaction states, responsive intent, target size, fallback behavior, and accessibility meaning across HTML/CSS, React, Flutter, and React Native.

## Canonical checks

For every style, the implementation seeds must expose:

- a canonical `--um-<style>-...` semantic token namespace in CSS;
- at least one token definition and one `var(--um-<style>-...)` consumption;
- a native/semantic interactive primitive;
- an explicit disabled/pressed/selected/loading/error state marker or documented equivalent;
- responsive adaptation based on available width or layout constraints;
- a primary interactive target of at least 44 CSS px on web and 48 logical px on React Native/Flutter;
- a deterministic fallback that preserves content hierarchy and semantic state when decorative effects are unavailable;
- an accessible name or visible relationship for interactive/form content where applicable;
- a focus/selection/state cue that remains understandable without decorative effects.

## Structured parity

`references/component-parity.json` is the normalized machine-readable contract for the primary interactive component. It maps the invariant semantic fields to renderer-specific evidence without requiring identical primitives or pixel values.

The parity order is:

`role → accessible name → state → responsive intent → target size → fallback`

`scripts/validate-component-parity.mjs` is the enforcement point for this normalized contract.

## Parity rule

Visual details may differ by renderer. Semantic role, content order, state meaning, responsive intent, accessibility behavior, and minimum target size must not silently diverge.

## Accessibility parity

Web examples must retain visible keyboard focus and forced-colors behavior. Flutter and React Native examples must retain native accessibility semantics and explicit interaction state where required. Loading, disabled, selected, pressed, and error states must remain distinguishable without relying on color, blur, shadow, glow, transparency, texture, or animation alone.

## Verification record

Every style seed must retain a short `Verification:` note describing the parity checks performed. Fallback notes must identify which decorative effect can be removed and what remains. Accessibility verification must cover focus, state semantics, target size, and relevant reduced-effect behavior.
