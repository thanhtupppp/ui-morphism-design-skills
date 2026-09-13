# Neumorphism — Cross-Platform Implementation Guide

## Canonical visual intent
Render a control as part of one continuous surface. The raised/recessed illusion comes from **paired soft light/dark depth cues**. Do not depend on exact pixel parity across renderers; preserve the visual meaning and state hierarchy.

## HTML/CSS
- Raised state: paired outer `box-shadow`.
- Recessed/pressed state: paired `inset` shadows.
- Focus: explicit `outline` or strong border; never shadow-only.
- Selected/checked: use semantic attributes such as `aria-pressed`, `:checked`, and visible icon/text/indicator cues.
- Keep blur and shadow radii bounded to controls; avoid applying the effect to whole-page containers.
- Use an opaque Flat fallback for forced-colors or environments where shadows are unreliable.

## React
- Prefer native `<button>`, `<input>`, `<select>`, checkbox/radio semantics and compose the visual shell around them.
- Keep state in React behavior/props; do not infer state from visual shadow classes alone.
- Map states to semantic class names such as `is-selected`, `is-invalid`, `is-disabled`, while retaining the native/ARIA state.

## Flutter
- Use `Container`/`DecoratedBox` with `BoxDecoration` and bounded `BoxShadow` lists for raised surfaces.
- Flutter does not expose CSS `inset` box-shadow directly. Approximate recessing with layered containers, internal gradients, borders, or a custom `DecoratedBox`; use the simplest construction that preserves the intended visual depth.
- Keep `Switch`, `Checkbox`, `Radio`, `Slider`, `TextField`, `FilledButton`, and related controls semantically native whenever possible.
- For focus, use `Focus`/`FocusNode` and a visible border/outline state instead of relying on shadow changes.
- For rotary controls, expose a non-rotary keyboard/touch alternative and semantics for current value.

## React Native / other renderers
- Map raised depth to the platform's bounded shadow/elevation primitives.
- If inset depth cannot be reproduced reliably, use a flatter surface plus border/indicator rather than a visually unstable approximation.
- Keep the semantic state independent from the renderer-specific shadow implementation.

## Shared state matrix
| State | Primary cue | Secondary cue |
|---|---|---|
| Default | raised surface | paired soft shadows |
| Hover | subtle contrast/translation | shadow adjustment |
| Pressed | recessed/pressed | short translation |
| Selected | check/icon/indicator/state text | recessed depth |
| Focus | high-contrast ring/border | existing depth |
| Disabled | reduced affordance + readable content | reduced decoration |
| Error | text/icon/border | optional depth |

## Responsive rules
- Keep touch targets at the platform policy minimum.
- On small screens, reduce decorative shadow size before reducing functional control size.
- Never use fixed-height containers that clip translated/localized text.
- Move dense data views to Flat/Material treatment.

## Accessibility/fallback rules
- Shadow is never the only state signal.
- Test keyboard navigation, screen readers, text scaling, contrast, grayscale, forced-colors/high-contrast, reduced motion, and localization.
- Offer reduced-transparency/flat mode when the product is used for extended periods and the soft-depth treatment causes readability problems.

## Performance rules
- Prefer 1–2 shadow layers per surface.
- Avoid large blur radii and hundreds of simultaneously shadowed list rows.
- Do not continuously animate shadows.
- For constrained devices, drop decorative depth before dropping interaction feedback or semantic indicators.
