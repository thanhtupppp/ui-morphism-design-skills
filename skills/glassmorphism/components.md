# Glassmorphism — Component Anatomy & Recipes

## 1. What makes glass look like glass

A beginner should recognize Glassmorphism from five visible ingredients:

1. **Translucent tint** — you can partially sense the controlled background through the surface.
2. **Frosting/blur** — background detail is softened behind the panel, not inside the text or icon.
3. **Rim/border** — a subtle light or contrasting edge describes the glass boundary.
4. **Depth shadow** — the glass plane separates from what sits behind it.
5. **Stable foreground content** — text, icons, controls, and states remain readable regardless of the backdrop.

Remove any two of the first four and it may simply look like a translucent card. The component is still valid, but the style signature becomes weaker.

## 2. Layer anatomy

Build glass from outside to inside:

`backdrop -> blur -> tint -> optional saturation -> rim -> shadow -> content`

Do not apply blur to the content itself. The blur belongs to the material layer that samples the backdrop.

### Levels
Use at most two glass levels in a screen:

- **Glass 1:** larger navigation, hero, toolbar, or modal chrome.
- **Glass 2:** small contextual control that must float above Glass 1 or the page.

Avoid three or more nested glass surfaces.

## 3. Core tokens

```css
:root {
  --glass-bg: #0b0b12;
  --glass-tint: rgb(255 255 255 / .14);
  --glass-tint-strong: rgb(255 255 255 / .22);
  --glass-fallback: #202331;
  --glass-ink: #ffffff;
  --glass-ink-muted: rgb(255 255 255 / .78);
  --glass-border: rgb(255 255 255 / .42);
  --glass-border-strong: rgb(255 255 255 / .62);
  --glass-blur-sm: 10px;
  --glass-blur-md: 20px;
  --glass-blur-lg: 32px;
  --glass-shadow: 0 8px 32px -8px rgb(0 0 0 / .38);
  --glass-radius-sm: 10px;
  --glass-radius-md: 16px;
  --glass-radius-lg: 20px;
  --glass-radius-pill: 999px;
  --glass-control-min: 44px;
}
```

Opacity belongs to the material. Do not make required text faint because the surface is translucent.

## 4. Button

A Glass button is usually a **small stable capsule or rounded control**, not a transparent text label floating over an image.

### Anatomy
`shape + tint/fill + rim + label/icon + state indicator + focus ring`

### States
- default: stable translucent/light fill
- hover: slight fill increase or brightness change
- pressed: subtle scale/translate or stronger tint
- selected: visible indicator/icon/fill change
- disabled: reduced affordance but readable label
- focus: solid high-contrast ring above the material
- loading: preserve button width and expose busy state

```css
.glass-button {
  min-height: var(--glass-control-min);
  padding: 10px 16px;
  border: 1px solid var(--glass-border);
  border-radius: var(--glass-radius-pill);
  background: rgb(255 255 255 / .88);
  color: #101426;
  font: inherit;
  font-weight: 650;
}
.glass-button:hover { background: rgb(255 255 255 / .96); }
.glass-button:active { transform: translateY(1px); }
.glass-button:focus-visible { outline: 3px solid #f8d34f; outline-offset: 3px; }
.glass-button:disabled { opacity: .62; }
```

The primary action often uses a more opaque fill than the surrounding panel. This prevents the CTA from becoming camouflage.

## 5. Icon button

Use for compact actions such as close, settings, mute, favorite, or overflow.

Rules:

- minimum target size from platform policy;
- visible shape even over changing backdrops;
- accessible name independent of tooltip;
- selected state cannot be conveyed only by glow.

Prefer a slightly stronger tint/border than the surrounding glass.

## 6. Card / panel

Glass cards work best for **short, bounded content**.

### Good content
- hero summary
- media metadata
- navigation group
- transient tool palette
- small status cluster

### Poor content
- long articles
- dense tables
- large editable forms
- log streams
- unpredictable user imagery

```css
.glass-card {
  padding: 20px;
  border: 1px solid var(--glass-border);
  border-radius: var(--glass-radius-lg);
  background: var(--glass-tint);
  box-shadow: var(--glass-shadow);
  backdrop-filter: blur(var(--glass-blur-md)) saturate(160%);
}
```

Keep the text region visually calm. A decorative image may exist behind the panel; content should remain readable when that image changes.

## 7. Input / form

The most common Glassmorphism error is placing ordinary text fields directly over an unpredictable background.

Use one of two safe modes:

- **Opaque field:** normal solid field inside a glass shell.
- **Controlled glass field:** stronger tint + border + carefully tested backdrop.

