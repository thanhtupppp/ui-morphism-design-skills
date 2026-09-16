# Bento UI Component Recipes

## 1. Core token model
Bento tokens describe **composition**, not surface physics.

```css
:root {
  --um-bento-ui-columns: 12;
  --um-bento-ui-gap: 16px;
  --um-bento-ui-page-padding: 24px;
  --um-bento-ui-card-padding: 24px;
  --um-bento-ui-radius: 24px;
  --um-bento-ui-bg: #f7f8fa;
  --um-bento-ui-surface-1: #ffffff;
  --um-bento-ui-surface-2: #f8fafc;
  --um-bento-ui-border: #e2e8f0;
  --um-bento-ui-ink: #18202a;
  --um-bento-ui-ink-muted: #64748b;
  --um-bento-ui-focus: #1d4ed8;
  --um-bento-ui-target-min: 44px;
}
```

Treat grid gap, outer padding, card padding, radius, and target size as a coordinated family. Do not independently choose a different gap/radius for every tile.

## 2. Canonical grid

```css
.um-bento-grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: var(--um-bento-ui-gap);
  padding: var(--um-bento-ui-page-padding);
  background: var(--um-bento-ui-bg);
}

.um-bento-card {
  min-width: 0;
  padding: var(--um-bento-ui-card-padding);
  border: 1px solid var(--um-bento-ui-border);
  border-radius: var(--um-bento-ui-radius);
  background: var(--um-bento-ui-surface-1);
  color: var(--um-bento-ui-ink);
}
```

`min-width: 0` is important for long headings, metrics, and localized content. The grid should not depend on overflow clipping to make cards fit.

## 3. Card role recipes

### Hero
Use for the primary proposition, result, metric, or CTA.

```css
.um-bento-card--hero {
  grid-column: span 6;
  grid-row: span 2;
}
```

A hero tile may contain media, but text hierarchy must remain clear when media fails to load.

### Supporting

```css
.um-bento-card--supporting { grid-column: span 4; }
```

Use for important secondary information that supports the hero.

### Wide/detail

```css
.um-bento-card--wide { grid-column: span 6; }
```

Use for charts, timelines, richer text, or collections needing more horizontal room.

### Utility

```css
.um-bento-card--utility { grid-column: span 3; }
```

Use for compact actions, small metrics, filters, or links. Do not put essential explanations into a tile that is too narrow to read comfortably.

### Alert
An alert may use a larger span than its visual weight would normally suggest because **importance** is part of layout hierarchy. The alert itself still follows the host application's semantic alert pattern.

## 4. Tile anatomy

A reusable tile should be composed conceptually as:

```text
Tile
├── optional eyebrow / category
├── heading
├── primary content
│   ├── metric / illustration / chart / preview / text
│   └── supporting context
├── optional primary action
├── optional secondary action / overflow
└── state layer
    ├── loading
    ├── empty
    └── error
```

A tile should not become a generic “box that can contain anything.” Its heading and primary content should explain why the tile exists.

## 5. Interactive tile patterns

### Whole-tile link
Use when the tile is one destination.

```html
<a class="um-bento-card um-bento-card--hero" href="/analytics">
  <h2>Analytics</h2>
  <p>View the latest performance summary.</p>
</a>
```

Do not place nested `<button>`/`<a>` controls inside this link.

### Non-interactive card with actions
Use when the tile contains several independent controls.

```html
<section class="um-bento-card" aria-labelledby="team-title">
  <h2 id="team-title">Team</h2>
  <button type="button">Invite</button>
</section>
```

### Selectable tile
Selection should have an explicit indicator such as a border, check icon, or selected label. Color change may reinforce the state but should not carry it alone.

### Expandable tile
Use a real disclosure control. Expansion changes content visibility, not the tile's semantic identity.

## 6. Button and icon action inside a tile

Bento itself does not invent a button style. Use the host design system, but preserve card hierarchy.

