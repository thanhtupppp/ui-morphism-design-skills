# Example Quality Gates

This contract defines what a style example must demonstrate before it is treated as production-ready reference code.

## Gate A — semantics
- Use native semantic controls for interaction.
- Expose selected, pressed, disabled, busy/loading, invalid, and expanded state when applicable.
- Keep accessible names, labels, and relationships independent from decoration.

## Gate B — responsive behavior
- Web examples must demonstrate a compact breakpoint or a content-driven responsive rule.
- Flutter examples must demonstrate compact/medium/expanded intent with `LayoutBuilder`, `MediaQuery`, `Wrap`, `GridView`, or an equivalent adaptive primitive.
- Never use fixed heights to solve wrapping or localization.

## Gate C — motion and visual fallback
- CSS examples with interactive motion must include `prefers-reduced-motion` handling.
- Effect-heavy examples must include a deterministic fallback before or alongside the enhancement.
- Forced-colors/high-contrast paths must retain visible boundaries, focus, and state meaning.

## Gate D — target size
- Web interactive examples should expose a minimum target policy and prefer at least 44 CSS px where practical.
- Flutter tappable controls should target at least 48x48 logical pixels.
- React Native primary tappable controls should target at least 48x48 logical pixels.

## Gate E — material-effect budget
- Blur, backdrop sampling, large filters, layered shadows, and animated gradients must be bounded to small surfaces.
- Decorative effects may be removed without changing component hierarchy or meaning.

## Gate F — cross-platform equivalence
For the same component, compare semantic anatomy rather than pixels:

`role → content hierarchy → interaction state → responsive behavior → accessibility → visual treatment → fallback`

A renderer may use different primitives while preserving this sequence.

## Gate G — React Native adapter
- React Native implementations must have a deterministic mapping for semantic roles, state, spacing, shape, effects, responsive behavior, accessibility, and fallback.
- Prefer `Pressable`, `TextInput`, `Switch`, `Slider`, and other native semantic primitives over custom painted controls.
- Unsupported blur, shadow, gradient, or advanced motion must degrade to a simpler native surface without changing hierarchy or meaning.
- Responsive behavior must use available-width primitives such as Flexbox, `useWindowDimensions`, `onLayout`, or the product's established breakpoint system.
- The canonical mapping contract is `references/react-native-adapter.md`.

## Gate H — accessibility parity
- Keyboard focus must remain visible without relying only on `box-shadow`.
- Forced-colors/high-contrast must preserve boundaries, focus, labels, and state meaning.
- Form controls must expose an accessible name through a visible label or equivalent semantic naming mechanism.
- Disabled, pressed, selected, loading, and error states must remain understandable when decorative effects are removed.
- Translucent/atmospheric examples should honor reduced-transparency preferences or provide an opaque replacement when the effect is intentionally disabled.
- The canonical accessibility contract is `references/accessibility-parity.md`.

## Warning policy
Validator warnings are quality-debt signals, not permission to weaken a contract. Resolve warnings by improving the example or documentation. Only promote a warning to a hard failure when the missing behavior is necessary for portability, accessibility, correctness, or repository integrity.
