# Bento UI

## Purpose
Bento UI is a **content composition and information-architecture system** built from modular tiles, deliberate spans, consistent gaps, and visible priority. It is not a material effect. A Bento layout can use Flat, Material, Glass, Clay, Aurora, or another surface language underneath it, but the grid hierarchy must remain understandable without that surface styling.

The core question is not “How many cards can fit?” but “Which pieces of information deserve which amount of visual space?”

## How to recognize Bento UI
A correct Bento composition has:
1. A coherent grid or tile system.
2. Repeated spacing and card anatomy.
3. Different tile sizes that communicate importance or content type.
4. Independent modules that can be scanned without losing the overall story.
5. A stable reading/task order that survives responsive changes.

Remove color, shadows, gradients, images, and decorative effects. If the hierarchy of large/small/supporting/utility modules is still understandable, the Bento structure is probably correct.

## Use when
- Product or feature overviews, landing pages, portfolios, dashboards, analytics summaries, control centers, profile summaries, media libraries, or modular settings overviews.
- Information naturally separates into independent modules with different importance.
- The composition benefits from a strong “overview first, drill down second” reading pattern.

## Avoid when
- The task is fundamentally sequential: checkout, step-by-step wizard, long form, legal text, article, documentation, or an uninterrupted editor.
- One operation requires several controls to be perceived as one cohesive work area.
- Tile boundaries would create artificial fragmentation or repeatedly force users to hunt across cards.

## Bento is hierarchy, not decoration
Do not choose spans because they “look dynamic.” Choose them from content priority and expected information density.

Recommended conceptual roles:
- **Hero**: primary outcome, key metric, product proposition, or dominant CTA.
- **Supporting**: secondary insight or feature that reinforces the hero.
- **Utility**: small controls, links, compact metrics, filters, or quick actions.
- **Alert**: important warning/error/system condition that deserves immediate visibility.
- **Detail**: richer content that can take more vertical space without becoming the page hero.

A page may use fewer than all roles. Every tile should have a reason for its size.

## Layout model
Use a logical grid rather than a collection of absolute coordinates.

Canonical 12-column desktop model:
- Hero: 6–8 columns, often 1–2 row units tall.
- Supporting: 4–6 columns.
- Utility: 2–4 columns.
- Full-width alert/detail: 8–12 columns when priority requires it.

These are starting ranges, not immutable numbers. The same semantic role may map to 4, 6, or 12 columns depending on viewport, density, and content.

Preserve:
- consistent outer padding;
- one primary gap token;
- predictable internal card padding;
- minimum readable width;
- stable alignment lines;
- explicit tile ownership of content and state.

Avoid absolute positioning and desktop-only coordinates for core content.

## Tile anatomy
A robust tile normally follows this order:

**container → eyebrow/label → heading → primary content → supporting context → action/status → overflow**

Not every tile needs every layer, but the hierarchy must be deliberate.

The tile contract:
- one primary job;
- one clear accessible name;
- one obvious primary result or message;
- optional supporting metadata;
- optional action;
- explicit loading/empty/error state;
- optional overflow only when it is not competing with the primary action.

Keep titles and key values close together. Do not put the only explanation in hover-only UI.

## Interaction rules
A Bento tile may be informational, interactive, or mixed, but its interaction model must be obvious.

### Clickable tile
Use one semantic link/button for a tile whose entire surface performs one action. Do not place nested links or buttons inside that same interactive surface.

### Mixed tile
The tile itself is not interactive; individual controls inside it are. This is appropriate for dashboards where a card contains a metric plus filters or a button.

### Expandable tile
Use an actual disclosure/expansion behavior with a visible affordance and preserved focus/order. Expansion must not depend on hover.

### Drag/reorderable tile
Drag is an enhancement, not the only means of reordering. Provide keyboard/touch alternatives or an equivalent menu action where reordering is meaningful.

## State model
Every production Bento tile should define:

