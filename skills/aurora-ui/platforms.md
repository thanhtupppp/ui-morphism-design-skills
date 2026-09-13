# Aurora UI — Cross-Platform Recipes

## Canonical intent
Aurora is an atmospheric background/emphasis system. It supplies mood behind stable content surfaces and is never the sole status or hierarchy signal.

## HTML/CSS
- Prefer isolated pseudo-elements or dedicated background layers with radial gradients.
- Animate only slow transform/opacity; respect `prefers-reduced-motion`.
- Keep text and controls on stable surfaces with tested contrast. Hide decorative gradients in forced-colors mode.

## React
- Implement Aurora as a page/background layer, not a styling rule copied onto every component.
- Pause or simplify non-essential animation when the document is hidden or reduced-motion is requested.

## Flutter
- Use `DecoratedBox`/`Container` gradients for static aurora.
- For dynamic ambient effects, prefer a bounded `CustomPaint`/gradient layer behind content, with a static gradient or solid fallback.
- Never blur a subtree containing text/controls just to achieve atmosphere.

## Component boundaries
Hero/background = Aurora; card = neutral/opaque; button/input = semantic solid controls; status = semantic color + label/icon.

## Performance/accessibility
Limit blur area, color stops, and animated layers. Test worst-case contrast at every focal region. Keep the UI functional when the Aurora layer is removed entirely.
