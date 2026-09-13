# Skeuomorphism Component System

## 1. What a beginner should see immediately

Skeuomorphism makes a digital control look like a believable physical object. The visual language should answer three questions without explanation:

1. **What is the object?** Button, knob, switch, slot, panel, paper, metal plate, etc.
2. **Where can I touch or manipulate it?** Raised edges, recessed wells, handles, grooves, labels, and physical grouping provide the signifier.
3. **What happened after I interact with it?** The object can visibly depress, slide, rotate, toggle, illuminate, or become disabled—but the state must also be communicated by semantics, text, icon, value, or explicit boundary.

The core illusion is **object + material + light + contact + state**. Do not confuse it with adding random gradients or shadows to ordinary UI.

## 2. Visual anatomy

### 2.1 Material body
The main surface represents a physical substance: painted metal, plastic, rubber, paper, wood, leather, glass, ceramic, fabric, or a restrained hybrid.

Rules:
- One dominant material per physical module.
- Material color comes from the simulated object, not from arbitrary decoration.
- Long reading surfaces should remain calm and mostly texture-free.

### 2.2 Bevel / edge
A bevel is the thin transition between top face and side face.

Use:
- light edge on the lit side;
- darker edge on the opposite side;
- consistent direction across the whole module.

The bevel explains thickness. It should not be the only border of an important control.

### 2.3 Highlight
A narrow highlight suggests reflected light on the upper/primary-lit edge.

Keep it subtle. It is a material cue, not a focus ring.

### 2.4 Contact shadow
The darkest soft shadow sits close to the object where it touches the surrounding surface. It explains contact and separation.

### 2.5 Cast shadow
A larger, softer shadow extends away from the object. It describes elevation above the parent surface.

### 2.6 Inset / recess
An inset shadow makes a field, slot, speaker grille, well, or button cavity look carved into the material.

### 2.7 Microtexture
Fine grain, pores, stitching, perforation, brushed metal lines, or paper fibers may reinforce the material.

Microtexture is decorative. It must disappear without breaking comprehension.

### 2.8 Physical grouping
Controls should look mounted into a believable panel, desk, device, instrument, console, folio, or card rather than floating independently.

## 3. Light model

Choose one scene light direction and keep it stable for every related component.

Recommended conceptual model:

- `key-light`: bright top/leading edge
- `fill`: parent surface tone
- `contact`: close dark separation
- `cast`: broad soft depth
- `specular`: tiny bright material cue

Do not rotate the light direction from one component to another. A raised button lit from top-left should not sit next to a card lit from bottom-right.

## 4. Depth ladder

Use named levels instead of arbitrary shadow values:

| Level | Meaning | Typical use |
|---|---|---|
| D0 | flush | labels, icons, reading surfaces |
| D1 | slight lift | compact button, toolbar item |
| D2 | normal module lift | card, mounted control group |
| D3 | pronounced object | floating device module, dialog |
| D4 | hero object | instrument/hero hardware, special focal control |
| R1 | shallow recess | input, slot, tray |
| R2 | deep recess | wells, dials, speaker cavity |

The numbers are semantic levels, not a promise of a particular pixel blur.

## 5. Token foundation

```css
:root {
  --sk-bg: #d8d1c5;
  --sk-face: #d8d1c5;
  --sk-face-dark: #aaa093;
  --sk-face-light: #eee9df;
  --sk-ink: #2e2a25;
  --sk-ink-muted: #625a50;
  --sk-border: #70685d;
  --sk-border-strong: #4f4942;
  --sk-highlight: rgb(255 255 255 / .78);
  --sk-shadow: rgb(0 0 0 / .28);
  --sk-shadow-soft: rgb(0 0 0 / .18);
  --sk-radius-sm: 6px;
  --sk-radius-md: 10px;
  --sk-radius-lg: 14px;
  --sk-control-min: 44px;
  --sk-focus: #0f5b78;
  --sk-danger: #a52a2a;
  --sk-success: #23663a;
  --sk-warn: #8a5b16;
}
```

