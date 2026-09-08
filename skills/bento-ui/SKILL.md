# Bento UI

## Purpose
Bento UI is a content and layout system: modular cards, deliberate grid spans, consistent gaps, and prioritized composition. It is not a surface material by itself.

## Use when
- The page is an overview, portfolio, feature index, dashboard summary, or product landing page.
- Content can be grouped into independent, scannable modules.

## Avoid when
- The task is a sequential form, long-form reading, checkout, or workflow where order is primary.
- Cards would split one cohesive task into many unrelated compartments.

## Visual DNA
- Use a consistent grid, gap, padding, radius, and card anatomy.
- Give high-priority content larger spans; do not make every tile equal.
- Keep one visual material across cards; Bento controls composition, not material physics.
- Prefer meaningful whitespace over excessive card borders and shadows.

## Layout recipe
```css
.um-bento-grid { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 16px; }
.um-bento-card { grid-column: span 4; min-width: 0; border-radius: 24px; padding: 24px; background: var(--um-bento-ui-surface-1); }
@media (max-width: 767px) { .um-bento-grid { grid-template-columns: 1fr; } .um-bento-card { grid-column: auto; } }
```

## Component rules
- Each card has one job, heading, content state, and optional action.
- Define hero, supporting, utility, and alert spans before styling.
- Keep DOM order equal to task priority; do not rely on `grid-auto-flow: dense` for meaning.
- Provide loading, empty, error, and overflow behavior inside each card.

## Accessibility and responsive
- Test 375, 768, 1024, and 1440px widths, zoom, localization, and keyboard order.
- Avoid fixed-height cards for variable text.
- Ensure card links have one clear accessible name and do not create nested interactive controls.

## Performance
The grid itself is cheap; tile contents are not. Size images, lazy-load media, and avoid backdrop-filter on every tile.

## Anti-patterns
- Card soup with no information hierarchy.
- Desktop coordinates that produce nonsense mobile order.
- Treating Bento as permission to hide primary actions inside decorative cards.
