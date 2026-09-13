# Liquid Glass — Component Anatomy & Recipes

Liquid Glass is a **functional translucent material**. Components must remain understandable when blur, reflection, and distortion are removed.

## 1. Surface anatomy
A Liquid surface is built in this order:

1. Stable layout and hit area.
2. Base/tinted surface.
3. Backdrop blur, only when supported.
4. Rim/border/highlight.
5. Depth/elevation.
6. Optional reflection.
7. Content and controls.

The material effect is decoration plus spatial grouping; semantics stay in the controls.

## 2. Recognition test
A beginner should be able to point out:
- the parent Liquid surface;
- where the backdrop is visible through it;
- the rim that defines its edge;
- which controls belong to the group;
- which control is selected/focused/pressed;
- what changes when the surface expands.

## 3. Tokens
```css
:root {
  --liquid-bg: #f5f5f7;
  --liquid-fill: rgb(255 255 255 / .62);
  --liquid-fill-strong: rgb(255 255 255 / .76);
  --liquid-fallback: #f5f5f7;
  --liquid-ink: #111827;
  --liquid-muted: #4b5563;
  --liquid-rim: rgb(255 255 255 / .72);
  --liquid-rim-strong: rgb(255 255 255 / .9);
  --liquid-focus: #155e75;
  --liquid-shadow: 0 8px 32px rgb(0 0 0 / .12);
  --liquid-blur-sm: 12px;
  --liquid-blur-md: 20px;
  --liquid-blur-lg: 32px;
  --liquid-radius-sm: 14px;
  --liquid-radius-lg: 26px;
  --liquid-radius-pill: 999px;
  --liquid-target: 44px;
}
```

## 4. Toolbar
A toolbar is one visual material containing multiple actions.

Rules:
- group related controls;
- keep spacing compact but touch-safe;
- selected action gets an explicit indicator;
- overflow action remains discoverable;
- compact state may be pill/capsule, expanded state may be rounded rectangle.

```css
.liquid-toolbar {
  display: flex;
  gap: 8px;
  align-items: center;
  min-height: 52px;
  padding: 6px;
  color: var(--liquid-ink);
  border: 1px solid var(--liquid-rim);
  border-radius: var(--liquid-radius-pill);
  background: var(--liquid-fallback);
  box-shadow: var(--liquid-shadow);
}
@supports (backdrop-filter: blur(1px)) {
  .liquid-toolbar {
    background: var(--liquid-fill);
    backdrop-filter: blur(var(--liquid-blur-md)) saturate(180%);
  }
}
```

## 5. Buttons
Buttons inside Liquid surfaces are usually transparent or lightly tinted.

States:
- default: transparent/light tint;
- hover: subtle surface tint for pointer devices;
- pressed: stronger tint + tiny compression;
- selected: persistent indicator or filled inner pill;
- focus: solid high-contrast ring;
- disabled: readable but visually quieter;
- loading: explicit spinner/progress.

```css
.liquid-button {
  min-width: var(--liquid-target);
  min-height: var(--liquid-target);
  padding: 10px 14px;
  border: 1px solid transparent;
  border-radius: var(--liquid-radius-pill);
  background: transparent;
  color: var(--liquid-ink);
}
.liquid-button:hover { background: rgb(255 255 255 / .36); }
.liquid-button:active { background: rgb(255 255 255 / .48); transform: scale(.98); }
.liquid-button:focus-visible { outline: 3px solid var(--liquid-focus); outline-offset: 3px; }
.liquid-button[aria-pressed="true"] { background: var(--liquid-fill-strong); border-color: var(--liquid-rim-strong); }
```

## 6. Icon button
Icon-only actions require an accessible name and a stable target. Never shrink the hit target merely to preserve a visual pill.

Recommended anatomy:
`icon → accessible name → state indicator when needed`

## 7. Navigation
Liquid navigation works best as a floating functional layer.

