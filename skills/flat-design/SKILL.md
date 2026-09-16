# Flat Design

## Definition
Flat Design is a visual language where hierarchy and affordance come primarily from **semantic color, typography, spacing, alignment, grouping, borders, and explicit state changes** instead of realistic depth, texture, bevels, or material simulation.

A flat interface is not an interface with every shadow removed. It is an interface whose meaning survives without decorative depth.

## Beginner recognition test
A person unfamiliar with design should be able to point at a screen and answer immediately:

- What is the page/background?
- Which regions belong together?
- Which elements are interactive?
- Which control is primary?
- Which navigation item is active?
- Which field has focus?
- Which content is selected, disabled, loading, or in error?

If removing shadows or gradients makes these answers unclear, the hierarchy is insufficiently semantic for Flat Design.

## Visual DNA
1. **Color roles** define semantic importance, not random decoration.
2. **Typography** defines hierarchy and reading order.
3. **Spacing** separates groups and establishes rhythm.
4. **Alignment** creates structure.
5. **Borders/separators** define functional boundaries when needed.
6. **Surface tone** distinguishes major regions.
7. **Icons** reinforce meaning but do not replace labels for critical actions.
8. **Depth is optional** and restrained; a zero-shadow component is fully valid.

## Core principles
- Use semantic tokens rather than component-specific one-off colors.
- Prefer one clear visual hierarchy over many competing accents.
- Make interaction states explicit and persistent enough to understand without hover.
- Keep content order and DOM/focus order aligned with task order.
- Use familiar controls when available rather than drawing imitations.
- Preserve meaning in grayscale, high-contrast, zoom, localization, and reduced-motion modes.
- Keep the visual language stable across mobile, tablet, desktop, and large-screen layouts.

## Component system
The canonical component set includes page/shell, header, navigation, tabs, buttons, icon buttons, links, cards/panels, lists, forms, inputs, selects, checkboxes, radios, switches, sliders, menus, dialogs/sheets, alerts/banners/snackbars, badges/chips, progress/meter, tables/data grids, pagination, loading/skeleton, empty state, and error recovery.

Every interactive component needs a state matrix appropriate to its behavior, including default, hover where supported, pressed, focus-visible/focused, selected/checked, disabled, loading, invalid/error and success where meaningful.

## Data-dense stance
Flat Design is the default recommendation when the product is operational, data-dense, cross-platform, accessibility-sensitive, performance-constrained, or expected to evolve for years. It can form the stable foundation beneath a bounded expressive accent style.

## Forms
Form fields use a persistent label, control, supporting/help text when useful, and explicit validation. Errors must explain what happened and what to do next. Required state should not rely on placeholder text alone.

## Navigation
Navigation communicates both destination and current location. Active state should combine at least two cues when practical, such as color + weight, color + underline/indicator, or icon + surface.

## Tables
Use stable opaque surfaces, clear header/body differentiation, predictable alignment, selected-row state, sort indicators, and explicit empty/loading/error behavior. Do not turn every cell into a bordered box.

## Responsive behavior
Use mobile-first CSS Grid/Flexbox on the web and adaptive layout primitives on native platforms. Prefer content-driven breakpoints and stable reading order. Validate compact phone, tablet, desktop, zoom/text scaling, long localization, and RTL when applicable.

## Motion
Use short, purposeful opacity/transform transitions for feedback. Critical state should be immediately understandable without waiting for animation. Under reduced motion, remove non-essential transitions and preserve state changes.

## Accessibility
Focus must be visible and not rely on color alone. Status, selection, and errors should have more than one communication channel when practical. Apply the repository accessibility contract for focus visibility, target geometry, text scaling, localization, reduced motion/effects, and high-contrast behavior, and verify those requirements per renderer.

For Flutter, prefer standard semantic widgets and theme-level token mapping rather than scattering one-off visual values across widgets. Use `ThemeData`/`ThemeExtension` or the host application's equivalent theme mechanism to map project tokens while preserving native semantics and adaptive behavior.

## Flutter mapping
Recommended primitives:

- surface/container → `Container`, `DecoratedBox`, `Card` with restrained elevation
- primary action → `FilledButton`
- secondary action → `OutlinedButton`
- tertiary action → `TextButton`
- field → `TextField`/`TextFormField` with `InputDecoration`
- navigation → standard `NavigationBar`/`NavigationRail`/appropriate app shell
- dialog → `Dialog`/`showDialog`
- transient message → `SnackBar`
- list → `ListView`/slivers
- data → `DataTable`/`PaginatedDataTable` or project data-grid primitive

When the host Flutter configuration uses Material components, Flat Design should intentionally neutralize unnecessary elevation, shape, and decorative color while preserving standard behavioral semantics. Do not pin the guidance to a particular framework release; validate the current host framework capabilities during implementation.

## Web mapping
Use semantic HTML first: `button`, `a`, `input`, `select`, `textarea`, `nav`, `dialog`, headings, lists and tables. React should preserve the same semantics and only handle composition/state; the exact styling mechanism is determined by the host project.

## Progressive enhancement
Flat Design is the mandatory fallback for advanced morphism styles. If blur, glow, transparency, texture, animation, or custom filters fail, the semantic structure and component states must remain fully usable.

## Anti-patterns
- Removing borders/focus indicators to appear minimal.
- Gray-on-gray body text.
- Color-only status or selection.
- Treating every item as a card.
- Replacing standard controls with inaccessible visual replicas.
- Fixed-height text containers that break under localization or scaling.
- Excessive micro-borders that turn the UI into a grid of boxes.
- Applying expressive gradients or effects to every component.
