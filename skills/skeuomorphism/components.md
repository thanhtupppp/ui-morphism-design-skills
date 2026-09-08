# Skeuomorphism Component Recipes

## Material tokens
```css
:root { --sk-face: #d8d1c5; --sk-face-dark: #aaa093; --sk-ink: #2e2a25; --sk-border: #70685d; --sk-highlight: rgb(255 255 255 / .78); --sk-shadow: rgb(0 0 0 / .28); --sk-radius: 10px; }
```

## Button
```css
.sk-button { min-height: 44px; padding: 10px 16px; color: var(--sk-ink); border: 1px solid var(--sk-border); border-radius: var(--sk-radius); background: linear-gradient(var(--sk-face), var(--sk-face-dark)); box-shadow: inset 0 1px var(--sk-highlight), 0 2px 4px var(--sk-shadow); }
.sk-button:hover { filter: brightness(1.06); }
.sk-button:active { transform: translateY(1px); box-shadow: inset 0 2px 4px var(--sk-shadow); }
.sk-button:focus-visible { outline: 3px solid #164e63; outline-offset: 3px; }
```

## Card, input, nav
```css
.sk-card { padding: 24px; border: 1px solid var(--sk-border); border-radius: 12px; background: linear-gradient(#e5dfd4, #b0a89c); box-shadow: 0 5px 14px var(--sk-shadow), inset 0 1px var(--sk-highlight); }
.sk-input { min-height: 44px; padding: 10px 12px; border: 1px solid var(--sk-border); border-radius: 6px; background: #eee9df; box-shadow: inset 0 2px 4px rgb(0 0 0 / .16); }
.sk-input:focus { outline: 3px solid #164e63; outline-offset: 2px; }
.sk-nav { padding: 12px 16px; border-bottom: 1px solid var(--sk-border); background: linear-gradient(#d8d1c5, #aaa093); }
```

## Component contract
Buttons need labels and explicit states; realistic texture is limited to bounded controls; data tables use flat opaque inner surfaces.
