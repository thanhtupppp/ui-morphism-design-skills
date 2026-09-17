# Accessibility Guide - Swiss Editorial

## Contrast Requirements

### Text Contrast
- **Normal text (< 18pt)**: Contrast ratio >= 4.5:1 [WCAG 2.1 AA]
- **Large text (>= 18pt)**: Contrast ratio >= 3:1 [WCAG 2.1 AA]
- **UI components & icons**: Contrast ratio >= 3:1 [WCAG 2.1 AA]

### Swiss Editorial Advantage
Swiss Editorial thường có contrast rất cao (đen trên trắng). Tuy nhiên:
- Test contrast với accent colors
- Đảm bảo text nhỏ (captions, footnotes) vẫn đạt 4.5:1
- Avoid pure black (#000) trên pure white (#fff) cho large text (gating mỏi)

### Testing Tools
- Web: Chrome DevTools Accessibility Inspector, axe DevTools
- Mobile: Accessibility Scanner (Android), Xcode Accessibility Inspector (iOS)
- Online: WebAIM Contrast Checker, Contrast Grid

## Typography Hierarchy

### Clear Hierarchy for Screen Readers
```html
<!-- Good: Semantic heading hierarchy -->
<article>
  <h1>Main Headline</h1>
  <p class="byline">By Author Name</p>
  <h2>Section Heading</h2>
  <p>Body text...</p>
  <h3>Subsection</h3>
  <p>More text...</p>
</article>

<!-- Bad: Divs with visual styling only -->
<div>
  <div class="headline">Main Headline</div>
  <div class="byline">By Author Name</div>
  <div class="section">Section Heading</div>
  <div>Body text...</div>
</div>
```

### Typography Scale
```css
/* Swiss typography scale */
:root {
  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px */
  --text-lg: 1.25rem;   /* 20px */
  --text-xl: 1.5rem;    /* 24px */
  --text-2xl: 2rem;     /* 32px */
  --text-3xl: 3rem;     /* 48px */
}

/* Line height for readability */
body {
  font-size: var(--text-base);
  line-height: 1.5; /* 24px for 16px base */
}
```

## Focus States

### Keyboard Navigation
```css
/* Swiss focus state example */
.swiss-link:focus {
  outline: 2px solid #000;
  outline-offset: 2px;
}

/* Focus-visible for better UX */
.swiss-link:focus:not(:focus-visible) {
  outline: none;
}

.swiss-link:focus-visible {
  outline: 2px solid #000;
  outline-offset: 2px;
}
```

## Grid & Layout

### Baseline Grid
```css
/* Baseline grid for vertical rhythm */
:root {
  --baseline: 8px;
}

body {
  font-size: 16px;
  line-height: calc(var(--baseline) * 3); /* 24px */
}

h1, h2, h3, p, ul, ol {
  margin-top: calc(var(--baseline) * 3); /* 24px */
  margin-bottom: calc(var(--baseline) * 3);
}
```

### Responsive Grid
```css
/* Swiss grid responsive */
.swiss-grid {
  display: grid;
  gap: 24px;
  grid-template-columns: repeat(12, 1fr);
}

@media (max-width: 1024px) {
  .swiss-grid {
    grid-template-columns: repeat(8, 1fr);
  }
}

@media (max-width: 640px) {
  .swiss-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

## Reduced Motion

### CSS Implementation
```css
/* Swiss with minimal transitions */
.swiss-link {
  transition: color 0.2s ease;
}

.swiss-link:hover {
  color: #000;
}

/* Respect reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  .swiss-link {
    transition: none;
  }
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- Good: Semantic structure -->
<header role="banner">
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/" aria-current="page">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>

<main role="main">
  <article aria-labelledby="article-title">
    <h1 id="article-title">Article Title</h1>
    <p>Content...</p>
  </article>
</main>

<footer role="contentinfo">
  <p>&copy; 2026 Publication Name</p>
</footer>
```

## Touch Targets

### Minimum Sizes
- **Mobile**: 44x44px (iOS HIG), 48x48dp (Material Design)
- **Desktop**: 24x24px minimum, 44x44px recommended

### Implementation
```css
.swiss-link {
  display: inline-block;
  min-width: 44px;
  min-height: 44px;
  padding: 8px 16px;
}

.swiss-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
}
```

## Testing Checklist

- [ ] Contrast ratio >= 4.5:1 for all text
- [ ] Focus states visible on all interactive elements
- [ ] Keyboard navigation works (Tab, Enter, Escape, Arrow keys)
- [ ] Screen reader announces all content correctly
- [ ] Reduced motion preference respected
- [ ] Touch targets >= 44x44px on mobile
- [ ] Typography hierarchy clear (H1 > H2 > H3 > body)
- [ ] Baseline grid consistent
- [ ] Left-aligned text (no justified)
- [ ] Generous whitespace maintained
- [ ] Color not used as sole indicator

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [Swiss Style Design](https://www.interaction-design.org/encyclopedia/swiss-style/)
