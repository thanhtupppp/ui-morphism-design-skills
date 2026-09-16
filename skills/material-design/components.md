# Material Design — Component Anatomy & Recipes

Material Design is a component and interaction system. Semantic roles, component anatomy, states, adaptive behavior and purposeful motion take priority over decoration.

## Core design tokens

```css
:root {
  --um-material-design-bg: #fffbfe;
  --um-material-design-surface-1: #f7f2fa;
  --um-material-design-surface-2: #f3edf7;
  --um-material-design-surface-3: #ece6f0;
  --um-material-design-ink: #1d1b20;
  --um-material-design-ink-muted: #49454f;
  --um-material-design-accent: #6750a4;
  --um-material-design-on-accent: #ffffff;
  --um-material-design-secondary: #625b71;
  --um-material-design-tertiary: #7d5260;
  --um-material-design-danger: #b3261e;
  --um-material-design-border: #79747e;
  --um-material-design-border-strong: #49454f;
  --um-material-design-focus: #4f378b;
  --um-material-design-radius-xs: 4px;
  --um-material-design-radius-sm: 8px;
  --um-material-design-radius-md: 12px;
  --um-material-design-radius-lg: 16px;
  --um-material-design-radius-xl: 28px;
  --um-material-design-radius-pill: 999px;
  --um-material-design-target-min: 48px;
  --um-material-design-elev-0: none;
  --um-material-design-elev-1: 0 1px 3px rgb(0 0 0 / .20), 0 1px 2px rgb(0 0 0 / .14);
  --um-material-design-elev-2: 0 2px 6px rgb(0 0 0 / .20), 0 2px 4px rgb(0 0 0 / .14);
  --um-material-design-elev-3: 0 6px 12px rgb(0 0 0 / .20), 0 3px 6px rgb(0 0 0 / .14);
}
```

## State layers

Every interactive component defines default, pointer hover where relevant, focus, pressed, selected/checked, disabled and task-specific loading/error/success/expanded states. Focus and selection remain explicit when elevation is removed.

## Buttons

```css
.md-button {
  min-height:var(--um-material-design-target-min);
  min-width:64px;
  padding:10px 18px;
  border:0;
  border-radius:var(--um-material-design-radius-pill);
  background:var(--um-material-design-accent);
  color:var(--um-material-design-on-accent);
  font:inherit;
  font-weight:650;
}
.md-button:hover { box-shadow:var(--um-material-design-elev-1); }
.md-button:focus-visible { outline:3px solid var(--um-material-design-focus); outline-offset:3px; }
```

## Component contract

Fields retain persistent labels/support/error text. Selection controls expose state semantically. Navigation uses persistent current-destination indicators. Dialogs manage focus entry/restoration. Tables preserve header/row/sort/loading/empty/error semantics without forcing elevation onto every row.

## Adaptive behavior

Recompose rather than shrink: navigation bar ↔ rail/drawer, multi-column ↔ single-column, side panel ↔ sheet, expanded actions ↔ overflow. Preserve semantic and task order.

## Accessibility and fallback

Names, focus, keyboard traversal, target size, text scaling, localization, RTL, reduced motion and high-contrast behavior remain usable. When elevation/state-layer effects are unavailable, use opaque surfaces, explicit borders and semantic color roles without changing behavior.

## Performance

Prefer native/framework primitives. Bound elevation and animation costs and avoid simultaneously animating large numbers of elevated surfaces.

## Anti-patterns

- Treating a palette or rounded cards as Material by itself.
- Elevation on every element.
- Custom-painted controls that discard native semantics.
- Hover-only critical information.
- State-layer opacity as a substitute for semantic state.
