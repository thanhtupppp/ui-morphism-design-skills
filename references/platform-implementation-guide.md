# Platform Implementation Guide

This guide defines how an agent should translate a selected morphism style into real code without losing semantics.

## 1. Read project constraints first

Identify target platform(s), rendering engine, existing component library, theme system, accessibility baseline, supported browser/OS range, density, device class, and performance budget. Do not introduce a second component library just to reproduce a visual effect.

## 2. Generate semantic tokens

Generate one canonical token set, for example:

```text
surface.canvas
surface.raised
surface.sunken
content.primary
content.secondary
content.disabled
border.default
border.strong
accent.primary
focus.ring
state.success
state.warning
state.danger
radius.sm/md/lg/pill
space.1..space.8
control.min
shadow.1..shadow.3
blur.1..blur.3
motion.fast/normal/slow
```

Add style-specific material tokens only when the selected style needs them.

## 3. Map tokens per platform

### Web
CSS custom properties + semantic HTML + media queries. Use `@supports` for progressive effects and `@media (prefers-reduced-motion: reduce)` / `@media (forced-colors: active)` for fallback behavior.

### React
Keep token storage in CSS variables/theme objects and component behavior in React. Do not put a React-specific abstraction into the canonical design skill when plain CSS/DOM semantics can express it.

### Flutter
Use `ThemeExtension` for custom tokens. Map shapes to `BorderRadius`/`ShapeBorder`, shadows to `BoxShadow`, typography to `TextTheme`, color roles to `ColorScheme` or extension tokens, spacing to constants/theme data, and effects to dedicated wrappers. Prefer standard Material/Cupertino widgets for semantics.

## 4. Component output

For each required component produce:

```text
Semantic anatomy
Token bindings
Web/React implementation
Flutter implementation
State matrix
Responsive behavior
Accessibility behavior
Effect fallback
Performance note
```

## 5. Capability negotiation

Treat advanced effects as optional capabilities. A platform adapter should expose something equivalent to:

```text
supports.blur
supports.backdropBlur
supports.shader
supports.texture
supports.advancedMotion
```

When unsupported or disabled, select the documented fallback rather than silently dropping the component's hierarchy.

## 6. Verification

Verify visual states at compact/medium/expanded sizes, keyboard focus, pointer/touch interaction, screen reader semantics, large text, localization, high contrast/forced colors, reduced motion, and low-power performance.

A successful implementation is the same design decision expressed through different rendering primitives—not a different design invented for each framework.
