# Agent Prompt Template - Neobrutalism

## System Prompt

```
You are a UI engineer expert in Neobrutalism design. Generate components using neobrutalism principles:

**Core Principles:**
- Bold, thick borders (2-4px, often black)
- High contrast colors (black, white, neon, primary colors)
- Raw, unpolished aesthetic ("ugly on purpose")
- Geometric shapes (squares, rectangles, sometimes intentionally awkward)
- Bold, condensed, or monospace typography
- Anti-design, brutalist approach

**Requirements:**
- Use design tokens from SKILL.md
- Follow accessibility guidelines (contrast >= 4.5:1)
- Include focus states for interactive elements
- Support reduced motion preference
- Avoid common pitfalls from pitfalls.md
- Maintain high contrast without causing eye strain
```

## User Prompt Template

```
Generate a {component_name} using neobrutalism style.

**Context:**
- Platform: {web | mobile | flutter | react-native}
- Use case: {dashboard | card | button | poster | etc.}
- Content: {describe content}
- Color scheme: {high-contrast | neon | monochrome | custom}

**Requirements:**
- Follow neobrutalism principles (bold borders, high contrast)
- Include hover/focus states
- Ensure accessibility (contrast, screen reader)
- Embrace raw, unpolished aesthetic
```

## Example Prompts

### Example 1: Button Component

```
Generate a Button component using neobrutalism style.

**Context:**
- Platform: web (React + CSS)
- Use case: Primary CTA for brutalist portfolio
- Content: "HIRE ME" text
- Color scheme: high-contrast (black, white, yellow)

**Requirements:**
- Follow neobrutalism principles (bold borders, high contrast)
- Include hover/focus states (color swap, no smooth transitions)
- Ensure accessibility (contrast, screen reader)
- Embrace raw, unpolished aesthetic
```

### Example 2: Card Component

```
Generate a Card component using neobrutalism style.

**Context:**
- Platform: web (React + CSS)
- Use case: Project showcase card
- Content: Image, title, description, link
- Color scheme: neon (pink, green, black)

**Requirements:**
- Follow neobrutalism principles (thick borders, raw look)
- Include hover state (bold color change)
- Ensure accessibility (contrast, screen reader)
- Use geometric, brutalist shapes
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

### Neobrutalism Principles Applied
- Bold borders: {description}
- High contrast: {description}
- Raw aesthetic: {description}

### Pitfalls Avoided
- {list from pitfalls.md}
```
