# Glassmorphism

## Purpose
Glassmorphism creates a translucent, frosted plane between the user and a controlled backdrop. The material effect communicates **layering**, not physical hardware.

## Visual identity
A recognizably glass surface combines:

1. A visible backdrop.
2. Translucent tint.
3. Bounded backdrop blur/frosting.
4. A subtle rim/border.
5. Restrained cast shadow.
6. Stable, readable foreground content.

The blur belongs to the material layer. Never blur text, icons, or controls to create the effect.

## When to use
- Floating navigation and toolbars.
- Hero summaries and short media cards.
- Modal sheets and command palettes.
- Contextual controls over a controlled background.
- Premium/atmospheric surfaces where the backdrop is part of the composition.

## Avoid
- Long-form reading.
- Dense tables, logs, or large editable forms.
- User-uploaded imagery that cannot be contrast-tested.
- Full-page blur.
- Nested glass-on-glass-on-glass surfaces.

## Material model
The default stack is:

`backdrop -> blur -> tint -> optional saturation -> rim -> shadow -> content`

Use one primary glass level and, at most, one smaller supporting level.

### Backdrop dependency
The backdrop is part of the component's visual input. Test the surface over:

- light areas;
- dark areas;
- saturated colors;
- gradients;
- imagery;
- motion/changing content.

A component that only works over one screenshot is not a valid glass component.

## Token system
Define semantic tokens for:

- backdrop;
- tint/fill;
- strong tint;
- fallback surface;
- foreground/muted text;
- rim/border;
- strong border/focus;
- blur-sm/md/lg;
- shadow;
- radius;
- control target size;
- reduced-effects mode.

Opacity describes material composition, not information hierarchy.

## Component rules

### Buttons
Use stronger fill than the panel. Glass buttons must remain obvious actions.

States: default, hover, pressed, focus, selected, disabled, loading.

### Icon buttons
Use a visible hit-area shell. Accessible name comes from semantics, not tooltip.

### Cards
Use for short, bounded content. Keep body text stable and readable. Do not glass every card on a dashboard.

### Inputs
Prefer opaque fields inside glass panels. Controlled glass fields require explicit border, strong tint, label, helper/error text, and worst-case backdrop testing.

### Navigation / toolbar
One shared glass shell, not a separate glass material for every item. Active location needs label/icon/indicator cues.

### Modal / sheet / command palette
Use a scrim first, then glass. The scrim stabilizes contrast and separates modal from page.

### Alerts / badges / chips / tabs / menus
Glass is allowed for bounded transient chrome, but state and semantics must be explicit. Never use glow or transparency as the only status cue.

### Tables / dense data
Keep inner data surfaces opaque Flat or Material. Glass may be reserved for toolbar/header chrome.

## State hierarchy
Use this order:

`semantic state -> explicit indicator -> material treatment -> decorative glow`

Focus must remain visible when glass, border, or shadow is removed.

## Accessibility
Test text contrast and focus on worst-case backdrop positions. Support reduced transparency/effects and forced-colors/high-contrast fallback. Keyboard order and accessible names must not depend on visual layering.

## Responsive rules
Reduce blur area/radius before reducing functional control size. Allow text and actions to wrap. Replace wide glass chrome with compact patterns on narrow screens.

## Performance rules
- Blur only small, bounded surfaces.
- Avoid nested backdrop sampling.
- Do not continuously animate blur.
- Avoid large blurred list grids.
- Prefer one shared backdrop layer where practical.
- Remove decorative blur before removing semantic boundaries.

## Progressive fallback
Preferred fallback sequence:

`full glass -> tinted opaque surface -> flat opaque surface`

The same component behavior, labels, focus, selected state, and error state must survive every stage.

## Anti-patterns
- Glass used as wallpaper.
- Glass applied to every nested container.
- Low-opacity white text over bright imagery.
- Blur used as a replacement for hierarchy.
- Interactive controls whose only affordance is a glow or transparency change.
