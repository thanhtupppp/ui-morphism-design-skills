# Material Design — Cross-Platform Recipes

## Canonical intent
Model the system as semantic roles: color, typography, shape, elevation, state layers, component anatomy, adaptive layout, and purposeful motion.

## HTML/CSS
- Represent roles with CSS custom properties rather than component-specific literals.
- Use semantic HTML for buttons, fields, lists, dialogs, navigation, and tables.
- Elevation is a named token ladder; borders may provide the deterministic fallback.
- Dialogs require modal semantics, focus management, Escape handling, and focus restoration.

## React
- Compose semantic DOM with the project's component primitives.
- Keep theme/token data independent from component logic so dark/light/brand themes do not require rewriting markup.
- Implement state layers with pseudo-elements or explicit state wrappers; never obscure text.

## Flutter
- Use `ThemeData` for app-wide roles and `ThemeExtension` for product-specific semantic tokens.
- Prefer Material widgets for Button, TextField, Navigation, Dialog, Menu, Snackbar, List, and Table behavior.
- Use `Material`/`elevation`, `ShapeBorder`, `ColorScheme`, and state properties for the visual layer.
- Keep custom components compatible with `Focus`, keyboard traversal, semantics, large text, and platform adaptation.

## State model
Every core component gets default/hover/focus/pressed/selected/disabled plus loading/error/success where relevant. Map web hover to desktop Flutter pointer state; do not require hover for mobile comprehension.

## Responsive/accessibility
Use compact/medium/expanded layout rules rather than shrinking desktop coordinates. Preserve accessible names, error associations, focus order, and scalable typography. Flutter's built-in widgets provide accessibility semantics; test TalkBack/VoiceOver and keyboard traversal.

## Performance
Prefer framework elevation and composited primitives over custom shadows. Keep motion bounded to local state transitions and provide reduced-motion alternatives.
