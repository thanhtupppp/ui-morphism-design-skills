# Cross-Platform Design Implementation Contract

The design skill is framework-agnostic at the token and component-decision level. Rendering is adapted to the target platform instead of changing the visual decision.

## Supported targets

- Web HTML/CSS: semantic HTML, CSS custom properties, media queries, progressive enhancement.
- React: semantic DOM plus CSS/className or the project's styling system; preserve native interaction semantics.
- Flutter: Material/Cupertino primitives where useful, `ThemeExtension` for generated tokens, `BoxDecoration`, `DecoratedBox`, `CustomPaint` only when necessary, and `Semantics` for custom controls.
- React Native: map the same semantic tokens to `StyleSheet` and platform capabilities; use native/Skia effects only when the selected style requires them.
- Other UI stacks: map the semantic token model first, then implement only effects supported by the renderer.

## Non-negotiable rule

A style is considered portable when the visual intent can be represented as semantic tokens and each required component has a concrete recipe for the selected target. Do not force a web-only effect into another renderer when the renderer cannot reproduce it reliably.

## Token layers

Separate tokens into four layers:

1. **Semantic** — surface, text, border, accent, focus, danger, success, disabled.
2. **Geometry** — spacing, radius, control height, stroke width, grid columns.
3. **Material/effect** — elevation, shadow, blur, translucency, gradient, highlight.
4. **Motion** — duration, curve, transform distance, reduced-motion behavior.

A platform adapter may change representation, not intent. For example, a CSS `box-shadow` may become Flutter `BoxShadow`, and a CSS opacity value may become `Color.withValues(alpha: ...)` or equivalent in the target SDK.

## Capability tiers

- **Required:** semantic color, typography, spacing, geometry, borders, focus/selected/disabled states, responsive behavior, accessibility labels, and touch/keyboard target sizing.
- **Preferred:** elevation/shadow, gradients, state transitions, scrims, platform-native adaptive controls.
- **Optional:** backdrop blur, displacement, animated glow, texture, reflection, shader effects.

Optional effects must have a deterministic fallback that keeps the component recognizable and usable.

## HTML/React baseline

Use semantic elements (`button`, `a`, `input`, headings, lists, dialogs) before custom div-based controls. CSS should use namespaced semantic variables. Progressive enhancement is required for blur, advanced color effects, and non-essential animation. Honor `prefers-reduced-motion` and forced colors.

## Flutter baseline

Prefer framework controls for semantics and interaction. Put generated style tokens in a `ThemeExtension` or an equivalent inherited theme object. Build surface/effect wrappers with `DecoratedBox`/`Container` and `BoxDecoration`; use `Material`/`PhysicalModel` for elevation semantics where appropriate. Custom painted/shader effects require a simpler fallback. Custom controls must expose semantics and keyboard/Focus behavior. Touch targets should be at least 48x48 logical pixels for tappable controls.

Flutter's web build also has an accessibility semantics layer, so visual customizations must not remove or obscure the semantic structure.

## State matrix

Every interactive component must specify at least: default, hover (where available), focus-visible, pressed/active, selected, disabled, loading, error/success where applicable.

States must remain understandable when decorative effects are removed.

## Responsive matrix

At minimum validate: compact phone (~375px), tablet (~768px), desktop (~1024px), and wide desktop (~1440px) on web; compact, medium, and expanded layouts on Flutter. Prefer content-driven constraints over fixed coordinates.

## Effect fallback policy

`advanced effect -> supported native/web implementation -> reduced effect -> opaque/flat fallback`.

Examples:

- backdrop blur -> native/web blur -> translucent tint -> opaque surface
- animated aurora -> slow gradient animation -> static gradient -> solid background
- texture -> vector/CSS gradient -> flat material
- soft shadow -> platform elevation/shadow -> explicit border

## Acceptance criteria

A platform implementation passes only when:

- The semantic component anatomy is unchanged.
- Required states are testable without hover or animation.
- Keyboard/screen-reader/touch access remains intact.
- Text scaling/localization does not clip controls.
- Unsupported effects degrade without breaking hierarchy.
- Reduced-motion behavior is deterministic.
- Forced colors/high-contrast mode preserves readable text, visible focus, explicit state boundaries, and semantic meaning when decorative effects are removed.
- Performance-sensitive effects are bounded to small surfaces.
