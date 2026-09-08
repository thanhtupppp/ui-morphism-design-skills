# Component-Level Code Contract

Every style folder now has `components.md`. The agent must read it after `SKILL.md` and before writing frontend code.

## Required component coverage

For each selected style, define concrete values and code for:

- Page/background surface.
- Button: default, hover, active, disabled, and focus-visible.
- Card/panel.
- Input/form field.
- Navigation or toolbar.
- Modal, alert, badge, table, or style-specific control where applicable.
- Opacity, blur, shadow, radius, border, and target-size decisions.

## Required output from the agent

```text
Style:
Primary surface:
Secondary surface:
Text opacity:
Decorative opacity:
Blur:
Shadow:
Radius:
Border:
Focus ring:
Button recipe:
Card recipe:
Input recipe:
Navigation recipe:
Responsive rule:
Reduced-motion/fallback:
```

Do not return only a style name or generic prose. Every component decision must be backed by a token and a code example. Extend the style's `components.md` when the project introduces a component not covered by the base recipes.
