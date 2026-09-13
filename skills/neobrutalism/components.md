# Neobrutalism Component Recipes

## 1. Core tokens
```css
:root {
  --neo-bg: #fef6e4;
  --neo-surface: #ffffff;
  --neo-ink: #0a0a0a;
  --neo-border: #0a0a0a;
  --neo-accent-1: #ffdc58;
  --neo-accent-2: #67e8f9;
  --neo-accent-3: #fb7185;
  --neo-focus: #155e75;
  --neo-border-w: 2px;
  --neo-shadow-1: 4px 4px 0 var(--neo-border);
  --neo-shadow-2: 8px 8px 0 var(--neo-border);
  --neo-radius: 0px;
  --neo-target-min: 44px;
}
```

Core rule: border + flat fill + hard zero-blur offset. Do not introduce blur, soft shadows, or transparency as default material behavior.

## 2. Anatomy order
For a beginner, build components in this order:

```text
semantic element
→ size/spacing
→ border
→ flat fill
→ hard offset
→ typography/icon
→ state cue
→ motion
```

The border and offset create visual structure; they are not substitutes for semantic HTML/widgets.

## 3. Button
```css
.neo-button {
  min-height: var(--neo-target-min);
  padding: 10px 16px;
  border: var(--neo-border-w) solid var(--neo-border);
  border-radius: var(--neo-radius);
  background: var(--neo-accent-1);
  color: var(--neo-ink);
  box-shadow: var(--neo-shadow-1);
  font-weight: 800;
}
.neo-button:hover {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0 var(--neo-border);
}
.neo-button:active {
  transform: translate(4px, 4px);
  box-shadow: none;
}
.neo-button:focus-visible {
  outline: 3px solid var(--neo-focus);
  outline-offset: 4px;
}
.neo-button:disabled {
  cursor: not-allowed;
  box-shadow: none;
  opacity: 0.72;
}
```

Press feedback should reduce the offset while preserving the control's semantic/hit bounds. Never depend on motion for feedback.

## 4. Button variants
- **Primary:** dominant accent, strongest hierarchy.
- **Secondary:** white/neutral fill with the same border language.
- **Destructive:** danger-semantic fill plus explicit label/icon.
- **Ghost/text:** use sparingly; retain visible affordance such as underline, border, or strong typographic treatment.
- **Icon-only:** square target, accessible name, visible focus outline.

Do not give every variant a different border/shadow dialect.

## 5. Card / panel
```css
.neo-card {
  min-width: 0;
  padding: 24px;
  border: 3px solid var(--neo-border);
  border-radius: var(--neo-radius);
  background: var(--neo-surface);
  color: var(--neo-ink);
  box-shadow: var(--neo-shadow-2);
}
```

Card anatomy:

```text
heading → supporting text/data → optional media → optional action
```

A card should have one clear job. Use the hard shadow to separate selected/raised modules, not every nested child.

## 6. Input / form field
```css
.neo-input {
  min-height: var(--neo-target-min);
  width: 100%;
  padding: 10px 12px;
  border: var(--neo-border-w) solid var(--neo-border);
  border-radius: 0;
  background: #fff;
  color: var(--neo-ink);
}
.neo-input:focus-visible {
  outline: 3px solid var(--neo-focus);
  outline-offset: 2px;
}
.neo-input[aria-invalid="true"] {
  border-width: 3px;
  border-color: var(--neo-border);
  background: #ffe4e6;
}
```

Form anatomy must remain conventional:

```text
label → input/select/textarea → helper → error/success
```

Never rotate fields, placeholders, helper text, or validation messages.

## 7. Checkbox, radio, switch
Use semantic/native controls or an accessible wrapper. Recommended state cues:

```text
unchecked → checked icon/mark
on → thumb position + fill/border
focus → distinct outline
error → border + icon/text
```

A saturated fill alone is insufficient to communicate selection.

## 8. Navigation / tabs
Navigation can use bold type, hard underline, a filled active block, or a small hard offset. Reserve the strongest treatment for the active/primary destination.

```css
.neo-tab[aria-selected="true"] {
  background: var(--neo-accent-2);
  border: 2px solid var(--neo-border);
  box-shadow: 3px 3px 0 var(--neo-border);
}
```

Do not make every tab look like a primary CTA.

## 9. Badge / chip
Badges and chips are natural places for compact accent blocks. Keep enough padding for wrapping/localization and use icon/text for semantic status.

```css
.neo-chip {
  display: inline-flex;
  min-height: 32px;
  align-items: center;
  gap: 8px;
  padding: 6px 10px;
  border: 2px solid var(--neo-border);
  background: var(--neo-accent-3);
  color: var(--neo-ink);
  font-weight: 700;
}
```

## 10. Alert / banner
Structure:

```text
icon → title/message → optional action/dismiss
```

Critical/error/success states must use explicit semantic language and icons; color only reinforces them.

## 11. Modal / dialog
The dialog may use the same border/offset treatment:

```css
.neo-dialog {
  width: min(92vw, 640px);
  padding: 24px;
  border: 3px solid var(--neo-border);
  background: var(--neo-surface);
  box-shadow: 10px 10px 0 var(--neo-border);
}
```

The overlay/scrim is functional separation, not decoration. Focus management, Escape handling, and return focus belong to the host framework/application.

## 12. Table / data grid
For dense data, use the Neobrutalist vocabulary selectively:

```text
strong outer boundary
→ clear column/header treatment
→ simple row dividers
→ restrained selected/error states
```

Do not put a floating hard shadow around every cell. If density becomes too high, Flat/Material treatment is an acceptable supporting style.

## 13. Loading / skeleton
Use solid blocks with strong boundaries rather than shimmering neon animation. A static skeleton is preferred for reduced motion.

Loading must not look like the page has failed. Preserve the final tile/control footprint where practical to minimize layout shift.

## 14. Empty / error states
**Empty:** clear message + optional illustration + primary next action.

**Error:** semantic error title + explanation + retry/action. Accent color reinforces the state; icon/text carry meaning.

## 15. State matrix
| State | Visual treatment |
|---|---|
| Default | border + fill + normal hard offset |
| Hover | small translation/offset reduction |
| Focus-visible | distinct high-contrast outline |
| Pressed | translate toward offset / remove offset |
| Selected | changed fill/border/icon or explicit marker |
| Disabled | reduced emphasis but still legible |
| Error | explicit border/icon/text treatment |
| Loading | stable shell + progress/skeleton |

## 16. Responsive rules
- Keep usable target sizes stable.
- Allow text and buttons to wrap vertically.
- Remove decorative rotation first.
- Reduce large display type before shrinking controls/body copy excessively.
- Reduce shadow offset when clipping/overflow appears.
- Collapse multi-column cards into document order.
- Do not rely on absolute positioning for semantic relationships.

## 17. Recognition test
Remove rotation, gradients, and illustrations. The system should still read as:

```text
bold typography + strong border + flat fill + hard offset
```

If the design still needs blur, softness, or translucent surfaces to feel like itself, the implementation has drifted toward another style.

## 18. Anti-patterns
- blurred or soft shadows;
- shadow-only boundaries;
- rotated form controls or validation text;
- every component using a different accent;
- oversized type that makes localization fail;
- fixed-height cards that clip text;
- nested interactive controls inside a whole-card link;
- animation used as the only state cue;
- visual noise mistaken for hierarchy.
