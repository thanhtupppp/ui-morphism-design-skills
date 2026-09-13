# UI Morphism Design Skill

## Code-first, cross-platform workflow

1. Analyze product, users, content density, device classes, brand, accessibility needs, target platforms, supported browsers/OS, existing component libraries, rendering constraints, and performance budget.
2. Read `references/comparison-matrix.md`.
3. Read `references/platform-contract.md` and `references/platform-matrix.md`.
4. Select one primary style and at most one supporting style. Treat Bento as a layout system and Aurora as an atmospheric accent; neither should automatically become a full-surface material.
5. Read the selected style's `SKILL.md`, `components.md`, `platforms.md`, and `example.css`/`example.tsx` before implementation.
6. Fill the component-level output contract in `references/component-code-contract.md`.
7. Generate namespaced semantic tokens for surfaces, text, opacity, blur, shadow/elevation, radius, border, focus, spacing, motion, and target size. Keep style tokens separate from semantic roles.
8. Map those tokens to each target: HTML/CSS, React, Flutter, and any additional supported stack. Do not make a CSS-only effect a required dependency for another renderer.
9. Implement concrete recipes for every required component and every required interactive state.
10. Apply capability negotiation: advanced effect -> supported implementation -> reduced effect -> opaque/flat fallback.
11. Read `references/quality-gates.md` and verify semantics, responsive behavior, motion/fallback, target size, effect budget, and cross-platform equivalence for every example produced or modified.
12. Test responsive/adaptive behavior, focus, semantics, contrast, forced colors/high contrast, large text, localization, reduced motion, reduced transparency where applicable, fallback behavior, and performance.

## Hard rules

- No style is considered implemented until its component decisions have corresponding code examples.
- No style is considered cross-platform until its semantic tokens and component decisions have a documented mapping for every requested target.
- Visual effects never carry essential meaning alone. Required state information must survive the removal of blur, texture, glow, shadow, animation, and transparency.
- Prefer native/standard controls for interaction semantics; style the shell instead of rebuilding accessible behavior from scratch.
- A platform adaptation may change the rendering primitive but must preserve the same design intent and state model.

## Target notes

### HTML/CSS and React
Use semantic HTML, namespaced CSS tokens, responsive media/container rules, progressive enhancement for advanced effects, `prefers-reduced-motion`, and `forced-colors` fallbacks.

### Flutter
Use standard Material/Cupertino interaction primitives where practical, `ThemeExtension`/theme data for tokens, `BoxDecoration`/`BoxShadow` for surfaces, `BackdropFilter` only for bounded effects, and `Semantics`/Focus APIs for custom controls. Tappable controls should target at least 48x48 logical pixels.

### React Native and other future targets
Follow the same semantic token contract. Implement supported material/effect primitives locally and fall back deterministically when a capability is unavailable.
