# UI Morphism Design Skill

## Code-first, cross-platform workflow

1. Analyze product, users, content density, device classes, brand, accessibility needs, target platforms, supported browsers/OS, existing component libraries, rendering constraints, and performance budget.
2. Read `references/comparison-matrix.md`.
3. Read `references/platform-contract.md` and `references/platform-matrix.md`.
4. Read `references/token-convention.md` before generating or adapting shared design tokens.
5. Select one primary style and at most one supporting style. Treat Bento as a layout system and Aurora as an atmospheric accent; neither should automatically become a full-surface material.
6. Read the selected style's `SKILL.md`, `components.md`, `platforms.md`, and all runnable examples (`example.css`, `example.tsx`, `example.flutter.dart`, `example.native.tsx`) before implementation.
7. Fill the component-level output contract in `references/component-code-contract.md`: decision record -> semantic token record -> component recipes -> platform mappings -> responsive/accessibility rules -> fallback rule -> verification record.
8. Generate namespaced semantic tokens for surfaces, text, opacity, blur, shadow/elevation, radius, border, focus, spacing, motion, and target size. Use the canonical grammar `--um-<style>-<group>[-<variant>]`; keep style tokens separate from semantic roles and provide opaque fallback tokens for translucent styles.
9. Map those tokens to each target: HTML/CSS, React, Flutter, and any additional supported stack. For React Native, use `references/react-native-adapter.md` as the canonical platform mapping; do not make a CSS-only effect a required dependency for another renderer.
10. Negotiate each visual capability using `references/platform-matrix.md`: preserve required capabilities, adapt preferred effects to the target renderer, and attach a deterministic fallback to optional effects.
11. Implement concrete recipes for every required component and every required interactive state. Mark each advanced effect as required, preferred, or optional and pair it with its deterministic fallback.
12. Apply capability negotiation: advanced effect -> supported implementation -> reduced effect -> opaque/flat fallback.
13. Read `references/quality-gates.md` and `references/semantic-parity.md`. Verify semantics, responsive behavior, motion/fallback, target size, effect budget, cross-platform equivalence, token namespace, theme override behavior, and React Native adapter requirements for every example produced or modified.
14. Record verification for responsive/adaptive behavior, focus, semantics, contrast, forced colors/high contrast, large text, localization, reduced motion, reduced transparency where applicable, fallback behavior, semantic parity, and performance.

## Hard rules

- No style is considered implemented until its component decisions have corresponding code examples.
- No style is considered cross-platform until its semantic tokens and component decisions have a documented mapping for every requested target.
- Every generated or modified example must include an auditable verification record or an equivalent verification summary.
- Every optional visual effect must declare its capability tier and deterministic fallback.
- Shared tokens must follow `references/token-convention.md`; do not introduce unnamespaced reusable aliases.
- Cross-platform examples must preserve semantic anatomy, state meaning, responsive intent, accessibility behavior, and minimum target size; renderer-specific visual differences are allowed.
- Explicit theme selection must override system preference where theme switching is implemented, while forced-colors/high-contrast behavior must remain independently supported.
- Visual effects never carry essential meaning alone. Required state information must survive the removal of blur, texture, glow, shadow, animation, and transparency.

## Target notes

### HTML/CSS
Prefer semantic HTML, namespaced CSS custom properties, responsive layout primitives, progressive enhancement for advanced effects, reduced-motion handling, and forced-colors fallbacks.

### React
Preserve semantic DOM elements and state attributes/props while reusing the same semantic token vocabulary as CSS. Do not move meaning into decorative wrappers.

### Flutter
Prefer native controls and theme data/ThemeExtension, use bounded BackdropFilter only where supported, and keep a 48x48 logical-pixel interaction target for primary controls. Theme overrides must remain deterministic.

### React Native
Use `references/react-native-adapter.md` as the canonical mapping. Prefer native interaction primitives such as Pressable, TextInput, Switch, Checkbox, Slider, and platform navigation. Responsive behavior must adapt to available width, and primary tappable controls should be at least 48px. Advanced visual effects remain optional and must degrade to a readable native surface without changing semantic state.
