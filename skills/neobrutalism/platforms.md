# Neobrutalism — Cross-Platform Implementation Guide

## Canonical intent
Neobrutalism is a graphic interaction language: flat fills, strong borders, bold type, and hard zero-blur offsets. Preserve those semantics across platforms without requiring pixel-identical rendering.

## Capability map

| Intent | HTML/CSS | React | Flutter | Other renderers |
|---|---|---|---|---|
| Strong boundary | `border` | semantic element + CSS | `BoxDecoration.border` | native border/stroke |
| Hard depth | zero-blur `box-shadow` | CSS visual layer | `BoxShadow(blurRadius: 0)` | platform shadow/stroke equivalent |
| Press feedback | `transform` + reduced offset | state in React, CSS presentation | `Transform.translate` around semantic control | platform pressed state |
| Focus | `:focus-visible` outline | semantic focus + CSS | `Focus`/`FocusNode` or theme focus | native focus ring |
| Flat fill | `background` | CSS token | `color`/`BoxDecoration` | native fill |

## HTML/CSS
Use semantic HTML first, then add the visual language:

```css
.neo-control {
  border: 2px solid var(--neo-border);
  background: var(--neo-accent);
  box-shadow: 4px 4px 0 var(--neo-border);
}
.neo-control:active {
  transform: translate(4px, 4px);
  box-shadow: none;
}
```

Keep the visual translation small enough that the control does not unexpectedly leave its layout or clipping context. The hit target is defined by the actual interactive element, not the apparent shadow edge.

Use `@media (prefers-reduced-motion: reduce)` to remove transition/motion while retaining the final state styling.

For forced/high-contrast modes, do not depend on subtle accent fills or shadow offsets to preserve meaning; the border and semantic states must remain visible.

## React
Recommended architecture:

```text
semantic component
→ props/state
→ host layout
→ Neobrutalist visual wrapper/classes
```

- Keep interaction logic in React and presentation in CSS/theme tokens.
- Use native `<button>`, `<a>`, `<input>`, `<select>`, `<dialog>` where appropriate.
- Whole-card links must not contain nested buttons/links.
- State attributes (`aria-pressed`, `aria-selected`, `aria-invalid`, `disabled`) should drive visual changes rather than click-handler-only class mutations.
- When a component needs multiple actions, make the card a non-link container with distinct semantic controls.

## Flutter
Flutter has no need to emulate CSS. Map intent to native primitives:

```dart
DecoratedBox(
  decoration: BoxDecoration(
    color: accent,
    border: Border.all(color: ink, width: 2),
    boxShadow: const [
      BoxShadow(color: ink, offset: Offset(4, 4), blurRadius: 0),
    ],
  ),
  child: const Text('Primary action'),
)
```

Recommended structure:

```text
Material / Semantics
  → visual decoration
  → native semantic control
```

Use `FilledButton`, `OutlinedButton`, `TextField`, `Checkbox`, `Radio`, `Switch`, `Slider`, `NavigationBar`, `Dialog`, and other native controls where they provide the expected semantics. Wrap/decorate them rather than rebuilding interaction primitives solely for visual fidelity.

For pressed motion, a small `Transform.translate` may be used around the visual wrapper. Keep semantics, hit testing, and focus independent of the decorative offset.

Respect Flutter text scaling and allow variable-height cards; do not fix a tile height merely to maintain the desktop collage.

## React Native / other renderers
Prefer the renderer's supported border, elevation/shadow, transform, focus/pressed, and responsive layout primitives. If zero-blur hard shadows are not supported exactly, approximate with a solid offset layer, outline, or platform-supported shadow without adding blur-heavy effects.

The invariant is:

```text
flat fill + strong boundary + hard offset + clear state
```

not a specific rendering API.

## Component mapping
### Button
Semantic button + flat accent + strong border + hard offset. Pressed state reduces/removes offset.

### Card
Strong outer boundary with optional offset. Do not duplicate the offset on every child.

### Form
Native field semantics + visible label/helper/error. Strong border is enough to establish the field; error adds icon/text in addition to color.

### Navigation
Active destination gets a strong block/underline/typographic cue. Avoid making every destination a heavy raised object.

### Dialog
Platform modal primitive + Neobrutalist shell. Preserve focus trapping, Escape/back dismissal where appropriate, and focus restoration.

## Responsive contract
```text
Expanded → expressive type + stronger offsets + multi-column layout
Medium   → reduced spans + moderate offsets
Compact  → one-column flow + reduced display type + no decorative rotation
```

Do not let a translated shadow create horizontal scrolling. Avoid absolute-positioned decorative elements overlapping important controls at compact widths.

## Accessibility contract
- Focus is an explicit state and must remain visible without hover.
- Color is supplemental to selected/error/status meaning.
- Heavy borders must not hide or resemble focus indicators.
- Text can wrap and components can grow.
- Keyboard traversal follows semantic order.
- Large text/text scaling and localization must not clip content.
- Forced/high-contrast modes must retain readable boundaries and state cues.

## Performance
The style is normally inexpensive: flat fills, borders, and zero-blur offsets avoid the cost of large blur regions. Main risks are many animated transforms, oversized shadows causing clipping, and large decorative media.

Prefer static styling and short pressed feedback over continuous motion. Avoid nesting many independently animated hard-shadow layers.

## Fallback ladder
```text
full Neobrutalism
→ hard offset + strong border + accent fill
→ strong border + accent fill
→ border + solid surface
→ host platform default component theme
```

The fallback changes appearance, never semantics or interaction behavior.

## Acceptance test
A cross-platform implementation passes when a reviewer can move from web to Flutter/native renderer and still identify the same component roles, hierarchy, interaction states, and visual vocabulary without requiring identical pixel geometry.
