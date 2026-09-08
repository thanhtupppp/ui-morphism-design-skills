# Bento UI Component Recipes

## Tokens and grid
```css
:root { --bento-gap: 16px; --bento-radius: 24px; --bento-surface: #fff; --bento-border: #e2e8f0; --bento-ink: #18202a; }
.bento-grid { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: var(--bento-gap); }
.bento-card { min-width: 0; padding: 24px; border: 1px solid var(--bento-border); border-radius: var(--bento-radius); background: var(--bento-surface); color: var(--bento-ink); }
```

## Card variants and responsive rules
```css
.bento-card--hero { grid-column: span 6; grid-row: span 2; }
.bento-card--wide { grid-column: span 6; }
.bento-card--small { grid-column: span 3; }
.bento-card:focus-within { outline: 3px solid #2563eb; outline-offset: 3px; }
@media (max-width: 1023px) { .bento-card--hero, .bento-card--wide { grid-column: span 8; } .bento-card--small { grid-column: span 4; } }
@media (max-width: 767px) { .bento-grid { grid-template-columns: 1fr; } .bento-card, .bento-card--hero, .bento-card--wide, .bento-card--small { grid-column: auto; grid-row: auto; } }
```

## Card contract
Every card needs one job, heading, state, and optional action. Keep DOM order equal to task priority; never use `grid-auto-flow: dense` when order affects meaning. Avoid fixed heights and nested interactive cards.
