# Flat Design — Component Anatomy & Recipes

Flat Design means hierarchy comes from semantic color, typography, spacing, alignment, grouping, borders, and explicit states rather than simulated physical depth.

## 1. Visual anatomy

Build a flat interface in this order: page background → spacing/layout → typography hierarchy → surface grouping → functional boundaries → semantic colors → interaction states → optional restrained elevation.

## 2. Design tokens

```css
:root {
  --um-flat-design-bg: #f7f8fa;
  --um-flat-design-surface-1: #ffffff;
  --um-flat-design-surface-2: #f1f5f9;
  --um-flat-design-surface-3: #e2e8f0;
  --um-flat-design-ink: #18202a;
  --um-flat-design-ink-muted: #52606d;
  --um-flat-design-border: #cbd5e1;
  --um-flat-design-border-strong: #64748b;
  --um-flat-design-accent: #2563eb;
  --um-flat-design-accent-hover: #1d4ed8;
  --um-flat-design-accent-active: #1e40af;
  --um-flat-design-success: #15803d;
  --um-flat-design-warning: #a16207;
  --um-flat-design-danger: #b91c1c;
  --um-flat-design-info: #0369a1;
  --um-flat-design-focus: #1d4ed8;
  --um-flat-design-on-accent: #ffffff;
  --um-flat-design-radius-sm: 6px;
  --um-flat-design-radius-md: 8px;
  --um-flat-design-radius-lg: 12px;
  --um-flat-design-target-min: 44px;
  --um-flat-design-space-1: 4px;
  --um-flat-design-space-2: 8px;
  --um-flat-design-space-3: 12px;
  --um-flat-design-space-4: 16px;
  --um-flat-design-space-5: 20px;
  --um-flat-design-space-6: 24px;
  --um-flat-design-space-8: 32px;
  --um-flat-design-shadow-1: 0 1px 2px rgb(0 0 0 / .08);
}
```

Tokens are semantic. Do not scatter literal colors across components.

### Theme profiles

Explicit theme choice overrides system preference. Change role values, not component structure.

```css
:root[data-theme="light"] {
  --um-flat-design-bg: #f7f8fa;
  --um-flat-design-surface-1: #ffffff;
  --um-flat-design-ink: #18202a;
  --um-flat-design-ink-muted: #52606d;
  --um-flat-design-border: #cbd5e1;
  --um-flat-design-border-strong: #64748b;
  --um-flat-design-accent: #2563eb;
  --um-flat-design-focus: #1d4ed8;
  --um-flat-design-on-accent: #ffffff;
}

:root[data-theme="dark"] {
  --um-flat-design-bg: #0f172a;
  --um-flat-design-surface-1: #111827;
  --um-flat-design-ink: #f8fafc;
  --um-flat-design-ink-muted: #cbd5e1;
  --um-flat-design-border: #475569;
  --um-flat-design-border-strong: #94a3b8;
  --um-flat-design-accent: #60a5fa;
  --um-flat-design-focus: #93c5fd;
  --um-flat-design-on-accent: #0f172a;
}
```

### Density profiles

Density reduces whitespace before interactive affordance.

```css
:root,
[data-density="standard"] {
  --um-flat-design-target-min: 44px;
  --um-flat-design-space-density-padding: 16px;
  --um-flat-design-space-density-gap: 12px;
}
[data-density="comfortable"] {
  --um-flat-design-target-min: 48px;
  --um-flat-design-space-density-padding: 20px;
  --um-flat-design-space-density-gap: 16px;
}
[data-density="compact"] {
  --um-flat-design-target-min: 44px;
  --um-flat-design-space-density-padding: 12px;
  --um-flat-design-space-density-gap: 8px;
}
```

## 3. Typography

Use typography as the primary depth system. Keep form labels persistent, allow localization to wrap, and do not depend on fixed-height text containers.

## 4. Buttons

```css
.flat-button {
  min-height: var(--um-flat-design-target-min);
  padding: 10px 16px;
  border: 1px solid transparent;
  border-radius: var(--um-flat-design-radius-md);
  background: var(--um-flat-design-accent);
  color: var(--um-flat-design-on-accent);
  font: inherit;
  font-weight: 650;
  cursor: pointer;
}
.flat-button:hover { background: var(--um-flat-design-accent-hover); }
.flat-button:active { background: var(--um-flat-design-accent-active); }
.flat-button:focus-visible { outline: 3px solid var(--um-flat-design-focus); outline-offset: 3px; }
.flat-button:disabled { opacity: .55; cursor: not-allowed; }
```

Every button defines default, pointer hover where supported, pressed, focus-visible, disabled, and loading when applicable.

## 5. Component recipes

- **Card/panel:** use `--um-flat-design-surface-1`, `--um-flat-design-border`, and spacing tokens. Shadow is optional grouping only.
- **Input:** persistent label, explicit border/focus and text/icon validation feedback.
- **Navigation:** persistent active cue in addition to color.
- **Table/data grid:** stable row/column relationships, semantic headers and explicit selected/sorted/loading/empty/error states.
- **Dialog/alert/banner:** semantic roles, clear heading/message/action relationships and focus independent of decoration.
- **Tabs:** correct tab semantics; selected state remains understandable without color alone.
- **Progress/status:** expose a machine-readable value/label where applicable and pair color with text/icon/state labels.

## 6. State contract

Removing color, shadow, animation and decoration must not erase default/focus/pressed/selected/disabled/loading/error/success meaning.

## 7. Responsive contract

Use content-driven sizing and wrapping. Preserve semantic/task order, localization, text scaling and platform-appropriate target sizes across compact, medium and expanded layouts.

## 8. Accessibility contract

Focus is explicit; color is never the only state channel; labels/errors are programmatically associated; keyboard, screen-reader, zoom, forced-colors and large-text behavior remain usable.

## 9. Motion, fallback and performance

Flat Design does not require animation. Respect reduced motion. Optional elevation degrades to borders/grouping without changing meaning. Prefer inexpensive opaque surfaces and native controls for dense or constrained interfaces.

## 10. Implementation rule

Across HTML/CSS, React, Flutter and React Native, preserve semantic roles, states, hierarchy, density intent and accessibility behavior. Pixel-perfect parity is not required; semantic parity is.
