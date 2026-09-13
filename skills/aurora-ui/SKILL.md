# Aurora UI

## Purpose
Aurora UI is an atmospheric lighting system built from layered multi-color gradients, diffuse glow, and controlled depth of color. Its primary job is to establish mood, focal hierarchy, and visual identity behind content; it is **not** a complete material language by itself.

A correct Aurora implementation should still make sense after the decorative light field is removed. Semantics, layout, controls, states, readability, and interaction must survive without the effect.

## How to recognize Aurora UI
Aurora usually looks like a dark or neutral canvas with a small number of large, soft, luminous color fields that blend into one another. The light feels spatial and atmospheric rather than like a painted border or a physical object.

The visual hierarchy is:

1. Base background/ground.
2. Large aurora light field.
3. One focal glow or emphasis region.
4. Stable content surface/scrim.
5. Semantic controls and text.
6. Optional restrained edge glow for emphasis.

Aurora is about **light behind the interface**, not translucency of the interface itself.

## Use when
- The product needs premium, experimental, AI, creative, cinematic, or futuristic atmosphere.
- The page has a clear hero, focal action, short narrative, or small set of high-value modules.
- A stable surface can protect text and controls from the changing background.
- Brand identity benefits from a distinctive color atmosphere without turning every component into a decorated object.

## Avoid when
- Users must continuously read dense tables, logs, long legal text, documentation, or highly repetitive operational forms.
- A gradient would become the only signal for error, success, selection, disabled, or focus.
- The design depends on constant animation that cannot be disabled for reduced-motion or constrained devices.
- Every card or control receives a different animated glow, creating visual noise and destroying hierarchy.
- The background is so bright or variable that text contrast becomes dependent on a particular animation frame.

## Core design principle: atmosphere, not material
Aurora should normally occupy a **background layer**. Glassmorphism defines a translucent surface; Liquid Glass defines a functional dynamic surface; Claymorphism defines an inflated opaque object; Skeuomorphism defines physical material cues. Aurora defines the light environment behind those things.

When choosing between them:

- **Aurora vs Glassmorphism:** Aurora can sit behind a glass surface, but Aurora itself does not require translucency or backdrop blur.
- **Aurora vs Liquid Glass:** Aurora is the environment; Liquid Glass is the interactive material placed within that environment.
- **Aurora vs Neumorphism:** Aurora uses colored atmospheric light, not paired neutral relief shadows.
- **Aurora vs Claymorphism:** Aurora does not inflate controls or cards; its color field lives behind them.
- **Aurora vs Flat Design:** Flat removes simulated atmosphere; Aurora intentionally adds a decorative lighting layer, while preserving Flat-like semantic controls when needed.

## Visual DNA
- Use 2–4 major color fields. More fields are possible, but each added field must have a hierarchy reason.
- Establish one dominant hue and one supporting accent before adding a third color.
- Prefer large radial or elongated fields over many small circles.
- Place the strongest light near the page or hero focal point rather than equally around every component.
- Use diffusion/blur only on the decorative layer; do not blur text, icons, form controls, or semantic boundaries.
- Keep foreground surfaces stable: opaque, high-opacity, or deliberately scrimmed.
- Keep text opaque and high contrast.
- Use gradients to shape mood and emphasis, not to communicate application state.
- Prefer color relationships that still look coherent when animation is frozen.

## Aurora field anatomy
A reusable Aurora field has five conceptual parts:

### 1. Ground
The stable background color beneath every effect. It supplies the fallback and determines the overall contrast envelope.

### 2. Light sources
Usually 2–4 large soft sources. Each source has a hue, position, scale, intensity, and optional motion path.

### 3. Diffusion
The mechanism that softens each source: gradient falloff, blur, or both. Diffusion should never make the content itself soft.

### 4. Focal region
One region receives the strongest visual energy. This anchors the eye and prevents the page from becoming an undifferentiated neon wallpaper.

### 5. Protection layer
A scrim, surface, or neutral card may sit between Aurora and content when contrast or stability requires it.

## Token model
Keep Aurora tokens namespaced and separate from semantic application tokens.

```css
:root {
  --um-aurora-ui-bg: #0d1021;
  --um-aurora-ui-surface-1: rgb(255 255 255 / 0.94);
  --um-aurora-ui-surface-2: rgb(255 255 255 / 0.98);
  --um-aurora-ui-aurora-a: #6d5dfc;
  --um-aurora-ui-aurora-b: #19c6b5;
  --um-aurora-ui-aurora-c: #ff6b9a;
  --um-aurora-ui-aurora-focus: #8b7cff;
  --um-aurora-ui-ink: #101426;
  --um-aurora-ui-ink-muted: #526078;
  --um-aurora-ui-on-dark: #ffffff;
  --um-aurora-ui-focus: #f8d34f;
  --um-aurora-ui-border: rgb(255 255 255 / 0.26);
  --um-aurora-ui-glow-opacity: 0.82;
  --um-aurora-ui-blur-1: 64px;
  --um-aurora-ui-blur-2: 96px;
  --um-aurora-ui-radius-md: 16px;
  --um-aurora-ui-radius-lg: 24px;
  --um-aurora-ui-motion-slow: 18s;
}
```

The exact colors are starter values, not a requirement. Preserve the semantic roles even when the palette changes.

