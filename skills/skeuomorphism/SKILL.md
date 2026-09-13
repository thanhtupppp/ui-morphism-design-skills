# Skeuomorphism

## Definition
Skeuomorphism is an interface visual language that borrows recognizable physical materials, geometry, lighting, and mechanical behavior to communicate what an object is and how it can be manipulated. The goal is **affordance transfer**, not photorealism: the user should understand “press”, “turn”, “slide”, “open”, or “insert” from visual cues before reading documentation. Contemporary skeuomorphism should keep useful physical signifiers while removing decorative clutter that harms clarity.

## What makes it unmistakable
A correct skeuomorphic object normally combines several of these cues:

- **material**: metal, plastic, rubber, leather, paper, wood, ceramic, glass, fabric;
- **thickness**: bevel, edge, rim, seam, recessed cavity;
- **light**: consistent highlight and shadow direction;
- **contact**: cast/contact shadow showing where the object sits;
- **mechanics**: press, slide, rotate, toggle, latch, dial, slot;
- **surface detail**: restrained grain, stitching, perforation, screws, ticks;
- **explicit semantics**: text, icon, value, state, focus, and accessible name.

Skeuomorphic styling is incomplete when the object only looks realistic but its interactive behavior does not match the implied physical behavior.

## Use when
- The product represents a device, instrument, vehicle, camera, audio tool, simulator, game control, or physical workspace.
- A physical metaphor materially improves discoverability or learnability.
- Material identity is part of the brand or product experience.
- A compact set of controls benefits from tactile differentiation.

## Avoid or constrain when
- The interface is mostly dense tables, forms, legal text, logs, or long reading.
- The physical metaphor is unfamiliar, misleading, or stronger than the task itself.
- Realistic assets create large transfer sizes or slow rendering.
- A full-screen texture would reduce text contrast or visual hierarchy.
- The product needs a highly neutral cross-platform system and realism offers no functional benefit.

## Design hierarchy
Use this order of importance:

1. Task and semantics.
2. Layout and grouping.
3. Functional boundary and state.
4. Physical depth and material cues.
5. Decorative realism.

Never invert this order.

## Visual grammar

### Material
Choose one dominant material per physical module. A believable surface has a base tone plus restrained highlights/shadows. Avoid mixing leather, chrome, wood, paper, and glass arbitrarily.

### Lighting
Pick one global light direction for a module family. All highlights and cast/contact shadows should agree with that direction. Light is a system token, not an isolated component decision.

### Depth
Use semantic depth levels such as flush, slight lift, module lift, floating, and recess. Do not create a unique arbitrary shadow for every component.

### Bevel
Bevels explain thickness. They are created with edge contrast, gradient transitions, borders, and/or layered decoration. A bevel is not a functional focus indicator.

### Texture
Texture is optional. Prefer CSS gradients/procedural effects or compact assets over large raster backgrounds. Texture may reinforce material but must not carry essential information.

### Physical behavior
Visual state should match implied mechanics:
- raised -> available/pressable;
- inset -> recessed/input/mounted;
- depressed -> pressed/engaged;
- moved -> slider/switch value changed;
- rotated -> dial value changed;
- illuminated -> state/status, paired with explicit semantics.

## Component principles

- **Button**: raised by default, visibly travels/presses, explicit focus ring, stable label.
- **Icon button**: physical body around a meaningful icon; accessible name required.
- **Switch**: track/casing + movable actuator + explicit on/off semantics.
- **Slider**: recessed rail + raised thumb + deterministic keyboard/touch path.
- **Knob**: circular body + indicator + value/range + keyboard alternative.
- **Input**: recessed opaque field with persistent label and visible focus.
- **Card/panel**: bounded physical module; inner content remains calm.
- **Toolbar**: hardware-like control strip; avoid crowding.
- **Dialog**: lifted module over a scrim; focus management remains explicit.
- **Table**: flat/opaque reading surface inside a physical shell, not dozens of mini physical objects.

See `components.md` for the full anatomy, state matrix, responsive behavior, tokens, and implementation recipes.

## Platform rule
The style is defined by intent, not by CSS syntax. HTML/CSS, React, Flutter, and React Native must preserve the same semantic anatomy while using native primitives for behavior and platform-appropriate rendering for effects.

Required implementation order:

1. semantic/accessible control;
2. layout and size;
3. material decoration;
4. depth/effect;
5. motion;
6. optional decorative texture.

When a platform cannot reproduce an effect, remove or simplify the effect and keep the interaction intact.

## Motion
Use short physical feedback: small translation for press, controlled rotation for dials, modest slide for switches. Do not bounce, shake, or continuously animate decorative texture. Respect reduced-motion preferences.

## Responsive and performance
- Keep touch targets at least 44px where practical.
- Do not shrink controls below usability to preserve a desktop metaphor.
- Reduce texture, shadow layers, and expensive custom painting on smaller/constrained devices.
- Prefer a few intentional layers over many composited shadows.
- Keep lists and tables mostly flat; reserve expensive material effects for bounded hero/device modules.

## Accessibility
Physical realism never replaces semantics. Labels, values, selection, errors, focus, disabled state, and keyboard/touch alternatives must remain explicit. Functional borders must survive removal of gradients, shadows, textures, and images.

## Fallback modes
Provide a `flat-fallback` or equivalent mode for:
- forced colors/high-contrast settings;
- reduced transparency/effects;
- low-power/constrained rendering;
- unsupported platform capabilities;
- print/export modes where appropriate.

A fallback may look less realistic. It must remain understandable and operable.

## Validation questions
Before declaring the style implemented, verify:

- Does a newcomer identify each control without a tutorial?
- Does the visual affordance match the actual interaction?
- Is light direction consistent?
- Are material and texture bounded?
- Are states explicit without relying on shadow/color alone?
- Can every custom gesture be replaced by a deterministic accessible action?
- Does the UI still work when decorative effects are removed?
- Does the same design intent survive on HTML/CSS, React, and Flutter?

## Anti-patterns
- Realism without affordance.
- Decorative texture used as a boundary or status signal.
- Shadow-only focus, selected, or disabled state.
- Inconsistent light direction.
- Full-page heavy textures.
- Every component receiving the same bevel and shadow.
- Hardware-looking controls that are not actually interactive.
- Tiny dials/targets with no alternate input path.
- Tables and forms made to look like collections of physical buttons.
