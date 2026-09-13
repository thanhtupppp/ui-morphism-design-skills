# Material Design — Component Anatomy & Recipes

## 1. What Material Design is

Material Design is not merely rounded cards, purple colors, or elevation. It is a **component and interaction system**. A Material interface is recognizable because components have predictable anatomy, semantic roles, state layers, adaptive behavior, and purposeful motion.

Beginner recognition test:

- A button clearly looks actionable and changes appearance when pressed/focused.
- A text field has a label, input area, supporting/error text, and clear focus state.
- A card groups related content and uses elevation/shape only when spatial separation helps.
- A dialog sits above the application with a scrim and contains a clear title, content, and actions.
- Navigation communicates the current destination with a persistent indicator, not color alone.
- Menus, lists, chips, tabs, switches, checkboxes, and radios follow recognizable interaction patterns.

## 2. System layers

Build Material in this order:

1. Semantic content and interaction.
2. Color roles.
3. Typography roles.
4. Shape scale.
5. Component anatomy.
6. State layers.
7. Elevation/surface hierarchy.
8. Motion.
9. Adaptive layout and density.

A component must remain understandable when elevation or animation is removed.

## 3. Core design tokens

```css
:root {
  --md-bg: #fffbfe;
  --md-surface: #f7f2fa;
  --md-surface-container: #f3edf7;
  --md-surface-high: #ece6f0;
  --md-ink: #1d1b20;
  --md-muted: #49454f;
  --md-primary: #6750a4;
  --md-on-primary: #ffffff;
  --md-secondary: #625b71;
  --md-tertiary: #7d5260;
  --md-error: #b3261e;
  --md-outline: #79747e;
  --md-outline-strong: #49454f;
  --md-focus: #4f378b;
  --md-radius-xs: 4px;
  --md-radius-sm: 8px;
  --md-radius-md: 12px;
  --md-radius-lg: 16px;
  --md-radius-xl: 28px;
  --md-pill: 999px;
  --md-min-target: 48px;
  --md-elev-0: none;
  --md-elev-1: 0 1px 3px rgb(0 0 0 / .20), 0 1px 2px rgb(0 0 0 / .14);
  --md-elev-2: 0 2px 6px rgb(0 0 0 / .20), 0 2px 4px rgb(0 0 0 / .14);
  --md-elev-3: 0 6px 12px rgb(0 0 0 / .20), 0 3px 6px rgb(0 0 0 / .14);
}
```

Use named elevation levels. Never invent arbitrary shadows per component.

## 4. State layers

Material communicates interaction through a combination of surface/color change, state layer, iconography, shape, and semantics.

Required states depend on the component:

`default → hover → focus → pressed → selected → disabled → loading → error/success`

Hover is relevant to pointer environments only. Mobile must communicate every important state without hover.

State layer rules:

- Do not cover labels or icons with a translucent overlay that harms contrast.
- Selected state must be persistent and obvious.
- Focus must be visible and independent of elevation.
- Disabled content may reduce emphasis, but must remain understandable and distinguishable from ordinary secondary content.

## 5. Buttons

### Filled button
Highest-emphasis action in a local action group.

### Outlined button
Secondary action with explicit outline.

### Tonal button
Moderate emphasis using a filled tonal surface.

### Text button
Low-emphasis action without container fill.

### FAB
Prominent compact action tied to the current screen context; do not use it as a generic decorative circle.

Required anatomy:

`container → leading icon(optional) → label → trailing icon(optional)`

Required states:

`default / hover / focus / pressed / disabled / loading`

```css
.md-button {
  min-height: var(--md-min-target);
  min-width: 64px;
  padding: 10px 18px;
  border: 0;
  border-radius: var(--md-pill);
  background: var(--md-primary);
  color: var(--md-on-primary);
  font: inherit;
  font-weight: 650;
}
.md-button:hover { box-shadow: var(--md-elev-1); }
.md-button:active { transform: scale(.98); }
.md-button:focus-visible { outline: 3px solid var(--md-focus); outline-offset: 3px; }
.md-button:disabled,[aria-disabled="true"] { opacity: .55; }
```

## 6. Icon buttons

Icon-only actions require an accessible name and a persistent target area. The visual icon does not replace semantics.

Use distinct treatment for:

- standard icon action
- selected toggle
- overflow/menu
- navigation icon

## 7. Text fields

A field anatomy is:

`label → input → supporting/error text → optional leading/trailing icon`

Required states:

