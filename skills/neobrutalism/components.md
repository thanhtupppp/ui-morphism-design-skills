# Neobrutalism Component Recipes

## Core tokens

```css
:root {
  --um-neobrutalism-bg: #fef6e4;
  --um-neobrutalism-surface-1: #ffffff;
  --um-neobrutalism-ink: #0a0a0a;
  --um-neobrutalism-border: #0a0a0a;
  --um-neobrutalism-accent-1: #ffdc58;
  --um-neobrutalism-accent-2: #67e8f9;
  --um-neobrutalism-accent-3: #fb7185;
  --um-neobrutalism-focus: #155e75;
  --um-neobrutalism-border-width: 2px;
  --um-neobrutalism-shadow-1: 4px 4px 0 var(--um-neobrutalism-border);
  --um-neobrutalism-shadow-2: 8px 8px 0 var(--um-neobrutalism-border);
  --um-neobrutalism-radius: 0px;
  --um-neobrutalism-target-min: 44px;
}
```

Core rule: semantic element → size/spacing → strong border → flat fill → hard zero-blur offset → typography/icon → explicit state cue → optional motion.

## Button

```css
.neo-button {
  min-height:var(--um-neobrutalism-target-min);
  padding:10px 16px;
  border:var(--um-neobrutalism-border-width) solid var(--um-neobrutalism-border);
  border-radius:var(--um-neobrutalism-radius);
  background:var(--um-neobrutalism-accent-1);
  color:var(--um-neobrutalism-ink);
  box-shadow:var(--um-neobrutalism-shadow-1);
  font-weight:800;
}
.neo-button:focus-visible { outline:3px solid var(--um-neobrutalism-focus); outline-offset:4px; }
```

Press feedback may reduce offset or translate the visual shell, but hit bounds and semantics stay stable.

## State matrix

| State | Required cue | Visual treatment |
|---|---|---|
| Default | Stable label and strong boundary | Flat accent fill and hard offset |
| Hover | Clear contrast or underline change | Optional offset change |
| Active / pressed | Pressed semantics where applicable | Reduced offset or short translation |
| Selected | Check, icon, label, or persistent inner mark | Persistent accent treatment |
| Focus-visible | Outline distinct from the component border | No rotation |
| Disabled | Disabled semantics and readable reduced emphasis | Muted fill and no motion |
| Loading | Busy semantics plus progress text, spinner, or skeleton | Static shell |

## Components

Cards use strong boundaries and limited offsets. Inputs retain conventional label/helper/error anatomy. Selection controls use marks/thumb position/icons in addition to saturated fills. Active navigation uses persistent indicators. Dialogs keep semantic modal behavior. Dense tables reduce border/shadow intensity rather than turning every cell into a card.

## Accessibility

Focus must be visually distinct from the ordinary heavy border. Color is not the only state channel. Large text/localization may expand controls. Decorative rotation never changes text/control interpretation or focus order.

## Responsive matrix

| Layout | Treatment |
|---|---|
| Compact, below 768px | Reduce offsets and decorative rotation; stack content and preserve target size. |
| Medium, 768–1023px | Use strong borders with moderate offsets on focal cards and controls. |
| Expanded, 1024px and above | Keep repeated grid items visually disciplined rather than increasing every offset. |

## Fallback and performance

```text
hard offset
→ strong border + accent fill
→ strong border + ordinary solid surface
```

Hard shadows are inexpensive, but oversized offsets can overflow; limit animated transforms and remove decorative rotation/offset before compromising layout or target geometry.

## Anti-patterns

- Blurred/soft shadows.
- Shadow-only boundaries.
- Rotated fields or validation text.
- Different arbitrary accent on every component.
- Focus treatment indistinguishable from ordinary borders.
- Fixed-height cards that clip localization.
