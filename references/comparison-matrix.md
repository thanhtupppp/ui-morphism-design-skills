# Morphism Comparison Matrix

This is an original implementation-oriented matrix inspired by the documentation architecture of [`Shubham7995/ui-morphism`](https://github.com/Shubham7995/ui-morphism/tree/main/docs). It is not a copy of that repository's prose. Use it to choose a style from product constraints rather than visual preference alone.

| Style | Visual signature | Best fit | Main risk | Default stance |
|---|---|---|---|---|
| Skeuomorphism | Material texture, bevel, specular highlight, contact shadow | Device panels, media tools, instrument controls | Texture and visual weight reduce clarity | Use for a bounded physical metaphor |
| Flat Design | Color, type, spacing, and borders create hierarchy | SaaS, CRUD, dashboards, docs | Minimal styling can weaken affordance | Safe production default |
| Neumorphism | Raised/pressed same-surface controls with paired shadows | Thermostat, smart-home, compact utilities | Shadow-only boundaries and low contrast | Accent component only |
| Material Design | Surfaces, elevation, state layers, components, motion | Cross-platform systems and app shells | Framework defaults can become generic | Strong system foundation |
| Glassmorphism | Translucent tinted plane, blur, rim, controlled backdrop | Navigation, hero cards, modal and transient chrome | Backdrop-dependent contrast and blur cost | Bounded overlay layer |
| Claymorphism | Opaque inflated forms, rounded geometry, soft hue-matched shadows | Education, onboarding, gamification | Toy-like tone and bulky dense layouts | Expressive surface only |
| Liquid Glass / Liquid UI | Dynamic translucent material with tint, reflection, and contextual depth | Platform chrome, navigation, contextual controls | Transparency, nested effects, platform mismatch | Functional material, not wallpaper |
| Aurora UI | Ambient multi-color gradient and glow behind content | AI/marketing hero, premium brand surfaces | Noise and reading contrast | Background accent only |
| Bento UI | Modular grid with intentional spans and content hierarchy | Overview pages, portfolios, feature sections | Card soup and broken mobile reading order | Layout system, not a material |
| Neobrutalism | Solid borders, hard offset shadows, saturated fills, bold type | Dev tools, portfolios, bold campaigns | Harsh hierarchy, overflow, localization | Deliberate high-contrast system |

## Depth models

- Skeuomorphism casts light onto a simulated object.
- Neumorphism extrudes a control from its own background.
- Claymorphism gives an opaque object its own volume and color.
- Glassmorphism and Liquid Glass place a translucent plane between the user and content.
- Flat Design, Bento UI, and Neobrutalism use layout, borders, gaps, or hard offsets instead of soft depth.

## Cost tiers

| Tier | Styles | Typical concern |
|---|---|---|
| Low visual cost | Flat Design, Material Design, Bento UI, Neobrutalism | Hierarchy, state clarity, content order |
| Medium visual cost | Skeuomorphism, Neumorphism, Glassmorphism, Claymorphism | Shadow count, contrast, asset weight, blur |
| High visual cost | Liquid Glass, Aurora UI at motion, heavy Skeuomorphism | Compositing, backdrop sampling, animation budget |

## Selection rule

Choose one primary visual language. Add at most one supporting style with a defined boundary. If the product is data-dense, critical, field-operated, or performance-constrained, prefer Flat Design or Material Design and borrow only a bounded layout or accent pattern.
