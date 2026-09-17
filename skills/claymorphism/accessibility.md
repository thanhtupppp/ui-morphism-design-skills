# Accessibility Guide - Claymorphism

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Claymorphism Challenge
Claymorphism dùng màu soft, pastel với contrast thấp. Giải pháp:
- Dùng màu đậm hơn cho text (contrast với background)
- Thêm border mỏng hoặc inner shadow để tách element
- Test contrast với nhiều background colors

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Focus States

### Keyboard Navigation
```css
/* Claymorphism focus state example */
.clay-button:focus {
  outline: none;
  box-shadow: 
    inset 4px 4px 8px rgba(0, 0, 0, 0.1),
    inset -4px -4px 8px rgba(255, 255, 255, 0.8),
    4px 4px 8px rgba(0, 0, 0, 0.15),
    -4px -4px 8px rgba(255, 255, 255, 0.8),
    0 0 0 3px rgba(100, 150, 255, 0.4);
}

/* Focus-visible for better UX */
.clay-button:focus:not(:focus-visible) {
  box-shadow: 
    inset 4px 4px 8px rgba(0, 0, 0, 0.1),
    inset -4px -4px 8px rgba(255, 255, 255, 0.8),
    4px 4px 8px rgba(0, 0, 0, 0.15),
    -4px -4px 8px rgba(255, 255, 255, 0.8);
}

.clay-button:focus-visible {
  box-shadow: 
    inset 4px 4px 8px rgba(0, 0, 0, 0.1),
    inset -4px -4px 8px rgba(255, 255, 255, 0.8),
    4px 4px 8px rgba(0, 0, 0, 0.15),
    -4px -4px 8px rgba(255, 255, 255, 0.8),
    0 0 0 3px rgba(100, 150, 255, 0.4);
}
```

### Focus Indicators
- Always visible, minimum 2px width
- High contrast (dừng màu claymorphism, dùng accent color)
- Don't rely on color alone (add outline hoặc glow effect)

## Reduced Motion

### CSS Implementation
```css
/* Default claymorphism with transitions */
.clay-card {
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.clay-card:hover {
  box-shadow: 
    inset 6px 6px 12px rgba(0, 0, 0, 0.1),
    inset -6px -6px 12px rgba(255, 255, 255, 0.8),
    6px 6px 12px rgba(0, 0, 0, 0.15),
    -6px -6px 12px rgba(255, 255, 255, 0.8);
  transform: translateY(-2px);
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .clay-card {
    transition: none;
  }
  
  .clay-card:hover {
    transform: none;
  }
}
```

## 3D Effect Considerations

### Avoid Motion Sickness
- Keep shadows subtle (not too deep or harsh)
- Avoid excessive depth changes on hover
- Provide option to reduce 3D effects

```css
/* Reduced 3D mode */
@media (prefers-reduced-motion: reduce) {
  .clay-element {
    box-shadow: 
      inset 2px 2px 4px rgba(0, 0, 0, 0.05),
      inset -2px -2px 4px rgba(255, 255, 255, 0.8),
      2px 2px 4px rgba(0, 0, 0, 0.1),
      -2px -2px 4px rgba(255, 255, 255, 0.8);
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<button class="clay-button" aria-label="Submit form">
  <span class="visually-hidden">Submit</span>
  <svg aria-hidden="true">...</svg>
</button>

<!-- Bad: Div with onclick -->
<div class="clay-button" onclick="submit()">
  <svg>...</svg>
</div>
```

### ARIA Labels
- Use `aria-label` for icon-only buttons
- Use `aria-labelledby` to reference headings
- Use `aria-pressed` for toggle buttons

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.clay-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
  border-radius: 20px; /* Large radius for clay look */
}

.clay-icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%; /* Circle for icon buttons */
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] 3D effects subtle (not overwhelming)
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Claymorphism Design Guide](https://www.joshwcomeau.com/claymorphism/)
