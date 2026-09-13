# Liquid Glass — Cross-Platform Implementation Guide

## Canonical visual intent
Liquid Glass is a functional translucent material whose appearance responds to surrounding content and context. Preserve **stable hit areas, grouping, readable content, boundaries, state hierarchy, and semantic behavior** across renderers. Pixel-identical blur/reflection is not a requirement.

## HTML / CSS
- Build the fallback first: opaque/tinted surface, border, and shadow.
- Add `backdrop-filter` only as progressive enhancement.
- Use CSS custom properties for tint, opacity, blur, rim, radius, and shadow.
- Keep blur on the smallest bounded surface; do not filter the whole page.
- Use `prefers-reduced-motion` to freeze decorative morph/reflection.
- Use `forced-colors`/high-contrast fallback with solid surfaces and boundaries.
- Do not require custom shaders or experimental displacement for interaction meaning.

## React
- Keep state and semantics in React/HTML; keep Liquid effects in the presentation layer.
- Use semantic `<button>`, links, dialogs, inputs, and navigation controls inside the material shell.
- Model `expanded`, `selected`, `disabled`, `busy`, and `invalid` explicitly.
- Provide a `reducedEffects` or static mode that removes blur/distortion without changing component behavior.
- For contextual/portal surfaces, explicitly manage stacking, focus, dismissal, and relationship to the anchor content.

## Flutter
- Use `ClipRRect` with `BackdropFilter(ImageFilter.blur(...))` for bounded blur.
- Put the translucent fill, tint, rim, and optional depth in a `DecoratedBox`/`Container` above the filtered backdrop.
- Prefer native semantic widgets (`NavigationBar`, `FilledButton`, `TextField`, `MenuAnchor`, `Dialog`, `BottomSheet`) inside the Liquid shell.
- Do not require shader displacement to qualify as Liquid Glass; tint + bounded blur + rim + contextual grouping are sufficient.
- Provide an opaque/static mode for low-power devices, accessibility settings, or performance budgets.
- Preserve focus, keyboard traversal, semantics, text scaling, and hit targets independently from the material shape.

## React Native / other renderers
- Use the platform's supported blur/material primitive when available.
- Where true backdrop sampling is unavailable, use a tinted translucent/opaque approximation with a clear rim and depth.
- Keep the same semantic state model across renderers.
- Prefer stable approximations over brittle platform-specific shader tricks.

## Portable component mapping
| Intent | HTML/CSS | React | Flutter | Fallback |
|---|---|---|---|---|
| Material shell | div + CSS vars + backdrop filter | visual wrapper | ClipRRect + BackdropFilter + DecoratedBox | opaque surface |
| Rim | border | CSS class | Border | strong border |
| Depth | box-shadow | CSS class | BoxShadow/Material | border + spacing |
| Scrim | overlay | modal layer | ModalBarrier | solid overlay |
| Focus | `:focus-visible` | native focus state | Focus/FocusNode | solid focus ring |
| Selected | aria/state class | React state + aria | selected state | icon/fill/border |
| Morph | transform/size | state-driven transition | AnimatedContainer/implicit animation | instant state |

## State rules
Visual changes are optional enhancements; semantic state is mandatory. Hover must never be required for touch comprehension. Focus must remain visible when the material is translucent.

## Responsive rules
- Prefer one contextual material group over many overlapping surfaces.
- Collapse or scroll toolbars while preserving action order.
- Keep labels and icons within stable target areas during morphing.
- Reduce blur/spread before reducing target size.

## Accessibility
Validate moving/bright/dark backdrops, contrast, grayscale, keyboard, screen reader, text scaling, localization/RTL, reduced motion, reduced transparency/effects, and forced colors/high contrast. Removing the Liquid layer must not remove meaning.

## Performance
Treat blur and distortion as budgeted compositing effects. Bound area and count, avoid nested sampling, avoid continuous large-area animation, and prefer static reflection layers. On constrained devices, fallback in this order: distortion → reflection → blur → translucent fill; retain boundaries, state indicators, and semantics throughout.