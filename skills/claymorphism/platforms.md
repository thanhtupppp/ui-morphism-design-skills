# Claymorphism — Cross-Platform Implementation Guide

## Canonical visual intent
Claymorphism represents an **opaque, inflated object**. Its own body color is stable; volume comes from soft highlights, subtle inner shading, large rounded geometry, and a bounded hue-matched outer shadow. Preserve this intent across renderers instead of chasing pixel-identical shadows.

## HTML / CSS
- Use semantic HTML for buttons, fields, links, navigation, dialogs, lists, and tables.
- Use `border-radius`/rounded geometry, gradients or layered backgrounds for highlight/shade, and bounded `box-shadow` for volume.
- Keep the clay body opaque unless a different style is explicitly selected.
- Use `:focus-visible` with a strong outline above decorative depth.
- Keep inputs, labels, errors, and status indicators conventional when density rises.
- Respect forced-colors and provide a solid-boundary fallback.

## React
- React owns component composition and state; CSS owns clay material tokens.
- Preserve native/semantic controls underneath the clay visual shell.
- Use explicit props/state for `disabled`, `selected`, `invalid`, `loading`, and `expanded` rather than inferring state from shadow classes.
- Keep cards flexible in height so localization and user text scaling can expand naturally.

## Flutter
- Map clay geometry to `BorderRadius`/`RoundedRectangleBorder` or a suitable `ShapeBorder`.
- Use `DecoratedBox`/`Container` with a small number of `BoxShadow`s for outer volume and layered decoration for highlights.
- Prefer `FilledButton`, `OutlinedButton`, `TextField`, `Checkbox`, `Radio`, `Switch`, `Slider`, `Dialog`, `NavigationBar`, and other semantic widgets inside clay shells.
- Do not attempt to reproduce CSS inset shadows literally when a simpler layered decoration communicates the same volume.
- Use `ThemeData`/`ThemeExtension` for semantic clay tokens and `Focus`/`FocusNode` for focus styling.

## React Native / other renderers
- Map the opaque surface to the renderer's rounded container/card primitive.
- Map depth to the platform's bounded shadow/elevation API.
- Approximate internal highlight/shading with gradients or layered views only when supported.
- If shadow fidelity is poor, preserve the body shape, color, border, and state indicator rather than adding unstable renderer-specific effects.

## Component mapping
| Intent | Web | Flutter | Portable fallback |
|---|---|---|---|
| Clay body | opaque background + radius | Container/DecoratedBox | opaque rounded surface |
| Outer volume | box-shadow | BoxShadow | border + spacing |
| Inner highlight | inset/gradient layer | layered decoration | lighter top edge |
| Inner shade | inset/gradient layer | layered decoration | darker lower edge/border |
| Focus | outline | Focus/FocusNode + border | strong solid ring |
| Selected | indicator/icon/fill | selected + indicator | explicit border/icon |
| Error | text/icon/border | errorText + border/icon | semantic color + text |

## Responsive
- Reduce shadow spread and decorative illustration size on small screens.
- Allow cards to grow vertically.
- Never sacrifice readable text wrapping to preserve a perfect pill/squircle.
- Keep clay concentrated on hero/feature/primary objects when screen density becomes high.

## Accessibility
Clay depth is decorative. It must not be the only indication of focus, selected state, error, or disabled state. Validate contrast, keyboard/screen-reader semantics, text scaling, grayscale, high contrast/forced colors, reduced motion, and localization.

## Performance
- Keep shadow layers bounded and small in count.
- Avoid deep shadow stacks on repeated list items.
- Do not continuously animate shadows.
- Lazy-load large illustrations.
- Drop decorative depth before functional feedback on constrained devices.
