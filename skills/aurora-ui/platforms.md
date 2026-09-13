# Aurora UI — Cross-Platform Implementation Guide

## Canonical contract
Aurora is an **atmospheric background/emphasis system**, not a required material for every component. Preserve this semantic contract across platforms:

`semantic content → stable component surface → optional Aurora atmosphere`

Pixel-identical rendering across HTML/CSS, React, Flutter, React Native, or other renderers is not required. The portable requirement is that hierarchy, meaning, states, accessibility, responsive behavior, and fallback behavior remain equivalent.

## Layer model

Implement the visual stack as independent layers:

1. **Ground** — stable background color.
2. **Aurora field** — 2–4 large gradient sources.
3. **Diffusion** — gradient falloff and optional bounded blur.
4. **Focal glow** — optional stronger region for hero/emphasis.
5. **Protection surface** — scrim, opaque card, or high-opacity surface where needed.
6. **Content** — semantic text and controls.

Do not make the content subtree responsible for the Aurora blur.

## HTML/CSS

Preferred primitives:
- `radial-gradient()` / `linear-gradient()` for light fields.
- Pseudo-elements or dedicated absolutely positioned layers for decoration.
- `isolation: isolate` to keep blend/layering predictable.
- `transform` and `opacity` for slow motion.
- CSS custom properties for Aurora tokens.
- `@media (prefers-reduced-motion: reduce)` for static effects.
- `@media (forced-colors: active)` to remove decorative gradients when necessary.

Typical structure:

```html
<main class="aurora-page">
  <div class="aurora-field" aria-hidden="true"></div>
  <section class="aurora-hero">
    <h1>Product title</h1>
    <p>Supporting message.</p>
    <button type="button">Get started</button>
  </section>
</main>
```

Keep the Aurora layer `pointer-events: none`, and ensure it cannot intercept keyboard or pointer interaction.

### CSS implementation rule

Do not apply `filter: blur()` to the entire `<main>` or to a wrapper containing text and controls. Blur only the decorative field.

## React

React should own semantics and behavior; CSS should own the Aurora presentation.

Recommended component boundaries:

```text
<AuroraPage>
  <AuroraField aria-hidden />
  <HeroSurface>
    <Button />
  </HeroSurface>
</AuroraPage>
```

Useful state props/modes:

```ts
type AuroraEffects = 'animated' | 'static' | 'minimal' | 'off';
```

The app can select a mode based on reduced-motion preferences, performance settings, or product policy. The semantic children should not change just because the effect mode changes.

Avoid putting animated Aurora logic in every `Card`, `Button`, or `Input`. Centralize the field and expose a small number of intentional emphasis variants.

## Flutter

Prefer Flutter's native layout/painting primitives:

- `DecoratedBox` or `Container` with `BoxDecoration` for static gradients.
- `Stack` for independent background/content layers.
- `ClipRect`/bounded clipping when an effect must stay inside a region.
- `CustomPaint` for specialized multi-source fields when ordinary decorations are insufficient.
- `AnimationController` plus `Transform`/opacity-style animation for slow ambient movement.
- Native Material/Cupertino semantic controls for buttons, fields, navigation, dialogs, and selection.

Recommended structure:

```text
Stack
├─ Positioned.fill: Aurora field
└─ SafeArea / content
   ├─ stable surface
   └─ semantic controls
```

Do not put a blur/filter around the entire `Stack` containing content. Keep expensive painting isolated to the decorative layer and provide a static/solid mode.

## React Native / other renderers

Use the strongest native gradient primitives available. When true blur or advanced GPU effects are unavailable, prefer a static gradient or opaque tint over inventing a fragile approximation that harms performance.

The fallback order remains:

`animated Aurora → static Aurora → simplified gradient → solid background`.

A less sophisticated but stable renderer is preferable to a visually impressive effect that causes dropped frames or blocks interaction.

## Component mapping

| Semantic component | Aurora implementation |
|---|---|
| Page shell | Background Aurora field |
| Hero | Focal Aurora + stable surface |
| Card | Stable card + optional subtle halo |
| Button | Native/semantic button; optional surrounding glow |
| Input | Stable opaque field |
| Navigation | Stable navigation shell + page-level Aurora behind |
| Dialog | Scrim + stable dialog surface; Aurora stays behind |
| Status | Semantic state tokens + label/icon; optional decoration |
| Table | Stable table/data surface |

## State mapping

Aurora decoration must be orthogonal to the interaction state model:

```text
focus-visible → explicit focus ring
selected      → explicit selected treatment
error         → semantic error treatment
success       → semantic success treatment
loading       → progress/skeleton
Aurora        → optional decoration
```

Do not bind business state directly to “brightness”, “glow”, or “blob position”.

## Accessibility and fallback

The effect system should have a disabled path with no semantic loss:

```text
Effects ON
  ↓
Static Effects
  ↓
Minimal Effects
  ↓
Effects OFF
```

Effects OFF should retain:
- page/background color
- readable text
- component boundaries
- focus treatment
- selected/disabled/error/success states
- keyboard/navigation behavior
- hit targets

For high-contrast or forced-color environments, hiding decorative gradients is valid; hiding controls or state information is not.

## Responsive behavior

Do not create a separate mobile component architecture solely for Aurora. Keep the content structure shared and change the effect budget:

- desktop: 2–4 fields, moderate blur
- mobile: 1–3 fields, smaller painted area
- constrained device: static or simplified field
- accessibility/reduced-motion: frozen/static field
- unsupported renderer: solid background

Preserve spacing, target size, text scaling, localization, and reading order regardless of effect mode.

## Performance checklist

Before shipping, verify:

- [ ] Only a small number of decorative layers are animated.
- [ ] Animation uses transform/opacity where practical.
- [ ] Blur is bounded to decorative regions.
- [ ] Off-screen or hidden-page ambient animation can pause.
- [ ] Mobile/constrained variants reduce the effect budget.
- [ ] Removing Aurora does not change layout measurements unexpectedly.
- [ ] No decorative layer captures pointer events.

## Platform portability test

Render the same component scenario in each target renderer:

```text
1. normal motion + full Aurora
2. reduced motion + static Aurora
3. effects disabled
4. narrow/mobile width
5. large text / zoom / localization
6. high-contrast / forced-color equivalent
```

Pass criteria are semantic equivalence, not pixel equality.
