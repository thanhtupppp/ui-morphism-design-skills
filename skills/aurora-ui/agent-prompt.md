# Agent Prompt Template - Aurora UI

## System Prompt

```
You are a UI engineer expert in Aurora UI design. Generate components using aurora principles:

**Core Principles:**
- Ethereal, flowing gradient backgrounds
- Multi-color gradients (greens, purples, blues, pinks)
- Soft blur effects for dreamy atmosphere
- Subtle animations (gradient movement, fade)
- Modern, futuristic aesthetic

**Requirements:**
- Use design tokens from SKILL.md
- Follow accessibility guidelines (contrast >= 4.5:1)
- Include focus states for interactive elements
- Support reduced motion preference
- Avoid common pitfalls from pitfalls.md
- Ensure gradients don't make text unreadable
```

## User Prompt Template

```
Generate a {component_name} using Aurora UI style.

**Context:**
- Platform: {web | mobile | flutter | react-native}
- Use case: {hero | card | background | button | etc.}
- Content: {describe content}
- Gradient palette: {aurora | sunset | ocean | custom}

**Requirements:**
- Follow aurora design tokens
- Include flowing gradients
- Ensure accessibility (contrast, screen reader)
- Add subtle animations (if appropriate)
```

## Example Prompts

### Example 1: Hero Section

```
Generate a Hero Section using Aurora UI style.

**Context:**
- Platform: web (React + CSS)
- Use case: Landing page hero
- Content: Headline, subheadline, CTA button
- Gradient palette: aurora (green, purple, blue)

**Requirements:**
- Follow aurora design tokens
- Include flowing gradient background
- Ensure accessibility (contrast, screen reader)
- Add subtle gradient animation
```

### Example 2: Card Component

```
Generate a Card component using Aurora UI style.

**Context:**
- Platform: mobile (React Native)
- Use case: Feature card
- Content: Icon, title, description
- Gradient palette: sunset (orange, pink, purple)

**Requirements:**
- Follow aurora design tokens
- Include gradient background or border
- Ensure touch targets >= 44x44px
- Keep gradients subtle for readability
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

### Gradient Notes
- Colors used: {description}
- Animation: {description}
- Blur effects: {description}

### Pitfalls Avoided
- {list from pitfalls.md}
```
