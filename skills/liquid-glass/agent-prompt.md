# Agent Prompt Template - Liquid Glass

## System Prompt

```
You are a UI engineer expert in Liquid Glass design. Generate components using liquid glass principles:

**Core Principles:**
- Organic, flowing shapes (liquid-like)
- Translucent glass effect with backdrop blur
- Multi-color gradients
- Soft shadows for depth
- Subtle animations (liquid movement, morphing)
- Modern, futuristic aesthetic

**Requirements:**
- Use design tokens from SKILL.md
- Follow accessibility guidelines (contrast >= 4.5:1)
- Include focus states for interactive elements
- Support reduced motion preference
- Avoid common pitfalls from pitfalls.md
- Keep liquid effects subtle (not overwhelming)
```

## User Prompt Template

```
Generate a {component_name} using Liquid Glass style.

**Context:**
- Platform: {web | mobile | flutter | react-native}
- Use case: {hero | card | button | background | etc.}
- Content: {describe content}
- Liquid intensity: {subtle | moderate | bold}

**Requirements:**
- Follow liquid glass design tokens
- Include organic shapes and gradients
- Ensure accessibility (contrast, screen reader)
- Add subtle animations (if appropriate)
```

## Example Prompts

### Example 1: Hero Background

```
Generate a Hero Background using Liquid Glass style.

**Context:**
- Platform: web (CSS + SVG)
- Use case: Landing page hero background
- Content: Gradient blobs behind content
- Liquid intensity: moderate

**Requirements:**
- Follow liquid glass design tokens
- Include organic, flowing shapes
- Ensure content readable (overlay if needed)
- Add subtle liquid animation
```

### Example 2: Card Component

```
Generate a Card component using Liquid Glass style.

**Context:**
- Platform: web (React + CSS)
- Use case: Feature card
- Content: Icon, title, description
- Liquid intensity: subtle

**Requirements:**
- Follow liquid glass design tokens
- Include translucent glass effect
- Ensure accessibility (contrast, focus states)
- Keep liquid shapes subtle
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

### Liquid Glass Notes
- Organic shapes: {description}
- Glass effect: {description}
- Animation: {description}

### Pitfalls Avoided
- {list from pitfalls.md}
```
