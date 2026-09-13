# Claymorphism — Component Anatomy & Recipes

## Visual language

Claymorphism uses **opaque, inflated, soft, highly rounded surfaces**. Volume comes from restrained highlights and hue-related shadows. Content, interaction states, and focus must remain understandable without decorative depth.

Clay is not Neumorphism: do not rely on gray paired relief. Clay is not Glassmorphism: do not make the body translucent.

## Surface anatomy

1. Opaque body color.
2. Rounded/squircle geometry.
3. Soft highlight.
4. Soft lower shade.
5. Bounded outer shadow.
6. Crisp content layer.
7. Explicit state layer.

Decorative volume is secondary to semantics.

## Core tokens

```css
:root {
  --clay-bg: #f4f1fb;
  --clay-surface: #cfd4ff;
  --clay-surface-alt: #ffffff;
  --clay-ink: #24233a;
  --clay-muted: #58556f;
  --clay-border: #554d86;
  --clay-focus: #3b2f8f;
  --clay-danger: #b42318;
  --clay-radius-md: 20px;
  --clay-radius-lg: 32px;
  --clay-shadow-soft: 0 12px 24px -10px rgb(80 65 150 / .24);
  --clay-shadow-deep: 0 24px 44px -12px rgb(80 65 150 / .32);
  --clay-highlight: inset 0 10px 18px -6px rgb(255 255 255 / .62);
  --clay-shade: inset 0 -10px 18px -6px rgb(52 42 91 / .32);
  --clay-target-min: 44px;
}
```

## Buttons

```css
.clay-button {
  min-height: var(--clay-target-min);
  padding: 10px 18px;
  border: 1px solid transparent;
  border-radius: var(--clay-radius-md);
  background: var(--clay-surface-alt);
  color: var(--clay-ink);
  box-shadow: var(--clay-shadow-soft), var(--clay-highlight), var(--clay-shade);
  font: inherit;
  font-weight: 650;
}
.clay-button:hover { transform: translateY(-1px); }
.clay-button:active { transform: translateY(1px) scale(.985); }
.clay-button:focus-visible { outline: 3px solid var(--clay-focus); outline-offset: 4px; }
.clay-button:disabled { opacity: .55; cursor: not-allowed; }
```

Required states: default, hover, pressed, selected where applicable, disabled, loading/busy where asynchronous, and focus. State meaning must not depend on shadow or pastel color alone.

## Icon buttons

Use a real button with an accessible name. Keep a visible hit area of at least the product minimum and prefer 44 CSS px on web.

## Cards, forms, navigation, dialogs

Cards use flexible height, large but bounded radius, and limited shadow layers. Inputs use conventional form semantics: `label → control → helper/error → state marker`. Navigation keeps recognizable destination labels and one explicit active indicator. Dialogs retain conventional title, content, primary/secondary actions, focus management, and dismissal behavior.

Dense tables, logs, and large lists should not make every row look inflated; reserve Clay for hierarchy such as hero modules, summary cards, or featured actions.

## Responsive behavior

Clay shapes can become visually heavy on small screens. Layout must adapt to the available width and must never clip localized or large text.

### Responsive matrix

| Width class | Layout | Spacing / geometry | Effect budget | Control policy |
|---|---|---|---|---|
| Compact: <600px | Single column; cards may become full width | Reduce outer padding and radius moderately | Reduce shadow spread/blur | Preserve target size and wrapping |
| Medium: 600–1023px | One or two columns, content-driven | Moderate spacing and radius | Normal depth on key objects | Inline controls only when space permits |
| Expanded: >=1024px | Featured/hero composition with bounded max width | Larger hierarchy spacing | Full depth only on primary objects | Preserve readable line length |

Implementation rule: prefer `LayoutBuilder`/available-width constraints in Flutter and responsive grid/flex rules in CSS/React. Avoid fixed heights for text-bearing clay surfaces.

## Accessibility and fallback

- Focus must be a high-contrast outline, never only a shadow.
- Borders/indicators must survive removal of decorative shadows.
- Status communicates through text and/or icon as well as color.
- Forced-colors/high-contrast mode needs solid boundaries.
- Large text and localization must wrap instead of clipping.
- Decorative clay effects may be removed without losing content or state meaning.

## Motion

Use restrained lift/press motion. Under reduced motion, remove transform animation or use immediate state changes.

## Performance

Prefer 1–3 shadow layers per major object. Avoid large blur radii over long lists and continuous shadow animation. Drop decorative depth before dropping semantic feedback.

## Anti-patterns

- Styling every component as inflated clay.
- Tiny text inside oversized decorative objects.
- Transparency that turns Clay into glass.
- Gray relief that turns Clay into Neumorphism.
- Huge repeated shadow stacks on dense lists.
