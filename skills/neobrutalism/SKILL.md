# Neobrutalism

## Purpose
Neobrutalism is a **high-contrast visual language built from blunt geometry, bold type, saturated fills, strong borders, and hard unblurred offsets**. The design communicates directly: structure is visible, interaction is physical-looking without trying to look realistic, and hierarchy is established through scale, contrast, weight, and position.

It is a complete component language, unlike Bento UI, which is primarily composition. Neobrutalism may be used inside a Bento layout, but the two decisions should remain separate.

## How to recognize it
A beginner should see:

```text
strong border + flat fill + hard offset shadow + bold typography + direct state change
```

The visual depth is discrete rather than soft. There is no blur, glass transparency, realistic material texture, or paired soft light/shadow system.

## Visual DNA
- Flat or minimally shaded surfaces.
- One strong border vocabulary, commonly 2–4px.
- Hard offset shadow with zero blur.
- Bold, often oversized typography used as layout structure.
- Saturated accent blocks balanced by a calmer ground.
- Small or zero radius unless the product defines a deliberate dialect.
- Optional small rotations only for secondary decoration; never for text, fields, errors, or critical controls.
- High visual contrast between primary action, supporting content, and background.

## Material and depth model
Neobrutalism has **graphic depth**, not physical depth:

1. Ground establishes the canvas.
2. Border defines the object boundary.
3. Flat fill establishes the object plane.
4. Hard offset creates a deliberate graphic displacement.
5. Typography/icons provide hierarchy.
6. Interaction state changes border, offset, position, fill, or a clear indicator.

Do not add blur to the shadow. A blurred shadow moves the style toward soft-material systems such as Claymorphism or Neumorphism.

## Distinguish from related styles
- **Flat Design:** both are flat, but Neobrutalism intentionally amplifies border weight, type scale, hard offsets, and expressive contrast.
- **Bento:** Bento controls composition; Neobrutalism controls visual language. They can be combined.
- **Skeuomorphism:** Skeuomorphism simulates physical materials; Neobrutalism uses deliberately artificial graphic construction.
- **Neumorphism:** Neumorphism uses soft paired shadows; Neobrutalism uses hard edges and zero-blur offsets.
- **Claymorphism:** Clay uses inflated rounded volume and soft shading; Neobrutalism prefers crisp geometry.

## Use when
- Expressive brands, creator products, campaigns, portfolios, indie products, event/launch pages, playful tools, experimental dashboards.
- The interface benefits from an intentionally constructed, hand-built, poster-like personality.

## Avoid when
- Dense regulated workflows where heavy borders and oversized type reduce information density.
- Long reading surfaces where expressive tiles compete with typography.
- Interfaces where rotation, large display text, or saturated fills conflict with localization or scanning.
- Products that require a very quiet, conservative visual tone.

## Token contract
Define geometry before styling:

```css
:root {
  --um-neobrutalism-bg: #fef6e4;
  --um-neobrutalism-surface: #ffffff;
  --um-neobrutalism-ink: #0a0a0a;
  --um-neobrutalism-border: #0a0a0a;
  --um-neobrutalism-accent-1: #ffdc58;
  --um-neobrutalism-accent-2: #67e8f9;
  --um-neobrutalism-accent-3: #fb7185;
  --um-neobrutalism-focus: #155e75;
  --um-neobrutalism-border-w: 2px;
  --um-neobrutalism-shadow-1: 4px 4px 0 var(--um-neobrutalism-border);
  --um-neobrutalism-shadow-2: 8px 8px 0 var(--um-neobrutalism-border);
  --um-neobrutalism-radius: 0px;
  --um-neobrutalism-target-min: 44px;
}
```

Tokenize accent roles rather than sprinkling arbitrary colors. A screen should usually have one dominant accent plus at most one or two supporting accents.

## Component strategy
### Button
Use a solid fill, strong border, and hard offset. Pressed state may translate the visual treatment toward its shadow. The actual interactive bounds remain stable.

### Icon button
Use a square/near-square target. Do not make decorative rotation the only active-state signal. Give icon-only controls accessible names.

### Card / panel
Use a strong border and optional offset shadow. Do not shadow every nested element. A card should have one clear job and an obvious content hierarchy.

