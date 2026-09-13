# Neumorphism — Component Anatomy & Recipes

## 1. What Neumorphism is

Neumorphism makes a control appear to **rise from** or **sink into** one continuous surface. Unlike Skeuomorphism, it does not imitate a physical material such as metal or leather. The illusion comes from the relationship between the surface color and two soft lights: a lighter edge on the light-facing side and a darker contact shadow on the opposite side.

### Beginner recognition test

A beginner should be able to point to:

- **Raised:** looks like the control is gently pushed out of the same background.
- **Pressed/concave:** looks like the control is pushed into the background.
- **Flat:** looks inactive, neutral, or intentionally un-elevated.
- **Focus:** a clear outline/border that remains visible even when shadows are removed.

If removing all shadows makes state or affordance impossible to understand, the implementation is incorrect.

## 2. The four visual states

### Raised / convex
Use paired outer shadows:

- light shadow toward the light source
- dark shadow away from the light source
- same or closely related base surface color

This is the default state for compact controls.

### Hover
On web/pointer interfaces, hover may slightly increase contrast or shift the control by 1px, but should not become a new depth system.

### Pressed / concave
Use paired inset shadows so the control appears pushed into its parent surface. The content itself should not visibly disappear.

### Selected / toggled
Selected controls may use the pressed treatment **plus** a persistent semantic cue such as a check mark, label, icon, stronger border, or state text. Do not use the pressed shadow alone.

### Focus-visible
Focus is always a separate system. Use a strong outline/border with enough separation from the soft shadow.

### Disabled
Reduce interaction affordance and decoration, but retain a readable label/icon and enough boundary information to distinguish the control from surrounding content.

## 3. Material rules

Neumorphism normally uses:

- one calm base surface
- one light direction
- one soft light shadow
- one soft dark shadow
- restrained radius
- minimal gradients

Avoid:

- multiple colored glows
- hard drop shadows
- unrelated textures
- glass transparency
- nested neon effects

The point is **continuity of surface**, not decorative complexity.

## 4. Token system

```css
:root {
  --neu-bg: #e6e7ee;
  --neu-surface: #e6e7ee;
  --neu-ink: #272b35;
  --neu-ink-muted: #5b6472;
  --neu-border: #697386;
  --neu-light: #ffffff;
  --neu-dark: #b8b9be;
  --neu-focus: #334155;
  --neu-raised: 8px 8px 16px var(--neu-dark), -8px -8px 16px var(--neu-light);
  --neu-raised-sm: 4px 4px 8px var(--neu-dark), -4px -4px 8px var(--neu-light);
  --neu-pressed: inset 5px 5px 10px var(--neu-dark), inset -5px -5px 10px var(--neu-light);
  --neu-radius-sm: 10px;
  --neu-radius-md: 14px;
  --neu-radius-lg: 24px;
  --neu-control-height: 44px;
}
```

Tokens must be role-based so a dark theme can replace the palette without rewriting component structure.

## 5. Buttons

### Primary neumorphic button
Use only when the product is low-density and the action benefits from a tactile control metaphor.

```css
.neu-button {
  min-height: var(--neu-control-height);
  padding: 10px 16px;
  border: 1px solid transparent;
  border-radius: var(--neu-radius-md);
  background: var(--neu-surface);
  color: var(--neu-ink);
  box-shadow: var(--neu-raised-sm);
  font: inherit;
  font-weight: 650;
}
.neu-button:hover { color: #111827; }
.neu-button:active,
.neu-button[aria-pressed="true"] { box-shadow: var(--neu-pressed); }
.neu-button:focus-visible { outline: 3px solid var(--neu-focus); outline-offset: 4px; }
.neu-button:disabled { opacity: .55; cursor: not-allowed; box-shadow: none; }
```

### Button anatomy
`label/icon → touch target → raised surface → paired shadow → focus ring → pressed state`

Never place critical text inside a shadow-only visual boundary.

## 6. Icon button

Use a circular or softly rounded raised body, but retain a visible hit area.

Requirements:

- accessible name
- pressed/selected representation when applicable
- focus ring
- minimum touch target
- tooltip only as supplementary discovery

## 7. Inputs and forms

An input is commonly **concave**, because the visual metaphor is that the user is entering content into a recessed area.

