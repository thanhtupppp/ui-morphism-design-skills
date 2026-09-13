# Flat Design — Component Anatomy & Recipes

Flat Design means that hierarchy comes from **semantic color, typography, spacing, alignment, grouping, borders, and explicit states** rather than simulated physical depth. A beginner should be able to remove all shadows from a screen and still understand what is a button, field, card, selected item, error, disabled item, and navigation location.

## 1. Visual anatomy

A flat interface is built in this order:

1. Page background.
2. Content container and spacing rhythm.
3. Typography hierarchy.
4. Surface grouping.
5. Functional boundaries such as borders or separators.
6. Semantic colors.
7. Interaction states.
8. Small optional elevation only where it improves grouping.

### Recognition test
A beginner should recognize:

- **Button:** a clearly bounded action with a verb or understandable icon.
- **Input:** a writable region with a persistent label and visible focus/error treatment.
- **Card:** a grouped content region, not automatically an interactive target.
- **Navigation:** a location selector with a persistent active cue.
- **Alert:** a semantic message with icon/text and an appropriate action.
- **Disabled control:** visibly unavailable and not merely light gray text.
- **Selected control:** selected through more than color alone.

## 2. Design tokens

```css
:root {
  --flat-bg: #f7f8fa;
  --flat-surface: #ffffff;
  --flat-surface-subtle: #f1f5f9;
  --flat-surface-strong: #e2e8f0;
  --flat-ink: #18202a;
  --flat-muted: #52606d;
  --flat-border: #cbd5e1;
  --flat-border-strong: #64748b;
  --flat-primary: #2563eb;
  --flat-primary-hover: #1d4ed8;
  --flat-primary-active: #1e40af;
  --flat-success: #15803d;
  --flat-warning: #a16207;
  --flat-danger: #b91c1c;
  --flat-info: #0369a1;
  --flat-focus: #1d4ed8;
  --flat-on-primary: #ffffff;
  --flat-radius-sm: 6px;
  --flat-radius-md: 8px;
  --flat-radius-lg: 12px;
  --flat-control-height: 44px;
  --flat-spacing-1: 4px;
  --flat-spacing-2: 8px;
  --flat-spacing-3: 12px;
  --flat-spacing-4: 16px;
  --flat-spacing-5: 20px;
  --flat-spacing-6: 24px;
  --flat-spacing-8: 32px;
  --flat-shadow-1: 0 1px 2px rgb(0 0 0 / .08);
}
```

Tokens are semantic. Do not scatter literal colors across components. A dark theme should replace roles, not redesign every component.

## 3. Typography

Use typography as the primary depth system:

- Display/hero: high emphasis, short content.
- Heading: section hierarchy.
- Body: default reading text.
- Label: control identification.
- Supporting/meta: secondary information, never critical meaning alone.
- Caption: non-critical supplementary information.

Rules:

- Keep labels persistent for forms.
- Use weight, size, line-height, and spacing before adding decoration.
- Do not use uppercase, italics, or bold on everything.
- Allow text to wrap; never depend on fixed card/button heights for localized copy.

## 4. Buttons

### Primary
Strong semantic fill, clear label, no required shadow.

### Secondary
Lower visual emphasis, usually outlined or neutral-filled.

### Tertiary/Ghost
Minimal surface treatment but still an obvious hit area and hover/focus cue.

### Destructive
Uses semantic danger role and confirmation when the action is irreversible.

### States
Every button has:

- default
- hover (web/pointer)
- pressed/active
- focus-visible
- disabled
- loading when applicable

```css
.flat-button {
  min-height: 44px;
  padding: 10px 16px;
  border: 1px solid transparent;
  border-radius: var(--flat-radius-md);
  background: var(--flat-primary);
  color: var(--flat-on-primary);
  font: inherit;
  font-weight: 650;
  cursor: pointer;
}
.flat-button:hover { background: var(--flat-primary-hover); }
.flat-button:active { background: var(--flat-primary-active); }
.flat-button:focus-visible { outline: 3px solid var(--flat-focus); outline-offset: 3px; }
.flat-button:disabled,
.flat-button[aria-disabled="true"] { opacity: .55; cursor: not-allowed; }
.flat-button[aria-busy="true"] { cursor: wait; }
```

Do not remove the focus ring because the button looks cleaner without it.

## 5. Icon button

An icon-only control must have an accessible name and a visible hit area. The icon itself is not the label.

```css
.flat-icon-button {
  width: 44px;
  height: 44px;
  border: 1px solid var(--flat-border);
  border-radius: 50%;
  background: var(--flat-surface);
  color: var(--flat-ink);
}
```

Use a tooltip only as supplementary discovery, not as the accessible name.

## 6. Inputs and forms

An input consists of:

`label → control → helper/error text → state marker`

Required states:

- empty
- filled
- focus
- disabled
- read-only
- invalid
- valid/success where meaningful
- loading when asynchronous

```css
.flat-input {
  min-height: 44px;
  width: 100%;
  padding: 10px 12px;
  border: 1px solid var(--flat-border-strong);
  border-radius: var(--flat-radius-md);
  background: var(--flat-surface);
  color: var(--flat-ink);
  font: inherit;
}
.flat-input:focus { border-color: var(--flat-primary); outline: 3px solid rgb(37 99 235 / .22); }
.flat-input[aria-invalid="true"] { border-color: var(--flat-danger); }
```

Error messages should state what is wrong and how to fix it. Never communicate invalidity only through a red border.

## 7. Select, checkbox, radio, switch

