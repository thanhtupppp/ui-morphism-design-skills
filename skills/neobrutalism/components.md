# Neobrutalism Component Recipes

## Tokens
```css
:root { --neo-bg: #fef6e4; --neo-surface: #fff; --neo-ink: #0a0a0a; --neo-border: #0a0a0a; --neo-accent: #ffdc58; --neo-shadow: 4px 4px 0 var(--neo-border); --neo-radius: 0px; }
```

## Button, card, input, alert
```css
.neo-card { padding: 24px; border: 3px solid var(--neo-border); border-radius: var(--neo-radius); background: var(--neo-surface); box-shadow: 8px 8px 0 var(--neo-border); }
.neo-button { min-height: 44px; padding: 10px 16px; border: 2px solid var(--neo-border); border-radius: var(--neo-radius); background: var(--neo-accent); color: var(--neo-ink); box-shadow: var(--neo-shadow); }
.neo-button:hover { transform: translate(2px, 2px); box-shadow: 2px 2px 0 var(--neo-border); }
.neo-button:active { transform: translate(4px, 4px); box-shadow: none; }
.neo-button:focus-visible { outline: 3px solid #155e75; outline-offset: 4px; }
.neo-input { min-height: 44px; padding: 10px 12px; border: 2px solid var(--neo-border); border-radius: var(--neo-radius); background: #fff; color: var(--neo-ink); }
.neo-alert { padding: 12px 16px; border: 2px solid var(--neo-border); background: #67e8f9; color: var(--neo-ink); }
```

## Opacity and geometry
Keep primary text and controls fully opaque. Use hard edges and offsets for hierarchy; do not rotate labels, inputs, or error messages. Limit accents to 2–3 per screen and test transformed hit areas.
