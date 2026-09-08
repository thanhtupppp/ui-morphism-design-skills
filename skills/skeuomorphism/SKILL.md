# Skeuomorphism

## Purpose
Skeuomorphism communicates function through physical material, texture, bevel, lighting, and recognizable object metaphors.

## Use when
- The product represents a device, instrument, vehicle, camera, audio tool, or physical workspace.
- Users benefit from a familiar physical affordance.
- The material metaphor is part of the product identity.

## Avoid when
- The interface is a dense ERP, table, form, documentation, or content reader.
- Texture competes with text or produces large image payloads.
- A realistic metaphor would be unfamiliar or misleading.

## Visual DNA
- Choose one material per surface: metal, rubber, paper, leather, glass, or plastic.
- Use one consistent light direction for highlight, bevel, and contact shadow.
- Use a restrained 3-stop gradient and subtle grain; never texture long text surfaces.
- Separate decorative edge tokens from functional boundary tokens.

## Components
- Button: bevel and pressed inset are supplemental; label and focus remain explicit.
- Knob: show label, current value, min/max, keyboard alternative, and pressed state.
- Card: use material only for a bounded device module, not every content container.
- Table/form: use flat opaque treatment inside a physical shell.

## Token recipe
```css
.um-skeuomorphism-control {
  background: linear-gradient(#d9d4c7, #aaa397);
  border: 1px solid #756f66;
  border-radius: var(--um-skeuomorphism-radius-md, 10px);
  box-shadow: 0 1px 2px rgb(0 0 0 / .28), 0 5px 12px rgb(0 0 0 / .18), inset 0 1px rgb(255 255 255 / .72), inset 0 -2px 3px rgb(0 0 0 / .14);
}
.um-skeuomorphism-control:active { box-shadow: inset 0 2px 4px rgb(0 0 0 / .28); }
```

## Motion
Use short press/release translation or dial rotation. Do not animate decorative grain. Provide an instant state change for reduced motion.

## Responsive and performance
Use optimized CSS gradients before raster textures. Lazy-load decorative assets and remove grain in forced-colors mode. Keep controls at least 44px where touch is expected.

## Accessibility checklist
- [ ] Labels and values do not depend on texture.
- [ ] Functional borders remain visible if shadows/background images disappear.
- [ ] Keyboard controls expose the same action as pointer manipulation.
- [ ] Focus is an outline or border, not only an inset shadow.

## Anti-patterns
- Fake hardware metaphors in generic admin interfaces.
- Four unrelated materials in one screen.
- Realistic visuals that look clickable but are not interactive.
