# Liquid Glass / Liquid UI

## Purpose
Liquid Glass is a dynamic translucent **functional material** for contextual navigation, floating controls, toolbars, media chrome, and transient surfaces. Unlike ordinary Glassmorphism, it is designed to adapt its appearance to surrounding content and interaction context.

## How to recognize it
A Liquid Glass surface looks like a polished translucent control layer that appears to float above its surroundings. Look for:
- translucent body with context-sensitive tint;
- controlled backdrop blur;
- a bright/subtle rim that defines the material boundary;
- soft depth/separation from the content behind it;
- grouped controls that visually behave as one movable/expandable material;
- restrained reflection/highlight that suggests a glossy surface;
- shape and grouping that can morph between compact and expanded states.

It is **not** simply a card with `opacity` and blur. The material participates in navigation and contextual interaction.

## Difference from Glassmorphism
- **Glassmorphism:** a frosted translucent surface placed above a controlled backdrop; usually static.
- **Liquid Glass:** a functional translucent material with contextual adaptation, dynamic grouping/morphing, and optional reflection/distortion.

When the design only needs a static frosted panel, choose Glassmorphism instead.

## Visual DNA
1. Stable functional silhouette and hit area.
2. Translucent tint that preserves content hierarchy.
3. Bounded backdrop blur.
4. Clear rim/border for the material edge.
5. Soft depth/elevation.
6. Optional specular reflection/highlight.
7. Optional controlled distortion/displacement only where the renderer can support it reliably.

Never make distortion the only signal of interaction or state.

## Material levels
- **Liquid 0:** opaque fallback surface.
- **Liquid 1:** translucent + rim.
- **Liquid 2:** translucent + blur + rim + depth.
- **Liquid 3:** Liquid 2 + restrained reflection/morphing.
- **Liquid 4:** optional distortion/shader enhancement; never required for usability.

Default to Liquid 2. Use higher levels only for bounded, high-value chrome.

## Component strategy
- **Navigation / toolbar:** primary use; controls are grouped into one material.
- **Floating action group:** useful for contextual actions.
- **Media controls:** useful when controls float over media.
- **Context menu / command surface:** use when it floats over known content.
- **Modal / sheet:** may use Liquid material around the shell, while critical reading/form content remains stable.
- **Buttons:** often transparent or softly tinted within a Liquid group; selected/pressed state needs explicit feedback.
- **Fields:** keep conventional and opaque when text entry is important.
- **Tables / data grids:** use Flat/Material surfaces.

## Shape and morphing
- Use a deliberate radius family: pill for compact toolbars, rounded rectangle for panels.
- Compact controls may be capsule-shaped; expanded surfaces should preserve a coherent parent silhouette.
- Morphing must preserve control identity, hit area, focus order, and accessible names.
- Never use shape animation to communicate a state that is not also exposed semantically.

## State rules
- Default: translucent stable material.
- Hover: subtle tint/illumination change on pointer platforms.
- Focus: explicit high-contrast ring above the rim.
- Pressed: slight compression/translation or stronger tint; preserve hit area.
- Selected: indicator/icon/fill plus optional material emphasis.
- Disabled: reduce visual decoration but keep content readable.
- Expanded: material grows/morphs while preserving semantic relationship.
- Loading: visible progress indicator; reflection/blur must not imply progress.
- Error/destructive: semantic icon/text/border/state color; never rely on glow.

## Motion
Use motion to explain grouping and spatial continuity. Favor short transform, opacity, and shape transitions. Reflection/distortion should be optional. Under reduced motion, freeze decorative dynamics and use simple state changes.

## Responsive rules
- Reduce blur area and effect density on small screens.
- Prefer a single bounded Liquid surface over several overlapping surfaces.
- Toolbars may wrap, collapse, or become scrollable, but control order must remain meaningful.
- Keep touch targets at the host platform minimum.
- Do not allow morphing or shadows to clip localized labels.

## Accessibility
- Content and state must remain understandable with Liquid effects removed.
- Focus must remain visible on light, dark, saturated, and moving backgrounds.
- Provide reduced-transparency/static mode where appropriate.
- Preserve accessible names and expanded/collapsed state.
- Test keyboard, screen reader, text scaling, contrast, grayscale, forced colors/high contrast, and localization.

## Performance
- Keep backdrop sampling bounded and shallow.
- Avoid nested Liquid/Glass surfaces.
- Avoid continuously animated large blur or distortion surfaces.
- Prefer static reflection layers.
- On constrained devices, reduce distortion first, then blur, while retaining tint, boundaries, and semantic state.

## Anti-patterns
- Liquid Glass as wallpaper.
- Glass-on-glass-on-glass nesting.
- Full-screen continuously distorted surfaces.
- Tiny controls inside oversized translucent shapes.
- Using glow/reflection/distortion instead of semantic state.
- Copying one platform's material literally into another without adapting to renderer capabilities.