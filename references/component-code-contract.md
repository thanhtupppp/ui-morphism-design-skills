# Component-Level Code Contract

Every style folder must document component recipes and a platform mapping. The agent must read the selected style's `SKILL.md`, `components.md`, `platforms.md`, and runnable examples before writing frontend code.

## Required component coverage

For each selected style, define concrete values and code for:

- Page/background surface.
- Button: default, hover (where supported), active/pressed, selected, disabled, loading, and focus-visible.
- Card/panel.
- Input/form field.
- Navigation or toolbar.
- Modal, alert, badge, table, or style-specific control where applicable.
- Opacity, blur, shadow/elevation, radius, border, typography, spacing, and target-size decisions.

## Required platform coverage

For every target requested by the project, provide:

- HTML/CSS recipe using semantic HTML and progressive enhancement where required.
- React recipe using semantic DOM and the host project's styling approach.
- Flutter recipe using the platform's theme/component primitives and explicit semantics/focus behavior.
- React Native recipe using native interaction primitives and the shared adapter contract.
- Additional target mapping when the project requests another renderer.

The platform recipe may approximate an optional visual effect, but it must preserve the semantic token, state, hierarchy, and interaction intent.

## Required runnable examples

Every style must provide four small implementation seeds:

- `example.css` — web/CSS progressive-enhancement baseline.
- `example.tsx` — React/semantic DOM baseline.
- `example.flutter.dart` — Flutter/theme-native baseline.
- `example.native.tsx` — React Native/native-primitive baseline.

The React Native seed must demonstrate a native interaction primitive, accessible state, available-width adaptation, a minimum 48px target for primary tappable controls, and a deterministic fallback for unsupported decoration.

## Required output from the agent

Produce the implementation in this order so the result is auditable:

1. **Decision record** — name the primary style, any bounded supporting style, component roles, material/effect choices, and the reason those choices fit the product constraints.
2. **Semantic token record** — list the semantic roles and canonical style tokens that back them; do not expose generic token names such as `--primary` or `--surface` in reusable CSS.
3. **Component recipes** — provide the required component states and their semantic anatomy before optional visual effects.
4. **Platform mappings** — map the same roles and states to every requested renderer; use the native interaction primitive for that renderer whenever available.
5. **Responsive/adaptive rule** — state what changes at compact, medium, and expanded widths and what must remain invariant.
6. **Accessibility rule** — state names/labels, keyboard or touch behavior, focus treatment, state exposure, text scaling, localization, and high-contrast/forced-colors behavior.
7. **Fallback rule** — state the exact degradation path for unsupported, disabled, or reduced effects.
8. **Verification record** — state the viewport/device checks, interaction states, accessibility checks, fallback checks, and performance-sensitive effects that were verified.

Use this machine-readable field set when a compact output is required:

```text
Style:
Primary surface:
Secondary surface:
Text opacity:
Decorative opacity:
Blur:
Shadow/elevation:
Radius:
Border:
Typography:
Spacing:
Minimum target:
Focus ring:
Button recipe:
Card recipe:
Input recipe:
Navigation recipe:
Platform mappings:
Responsive/adaptive rule:
Accessibility/semantics rule:
Reduced-motion/transparency rule:
Unsupported-effect fallback:
Performance constraint:
Verification:
```

### Output invariants

- Never return a platform recipe without its corresponding semantic role and state model.
- Never describe an effect without its capability tier (`required`, `preferred`, or `optional`) and fallback.
- Never claim a state is implemented when it exists only through decoration or animation.
- Never omit the verification record for generated or modified example code.
- Never omit the React Native seed when React Native is a requested target.
- Primary React Native tappable controls must target at least 48px in their minimum dimension.

## Semantic-state rule

State must remain understandable after removing decorative effects. Do not use color, shadow, opacity, blur, glow, texture, or motion as the only channel for selection, error, disabled, success, or focus.

## Responsive rule

The same component anatomy must survive compact, medium, and expanded widths. Do not solve localization/text scaling with fixed heights or clipped overflow.
