# Neumorphism Component Recipes

## Tokens
```css
:root { --neu-bg: #e6e7ee; --neu-ink: #272b35; --neu-border: #697386; --neu-light: #fff; --neu-dark: #b8b9be; --neu-raised: 8px 8px 16px var(--neu-dark), -8px -8px 16px var(--neu-light); --neu-pressed: inset 5px 5px 10px var(--neu-dark), inset -5px -5px 10px var(--neu-light); }
```

## Button, input, card
```css
.neu-button { min-height: 44px; padding: 10px 16px; border: 1px solid transparent; border-radius: 14px; background: var(--neu-bg); color: var(--neu-ink); box-shadow: var(--neu-raised); }
.neu-button:hover { color: #111827; }
.neu-button:active, .neu-button[aria-pressed="true"] { box-shadow: var(--neu-pressed); }
.neu-button:focus-visible { outline: 3px solid var(--neu-border); outline-offset: 4px; }
.neu-input { min-height: 44px; padding: 10px 12px; border: 1px solid var(--neu-border); border-radius: 12px; background: var(--neu-bg); color: var(--neu-ink); box-shadow: var(--neu-pressed); }
.neu-card { padding: 24px; border-radius: 24px; background: var(--neu-bg); box-shadow: var(--neu-raised); }
.neu-nav { display: flex; gap: 12px; padding: 16px; background: var(--neu-bg); }
```

## Opacity and boundaries
Do not use faint opacity as the only disabled/selected cue. Soft shadows are decorative; labels, borders, outlines, icons, and text must communicate state. Use Neumorphism only for compact controls and keep forms/tables Flat or Material.
