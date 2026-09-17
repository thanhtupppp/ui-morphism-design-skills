# Accessibility Guide - Glassmorphism

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Focus States

### Keyboard Navigation
```css
/* Glassmorphism focus state example */
.glass-button:focus {
  outline: 2px solid rgba(255, 255, 255, 0.8);
  outline-offset: 2px;
  box-shadow: 
    0 0 0 4px rgba(255, 255, 255, 0.3),
    var(--glass-shadow);
}

/* Focus-visible for better UX */
.glass-button:focus:not(:focus-visible) {
  outline: none;
}

.glass-button:focus-visible {
  outline: 2px solid rgba(255, 255, 255, 0.8);
  outline-offset: 2px;
}
```

### Focus Indicators
- Always visible, minimum 2px width
- High contrast against glass background
- Don't rely on color alone (add outline/box-shadow)

## Reduced Motion

### CSS Implementation
```css
/* Default glassmorphism with transitions */
.glass-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.glass-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--glass-shadow-hover);
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .glass-card {
    transition: none;
  }
  
  .glass-card:hover {
    transform: none;
  }
}
```

### JavaScript Implementation
```javascript
// Check for reduced motion preference
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Disable animations
  element.style.transition = 'none';
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<article class="glass-card" aria-labelledby="card-title">
  <h3 id="card-title">Product Name</h3>
  <p class="glass-description">Product description here</p>
  <button class="glass-button" aria-label="Add Product Name to cart">
    Add to Cart
  </button>
</article>

<!-- Bad: Div soup -->
<div class="glass-card">
  <div class="glass-title">Product Name</div>
  <div class="glass-desc">Product description here</div>
  <div class="glass-btn" onclick="addToCart()">Add to Cart</div>
</div>
```

### ARIA Labels
- Use `aria-label` for icon-only buttons
- Use `aria-labelledby` to reference headings
- Use `aria-describedby` for additional context
- Avoid `aria-hidden="true"` on interactive elements

### Live Regions
```html
<!-- Announce dynamic content changes -->
<div aria-live="polite" aria-atomic="true" class="sr-only">
  {notificationMessage}
</div>
```

## Color & Visual Design

### Background Transparency
```css
/* Ensure text readability on glass backgrounds */
.glass-card {
  background: rgba(255, 255, 255, 0.15); /* Not too transparent */
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

/* Add subtle overlay for text areas */
.glass-card__content {
  background: rgba(255, 255, 255, 0.05);
  padding: 16px;
  border-radius: 8px;
}
```

### Color Blindness Considerations
- Don't use color alone to convey information
- Add icons, patterns, or text labels
- Test with color blindness simulators:
  - Chrome DevTools: Rendering > Emulate vision deficiencies
  - Figma: Color Blind plugin
  - Online: Toptal Color Blind Filter

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.glass-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px; /* Generous padding */
}

/* Icon button with adequate touch area */
.glass-icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text
- [ ] Dynamic content changes announced (aria-live)

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Inclusive Components](https://inclusive-components.design/)
