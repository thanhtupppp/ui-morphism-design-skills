# Platform Capability Matrix

Use this matrix during style selection and capability negotiation. `Native` means the renderer has a first-class primitive; `Adapt` means the effect should be translated to the renderer's closest supported primitive; `Fallback` means the effect must not be required for usability.

| Style | HTML/CSS | React | Flutter | React Native | Primary implementation strategy |
|---|---|---|---|---|---|
| Skeuomorphism | Native + CSS gradients/shadows | Same DOM/CSS recipe | Adapt with `BoxDecoration`, `BoxShadow`, gradients, optional assets | Adapt with nested `View` styles and platform shadows; omit asset-heavy decoration when costly | Material shell + bounded physical controls |
| Flat Design | Native | Native React + CSS | Theme tokens + standard widgets | Native primitives + `StyleSheet` semantic tokens | Semantic surfaces and explicit states |
| Neumorphism | Native CSS shadows | Same DOM/CSS recipe | Adapt with paired `BoxShadow`s; explicit border/focus | Adapt paired shadows/elevation where supported; explicit border/focus fallback | Bounded controls, not whole data surfaces |
| Material Design | Native CSS primitives | React + design-system primitives | Material widgets + `ThemeExtension` | Native platform controls + shared semantic state tokens | Component/state system first |
| Glassmorphism | Progressive enhancement (`backdrop-filter`) | Same web capability | Adapt with `BackdropFilter` + translucent surface | Optional native/third-party blur only when supported; opaque surface fallback | Small overlays with opaque fallback |
| Claymorphism | Native CSS shadows/gradients | Same DOM/CSS recipe | `BoxDecoration` + multiple `BoxShadow`s | Opaque rounded `View` surfaces + bounded shadow/elevation | Opaque inflated surfaces |
| Liquid Glass | Progressive enhancement; optional advanced effects | Same web capability | `BackdropFilter`/native effect wrappers when supported | Native blur/material APIs when available; static opaque surface fallback otherwise | Functional chrome, bounded effect |
| Aurora UI | Native gradients/filters | Same web capability | `CustomPaint`/gradients; keep static fallback | Layered gradients or simple static backdrop; avoid requiring shader support | Background atmosphere only |
| Bento UI | CSS Grid/Flex | React layout primitives | `LayoutBuilder`/`Wrap`/`GridView` | Flexbox or maintained grid/layout library; deterministic grouping when spans are unavailable | Content-first modular layout |
| Neobrutalism | Native borders/transforms | Same DOM/CSS recipe | Borders + offsets/physical translation | Borders + `transform` offsets; avoid overflow-prone decoration | High-contrast structural styling |

## Capability tier legend

| Capability | Required | Preferred | Optional |
|---|---|---|---|
| Semantic roles/states | All renderers | — | — |
| Responsive layout | All renderers | Container/grid helpers | — |
| Focus/accessibility | All interactive renderers | Platform-specific focus affordances | — |
| Borders/radius/spacing | All renderers | — | — |
| Shadow/elevation | — | Web, Flutter, React Native platform primitives | Decorative multi-layer effects |
| Gradient | — | Web, Flutter, React Native where supported | Animated or shader-based gradient |
| Backdrop blur/translucency | — | Web/Flutter/native APIs when bounded | Continuous large-area blur |
| Advanced shader/displacement | — | — | Only when renderer and performance budget support it |
| Decorative animation | — | Small local surfaces | Large continuously animated effect regions |

## Selection and fallback rule

Select the strongest capability tier that the product and target renderer can support without changing semantic anatomy.

Use the deterministic degradation path:

`full effect → reduced effect → opaque/static effect → simpler native surface`

An unsupported effect must never remove content, change priority, hide state, or reduce the interaction target.

## Target-specific rules

### HTML/CSS
Use real HTML semantics and CSS custom properties. Treat advanced effects as progressive enhancement. Maintain an accessible fallback when blur, animation, or color features are unavailable.

### React
React does not define a styling system; use semantic DOM with the project's CSS, CSS Modules, Tailwind, or other existing styling layer. Keep visual tokens separate from component behavior.

### Flutter
Use `ThemeExtension`/theme data as the semantic token transport. Prefer standard Material/Cupertino widgets for semantics. Wrap visual treatment around them instead of rebuilding interaction semantics from `GestureDetector` when a standard control exists.

### React Native and future adapters
Follow `references/react-native-adapter.md` for role/state/token/responsive/accessibility mapping. Prefer native primitives and Flexbox/layout APIs. CSS-only assumptions are prohibited in the canonical design decision.
