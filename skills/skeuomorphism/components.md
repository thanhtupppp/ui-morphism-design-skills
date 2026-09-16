# Skeuomorphism Component System

Skeuomorphism transfers useful physical affordances into digital controls. Realism never replaces semantic behavior.

## Token foundation

```css
:root {
  --um-skeuomorphism-bg: #d8d1c5;
  --um-skeuomorphism-surface-1: #d8d1c5;
  --um-skeuomorphism-surface-dark: #aaa093;
  --um-skeuomorphism-surface-light: #eee9df;
  --um-skeuomorphism-ink: #2e2a25;
  --um-skeuomorphism-ink-muted: #625a50;
  --um-skeuomorphism-border: #70685d;
  --um-skeuomorphism-border-strong: #4f4942;
  --um-skeuomorphism-highlight: rgb(255 255 255 / .78);
  --um-skeuomorphism-shadow-contact: rgb(0 0 0 / .28);
  --um-skeuomorphism-shadow-soft: rgb(0 0 0 / .18);
  --um-skeuomorphism-radius-sm: 6px;
  --um-skeuomorphism-radius-md: 10px;
  --um-skeuomorphism-radius-lg: 14px;
  --um-skeuomorphism-target-min: 44px;
  --um-skeuomorphism-focus: #0f5b78;
  --um-skeuomorphism-danger: #a52a2a;
  --um-skeuomorphism-success: #23663a;
  --um-skeuomorphism-warning: #8a5b16;
}
```

## Button and input recipes

```css
.sk-button {
  min-height:var(--um-skeuomorphism-target-min);
  padding:10px 16px;
  color:var(--um-skeuomorphism-ink);
  border:1px solid var(--um-skeuomorphism-border);
  border-radius:var(--um-skeuomorphism-radius-md);
  background:linear-gradient(var(--um-skeuomorphism-surface-light), var(--um-skeuomorphism-surface-dark));
  box-shadow:inset 0 1px 0 var(--um-skeuomorphism-highlight), 0 2px 4px var(--um-skeuomorphism-shadow-contact), 0 6px 12px var(--um-skeuomorphism-shadow-soft);
}
.sk-button:focus-visible { outline:3px solid var(--um-skeuomorphism-focus); outline-offset:3px; }

.sk-input {
  min-height:var(--um-skeuomorphism-target-min);
  border:1px solid var(--um-skeuomorphism-border);
  border-radius:var(--um-skeuomorphism-radius-sm);
  background:var(--um-skeuomorphism-surface-light);
  color:var(--um-skeuomorphism-ink);
}
```

## Physical controls and semantic parity

Switches, sliders and knobs may visually depress, slide or rotate, but expose explicit state/value semantics. Pointer/touch drag is never the only interaction path; provide keyboard increment/decrement, buttons or an accessible range-control equivalent. Tables and long reading surfaces stay mostly flat inside a physical shell.

## Accessibility

Use a separate focus outline, persistent labels/values, explicit selected/disabled/loading/error states, stable target sizes and non-color status cues. Forced colors and removal of gradients/shadows/textures must retain boundaries and operability.

## Fallback

```text
material + bevel + texture + depth
→ material + restrained depth
→ opaque surface + explicit border
→ flat semantic control
```

## Performance

Bound textures and shadow layers to important physical modules. Avoid full-screen raster textures, animated grain, repeated heavy shadows and unnecessary custom painting where native controls can provide behavior.

## Anti-patterns

- Realism without affordance.
- Inconsistent light direction.
- Texture as a state/boundary signal.
- Shadow-only focus or selection.
- Gesture-only knobs/sliders.
- Physical styling applied to every table cell or form row.
