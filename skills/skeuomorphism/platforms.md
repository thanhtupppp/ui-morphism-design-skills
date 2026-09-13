# Skeuomorphism — Cross-Platform Recipes

## Canonical intent
Simulate a bounded physical object with material, bevel, highlight, contact shadow, and a consistent light direction. Physical cues supplement labels and state.

## HTML/CSS
- Prefer gradients, inset/outset shadows, borders, and small texture assets over large raster backgrounds.
- Keep realistic treatment inside bounded controls/modules.
- Focus uses an explicit outline; `:active` may add inset shadow/translation.

## React
- Reuse the HTML semantics and CSS recipe; React supplies component composition, not a different visual language.
- Keep knobs/sliders backed by native or accessible controls, with the visual shell layered around them.

## Flutter
- Use `DecoratedBox`/`Container` with `BoxDecoration`, linear gradients, borders, and a small number of `BoxShadow`s.
- For knobs/dials, expose value and increment/decrement semantics; prefer `Slider`/`Focus`/keyboard actions with a custom visual shell over an inaccessible painted-only control.
- Use `PhysicalModel`/`Material` only when its elevation semantics are useful; do not replace explicit focus with shadow.

## Recipe
Surface = material body + edge token + one light direction. Button = explicit label/state + bevel; Card = bounded device module; Input/table = flat opaque inner surface.

## Accessibility/performance
Textures are decorative and can disappear in forced-colors/reduced-data contexts. Provide keyboard alternatives for rotary gestures. Optimize/lazy-load assets and avoid animating grain or large shadows.
