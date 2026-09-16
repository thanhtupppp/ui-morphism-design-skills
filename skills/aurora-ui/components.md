# Aurora UI Component Recipes

Aurora is primarily an atmospheric layer. Component recipes below preserve semantic, stable controls while using Aurora selectively for emphasis.

## 1. Token contract

```css
:root {
  --um-aurora-ui-bg: #0d1021;
  --um-aurora-ui-aurora-a: #6d5dfc;
  --um-aurora-ui-aurora-b: #19c6b5;
  --um-aurora-ui-aurora-c: #ff6b9a;
  --um-aurora-ui-surface-1: rgb(255 255 255 / .94);
  --um-aurora-ui-surface-2: rgb(255 255 255 / .98);
  --um-aurora-ui-ink: #101426;
  --um-aurora-ui-ink-muted: #526078;
  --um-aurora-ui-focus: #f8d34f;
  --um-aurora-ui-border: rgb(255 255 255 / .26);
  --um-aurora-ui-blur-1: 64px;
  --um-aurora-ui-radius-md: 16px;
  --um-aurora-ui-radius-lg: 24px;
  --um-aurora-ui-target-min: 44px;
}
```

Keep decorative Aurora tokens separate from application semantic tokens such as error, success, and selected roles.

## 2. Anatomy of an Aurora page

```text
page
├─ stable ground
├─ aurora field
│  ├─ light source A
│  ├─ light source B
│  └─ optional light source C
├─ optional scrim/protection layer
└─ content
   ├─ navigation
   ├─ hero/focal module
   ├─ cards
   └─ controls/data
```

The Aurora field should be a sibling/ancestor of content, not an effect that causes content itself to become blurred or translucent.

## 3. Base background

```css
.aurora-page {
  position: relative;
  isolation: isolate;
  min-height: 100%;
  overflow: hidden;
  padding: 24px;
  background: var(--um-aurora-ui-bg);
}

.aurora-page::before {
  content: "";
  position: absolute;
  inset: -30%;
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

The page remains usable when `::before` is removed.

## 4. Hero and cards

Prefer a stable surface when text overlaps a strong or moving light region.

```css
.aurora-hero,
.aurora-card {
  padding: 24px;
  border: 1px solid var(--um-aurora-ui-border);
  border-radius: var(--um-aurora-ui-radius-lg);
  background: var(--um-aurora-ui-surface-1);
  color: var(--um-aurora-ui-ink);
}
```

A single featured card may receive restrained decorative depth, but hierarchy must still be clear with shadows/glow removed.

## 5. Buttons and icon buttons

```css
.aurora-button {
  min-height: var(--um-aurora-ui-target-min);
  min-width: var(--um-aurora-ui-target-min);
  padding: 10px 16px;
  border: 1px solid transparent;
  border-radius: var(--um-aurora-ui-radius-md);
  background: #4338ca;
  color: #fff;
  font: inherit;
  font-weight: 700;
}

.aurora-button:hover { filter: brightness(1.05); }
.aurora-button:active { transform: translateY(1px); }
.aurora-button:focus-visible { outline: 3px solid var(--um-aurora-ui-focus); outline-offset: 3px; }
.aurora-button:disabled { opacity: .55; cursor: not-allowed; }

.aurora-icon-button {
  width: var(--um-aurora-ui-target-min);
  height: var(--um-aurora-ui-target-min);
  border: 1px solid var(--um-aurora-ui-border);
  border-radius: var(--um-aurora-ui-radius-md);
  background: var(--um-aurora-ui-surface-2);
}
```

Provide accessible names for icon buttons and persistent state cues independent of glow.

## 6. Inputs and selection controls

```css
.aurora-input {
  min-height: var(--um-aurora-ui-target-min);
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #9ca3af;
  border-radius: var(--um-aurora-ui-radius-md);
  background: #fff;
  color: var(--um-aurora-ui-ink);
  font: inherit;
}

.aurora-input:focus-visible { outline: 3px solid var(--um-aurora-ui-focus); outline-offset: 2px; }
.aurora-field[data-invalid="true"] .aurora-input { border-color: #b42318; }
```

Selection, validation, loading, disabled, and success states must remain explicit without Aurora decoration.

## 7. Navigation, dialogs, data, and status

Use Aurora at the page/chrome level. Navigation retains an explicit current destination. Dialogs use a scrim plus stable surface and correct focus management. Dense lists/tables use stable opaque surfaces. Status uses semantic color + text/icon; glow is optional decoration only.

## 8. State matrix

| State | Required cue | Aurora role |
|---|---|---|
| Default | Stable fill/border | ambient support |
| Hover | Clear interactive change | optional slight glow |
| Pressed | Persistent tactile/state change | decorative only |
| Focus-visible | Solid high-contrast ring | never sufficient alone |
| Selected | Fill/border/icon/label | optional emphasis |
| Disabled | Readable reduced emphasis | remove most glow |
| Loading | Spinner/progress/skeleton | no pulse-only cue |
| Error | Error color + text/icon | no glow-only cue |
| Success | Success color + text/icon | no glow-only cue |

## 9. Motion and fallback

Default motion is slow and ambient. Prefer transform/opacity and provide a static mode.

```css
@media (prefers-reduced-motion: reduce) {
  .aurora-page::before { animation: none !important; }
  .aurora-button:active { transform: none; }
}
```

Fallback ladder:

```text
Aurora animated
→ Aurora static
→ simplified gradient
→ solid ground
```

Every step preserves structure, semantic meaning, state, focus, target geometry, and interaction.

## 10. Responsive and performance rules

On narrow or constrained devices, reduce the number/area/opacity/blur of decorative fields before changing text size, spacing, controls, or content order. Bound blur to decorative layers, pause non-essential animation when hidden, and avoid per-card animated effects.

| Layout | Treatment |
|---|---|
| Compact, below 768px | Use one or two static fields with reduced blur area and opacity. |
| Medium, 768–1023px | Keep up to three bounded fields behind stable content surfaces. |
| Expanded, 1024px and above | Increase field coverage only when contrast and performance remain stable. |