Desktop:
- horizontal toolbar or floating navigation;
- active item uses indicator + label/weight.

Mobile:
- compact bottom bar or floating navigation;
- avoid too many items;
- preserve order and accessible labels.

Navigation must remain usable if the material becomes opaque.

## 8. Contextual action group
Use for selection-aware actions, media controls, text editing, or object manipulation.

Behavior:
- appears near relevant content;
- expands without changing action meaning;
- dismisses predictably;
- supports keyboard focus movement;
- has an equivalent non-drag interaction path.

## 9. Floating panel / sheet
A Liquid panel may use rounded geometry and blur, but critical content should remain on a stable inner surface.

Use:
`material shell → optional opaque content region → actions`

Do not place large tables or long reading content directly on a heavily translucent backdrop.

## 10. Dialog
A dialog is a semantic modal first and Liquid material second.

Requirements:
- modal semantics;
- scrim;
- focus trap/containment;
- Escape/close behavior where supported;
- focus restoration;
- stable text contrast;
- opaque fallback.

## 11. Search / command palette
Good use case because the surface is transient and bounded.

Recommended structure:
`Liquid shell → search field → result list → keyboard shortcut/help`

Keep the result list readable and use stable selected-row indicators.

## 12. Form fields
Use conventional, high-contrast fields inside Liquid shells.

A text field needs:
`label → field → helper/error → state`

A translucent field background is allowed only when the backdrop is controlled and contrast-tested. Otherwise use opaque fill.

## 13. Slider / progress
The track may use Liquid styling, but value must be explicit.

For sliders:
- thumb is visually distinct;
- current value is available to assistive tech;
- keyboard increment/decrement works;
- drag is not the only interaction.

## 14. Chips / segmented controls
Chips can use compact Liquid capsules.

Selected chip:
`indicator/fill/border + optional material emphasis`

Do not communicate selection solely by blur or reflection.

## 15. Badge / status
Liquid badge is suitable for non-critical decorative or contextual labels.

Critical status uses semantic color + icon/text; avoid glow-only meaning.

## 16. Lists
Lists inside Liquid navigation are acceptable when the panel is bounded. Each row needs a stable selected/hover/focus cue.

For large lists, reduce blur and use an opaque inner list surface.

## 17. Tables / data grids
Do not place the table itself on a heavily translucent, moving backdrop.

Preferred:
`Liquid outer shell → opaque table surface → semantic rows/cells`

## 18. Expansion / morph state
Liquid surfaces may morph between compact and expanded forms.

Rules:
- stable semantic identity;
- preserve focus when possible;
- announce expanded/collapsed state;
- do not move a focused control to an unrelated location without reason;
- retain usable target size throughout animation.

## 19. State matrix
| State | Main visual cue | Required semantic cue |
|---|---|---|
| Default | translucent material | normal control semantics |
| Hover | tint/highlight | pointer-only enhancement |
| Pressed | stronger tint/compression | pressed/active state |
| Selected | persistent inner fill/indicator | selected/checked state |
| Focus | solid high-contrast ring | keyboard focus |
| Disabled | reduced decoration | disabled state |
| Loading | explicit progress | busy/loading state |
| Error | semantic border/icon/text | error state |
| Expanded | morph/shape change | expanded/collapsed state |

## 20. Fallback ladder
If capabilities are reduced:

**Liquid 4:** blur + tint + rim + reflection + optional distortion

↓

**Liquid 3:** blur + tint + rim + depth

↓

**Liquid 2:** tint + rim + depth

↓

**Liquid 1:** opaque/tinted surface + rim

↓

**Flat fallback:** opaque surface + border

The component must remain functionally identical through the ladder.

## 21. Anti-patterns
- Using Liquid Glass as the whole page background.
- Nested Liquid surfaces where each samples another.
- Full-screen animated distortion.
- Tiny icon buttons below the platform hit target.
- Long text directly over unpredictable imagery.
- Using reflection/glow/distortion as selection or error semantics.