The project-level theme may replace colors, but preserve the same semantic token roles.

## 6. Buttons

### Visual anatomy
A primary skeuomorphic button normally has:

`label + material face + bevel + contact/cast shadow + pressed state`

### Default
Raised surface; light upper edge; soft outer shadow.

### Hover
Slight brightness or highlight increase. Do not make the button jump.

### Active / pressed
Reduce outer elevation and increase inset shadow. Optional 1px–2px translation may reinforce physical travel.

### Focus-visible
Use a **separate explicit outline/ring** outside the object. Never use inset shadow alone.

### Disabled
Use a stable, lower-contrast material plus disabled semantics. Do not merely make the control look farther away.

```css
.sk-button {
  min-height: var(--sk-control-min);
  padding: 10px 16px;
  color: var(--sk-ink);
  border: 1px solid var(--sk-border);
  border-radius: var(--sk-radius-md);
  background: linear-gradient(var(--sk-face-light), var(--sk-face-dark));
  box-shadow:
    inset 0 1px 0 var(--sk-highlight),
    0 2px 4px var(--sk-shadow),
    0 6px 12px var(--sk-shadow-soft);
}
.sk-button:hover { filter: brightness(1.04); }
.sk-button:active {
  transform: translateY(1px);
  box-shadow: inset 0 2px 4px var(--sk-shadow), 0 1px 2px var(--sk-shadow-soft);
}
.sk-button:focus-visible { outline: 3px solid var(--sk-focus); outline-offset: 3px; }
.sk-button:disabled { filter: saturate(.55); opacity: .62; cursor: not-allowed; }
```

## 7. Icon buttons

Use a physical control body, not a naked icon floating on the panel.

Required:
- accessible name;
- visible pressed/selected state;
- consistent hit target;
- icon remains centered when the physical body depresses.

## 8. Toggle / switch

Think of it as a physical rocker or slide switch.

Visual anatomy:
- track or mounting plate;
- movable actuator;
- clear ON/OFF position;
- optional status lamp.

Do not rely on the position alone. Provide a text/semantic state such as `On` / `Off` to assist screen readers and nonvisual users.

Pressed/checked states can use a recessed track + shifted actuator.

## 9. Slider

A physical slider should look like a rail or slot with a movable handle.

Anatomy:
- rail/channel = recess;
- thumb = raised physical piece;
- value = explicit numeric/text readout where precision matters;
- min/max = optional visible scale for instrument-like controls.

The visual shell must wrap a real accessible range control where possible. Never make a painted thumb the only keyboard-accessible mechanism.

## 10. Knob / rotary control

This is one of the strongest skeuomorphic controls because the physical metaphor directly communicates rotation.

Anatomy:
- circular body;
- center/axis cue;
- indicator line or notch;
- scale/ticks;
- label;
- current value;
- min/max or units where useful.

Interaction:
- pointer/touch drag may rotate;
- keyboard must provide increment/decrement;
- screen reader must expose name, value, and range.

Do not force users to rotate precisely with a gesture. Provide buttons, arrow keys, or another deterministic input path.

## 11. Input / text field

Inputs should look like recessed fields rather than decorative metal plates.

Anatomy:
- persistent label above or beside field;
- opaque inner surface;
- shallow inset shadow;
- visible border;
- helper/error text;
- focus ring outside the recess.

```css
.sk-input {
  min-height: var(--sk-control-min);
  padding: 10px 12px;
  border: 1px solid var(--sk-border);
  border-radius: var(--sk-radius-sm);
  background: var(--sk-face-light);
  color: var(--sk-ink);
  box-shadow: inset 0 2px 4px rgb(0 0 0 / .16);
}
.sk-input:focus { outline: 3px solid var(--sk-focus); outline-offset: 2px; }
```

## 12. Select / dropdown

Treat the control as a physical selector mounted into the panel.

