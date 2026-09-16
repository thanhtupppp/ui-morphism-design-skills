# Style Audit Matrix — v1.9 Stabilization

This matrix tracks the 10 supported styles across the 7 required files per style (70 files total).

## Status legend

- **PASS**: verified by current CI and/or manual review for the stated criterion.
- **FAIL**: confirmed defect that must be fixed before stabilization is complete.
- **REVIEW**: current CI is green, but the file still requires deeper manual audit for this criterion.
- **Overall = FAIL** when any criterion is FAIL; otherwise **REVIEW** until all criteria are manually closed; then **PASS**.

## Audit criteria

1. **Token namespace** — reusable tokens must follow `--um-<style>-<group>[-<variant>]`; no legacy aliases in reusable recipes.
2. **Semantic parity** — meaning, component anatomy, state semantics and responsive intent remain equivalent across CSS/React/Flutter/React Native.
3. **Accessibility** — names, focus, state, target size, large text/localization, reduced motion/effects and high-contrast behavior remain usable.
4. **Fallback** — visual effects can degrade deterministically without losing content, state or interaction meaning.
5. **Performance** — effects are bounded; expensive blur/shadow/animation work is optional/reducible; dense content remains efficient.

## 1. Aurora UI

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/aurora-ui/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Core guidance is sound; manual parity cross-check pending. |
| `skills/aurora-ui/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--aurora-*` tokens instead of `--um-aurora-ui-*`. |
| `skills/aurora-ui/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | CI passes; renderer guidance needs manual comparison with examples. |
| `skills/aurora-ui/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/aurora-ui/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/aurora-ui/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/aurora-ui/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 2. Bento UI

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/bento-ui/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Strong source-order and responsive hierarchy guidance. |
| `skills/bento-ui/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Namespace already conforms to `--um-bento-ui-*`; manual interaction audit pending. |
| `skills/bento-ui/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | CI passes; verify visual-order vs semantic-order mapping on all renderers. |
| `skills/bento-ui/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/bento-ui/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/bento-ui/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/bento-ui/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 3. Claymorphism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/claymorphism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Core guidance separates decorative volume from semantics. |
| `skills/claymorphism/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--clay-*` token namespace. |
| `skills/claymorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | CI passes; verify shadow reduction/fallback consistency manually. |
| `skills/claymorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/claymorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/claymorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/claymorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 4. Flat Design

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/flat-design/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | **FAIL** | Contains non-portable ChatGPT session citations and an unnecessary framework-version-pinned claim. |
| `skills/flat-design/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--flat-*` tokens and legacy theme token examples. |
| `skills/flat-design/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | CI passes; manually verify token mapping after namespace migration. |
| `skills/flat-design/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/flat-design/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/flat-design/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/flat-design/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 5. Glassmorphism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/glassmorphism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Opaque fallback sequence is documented correctly. |
| `skills/glassmorphism/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--glass-*` tokens. |
| `skills/glassmorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify reduced-transparency and opaque fallback mapping manually. |
| `skills/glassmorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/glassmorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/glassmorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/glassmorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 6. Liquid Glass

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/liquid-glass/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Capability tiers and effect degradation are documented. |
| `skills/liquid-glass/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--liquid-*` tokens. |
| `skills/liquid-glass/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Manually verify distortion/blur/tint/opaque capability ladder per renderer. |
| `skills/liquid-glass/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/liquid-glass/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/liquid-glass/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/liquid-glass/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 7. Material Design

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/material-design/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | System-level guidance is consistent with semantic role approach. |
| `skills/material-design/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--md-*` tokens. |
| `skills/material-design/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify component-role mapping and state layers across all renderers. |
| `skills/material-design/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/material-design/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/material-design/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/material-design/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 8. Neobrutalism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/neobrutalism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Focus-vs-heavy-border rule is documented; manual example comparison pending. |
| `skills/neobrutalism/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--neo-*` tokens. |
| `skills/neobrutalism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify pressed translation does not alter semantic/hit bounds across renderers. |
| `skills/neobrutalism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neobrutalism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neobrutalism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neobrutalism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 9. Neumorphism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/neumorphism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Explicit flat fallback and shadow-independent state guidance are present. |
| `skills/neumorphism/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--neu-*` tokens. |
| `skills/neumorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify inset-shadow degradation and explicit state cues on native renderers. |
| `skills/neumorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neumorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neumorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neumorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 10. Skeuomorphism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/skeuomorphism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Custom gesture alternatives and flat fallback are explicitly required. |
| `skills/skeuomorphism/components.md` | **FAIL** | REVIEW | PASS | PASS | PASS | **FAIL** | Uses legacy `--sk-*` tokens. |
| `skills/skeuomorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify knob/slider/switch accessible alternatives across renderers. |
| `skills/skeuomorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/skeuomorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/skeuomorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/skeuomorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## Current stabilization summary

| Metric | Count |
|---|---:|
| Styles | 10 |
| Required files | 70 |
| Files with confirmed FAIL | 10 |
| `components.md` namespace failures | 9 |
| `SKILL.md` content-leak/version-drift failures | 1 |
| Example files passing current automated gates | 40 |
| Files still requiring deeper manual parity review | 20 |

### Confirmed fix queue

1. Normalize 9 `components.md` files to the canonical `--um-<style>-...` namespace.
2. Remove ChatGPT-session citations and version-pinned Flutter wording from `skills/flat-design/SKILL.md`.
3. Re-run semantic/accessibility/quality gates after token migration.
4. Manually close all REVIEW cells by comparing `platforms.md` and four renderer examples per style.
5. Add validator rules so legacy token aliases and session citations cannot return.

## Definition of Done

The style audit is complete only when all 70 rows are **PASS**, with zero legacy token aliases, zero session citations, zero semantic/accessibility/fallback/performance regressions, and full CI green on the final head.