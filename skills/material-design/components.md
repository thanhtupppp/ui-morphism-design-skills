# Material Design Component Recipes

## Tokens
```css
:root { --md-bg: #fffbfe; --md-surface: #f7f2fa; --md-ink: #1d1b20; --md-muted: #49454f; --md-primary: #6750a4; --md-outline: #79747e; --md-radius: 999px; }
```

## Button, field, card, dialog
```css
.md-button { min-height: 44px; padding: 10px 18px; border: 0; border-radius: var(--md-radius); background: var(--md-primary); color: #fff; box-shadow: 0 1px 2px rgb(0 0 0 / .2); }
.md-button:hover { box-shadow: 0 2px 6px rgb(0 0 0 / .22); }
.md-button:active { transform: scale(.98); }
.md-button:focus-visible { outline: 3px solid #4f378b; outline-offset: 3px; }
.md-field { display: grid; gap: 6px; color: var(--md-ink); }
.md-field input { min-height: 56px; padding: 16px; border: 1px solid var(--md-outline); border-radius: 4px; background: var(--md-bg); }
.md-field input:focus { border: 2px solid var(--md-primary); outline: 0; }
.md-card { padding: 24px; border-radius: 16px; background: var(--md-surface); box-shadow: 0 1px 3px rgb(0 0 0 / .2), 0 1px 2px rgb(0 0 0 / .14); }
.md-dialog { max-width: 560px; padding: 24px; border: 0; border-radius: 28px; background: var(--md-surface); box-shadow: 0 8px 24px rgb(0 0 0 / .25); }
```

## Component rule
Elevation is a semantic level, not a random shadow. Every field needs label, helper/error text, focus, disabled, and validation states. Dialogs must trap focus and restore it on close.
