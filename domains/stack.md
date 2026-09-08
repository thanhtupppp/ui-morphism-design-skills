# Stack Guidance

## React / Next.js
Keep semantic structure and state logic independent from visual tokens. Use CSS variables for morphism parameters and component variants for style boundaries.

## Tailwind
Map semantic tokens in the Tailwind theme. Avoid arbitrary shadow/blur values inside individual components.

## Flutter
Put colors, shapes, elevations, and motion in `ThemeData` or a custom `ThemeExtension`. Respect platform reduced-motion settings.

## CSS
Use `@supports` for advanced effects. Pair every translucent or blurred surface with a stable fallback and explicit text contrast.
