# Skeuomorphism — Cross-Platform Implementation Guide

## Canonical intent
Simulate a bounded physical object with material, thickness, consistent light direction, contact/cast depth, and believable interaction. Visual realism is a progressive layer over an accessible semantic control.

## Platform-neutral contract
Every implementation should preserve this anatomy:

`semantic control -> layout/geometry -> material -> edge/bevel -> depth -> state -> motion -> optional texture`

If an effect is unsupported, remove that effect without changing semantics or layout.

## HTML / CSS

### Preferred primitives
- semantic native HTML controls (`button`, `input`, `select`, `input[type=range]`, etc.);
- `linear-gradient` and `radial-gradient` for material bodies;
- `border` for functional boundaries;
- `box-shadow` for cast/contact/inset depth;
- pseudo-elements for small highlights, seams, or edge details;
- local background images for restrained texture.

### State mapping
- default: raised/outset;
- hover: small luminance/highlight adjustment;
- focus-visible: explicit outer outline;
- active: inset depth + small physical travel;
- disabled: semantic `disabled` plus reduced material intensity;
- selected/pressed: explicit border/accent + physical state.

### Fallback
Use a solid opaque surface whenever gradients, images, or advanced effects are unavailable. Forced-color modes must preserve functional boundaries and focus.

## React

React should not invent a second visual language. Reuse the same HTML semantic primitives and tokens.

Recommended component split:

- `SkeuoButton`
- `SkeuoIconButton`
- `SkeuoSwitch`
- `SkeuoSlider`
- `SkeuoKnob`
- `SkeuoInput`
- `SkeuoPanel`
- `SkeuoToolbar`
- `SkeuoDialog`

Keep the visual shell separate from the behavioral control when custom painting is involved. For example, a knob can render a styled dial around an accessible range input rather than replacing the range interaction entirely.

## Flutter

### Preferred primitives
- `Container` / `DecoratedBox` + `BoxDecoration` for material and gradients;
- `Border` / `BorderSide` for functional edges;
- a small number of `BoxShadow`s for depth;
- `CustomPainter` only for genuinely custom physical details such as tick marks, indicator needles, or complex bevel geometry;
- `FilledButton`, `ElevatedButton`, `IconButton`, `Switch`, `Slider`, `TextField`, `DropdownButton`/Material alternatives for behavior;
- `Semantics` and `Focus`/keyboard actions for custom controls.

### Layering rule
Keep behavior in native/accessible widgets and put the physical treatment in the surrounding decoration. Avoid an all-canvas UI where hit testing, focus, values, and labels must be recreated manually.

### Mapping examples
| Intent | Flutter |
|---|---|
| painted metal/plastic | `BoxDecoration.gradient` |
| raised button | `DecoratedBox` + `FilledButton`/custom `ButtonStyle` |
| inset field | `InputDecoration` + surrounding `BoxDecoration` |
| dial ticks | `CustomPainter` |
| dial value | `Slider`/`Focus` + custom visual shell |
| status lamp | small decorated `Container` + visible label/semantics |
| physical panel | `DecoratedBox` with bounded shadow stack |
| modal | `Dialog` + themed physical surface |

### Flutter-specific caution
Do not assume CSS blur/filter APIs exist as equivalents. A skeuomorphic effect should be translated into Flutter's compositing and paint primitives, not copied literally from CSS.

## React Native

Use native interaction components such as `Pressable`, `TextInput`, `Switch`, and `Slider`. Treat shadows and elevation as platform-adapter details because Android and iOS expose different rendering capabilities. Keep semantic names, states, and hit targets independent of visual decoration.

## Desktop / web hybrid frameworks

For Electron, Tauri, React Native Web, Flutter Web, or similar environments, select the renderer's native primitive first and then add the material shell. Do not use a web-only feature as a required part of the design contract.

## Accessibility invariant
The following must survive removal of realism:

- accessible role/name;
- current value;
- selected/pressed state;
- disabled state;
- error/success state;
- focus visibility;
- keyboard or deterministic alternative to pointer gestures.

Physical cues supplement these signals; they never replace them.

## Responsive rule
Do not preserve realism by shrinking controls. At narrow widths:

- reduce texture resolution/detail;
- reduce shadow layers;
- stack modules;
- preserve readable labels and hit targets;
- move secondary decorative details into noncritical surfaces.

## Performance rule
Use the least expensive technique that communicates the same physical idea. Gradients and simple shadows are preferred; large raster textures, continuous effects, and many simultaneous compositing layers are reserved for bounded hero surfaces.

## Validation matrix
For each platform, verify:

| Capability | HTML/CSS | React | Flutter | RN |
|---|---:|---:|---:|---:|
| semantic native control | ✓ | ✓ | ✓ | ✓ |
| material gradient | ✓ | ✓ | ✓ | ✓/adapter |
| outer shadow | ✓ | ✓ | ✓ | adapter |
| inset/recess | ✓ | ✓ | custom/decoration | adapter/custom |
| explicit focus | ✓ | ✓ | ✓ | ✓ |
| keyboard alternative | ✓ | ✓ | ✓ | ✓/platform |
| texture fallback | ✓ | ✓ | ✓ | ✓ |
| reduced-motion/effect mode | ✓ | ✓ | ✓ | platform-specific |

The implementation is valid only when the lowest-capability target still preserves the semantic contract and an understandable physical metaphor.