### Input / form
Fields stay conventional. Label → field → helper/error. Use border/fill/icon/text for invalid state; never rely on a red background alone. Avoid rotated fields and intentionally awkward typing geometry.

### Checkbox / radio / switch
Use the host platform's semantic control with a Neobrutalist visual wrapper. Selection should have at least one non-color cue such as checkmark, thumb position, outline, or icon.

### Navigation / tabs
Active state may use fill swap, bold type, hard underline/block, or small offset. Do not make every navigation item visually loud; reserve the strongest treatment for current location and primary action.

### Badge / chip
Good place for expressive accent fills. Keep text legible and avoid so many accent chips that the page becomes visually noisy.

### Alert / banner
Use strong border + semantic icon + text. Critical alerts may use a stronger accent, but the message and icon carry meaning independently of color.

### Modal / dialog
Maintain clear overlay separation and focus management. The shell can use the same border/offset language, but the scrim should remain functional and the dialog must not visually jump when focus changes.

### Table / data grid
Use Neobrutalist typography and borders sparingly. For dense tables, reduce border weight and use Flat/Material-like row structure where necessary. Do not turn every cell into a floating hard-shadow card.

## State model
Every interactive component should define:

```text
default
→ hover (pointer-capable)
→ focus-visible
→ pressed
→ selected/checked
→ disabled
```

Recommended visual mapping:

| State | Primary cue |
|---|---|
| Default | Full border + normal offset |
| Hover | Small visual translation or offset reduction |
| Focus-visible | Distinct high-contrast outline + existing component boundary |
| Pressed | Larger translation toward the shadow, or shadow reduction |
| Selected | Fill/outline/icon change, not color alone |
| Disabled | Reduced emphasis + explicit disabled semantics; avoid unreadable low contrast |

Never use hover-only affordances for essential functionality.

## Typography
Typography is structural. Define heading, body, label, metadata, and button roles before choosing decorative display faces. Large display text may be expressive in hero areas, but controls and forms need stable line-height, wrapping, and localization behavior.

## Motion
Use brief `transform`/shadow-offset feedback for interaction. Good motion is immediate and short. Avoid shake loops, perpetual rotation, or random jitter. Respect reduced-motion preferences and keep state communication visible when motion is removed.

## Responsive behavior
At compact widths:
- remove decorative rotation first;
- reduce display type scale before reducing usable body/control text below readability targets;
- collapse multi-column compositions into natural document flow;
- reduce shadow offsets when overflow/clipping becomes a problem;
- preserve minimum interactive target size;
- allow buttons, cards, alerts, and labels to grow vertically.

Do not preserve a desktop collage at the expense of reading order.

## Accessibility contract
- Contrast must be tested for every accent/fill/text combination actually used.
- Focus must be stronger and distinguishable from the component's heavy border.
- Selection, error, and status must have text/icon/shape cues in addition to color.
- Forced-colors/high-contrast modes must retain semantic boundaries.
- Large text and localization must be allowed to expand components.
- Keyboard order follows DOM/widget order, not decorative placement.
- Rotation must never change the interpretation of text or control orientation.

## Performance
Hard borders and zero-blur shadows are comparatively inexpensive. The main risks are oversized shadows causing overflow, animated transforms on many elements, and large images inside expressive cards. Prefer compositor-friendly transforms for short interaction feedback and keep decorative layers limited.

## Fallback
When expressive styling is unavailable or undesirable, reduce in this order:

```text
hard shadow → border emphasis → accent fill → ordinary solid surface
```

Never remove semantics, labels, focus, or status cues as part of the visual fallback.

## Recognition test
The implementation is recognizably Neobrutalist when the designer can remove every rotation and still see:

```text
bold type + strong border + flat fill + hard offset + direct state change
```

If removing the border and hard offset leaves a soft, translucent, or physically shaded UI, the implementation has drifted to another style.

## Anti-patterns
- Shadow-only boundaries.
- Blurred shadows.
- Rotated labels, inputs, or error messages.
- Every element receiving a different accent color.
- Making accessibility focus look identical to ordinary borders.
- Fixed-height cards that clip localized text.
- Treating chaos as the design system.
