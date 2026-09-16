# Glassmorphism — Component Anatomy & Recipes

Glassmorphism is a translucent, frosted plane above a controlled backdrop. Blur belongs to the material layer, never to foreground content.

## Core tokens

```css
:root {
  --um-glassmorphism-bg: #0b0b12;
  --um-glassmorphism-surface-1: rgb(255 255 255 / .14);
  --um-glassmorphism-surface-2: rgb(255 255 255 / .22);
  --um-glassmorphism-surface-fallback: #202331;
  --um-glassmorphism-ink: #ffffff;
  --um-glassmorphism-ink-muted: rgb(255 255 255 / .78);
  --um-glassmorphism-border: rgb(255 255 255 / .42);
  --um-glassmorphism-border-strong: rgb(255 255 255 / .62);
  --um-glassmorphism-focus: #f8d34f;
  --um-glassmorphism-blur-sm: 10px;
  --um-glassmorphism-blur-md: 20px;
  --um-glassmorphism-blur-lg: 32px;
  --um-glassmorphism-shadow-1: 0 8px 32px -8px rgb(0 0 0 / .38);
  --um-glassmorphism-radius-sm: 10px;
  --um-glassmorphism-radius-md: 16px;
  --um-glassmorphism-radius-lg: 20px;
  --um-glassmorphism-radius-pill: 999px;
  --um-glassmorphism-target-min: 44px;
}
```

## Material hierarchy

`backdrop → blur → tint → optional saturation → rim → shadow → content`

Use at most two meaningful glass levels and avoid nested backdrop sampling.

## Button

```css
.glass-button {
  min-height: var(--um-glassmorphism-target-min);
  padding: 10px 16px;
  border: 1px solid var(--um-glassmorphism-border);
  border-radius: var(--um-glassmorphism-radius-pill);
  background: rgb(255 255 255 / .88);
  color: #101426;
  font: inherit;
  font-weight: 650;
}
.glass-button:hover { background: rgb(255 255 255 / .96); }
.glass-button:active { transform: translateY(1px); }
.glass-button:focus-visible { outline: 3px solid var(--um-glassmorphism-focus); outline-offset: 3px; }
.glass-button:disabled { opacity: .62; }
```

Selected/loading/error meaning must use explicit semantic cues rather than transparency or glow alone.

## Card / panel

```css
.glass-card {
  padding: 20px;
  border: 1px solid var(--um-glassmorphism-border);
  border-radius: var(--um-glassmorphism-radius-lg);
  background: var(--um-glassmorphism-surface-fallback);
  box-shadow: var(--um-glassmorphism-shadow-1);
}
@supports (backdrop-filter: blur(1px)) {
  .glass-card {
    background: var(--um-glassmorphism-surface-1);
    backdrop-filter: blur(var(--um-glassmorphism-blur-md)) saturate(160%);
  }
}
```

Use Glass for short bounded content. Dense tables, long reading and large editable forms use stable opaque surfaces.

## Input / form

```css
.glass-input {
  min-height: var(--um-glassmorphism-target-min);
  width: 100%;
  padding: 10px 12px;
  border: 1px solid var(--um-glassmorphism-border-strong);
  border-radius: var(--um-glassmorphism-radius-sm);
  background: var(--um-glassmorphism-surface-fallback);
  color: var(--um-glassmorphism-ink);
}
.glass-input:focus-visible {
  outline: 3px solid var(--um-glassmorphism-focus);
  outline-offset: 2px;
}
```

Persistent labels and text/icon validation remain mandatory.

## Navigation, modal and data

Use one shared glass shell for navigation/toolbars. Modal surfaces require a stabilizing scrim and focus management. Data-heavy content remains opaque; optional glass is limited to surrounding chrome.

## State hierarchy

`semantic state → explicit indicator → material effect → decorative glow`

Focus, selected, disabled, loading and validation states survive removal of blur/transparency.

## Responsive and accessibility

Reduce blur/transparency before reducing control size. Test worst-case backdrops, keyboard/focus, accessible names, large text/localization, forced colors/high contrast and reduced transparency/effects.

## Fallback ladder

```text
full glass
→ tinted opaque surface
→ flat opaque surface
```

The same labels, state semantics, focus and interaction survive every stage.

## Performance

Blur only bounded surfaces, avoid nested glass, do not animate blur continuously, and remove blur before semantic boundaries or state indicators on constrained devices.
