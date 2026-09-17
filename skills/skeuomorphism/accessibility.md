# Accessibility Guide - Skeuomorphism

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Skeuomorphism Challenge
Skeuomorphism dùng textures phức tạp, có thể làm contrast không đều. Giải pháp:
- Dùng text color đậm trên textured backgrounds
- Thêm semi-transparent overlay dưới text areas
- Test contrast tại multiple points trên texture

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Texture Best Practices

### Readable Text on Textures
```css
/* Bad: Text directly on wood texture */
.skeuo-notebook {
  background: url('wood-texture.jpg');
  color: #333; /* May have low contrast in some areas */
}

/* Good: Overlay for text readability */
.skeuo-notebook {
  background: url('wood-texture.jpg');
  position: relative;
}

.skeuo-notebook__content {
  position: relative;
  z-index: 1;
  background: rgba(255, 255, 255, 0.9); /* Semi-transparent overlay */
  padding: 16px;
}
```

## Focus States

### Keyboard Navigation
```css
/* Skeuomorphism focus state example */
.skeuo-button:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
  box-shadow: 
    inset 2px 2px 4px rgba(0, 0, 0, 0.3),
    inset -2px -2px 4px rgba(255, 255, 255, 0.8),
    0 0 0 4px rgba(255, 255, 255, 0.5);
}

/* Focus-visible for better UX */
.skeuo-button:focus:not(:focus-visible) {
  outline: none;
  box-shadow: 
    inset 2px 2px 4px rgba(0, 0, 0, 0.3),
    inset -2px -2px 4px rgba(255, 255, 255, 0.8);
}

.skeuo-button:focus-visible {
  outline: 2px solid #000;
  outline-offset: 2px;
}
```

## Reduced Motion

### CSS Implementation
```css
/* Skeuomorphism with subtle transitions */
.skeuo-button {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.skeuo-button:active {
  transform: scale(0.98);
  box-shadow: 
    inset 3px 3px 6px rgba(0, 0, 0, 0.4),
    inset -3px -3px 6px rgba(255, 255, 255, 0.8);
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .skeuo-button {
    transition: none;
  }
  
  .skeuo-button:active {
    transform: none;
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<article class="skeuo-notebook" aria-labelledby="notebook-title">
  <h2 id="notebook-title">My Notes</h2>
  <ul class="skeuo-paper-list">
    <li class="skeuo-paper">Note 1</li>
    <li class="skeuo-paper">Note 2</li>
  </ul>
</article>

<!-- Bad: Div soup -->
<div class="skeuo-notebook">
  <div class="skeuo-title">My Notes</div>
  <div class="skeuo-list">
    <div class="skeuo-item">Note 1</div>
    <div class="skeuo-item">Note 2</div>
  </div>
</div>
```

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.skeuo-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
  /* Skeuomorphic details don't reduce touch area */
}

.skeuo-icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text (test at multiple texture points)
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] Textures không làm text khó đọc
- [ ] Light source consistent across component
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Skeuomorphism Design Guide](https://www.interaction-design.org/encyclopedia/skeuomorphism/)
