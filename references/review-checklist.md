# Production Review Checklist

## Style
- [ ] One primary style is named and used consistently.
- [ ] Supporting style is limited to a defined surface or component role.
- [ ] Materials, shadows, borders, gradients, and motion communicate hierarchy.
- [ ] No accidental mixing of incompatible visual languages.

## Accessibility
- [ ] Body text contrast is at least 4.5:1; large text is at least 3:1.
- [ ] Focus is visible, high contrast, and not obscured by overlays.
- [ ] All controls have accessible names and keyboard behavior.
- [ ] Color is not the only indicator for state or validation.
- [ ] Reduced motion is supported.
- [ ] Forms have persistent labels and associated errors.

## Responsive
- [ ] Tested at 375, 768, 1024, and 1440 CSS pixels.
- [ ] No horizontal scrolling caused by layout or effects.
- [ ] Bento cells stack in meaningful DOM order.
- [ ] Text survives localization and zoom.

## Performance
- [ ] Large-area blur is limited or disabled on constrained devices.
- [ ] Decorative animation is reduced when needed.
- [ ] Fallback styles work when blur, gradient, or advanced effects are unavailable.
- [ ] Images and fonts are optimized.
