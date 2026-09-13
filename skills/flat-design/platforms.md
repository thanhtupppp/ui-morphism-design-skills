# Flat Design — Cross-Platform Recipes

## Canonical intent
Hierarchy is created by semantic color, typography, spacing, alignment, borders, and explicit component states. Depth is optional and must never carry meaning alone.

## HTML/CSS
- Use semantic HTML controls and CSS custom properties for role tokens.
- Button states: `:hover`, `:active`, `:focus-visible`, `[aria-disabled="true"]`; never rely on color alone for selected/error.
- Forms use `<label>`, helper/error text, `aria-describedby`, and visible error/success markers.
- Responsive layout uses Grid/Flex and content-driven breakpoints.

## React
- Keep component behavior separate from tokens.
- Prefer `className`/CSS Modules/Tailwind according to the host project; the skill does not mandate a styling library.
- Preserve native button/input/dialog semantics before introducing custom primitives.

## Flutter
- Map semantic colors, text styles, shapes, and spacing into `ThemeData` or `ThemeExtension`.
- Prefer `FilledButton`, `OutlinedButton`, `TextButton`, `TextField`, `NavigationBar`, `Dialog`, `SnackBar`, and standard list/table widgets for semantics and interaction.
- Use `InputDecoration` for persistent labels/helper/error text; use `Focus`/`FocusNode` for keyboard styling.
- Keep an optional `elevation: 0` baseline rather than inventing shadows for flat surfaces.

## React Native and other renderers
- Use the renderer's native semantic controls and layout primitives.
- Map the same role tokens, state cues, spacing, and responsive intent; do not require pixel-identical rendering.
- When a renderer lacks a web-style primitive, use its closest accessible native equivalent rather than a custom painted control.
- The fallback is a simpler opaque surface with explicit border/state cues; Flat Design should remain usable without any decorative effect capability.

## Shared component recipe
Button = semantic fill + explicit focus/pressed/disabled states; Card = surface + border + spacing; Input = label + border + focus + helper/error; Navigation = active icon/label/indicator; Table = stable row/header state cues.

## Responsive/accessibility
Validate compact phone, tablet, desktop and text scaling/localization. Flutter tappable targets should be >=48x48 logical px; web controls should use the product's minimum target policy. Ensure grayscale, high contrast, keyboard, screen reader, and forced-colors paths remain understandable. Use reduced-motion behavior for any transition or state animation: content and state changes must remain fully understandable without motion.

## Reduced motion
When `prefers-reduced-motion: reduce` applies on web, reduce or remove nonessential transitions. On Flutter, honor the platform accessibility/reduced-motion setting when available. Never hide state changes behind animation.

## Performance
This style is the preferred fallback for all effect-heavy styles because it avoids expensive compositing and backdrop sampling.