The closed state needs:
- selected value;
- down-arrow or recognizable selector affordance;
- visible boundary.

The menu itself can remain flatter than the shell so scanning and text readability stay strong.

## 13. Checkbox / radio

Checkbox:
- think inset square well + physical tick plate.

Radio:
- think circular socket + raised/recessed indicator.

The checked state should change at least two channels: indicator + color/border/icon/text where practical.

## 14. Card / panel

A skeuomorphic card is usually a **bounded physical module**, not every container in the application.

Anatomy:
- outer material shell;
- heading/label area;
- calm inner content surface;
- optional fasteners, seams, slots, meters, or decorative details only when they support the metaphor.

```css
.sk-card {
  padding: 24px;
  border: 1px solid var(--sk-border);
  border-radius: var(--sk-radius-lg);
  background: linear-gradient(#e5dfd4, #b0a89c);
  box-shadow:
    inset 0 1px 0 var(--sk-highlight),
    0 5px 14px var(--sk-shadow);
}
```

## 15. Toolbar / navigation

A toolbar can look like the control strip on a real instrument, camera, mixer, editor, or console.

Rules:
- group commands by physical function;
- keep the number of controls manageable;
- place frequently used actions in predictable locations;
- do not use texture to replace labels or icon meaning.

Navigation is usually better as a physical frame around flatter content than as a heavily textured strip across the whole application.

## 16. Tabs

Use tabs when content genuinely behaves like physical sheets, compartments, or instrument modes.

The active tab should look raised, inserted, or mechanically selected. The state must also be communicated through text/icon/border and not only through shadow.

## 17. Modal / dialog

Think of a lifted physical module above the work surface.

Recipe:
1. dim/scrim the background;
2. raise the dialog one or two depth levels;
3. keep the content area clean and readable;
4. provide an obvious title, close action, and focus management;
5. avoid heavy realistic decoration around text.

## 18. Alert / status lamp

Industrial and hardware-inspired interfaces can use indicator lights, but the light is supplementary.

A status must have:
- semantic color;
- text/icon or accessible name;
- visible state in non-color or forced-color modes.

Example: `● Recording` is stronger than a red glow with no label.

## 19. Badge / indicator

Small metallic plates, embossed labels, LED-like lamps, and serial-number tags can work well.

Keep micro-detail at a scale where it survives device pixel ratios and localization. Do not use tiny engraved text for essential information.

## 20. Table / data grid

Do **not** make every cell a physical object.

Preferred composition:

`skeuomorphic outer console -> flat/opaque table surface -> restrained row states`

The table should optimize scanning. Selected rows, sort state, errors, and focus remain explicit.

## 21. Progress / meter

A physical meter can use:
- recessed track;
- raised fill;
- tick marks;
- needle or LED indicators.

Still expose the exact numeric progress to assistive technology when precision is useful.

## 22. Tooltip

Tooltips can resemble a small physical label or embossed plate, but keep them mostly flat for readability. They must not be the only place where an essential instruction appears.

## 23. Scrollbars

A hardware-like scrollbar can reinforce a desktop/device metaphor, but native scrolling behavior must remain intact. Never make the track so stylized that users cannot discover it.

## 24. State matrix

| State | Visual cue | Semantic cue |
|---|---|---|
| default | raised | normal |
| hover | highlight/brightness | none required if focus/activation remains clear |
| focus | outer high-contrast ring | focus semantics |
| pressed | inset shadow + slight travel | pressed/active semantics |
| selected | stable physical position + explicit accent/border | selected semantics |
| disabled | lower contrast + flatter depth | disabled semantics |
| loading | restrained progress indicator | busy semantics |
| success | semantic color/icon/text | status text |
| error | semantic color/icon/text | error association |

## 25. Responsive behavior

### Mobile / touch
- Preserve at least 44px touch targets where practical.
- Reduce ornamental texture and shadow complexity.
- Prefer vertical stacking over shrinking tiny controls.
- Move secondary hardware-like details behind expandable sections.

