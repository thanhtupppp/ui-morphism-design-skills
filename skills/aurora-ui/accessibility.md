# Accessibility Guide - Aurora UI

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Aurora UI Challenge
Aurora UI dùng gradient nhiều màu, có thể làm contrast không đều. Giải pháp:
- Dùng text color đậm (đen, trắng) trên gradient
- Thêm semi-transparent overlay dưới text areas
- Test contrast tại multiple points trên gradient

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Gradient Best Practices

### Readable Text on Gradients
```css
/* Bad: Text directly on gradient */
.aurora-hero {
  background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
  color: #fff; /* May have low contrast in some areas */
}

/* Good: Overlay for text readability */
.aurora-hero {
  background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
  position: relative;
}

.aurora-hero__content {
  position: relative;
  z-index: 1;
}

.aurora-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.3); /* Dark overlay */
  z-index: 0;
}
```

### Gradient Animation
```css
/* Subtle gradient animation */
.aurora-background {
  background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #fbc2eb);
  background-size: 400% 400%;
  animation: aurora 15s ease infinite;
}

@keyframes aurora {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .aurora-background {
    animation: none;
    background-position: 0% 50%;
  }
}
```

## Focus States

### Keyboard Navigation
```css
/* Aurora focus state example */
.aurora-button:focus {
  outline: 2px solid #fff;
  outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.3);
}

/* Focus-visible for better UX */
.aurora-button:focus:not(:focus-visible) {
  outline: none;
  box-shadow: none;
}

.aurora-button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}
```

## Reduced Motion

### CSS Implementation
```css
/* Default aurora with animation */
.aurora-card {
  background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb);
  background-size: 300% 300%;
  animation: aurora-shift 10s ease infinite;
  transition: transform 0.3s ease;
}

.aurora-card:hover {
  transform: translateY(-4px);
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .aurora-card {
    animation: none;
    background-size: 100% 100%;
    transition: none;
  }
  
  .aurora-card:hover {
    transform: none;
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<section class="aurora-hero" aria-label="Welcome section">
  <h1>Welcome to Our Platform</h1>
  <p>Build amazing things with us</p>
  <a href="/signup" class="aurora-button">Get Started</a>
</section>

<!-- Bad: Div soup -->
<div class="aurora-hero">
  <div class="aurora-title">Welcome to Our Platform</div>
  <div class="aurora-subtitle">Build amazing things with us</div>
  <div class="aurora-button" onclick="navigate('/signup')">Get Started</div>
</div>
```

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.aurora-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
  border-radius: 8px;
}

.aurora-icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text (test at multiple gradient points)
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] Gradient không làm text khó đọc
- [ ] Gradient animation subtle (not distracting)
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Gradient Accessibility](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
