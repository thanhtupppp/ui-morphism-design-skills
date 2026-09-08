# Liquid Glass / Liquid UI

## Intent
Use a dynamic translucent material that adapts to surrounding content while keeping controls and navigation legible.

## Rules
- Treat the material as a functional layer: navigation, toolbar, contextual control, or floating action.
- Use tint, blur, reflection, and shape changes sparingly.
- Preserve content hierarchy beneath the material.
- Define expanded, collapsed, focused, scrolled, and reduced-motion states.
- Provide a solid fallback for unsupported blur or low-performance contexts.

## Avoid
- Decorative transparency over critical text.
- Platform imitation without adapting to the actual product and device.
- Applying the effect to every card or the whole page.
