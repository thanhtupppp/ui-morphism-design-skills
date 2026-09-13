# Claymorphism

## Purpose
Claymorphism uses opaque, inflated, rounded objects with soft highlights and hue-matched shadows to communicate friendliness, warmth, and approachable physicality.

## How to recognize it
A Claymorphic object looks like a soft molded piece of colored clay: rounded, opaque, inflated, and gently shaded. The body itself has color and volume; it is not transparent and does not depend on a photographic texture.

## Use when
- The product is educational, playful, onboarding-focused, wellness-oriented, creative, or gamified.
- A hero object or featured module benefits from warmth and physicality.
- The interface has enough whitespace for large rounded objects.

## Avoid when
- The workflow is regulated, dense, data-heavy, or credibility-first.
- Every list item would become a large inflated object.
- Pastel colors cannot maintain text/focus contrast.
- Transparency or realistic material is the stronger product metaphor.

## Visual DNA
- Opaque pastel, candy, or brand-colored body.
- Large rounded or squircle geometry.
- One consistent light direction.
- Soft light inner highlight.
- Soft darker inner shade on the opposite side.
- Hue-matched outer shadow rather than generic black blur.
- Crisp typography and conventional information structure above the decorative layer.

## Material hierarchy
1. Body color establishes the object.
2. Shape establishes the inflated silhouette.
3. Inner highlight/shade establishes curvature.
4. Outer shadow establishes separation from the page.
5. Content establishes meaning.
6. Explicit state styling establishes interaction.

Decorative volume must never replace semantic affordance.

## Component strategy
- Hero/feature card: strongest Clay expression.
- Primary CTA: smaller, clearer clay object.
- Icon button/badge/chip: use restrained clay treatment.
- Form controls: conventional opaque controls inside a clay shell when density or precision matters.
- Tables/data grids: Flat or Material surfaces.
- Empty states/illustrations: excellent place for expressive Clay shapes.

## Distinction from similar styles
- **Neumorphism:** shared-surface relief; Clay uses its own opaque colored body.
- **Glassmorphism:** translucent and backdrop-dependent; Clay is opaque.
- **Skeuomorphism:** realistic physical material and texture; Clay is stylized and simplified.
- **Flat Design:** hierarchy without physical volume; Clay intentionally adds soft volume around selected objects.

## State rules
- Default: stable inflated form.
- Hover: subtle lift/brightness, primarily for pointer devices.
- Pressed: tiny inward translation/scale and optional shadow compression.
- Focus: explicit high-contrast ring/border.
- Selected: visible indicator, icon, stronger fill, or textual cue in addition to depth.
- Disabled: semantic disabled treatment; reduce decoration without destroying legibility.
- Error: text/icon/border; never rely on pastel hue or shadow alone.

## Motion
Use short, soft feedback. Avoid perpetual bouncing, excessive spring overshoot, or decorative rotation. Reduced motion should collapse to instant or near-instant state changes.

## Responsive and performance
- Reduce shadow spread and decorative object size before reducing usable target size.
- Avoid fixed-height cards.
- Reduce effect density on small screens.
- Avoid large blur/shadow stacks across repeated list items.
- Lazy-load large decorative illustrations.

## Fallback behavior
When soft highlights, blur, complex shadows, or custom compositing are unavailable or too expensive, keep the Clay identity through opaque shape, color, spacing, and explicit borders/state cues. Fall back to a flatter rounded surface rather than removing semantic affordances. On constrained renderers, a simple filled rounded container is the required baseline.

## Accessibility checklist
- [ ] Body text and controls maintain required contrast.
- [ ] Focus is visible without relying on shadow.
- [ ] Selection/disabled/error states remain understandable in grayscale.
- [ ] Forced-colors/high-contrast mode exposes solid boundaries and semantic state.
- [ ] Text scaling and localization do not clip inside rounded shapes.
- [ ] Interactive semantics remain native/accessible.

## Anti-patterns
- Applying Clay to every component.
- Making all cards, buttons, and badges identical in radius and shadow.
- Tiny typography inside oversized shapes.
- Turning Clay transparent and calling it glass.
- Using neutral paired relief shadows until the UI becomes Neumorphic.
- Using decoration to communicate state without semantic labels/indicators.
