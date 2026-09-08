# UI Morphism Design Skill

## Mission

Select and apply a UI morphism style to a real frontend without sacrificing clarity, accessibility, responsive behavior, performance, or maintainability.

## Research-informed workflow

Use the same evidence-oriented sequence for every project:

1. Parse the brief and identify product, audience, context, density, device, and constraints.
2. Read `references/comparison-matrix.md` for visual signature, fit, risk, depth model, and cost.
3. Query `domains/product.csv` for candidate styles.
4. Apply `domains/reasoning.csv` and `domains/hybrid-rules.csv` from highest priority to lowest priority.
5. Select exactly one primary style and at most one supporting style.
6. Read the selected style's `SKILL.md` and `domains/implementation.md`.
7. Generate namespaced semantic tokens using `references/token-convention.md`.
8. Map tokens to component states: default, hover, focus, active, disabled, loading, error, empty, and success.
9. Build mobile-first and preserve semantic DOM order.
10. Audit contrast, target size, forced-colors behavior, reduced motion, fallback rendering, and performance.

## Hard rules

- Visual style must never be the only carrier of meaning.
- Text and essential controls need a stable surface when transparency or gradients reduce contrast.
- Every interactive control needs visible keyboard focus and a non-hover interaction state.
- Support `prefers-reduced-motion` and a fallback for advanced transparency when required.
- Do not use heavy blur over large areas without a performance test.
- Keep CSS effects in namespaced tokens and utility classes.
- Preserve semantic HTML, accessible names, labels, error association, and logical focus order.
- Do not mix two styles on the same control vocabulary unless the hybrid rule explicitly allows it.

## Output contract

Return the primary style and rationale, supporting style and boundary, risk profile, namespaced token table, component/state plan, responsive and motion behavior, implementation plan, and audit checklist.