An input consists of:

`label -> field -> helper/error -> state`

Required states: empty, filled, focus, disabled, read-only, invalid, valid, loading.

```css
.glass-input {
  min-height: var(--glass-control-min);
  width: 100%;
  padding: 10px 12px;
  border: 1px solid var(--glass-border-strong);
  border-radius: var(--glass-radius-sm);
  background: rgb(0 0 0 / .22);
  color: var(--glass-ink);
}
.glass-input:focus {
  border-color: #ffffff;
  outline: 3px solid rgb(248 211 79 / .52);
  outline-offset: 2px;
}
.glass-input[aria-invalid="true"] {
  border-color: #ff8a8a;
}
```

Never use low-opacity placeholder text as a substitute for the label.

## 8. Navigation / toolbar

This is one of the strongest use cases for Glassmorphism.

The navigation surface floats above page content and should visually read as a single plane.

Rules:

- keep one glass layer;
- use a stronger active indicator;
- active state uses icon/label/indicator, not color alone;
- maintain stable padding when the backdrop changes;
- do not make every nav item individually glassy.

Recommended anatomy:

`glass shell -> group -> item -> active indicator -> optional overflow`

## 9. Modal / command palette / sheet

Glass can be used for transient surfaces when the page behind it is controlled.

Required layers:

`page -> dim/scrim -> glass dialog -> content`

The scrim stabilizes contrast; the glass should not be the only contrast mechanism.

Dialog requirements:

- accessible title/name;
- predictable close behavior;
- focus entry and restoration;
- keyboard Escape where platform-appropriate;
- content must remain readable if blur is removed.

## 10. Alert / banner / status

Use a neutral glass shell with semantic status treatment inside it.

Status must include:

`icon + title/message + optional action`

Use semantic colors and text. Never use a red/green/blue glow as the only status channel.

## 11. Badge / chip

Glass chips are useful for tags, filters, metadata, and compact categories.

Selected chips need:

- stronger fill or border;
- check/icon/weight change where appropriate;
- readable label.

Do not create dozens of different translucent chip levels on one page.

## 12. Tabs

Use one shared glass/tab container rather than individual floating glass cards for every tab.

Selected tab:

`indicator/fill + label/icon emphasis`

Inactive tab:

`neutral text + stable hit area`

Keyboard focus remains visible above the tab container.

## 13. Menu / dropdown

The menu surface can be glass when it floats over a known backdrop.

Menu items should remain opaque enough to read during scroll or movement. Keep item hover/pressed state inside the same surface rather than creating nested glass layers.

## 14. Table / data-heavy surfaces

Do not use translucent rows over imagery.

Use:

`opaque table shell + optional glass toolbar/header`

This preserves scanability and prevents row boundaries from disappearing against changing backgrounds.

## 15. Skeleton / loading

A glass skeleton should use a stable neutral placeholder. Avoid animated shimmer through the entire translucent page.

Loading indicators must remain visible even when the backdrop changes.

## 16. Focus and state hierarchy

State priority is:

`semantic state -> explicit indicator -> material effect -> decorative glow`

Focus is never represented by blur, glow, or rim alone.

## 17. Responsive behavior

At narrow widths:

- reduce blur radius before reducing text size;
- reduce decorative transparency before shrinking controls;
- convert wide glass nav bars to a compact pattern;
- avoid horizontal overflow caused by large pills;
- allow content to wrap.

For reduced-effects or low-power mode:

`glass -> tinted opaque surface -> flat surface`

while preserving all interaction and state cues.

## 18. Accessibility and forced fallback

The screen must still work when:

- transparency is reduced;
- blur is unavailable;
- forced colors are active;
- contrast mode is stronger;
- motion is reduced;
- the backdrop is bright, dark, colorful, or animated.

Content remains understandable after deleting `backdrop-filter` from the stylesheet.

## 19. Performance rules

- Blur the smallest possible surface.
- Avoid nested backdrop sampling.
- Avoid dozens of simultaneous blurred cards.
- Prefer one backdrop layer shared by nearby controls.
- Do not animate blur radius continuously.
- For low-power/mobile modes, remove blur before removing borders, labels, or state indicators.

## 20. Beginner recognition checklist

A screen is recognizably Glassmorphism when the beginner can point to:

- a translucent/frosted plane;
- a visible controlled backdrop behind it;
- softened background detail through the plane;
- a rim/border catching light;
- separation from the background by restrained shadow;
- stable foreground content that does not become transparent decoration.

If the result is simply a white card with a subtle shadow, it is not meaningfully Glassmorphism.
