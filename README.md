# UI Morphism Design Intelligence

This repository is a reusable frontend design skill for selecting and implementing UI morphism styles in production products across web and application renderers.

## Current contract

Version `1.9.0` supports eleven visual styles with semantic-first cross-platform implementation, auditable agent output, explicit platform capability negotiation, semantic, accessibility, and structured component parity validation, React Native implementation seeds, ChatGPT Skill discovery metadata, release-grade package validation, deterministic routing evals, quality thresholds, and baseline regression gates. It adds **Swiss Editorial** for journals, research libraries, and typography-led portfolios, including an interactive React preview and Flutter and React Native seeds. `SKILL.md` is the source of truth; `skill.json` declares the supported styles, platforms, workflow, and contract references.

## Try the interactive examples

![Swiss Editorial journal preview](assets/swiss-editorial-preview.png)

Use Node.js 22.12+ or 24+ and npm. From the repository root:

```bash
npm ci
npm run dev
```

Open the local URL printed by Vite. The root preview opens **Aurora UI** and imports `skills/aurora-ui/example.tsx` directly. Its controls exercise the primary action, workflow selection, responsive layout, forced-colors fallback, and full/off effect modes. Use the Style selector to switch to Swiss Editorial, whose filters, search, inline reading, and save/unsave actions also work locally. Both examples require no account, backend, remote fonts, or API keys.

```bash
npm run build
npm run preview
```

The production build is written to `dist/`. For Aurora UI, start with its [skill](skills/aurora-ui/SKILL.md), [component recipes](skills/aurora-ui/components.md), [platform mappings](skills/aurora-ui/platforms.md), and [verification record](skills/aurora-ui/verification.md). For Swiss Editorial, use its [skill](skills/swiss-editorial/SKILL.md), [component recipes](skills/swiss-editorial/components.md), [platform mappings](skills/swiss-editorial/platforms.md), and [verification record](skills/swiss-editorial/verification.md).

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

`references/semantic-parity.md` defines cross-renderer invariants. `scripts/validate-semantic-parity.mjs` checks all eleven styles for canonical CSS token definition/consumption, semantic interactive primitives, state coverage, responsive intent, target-size guidance, fallback behavior, accessibility parity references, and verification records. Renderer-specific visual treatment may differ; semantic anatomy and state meaning may not silently diverge.

`references/accessibility-parity.md` defines cross-renderer accessibility invariants. `scripts/validate-accessibility-parity.mjs` checks focus visibility, forced-colors handling, reduced motion, accessible naming, native controls, target-size guidance, explicit state semantics, and fallback behavior across all eleven styles.

## Structured component parity

`references/component-parity.json` is the normalized machine-readable contract for the primary interactive component. It defines the baseline role, accessible-name requirement, default/pressed/disabled states, responsive intent, target-size policy, and deterministic fallback requirement, plus renderer-specific evidence signals.

`references/component-parity.md` documents the normalization model, and `scripts/validate-component-parity.mjs` validates its schema and checks source evidence across all eleven styles × four renderers. Missing renderers and malformed evidence rules fail validation. Source checks remain heuristic and do not replace runtime interaction or accessibility testing.

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
- `references/component-parity.json` — machine-readable normalized primary-action parity contract.
- `references/component-parity.md` — structured component parity rules.
- `references/platform-contract.md` — framework-agnostic implementation and fallback rules.
- `references/platform-matrix.md` — renderer capability matrix and capability negotiation.
- `references/platform-implementation-guide.md` — semantic tokens, capability negotiation, and verification workflow.
- `references/quality-gates.md` — production-readiness checks for semantics, responsiveness, motion/fallback, target size, effect budget, and cross-platform equivalence.
- `references/react-native-adapter.md` — canonical React Native role/state/token/responsive/accessibility/fallback mapping.
- `references/token-convention.md` — canonical token namespace, accessibility token rules, and theme override behavior.
- `references/semantic-parity.md` — cross-renderer semantic invariants.
- `references/accessibility-parity.md` — cross-renderer accessibility invariants.

## Supported platforms

HTML/CSS, React, Flutter, React Native, and other renderers through the adapter contract.

## Validation and evals

Run all repository validators locally:

```bash
node scripts/validate-repo.mjs
node scripts/validate-quality-gates.mjs
node scripts/validate-semantic-parity.mjs
node scripts/validate-accessibility-parity.mjs
node scripts/validate-component-parity.mjs
node --test scripts/validate-component-parity.test.mjs
```

The dependency-free validators check documentation and source contracts. They do not establish runtime correctness. The interactive example also has TypeScript/build checks and browser behavior/accessibility tests:

```bash
npm run build
npx playwright install chromium
npm test
```

Validate the ChatGPT Skill package and build its deterministic release artifacts:

```bash
python3 scripts/validate-skill-package.py .
python3 scripts/package-skill.py --root . --output release/skill.zip --json
python3 scripts/verify-release.py release
```

Run routing, threshold, baseline, and semantic-parity evals:

```bash
python3 scripts/run-evals.py --output eval-report.json
```

The eval report preserves the 1.2.0 schema and includes confusion-matrix metrics, per-style precision/recall/F1, threshold failures, and baseline regressions for CI diagnostics. Swiss Editorial routing fixtures and thresholds are included in the eleven-style baseline.

GitHub Actions runs the eleven-style matrix, all validators, preview build and browser suite, regression suites, release verification, and eval gates on pushes and pull requests targeting `main`.

## Supported styles

Skeuomorphism, Flat Design, Neumorphism, Material Design, Glassmorphism, Claymorphism, Liquid Glass, Aurora UI, Bento UI, Neobrutalism, and Swiss Editorial.

## Design principle

Choose one primary visual language and at most one supporting style. Treat Bento as a layout system and Aurora as an atmospheric accent unless the product specifically calls for broader use. Translate semantic intent across renderers; never make blur, texture, glow, shadow, transparency, or animation the only source of meaning. Advanced effects must have a deterministic fallback, and native/standard interaction primitives should be preferred over custom painted controls.
