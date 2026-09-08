# Glassmorphism

## Purpose
Glassmorphism creates a translucent, frosted plane between the user and a controlled backdrop.

## Use when
- The product needs floating navigation, hero cards, modal sheets, command palettes, or transient chrome.
- The background is controlled, structured, and contrast-tested.

## Avoid when
- The surface contains long text, data tables, dense forms, or user-uploaded imagery.
- Multiple nested blurred surfaces are required to make the style visible.
- The application must render consistently on very low-power devices.

## Visual DNA
- Use translucent tint, backdrop blur, subtle border, and a controlled shadow/rim.
- Keep one or two glass levels; use solid surfaces for content.
- Treat the backdrop as a dependency and test worst-case luminance.

## Token recipe
```css
:root {
  --um-glassmorphism-bg: #0b0b12;
  --um-glassmorphism-surface-1: rgb(255 255 255 / .14);
  --um-glassmorphism-surface-fallback: #202331;
  --um-glassmorphism-border-strong: rgb(255 255 255 / .42);
  --um-glassmorphism-blur-2: 20px;
  --um-glassmorphism-shadow-1: 0 8px 32px -8px rgb(0 0 0 / .38);
}
.um-glass { background: var(--um-glassmorphism-surface-fallback); border: 1px solid var(--um-glassmorphism-border-strong); }
@supports (backdrop-filter: blur(1px)) { .um-glass { background: var(--um-glassmorphism-surface-1); backdrop-filter: blur(var(--um-glassmorphism-blur-2)) saturate(160%); } }
```

## Component rules
- Navigation/modal: glass can sit above content with a stable scrim.
- Card: keep text area stable and limit blur to the card boundary.
- Form/table: use opaque Material or Flat surface.
- Focus: outline must sit above the glass border and remain visible on every backdrop.

## Motion and performance
Bound `backdrop-filter` to small surfaces. Do not blur the page subtree or nest glass surfaces. Use opaque fallback under unsupported effects and reduced-motion settings.

## Accessibility checklist
- [ ] Test light, dark, colorful, and moving backgrounds.
- [ ] Text and focus remain readable at every scroll position.
- [ ] Forced-colors mode removes decorative transparency.
- [ ] User can disable transparency if the product needs extended use.

## Anti-patterns
- Full-screen blur as a page background.
- Glass on glass on glass.
- White low-opacity text over bright imagery.
