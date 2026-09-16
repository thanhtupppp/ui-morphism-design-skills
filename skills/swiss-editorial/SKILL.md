---
name: swiss-editorial
description: Create typography-led editorial interfaces with an asymmetric grid, strong rules, restrained color, and readable long-form content. Use for journals, research libraries, cultural sites, and editorial portfolios.
---

# Swiss Editorial

## When to choose it

Use this style when headlines, essays, project narratives, and publication metadata carry the experience. Its identity comes from asymmetric typographic hierarchy and a disciplined reading grid, rather than Flat Design's general-purpose component system or Neobrutalism's hard shadows and exaggerated boundaries.

For operational tables or complex transactional forms, prefer Flat Design or Material Design. Preserve an existing brand's type family rather than importing a decorative font solely to imitate print.

## Visual system

- Opaque paper/ink surfaces, one vermilion accent, zero blur and zero shadow.
- Large, short headlines; readable sentence-case body copy; compact numbered metadata.
- A lead-story column with a smaller index column on wide screens; one continuous reading order on compact screens.
- Horizontal rules separate articles. Avoid boxing every paragraph into a card.
- Use whitespace and weight before increasing font size. Headlines may wrap; body measure stays near 60 characters.

Read [components.md](components.md) for recipes, [platforms.md](platforms.md) for target mappings, and the example for each requested renderer. `example.css` is the canonical web token set; `example.tsx` demonstrates working search, filters, inline reading, and local bookmarks.

## Accessibility and responsive behavior

Keep source order equal to reading order; never use CSS ordering to simulate a magazine spread. Use persistent field labels, real buttons, visible focus, and text plus semantic state for filters and bookmarks. Keep all controls at least 48px high. At compact widths, stack the lead and index; long titles and enlarged text must wrap without fixed-height clipping.

## Performance and fallback

Required: readable type, opaque surfaces, native controls, and semantic states. Preferred: asymmetric grid. Optional: custom fonts and the decorative index numeral. Fallback: system sans-serif, a single column, and standard bordered controls. No images, third-party font requests, animation, blur, or shadow are needed by the seed. Removing decoration must retain content, order, selection, and focus.

## Anti-patterns

- Tiny uppercase text used for essential metadata.
- Huge headlines that push the primary task beyond several screens.
- Editorial asymmetry implemented by changing keyboard or screen-reader order.
- Low-contrast gray text justified as a print aesthetic.
- A red accent used as the only marker of selection or an error.
- Fake article links, nonfunctional search fields, and decorative bookmark buttons.

See [verification.md](verification.md) for the actual checks and remaining platform validation.
