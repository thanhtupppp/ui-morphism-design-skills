# UI Morphism Design Intelligence

This repository is a reusable frontend design skill for selecting and implementing UI morphism styles in production products across web and application renderers.

## Current contract

Version `1.9.0` supports ten visual styles with semantic-first cross-platform implementation, auditable agent output, explicit platform capability negotiation, a canonical token namespace/theme contract, semantic parity validation, accessibility parity validation, React Native implementation seeds, ChatGPT Skill discovery metadata, release-grade package validation, deterministic routing evals, quality thresholds, and baseline regression gates. `SKILL.md` is the source of truth; `skill.json` declares the supported styles, platforms, workflow, and contract references.

## Code-first, cross-platform usage

Every style directory contains:

- `SKILL.md`: when to use, visual system, risks, accessibility, and anti-patterns.
- `components.md`: component-level recipes for buttons, cards, inputs, navigation, states, opacity, blur, shadows, radius, borders, and responsive behavior.
- `platforms.md`: how the same visual intent maps to HTML/CSS, React, Flutter, React Native, and other renderers.
- `example.css`: a runnable web/CSS starter with canonical semantic tokens.
- `example.tsx`: a runnable React/semantic HTML starter.
- `example.flutter.dart`: a Flutter implementation seed using native/theme primitives.
- `example.native.tsx`: a React Native implementation seed using native interaction primitives and deterministic fallbacks.

An agent should read all style files above before implementing a selected style. Do not output only generic visual advice; use the concrete recipes and platform mappings, then adapt tokens and primitives to the project.

## Agent output contract

`references/component-code-contract.md` requires an auditable sequence:

`decision record -> semantic token record -> component recipes -> platform mappings -> responsive/accessibility rules -> fallback rule -> verification record`

For generated or modified examples, record what was verified instead of treating the presence of visual code as proof of correctness.

## Semantic token and theme contract

`references/token-convention.md` is the canonical naming and theme contract. Reusable tokens use the grammar:

`--um-<style>-<group>[-<variant>]`

Use full style names rather than short aliases, keep style tokens separate from semantic roles, expose opaque fallback surfaces for translucent styles, and provide focus fallbacks that do not depend only on `box-shadow`. Explicit `[data-theme="dark"]` and `[data-theme="light"]` choices must override system preference where theme switching is implemented.

## Semantic parity

`references/semantic-parity.md` defines cross-platform equivalence for semantic anatomy, state meaning, responsive intent, accessibility behavior, minimum target size, and deterministic fallback. Renderer-specific visual differences are allowed when those invariants remain intact.

## Validation and evals

Run the release validator:

```bash
python3 scripts/validate-skill-package.py .
```

Run routing, threshold, baseline, and semantic-parity evals:

```bash
python3 scripts/run-evals.py --output eval-report.json
```

The eval report preserves the 1.2.0 schema and includes confusion-matrix metrics, per-style precision/recall/F1, threshold failures, and baseline regressions for CI diagnostics.
