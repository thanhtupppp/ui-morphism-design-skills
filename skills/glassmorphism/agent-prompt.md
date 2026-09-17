# Agent Prompt Template - Glassmorphism

## System Prompt

```
You are a UI engineer expert in Glassmorphism design. Generate components using glassmorphism principles:

**Core Principles:**
- Translucent backgrounds with backdrop blur
- Thin, subtle borders (1px, rgba(255,255,255,0.2-0.5))
- Soft shadows for depth
- Light, airy color palette
- Background blur effect (backdrop-filter: blur(10-20px))

**Requirements:**
- Use design tokens from SKILL.md
- Follow accessibility guidelines (contrast >= 4.5:1)
- Include focus states for interactive elements
- Support reduced motion preference
- Avoid common pitfalls from pitfalls.md
```

## User Prompt Template

```
Generate a {component_name} using glassmorphism style.

**Context:**
- Platform: {web | mobile | flutter | react-native}
- Use case: {dashboard | card | modal | navigation | etc.}
- Content: {describe content}

**Requirements:**
- Follow glassmorphism design tokens
- Include hover/focus states
- Ensure accessibility (contrast, screen reader)
- Provide responsive variants if needed
```

## Example Prompts

### Example 1: Card Component

```
Generate a Card component using glassmorphism style.

**Context:**
- Platform: web (React + CSS)
- Use case: Product card for e-commerce dashboard
- Content: Product image, title, price, rating, add-to-cart button

**Requirements:**
- Follow glassmorphism design tokens
- Include hover/focus states
- Ensure accessibility (contrast, screen reader)
- Provide responsive variants if needed
```

### Example 2: Modal Component

```
Generate a Modal component using glassmorphism style.

**Context:**
- Platform: web (React + CSS)
- Use case: Confirmation dialog for delete action
- Content: Warning icon, title, description, cancel button, confirm button

**Requirements:**
- Follow glassmorphism design tokens
- Include focus trap for accessibility
- Support keyboard navigation (Escape to close)
- Ensure backdrop blur effect on overlay
```

### Example 3: Navigation Bar

```
Generate a Navigation Bar using glassmorphism style.

**Context:**
- Platform: mobile (React Native)
- Use case: Bottom tab navigation for social app
- Content: 4-5 tab icons with labels

**Requirements:**
- Follow glassmorphism design tokens
- Include active/inactive states
- Ensure touch targets >= 44x44px
- Support safe area insets
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

### Pitfalls Avoided
- {list from pitfalls.md}
```
