# Accessibility Guide - Neobrutalism

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Neobrutalism Advantage
Neobrutalism thường có contrast rất cao (đen/trắng, neon). Tuy nhiên:
- Test contrast với neon colors (đoi khi không đạt 4.5:1)
- Đảm bảo text readable trên background sặc sỡ
- Tránh dùng quá nhiều neon cùng lúc (gating mỏi mắt)

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Focus States

### Keyboard Navigation
```css
/* Neobrutalism focus state example */
.neumo-button:focus {
  outline: 3px solid #000;
  outline-offset: 3px;
  box-shadow: 4px 4px 0 #000;
}

/* Alternative: Bold background change */
.neumo-button:focus {
  outline: none;
  background-color: #000;
  color: #fff;
  box-shadow: none;
}

/* Focus-visible for better UX */
.neumo-button:focus:not(:focus-visible) {
  outline: none;
  box-shadow: 4px 4px 0 #000;
}

.neumo-button:focus-visible {
  outline: 3px solid #000;
  outline-offset: 3px;
}
```

### Focus Indicators
- Always visible, minimum 3px width (bold như style neobrutalism)
- High contrast (đen, trắng, hoặc neon đối lập)
- Don't rely on color alone (add outline hoặc shadow)

## Reduced Motion

### CSS Implementation
```css
/* Neobrutalism with minimal or no transitions */
.neumo-button {
  transition: none; /* Brutalist: instant state changes */
}

.neumo-button:hover {
  background-color: #ff0;
  box-shadow: 6px 6px 0 #000;
}

/* Respect reduced motion preference (already minimal) */
@media (prefers-reduced-motion: reduce) {
  .neumo-button {
    transition: none;
  }
}
```

## High Contrast Considerations

### Avoid Eye Strain
Neobrutalism dùng contrast cao, nhưng:
- Tránh dùng 100% đen (#000) trên 100% trắng (#fff) cho large text areas
- Dùng off-black (#111) hoặc off-white (#fefefe) cho comfort
- Limit neon colors cho accents, không dùng cho large backgrounds

```css
/* Better than pure black/white */
.neumo-card {
  background: #fefefe; /* off-white */
  border: 3px solid #111; /* off-black */
  color: #111;
}

/* Neon accents only */
.neumo-accent {
  background: #ff0; /* neon yellow */
  border: 3px solid #000;
  color: #000;
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<button class="neumo-button" aria-label="Submit form">
  SUBMIT
</button>

<nav aria-label="Main navigation">
  <a href="/" class="neumo-link" aria-current="page">HOME</a>
  <a href="/about" class="neumo-link">ABOUT</a>
</nav>

<!-- Bad: Div soup -->
<div class="neumo-button" onclick="submit()">SUBMIT</div>
<div class="neumo-link">HOME</div>
```

### ARIA Labels
- Use `aria-label` for icon-only buttons
- Use `aria-labelledby` to reference headings
- Use `aria-current="page"` for active links

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
  border: 3px solid #000;
}

.neumo-icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 3px solid #000;
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] High contrast không gây mỏi mắt (test với large text areas)
- [ ] Neon colors chỉ dùng cho accents
- [ ] Color not used as sole indicator
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Neobrutalism in Web Design](https://www.awwwards.com/neobrutalism-in-web-design-what-is-it-and-how-to-use-it.html)
