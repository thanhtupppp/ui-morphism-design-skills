# Glassmorphism — Cross-Platform Implementation Guide

## Canonical visual intent
A translucent tinted plane with bounded backdrop sampling creates a frosted glass layer above a known backdrop. Preserve **layering, readable foreground content, boundary, and state hierarchy** across renderers rather than chasing pixel-identical blur.

## HTML / CSS
- Use semantic HTML for all interactive elements.
- Use `backdrop-filter` as progressive enhancement; always define an opaque fallback first.
- Limit blur to the smallest rounded surface that needs it.
- Use a tint/scrim to stabilize contrast over the backdrop.
- Keep `:focus-visible` above the border and visible on worst-case backgrounds.
- In forced-colors/high-contrast contexts, remove decorative transparency and use solid borders/surfaces.

## React
- Keep glass as a local visual wrapper around semantic components.
- Expose a `reducedEffects`/static mode for users or devices that need less transparency.
- Keep component state independent of CSS effect classes.
- For portals/dialogs, manage focus and layering explicitly; the glass surface must not accidentally sample an unrelated page subtree.

## Flutter
- Use `ClipRRect` + `BackdropFilter(ImageFilter.blur(...))` for bounded surfaces.
- Place a translucent `DecoratedBox`/`Container` over the filtered backdrop so the tint, border, and fill remain explicit.
- Keep the blur region narrow; do not wrap the entire screen in one `BackdropFilter`.
- Use `Material`, `Dialog`, `NavigationBar`, `FilledButton`, `TextField`, and other semantic widgets inside the glass shell where appropriate.
- Provide an opaque mode for accessibility, low-power devices, and environments where the blur cost is unacceptable.

## React Native / other renderers
- Map glass to the renderer's supported blur/material primitive.
- If true backdrop sampling is unavailable or unreliable, use a translucent/tinted opaque surface with border and shadow.
- Do not replace semantics with custom-painted controls just to reproduce the visual effect.

## Component mapping
| Intent | Web | Flutter | Portable fallback |
|---|---|---|---|
| Glass panel | backdrop-filter + tint | BackdropFilter + tint | opaque tinted surface |
| Rim | border | Border | strong border |
| Depth | box-shadow | BoxShadow / Material elevation | border + spacing |
| Scrim | rgba overlay | ModalBarrier/scrim | solid scrim |
| Focus | outline | Focus/FocusNode + border | solid focus ring |
| Selected | indicator/icon/fill | selected state + indicator | explicit icon/border |

## Accessibility
Test bright/dark/saturated/moving backdrops, zoom/text scaling, keyboard traversal, screen readers, reduced motion, forced colors/high contrast, and reduced transparency/effects. Removing blur must not remove meaning.

## Performance
- Bound blur regions.
- Avoid nested backdrop sampling.
- Avoid dozens of large blurred surfaces.
- Prefer shared/static backdrops when possible.
- Disable continuous blur animation.
- Drop blur before dropping functional borders or state indicators.