An input consists of:

`persistent label → field → helper/error text → state marker`

```css
.neu-input {
  min-height: var(--neu-control-height);
  width: 100%;
  padding: 10px 12px;
  border: 1px solid var(--neu-border);
  border-radius: var(--neu-radius-sm);
  background: var(--neu-surface);
  color: var(--neu-ink);
  box-shadow: var(--neu-pressed);
}
.neu-input:focus { outline: 3px solid var(--neu-focus); outline-offset: 2px; }
.neu-input[aria-invalid="true"] { border-color: #b91c1c; }
```

Error and success states need text/icon cues. Border and inset shadow are visual supplements.

## 8. Checkbox, radio, switch

### Checkbox
A raised square can become pressed/selected with a visible check mark. The check mark is the semantic state cue.

### Radio
A recessed circle plus a clear inner mark works better than changing shadow intensity only.

### Switch
Use a raised track and a movable thumb, but expose the on/off state through accessible semantics and a persistent visual cue. The thumb movement is not sufficient on its own.

## 9. Slider and knob-like controls

Neumorphism works especially well for compact hardware-like utilities.

### Slider
- track: recessed
- thumb: raised
- active portion: explicit color/indicator
- current value: text when precision matters
- keyboard increment/decrement: required on accessible implementations

### Rotary control
A rotary dial may use a concentric raised body, recessed center, and indicator notch. Never make rotation the only way to change the value; provide keyboard/buttons or an accessible slider alternative.

## 10. Cards and panels

Cards should use **fewer and larger** shadows than individual controls. The whole page must not look like a field of floating blobs.

```css
.neu-card {
  padding: 24px;
  border-radius: var(--neu-radius-lg);
  background: var(--neu-surface);
  box-shadow: var(--neu-raised);
}
```

Use cards for bounded groups, not every paragraph or row.

## 11. Navigation

Navigation should normally use a Flat/Material treatment around neumorphic controls. If navigation itself is neumorphic, use only one depth level and keep the active destination explicit through icon/label weight, indicator, or pressed treatment.

## 12. Menus, dialogs, alerts

- **Menu:** use a raised surface with clear item separation and keyboard focus.
- **Dialog:** can be raised from the page surface, but use a scrim/overlay so boundaries remain obvious.
- **Alert:** semantic color, icon, and text carry meaning; neumorphic depth is decorative.

## 13. Progress and status

Do not communicate progress or health through shadow strength. Use a track + explicit fill/value. Status lamps can be raised, but status must also be labeled or iconified.

## 14. Lists and tables

Neumorphism is a poor fit for dense tables. Prefer Flat or Material surfaces. For short lists, a selected item may use a recessed treatment, but maintain text/icon contrast and clear spacing.

## 15. Motion

Use short interaction transitions:

- hover: subtle color/translation
- press: shallow transition to inset
- release: return to raised state
- toggle: immediate semantic state + optional short motion

Do not animate large numbers of soft shadows simultaneously. Under reduced motion, switch directly between states.

## 16. Responsive behavior

Neumorphism should become **simpler**, not more crowded, on small screens.

- collapse decorative shadow layers
- maintain touch targets
- allow labels to wrap
- avoid fixed-height cards
- move dense data areas to Flat/Material surfaces
- keep one consistent light direction

## 17. Accessibility and fallback

The visual fallback is a Flat opaque surface with explicit borders and state indicators.

Test:

- keyboard focus
- screen-reader names/states
- high contrast / forced colors
- dark theme
- grayscale
- text scaling
- localization/RTL
- reduced motion
- low-power mode

Shadow is decorative. It must never be the only indication of focus, selection, error, disabled, or enabled state.

## 18. Anti-pattern gallery

### Wrong: full-page relief
Every surface has the same two shadows and nothing has hierarchy.

### Wrong: shadow-only selected state
The user cannot tell what is selected without seeing the bevel.

### Wrong: gray-on-gray text
Soft surfaces make low-contrast text even harder to read.

### Wrong: neumorphic table
Rows, cells, headers, and controls all become raised objects, destroying scanability.

### Wrong: mixed material systems
Neumorphism + glass + neon gradients on the same control create an incoherent visual language.
