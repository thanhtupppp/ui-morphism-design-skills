# Bento UI — Cross-Platform Implementation Contract

## Canonical intent
Bento is a **layout and composition system**, not a material. Its visual identity comes from modular information architecture: a shared grid, meaningful spans, consistent gaps, predictable card anatomy, and deliberate priority. The selected material (Flat, Material, Glass, etc.) is supplied separately.

The portable invariant is:
`content priority → semantic tile role → grid/span decision → responsive reflow → platform layout primitive`.

Do not force identical pixel coordinates across renderers. Preserve hierarchy, reading order, interaction semantics, density intent, and component states.

## Role model
Define each tile before writing layout code:

- **Hero:** primary message, KPI, feature, or action; usually the largest visual span.
- **Supporting:** important secondary content; medium span.
- **Utility:** compact controls, metadata, filters, shortcuts, or small KPIs.
- **Alert/status:** important transient or persistent state; span follows urgency, not decoration.
- **Detail/media:** supporting visual or content module; size follows the content's aspect ratio and priority.

Every tile should declare `role`, `priority`, `contentDensity`, `interaction`, `state`, and `responsiveSpan` (or equivalent) before rendering.

## Grid contract
Use a logical grid rather than a desktop coordinate collage.

Recommended web starting point:
- wide: 12 columns;
- medium: 6–8 columns;
- compact: 1–2 columns, depending on content.

The exact column count is adaptable. Gap, outer gutter, and minimum readable tile width are the important invariants.

Do not depend on `grid-auto-flow: dense` when visual packing can change reading or task order. CSS placement may rearrange appearance, but DOM/source order remains the source of truth for meaning and keyboard traversal.

## HTML/CSS
Use CSS Grid for two-dimensional Bento compositions.

Prefer explicit role classes or data attributes:

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: 16px;
}

.bento-tile--hero { grid-column: span 6; }
.bento-tile--supporting { grid-column: span 3; }
.bento-tile--utility { grid-column: span 3; }

@media (max-width: 1023px) {
  .bento-grid { grid-template-columns: repeat(6, minmax(0, 1fr)); }
  .bento-tile--hero { grid-column: span 6; }
  .bento-tile--supporting { grid-column: span 3; }
  .bento-tile--utility { grid-column: span 3; }
}

@media (max-width: 767px) {
  .bento-grid { grid-template-columns: 1fr; }
  .bento-tile--hero,
  .bento-tile--supporting,
  .bento-tile--utility { grid-column: auto; }
}
```

Let tile height be content-driven unless the product explicitly requires a fixed visual ratio. For media tiles, reserve intrinsic aspect-ratio space to reduce layout shift.

## React
Separate **composition data** from the tile component.

The grid should receive semantic tile definitions such as:

```ts
type BentoTile = {
  id: string;
  role: 'hero' | 'supporting' | 'utility' | 'alert' | 'detail';
  priority: number;
  state: 'ready' | 'loading' | 'empty' | 'error';
  span: { compact: number; medium: number; expanded: number };
};
```

Keep source order in the array equal to task/content priority. Do not build accessibility around CSS `order` changes. A whole-card click target should be one semantic link/button; do not nest additional links or buttons inside it.

Use React for state, data, and interaction behavior; keep grid geometry in CSS or the project's responsive layout primitive.

## Flutter
Map the same tile roles into Flutter's layout primitives instead of simulating CSS Grid coordinates.

Preferred options:
- `LayoutBuilder` for compact/medium/expanded decisions;
- `GridView`/`SliverGrid` for regular grids;
- `CustomScrollView` + slivers for long dashboards;
- `Wrap` for small adaptive groups where equal row structure is not required.

For irregular Bento compositions, use explicit layout delegates or responsive composition rules only when the reading order remains obvious. Avoid using absolute positioning as the primary layout model.

Keep the semantic widget tree in priority order even when visual placement differs. Use standard interactive widgets for buttons, links, menus, fields, and controls.

## React Native and other renderers
Use the renderer's native grid/flex primitives or a maintained layout library already used by the product. Map the same semantic role/spans to supported primitives. When arbitrary CSS Grid spans are unavailable, use deterministic row/column grouping rather than forcing a pixel-perfect imitation.

The fallback is always a simpler grid, not a loss of hierarchy.

## Responsive transformation rules
Bento should **recompose**, not merely shrink.

Expanded → medium → compact:
1. preserve hero/primary content;
2. reduce column spans and tile count per row;
3. merge or stack related modules;
4. move secondary utilities below primary content when needed;
5. allow content-driven height and wrapping;
6. preserve semantic/task order.

A compact layout can intentionally use a different span structure from desktop. Do not reserve empty desktop cells merely to preserve a screenshot.

## Interaction contract
A tile can be:
- static informational;
- a single whole-tile link/action;
- a container holding multiple independent controls.

Choose one interaction model per tile. A tile containing multiple controls must not masquerade as one giant button/link.

States belong to the tile's semantic control or content, not to its position in the grid:
`default → hover (pointer) → focus-visible → pressed → selected → disabled → loading → error/success where applicable`.

Focus must remain visible even when the tile has no border or when the material is decorative.

## Accessibility
- Source order must communicate the same priority as visual order.
- Avoid nested interactive controls.
- Do not encode meaning with tile color/size alone.
- Support large text, localization, zoom/text scaling, keyboard traversal, and screen-reader names.
- A linked tile needs one clear accessible name; supplementary metadata should not become accidental extra links.
- Do not use fixed tile heights that clip translated or enlarged text.
- Test compact widths around 375px, tablet around 768px, desktop around 1024px, and wide desktop around 1440px on web; validate compact/medium/expanded layouts on Flutter.

## Performance
The grid algorithm is usually inexpensive compared with tile content. Optimize the contents:
- size and reserve media dimensions before loading;
- lazy-load offscreen heavy images/video;
- virtualize long dashboard lists when supported;
- avoid backdrop blur or large filters on every tile;
- avoid excessive nested shadows/borders supplied by the chosen material;
- do not render decorative media solely to communicate tile priority.

## Material separation
Bento can be combined with another visual style, but only one material language should govern the tiles unless a deliberate supporting style is documented.

Examples:
- Bento + Flat: solid cards, strong spacing, minimal decoration.
- Bento + Material: elevation/state layers remain subordinate to layout.
- Bento + Glass: use glass selectively; do not blur every tile.
- Bento + Aurora: aurora remains a background/focal accent, not a different material per tile.

## Verification checklist
- [ ] Each tile has one clear semantic role and priority.
- [ ] Desktop composition can be removed and rebuilt without changing source order.
- [ ] Hero/supporting/utility hierarchy remains obvious at compact width.
- [ ] No fixed-height tile clips large text or localization.
- [ ] Whole-tile and multi-control interaction models are not mixed.
- [ ] Loading/empty/error/overflow states exist for data-bearing tiles.
- [ ] Unsupported span features fall back to a simpler grid.
- [ ] The selected material remains consistent across tiles.
- [ ] The grid works with keyboard, screen reader, touch, zoom, and text scaling.
