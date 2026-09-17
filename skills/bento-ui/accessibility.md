# Accessibility Guide - Bento UI

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Bento UI Considerations
Bento UI dùng grid modules với background colors khác nhau. Đảm bảo:
- Text contrast đủ trên tất cả module backgrounds
- Border hoặc divider rõ giữa các modules
- Focus states visible trên grid

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Focus States

### Keyboard Navigation
```css
/* Bento focus state example */
.bento-card:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
}

/* Focus-visible for better UX */
.bento-card:focus:not(:focus-visible) {
  outline: none;
}

.bento-card:focus-visible {
  outline: 2px solid #000;
  outline-offset: 2px;
}
```

### Grid Navigation
- Tab order theo logical flow (left-to-right, top-to-bottom)
- Arrow keys navigation cho grid (nếu interactive)
- Focus trap cho modal bento cards

## Responsive Grid

### CSS Grid Implementation
```css
/* Bento grid responsive */
.bento-grid {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(3, 1fr); /* Desktop */
}

@media (max-width: 1024px) {
  .bento-grid {
    grid-template-columns: repeat(2, 1fr); /* Tablet */
  }
}

@media (max-width: 640px) {
  .bento-grid {
    grid-template-columns: 1fr; /* Mobile */
  }
}
```

### Screen Reader Considerations
- Dùng `role="grid"` cho semantic grid
- `aria-rowindex` và `aria-colindex` cho grid cells
- Hoặc đơn giản: semantic HTML với flexbox (screen reader friendly hơn)

## Reduced Motion

### CSS Implementation
```css
/* Bento with minimal transitions */
.bento-card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.bento-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .bento-card {
    transition: none;
  }
  
  .bento-card:hover {
    transform: none;
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<main>
  <h1>Dashboard</h1>
  <div class="bento-grid" role="grid" aria-label="Dashboard widgets">
    <article class="bento-card" aria-labelledby="card-1-title">
      <h2 id="card-1-title">Stats</h2>
      <p>Content here</p>
    </article>
    <article class="bento-card" aria-labelledby="card-2-title">
      <h2 id="card-2-title">Chart</h2>
      <p>Content here</p>
    </article>
  </div>
</main>

<!-- Bad: Div soup -->
<div class="bento-grid">
  <div class="bento-card">
    <div class="bento-title">Stats</div>
    <div>Content here</div>
  </div>
  <div class="bento-card">
    <div class="bento-title">Chart</div>
    <div>Content here</div>
  </div>
</div>
```

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.bento-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
}

.bento-card--interactive {
  cursor: pointer;
}

.bento-card--interactive:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] Grid layout responsive (mobile, tablet, desktop)
- [ ] Grid cells có semantic meaning (article, section)
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [CSS Grid Accessibility](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)
