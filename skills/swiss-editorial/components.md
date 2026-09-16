# Swiss Editorial component recipes

## Semantic token record

All shared CSS tokens use `--um-swiss-editorial-<group>[-<variant>]`. The executable values live in `example.css`.

| Role | Token suffix | Light / dark |
|---|---|---|
| Page and panel | `bg`, `surface` | warm paper / charcoal |
| Text and supporting copy | `ink`, `ink-muted` | dark ink / light paper |
| Action and selected mark | `accent`, `accent-ink` | deep vermilion + white / pale coral + dark ink |
| Interactive boundary | `border-strong` | ink / paper |
| Keyboard focus | `focus` | blue / light blue |
| Control geometry | `target-min`, `radius` | 48px, 0 |
| Material effects | `shadow`, `blur` | none, 0px |

Text opacity and surface opacity are 1. Use 8/16/24/32px spacing and a system sans-serif family. Explicit document light/dark theme overrides system preference. Keep theme switching in the host application, not in every card.

## Button and selection states

| State | Recipe | Semantic behavior |
|---|---|---|
| Default | Opaque surface, 1px strong border, 48px minimum target | Native button with a verb |
| Hover | Underline the label, preserve contrast | Pointer enhancement only |
| Active / pressed | 2px inset outline | Immediate native activation |
| Selected | Accent fill, strong border, visible check mark | `aria-pressed`; native selected state |
| Disabled | Dashed border and explicit unavailable label | Native disabled attribute/state |
| Loading | Keep label and target; replace label with “Loading…” | Busy state plus disabled action; optional host async integration |
| Focus-visible | 3px outline with 3px offset | Independent of hover, fill, and shadow |

The example uses synchronous local state and does not simulate a network request. Loading/error handling belongs to the host when a backend is added. Bookmark state lasts for the mounted instance; storage is deliberately not implied.

## Card / article panel

Use an `article` with a metadata line, heading, summary, reading disclosure, and bookmark button. A horizontal rule separates entries; the entire panel is not clickable. Numbering is decorative when the same order is already conveyed by the list. Disclosure uses `aria-expanded` and `aria-controls`; keep focus on its trigger. Native seeds keep the body visible to reduce platform-specific disclosure mechanics.

## Input / form field

Search uses a visible label, 48px minimum height, an opaque surface, and a strong border. Search applies immediately to titles and summaries. Combine it with category filtering; show an explicit empty message and a reset action. Do not replace the label with a placeholder. A host validation error needs explanatory text and a programmatic association, not only a red outline.

## Navigation and toolbar

The web navigation uses real in-page destinations. Category choices are toggle buttons in a labelled group, not ARIA tabs: they filter a shared result list. Keep an “All” option and announce the result count politely. A bookmark changes its visible label to “Saved” and its pressed/selected state. Wrap controls instead of truncating them.

## Responsive and accessibility rules

- Compact (375px): one column, wrapping masthead and filter row, 16px page gutters.
- Medium (768px): generous gutters, lead story still above the article index.
- Expanded (1024/1440px): two-column lead/index layout with unchanged source order.
- At 200% text size, use content height and a single-column fallback as space requires.
- RTL: use logical spacing and inherited text direction; do not reverse source order.
- Forced colors: system Canvas/CanvasText/ButtonFace/ButtonText and Highlight outline; preserve selection check marks and boundary styles.
- Reduced motion: no animated decoration; transitions are disabled in the scoped root.

## Effect budget and verification

Zero blur, zero shadows, zero remote assets. The optional large issue numeral is hidden from assistive technology. All interactions remain useful with decoration removed. Browser checks and native limitations are recorded in [verification.md](verification.md).
