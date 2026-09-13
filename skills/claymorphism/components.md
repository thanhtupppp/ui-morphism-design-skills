# Claymorphism — Component Anatomy & Recipes

## 1. What Claymorphism is

Claymorphism makes UI objects look **inflated, soft, opaque, rounded, and slightly toy-like**. The body has its own color; volume comes from internal highlights and soft external shadows.

A beginner recognition test:

- The object is **opaque**, not see-through.
- The shape is highly rounded or squircle-like.
- The surface feels inflated rather than metallic or glassy.
- A light highlight appears toward the light source.
- A darker, usually hue-related shadow appears on the opposite/lower side.
- The object can still be understood when all decorative shadows are removed.
- Typography remains crisp and simpler than the object itself.

### Clay vs similar styles

| Style | Surface | Depth source | Typical feeling |
|---|---|---|---|
| Claymorphism | Opaque colored body | Soft inflated highlights + hue-matched shadow | Friendly, playful |
| Neumorphism | Same/shared base surface | Paired light/dark relief | Calm, tactile, minimal |
| Glassmorphism | Translucent | Backdrop blur + tint | Floating, translucent |
| Skeuomorphism | Material/texture | Bevel + realistic light | Physical, realistic |

Do not turn Claymorphism into Neumorphism by using only gray paired shadows. Do not turn it into Glassmorphism by making the body translucent.

## 2. Surface anatomy

Build a clay surface in this order:

1. Opaque body color.
2. Large radius/squircle geometry.
3. Soft top/inner highlight.
4. Soft lower/inner shade.
5. Bounded outer shadow.
6. Crisp content layer.
7. Explicit functional state layer.

Decorative volume is secondary to content and state.

## 3. Tokens

```css
:root {
  --clay-bg: #f4f1fb;
  --clay-surface: #cfd4ff;
  --clay-surface-alt: #ffffff;
  --clay-ink: #24233a;
  --clay-muted: #58556f;
  --clay-border: #554d86;
  --clay-focus: #3b2f8f;
  --clay-success: #067647;
  --clay-warning: #8a5700;
  --clay-danger: #b42318;
  --clay-radius-sm: 14px;
  --clay-radius-md: 20px;
  --clay-radius-lg: 32px;
  --clay-radius-xl: 40px;
  --clay-shadow-soft: 0 12px 24px -10px rgb(80 65 150 / .24);
  --clay-shadow-deep: 0 24px 44px -12px rgb(80 65 150 / .32);
  --clay-highlight: inset 0 10px 18px -6px rgb(255 255 255 / .62);
  --clay-shade: inset 0 -10px 18px -6px rgb(52 42 91 / .32);
  --clay-target-min: 44px;
}
```

Prefer product semantic tokens over hard-coded colors. Theme variants should replace the surface roles rather than rewrite component anatomy.

## 4. Typography

Clay objects may be playful; typography should usually be calmer.

Recommended hierarchy:

- Display: short hero statement.
- Heading: section/object title.
- Body: normal reading content.
- Label: control identification.
- Meta: secondary information.
- Caption: non-critical detail.

Do not use oversized playful type inside every control. Avoid fixed-height text containers because rounded forms often tempt designers to clip content.

## 5. Buttons

### Primary clay button

