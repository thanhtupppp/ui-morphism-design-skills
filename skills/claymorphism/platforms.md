# Claymorphism — Cross-Platform Recipes

## Canonical intent
Use opaque, inflated geometry, soft highlights, and hue-matched shadows for warmth. Content and typography remain crisp and conventional.

## HTML/CSS
- Use large radius/squircle-like geometry, inset highlights, and a bounded outer shadow.
- Keep fields, errors, and focus explicit; decorative depth is supplemental.

## React
- Use semantic HTML and style the component shell with the project's CSS system.
- Keep cards flexible in height so localization and text scaling do not clip content.

## Flutter
- Map the shape to `BorderRadius`/`ShapeBorder` and depth to a small set of `BoxShadow`s.
- Prefer `Material`/standard buttons and fields inside clay containers so semantics and states remain native.
- Avoid recreating CSS inset shadow literally when a simpler layered decoration produces the same visual intent.

## Recipe
Hero/feature card = opaque clay body; button = smaller/high-contrast clay control; form = conventional field inside clay shell; dense lists/tables = Flat surfaces.

## Accessibility/performance
Do not use pastel text as a contrast strategy. Provide solid boundaries when shadows disappear. Limit shadow layers and avoid fixed heights. Reduce effects on small/low-power devices and under reduced motion.
