# Flat Design Component Recipes

## Tokens
```css
:root { --flat-bg: #f7f8fa; --flat-surface: #fff; --flat-ink: #18202a; --flat-muted: #52606d; --flat-border: #d7dde5; --flat-primary: #2563eb; --flat-danger: #b91c1c; --flat-radius: 8px; }
```

## Button, input, card
```css
.flat-button { min-height: 44px; padding: 10px 16px; border: 0; border-radius: var(--flat-radius); background: var(--flat-primary); color: #fff; }
.flat-button:hover { background: #1d4ed8; }
.flat-button:active { background: #1e40af; }
.flat-button:disabled { opacity: .55; cursor: not-allowed; }
.flat-button:focus-visible { outline: 3px solid #1e3a8a; outline-offset: 3px; }
.flat-input { min-height: 44px; width: 100%; padding: 10px 12px; border: 1px solid var(--flat-border); border-radius: var(--flat-radius); background: var(--flat-surface); color: var(--flat-ink); }
.flat-input:focus { border-color: var(--flat-primary); outline: 3px solid rgb(37 99 235 / .28); }
.flat-card { padding: 24px; border: 1px solid var(--flat-border); border-radius: 12px; background: var(--flat-surface); }
.flat-nav { display: flex; gap: 16px; padding: 12px 16px; border-bottom: 1px solid var(--flat-border); background: var(--flat-surface); }
.flat-nav a[aria-current="page"] { color: var(--flat-primary); font-weight: 700; text-decoration: underline; text-underline-offset: 5px; }
```

## Opacity rule
Use opacity only for disabled/non-interactive decoration. Never make body text or an active control faint to create hierarchy; use color roles and spacing instead.
