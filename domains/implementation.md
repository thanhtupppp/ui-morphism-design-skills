# Implementation Recipes

## React and Next.js

Keep semantic markup, state, and accessibility behavior independent from the selected visual style. Use a `data-style` or component variant to swap token scopes rather than duplicating component trees.

```tsx
<button className="um-button" aria-pressed={pressed}>
  <span>Set temperature</span>
  <output aria-live="polite">21°</output>
</button>
```

## CSS layers

Keep the effect in a named surface class and provide a fallback before the advanced effect:

```css
.um-glass-surface {
  background: var(--um-glassmorphism-surface-fallback);
  border: 1px solid var(--um-glassmorphism-border-strong);
}

@supports (backdrop-filter: blur(1px)) {
  .um-glass-surface {
    background: var(--um-glassmorphism-surface-1);
    backdrop-filter: blur(var(--um-glassmorphism-blur-2)) saturate(150%);
  }
}
```

## Tailwind

Expose semantic utilities such as `um-surface`, `um-surface-glass`, `um-focus`, `um-press`, and `um-elevation-1`. Do not scatter arbitrary blur and shadow values through JSX.

## Flutter

Store colors, shape, elevation, and motion in `ThemeData` or a custom `ThemeExtension`. Keep platform reduced-motion and high-contrast settings in the theme layer.

## Performance budgets

- Prefer zero-blur Flat, Bento, and Neobrutalist effects on low-end devices.
- Bound backdrop-filter to small areas and avoid nested translucent surfaces.
- Animate opacity and transform before animating layout dimensions.
- Lazy-load large textures, images, and decorative 3D assets.