### Tablet
- Maintain coherent physical modules with wider spacing.
- Allow toolbars to wrap or overflow into an intentional menu rather than shrinking labels below usability.

### Desktop
- Use richer instrument/panel grouping when density permits.
- Keep keyboard shortcuts and focus order independent of visual realism.

### Large screens
- Do not stretch texture-heavy objects indefinitely.
- Constrain physical modules to believable proportions and let the surrounding background carry empty space.

## 26. Dark mode

Dark skeuomorphism is not simply `invert()`. Rebuild the material model:
- lower but controlled base luminance;
- lighter edge highlights;
- shadow values that remain visible without becoming pure black holes;
- text contrast recalculated against the new material.

## 27. Texture policy

Texture levels:

- T0: no texture;
- T1: subtle procedural grain/noise;
- T2: fine material texture on bounded surfaces;
- T3: detailed texture only for hero/device surfaces.

Never use T2/T3 for long text backgrounds.

## 28. CSS / React / HTML mapping

HTML/CSS owns the visual primitives:
- `linear-gradient` / `radial-gradient` for material;
- borders for functional boundaries;
- `box-shadow` for contact/cast/inset depth;
- pseudo-elements for highlights and restrained decorative details;
- semantic native controls for behavior.

React should compose these semantics into reusable components. The style is not a React-specific visual implementation.

## 29. Flutter mapping

| Visual intent | Flutter primitive |
|---|---|
| material body | `Container` / `DecoratedBox` + `BoxDecoration` |
| bevel-like edge | border + layered decoration |
| outer depth | one or two `BoxShadow`s |
| inset/recess | layered decoration / `CustomPainter` when necessary |
| gradient | `LinearGradient` / `RadialGradient` |
| physical shell | `DecoratedBox`, `Material`, or `PhysicalModel` when appropriate |
| accessible button | `ElevatedButton`/`FilledButton` inside styled shell |
| input | `TextField` with custom `InputDecoration` |
| slider | `Slider` with custom theme/surrounding shell |
| semantics | `Semantics`, native control semantics, `Focus`/keyboard actions |

Prefer native interactive widgets plus a visual shell over a canvas-only painted control.

## 30. React Native mapping

Use `View`, `Pressable`, `TextInput`, `Slider`, `Switch`, theme tokens, and layered shadows appropriate to the platform. Keep platform-specific shadow behavior behind an adapter rather than assuming browser CSS semantics exist.

## 31. Forced colors and fallback

When decorative gradients, images, textures, or complex shadows disappear, the component must still expose:
- surface boundary;
- label/value;
- focus;
- selected/pressed/disabled state;
- action affordance.

The fallback can be visually flatter. That is acceptable; the interaction contract is not allowed to disappear.

## 32. Performance budget

Avoid:
- dozens of simultaneous large blurred shadows;
- animated grain;
- full-screen raster textures;
- texture applied to every list row;
- unnecessary custom painting of controls that can use native widgets.

Prefer gradients and small overlays over heavy images. Lazy-load hero textures and remove decorative layers on constrained devices.

## 33. Beginner recognition test

A screen is convincingly skeuomorphic when a newcomer can answer, without explanation:

- Which object is the button?
- Which area is recessed input?
- Which part physically moves?
- Which state is active/pressed/selected?
- What material is this object pretending to be?
- From which direction is light coming?
- Which parts are decoration and which parts carry meaning?

If the answers require inspecting CSS instead of looking at the screen, the visual language is incomplete.

## 34. Anti-patterns

- Every component receives the same bevel and shadow.
- Random material mixing with no physical story.
- Decorative texture behind long text.
- Realistic control that is not actually interactive.
- Shadow-only focus/selected/disabled states.
- Tiny rotary controls with no keyboard or deterministic alternative.
- Full-page leather/metal wallpaper that destroys hierarchy.
- Making a table look like 40 separate physical buttons.