Use a smaller, denser inflated object than the surrounding hero/card. It needs a strong label and clear contrast.

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
  cursor: pointer;
}
.clay-button:hover { transform: translateY(-1px); }
.clay-button:active { transform: translateY(1px) scale(.985); }
.clay-button:focus-visible { outline: 3px solid var(--clay-focus); outline-offset: 4px; }
.clay-button:disabled { opacity: .55; cursor: not-allowed; }
```

States:

- Default: inflated body.
- Hover: very small lift or brightness change.
- Pressed: tiny inward/lower translation.
- Focus: explicit high-contrast outline.
- Disabled: semantic disabled cue plus reduced decoration.
- Loading: preserve label width when practical and expose busy state.

Do not make the entire button disappear into the card by using the same color, radius, and shadow.

## 6. Icon button

An icon-only button must have an accessible name and a visible hit area.

```css
.clay-icon-button {
  width: 44px;
  height: 44px;
  border-radius: 16px;
  border: 1px solid transparent;
  background: var(--clay-surface-alt);
  color: var(--clay-ink);
  box-shadow: var(--clay-shadow-soft), var(--clay-highlight), var(--clay-shade);
}
```

Use tooltip text only as discovery support; the accessible name must exist independently.

## 7. Cards and feature panels

Clay cards are usually the strongest expression of the style.

Recommended anatomy:

`illustration/icon → title → supporting content → action`

Rules:

- Large clay radius for hero/feature cards.
- Distinguish card scale from button scale.
- Keep content flexible in height.
- Do not inflate every list item.
- Use one visual material per card family.

```css
.clay-card {
  min-width: 0;
  padding: 28px;
  border-radius: var(--clay-radius-lg);
  background: var(--clay-surface);
  box-shadow: var(--clay-shadow-deep), var(--clay-highlight), var(--clay-shade);
}
```

## 8. Inputs and forms

Claymorphism should normally use conventional form controls inside a clay shell rather than making the control itself excessively decorative.

An input consists of:

`label → control → helper/error → state marker`

Required states:

- empty
- filled
- focus
- disabled
- read-only
- invalid
- valid/success when meaningful
- loading when asynchronous

```css
.clay-input {
  min-height: var(--clay-target-min);
  width: 100%;
  padding: 10px 12px;
  border: 2px solid var(--clay-border);
  border-radius: var(--clay-radius-sm);
  background: var(--clay-surface-alt);
  color: var(--clay-ink);
}
.clay-input:focus {
  border-color: var(--clay-focus);
  outline: 3px solid rgb(59 47 143 / .22);
}
.clay-input[aria-invalid="true"] { border-color: var(--clay-danger); }
```

Do not communicate an error only with a shadow or pastel color.

## 9. Selection controls

### Checkbox
Use a clear checked indicator. The clay body can surround it, but selection must remain recognizable when shadows are removed.

### Radio
Use a conventional selected dot/ring within a clay container.

### Switch
Clay may style the track/thumb shell, but the on/off state must be explicit.

### Segmented control
Clay may provide the overall container while the selected segment uses a stronger fill, inset treatment, indicator, or icon.

## 10. Sliders and progress

A slider may use a clay track with an opaque thumb.

- Track: broad rounded clay channel.
- Thumb: smaller raised object.
- Filled portion: semantic accent.
- Focus: clear outline around the thumb/control.
- Value: expose numerically when precision matters.

Progress indicators should not rely on shadow or color alone; expose a value where appropriate.

## 11. Badges, chips, tags

These are ideal for clay only when they remain visually subordinate.

```css
.clay-badge {
  display: inline-flex;
  min-height: 32px;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 999px;
  background: var(--clay-surface-alt);
  color: var(--clay-ink);
  box-shadow: var(--clay-shadow-soft);
}
```

For status, pair color with text/icon.

## 12. Navigation and tabs

Clay navigation should remain structurally conventional.

Good pattern:

- neutral shell
- clear destination labels
- one active indicator
- moderate clay treatment on the navigation container

Avoid making every navigation item a floating pill unless the product is genuinely playful and sparse.

Active state must not depend on color only.

## 13. Menus and popovers

Use clay for a bounded floating menu, not for the whole page.

An open menu needs:

`trigger relationship → surface → items → focus → dismissal`

Keyboard and pointer behavior must remain conventional.

## 14. Dialogs and sheets

Clay dialog:

- opaque body
- large radius
- strong separation from page
- clear title
- readable body
- explicit primary/secondary action
- focus management

The overlay/scrim should be conventional and stable. Do not use a soft clay effect as a substitute for modal separation.

## 15. Empty states and illustrations

Claymorphism is especially strong for empty states.

Use:

`clay illustration → short explanation → primary action`

The illustration can be expressive; the text and CTA should stay conventional and high contrast.

## 16. Tables and dense data

Do **not** make every row a clay object.

Use Flat or Material surfaces for:

- tables
- logs
- dense filters
- enterprise forms
- large lists

Clay may remain in the page header, summary card, or hero module.

## 17. Alerts and status

Clay alert containers can be rounded and soft, but meaning must remain semantic.

Every alert should provide an icon and/or text label in addition to color.

Error, warning, success, and info should remain distinguishable in grayscale.

## 18. Responsive behavior

Clay shapes often become visually heavy on small screens.

At narrow widths:

- reduce radius slightly before reducing usable control size;
- reduce outer shadow spread;
- reduce decorative illustration size;
- allow cards to become full-width;
- avoid fixed heights;
- preserve readable line length and wrapping;
- keep hit areas at least the product's minimum target policy.

At larger widths, use clay primarily for hierarchy: hero, featured card, primary CTA, or empty-state illustration.

## 19. Dark theme

Do not simply invert light Clay colors.

Dark Clay needs:

- darker opaque body;
- sufficient body/text contrast;
- restrained highlight intensity;
- shadow colors that remain visible on the dark ground;
- clear borders or indicators when shadows disappear.

## 20. Motion

Clay motion should feel soft and physical, not bouncy by default.

Good:

- small translate/scale on press;
- short lift on hover;
- restrained opacity/transform on entry.

Avoid:

- perpetual bouncing;
- large spring overshoot;
- rotating controls merely for decoration.

Under reduced motion, switch to instant state changes or a simple opacity change.

## 21. Accessibility and fallback

- Decorative shadows and highlights are optional.
- Functional borders/indicators must survive without shadows.
- Focus is never only an outer or inner shadow.
- Text and status remain understandable in grayscale.
- Forced-colors/high-contrast mode should provide solid boundaries.
- Large text and localization must not be clipped by rounded cards.

## 22. Performance

- Prefer 1–3 shadow layers per major object.
- Avoid large blur radii across long lists.
- Avoid animating shadow stacks continuously.
- Lazy-load large decorative illustrations.
- Drop decorative depth before dropping semantic state feedback.

## 23. Anti-patterns

- Clay styling on every component.
- Tiny text inside oversized inflated objects.
- Pastel text used as the only contrast strategy.
- Glass/transparency introduced into the clay body.
- Gray paired shadows that make Clay look like Neumorphism.
- Huge shadow stacks repeated across hundreds of list items.
