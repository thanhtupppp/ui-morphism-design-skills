# Liquid Glass Component Recipes

## Tokens
```css
:root { --liquid-fallback: #f5f5f7; --liquid-fill: rgb(255 255 255 / .62); --liquid-border: rgb(255 255 255 / .72); --liquid-ink: #111827; --liquid-blur: 20px; }
```

## Toolbar, button, panel
```css
.liquid-toolbar { display: flex; gap: 8px; padding: 8px; border: 1px solid var(--liquid-border); border-radius: 999px; background: var(--liquid-fallback); box-shadow: 0 8px 32px rgb(0 0 0 / .12); }
@supports (backdrop-filter: blur(1px)) { .liquid-toolbar { background: var(--liquid-fill); backdrop-filter: blur(var(--liquid-blur)) saturate(180%); } }
.liquid-button { min-height: 44px; padding: 10px 14px; border: 0; border-radius: 999px; background: transparent; color: var(--liquid-ink); }
.liquid-button:hover { background: rgb(255 255 255 / .36); }
.liquid-button:focus-visible { outline: 3px solid #155e75; outline-offset: 3px; }
.liquid-panel { padding: 24px; border: 1px solid var(--liquid-border); border-radius: 26px; background: var(--liquid-fallback); }
```

## Component rule
Liquid material belongs to navigation and contextual controls. Keep content panels opaque when text or form fields are critical. Provide expanded/collapsed labels and non-drag alternatives for movable controls.
