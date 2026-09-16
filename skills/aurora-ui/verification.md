# Aurora UI verification record

Verified on 2026-09-16. This record covers the Aurora React example rendered by the root preview.

## Decision and capability record

Primary style: Aurora UI. The ambient fields sit behind stable dark surfaces and never carry content, state, or interaction meaning. Required capabilities are document structure, readable text, semantic controls, explicit pressed state, focus visibility, target geometry, and responsive order. Animated glow is optional; the `effects="off"` path removes it without changing content or behavior.

## Checks completed

| Check | Result | Scope |
|---|---|---|
| TypeScript and Vite production build | Pass | React component and shared preview |
| Playwright Chromium | 9 Aurora tests pass | CTA status, workflow selection, effects fallback, responsive widths, keyboard focus, and forced colors |
| Automated accessibility scan | No violations in selected axe rules | Effects on and off; WCAG 2 A/AA, 2.1 AA, and 2.2 AA tags |
| Responsive checks | Pass at 375, 768, and 1440px | No horizontal overflow; visible links and buttons are at least 48px high |
| Repository and quality validators | Pass | Eleven-style source and documentation contracts |
| Semantic, accessibility, and component parity | Pass | HTML/CSS, React, Flutter, and React Native evidence |

## Repeat verification

From the repository root:

```bash
npm ci
npm run validate
npm run build
npx playwright install chromium
npm test
```

## Remaining integration checks

- Test device screen readers, high contrast, text scaling, and GPU performance in the host application.
- Browser automation currently runs Chromium; Safari and Firefox remain manual checks.
- The automated axe scan is supporting evidence rather than a full accessibility certification.
