# UI Morphism Design Intelligence

This repository is a reusable frontend design skill for selecting and implementing UI morphism styles in production products.

## Reference-informed improvements

The repository now includes an original comparison matrix, token namespace convention, hybrid compatibility rules, and stack implementation guidance. The organization is informed by the public documentation structure of [`Shubham7995/ui-morphism`](https://github.com/Shubham7995/ui-morphism/tree/main/docs), especially its comparison matrix, per-style documents, glossary, contrast checker, and link validation approach.

## Supported styles

Skeuomorphism, Flat Design, Neumorphism, Material Design, Glassmorphism, Claymorphism, Liquid Glass / Liquid UI, Aurora UI, Bento UI, and Neobrutalism.

## Agent usage

1. Read `SKILL.md`.
2. Read `references/comparison-matrix.md`.
3. Describe product, users, context, density, device, brand personality, stack, and constraints.
4. Choose exactly one primary style and at most one supporting style using `domains/product.csv`, `domains/reasoning.csv`, and `domains/hybrid-rules.csv`.
5. Read the selected style file under `skills/`.
6. Generate tokens using `references/token-convention.md` and `templates/design-tokens.css`.
7. Plan components, implement, and run `references/review-checklist.md`.
