# Accessibility Guide - Flat Design

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Flat Design Challenge
Flat design thường dùng màu bold, vibrant nhưng đôi khi contrast thấp giữa adjacent colors. Giải pháp:
- Test contrast giữa text và background
- Thêm border hoặc outline nếu contrast thấp
- Dùng màu dark cho text trên background sáng và ngược lại

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Focus States

### Keyboard Navigation
```css
/* Flat design focus state example */
.flat-button:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
}

/* Alternative: High contrast background */
.flat-button:focus {
  outline: none;
  background-color: #000;
  color: #fff;
}

/* Focus-visible for better UX */
.flat-button:focus:not(:focus-visible) {
  outline: none;
}

.flat-button:focus-visible {
  outline: 2px solid #000;
  outline-offset: 2px;
}
```

### Focus Indicators
- Always visible, minimum 2px width
- High contrast (đen, trắng, hoặc accent color đậm)
- Don't rely on color alone (add outline hoặc background change)

## Color Usage

### Don't Use Color Alone
Flat design dùng màu bold, nhưng KHÔNG dùng màu làm indicator duy nhất:

```css
/* Bad: Color alone indicates state */
.status-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}
.status-success { background: green; }
.status-error { background: red; }

/* Good: Color + shape/icon */
.status-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  position: relative;
}
.status-success {
  background: green;
}
.status-success::after {
  content: '✓';
  position: absolute;
  color: white;
  font-size: 8px;
}
.status-error {
  background: red;
}
.status-error::after {
  content: '×¹';
  position: absolute;
  color: white;
  font-size: 10px;
}
```

### Color Blindness Considerations
- Test với color blindness simulators
- Thêm icons, patterns, hoặc text labels
- Dùng tools:
  - Chrome DevTools: Rendering > Emulate vision deficiencies
  - Figma: Color Blind plugin
  - Online: Toptal Color Blind Filter

## Reduced Motion

### CSS Implementation
```css
/* Flat design with minimal transitions */
.flat-button {
  transition: background-color 0.2s ease, color 0.2s ease;
}

.flat-button:hover {
  background-color: #000;
  color: #fff;
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .flat-button {
    transition: none;
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<button class="flat-button" aria-label="Submit form">
  Submit
</button>

<nav aria-label="Main navigation">
  <a href="/" class="flat-link" aria-current="page">Home</a>
  <a href="/about" class="flat-link">About</a>
</nav>

<!-- Bad: Div soup -->
<div class="flat-button" onclick="submit()">Submit</div>
<div class="flat-link">Home</div>
```

### ARIA Labels
- Use `aria-label` for icon-only buttons
- Use `aria-labelledby` to reference headings
- Use `aria-current="page"` for active navigation links

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.flat-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
  border-radius: 0; /* or 4px for slight rounding */
}

.flat-icon-button {
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
- [ ] Icons have labels or aria-labels
- [ ] Form labels and error messages announced
- [ ] Images have alt text

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Flat Design Accessibility](https://www.smashingmagazine.com/2017/02/designing-accessible-flat-interfaces/)
