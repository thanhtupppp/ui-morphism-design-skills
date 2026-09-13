# Liquid Glass — Cross-Platform Recipes

## Canonical intent
Treat translucency, contextual tint, blur, rim/reflection, and grouping as a functional material for navigation and contextual controls—not as wallpaper.

## HTML/CSS
- Build from translucent fill + border + `backdrop-filter` as enhancement.
- Keep hit areas and grouping independent of the visual shape.
- Provide a solid fallback and avoid relying on browser-specific displacement/shader tricks for meaning.

## React
- Keep the effect local to a toolbar/contextual surface.
- Use semantic buttons/links and accessible expanded/collapsed names; CSS controls appearance only.

## Flutter
- Compose `BackdropFilter` + clipped surface + tint/border. Use a stable opaque surface when blur is unavailable or too costly.
- Do not require shader displacement to reproduce the style; contextual depth can be represented with tint, blur, rim and elevation.
- Drag/resize visuals need keyboard/tap alternatives and explicit semantics.

## Motion
Use short opacity/scale/morph transitions. Reflection and distortion are optional and should be static under reduced motion. Never continuously animate a large blurred surface by default.

## Accessibility/performance
Focus must remain visible above the material. Keep blur bounded. Preserve reading order beneath overlays and provide reduced-transparency/static modes where needed.
