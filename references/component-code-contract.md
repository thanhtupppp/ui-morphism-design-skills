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
- Additional target mapping when the project requests another renderer.

The platform recipe may approximate an optional visual effect, but it must preserve the semantic token, state, hierarchy, and interaction intent.

## Required output from the agent

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
```

## Semantic-state rule

State must remain understandable after removing decorative effects. Do not use color, shadow, opacity, blur, glow, texture, or motion as the only channel for selection, error, disabled, success, or focus.

## Responsive rule

The same component anatomy must survive compact, medium, and expanded widths. Do not solve localization/text scaling with fixed heights or clipped overflow.
