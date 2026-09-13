# UI Morphism Design Intelligence

This repository is a reusable frontend design skill for selecting and implementing UI morphism styles in production products across web and application renderers.

## Current contract

Version `1.5.1` supports ten visual styles with semantic-first cross-platform implementation, auditable agent output, explicit platform capability negotiation, and React Native implementation seeds. `SKILL.md` is the source of truth; `skill.json` declares the supported styles, platforms, workflow, and contract references.

## Code-first, cross-platform usage

Every style directory contains:

- `SKILL.md`: when to use, visual system, risks, accessibility, and anti-patterns.
- `components.md`: component-level recipes for buttons, cards, inputs, navigation, states, opacity, blur, shadows, radius, borders, and responsive behavior.
- `platforms.md`: how the same visual intent maps to HTML/CSS, React, Flutter, React Native, and other renderers.
- `example.css`: a runnable web/CSS starter.
- `example.tsx`: a runnable React/semantic HTML starter.
- `example.flutter.dart`: a Flutter implementation seed using native/theme primitives.
- `example.native.tsx`: a React Native implementation seed using native interaction primitives and deterministic fallbacks.

An agent should read all style files above before implementing a selected style. Do not output only generic visual advice; use the concrete recipes and platform mappings, then adapt tokens and primitives to the project.

## Agent output contract

`references/component-code-contract.md` requires an auditable sequence:

`decision record -> semantic token record -> component recipes -> platform mappings -> responsive/accessibility rules -> fallback rule -> verification record`

For generated or modified examples, record what was verified instead of treating the presence of visual code as proof of correctness.

## Platform capability negotiation

`references/platform-matrix.md` is the capability decision table for HTML/CSS, React, Flutter, and React Native. It distinguishes `Native`, `Adapt`, and `Fallback` behavior and separates `Required`, `Preferred`, and `Optional` effects.

The deterministic degradation path is:

`full effect -> reduced effect -> opaque/static effect -> simpler native surface`

Unsupported effects must not change content priority, semantic state, accessibility, responsive behavior, or interaction target size.

## React Native examples

Every style includes `example.native.tsx`. These seeds preserve semantic roles and state through `Pressable` or other native primitives, respond to available width, target at least 48px for primary tappable controls, and document what survives when decorative effects are removed.

## Core contracts

- `references/comparison-matrix.md` — style selection and depth/cost guidance.
- `references/component-code-contract.md` — required component/state output and auditable agent workflow.
- `references/platform-contract.md` — framework-agnostic implementation and fallback rules.
- `references/platform-matrix.md` — renderer capability matrix and capability negotiation.
- `references/platform-implementation-guide.md` — semantic tokens, capability negotiation, and verification workflow.
- `references/quality-gates.md` — production-readiness checks for semantics, responsiveness, motion/fallback, target size, effect budget, and cross-platform equivalence.
- `references/react-native-adapter.md` — canonical React Native role/state/token/responsive/accessibility/fallback mapping.

## Supported platforms

HTML/CSS, React, Flutter, React Native, and other renderers through the adapter contract.

## Validation

Run the repository validators locally:

```bash
node scripts/validate-repo.mjs
node scripts/validate-quality-gates.mjs
```

GitHub Actions runs both validators on pushes and pull requests targeting `main`.

## Supported styles

Skeuomorphism, Flat Design, Neumorphism, Material Design, Glassmorphism, Claymorphism, Liquid Glass, Aurora UI, Bento UI, and Neobrutalism.

## Design principle

Choose one primary visual language and at most one supporting style. Treat Bento as a layout system and Aurora as an atmospheric accent unless the product specifically calls for broader use. Translate semantic intent across renderers; never make blur, texture, glow, shadow, transparency, or animation the only source of meaning. Advanced effects must have a deterministic fallback, and native/standard interaction primitives should be preferred over custom painted controls.