- **Select:** clear label and current value; custom styling must preserve keyboard behavior.
- **Checkbox:** represents independent boolean choices; selected state must include a check/filled state.
- **Radio:** represents one choice in a group; selected state must be obvious without relying on color.
- **Switch:** represents an immediate on/off setting and needs an accessible state announcement.

Avoid drawing fake controls when native/standard controls already provide correct semantics and interaction.

## 8. Cards and panels

Flat cards are containers first. They may be:

- informational
- interactive
- selectable
- expandable
- draggable

Do not make the entire card clickable unless the card truly represents one action.

```css
.flat-card {
  padding: 24px;
  border: 1px solid var(--flat-border);
  border-radius: var(--flat-radius-lg);
  background: var(--flat-surface);
}
```

For interactive cards, provide a single clear accessible name and avoid nested competing interactive controls.

## 9. Lists

A list needs:

`leading cue → title → secondary information → trailing action/state`

Selected, disabled, unread, loading, and error states must have explicit cues.

Use separators when scanability benefits; otherwise use spacing and grouping.

## 10. Navigation

Navigation identifies **where the user is** and **where they can go**.

Desktop may use top/side navigation; mobile may use bottom navigation or compact menus depending on task frequency.

```css
.flat-nav {
  display: flex;
  gap: 16px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--flat-border);
  background: var(--flat-surface);
}
.flat-nav a[aria-current="page"] {
  color: var(--flat-primary);
  font-weight: 700;
  text-decoration: underline;
  text-underline-offset: 5px;
}
```

The active cue should survive grayscale testing.

## 11. Tabs

Tabs switch between peer views, not unrelated routes. Use a selected indicator plus an accessible selected state. Never make the active tab distinguishable only by a slightly different color.

## 12. Menus and command surfaces

Menu items require a clear label, predictable keyboard order, hover/pressed behavior, disabled treatment, and a visible current selection when selection exists. Group unrelated actions with separators or headings.

## 13. Dialogs and sheets

Flat dialogs rely on:

`surface + scrim + spacing + typography + explicit close/focus behavior`

The scrim separates the modal task from the page. The dialog itself should remain opaque and readable.

## 14. Alerts, banners, snackbars

Use semantic role + icon + text + action. Severity examples:

- info
- success
- warning
- error

Color is supplementary. An error should still be understandable in monochrome.

## 15. Badges, chips, tags

Badges are for concise metadata/status. Chips can represent filters, selections, or compact actions. Do not turn every piece of metadata into a chip; overuse creates visual noise.

## 16. Tables and data grids

Flat Design is especially strong for data-dense interfaces.

Required table states:

- header
- body
- hover/focus where applicable
- selected row
- sorted column
- loading
- empty
- error
- pagination/overflow

Keep table surfaces opaque. Prefer alignment and column spacing to excessive borders.

## 17. Forms and dense workflows

Use a consistent vertical rhythm. Group fields by task, not by data type. Keep destructive actions visually and spatially separated from routine actions. Preserve DOM/focus order when layouts change responsively.

## 18. Progress and status

Progress bars, meters, spinners, and status dots must have a textual or semantic interpretation when the state matters. Never encode status solely as green/yellow/red.

## 19. Empty, loading, and error states

Every major content surface should define:

- empty: what this means + what to do next
- loading: stable skeleton or progress cue
- error: what failed + retry/recovery action
- partial: what is available and what is missing

## 20. Responsive behavior

Use mobile-first layout. Recommended validation widths:

- 320–375px compact phone
- 768px tablet
- 1024px desktop/tablet landscape
- 1440px large desktop

Use content-driven breakpoints. Let columns collapse before text becomes unreadably narrow. Preserve logical DOM order. Do not solve mobile layout by simply shrinking desktop typography.

## 21. Density modes

Flat Design supports explicit density profiles:

- Comfortable: more padding and larger rows.
- Standard: balanced production default.
- Compact: dense tables and professional tools.

Changing density should alter spacing and control height consistently rather than randomly shrinking individual elements.

## 22. Motion

Motion is optional. Prefer short opacity/transform transitions for state feedback. Never use motion to communicate information that is unavailable in the final static state. Under reduced motion, remove non-essential transitions and preserve immediate state feedback.

## 23. Dark mode

Dark mode changes semantic surface and text roles. Do not simply invert colors. Preserve hierarchy through contrast, border strength, and spacing. Re-test status colors and focus indicators on both themes.

## 24. Accessibility and resilience

Flat Design is the baseline/fallback for effect-heavy styles. Test:

- keyboard-only operation
- visible focus
- screen-reader names/roles/states
- grayscale
- high contrast / forced colors where supported
- zoom and text scaling
- long localized strings
- RTL layouts when applicable
- disabled motion
- missing imagery

WCAG 2.2 adds requirements around focus not being obscured and minimum target size; the design system should account for these at the component level rather than leaving them to individual screens. See the platform contract for renderer-specific target guidance.

## 25. Performance

Flat Design should be the cheapest visual path. Avoid unnecessary filters, large shadows, decorative background images, and layout-triggering animation. Keep component styles tokenized so theming does not duplicate whole component trees.

## 26. Anti-patterns

- “Flat” meaning no hierarchy.
- Gray-on-gray text.
- Hidden borders and removed focus indicators.
- Every item given the same visual weight.
- Color as the only state signal.
- Giant rounded cards for every tiny piece of information.
- Fixed-height controls that break under localization or text scaling.
- Custom controls that reproduce native behavior poorly.
