# Material Design

## Purpose
Material Design is a component and interaction system based on roles, surfaces, elevation, state layers, adaptive layout, and purposeful motion.

## Use when
- The product needs a reusable cross-platform design system.
- The interface contains navigation, forms, dialogs, menus, tables, and frequent state changes.
- Teams need predictable component anatomy and scalable tokens.

## Visual DNA
- Define color roles, typography roles, shape scale, elevation levels, and state layers.
- Elevation communicates spatial relationship; it is not a substitute for semantics.
- Use a small, named elevation ladder rather than arbitrary shadows.
- Keep theme tokens separate from component structure.

## Component rules
- Button, field, dialog, menu, snackbar, navigation, and list components need complete state matrices.
- Use explicit labels and supporting/error text for fields.
- Dialogs must manage focus, close behavior, escape, and restoration of focus.
- Tables and dashboards should use stable surfaces and clear density modes.

## Token recipe
```css
:root {
  --um-material-design-bg: #fffbfe;
  --um-material-design-surface-1: #f7f2fa;
  --um-material-design-ink: #1d1b20;
  --um-material-design-ink-muted: #49454f;
  --um-material-design-primary: #6750a4;
  --um-material-design-border-strong: #79747e;
  --um-material-design-elev-1: 0 1px 3px rgb(0 0 0 / .20), 0 1px 2px rgb(0 0 0 / .14);
  --um-material-design-focus: #4f378b;
}
```

## Motion
Use motion to explain state, hierarchy, and spatial continuity. Prefer transform/opacity and short feedback. Provide reduced-motion alternatives and avoid unbounded movement.

## Responsive and implementation
Use adaptive layout rather than desktop shrinkage. Keep content density configurable. In React/Tailwind, map roles to semantic tokens; in Flutter, use `ThemeData` or `ThemeExtension`.

## Accessibility checklist
- [ ] Contrast, focus, labels, error association, and target size are configured rather than assumed.
- [ ] Keyboard order and screen-reader names are correct.
- [ ] State layers do not hide text or focus.
- [ ] Motion has a reduced path.

## Anti-patterns
- Copying framework defaults without product research.
- Using elevation for every element.
- Treating Material as a visual skin while ignoring component behavior.
