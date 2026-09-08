# Liquid Glass / Liquid UI

## Purpose
Liquid Glass is a dynamic translucent material for contextual controls and navigation. It adapts to surrounding content instead of behaving like a decorative background.

## Use when
- The product uses platform-like navigation, floating toolbars, contextual controls, or premium media chrome.
- The platform can render the material reliably or the web implementation has a solid fallback.

## Avoid when
- Critical reading content sits directly on moving or unpredictable imagery.
- The product requires identical rendering across browsers without progressive enhancement.
- Nested liquid/glass layers are needed.

## Visual DNA
- Combine tint, translucency, controlled blur, subtle reflection, and a clear rim.
- Use a functional layer with stable hit areas and predictable grouping.
- Keep opacity high enough for arbitrary backdrops; never assume the background will help.
- Use one liquid dialect per surface class; do not mix decorative glass and liquid glass on the same layer.

## Token recipe
```css
:root {
  --um-liquid-glass-bg: #f5f5f7;
  --um-liquid-glass-surface-1: rgb(255 255 255 / .62);
  --um-liquid-glass-surface-fallback: #f5f5f7;
  --um-liquid-glass-border-strong: rgb(255 255 255 / .72);
  --um-liquid-glass-blur-2: 20px;
  --um-liquid-glass-radius-pill: 999px;
}
.um-liquid-surface { background: var(--um-liquid-glass-surface-fallback); border: 1px solid var(--um-liquid-glass-border-strong); border-radius: var(--um-liquid-glass-radius-pill); }
@supports (backdrop-filter: blur(1px)) { .um-liquid-surface { background: var(--um-liquid-glass-surface-1); backdrop-filter: blur(var(--um-liquid-glass-blur-2)) saturate(180%); } }
```

## Component rules
- Toolbar/navigation: keep controls grouped and labels discoverable.
- Contextual action: expand/collapse states need explicit accessible names.
- Panel: provide an opaque mode and preserve reading order beneath it.
- Drag/resize: provide non-drag alternatives for keyboard and touch users.

## Motion and performance
Use restrained morph/opacity transitions. Do not continuously animate reflection or distortion by default. Disable displacement and reduce blur for reduced motion or constrained devices. Avoid nested backdrop sampling.

## Accessibility checklist
- [ ] Content remains legible as the background changes.
- [ ] Focus is visible above the material.
- [ ] A solid fallback exists for unsupported CSS.
- [ ] Reduced transparency or static mode is available where needed.
- [ ] Touch target and keyboard behavior are independent of visual shape.

## Anti-patterns
- Liquid material as wallpaper behind critical text.
- Nested liquid glass surfaces.
- Platform imitation that ignores browser support and product context.
