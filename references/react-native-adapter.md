# React Native Adapter Contract

This contract defines how UI Morphism styles map to React Native without requiring web-specific CSS behavior.

## 1. Semantic-first mapping

Preserve this order across renderers:

`role → content hierarchy → interaction state → responsive behavior → accessibility → visual treatment → fallback`

Use React Native primitives for behavior and composition. Visual fidelity is secondary to semantic equivalence.

## 2. Canonical token mapping

Map the shared semantic roles to the renderer instead of copying CSS variables literally.

| Semantic role | React Native mapping |
|---|---|
| `surface.*` | `backgroundColor` / nested surface styles |
| `content.*` | `color` / typography style |
| `border.*` | `borderWidth` + `borderColor` |
| `radius.*` | `borderRadius` |
| `space.*` | `margin` / `padding` / `gap` where supported |
| `shadow.*` | platform shadow/elevation adapter |
| `focus.ring` | focus-visible state + explicit border/outline treatment where supported |
| `state.*` | explicit state style and/or accessible state metadata |
| `motion.*` | Animated/Reanimated or platform motion primitive |

Keep style-specific tokens under the canonical `--um-<style>-<group>` naming model at the source-design level.

## 3. Native interaction primitives

Prefer:

- `Pressable` for buttons, tabs, cards, and other tappable surfaces.
- `TextInput` for text entry.
- `Switch`, `Checkbox`, `Slider`, and platform navigation primitives for native semantics.
- `AccessibilityInfo` and accessibility props for state and assistive technology behavior.

Do not emulate a control with a plain `View` plus a gesture handler when a native semantic primitive can express it.

## 4. Responsive adaptation

React Native layouts should respond to available width rather than desktop pixel coordinates.

Use the project's established responsive primitive such as `useWindowDimensions`, `onLayout`, Flexbox, `gap`, or an existing breakpoint hook.

Recommended intent:

| Width class | Behavior |
|---|---|
| Compact | Single-column flow, tighter decorative spacing, preserve target size |
| Medium | Two-column or mixed layout when content allows |
| Expanded | Full hierarchy, bounded content width, larger spacing |

Do not encode responsiveness as visual-only scaling of every component.

## 5. Style-specific capability rules

### Skeuomorphism
Prefer bounded gradients, borders, and platform shadows. Reduce material decoration before reducing text or target size.

### Flat Design
Use minimal depth, clear borders, semantic color roles, and native controls. Avoid adding elevation just to simulate a web card.

### Neumorphism
Treat paired shadows as optional decoration. Preserve explicit borders, focus, and selected/pressed state without them.

### Material Design
Map elevation and state layers to platform-supported elevation/pressed-state APIs. Preserve component hierarchy rather than reproducing CSS overlays.

### Glassmorphism
Treat blur/translucency as optional. Provide an opaque surface path when backdrop blur is unavailable, expensive, or disabled.

### Claymorphism
Use opaque rounded surfaces, bounded shadows, and restrained highlights. Keep content readable when decorative volume is removed.

### Liquid Glass
Prefer the strongest supported translucent/blur primitive, but always maintain an opaque fallback. Never make blur a prerequisite for interaction.

### Aurora UI
Treat Aurora as atmospheric background/emphasis. Keep foreground surfaces semantic and readable with the atmosphere disabled.

### Bento UI
Use Flexbox or a maintained grid/layout library. When arbitrary grid spans are unavailable, group content deterministically without changing priority.

### Neobrutalism
Use hard borders, flat fills, and offset shadows where supported. Keep focus, pressed, and disabled states explicit.

## 6. Accessibility

- Preserve accessible labels and roles independent from decoration.
- Expose selected/pressed/disabled/busy/expanded state where applicable.
- Keep touch targets at least the platform's documented minimum; for this skill's Flutter policy use 48×48 logical pixels, while React Native targets should follow the product/platform accessibility baseline.
- Do not depend on hover, blur, shadow, transparency, or color alone for meaning.
- Respect large text and localization by allowing variable-height content.

## 7. Performance and fallback

Effect capability should degrade in this order:

`full effect → reduced effect → opaque/static effect → simpler native surface`

Bound expensive blur, image filters, gradients, and shadow layers to local surfaces. Avoid continuously animating large effect regions.

The fallback must preserve semantic role, hierarchy, state, accessibility, responsive behavior, and readable content.
