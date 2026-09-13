# Neumorphism

## Purpose
Neumorphism creates the appearance that controls are gently raised from or pressed into a shared surface. It is a **depth language**, not a material language: unlike Skeuomorphism, it should not imitate metal, leather, wood, paper, or hardware textures.

## How to recognize it
A beginner should see:

- one continuous background/surface family
- soft light shadow on one side
- soft dark/contact shadow on the opposite side
- controls that look gently extruded or recessed
- very little texture or hard depth

The signature is the **paired soft-light relationship**, not simply “rounded cards with shadows.”

## Best use
- Compact utilities such as thermostats, media controls, clocks, timers, smart-home panels, and simple device controls.
- Low-density interfaces where tactile grouping is useful.
- Small control clusters that can afford a stable background and restrained palette.

## Avoid
- Dense tables, long forms, documentation, legal text, enterprise CRUD, and large navigation systems.
- Interfaces where background luminance changes constantly.
- Any design where shadows are the only way to identify focus, selection, error, or enabled state.

## Visual DNA
1. Shared or closely related base surface.
2. One consistent light direction.
3. Paired light/dark soft shadows.
4. Raised, flat, and recessed states.
5. Explicit borders/outlines for semantics and accessibility.
6. Minimal texture and minimal gradient complexity.

## Depth model

### Raised
The object visually sits above the same surface.

### Recessed
The object visually sinks into the same surface.

### Flat
Used as a neutral state or where excessive depth would reduce density.

### Pressed
Usually a temporary recessed treatment during activation.

Do not confuse Neumorphism with a generic soft-shadow UI. The parent surface and the control should read as part of the same material plane.

## State rules

State hierarchy should be:

**semantic state → explicit visual cue → optional depth cue**

Examples:

- selected = label/icon/check/indicator + optional pressed shadow
- focus = strong outline/border + optional depth
- invalid = text/icon/border + optional depth
- disabled = reduced interaction + readable content + reduced decoration
- pressed = semantic activation + recessed treatment

## Responsive/adaptive behavior
Neumorphism is sensitive to surface continuity and shadow scale. Recompose rather than shrink a desktop composition:

- **Compact:** reduce decorative shadow spread, stack controls, preserve readable spacing, and keep target sizes intact.
- **Medium:** retain grouped controls while allowing content-driven wrapping and flexible containers.
- **Expanded:** use larger breathing room and bounded shadow stacks without turning every surface into a floating object.

Use flexible Grid/Flex or native layout primitives. Avoid fixed heights and avoid layouts that clip when text scales or localization expands labels. Responsive changes must preserve semantic order and explicit state cues.

## Accessibility and fallback
The fallback is **Flat Design**: opaque surface, explicit border, clear state indicators, no dependence on shadow. Preserve native semantics on web and Flutter controls; apply neumorphic styling around them rather than painting inaccessible custom controls from scratch.

## Performance
Soft shadows are more expensive when numerous and large. Prefer small bounded shadow stacks, avoid animating many shadows simultaneously, and simplify effects on constrained devices.

## Cross-platform principle
The visual intent must survive renderer changes:

- HTML/CSS → paired `box-shadow`
- React → semantic/native DOM + CSS visual shell
- Flutter → `BoxDecoration` + bounded `BoxShadow` + native interactive widgets
- React Native/other → equivalent bounded elevation/shadow primitives, with a flatter fallback when exact inset rendering is unavailable

## Anti-patterns
- full-page monochrome relief
- shadow-only focus/selection
- gray-on-gray text
- every row becoming a floating object
- mixing glass, neon glow, hard brutalist shadows, and neumorphic depth in one component