`empty / filled / focused / hovered(web) / disabled / read-only / invalid / valid / loading`

For outlined fields, label placement must remain understandable at rest and focus. Error information must include text, not only a red outline.

## 8. Selection controls

### Checkbox
Independent boolean choice. Selected state uses check/box fill and semantics.

### Radio
One choice within a group. The group needs a visible label and logical keyboard/navigation order.

### Switch
Immediate on/off setting. Show the current state through thumb/track plus accessible state semantics.

### Segmented control
Mutually exclusive or action-group control. Selected segment requires explicit indicator plus accessible state.

## 9. Chips

Use chips for compact filters, categories, selections, or suggestions.

Types:

`assist / filter / input / suggestion`

Do not use chips as miniature paragraphs or unrelated badges.

## 10. Cards and surfaces

Card anatomy:

`container → optional media → title → supporting content → action area`

Card variants:

- elevated
- filled
- outlined

Use elevation to communicate spatial separation, not to decorate every card. Avoid nested cards when a simple section/group is sufficient.

## 11. Lists

List anatomy:

`leading content → headline → supporting content → trailing content`

States may include:

`selected / pressed / disabled / unread / loading / error`

Maintain comfortable row height for touch; do not cram dense desktop data into touch-first list rows.

## 12. Navigation

Common Material navigation patterns:

- Navigation bar for compact/mobile destinations.
- Navigation rail for larger screens.
- Navigation drawer for broader destination sets.
- Tabs for sibling content within one destination.

Active destination must have a persistent indicator, accessible name, and correct selected/current semantics.

## 13. Menus and bottom sheets

Menu anatomy:

`trigger → popup surface → menu item → optional leading/trailing content`

Bottom sheet anatomy:

`drag/position cue → title(optional) → content → actions`

Menus must handle keyboard navigation and dismissal. Sheets must preserve focus and reading order.

## 14. Dialogs

A dialog must:

- block or explicitly separate background interaction when modal;
- expose a title/accessible name;
- provide clear content and actions;
- manage focus entry and focus restoration;
- support Escape/back dismissal where appropriate;
- preserve readable width and text wrapping.

```css
.md-dialog {
  width: min(560px, calc(100vw - 32px));
  padding: 24px;
  border: 0;
  border-radius: var(--md-radius-xl);
  background: var(--md-surface);
  box-shadow: var(--md-elev-3);
}
```

## 15. Snackbar, banner, alert

### Snackbar
Brief feedback about an operation, with optional action. Do not use it for information that must remain visible until acknowledged.

### Banner
Persistent contextual information inside the page hierarchy.

### Alert
Immediate semantic feedback for important error/warning/success information.

Each needs text/icon/state semantics independent of color.

## 16. Progress, loading, and skeletons

Use determinate progress when percentage/quantity is known. Use indeterminate progress when completion cannot be estimated.

Skeletons reserve the same layout region as the eventual content and should not become noisy animated decoration.

## 17. Tables and data-dense surfaces

Material can host dense tables but should not force card-like elevation onto every row.

Required states:

`header / hover / selected / sorted / loading / empty / error`

Keep header, row, and action hierarchy clear. Use density modes for desktop workloads.

## 18. Motion

Motion must explain:

- state change
- spatial relationship
- appearance/disappearance
- continuity between surfaces

Prefer local transform/opacity changes. Do not animate every component. Under reduced motion, replace transitions with immediate state changes or minimal opacity.

## 19. Adaptive layout

Do not scale a desktop layout down until everything becomes tiny. Switch composition according to available space.

Examples:

`navigation rail → navigation bar`
`multi-column → single-column`
`side panel → bottom sheet`
`expanded actions → overflow/menu`

Preserve semantic reading/task order when changing layout.

## 20. Accessibility checklist

- [ ] Names/labels are explicit.
- [ ] Focus is visible without relying on elevation.
- [ ] Color is not the only state channel.
- [ ] Text scales without clipping.
- [ ] Keyboard traversal follows task order.
- [ ] Dialogs manage focus.
- [ ] Disabled/selected/error states remain distinguishable.
- [ ] Touch targets meet the platform policy.
- [ ] Reduced-motion mode works.
- [ ] Contrast is validated for the chosen palette.

## 21. Anti-patterns

- Calling any purple rounded UI “Material”.
- Using elevation on every element.
- Copying default framework components without product adaptation.
- Custom painting standard controls when native semantics already solve the behavior.
- Relying on hover for critical information.
- Treating state-layer opacity as a substitute for accessible semantics.
