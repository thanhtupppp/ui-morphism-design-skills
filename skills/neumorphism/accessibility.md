# Accessibility Guide - Neumorphism

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Neumorphism Challenge
Neumorphism thường dùng màu monochromatic với contrast thấp. Giải pháp:
- Dùng màu đậm hơn cho text ( không cùng hue với background)
- Thêm inner shadow hoặc border mỏng để tách element
- Test contrast với nhiều background colors

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Focus States

### Keyboard Navigation
```css
/* Neumorphism focus state example */
.neumo-button:focus {
  outline: none;
  box-shadow: 
    8px 8px 16px var(--shadow-dark),
    -8px -8px 16px var(--shadow-light),
    inset 0 0 0 3px rgba(100, 150, 255, 0.4);
}

/* Focus-visible for better UX */
.neumo-button:focus:not(:focus-visible) {
  box-shadow: 
    8px 8px 16px var(--shadow-dark),
    -8px -8px 16px var(--shadow-light);
}

.neumo-button:focus-visible {
  box-shadow: 
    8px 8px 16px var(--shadow-dark),
    -8px -8px 16px var(--shadow-light),
    inset 0 0 0 3px rgba(100, 150, 255, 0.4);
}
```

### Focus Indicators
- Always visible, minimum 2px width
- High contrast (dừng màu neumorphism, dùng accent color)
- Don't rely on color alone (add inset shadow hoặc outline)

## Reduced Motion

### CSS Implementation
```css
/* Default neumorphism with transitions */
.neumo-card {
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.neumo-card:hover {
  box-shadow: 
    12px 12px 24px var(--shadow-dark),
    -12px -12px 24px var(--shadow-light);
  transform: translateY(-2px);
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .neumo-card {
    transition: none;
  }
  
  .neumo-card:hover {
    transform: none;
  }
}
```

## Performance Optimization

### Shadow Performance
Neumorphism dùng nhiều box-shadow có thể gây chậm trên mobile:

```css
/* Good: Simple shadows */
.neumo-element {
  box-shadow: 
    8px 8px 16px rgba(0, 0, 0, 0.15),
    -8px -8px 16px rgba(255, 255, 255, 0.8);
}

/* Bad: Too many shadows, high blur */
.neumo-element {
  box-shadow: 
    5px 5px 10px rgba(0, 0, 0, 0.1),
    10px 10px 20px rgba(0, 0, 0, 0.1),
    -5px -5px 10px rgba(255, 255, 255, 0.8),
    -10px -10px 20px rgba(255, 255, 255, 0.8),
    inset 2px 2px 4px rgba(0, 0, 0, 0.1);
}
```

### Mobile Optimization
```css
/* Reduce shadow complexity on mobile */
@media (max-width: 768px) {
  .neumo-element {
    box-shadow: 
      4px 4px 8px rgba(0, 0, 0, 0.12),
      -4px -4px 8px rgba(255, 255, 255, 0.8);
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<button class="neumo-button" aria-label="Submit form">
  <span class="visually-hidden">Submit</span>
  <svg aria-hidden="true">...</svg>
</button>

<!-- Bad: Div with onclick -->
<div class="neumo-button" onclick="submit()">
  <svg>...</svg>
</div>
```

### ARIA Labels
- Use `aria-label` for icon-only buttons
- Use `aria-labelledby` to reference headings
- Use `aria-pressed` for toggle buttons (neumorphism deboss = pressed)

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.neumo-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
}

.neumo-icon-button {
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
- [ ] Shadows optimized for performance (max 2-3 shadows)
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [CSS Shadow Performance](https://developers.google.com/web/updates/2016/06/css-shadow-painting-performance)
