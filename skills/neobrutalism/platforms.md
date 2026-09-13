# Neobrutalism — Cross-Platform Recipes

## Canonical intent
High-contrast flat fills, strong borders, bold type, and hard offset shadows communicate directness. Geometry remains structural rather than ornamental.

## HTML/CSS
- Use solid borders and unblurred `box-shadow` offsets.
- Press feedback may translate the control by the shadow amount while preserving target size.
- Keep rotation optional; never rotate labels, fields, or errors.

## React
- Use semantic buttons/links/inputs and CSS for hard offsets.
- Keep focus as a distinct outline from the heavy component border so keyboard focus remains visible.

## Flutter
- Use `BoxDecoration(border: Border.all(...), boxShadow: [...])` with zero blur for the hard shadow.
- Pressed feedback can use a small `Transform.translate`, but the hit target and semantic bounds must not depend on the visual shift.
- Use standard button/field widgets for semantics and wrap them with the visual treatment.

## Responsive/accessibility
Reduce oversized type and remove decorative rotations at narrow widths. Test accent fills for contrast, localization overflow, keyboard traversal, large text, and high-contrast/forced-colors paths.

## Performance
The effect is cheap compared with blur-heavy styles. Keep shadow offsets moderate to avoid overflow/clipping and avoid many nested translated layers.
