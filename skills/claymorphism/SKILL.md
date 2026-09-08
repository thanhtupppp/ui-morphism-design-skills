# Claymorphism

## Purpose
Claymorphism uses opaque, inflated, rounded objects with soft highlights and hue-matched shadows to communicate friendliness.

## Use when
- The product is educational, playful, onboarding-focused, wellness-oriented, or gamified.
- Visual objects need warmth and approachable physicality.

## Avoid when
- The workflow is regulated, dense, data-heavy, or credibility-first.
- Every list item would need a large inflated surface.
- Pastel colors cannot maintain text and focus contrast.

## Visual DNA
- Use an opaque pastel or candy-colored body.
- Use large radius/squircle geometry and one consistent light source.
- Pair a light inset top, dark inset bottom, and hue-matched outer shadow.
- Keep typography crisp and less playful than the object layer.

## Token recipe
```css
:root {
  --um-claymorphism-bg: #f4f1fb;
  --um-claymorphism-surface-1: #cfd4ff;
  --um-claymorphism-ink: #24233a;
  --um-claymorphism-border-strong: #554d86;
  --um-claymorphism-radius-lg: 32px;
  --um-claymorphism-shadow-1: inset 0 10px 18px -6px rgb(255 255 255 / .62), inset 0 -10px 18px -6px rgb(52 42 91 / .32), 0 24px 44px -12px rgb(80 65 150 / .32);
}
.um-clay { border: 1px solid transparent; border-radius: var(--um-claymorphism-radius-lg); background: var(--um-claymorphism-surface-1); box-shadow: var(--um-claymorphism-shadow-1); }
.um-clay:focus-visible { outline: 3px solid var(--um-claymorphism-border-strong); outline-offset: 4px; }
```

## Component rules
- Card/button: use different scale, not identical radius and shadow everywhere.
- Empty state: clay illustration can be expressive while text/action remains conventional.
- Form: use explicit labels, borders, and error text; do not rely on indentation or shadow.
- Dense content: switch to Flat Design surfaces around clay hero objects.

## Motion
Use soft scale/translate feedback. Avoid bouncing loops and large spring overshoot. Freeze or simplify motion under reduced motion.

## Responsive and performance
Limit deep shadow stacks and large blur radii in lists. Avoid fixed-height cards that clip translated/localized text. Keep illustrations lazy-loaded.

## Accessibility checklist
- [ ] Pastel text and icons meet contrast.
- [ ] Controls remain visible if shadows are removed.
- [ ] Focus ring differs from the body shadow.
- [ ] Forced-colors mode provides solid boundaries.

## Anti-patterns
- Tiny text inside giant soft shapes.
- Clay styling on every table row.
- Translucent clay surfaces whose body cannot be shaded consistently.
