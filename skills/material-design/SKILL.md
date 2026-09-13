# Material Design

## Definition
Material Design is a **design system for components and interaction**, not a color palette or collection of rounded cards. Its visual language comes from semantic color roles, typography, shape, surfaces, elevation, state layers, adaptive layouts, and purposeful motion working together.

## Beginner recognition test
A Material interface should let a new user recognize familiar patterns immediately: filled/outlined/tonal/text buttons, labeled text fields, cards, chips, menus, dialogs, snackbars, navigation bars/rails/drawers, tabs, lists, checkboxes, radios, switches, sliders, and progress indicators. Behavior is part of the style.

## Core principles
1. **Semantics before styling.** Start with the correct control and accessible name.
2. **Roles before literals.** Colors and typography are named roles, not scattered hex values.
3. **Components before decoration.** Anatomy and states are consistent across screens.
4. **Elevation explains spatial relationship.** It does not replace borders, focus, or semantic state.
5. **State is explicit.** Default, hover, focus, pressed, selected, disabled and task-specific states are designed intentionally.
6. **Adaptive rather than shrunken.** Recompose navigation and content when space changes.
7. **Motion explains change.** Use local, purposeful motion; support reduced motion.
8. **Platform-aware rendering.** Web and Flutter preserve the same intent while using native capabilities.

## Visual system
### Color
Use primary, secondary, tertiary, error, surface, background, on-* content roles, plus outline/outline-variant roles. Build light/dark themes by swapping role values rather than rewriting component logic.

### Typography
Use a deliberate hierarchy for display, headline, title, body, label, and supporting text. Typography carries information hierarchy even when elevation is removed.

### Shape
Use a named shape scale from small corners on fields to larger corners on containers/dialogs. Pills are appropriate for selected component families, not every component.

### Elevation and surfaces
Use a small named elevation ladder. Elevation should communicate that a surface is above another surface or is an active floating layer. Do not create arbitrary shadows for each element.

### State layers
Hover, focus, pressed, dragged and selected states may use bounded overlays or color changes. These layers must not reduce text/icon readability.

## Component rules
Core families must have anatomy + states + responsive behavior + accessibility behavior documented in `components.md`:

- Buttons: filled, outlined, tonal, text, icon, FAB.
- Fields: text, search, multiline, validation/helper states.
- Selection: checkbox, radio, switch, segmented control, chips.
- Containers: card, list, surface, dialog, sheet.
- Navigation: bar, rail, drawer, tabs.
- Feedback: snackbar, banner, alert, progress, loading, skeleton.
- Data: list, table, data grid, pagination, filters, empty/error states.
- Menus: menu, submenu, popup/context actions.

## Interaction state contract
Every interactive component defines at minimum:

`default → hover(pointer only) → focus-visible → pressed → selected/checked → disabled`

and adds `loading`, `error`, `success`, `dragged`, `expanded`, or `read-only` when applicable.

Critical information must never exist only in hover, elevation, or color.

## Adaptive behavior
Use compact/medium/expanded layouts and task-driven breakpoints. Examples include navigation bar↔rail↔drawer, single-column↔multi-column, side panel↔sheet, and inline actions↔overflow menu. Preserve semantic and task order when layout changes.

## Accessibility
Material implementations must test contrast, focus visibility, target size, keyboard traversal, screen-reader names, dialog focus management, text scaling, localization, RTL, reduced motion, forced-colors/high-contrast equivalents where relevant, and error association.

## Performance
Prefer framework primitives and semantic native controls. Bound elevation, blur, and animation costs. Avoid a page full of simultaneously animated or heavily elevated elements.

## Cross-platform policy
Do not demand pixel-identical rendering across HTML/CSS, React, Flutter, or React Native. Demand **semantic equivalence and recognizable material behavior**. Renderer-specific differences are acceptable when roles, hierarchy, states, interaction, accessibility, and responsive intent remain equivalent.

## Anti-patterns
- “Purple rounded UI” presented as Material without component behavior.
- Elevation on every surface.
- Custom-painted controls that discard native semantics.
- Hover-only information on mobile-capable products.
- Fixed desktop coordinates that collapse at compact widths.
- State-layer opacity that makes labels unreadable.
