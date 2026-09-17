# Versioning - Material Design 2 vs Material Design 3

## Overview

Material Design 3 (M3) là version mới nhất, ra mắt 2021, với nhiều thay đổi so với M2.

## Key Differences

### 1. Color System

| Aspect | Material 2 | Material 3 |
|--------|-----------|------------|
| Primary color | Single hue | Tonal palette (5 tones) |
| Secondary colors | Optional | Secondary, Tertiary containers |
| Surface colors | Light/Dark variants | Surface, Surface Variant, Inverse |
| Dynamic color | Android only | Cross-platform (Material You) |

### 2. Typography

| Aspect | Material 2 | Material 3 |
|--------|-----------|------------|
| Font scale | 13 styles | 15 styles (Display, Headline, Title, Body, Label) |
| Line height | Fixed ratios | Optical sizing |
| Weight | Regular, Medium, Bold | More granular weights |

### 3. Elevation & Shadows

| Aspect | Material 2 | Material 3 |
|--------|-----------|------------|
| Shadow style | Soft, diffused | More defined, layered |
| Elevation levels | 0-24 (25 levels) | 0-5 (6 levels, simplified) |
| Surface tint overlay | Yes (on colored surfaces) | Removed (cleaner look) |

### 4. Shape & Radius

| Component | Material 2 | Material 3 |
|-----------|-----------|------------|
| Cards | 4px | 12px |
| Buttons | 4px | 20px (fully rounded) |
| FAB | 50% (circle) | 16px (squircle) |
| Inputs | 4px | 4px (top corners only for filled) |

### 5. Components

| Component | Material 2 | Material 3 |
|-----------|-----------|------------|
| App Bar | Top App Bar | Top App Bar (Small, Medium, Large) |
| Bottom Navigation | Fixed | Navigation Bar (with badges) |
| Bottom Sheet | Modal/Standard | Bottom Sheet (with handle) |
| Chips | Filter, Input, Choice, Action | Assist, Filter, Input, Suggestion |
| FAB | Single | Extended FAB, FAB with icon |
| Cards | Outlined, Elevated, Filled | Elevated, Filled, Outlined, Tonal |

## Migration Guide: M2 → M3

### Step 1: Update Design Tokens

```css
/* Before (M2) */
:root {
  --md-primary: #6200EE;
  --md-primary-variant: #3700B3;
  --md-secondary: #03DAC6;
  --md-background: #FFFFFF;
  --md-surface: #FFFFFF;
  --md-error: #B00020;
}

/* After (M3) */
:root {
  --md-sys-color-primary: #6750A4;
  --md-sys-color-on-primary: #FFFFFF;
  --md-sys-color-primary-container: #EADDFF;
  --md-sys-color-on-primary-container: #21005D;
  --md-sys-color-secondary: #625B71;
  --md-sys-color-secondary-container: #E8DEF8;
  --md-sys-color-tertiary: #7D5260;
  --md-sys-color-surface: #FEF7FF;
  --md-sys-color-surface-variant: #E7E0EC;
}
```

### Step 2: Update Typography

```css
/* Before (M2) */
h1 { font: 96/116% Roboto, sans-serif; font-weight: 300; }
h2 { font: 60/72% Roboto, sans-serif; font-weight: 300; }
h3 { font: 48/56% Roboto, sans-serif; font-weight: 400; }
h4 { font: 34/42% Roboto, sans-serif; font-weight: 400; }
h5 { font: 24/32% Roboto, sans-serif; font-weight: 400; }
h6 { font: 20/28% Roboto, sans-serif; font-weight: 500; }

/* After (M3) */
.display-large { font: 57/64% Roboto, sans-serif; font-weight: 400; }
.display-medium { font: 45/52% Roboto, sans-serif; font-weight: 400; }
.display-small { font: 36/44% Roboto, sans-serif; font-weight: 400; }
.headline-large { font: 32/40% Roboto, sans-serif; font-weight: 400; }
.headline-medium { font: 28/36% Roboto, sans-serif; font-weight: 400; }
.headline-small { font: 24/32% Roboto, sans-serif; font-weight: 400; }
.title-large { font: 22/28% Roboto, sans-serif; font-weight: 400; }
.title-medium { font: 16/24% Roboto, sans-serif; font-weight: 500; }
.title-small { font: 14/20% Roboto, sans-serif; font-weight: 500; }
.body-large { font: 16/24% Roboto, sans-serif; font-weight: 400; }
.body-medium { font: 14/20% Roboto, sans-serif; font-weight: 400; }
.body-small { font: 12/16% Roboto, sans-serif; font-weight: 400; }
.label-large { font: 14/20% Roboto, sans-serif; font-weight: 500; }
.label-medium { font: 12/16% Roboto, sans-serif; font-weight: 500; }
.label-small { font: 11/16% Roboto, sans-serif; font-weight: 500; }
```

### Step 3: Update Components

#### Button

```css
/* M2 Button */
.md-button {
  border-radius: 4px;
  padding: 8px 16px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.089em;
}

/* M3 Button */
.md3-button {
  border-radius: 20px;
  padding: 10px 24px;
  font-weight: 500;
  text-transform: none;
  letter-spacing: 0.01em;
}
```

#### Card

```css
/* M2 Card */
.md-card {
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}

/* M3 Card */
.md3-card {
  border-radius: 12px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15);
}
```

## Compatibility

### Use M2 When:
- Legacy project, migration cost too high
- Design system already built on M2
- Team familiarity with M2

### Use M3 When:
- New project from scratch
- Want latest design trends
- Need dynamic color (Material You)
- Better accessibility out of the box

## Resources

- [Material Design 3 Documentation](https://m3.material.io/)
- [Material Design 2 Archive](https://material.io/design)
- [M3 Migration Guide](https://m3.material.io/getting-started/migration)
- [Material Web Components (M3)](https://github.com/material-components/material-web)
- [Material Tokens (M3)](https://github.com/material-foundation/material-tokens)
