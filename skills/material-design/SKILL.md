# Material Design Skill

## TL;DR
Material Design (M2 & M3) là hệ thống thiết kế của Google với elevation (z-axis), typography scale, và color system. M3 (Material You) có dynamic color và elevation đơn giản hơn.

## Core Principles
- Elevation system (z-axis depth)
- Typography scale (13 styles M2, 15 styles M3)
- Color system (primary, secondary, tertiary, surface, error)
- Motion principles (easing, duration)
- Responsive grid layouts

## Design Tokens

### M2 (Material Design 2)
```css
:root {
  /* Colors */
  --md2-primary: #6200EE;
  --md2-primary-variant: #3700B3;
  --md2-secondary: #03DAC6;
  --md2-error: #B00020;
  --md2-surface: #FFFFFF;
  --md2-background: #FFFFFF;
  
  /* Elevation */
  --md2-elevation-1: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  --md2-elevation-2: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  --md2-elevation-3: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  
  /* Motion */
  --md2-easing-standard: cubic-bezier(0.4, 0.0, 0.2, 1);
  --md2-easing-decelerate: cubic-bezier(0.0, 0.0, 0.2, 1);
  --md2-easing-accelerate: cubic-bezier(0.4, 0.0, 1, 1);
  --md2-duration-short: 150ms;
  --md2-duration-medium: 300ms;
  --md2-duration-long: 500ms;
}
```

### M3 (Material Design 3 / Material You)
```css
:root {
  /* Colors - Tonal palette */
  --md3-primary: #6750A4;
  --md3-on-primary: #FFFFFF;
  --md3-primary-container: #EADDFF;
  --md3-on-primary-container: #21005D;
  --md3-secondary: #625B71;
  --md3-secondary-container: #E8DEF8;
  --md3-tertiary: #7D5260;
  --md3-surface: #FEF7FF;
  --md3-surface-variant: #E7E0EC;
  
  /* Elevation - Simplified (0-5) */
  --md3-elevation-1: 0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15);
  --md3-elevation-2: 0 1px 2px rgba(0,0,0,0.3), 0 2px 6px 2px rgba(0,0,0,0.15);
  --md3-elevation-3: 0 1px 3px rgba(0,0,0,0.3), 0 4px 8px 3px rgba(0,0,0,0.15);
  
  /* Shape */
  --md3-shape-corner-small: 8px;
  --md3-shape-corner-medium: 12px;
  --md3-shape-corner-large: 16px;
  --md3-shape-corner-extra-large: 28px;
}
```

## Typography

### M2 Typography Scale (13 styles)
```css
/* Display */
h1 { font: 96/116% Roboto, sans-serif; font-weight: 300; }
h2 { font: 60/72% Roboto, sans-serif; font-weight: 300; }
h3 { font: 48/56% Roboto, sans-serif; font-weight: 400; }
h4 { font: 34/42% Roboto, sans-serif; font-weight: 400; }
h5 { font: 24/32% Roboto, sans-serif; font-weight: 400; }
h6 { font: 20/28% Roboto, sans-serif; font-weight: 500; }

/* Body */
.subtitle1 { font: 16/28% Roboto, sans-serif; font-weight: 400; }
.subtitle2 { font: 14/24% Roboto, sans-serif; font-weight: 500; }
.body1 { font: 16/28% Roboto, sans-serif; font-weight: 400; }
.body2 { font: 14/24% Roboto, sans-serif; font-weight: 400; }

/* Other */
.button { font: 14/14% Roboto, sans-serif; font-weight: 500; text-transform: uppercase; }
.caption { font: 12/20% Roboto, sans-serif; font-weight: 400; }
.overline { font: 10/16% Roboto, sans-serif; font-weight: 500; text-transform: uppercase; }
```

### M3 Typography Scale (15 styles)
```css
/* Display */
.display-large { font: 57/64% Roboto, sans-serif; font-weight: 400; }
.display-medium { font: 45/52% Roboto, sans-serif; font-weight: 400; }
.display-small { font: 36/44% Roboto, sans-serif; font-weight: 400; }

/* Headline */
.headline-large { font: 32/40% Roboto, sans-serif; font-weight: 400; }
.headline-medium { font: 28/36% Roboto, sans-serif; font-weight: 400; }
.headline-small { font: 24/32% Roboto, sans-serif; font-weight: 400; }

/* Title */
.title-large { font: 22/28% Roboto, sans-serif; font-weight: 400; }
.title-medium { font: 16/24% Roboto, sans-serif; font-weight: 500; }
.title-small { font: 14/20% Roboto, sans-serif; font-weight: 500; }

/* Body */
.body-large { font: 16/24% Roboto, sans-serif; font-weight: 400; }
.body-medium { font: 14/20% Roboto, sans-serif; font-weight: 400; }
.body-small { font: 12/16% Roboto, sans-serif; font-weight: 400; }

/* Label */
.label-large { font: 14/20% Roboto, sans-serif; font-weight: 500; }
.label-medium { font: 12/16% Roboto, sans-serif; font-weight: 500; }
.label-small { font: 11/16% Roboto, sans-serif; font-weight: 500; }
```

## Motion & Easing

### Easing Curves
```css
/* Standard (default for most animations) */
--md-easing-standard: cubic-bezier(0.4, 0.0, 0.2, 1);

/* Decelerate (entering screen) */
--md-easing-decelerate: cubic-bezier(0.0, 0.0, 0.2, 1);

/* Accelerate (exiting screen) */
--md-easing-accelerate: cubic-bezier(0.4, 0.0, 1, 1);

/* Sharp (quick movements) */
--md-easing-sharp: cubic-bezier(0.4, 0.0, 0.6, 1);
```

### Duration
```css
/* Short: 150ms - small elements, micro-interactions */
--md-duration-short: 150ms;

/* Medium: 300ms - default for most animations */
--md-duration-medium: 300ms;

/* Long: 500ms - large elements, page transitions */
--md-duration-long: 500ms;
```

### Usage Examples
```css
/* Button hover */
.md-button {
  transition: background-color 150ms cubic-bezier(0.4, 0.0, 0.2, 1);
}

/* Card enter animation */
.md-card {
  animation: card-enter 300ms cubic-bezier(0.0, 0.0, 0.2, 1);
}

/* FAB press */
.md-fab:active {
  transition: transform 150ms cubic-bezier(0.4, 0.0, 1, 1);
}
```

## Components
Xem components.md

## Platforms
Xem platforms.md

## Common Pitfalls
- Mixing M2 and M3 tokens in same component
- Using wrong elevation level for context
- Ignoring motion/easing standards
- Not testing dark mode compatibility
