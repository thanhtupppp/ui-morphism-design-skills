# Real Code Examples

Each style directory contains implementation seeds:

- `example.css` contains tokenized HTML/CSS and interaction states.
- `example.tsx` contains a React component using semantic HTML and accessible states.
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
