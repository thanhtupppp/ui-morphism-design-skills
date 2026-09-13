# Glassmorphism — Cross-Platform Recipes

## Canonical intent
A translucent tinted plane with controlled backdrop blur, rim/border, and shadow sits above a known backdrop. Critical content should not depend on the backdrop.

## HTML/CSS
- Use `backdrop-filter` only as progressive enhancement with an opaque fallback.
- Bound blur to the smallest surface that needs it; avoid page-wide filters and nested glass.
- Use a scrim/tint strong enough to keep text readable over worst-case imagery.

## React
- Keep the glass component as a local surface wrapper and expose a `reducedEffects`/static mode when the product needs user-controlled transparency reduction.
- Preserve semantic dialog/navigation/button elements inside the visual shell.

## Flutter
- Use `BackdropFilter` with `ImageFilter.blur` for bounded surfaces, combined with a translucent `DecoratedBox` and border.
- Wrap expensive blur regions narrowly in a `ClipRRect` so sampling does not cover the whole subtree.
- Provide an opaque `Container`/`Material` fallback controlled by capability or accessibility settings.

## Component recipe
Navigation/modal/card chrome may use glass; dense forms/tables use opaque Flat/Material surfaces. Focus sits above the glass border as a solid ring.

## Accessibility/performance
Test bright, dark, colorful, and changing backdrops. Never use translucency as the only contrast mechanism. Flutter blur can be expensive; limit area and count. Web uses `@supports` fallback and `forced-colors` removal of decorative transparency.
