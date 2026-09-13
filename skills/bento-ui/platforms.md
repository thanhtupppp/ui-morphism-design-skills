# Bento UI — Cross-Platform Recipes

## Canonical intent
Bento is a layout/composition system. It controls grid spans, gaps, hierarchy, and content order; it does not prescribe a material or visual effect.

## HTML/CSS
- Use CSS Grid with explicit semantic spans and stable DOM order.
- Avoid `grid-auto-flow: dense` when it can alter reading/task order.
- Collapse to one or a few columns at compact widths and let content determine height.

## React
- Build cards as independent components with one job, state, heading, and optional action.
- Keep card interaction semantic: a whole-card link should not contain nested buttons/links.
- Use the host project's responsive primitives; the skill defines hierarchy, not breakpoint syntax.

## Flutter
- Use `LayoutBuilder`, `GridView`, `SliverGrid`, `Wrap`, or a responsive layout package already used by the app.
- Define compact/medium/expanded span rules instead of desktop pixel coordinates.
- Preserve semantic/task order in the widget tree even when visual placement changes.

## Recipe
Hero tile = 2–6 column-equivalent span; supporting tile = 2–4; utility = 1–3; alert = high-priority span. Each tile owns loading/empty/error/overflow behavior.

## Accessibility/performance
Avoid fixed-height cards and nested interactive controls. Size images before rendering and lazy-load heavy media. Test 375/768/1024/1440 web widths plus large text/localization and Flutter text scaling.
