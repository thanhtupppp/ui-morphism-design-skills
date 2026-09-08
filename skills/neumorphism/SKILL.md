# Neumorphism

## Purpose
Neumorphism makes controls appear raised from or pressed into a shared surface using soft light and dark shadows.

## Use when
- The screen contains compact controls such as thermostat knobs, media transport, clocks, or smart-home actions.
- The product can tolerate a restrained, low-density control surface.

## Avoid when
- The screen contains complex forms, tables, navigation, legal text, or high-density operations.
- The surface/background cannot remain visually stable.
- Contrast and focus cannot be repaired with explicit borders and outlines.

## Visual DNA
- Parent and control share a related base color.
- Use one light direction and paired highlight/contact shadows.
- Use four states deliberately: flat, convex, concave, and pressed.
- Never let shadow be the only enabled, disabled, selected, or focus signal.

## Token recipe
```css
:root {
  --um-neumorphism-bg: #e6e7ee;
  --um-neumorphism-surface-1: #e6e7ee;
  --um-neumorphism-ink: #272b35;
  --um-neumorphism-border-strong: #697386;
  --um-neumorphism-shadow-1: 8px 8px 16px #b8b9be, -8px -8px 16px #fff;
  --um-neumorphism-shadow-press: inset 5px 5px 10px #b8b9be, inset -5px -5px 10px #fff;
}
.um-neumorphic { background: var(--um-neumorphism-surface-1); box-shadow: var(--um-neumorphism-shadow-1); border: 1px solid transparent; }
.um-neumorphic:focus-visible { outline: 3px solid var(--um-neumorphism-border-strong); outline-offset: 3px; }
.um-neumorphic[aria-pressed="true"] { box-shadow: var(--um-neumorphism-shadow-press); }
```

## Component rules
- Knob/toggle: include text label, value, state, and keyboard increment/decrement.
- Input: use an explicit border and label; inset shadow is supplemental.
- Card: use larger radius and fewer shadow layers than controls.
- Navigation: prefer Flat or Material treatment around neumorphic controls.

## Motion and performance
Use short transform/shadow changes only on interaction. Avoid animating many shadows simultaneously. Disable heavy shadow transitions for low-power devices.

## Accessibility checklist
- [ ] Focus does not use box-shadow alone.
- [ ] Selected and disabled states include text, icon, border, or opacity change.
- [ ] Contrast is tested in light and dark themes.
- [ ] Forced-colors mode preserves visible boundaries.
- [ ] Touch targets are at least 44px where practical.

## Anti-patterns
- Full-page monochrome relief.
- Neumorphic data tables or complex forms.
- Glass or vivid gradient placed inside the same soft-shadow surface.
