# Glassmorphism

## Intent
Create layered frosted surfaces that reveal but soften the content behind them.

## Rules
- Use translucent tint, subtle border, controlled blur, and depth through overlap.
- Keep important text on a stable surface and add a scrim when needed.
- Use one or two glass levels, not competing translucencies.
- Good for hero cards, floating navigation, modal surfaces, and contextual panels.
- Provide an opaque fallback surface.
- Bound `backdrop-filter` to small surfaces and test on mobile hardware.

## Avoid
- Full-screen blur as the default page background.
- Low-contrast text over busy imagery.
- Glass for long reading, data tables, or complex forms.
