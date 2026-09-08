# UI Morphism Design Skill

## Mission

Select and apply a UI morphism style to a real frontend without sacrificing clarity, accessibility, responsive behavior, performance, or maintainability.

## Required input

- Product type and primary user.
- Primary tasks and interaction density.
- Data density: low, medium, or high.
- Device and environment.
- Brand personality and content tone.
- Frontend stack and browser support.
- Accessibility, performance, localization, and dark-mode constraints.

## Decision workflow

1. Parse the brief and identify product, audience, context, density, device, and constraints.
2. Query `domains/product.csv` for candidate styles.
3. Apply `domains/reasoning.csv` from highest priority to lowest priority.
4. Select exactly one primary style and at most one supporting style.
5. Read the selected style's `SKILL.md` and implementation notes.
6. Generate semantic design tokens and map them to component states.
7. Build mobile-first and preserve semantic DOM order.
8. Audit accessibility, performance, responsive behavior, and anti-patterns.

## Hard rules

- Visual style must never be the only carrier of meaning.
- Text and essential controls need a stable surface when transparency or gradients reduce contrast.
- Every interactive control needs visible keyboard focus and a non-hover interaction state.
- Support `prefers-reduced-motion`.
- Provide fallbacks for blur, gradient, shadow, and unsupported CSS features.
- Do not use heavy blur over large areas without a performance test.
- Keep CSS effects in tokens and utility classes.
- Preserve semantic HTML, accessible names, labels, error association, and logical focus order.

## Output contract

Return primary style and rationale, supporting style and boundaries, risks, token table, component/state plan, responsive and motion behavior, implementation plan, and audit checklist.
