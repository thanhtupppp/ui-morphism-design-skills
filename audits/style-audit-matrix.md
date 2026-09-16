# Style Audit Matrix — v1.9 Stabilization

This matrix tracks the 11 supported styles across the 7 required files per style (77 files total).

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
| `skills/aurora-ui/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-aurora-ui-*` tokens are enforced; manual component comparison remains. |
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
| `skills/claymorphism/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-claymorphism-*` tokens are enforced; manual component comparison remains. |
| `skills/claymorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | CI passes; verify shadow reduction/fallback consistency manually. |
| `skills/claymorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/claymorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/claymorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/claymorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 4. Flat Design

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/flat-design/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Non-portable citations and framework-version-pinned wording were removed. |
| `skills/flat-design/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-flat-design-*` tokens are enforced; manual component comparison remains. |
| `skills/flat-design/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | CI passes; manually verify token mapping after namespace migration. |
| `skills/flat-design/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/flat-design/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/flat-design/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/flat-design/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 5. Glassmorphism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/glassmorphism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Opaque fallback sequence is documented correctly. |
| `skills/glassmorphism/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-glassmorphism-*` tokens are enforced; manual component comparison remains. |
| `skills/glassmorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify reduced-transparency and opaque fallback mapping manually. |
| `skills/glassmorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/glassmorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/glassmorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/glassmorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 6. Liquid Glass

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/liquid-glass/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Capability tiers and effect degradation are documented. |
| `skills/liquid-glass/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-liquid-glass-*` tokens are enforced; manual component comparison remains. |
| `skills/liquid-glass/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Manually verify distortion/blur/tint/opaque capability ladder per renderer. |
| `skills/liquid-glass/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/liquid-glass/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/liquid-glass/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/liquid-glass/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 7. Material Design

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/material-design/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | System-level guidance is consistent with semantic role approach. |
| `skills/material-design/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-material-design-*` tokens are enforced; manual component comparison remains. |
| `skills/material-design/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify component-role mapping and state layers across all renderers. |
| `skills/material-design/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/material-design/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/material-design/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/material-design/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 8. Neobrutalism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/neobrutalism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Focus-vs-heavy-border rule is documented; manual example comparison pending. |
| `skills/neobrutalism/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-neobrutalism-*` tokens are enforced; manual component comparison remains. |
| `skills/neobrutalism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify pressed translation does not alter semantic/hit bounds across renderers. |
| `skills/neobrutalism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neobrutalism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neobrutalism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neobrutalism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 9. Neumorphism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/neumorphism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Explicit flat fallback and shadow-independent state guidance are present. |
| `skills/neumorphism/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-neumorphism-*` tokens are enforced; manual component comparison remains. |
| `skills/neumorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify inset-shadow degradation and explicit state cues on native renderers. |
| `skills/neumorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neumorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neumorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/neumorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 10. Skeuomorphism

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/skeuomorphism/SKILL.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Custom gesture alternatives and flat fallback are explicitly required. |
| `skills/skeuomorphism/components.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Canonical `--um-skeuomorphism-*` tokens are enforced; manual component comparison remains. |
| `skills/skeuomorphism/platforms.md` | PASS | REVIEW | PASS | PASS | PASS | REVIEW | Verify knob/slider/switch accessible alternatives across renderers. |
| `skills/skeuomorphism/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/skeuomorphism/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/skeuomorphism/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |
| `skills/skeuomorphism/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Current automated parity/accessibility/quality gates pass. |

## 11. Swiss Editorial

| File | Token namespace | Semantic parity | Accessibility | Fallback | Performance | Overall | Notes |
|---|---|---|---|---|---|---|---|
| `skills/swiss-editorial/SKILL.md` | PASS | PASS | PASS | PASS | PASS | PASS | Typography-led scope, selection criteria, and fallbacks are explicit. |
| `skills/swiss-editorial/components.md` | PASS | PASS | PASS | PASS | PASS | PASS | Canonical tokens, state matrix, and responsive behavior are documented. |
| `skills/swiss-editorial/platforms.md` | PASS | PASS | PASS | PASS | PASS | PASS | Web, React, Flutter, React Native, and adapter mappings are documented. |
| `skills/swiss-editorial/example.css` | PASS | PASS | PASS | PASS | PASS | PASS | Automated parity, accessibility, responsive, and forced-colors gates pass. |
| `skills/swiss-editorial/example.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | Browser interaction and automated accessibility tests pass. |
| `skills/swiss-editorial/example.flutter.dart` | PASS | PASS | PASS | PASS | PASS | PASS | Flutter analysis and widget tests pass in the recorded harness. |
| `skills/swiss-editorial/example.native.tsx` | PASS | PASS | PASS | PASS | PASS | PASS | TypeScript validation passes; device checks remain documented in the verification record. |

## Current stabilization summary

| Metric | Count |
|---|---:|
| Styles | 11 |
| Required files | 77 |
| Files with confirmed FAIL | 0 |
| `components.md` namespace failures | 0 |
| `SKILL.md` content-leak/version-drift failures | 0 |
| Example files passing current automated gates | 44 |
| Swiss Editorial browser tests | 11 passing |

### Remaining review queue

1. Manually close the retained REVIEW cells by comparing `platforms.md` and four renderer examples per style.
2. Run device screen-reader, hardware keyboard, high-contrast, safe-area, and OS text-scaling checks for Swiss Editorial in host applications.
3. Keep the namespace, citation, semantic, accessibility, component parity, packaging, and eval gates green as styles evolve.

## Definition of Done

The style audit is complete only when all 77 rows are **PASS**, with zero legacy token aliases, zero session citations, zero semantic/accessibility/fallback/performance regressions, and full CI green on the final head.
