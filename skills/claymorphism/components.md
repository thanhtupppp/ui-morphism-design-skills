# Claymorphism Component Recipes

## Tokens
```css
:root { --clay-bg: #f4f1fb; --clay-surface: #cfd4ff; --clay-ink: #24233a; --clay-border: #554d86; --clay-radius: 32px; --clay-shadow: inset 0 10px 18px -6px rgb(255 255 255 / .62), inset 0 -10px 18px -6px rgb(52 42 91 / .32), 0 24px 44px -12px rgb(80 65 150 / .32); }
```

## Button, card, badge, input
```css
.clay-card { padding: 28px; border-radius: var(--clay-radius); background: var(--clay-surface); box-shadow: var(--clay-shadow); }
.clay-button { min-height: 44px; padding: 10px 18px; border: 0; border-radius: 20px; background: #fff; color: var(--clay-ink); box-shadow: 0 5px 12px rgb(80 65 150 / .2); }
.clay-button:active { transform: scale(.98); }
.clay-button:focus-visible { outline: 3px solid var(--clay-border); outline-offset: 4px; }
.clay-badge { display: inline-flex; min-height: 32px; align-items: center; padding: 6px 12px; border-radius: 999px; background: #a7f3d0; color: #064e3b; }
.clay-input { min-height: 44px; padding: 10px 12px; border: 2px solid var(--clay-border); border-radius: 16px; background: #fff; color: var(--clay-ink); }
```

## Component rule
Use clay for expressive objects and empty states; use conventional opaque form controls when information density rises. Pastel opacity must never weaken label, error, or focus contrast.
