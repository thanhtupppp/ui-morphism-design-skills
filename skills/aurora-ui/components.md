# Aurora UI Component Recipes

Aurora is primarily an atmospheric layer. Component recipes below preserve semantic, stable controls while using Aurora selectively for emphasis.

## 1. Token contract

```css
:root {
  --um-aurora-ui-bg: #0d1021;
  --um-aurora-ui-aurora-a: #6d5dfc;
  --um-aurora-ui-aurora-b: #19c6b5;
  --um-aurora-ui-aurora-c: #ff6b9a;
  --um-aurora-ui-surface-1: rgb(255 255 255 / .94);
  --um-aurora-ui-surface-2: rgb(255 255 255 / .98);
  --um-aurora-ui-ink: #101426;
  --um-aurora-ui-ink-muted: #526078;
  --um-aurora-ui-focus: #f8d34f;
  --um-aurora-ui-border: rgb(255 255 255 / .26);
  --um-aurora-ui-blur-1: 64px;
  --um-aurora-ui-radius-card: 20px;
  --um-aurora-ui-radius-control: 12px;
  --um-aurora-ui-target-min: 44px;
}
```

Keep decorative Aurora tokens separate from application semantic tokens such as error, success, and selected roles.

## 2. Anatomy of an Aurora page

```text
page
├─ stable ground
├─ aurora field
│  ├─ light source A
│  ├─ light source B
│  └─ optional light source C
├─ optional scrim/protection layer
└─ content
   ├─ navigation
   ├─ hero/focal module
   ├─ cards
   └─ controls/data
```

The Aurora field should be siblings/ancestors of content, not an effect that causes content itself to become blurred or translucent.

## 3. Base background

Use a few large light fields. Start with one dominant and one accent, then add a third only when it improves hierarchy.

```css
.aurora-page {
  position: relative;
  isolation: isolate;
  min-height: 100%;
  overflow: hidden;
  padding: 24px;
  background: var(--um-aurora-ui-bg);
}

.aurora-page::before {
  content: "";
  position: absolute;
  inset: -30%;
  z-index: -1;
  pointer-events: none;
  background:
    radial-gradient(circle at 18% 22%, var(--um-aurora-ui-aurora-a), transparent 34%),
    radial-gradient(circle at 78% 18%, var(--um-aurora-ui-aurora-b), transparent 30%),
    radial-gradient(circle at 58% 82%, var(--um-aurora-ui-aurora-c), transparent 32%);
  filter: blur(var(--um-aurora-ui-blur-1));
  opacity: .82;
}
```

The page remains usable when `::before` is removed.

## 4. Hero

Hero anatomy:

`Aurora field → protection layer → eyebrow → heading → supporting text → primary CTA → secondary CTA`

Prefer a stable hero surface when text overlaps a strong or moving light region.

```css
.aurora-hero {
  max-width: 760px;
  padding: 32px;
  border-radius: var(--um-aurora-ui-radius-card);
  background: var(--um-aurora-ui-surface-1);
  color: var(--um-aurora-ui-ink);
}
```

Hero focus should come from composition and content importance. A stronger glow can support the hero, but must not replace layout hierarchy.

## 5. Card / feature card

A card can be completely neutral. A single primary card may receive a restrained edge glow.

```css
.aurora-card {
  padding: 24px;
  border: 1px solid var(--um-aurora-ui-border);
  border-radius: var(--um-aurora-ui-radius-card);
  background: var(--um-aurora-ui-surface-1);
  color: var(--um-aurora-ui-ink);
}

.aurora-card--featured {
  box-shadow: 0 0 0 1px rgb(139 124 255 / .18), 0 18px 50px rgb(0 0 0 / .16);
}
```

Do not place an animated gradient background on every card.

## 6. Button

The button remains a semantic control. Aurora can provide surrounding atmosphere but the button itself must show its state through fill, border, contrast, or native interaction feedback.

```css
.aurora-button {
  min-height: var(--um-aurora-ui-target-min);
  min-width: var(--um-aurora-ui-target-min);
  padding: 10px 16px;
  border: 0;
  border-radius: 999px;
  background: #4338ca;
  color: #fff;
  font: inherit;
  font-weight: 700;
}

.aurora-button:hover { filter: brightness(1.05); }
.aurora-button:active { transform: translateY(1px); }
.aurora-button:focus-visible {
  outline: 3px solid var(--um-aurora-ui-focus);
  outline-offset: 3px;
}
.aurora-button:disabled {
  opacity: .55;
  cursor: not-allowed;
}
```

Avoid a transparent button whose only visible difference is a glowing halo.

## 7. Icon button

Use the same state contract as a normal button. Provide an accessible name.

```css
.aurora-icon-button {
  width: var(--um-aurora-ui-target-min);
  height: var(--um-aurora-ui-target-min);
  border: 1px solid rgb(16 20 38 / .16);
  border-radius: var(--um-aurora-ui-radius-control);
  background: var(--um-aurora-ui-surface-2);
}
```

