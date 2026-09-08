# Aurora UI

## Purpose
Aurora UI uses ambient multi-color gradients, diffuse glow, and soft atmospheric light to establish mood. It is primarily a background and emphasis system, not a complete component language.

## Use when
- The product needs premium, experimental, AI, creative, or futuristic atmosphere.
- The page has a clear hero, focal action, or short marketing narrative.
- Content can sit on stable opaque or high-contrast surfaces above the effect.

## Avoid when
- Users must read dense tables, forms, logs, legal text, or long documentation.
- The gradient is the only indicator of error, success, selection, or status.
- The product targets low-power devices and cannot disable continuous animation.

## Visual DNA
- Use 2–4 related color stops with one dominant hue and one accent hue.
- Place glow behind content using pseudo-elements or isolated background layers.
- Keep content surfaces calm: solid, translucent with a scrim, or neutral cards.
- Use large blur for atmosphere, but do not blur text or interactive controls.
- Maintain one focal light region; competing bright regions destroy hierarchy.

## Token recipe

```css
:root {
  --um-aurora-ui-bg: #0d1021;
  --um-aurora-ui-surface-1: rgb(255 255 255 / 0.92);
  --um-aurora-ui-aurora-a: #6d5dfc;
  --um-aurora-ui-aurora-b: #19c6b5;
  --um-aurora-ui-aurora-c: #ff6b9a;
  --um-aurora-ui-ink: #101426;
  --um-aurora-ui-ink-muted: #526078;
  --um-aurora-ui-focus: #f8d34f;
  --um-aurora-ui-blur-1: 64px;
}

.um-aurora-background {
  position: relative;
  isolation: isolate;
  background: var(--um-aurora-ui-bg);
}

.um-aurora-background::before {
  content: "";
  position: absolute;
  inset: -20%;
  z-index: -1;
  pointer-events: none;
  background:
    radial-gradient(circle at 18% 22%, var(--um-aurora-ui-aurora-a), transparent 34%),
    radial-gradient(circle at 78% 18%, var(--um-aurora-ui-aurora-b), transparent 30%),
    radial-gradient(circle at 58% 82%, var(--um-aurora-ui-aurora-c), transparent 32%);
  filter: blur(var(--um-aurora-ui-blur-1));
  opacity: .82;
}
```

## Component rules
- Hero: place the primary heading and CTA on an opaque or contrast-tested surface.
- Card: use a neutral card with aurora as a border glow or controlled backdrop only.
- Button: use semantic solid color; never rely on glow alone for hover or focus.
- Form: keep inputs opaque and errors explicit with text and icons.
- Status: use semantic color, label, icon, and live-region feedback independently of the gradient.

## Motion
- Animate only slow `transform` and `opacity`, never rapid hue cycling.
- Default animation should be subtle and pause when the page is hidden.
- Under `prefers-reduced-motion: reduce`, freeze the gradient or use one static composition.

## Responsive and performance
- Reduce glow area and blur on mobile or low-power devices.
- Avoid multiple animated pseudo-elements per card.
- Do not apply `filter: blur()` to a large DOM subtree containing content.
- Keep the layout functional when the aurora layer is removed.

## Accessibility checklist
- [ ] Text contrast tested against the worst visible gradient position.
- [ ] Focus ring is a solid, high-contrast outline.
- [ ] Status is communicated with text/icon, not glow or hue only.
- [ ] Reduced-motion and static-background modes work.
- [ ] Forced-colors mode hides decorative gradients and keeps content readable.

## Anti-patterns
- Neon background behind long paragraphs.
- Every card having a different animated gradient.
- Glow used as a replacement for hierarchy, border, or focus.
- Low-opacity white text over a moving background.
