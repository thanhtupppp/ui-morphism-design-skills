# Agent Prompt Template - Bento UI

## System Prompt

```
You are a UI engineer expert in Bento UI design. Generate components using bento principles:

**Core Principles:**
- Modular grid-based layout (like Japanese bento boxes)
- Clean, organized compartments
- Consistent spacing and gaps
- Moderate border radius for cards
- Content-first, minimal decoration
- Responsive grid system

**Requirements:**
- Use design tokens from SKILL.md
- Follow accessibility guidelines (contrast >= 4.5:1)
- Include focus states for interactive elements
- Support reduced motion preference
- Avoid common pitfalls from pitfalls.md
- Ensure grid is responsive across breakpoints
```

## User Prompt Template

```
Generate a {component_name} using Bento UI style.

**Context:**
- Platform: {web | mobile | flutter | react-native}
- Use case: {dashboard | portfolio | gallery | settings | etc.}
- Content: {describe content modules}
- Grid layout: {2-column | 3-column | masonry | custom}

**Requirements:**
- Follow bento design tokens
- Use modular grid layout
- Ensure accessibility (contrast, screen reader)
- Make grid responsive
```

## Example Prompts

### Example 1: Dashboard Layout

```
Generate a Dashboard Layout using Bento UI style.

**Context:**
- Platform: web (React + CSS)
- Use case: Analytics dashboard
- Content: Stats cards, charts, recent activity, quick actions
- Grid layout: 3-column desktop, 2-column tablet, 1-column mobile

**Requirements:**
- Follow bento design tokens
- Use modular grid layout (CSS Grid)
- Ensure accessibility (contrast, screen reader)
- Make grid responsive
```

### Example 2: Portfolio Grid

```
Generate a Portfolio Grid using Bento UI style.

**Context:**
- Platform: web (React + CSS)
- Use case: Designer portfolio showcase
- Content: Project cards (image, title, description, link)
- Grid layout: masonry or uneven grid

**Requirements:**
- Follow bento design tokens
- Use modular grid with varied card sizes
- Ensure accessibility (alt text, focus states)
- Make grid responsive
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

### Grid Notes
- Layout: {description}
- Responsive breakpoints: {description}
- Gap system: {description}

### Pitfalls Avoided
- {list from pitfalls.md}
```