```css
.um-bento-card .um-bento-action {
  min-width: var(--um-bento-ui-target-min);
  min-height: var(--um-bento-ui-target-min);
  border-radius: 10px;
}

.um-bento-card :focus-visible {
  outline: 3px solid var(--um-bento-ui-focus);
  outline-offset: 3px;
}
```

Avoid placing tiny icon-only controls in the top-right corner without an accessible name and adequate target size.

## 7. Forms inside Bento
A form can live inside a tile when the form is a contained subtask, such as a filter, quick add, search, or settings snippet.

Do not split one multi-step form across unrelated tiles merely to make the page look more “Bento.”

Recommended anatomy:
`label → field → helper/error → action`

Keep fields visually stable and explicit. The grid should provide grouping; the field still needs normal form semantics.

## 8. Navigation and tabs
Navigation can sit in its own tile or outside the Bento grid. Do not scatter one navigation system across multiple tiles.

Tabs should preserve one related content context. A tab control is not a replacement for arbitrary tile rearrangement.

## 9. Data and charts
Bento works well as the outer composition for dashboard metrics and charts.

Recommended:
- metric card for headline KPI;
- chart tile for trend/detail;
- alert tile for data-quality/system conditions;
- utility tile for filters or shortcuts.

The chart itself needs its own semantics, labels, loading state, empty state, and responsive behavior. Do not treat the chart canvas as decorative content only.

## 10. Loading, empty, and error states

### Loading
Keep the tile footprint stable when practical without imposing a fixed text-bearing height. Use a local skeleton/progress treatment so neighboring tiles do not unexpectedly reflow.

### Empty
Explain what is absent and what the user can do next.

### Error
State the problem plainly and expose retry/recovery when appropriate. Never communicate data failure only by turning the entire tile red.

## 11. Responsive recipes

### Expanded ≥ 1024px
```css
.um-bento-card--hero { grid-column: span 6; grid-row: span 2; }
.um-bento-card--wide { grid-column: span 6; }
.um-bento-card--supporting { grid-column: span 4; }
.um-bento-card--utility { grid-column: span 3; }
```

### Medium 768–1023px
```css
.um-bento-grid { grid-template-columns: repeat(8, minmax(0, 1fr)); }
.um-bento-card--hero,
.um-bento-card--wide { grid-column: span 8; }
.um-bento-card--supporting { grid-column: span 4; }
.um-bento-card--utility { grid-column: span 4; }
```

### Compact ≤ 767px
```css
.um-bento-grid { grid-template-columns: 1fr; }
.um-bento-card,
.um-bento-card--hero,
.um-bento-card--wide,
.um-bento-card--supporting,
.um-bento-card--utility {
  grid-column: auto;
  grid-row: auto;
}
```

The exact breakpoints may be adapted to the host application; the important rule is role remapping rather than geometric shrinking.

## 12. Density levels

### Comfortable
24px page/card padding, 16–24px gaps, larger media and fewer tiles above the fold.

### Standard
16–24px card padding, 16px gaps, normal heading/value spacing.

### Compact
12–16px card padding, 12px gaps, smaller utility content. Do not shrink touch targets to make more tiles fit.

## 13. State matrix

| Component | Default | Hover | Focus | Pressed | Selected | Disabled |
|---|---|---|---|---|---|---|
| Tile link | stable surface | subtle emphasis | solid ring | small feedback | explicit indicator | readable muted state |
| Tile action | host style | host style | host ring | host style | host style | host style |
| Tab | neutral/active | subtle | solid ring | subtle | active indicator | readable |
| Selectable tile | neutral | optional emphasis | ring | small feedback | border/icon/label | reduced affordance |

The Bento layout itself should not jump between states.

## 14. Anti-patterns
- Fixed-height tiles that clip localized or user-generated content.
- Nested whole-card links containing buttons/links.
- `grid-auto-flow: dense` changing visual reading order.
- Equal-size tiles for content with strongly unequal priority.
- Every tile receiving a different material/effect.
- Tiny controls scattered over a decorative image.
- Using tile color alone for success/error/selection.