## Component strategy
Aurora is strongest on containers and emphasis surfaces, while the actual controls should remain conventional and legible.

| Component | Aurora role | Required stable layer |
|---|---|---|
| Page/background | Primary atmospheric field | Ground color |
| Hero | Focal light + optional protected content surface | Scrim/surface for text when needed |
| Card | Optional local glow or aurora window | Opaque/high-opacity card |
| Button | Minimal glow only as decorative emphasis | Solid semantic fill/border |
| Input | Normally none or extremely restrained edge tint | Opaque field + explicit state |
| Navigation | Background field or single active-region accent | Stable navigation container |
| Modal/dialog | Aurora may remain behind scrim | Solid/controlled dialog surface |
| Status/badge | Aurora may decorate the group | Color + text/icon/state semantics |
| Table/data grid | Prefer no local animation | Stable surface |

## State rules
Aurora must never become the state model.

- **Default:** calm background and stable surface.
- **Hover:** optional slight glow increase or tiny opacity change.
- **Pressed:** control changes by fill, border, transform, or native pressed state; never by glow alone.
- **Focus-visible:** solid high-contrast ring or platform focus treatment above the decoration.
- **Selected:** persistent semantic fill/border/icon indicator.
- **Disabled:** lower-emphasis control with sufficient text contrast; decorative glow should reduce or disappear.
- **Loading:** explicit progress/spinner/skeleton; never a pulsing aura alone.
- **Error:** semantic error color + text/icon/validation message.
- **Success:** semantic success color + text/icon/status feedback.

## Hero rules
The hero is the natural home for Aurora because the effect can support one clear focal region.

Use this stack:

`Ground → Aurora field → optional scrim/hero surface → heading/supporting copy → primary CTA → secondary content`

Do not place long text directly on a moving gradient unless contrast is validated at the worst visible point. A local opaque or high-opacity surface is often the more robust choice.

## Card rules
Cards should remain structurally obvious even without Aurora.

Good uses include a faint aurora edge, a controlled glow behind the card, or a single focal card receiving slightly more illumination than siblings.

Avoid assigning each card a different animated gradient. The eye should still know which card is primary from size, placement, typography, and semantics rather than color noise.

## Navigation rules
A page-level Aurora can sit behind navigation, but navigation must retain a stable hit area and readable active state. On small screens, reduce or remove the decorative field before shrinking navigation targets.

## Form and data rules
Use conventional controls inside stable surfaces. Labels, helper text, validation, sorting, selection, table headers, and row affordances must remain clear without Aurora.

The denser the information, the more the implementation should migrate toward Flat or Material component treatment while retaining a restrained Aurora background if appropriate.

## Motion
Aurora motion should feel like ambient light, not a status animation.

Preferred motion:
- Slow translation of large light fields.
- Very slow opacity drift.
- Small positional interpolation between predefined compositions.

Avoid:
- Rapid hue cycling.
- High-frequency scaling/pulsing.
- Per-component glow loops.
- Continuous animation on every card.
- Motion that changes text contrast dramatically frame to frame.

Use a static composition as the canonical reduced-motion state. For web, respect `prefers-reduced-motion`; for native renderers expose an equivalent reduced-motion/static-effects mode where available.

## Responsive behavior
Aurora should degrade in this order:

1. Fewer light sources.
2. Smaller glow area.
3. Lower opacity.
4. Lower blur radius or remove blur.
5. Freeze motion.
6. Keep only a static gradient.
7. Remove the gradient entirely and retain the ground surface.

Do **not** trade away usable hit targets, text size, spacing, or content order to preserve the effect.

## Performance rules
- Keep the number of animated layers small.
- Prefer a few large layers to many small per-component effects.
- Animate `transform` and `opacity` rather than expensive layout properties.
- Avoid `filter: blur()` on a large subtree that contains content or controls.
- Bound the painted area when possible.
- Pause non-essential animation when the page is hidden or the effect is outside the visible viewport.
- Treat mobile/low-power modes as first-class variants rather than late optimizations.

## Accessibility rules
- Test text and essential controls against the worst visible Aurora position, not the average frame.
- Keep focus visible with a solid high-contrast treatment.
- Communicate status with text/icon/structure independent of glow or hue.
- Preserve native semantics and keyboard/focus behavior.
- Support reduced-motion and static-effect modes.
- In forced-colors/high-contrast modes, decorative gradients may be removed while content remains fully usable.
- Check long labels, localization, text scaling, and zoom without relying on a fixed background composition.

## Recognition test
A beginner or AI coding agent should be able to answer “yes” to all of these:

1. Is Aurora behind the interface rather than being the interface material itself?
2. Can the page still be understood when the Aurora layer is disabled?
3. Is there one clear focal light region?
4. Are text and controls on stable enough surfaces?
5. Are states visible through semantic controls, not glow alone?
6. Is motion slow, bounded, and removable?

If the answers are mostly yes, the implementation is probably Aurora UI rather than generic neon styling.

## Anti-patterns
- Neon wallpaper behind long-form reading content.
- A different animated gradient on every component.
- Glow used as a replacement for focus, border, selected state, or validation.
- Low-opacity white text directly over a moving field.
- Large animated blur layers covering the full interactive subtree.
- Treating Aurora as a complete component system instead of layering it behind a stable one.
