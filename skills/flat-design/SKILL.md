# Flat Design

## Purpose
Flat Design uses color, typography, spacing, alignment, icons, and explicit states instead of simulated physical depth.

## Use when
- The product is data-dense, operational, cross-platform, or long-lived.
- Speed, scanning, readability, and maintainability matter more than material drama.
- The team needs a stable design-system foundation.

## Visual DNA
- Use semantic color roles rather than one-off hex values.
- Create hierarchy with spacing, type scale, grouping, borders, and surface tone.
- Use restrained radius and shadow; zero shadow is valid, but zero hierarchy is not.
- Keep icon geometry and text contrast consistent.

## Component rules
- Button: primary, secondary, destructive, ghost, and disabled variants need distinct states.
- Form: persistent label, helper text, inline error, focus, and success treatment.
- Table: opaque header/body, selected row, sortable state, loading, empty, and error state.
- Navigation: active state must include more than color, such as icon, underline, weight, or surface.

## Token recipe
```css
:root {
  --um-flat-design-bg: #f7f8fa;
  --um-flat-design-surface-1: #ffffff;
  --um-flat-design-ink: #18202a;
  --um-flat-design-ink-muted: #52606d;
  --um-flat-design-border-strong: #64748b;
  --um-flat-design-accent: #2563eb;
  --um-flat-design-focus: #1d4ed8;
}
.um-flat-button { min-height: 44px; border: 1px solid transparent; border-radius: 8px; background: var(--um-flat-design-accent); color: white; }
.um-flat-button:focus-visible { outline: 3px solid var(--um-flat-design-focus); outline-offset: 3px; }
```

## Motion
Prefer opacity and transform for feedback. Use short transitions for hover/focus and immediate feedback for critical status. Respect reduced motion.

## Responsive and performance
Build mobile-first. Use CSS Grid/Flexbox, content-based breakpoints, and stable DOM order. Flat Design is a good fallback for all advanced styles.

## Accessibility checklist
- [ ] Body text and controls meet contrast requirements.
- [ ] Every interactive state is visible without hover.
- [ ] Color is not the only status channel.
- [ ] Keyboard order follows visual/task order.
- [ ] Zoom and localization do not clip content.

## Anti-patterns
- Removing borders and focus indicators to look minimalist.
- Gray-on-gray text and disabled controls that become invisible.
- Inconsistent component states across screens.