The icon should not be the only state indicator when the action becomes selected/active.

## 8. Input / text field

Input anatomy:

`label → field → helper text or error → state marker`

```css
.aurora-input {
  min-height: var(--um-aurora-ui-target-min);
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #9ca3af;
  border-radius: var(--um-aurora-ui-radius-control);
  background: #fff;
  color: var(--um-aurora-ui-ink);
  font: inherit;
}

.aurora-input:focus-visible {
  outline: 3px solid var(--um-aurora-ui-focus);
  outline-offset: 2px;
}

.aurora-field[data-invalid="true"] .aurora-input {
  border-color: #b42318;
}
```

Do not use an animated glow as the validation state.

## 9. Select / checkbox / radio / switch

Keep the interactive primitive visually conventional and semantic. Aurora may remain behind the group, but selection must be persistent and explicit.

Recommended hierarchy:

`label → native control → visible selected/unselected state → helper/error`

## 10. Slider / progress / meter

Use a stable track and explicit value. Aurora may tint the surrounding region, but the value indicator must remain distinct without glow.

```css
.aurora-progress {
  height: 8px;
  overflow: hidden;
  border-radius: 999px;
  background: rgb(16 20 38 / .12);
}

.aurora-progress > span {
  display: block;
  height: 100%;
  width: 62%;
  border-radius: inherit;
  background: #4338ca;
}
```

## 11. Navigation / tabs

Use Aurora at the page/chrome level. The active item gets an explicit label, fill, underline, border, or icon treatment.

Desktop anatomy:

`navigation shell → brand → primary links → active state → utility actions`

Mobile anatomy:

`compact shell → primary destinations → active state → overflow/secondary actions`

Never make active navigation depend only on which gradient happens to be brightest.

## 12. Dialog / sheet

Keep the overlay and content stable:

```text
page Aurora
→ scrim
→ dialog/sheet surface
→ title
→ content
→ actions
```

The scrim should reduce background distraction. The dialog surface should preserve readable content and clear focus behavior.

## 13. Badge / chip / status

Aurora can supply decorative context, but the semantic state is carried independently.

```text
status = semantic color + label/icon + optional decorative glow
```

For example, “Synced” should remain understandable when all Aurora decoration is disabled.

## 14. Alert / banner / toast

Use an explicit semantic surface with role-appropriate color and iconography. A background glow can reinforce importance but should never be the message.

For transient feedback, ensure that accessible announcements and dismissal/focus behavior come from the interaction system rather than animation.

## 15. Lists / media rows

Use Aurora to emphasize a section or one featured row, not every row.

A useful pattern is:

`section Aurora → stable list surface → conventional row states`

This preserves scanability for repeated content.

## 16. Table / data grid

Default to a stable surface with no animated local Aurora.

Required cues include:
- header hierarchy
- row/column alignment
- selected row
- sort direction
- loading state
- empty state
- error state

Aurora may remain in the outer page background when it does not reduce readability.

## 17. Skeleton / loading

Skeletons should use a stable neutral placeholder. A slow ambient shimmer may be used only when consistent with the broader motion contract, but Aurora glow must not be confused with progress.

## 18. Empty state

Empty states are a good place for a static Aurora halo because the content volume is low. Use a clear heading, explanation, and primary action. The decorative field remains subordinate to the message.

## 19. State matrix

| State | Visual requirement | Aurora role |
|---|---|---|
| Default | Stable fill/border | none or ambient support |
| Hover | Clear interactive change | optional slight glow |
| Pressed | Persistent tactile/state change | decorative only |
| Focus-visible | Solid high-contrast ring | never sufficient alone |
| Selected | Fill/border/icon/label | optional emphasis |
| Disabled | Readable but reduced emphasis | remove most glow |
| Loading | Spinner/progress/skeleton | no pulse-only cue |
| Error | Error color + text/icon | no red glow-only cue |
| Success | Success color + text/icon | no green glow-only cue |

## 20. Opacity rule
Aurora opacity belongs to decorative light only. Keep important surfaces stable, normally around 0.92 or higher when using light translucent cards; keep text opaque; avoid low-opacity white text over changing backgrounds.

## 21. Motion rule
Default motion should be slow and ambient. Use only transform/opacity where possible.

```css
@media (prefers-reduced-motion: reduce) {
  .aurora-page::before {
    animation: none !important;
    filter: none;
  }
}
```

A static gradient is the canonical reduced-motion fallback.

## 22. Responsive rule
On narrow screens:
- reduce the number of light sources before reducing usable content space
- shrink the glow area before shrinking controls
- reduce blur before introducing expensive effects
- freeze or remove motion on constrained devices
- keep content order and hit targets unchanged

## 23. Fallback ladder

```text
Aurora animated
↓
Aurora static
↓
Simplified gradient
↓
Solid ground
```

Every step must preserve page structure, semantic meaning, states, focus, and interactions.
