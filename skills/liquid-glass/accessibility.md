# Accessibility Guide - Liquid Glass

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Liquid Glass Challenge
Liquid Glass dùng gradients và translucency, có thể làm contrast không đều. Giải pháp:
- Dùng text color đậm (đen, trắng) trên backgrounds
- Thêm semi-transparent overlay dưới text areas
- Test contrast tại multiple points trên gradient

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Liquid Effect Considerations

### Avoid Motion Sickness
- Keep liquid animations subtle (slow, smooth)
- Avoid rapid morphing or color changes
- Provide option to reduce motion

```css
/* Subtle liquid animation */
.liquid-shape {
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: liquid-morph 8s ease-in-out infinite;
}

@keyframes liquid-morph {
  0%, 100% {
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  }
  50% {
    border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
  }
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .liquid-shape {
    animation: none;
    border-radius: 50%; /* Simple circle */
  }
}
```

## Focus States

### Keyboard Navigation
```css
/* Liquid Glass focus state example */
.liquid-button:focus {
  outline: 2px solid #fff;
  outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.3);
}

/* Focus-visible for better UX */
.liquid-button:focus:not(:focus-visible) {
  outline: none;
  box-shadow: none;
}

.liquid-button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}
```

## Reduced Motion

### CSS Implementation
```css
/* Default liquid glass with animation */
.liquid-card {
  background: linear-gradient(135deg, rgba(255,255,255,0.4), rgba(255,255,255,0.1));
  backdrop-filter: blur(10px);
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: liquid-morph 10s ease-in-out infinite;
  transition: transform 0.3s ease;
}

.liquid-card:hover {
  transform: translateY(-4px);
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .liquid-card {
    animation: none;
    border-radius: 16px; /* Simple rounded corners */
    transition: none;
  }
  
  .liquid-card:hover {
    transform: none;
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<article class="liquid-card" aria-labelledby="card-title">
  <h3 id="card-title">Feature Name</h3>
  <p>Description here</p>
  <a href="/learn-more" class="liquid-button">Learn More</a>
</article>

<!-- Bad: Div soup -->
<div class="liquid-card">
  <div class="liquid-title">Feature Name</div>
  <div>Description here</div>
  <div class="liquid-button" onclick="navigate('/learn-more')">Learn More</div>
</div>
```

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.liquid-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
  border-radius: 24px; /* Fully rounded */
}

.liquid-icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text (test at multiple gradient points)
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] Liquid animation subtle (not distracting or nauseating)
- [ ] Gradient không làm text khó đọc
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Motion Accessibility](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)
