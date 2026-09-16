# Real Code Examples

Each style directory contains implementation seeds:

- `example.css` contains tokenized HTML/CSS and interaction states.
- `example.tsx` contains a React component using semantic HTML and accessible states.
- `example.flutter.dart` contains the Flutter widget seed.
- `example.native.tsx` contains the React Native seed.
- `platforms.md` contains the Flutter mapping and cross-platform implementation rules.

These examples are intentionally small, composable primitives rather than complete product screens. For React/Next.js, copy the semantic component and CSS recipe into the host project, then replace literal values with generated semantic tokens.

For Flutter, translate the same semantic decisions into `ThemeExtension`/theme data, standard Material/Cupertino controls, `BoxDecoration`/`BoxShadow`, bounded `BackdropFilter` where required, and explicit `Semantics`/Focus behavior for custom controls.

## Usage

```tsx
import { AuroraHero } from './skills/aurora-ui/example';

export default function Page() {
  return <AuroraHero />;
}
```

The example is an implementation seed, not permission to apply every effect globally. Keep the selected style's boundaries, fallback, responsive, accessibility, and performance rules.

## Interactive editorial example

Run `npm ci` and `npm run dev` from the repository root to explore `SwissEditorialExample` from `skills/swiss-editorial/example.tsx`. It demonstrates category/search composition, local bookmarks, inline reading, empty-state recovery, and explicit theme selection. The preview imports the real seed. `npm run build` type-checks the web preview; `npm test` exercises the built app after installing Playwright Chromium. Native setup and verification boundaries are documented in `skills/swiss-editorial/platforms.md` and `verification.md`.
