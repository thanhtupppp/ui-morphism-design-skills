# Liquid Glass — Component Anatomy & Recipes

Liquid Glass is a functional translucent material. Components must remain understandable when blur, reflection, and distortion are removed.

## Surface anatomy

Stable layout and hit area → base/tinted surface → optional blur → rim/highlight → depth → optional reflection/distortion → content and controls.

## Tokens

```css
:root {
  --um-liquid-glass-bg: #f5f5f7;
  --um-liquid-glass-surface-1: rgb(255 255 255 / .62);
  --um-liquid-glass-surface-2: rgb(255 255 255 / .76);
  --um-liquid-glass-surface-fallback: #f5f5f7;
  --um-liquid-glass-ink: #111827;
  --um-liquid-glass-ink-muted: #4b5563;
  --um-liquid-glass-border: rgb(255 255 255 / .72);
  --um-liquid-glass-border-strong: rgb(255 255 255 / .9);
  --um-liquid-glass-focus: #155e75;
  --um-liquid-glass-shadow-1: 0 8px 32px rgb(0 0 0 / .12);
  --um-liquid-glass-blur-sm: 12px;
  --um-liquid-glass-blur-md: 20px;
  --um-liquid-glass-blur-lg: 32px;
  --um-liquid-glass-radius-sm: 14px;
  --um-liquid-glass-radius-lg: 26px;
  --um-liquid-glass-radius-pill: 999px;
  --um-liquid-glass-target-min: 44px;
}
```

## Toolbar

```css
.liquid-toolbar {
  display:flex;
  gap:8px;
  align-items:center;
  min-height:52px;
  padding:6px;
  color:var(--um-liquid-glass-ink);
  border:1px solid var(--um-liquid-glass-border);
  border-radius:var(--um-liquid-glass-radius-pill);
  background:var(--um-liquid-glass-surface-fallback);
  box-shadow:var(--um-liquid-glass-shadow-1);
}
@supports (backdrop-filter: blur(1px)) {
  .liquid-toolbar {
    background:var(--um-liquid-glass-surface-1);
    backdrop-filter:blur(var(--um-liquid-glass-blur-md)) saturate(180%);
  }
}
```

## Buttons

```css
.liquid-button {
  min-width:var(--um-liquid-glass-target-min);
  min-height:var(--um-liquid-glass-target-min);
  padding:10px 14px;
  border:1px solid transparent;
  border-radius:var(--um-liquid-glass-radius-pill);
  background:transparent;
  color:var(--um-liquid-glass-ink);
}
.liquid-button:focus-visible { outline:3px solid var(--um-liquid-glass-focus); outline-offset:3px; }
.liquid-button[aria-pressed="true"] { background:var(--um-liquid-glass-surface-2); border-color:var(--um-liquid-glass-border-strong); }
```

Icon buttons require accessible names and stable targets. Selection, focus, error, loading and expanded state must remain explicit without blur/reflection.

## Forms, navigation and data

Use conventional high-contrast fields inside Liquid shells. Navigation remains usable if the material becomes opaque. Large lists and tables use an opaque inner surface; Liquid is reserved for bounded chrome or outer shells.

## Semantic state contract

Default, hover, pressed, selected, focus, disabled, loading, error and expanded/collapsed states must each retain semantic meaning independently of material effects.

## Fallback ladder

```text
blur + tint + rim + reflection/distortion
→ blur + tint + rim
→ tint + rim
→ opaque/tinted surface + rim
→ flat opaque surface + border
```

The component remains functionally identical through every tier.

## Accessibility

Preserve accessible names, state semantics, keyboard alternatives for drag/slider/rotary interactions, focus restoration for dialogs, target sizes, large text/localization and high-contrast behavior.

## Performance

Bound blur to the smallest useful surface, avoid nested backdrop sampling and full-screen distortion, and remove distortion/blur before removing borders, labels or state indicators.

## Anti-patterns

- Full-page animated distortion.
- Nested Liquid surfaces sampling one another.
- Tiny icon targets.
- Long text directly over unpredictable imagery.
- Reflection/glow/distortion as the only state cue.
