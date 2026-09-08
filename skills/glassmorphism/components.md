# Glassmorphism Component Recipes

## Tokens
```css
:root { --glass-fallback: #202331; --glass-fill: rgb(255 255 255 / .14); --glass-border: rgb(255 255 255 / .42); --glass-ink: #fff; --glass-blur: 20px; --glass-radius: 20px; }
```

## Surface, button, input, modal
```css
.glass-surface { padding: 24px; color: var(--glass-ink); border: 1px solid var(--glass-border); border-radius: var(--glass-radius); background: var(--glass-fallback); box-shadow: 0 8px 32px -8px rgb(0 0 0 / .38); }
@supports (backdrop-filter: blur(1px)) { .glass-surface { background: var(--glass-fill); backdrop-filter: blur(var(--glass-blur)) saturate(160%); } }
.glass-button { min-height: 44px; padding: 10px 16px; border: 1px solid var(--glass-border); border-radius: 999px; background: rgb(255 255 255 / .88); color: #101426; }
.glass-button:hover { background: #fff; }
.glass-button:focus-visible { outline: 3px solid #f8d34f; outline-offset: 3px; }
.glass-input { min-height: 44px; padding: 10px 12px; border: 1px solid var(--glass-border); border-radius: 10px; background: rgb(0 0 0 / .22); color: #fff; }
.glass-modal { max-width: 560px; background: var(--glass-fallback); }
```

## Opacity rule
Opacity is material, not hierarchy. Do not lower text opacity until it becomes unreadable. Keep essential text on a contrast-tested surface and provide a solid fallback. Limit blur to bounded overlays; never blur every card.
