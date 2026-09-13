# Neumorphism — Cross-Platform Recipes

## Canonical intent
A shared surface with paired light/dark soft shadows creates raised or pressed controls. Contrast, borders, labels, and focus remain explicit.

## HTML/CSS
- Use paired `box-shadow` for raised/pressed states.
- Use a visible border/focus outline for fields and keyboard focus.
- Keep controls bounded; avoid using the effect for complex tables/forms.

## React
- Reuse native controls where possible and apply the visual shell via CSS classes.
- Use `aria-pressed`/native checked state for toggles so state survives the visual fallback.

## Flutter
- Represent paired shadows with `BoxDecoration(boxShadow: [...])` and `inset`-style treatment by using layered containers/foreground gradients when necessary.
- There is no need to reproduce every CSS optical trick. A raised `BoxShadow` plus a strong border/focus state is the preferred portable approximation.
- Keep switches, sliders, text fields, and buttons semantically native; decorate them rather than painting interaction from scratch.

## State recipe
Raised -> paired outer shadows; pressed/selected -> pressed shadow; focus -> explicit high-contrast ring/border; disabled -> semantic disabled styling plus reduced decoration.

## Accessibility/performance
Shadow must never be the only state cue. Reduce shadow count on low-power devices. Provide a Flat/opaque fallback for forced-colors and extreme contrast modes.
