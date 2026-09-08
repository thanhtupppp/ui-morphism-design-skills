# Aurora UI Component Recipes

## Tokens
```css
:root { --aurora-bg: #0d1021; --aurora-a: #6d5dfc; --aurora-b: #19c6b5; --aurora-c: #ff6b9a; --aurora-card: rgb(255 255 255 / .94); --aurora-ink: #101426; --aurora-focus: #f8d34f; --aurora-blur: 64px; }
```

## Background, card, button, input
```css
.aurora-page { position: relative; isolation: isolate; min-height: 100%; overflow: hidden; padding: 24px; background: var(--aurora-bg); }
.aurora-page::before { content: ""; position: absolute; inset: -30%; z-index: -1; pointer-events: none; background: radial-gradient(circle at 18% 22%, var(--aurora-a), transparent 34%), radial-gradient(circle at 78% 18%, var(--aurora-b), transparent 30%), radial-gradient(circle at 58% 82%, var(--aurora-c), transparent 32%); filter: blur(var(--aurora-blur)); opacity: .82; }
.aurora-card { max-width: 560px; padding: 24px; border-radius: 20px; background: var(--aurora-card); color: var(--aurora-ink); }
.aurora-button { min-height: 44px; padding: 10px 16px; border: 0; border-radius: 999px; background: #4338ca; color: #fff; }
.aurora-button:focus-visible { outline: 3px solid var(--aurora-focus); outline-offset: 3px; }
.aurora-input { min-height: 44px; width: 100%; padding: 10px 12px; border: 1px solid #9ca3af; border-radius: 10px; background: #fff; color: var(--aurora-ink); }
@media (prefers-reduced-motion: reduce) { .aurora-page::before { filter: none; } }
```

## Opacity rule
Aurora opacity belongs to decorative light only. Keep cards at a stable opacity (usually 0.92 or higher), keep text opaque, and never use glow/hue as the only focus or status indicator.
