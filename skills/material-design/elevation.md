# Elevation System - Material Design

## Overview

Elevation là khoảng cách z-axis giữa surface và shadow, tạo depth và hierarchy.

## Elevation Levels

| Level | Use Case | Shadow (M2) | Shadow (M3) |
|-------|----------|-------------|-------------|
| 0 | Flat surface, background | none | none |
| 1 | Cards, buttons (resting) | 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24) | 0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15) |
| 2 | Cards (hover), FAB (resting) | 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23) | 0 1px 2px rgba(0,0,0,0.3), 0 2px 6px 2px rgba(0,0,0,0.15) |
| 3 | FAB (hover), dialogs | 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23) | 0 1px 3px rgba(0,0,0,0.3), 0 4px 8px 3px rgba(0,0,0,0.15) |
| 4 | Modal sheets, pickers | 0 15px 25px rgba(0,0,0,0.15), 0 5px 10px rgba(0,0,0,0.05) | 0 2px 3px rgba(0,0,0,0.3), 0 6px 16px 6px rgba(0,0,0,0.15) |
| 5 | Popovers, tooltips | 0 20px 40px rgba(0,0,0,0.12), 0 10px 20px rgba(0,0,0,0.08) | 0 4px 8px 3px rgba(0,0,0,0.15), 0 1px 2px rgba(0,0,0,0.3) |

## CSS Variables

```css
/* Material Design 2 Elevation */
:root {
  --md-elevation-0: none;
  --md-elevation-1: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  --md-elevation-2: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  --md-elevation-3: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  --md-elevation-4: 0 15px 25px rgba(0,0,0,0.15), 0 5px 10px rgba(0,0,0,0.05);
  --md-elevation-5: 0 20px 40px rgba(0,0,0,0.12), 0 10px 20px rgba(0,0,0,0.08);
}

/* Material Design 3 Elevation */
:root {
  --md3-elevation-0: none;
  --md3-elevation-1: 0 1px 2px rgba(0,0,0,0.3), 0 1px 3px 1px rgba(0,0,0,0.15);
  --md3-elevation-2: 0 1px 2px rgba(0,0,0,0.3), 0 2px 6px 2px rgba(0,0,0,0.15);
  --md3-elevation-3: 0 1px 3px rgba(0,0,0,0.3), 0 4px 8px 3px rgba(0,0,0,0.15);
  --md3-elevation-4: 0 2px 3px rgba(0,0,0,0.3), 0 6px 16px 6px rgba(0,0,0,0.15);
  --md3-elevation-5: 0 4px 8px 3px rgba(0,0,0,0.15), 0 1px 2px rgba(0,0,0,0.3);
}
```

## Usage Examples

### Card Component

```css
/* Resting state */
.md-card {
  box-shadow: var(--md-elevation-1);
  transition: box-shadow 0.3s ease;
}

/* Hover state */
.md-card:hover {
  box-shadow: var(--md-elevation-2);
}
```

### FAB Component

```css
/* Resting state */
.md-fab {
  box-shadow: var(--md-elevation-2);
  transition: box-shadow 0.3s ease, transform 0.2s ease;
}

/* Hover state */
.md-fab:hover {
  box-shadow: var(--md-elevation-3);
}

/* Pressed state */
.md-fab:active {
  box-shadow: var(--md-elevation-1);
  transform: scale(0.98);
}
```

### Modal/Dialog

```css
.md-dialog {
  box-shadow: var(--md-elevation-4);
  border-radius: 4px;
  background: white;
}
```

## Animation

### Elevation Transitions
```css
.md-surface {
  transition: box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### State Changes
- Resting → Hover: 300ms ease
- Hover → Pressed: 150ms ease
- Pressed → Resting: 300ms ease

## Best Practices

1. **Use consistent elevation levels** - Don't create custom shadows
2. **Higher elevation = more important** - Use for modals, dialogs, FABs
3. **Animate elevation changes** - Smooth transitions for hover/focus
4. **Consider performance** - Box-shadow can be expensive on mobile
5. **Test on dark backgrounds** - Shadows less visible on dark mode

## Accessibility

- Don't rely on elevation alone to convey hierarchy
- Use semantic HTML (heading levels, ARIA landmarks)
- Ensure focus states are visible regardless of elevation
- Test with high contrast mode enabled

## Resources

- [Material Design 2 Elevation](https://material.io/design/environment/elevation.html)
- [Material Design 3 Elevation](https://m3.material.io/design/environment/elevation.html)
- [Material Web Components](https://github.com/material-components/material-web)
