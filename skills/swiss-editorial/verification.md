# Swiss Editorial verification record

Verified on 2026-09-16. This record covers the new Swiss Editorial seeds; it does not extend runtime coverage to the ten existing styles.

## Decision and capability record

Primary style: Swiss Editorial. No supporting material style. Opaque surfaces, a type-led reading grid, and explicit controls suit the fictional journal. Required capabilities are reading order, text, semantics, state, focus, and responsive layout. The asymmetric grid is preferred; the cover numeral is optional and hidden from assistive technology. System fonts and a single-column native layout provide the fallback. Blur, shadows, external fonts, and animation are absent.

## Checks completed

| Check | Result | Scope |
|---|---|---|
| Repository and quality-gate validators | Pass, 11 styles, no warnings | File presence and source/documentation contracts |
| Root and Swiss Editorial skill validation | Pass | Frontmatter and naming |
| TypeScript and Vite production build | Pass | Web component and preview |
| Playwright Chromium | 11 tests pass | Search/category composition, reset, reading disclosure, save/unsave through filtering, theme precedence, responsive targets, keyboard focus, RTL and enlarged text |
| Automated accessibility scan | No violations in selected axe rules | Light and dark web preview; WCAG 2 A/AA, 2.1 AA, 2.2 AA tags |
| Responsive checks | Pass at 375, 768, 1024, 1440px | No horizontal overflow; controls at least 48px high |
| Forced colors and reduced motion | Pass in browser emulation | Keyboard filtering retains focus outline and selected state |
| Visual review | Desktop, 375px mobile, dark desktop inspected | No clipping or overlapping text in the captured states |
| Flutter analyze | No issues | Seed copied into an isolated Flutter 3.38.5 / Dart 3.10.4 application |
| Flutter widget tests | 3 tests pass | Filter/search/reset, bookmark persistence across filters, compact dark layout with 2x text |
| React Native TypeScript | Pass against React Native 0.87.1 | Seed in an isolated TypeScript project |

The web fixture uses Node 22.22.0; exact npm versions are recorded in the root lockfile. Browser checks run against the production build, not only the development server.

## Repeat web verification

From the repository root:

```bash
npm ci
npm run validate
npm run build
npx playwright install chromium
npm test
```

## Repeat Flutter verification

Create an empty Flutter application in a temporary directory with `flutter create --empty swiss_seed_check`. Copy `example.flutter.dart` to its `lib/swiss_editorial.dart`, then copy this repository's `tests/flutter/swiss_editorial_test.dart` to its `test/swiss_editorial_test.dart`. From that application, run:

```bash
flutter analyze
flutter test test/swiss_editorial_test.dart
```

The fixture imports the copied seed directly; it does not require a particular application package name. The application is a test harness, not part of the shipped skill.

## Remaining integration checks

- Flutter and React Native still require device screen-reader, hardware keyboard, platform high-contrast, safe-area, and OS text-scaling validation in the host app.
- React Native was type-checked, not rendered on a device or simulator.
- Browser automation currently runs Chromium. Safari and Firefox are not covered.
- The axe scan is automated evidence, not a full accessibility certification. Manual screen-reader and content-specific contrast review remain necessary for a production integration.
- Bookmarks are component-local state. Reload/unmount clears them. There is no backend, persistence, or network loading/error path.
- The repository's older regex-based validators do not parse or execute every existing example.

## Implementation references

The preview follows [Vite's application setup](https://vite.dev/guide/), uses [React useId](https://react.dev/reference/react/useId) for instance-specific DOM relationships, and uses [React Native Pressable](https://reactnative.dev/docs/pressable) for native actions.
