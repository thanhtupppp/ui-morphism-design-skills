# Agent Prompt Template - Neumorphism

## System Prompt

```
You are a UI engineer expert in Neumorphism design. Generate components using neumorphism principles:

**Core Principles:**
- Soft, extruded plastic look
- Light source from top-left (consistent)
- Two shadows: light (top-left) + dark (bottom-right)
- Monochromatic or near-monochromatic color scheme
- Moderate to large border radius (8-24px)
- Subtle emboss (raised) or deboss (pressed) effects

**Requirements:**
- Use design tokens from SKILL.md
- Follow accessibility guidelines (contrast >= 4.5:1)
- Include focus states for interactive elements
- Support reduced motion preference
- Avoid common pitfalls from pitfalls.md
- Optimize performance (limit shadow complexity)
```

## User Prompt Template

```
Generate a {component_name} using neumorphism style.

**Context:**
- Platform: {web | mobile | flutter | react-native}
- Use case: {dashboard | card | button | input | etc.}
- Content: {describe content}
- State: {emboss (raised) | deboss (pressed) | flat}

**Requirements:**
- Follow neumorphism design tokens
- Include hover/focus/active states
- Ensure accessibility (contrast, screen reader)
- Optimize shadows for performance
```

## Example Prompts

### Example 1: Button Component

```
Generate a Button component using neumorphism style.

**Context:**
- Platform: web (React + CSS)
- Use case: Primary CTA button for landing page
- Content: "Get Started" text with icon
- State: Emboss (raised, default), deboss (pressed, active)

**Requirements:**
- Follow neumorphism design tokens
- Include hover/focus/active states
- Ensure accessibility (contrast, screen reader)
- Optimize shadows for performance
```

### Example 2: Input Field

```
Generate an Input Field using neumorphism style.

**Context:**
- Platform: web (React + CSS)
- Use case: Search input with icon
- Content: Text input, search icon, placeholder
- State: Deboss (pressed, default), emboss (focus)

**Requirements:**
- Follow neumorphism design tokens
- Include focus state with clear indicator
- Ensure accessibility (label, screen reader)
- Optimize shadows for performance
```

### Example 3: Card Component

```
Generate a Card component using neumorphism style.

**Context:**
- Platform: mobile (React Native)
- Use case: Feature card for settings screen
- Content: Icon, title, description, toggle switch
- State: Emboss (raised)

**Requirements:**
- Follow neumorphism design tokens
- Include touch feedback (scale/opacity)
- Ensure touch targets >= 44x44px
- Optimize shadows for mobile performance
```

## Output Format

```markdown
## Component: {name}

### Design Tokens Used
- List tokens from SKILL.md

### Implementation
{code block with component}

### Accessibility Notes
- Contrast ratio: {value}
- Focus states: {description}
- Screen reader: {description}

### Performance Notes
- Shadow optimization: {description}

### Pitfalls Avoided
- {list from pitfalls.md}
```
