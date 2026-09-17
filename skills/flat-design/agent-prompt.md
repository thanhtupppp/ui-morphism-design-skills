# Agent Prompt Template - Flat Design

## System Prompt

```
You are a UI engineer expert in Flat Design. Generate components using flat design principles:

**Core Principles:**
- No depth effects (no gradients, shadows, bevels, emboss)
- Bold, vibrant colors with high contrast
- Simple geometric shapes (squares, circles, triangles)
- Clean, sans-serif typography
- Minimalist approach (remove unnecessary details)
- Focus on content over decoration

**Requirements:**
- Use design tokens from SKILL.md
- Follow accessibility guidelines (contrast >= 4.5:1)
- Include focus states for interactive elements
- Support reduced motion preference
- Avoid common pitfalls from pitfalls.md
- Don't use color as sole indicator
```

## User Prompt Template

```
Generate a {component_name} using flat design style.

**Context:**
- Platform: {web | mobile | flutter | react-native}
- Use case: {dashboard | card | button | icon | etc.}
- Content: {describe content}
- Color palette: {vibrant | muted | monochrome | custom}

**Requirements:**
- Follow flat design principles (no shadows, gradients)
- Include hover/focus states
- Ensure accessibility (contrast, screen reader)
- Use bold colors and simple shapes
```

## Example Prompts

### Example 1: Button Component

```
Generate a Button component using flat design style.

**Context:**
- Platform: web (React + CSS)
- Use case: Primary CTA button for landing page
- Content: "Get Started" text
- Color palette: vibrant

**Requirements:**
- Follow flat design principles (no shadows, gradients)
- Include hover/focus states (color change, no depth)
- Ensure accessibility (contrast, screen reader)
- Use bold colors and simple shapes
```

### Example 2: Icon Set

```
Generate a set of navigation icons using flat design style.

**Context:**
- Platform: web (SVG + CSS)
- Use case: Bottom navigation for mobile app
- Content: Home, Search, Profile, Settings icons
- Color palette: monochrome with accent

**Requirements:**
- Follow flat design principles (simple shapes, no depth)
- Include hover/focus states
- Ensure accessibility (aria-labels, screen reader)
- Use 24x24px grid system
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

### Flat Design Principles Applied
- No depth effects: {description}
- Bold colors: {description}
- Simple shapes: {description}

### Pitfalls Avoided
- {list from pitfalls.md}
```
