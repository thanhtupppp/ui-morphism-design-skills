# Claymorphism — Component Anatomy & Recipes

Claymorphism uses opaque, inflated, soft, highly rounded surfaces. Decorative volume is secondary to semantics.

## Core tokens

```css
:root {
  --um-claymorphism-bg: #f4f1fb;
  --um-claymorphism-surface-1: #cfd4ff;
  --um-claymorphism-surface-2: #ffffff;
  --um-claymorphism-ink: #24233a;
  --um-claymorphism-ink-muted: #58556f;
  --um-claymorphism-border: #554d86;
  --um-claymorphism-focus: #3b2f8f;
  --um-claymorphism-danger: #b42318;
  --um-claymorphism-radius-md: 20px;
  --um-claymorphism-radius-lg: 32px;
  --um-claymorphism-shadow-soft: 0 12px 24px -10px rgb(80 65 150 / .24);
  --um-claymorphism-shadow-deep: 0 24px 44px -12px rgb(80 65 150 / .32);
  --um-claymorphism-shadow-highlight: inset 0 10px 18px -6px rgb(255 255 255 / .62);
  --um-claymorphism-shadow-shade: inset 0 -10px 18px -6px rgb(52 42 91 / .32);
  --um-claymorphism-target-min: 44px;
}
```

## Buttons

```css
.clay-button {
  min-height:var(--um-claymorphism-target-min);
  padding:10px 18px;
  border:1px solid transparent;
  border-radius:var(--um-claymorphism-radius-md);
  background:var(--um-claymorphism-surface-2);
  color:var(--um-claymorphism-ink);
  box-shadow:var(--um-claymorphism-shadow-soft), var(--um-claymorphism-shadow-highlight), var(--um-claymorphism-shadow-shade);
}
.clay-button:focus-visible { outline:3px solid var(--um-claymorphism-focus); outline-offset:4px; }
```

Default, hover, pressed, selected, disabled, loading and focus meaning must not depend on shadow or pastel color alone.

## Components

Cards use flexible height and bounded depth. Inputs preserve `label → control → helper/error → state`. Navigation has a persistent active indicator. Dialogs retain title/content/actions, focus management and predictable dismissal. Dense tables/lists use flatter supporting surfaces.

## Responsive and accessibility

Reduce radius/shadow complexity on compact layouts before reducing target size. Large text and localization wrap rather than clip. Focus is an explicit high-contrast outline; status uses text/icon in addition to color; forced-colors retains solid boundaries.

## Fallback and performance

```text
full clay depth
→ reduced shadow/highlight
→ opaque rounded surface + border
→ flat opaque surface
```

Prefer 1–3 shadow layers per major object, avoid large repeated blur stacks and continuous shadow animation, and drop decorative depth before semantic feedback.

## Anti-patterns

- Inflating every component.
- Transparency that turns Clay into glass.
- Gray paired relief that turns Clay into Neumorphism.
- Huge shadow stacks on dense lists.
