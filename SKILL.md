# UI Morphism Design Skill

## Code-first workflow

1. Analyze product, user, density, device, brand, stack, and constraints.
2. Read `references/comparison-matrix.md`.
3. Select one primary style and at most one supporting style.
4. Read the selected style's `SKILL.md`, `components.md`, and `example.css`/`example.tsx`.
5. Fill the component-level output contract in `references/component-code-contract.md`.
6. Generate namespaced tokens for surfaces, text, opacity, blur, shadow, radius, border, focus, spacing, motion, and target size.
7. Implement concrete recipes for every required component.
8. Test responsive behavior, focus, contrast, forced colors, reduced motion, fallback, and performance.

## Hard rule

No style is considered implemented until its component decisions have corresponding code examples. The style file must specify not only what the style looks like, but how each frontend component is built.