| State | Expected cue |
|---|---|
| Default | Stable surface, hierarchy unchanged |
| Hover | Subtle emphasis only; do not resize surrounding tiles |
| Focus | High-contrast focus ring on interactive element or tile |
| Pressed | Small visual response; maintain dimensions |
| Selected | Explicit border/indicator/text, not color alone |
| Disabled | Reduced affordance while preserving readable label/state |
| Loading | Skeleton/progress inside the tile footprint when useful |
| Empty | Explain what is missing and what action is possible |
| Error | Explicit message/icon + recovery action where appropriate |
| Overflow | Menu/secondary action that does not obscure primary content |

Never move grid geometry on hover merely to create a dramatic effect.

## Responsive strategy
Responsive Bento is a **role remapping problem**, not simply “shrink every card.”

### Compact
- Collapse to one column when tiles become narrower than their content minimum.
- Preserve DOM order from highest task priority to lower priority.
- Remove decorative spans/row heights that no longer communicate value.
- Let content determine height.

### Medium
- Use 2–8 logical columns depending on available width.
- Keep hero/supporting relationships visible.
- Avoid forcing tiny utility cards beside large text-heavy cards.

### Expanded
- Use the full grid to communicate hierarchy.
- Align important edges and baselines.
- Allow hero content to breathe without making utility information visually dominant.

Do not rely on `grid-auto-flow: dense` when visual packing can change meaning or reading order.

## Grid and content rules
- Use `minmax(0, 1fr)` to prevent long content from expanding the grid unexpectedly.
- Allow variable height where content varies.
- Give media an explicit aspect ratio or intrinsic dimensions.
- Keep text containers wide enough for expected localization.
- Avoid cards so small that headings wrap into awkward two-to-four-line fragments.
- Avoid a dozen unrelated tiny cards when 3–6 coherent modules would communicate better.

## Material relationship
Bento does not define the surface physics.

Possible combinations:
- Bento + Flat: strongest for dashboards and data summaries.
- Bento + Material: strongest for system/product overview flows.
- Bento + Glass: useful for controlled, visual landing pages; keep dense content opaque.
- Bento + Aurora: use Aurora behind the composition, not as a different gradient on every tile.
- Bento + Clay: useful for playful feature/education layouts.

Do not mix multiple competing surface languages just because the grid contains multiple tiles.

## Accessibility
- Preserve semantic DOM/widget order even when visual placement changes.
- Never require hover to discover a control or state.
- Keep focus visible against every tile surface.
- Do not communicate status by tile color alone.
- Test large text, browser zoom, text scaling, localization, and keyboard navigation.
- Avoid nested interactive descendants inside a single clickable tile.
- Ensure an entire tile link has a meaningful accessible name.

## Performance
The grid layout is usually inexpensive; tile content can be expensive.

Prioritize:
- correctly sized images;
- lazy loading below the initial viewport;
- limited video/animation tiles;
- avoiding blur/backdrop effects on every tile;
- avoiding layout-thrashing resize logic;
- virtualization for genuinely large repeated collections rather than for a small marketing grid.

## Implementation checklist
Before shipping a Bento page, verify:
- [ ] Every tile has a clear semantic role.
- [ ] Spans reflect content priority.
- [ ] DOM order reflects task/reading priority.
- [ ] Card heights are not fixed unnecessarily.
- [ ] Loading/empty/error behavior exists for dynamic data.
- [ ] No nested interactive controls inside whole-tile links/buttons.
- [ ] Compact layout is still understandable without desktop spans.
- [ ] Focus and status are visible without relying on color or hover.
- [ ] Heavy media is sized/lazy-loaded appropriately.

## Anti-patterns
- **Card soup**: many equal cards with no hierarchy.
- **Random masonry**: arbitrary placement that destroys scan order.
- **Desktop coordinates**: absolute positions that collapse badly on mobile.
- **Span theater**: changing sizes for visual novelty without content reason.
- **Interaction ambiguity**: unclear whether the card, an icon, or a nested button is clickable.
- **Tiny tile syndrome**: important content squeezed into decorative small cards.
- **Bento as a material**: treating the grid itself as permission to add unrelated shadows, glass, gradients, or clay effects everywhere.