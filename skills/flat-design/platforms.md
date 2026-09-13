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

## Shared component recipe
Button = semantic fill + explicit focus/pressed/disabled states; Card = surface + border + spacing; Input = label + border + focus + helper/error; Navigation = active icon/label/indicator; Table = stable row/header state cues.

## Responsive/accessibility
Validate compact phone, tablet, desktop and text scaling/localization. Flutter tappable targets should be >=48x48 logical px; web controls should use the product's minimum target policy. Ensure grayscale, high contrast, keyboard, screen reader, and forced-colors paths remain understandable.

## Performance
This style is the preferred fallback for all effect-heavy styles because it avoids expensive compositing and backdrop sampling.
