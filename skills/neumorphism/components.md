# Neumorphism — Component Anatomy & Recipes

Neumorphism makes controls rise from or sink into one continuous surface. Shadow is decorative depth; semantic state must survive when shadows disappear.

## Token system

```css
:root {
  --um-neumorphism-bg: #e6e7ee;
  --um-neumorphism-surface-1: #e6e7ee;
  --um-neumorphism-ink: #272b35;
  --um-neumorphism-ink-muted: #5b6472;
  --um-neumorphism-border: #697386;
  --um-neumorphism-shadow-light: #ffffff;
  --um-neumorphism-shadow-dark: #b8b9be;
  --um-neumorphism-focus: #334155;
  --um-neumorphism-shadow-raised: 8px 8px 16px var(--um-neumorphism-shadow-dark), -8px -8px 16px var(--um-neumorphism-shadow-light);
  --um-neumorphism-shadow-raised-sm: 4px 4px 8px var(--um-neumorphism-shadow-dark), -4px -4px 8px var(--um-neumorphism-shadow-light);
  --um-neumorphism-shadow-pressed: inset 5px 5px 10px var(--um-neumorphism-shadow-dark), inset -5px -5px 10px var(--um-neumorphism-shadow-light);
  --um-neumorphism-radius-sm: 10px;
  --um-neumorphism-radius-md: 14px;
  --um-neumorphism-radius-lg: 24px;
  --um-neumorphism-target-min: 44px;
}
```

## Buttons and inputs

```css
.neu-button {
  min-height:var(--um-neumorphism-target-min);
  padding:10px 16px;
  border:1px solid var(--um-neumorphism-border);
  border-radius:var(--um-neumorphism-radius-md);
  background:var(--um-neumorphism-surface-1);
  color:var(--um-neumorphism-ink);
  box-shadow:var(--um-neumorphism-shadow-raised-sm);
}
.neu-button:active,
.neu-button[aria-pressed="true"] { box-shadow:var(--um-neumorphism-shadow-pressed); }
.neu-button:focus-visible { outline:3px solid var(--um-neumorphism-focus); outline-offset:4px; }

.neu-input {
  min-height:var(--um-neumorphism-target-min);
  width:100%;
  border:1px solid var(--um-neumorphism-border);
  border-radius:var(--um-neumorphism-radius-sm);
  background:var(--um-neumorphism-surface-1);
  color:var(--um-neumorphism-ink);
  box-shadow:var(--um-neumorphism-shadow-pressed);
}
```

Selected controls require a persistent check/icon/label/border cue in addition to pressed depth. Inputs retain labels and text/icon validation feedback.

## State matrix

| State | Required cue | Depth treatment |
|---|---|---|
| Default | Stable border and readable label | Raised surface |
| Hover | Clear affordance without relying on shadow | Slight contrast change |
| Active / pressed | Pressed semantics where applicable | Inset surface |
| Selected | Check, icon, label, or persistent border | Optional inset surface |
| Focus-visible | High-contrast outline | Depth unchanged |
| Disabled | Disabled semantics and readable reduced emphasis | Reduced shadow |
| Loading | Busy semantics plus progress text, spinner, or skeleton | Static surface |

## Components and semantics

Checkboxes, radios, switches, sliders and rotary controls use native/semantic behavior first. Drag or rotation always has a keyboard/button or accessible slider alternative. Cards use fewer shadow layers than controls; dense tables use Flat/Material surfaces.

## Accessibility and fallback

Focus uses an explicit outline. Error, selection, disabled and loading states never depend on shadow alone. Forced-colors, large text, localization, RTL and reduced motion remain usable.

## Responsive matrix

| Layout | Treatment |
|---|---|
| Compact, below 768px | Reduce shadow spread and radius before changing control size or spacing. |
| Medium, 768–1023px | Use raised depth on controls and a flatter treatment for supporting cards. |
| Expanded, 1024px and above | Keep depth hierarchy bounded; do not repeat large shadows across dense grids. |

Fallback:

```text
paired soft depth
→ reduced depth + explicit border
→ flat opaque surface + border/state indicators
```

## Performance

Keep shadow stacks bounded, avoid simultaneous shadow animation across large lists, and simplify depth on constrained devices before changing semantics or target geometry.

## Anti-patterns

- Full-page relief with no hierarchy.
- Shadow-only selection/focus.
- Gray-on-gray unreadable text.
- Neumorphic dense tables.
- Mixing glass/neon/hard-shadow material systems into the same control.
