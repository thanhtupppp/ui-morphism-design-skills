# Platform Capability Matrix

Use this matrix during style selection. `Native` means the renderer has a first-class primitive; `Adapt` means the effect should be translated; `Fallback` means the effect must not be required for usability.

| Style | HTML/CSS | React | Flutter | Primary implementation strategy |
|---|---|---|---|---|
| Skeuomorphism | Native + CSS gradients/shadows | Same DOM/CSS recipe | Adapt with `BoxDecoration`, `BoxShadow`, gradients, optional assets | Material shell + bounded physical controls |
| Flat Design | Native | Native React + CSS | Theme tokens + standard widgets | Semantic surfaces and explicit states |
| Neumorphism | Native CSS shadows | Same DOM/CSS recipe | Adapt with paired `BoxShadow`s; explicit border/focus | Bounded controls, not whole data surfaces |
| Material Design | Native CSS primitives | React + design-system primitives | Material widgets + `ThemeExtension` | Component/state system first |
| Glassmorphism | Progressive enhancement (`backdrop-filter`) | Same web capability | Adapt with `BackdropFilter` + translucent surface | Small overlays with opaque fallback |
| Claymorphism | Native CSS shadows/gradients | Same DOM/CSS recipe | `BoxDecoration` + multiple `BoxShadow`s | Opaque inflated surfaces |
| Liquid Glass | Progressive enhancement; optional advanced effects | Same web capability | `BackdropFilter`/native effect wrappers when supported | Functional chrome, bounded effect |
| Aurora UI | Native gradients/filters | Same web capability | `CustomPaint`/gradients; keep static fallback | Background atmosphere only |
| Bento UI | CSS Grid/Flex | React layout primitives | `LayoutBuilder`/`Wrap`/`GridView` | Content-first modular layout |
| Neobrutalism | Native borders/transforms | Same DOM/CSS recipe | Borders + offsets/physical translation | High-contrast structural styling |

## Target-specific rules

### HTML/CSS
Use real HTML semantics and CSS custom properties. Treat advanced effects as progressive enhancement. Maintain an accessible fallback when blur, animation, or color features are unavailable.

### React
React does not define a styling system; use semantic DOM with the project's CSS, CSS Modules, Tailwind, or other existing styling layer. Keep visual tokens separate from component behavior.

### Flutter
Use `ThemeExtension`/theme data as the semantic token transport. Prefer standard Material/Cupertino widgets for semantics. Wrap visual treatment around them instead of rebuilding interaction semantics from `GestureDetector` when a standard control exists.

### React Native and future adapters
The same semantic token names should be retained. Effects unavailable in the platform become bounded fallbacks. Do not embed CSS-only assumptions into the canonical design decision.
