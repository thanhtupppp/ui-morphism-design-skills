# Neobrutalism

## Purpose
Neobrutalism uses saturated flat fills, bold typography, solid borders, hard offset shadows, and direct interaction feedback.

## Use when
- The brand is expressive, indie, technical, creator-focused, or campaign-oriented.
- Differentiation and a hand-built tone matter more than quiet neutrality.

## Avoid when
- The product is a regulated workflow, dense enterprise tool, luxury system, or reading-heavy interface.
- Thick borders, rotation, or large type would harm localization and scanning.

## Visual DNA
- Use one hard border token and one unblurred offset shadow scale.
- Keep radius 0–8px or define a deliberate dialect; do not drift into claymorphism.
- Use 2–3 accent colors per screen and a calm paper/ink ground.
- Treat typography as structure, not decoration.

## Token recipe
```css
:root {
  --um-neobrutalism-bg: #fef6e4;
  --um-neobrutalism-surface-1: #ffffff;
  --um-neobrutalism-ink: #0a0a0a;
  --um-neobrutalism-border-strong: #0a0a0a;
  --um-neobrutalism-accent: #ffdc58;
  --um-neobrutalism-shadow-2: 4px 4px 0 var(--um-neobrutalism-border-strong);
  --um-neobrutalism-target-min: 44px;
}
.um-neo-button { min-height: var(--um-neobrutalism-target-min); border: 2px solid var(--um-neobrutalism-border-strong); background: var(--um-neobrutalism-accent); color: var(--um-neobrutalism-ink); box-shadow: var(--um-neobrutalism-shadow-2); }
.um-neo-button:hover { transform: translate(2px, 2px); box-shadow: 2px 2px 0 var(--um-neobrutalism-border-strong); }
.um-neo-button:focus-visible { outline: 3px solid #155e75; outline-offset: 4px; }
```

## Component rules
- Button: press translation must preserve target size and focus.
- Card: use hard shadow for selected/raised state, not for every element.
- Form: keep labels and errors conventional; do not rotate input text or controls.
- Badge/alert: use explicit icon/text; color is supplementary.

## Motion and responsive
Use short transform feedback only. Avoid shaking, looping, or decorative rotation. Remove rotation and reduce type scale at narrow widths. Check translated shadows for overflow.

## Accessibility checklist
- [ ] Text contrast is tested against each accent fill.
- [ ] Focus ring is distinguishable from the thick border.
- [ ] Forced-colors mode retains border and semantic state.
- [ ] DOM order is meaningful without visual collage.
- [ ] Localization does not overflow fixed cards or buttons.

## Anti-patterns
- Shadow-only boundaries.
- Rotated labels, inputs, or error messages.
- Every component competing with the primary action.
