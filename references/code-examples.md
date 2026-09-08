# Real Code Examples

Each style directory now contains executable starter code:

- `example.css` contains tokenized CSS and interaction states.
- `example.tsx` contains a React component using semantic HTML and accessible states.

These examples are intentionally small, composable primitives rather than complete product screens. Copy the pair into a React/Next.js project, then replace literal tokens with the project's generated `--um-*` theme tokens.

## Usage

```tsx
import { AuroraHero } from './skills/aurora-ui/example';

export default function Page() {
  return <AuroraHero />;
}
```

Use the examples as implementation seeds, not as permission to apply every effect globally. Keep the selected style's boundaries, fallback, responsive, accessibility, and performance rules.
