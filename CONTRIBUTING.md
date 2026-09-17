# Contributing to UI Morphism Design Skills

Cảm ơn bạn đã quan tâm đóng góp! Hướng dẫn này giúp bạn thêm skill mới hoặc cải thiện skill hiện có.

## Cấu trúc repository

```
ui-morphism-design-skills/
├── skills/
│   ├── {skill-id}/
│   │   ├── SKILL.md           # Required: Core principles & tokens
│   │   ├── components.md      # Required: Component examples
│   │   ├── platforms.md       # Required: Platform-specific guidance
│   │   ├── example.css        # Required: CSS example
│   │   ├── example.tsx        # Required: React example
│   │   ├── example.flutter.dart  # Optional: Flutter example
│   │   ├── example.native.tsx    # Optional: React Native example
│   │   ├── quality-gate.md    # Recommended: Quality checklist
│   │   ├── agent-prompt.md    # Recommended: Agent prompt template
│   │   ├── accessibility.md   # Recommended: Accessibility guide
│   │   ├── pitfalls.md        # Optional: Common mistakes
│   │   ├── elevation.md       # Optional: For Material Design
│   │   └── versioning.md      # Optional: Version comparison
│   └── ...
├── templates/
├── tests/
├── evals/
└── ...
```

## Thêm skill mới

### Bước 1: Tạo thư mục skill

```bash
mkdir -p skills/{skill-id}
cd skills/{skill-id}
```

### Bước 2: Tạo các file bắt buộc

1. **SKILL.md** - Nguyên lý cốt lõi & design tokens
   - TL;DR section (< 50 từ)
   - Core Principles (< 300 từ)
   - Design Tokens (color, spacing, radius, shadow, etc.)
   - Common Pitfalls
   - Evaluation Criteria

2. **components.md** - Ví dụ components
   - 5+ components phổ biến
   - Code examples cho mỗi component
   - Before/After (nếu có)

3. **platforms.md** - Hướng dẫn theo platform
   - Web (CSS, React)
   - Mobile (React Native, Flutter)
   - Platform-specific considerations

4. **example.css** - CSS example
   - Design tokens as CSS variables
   - 2-3 component implementations
   - Comments giải thích

5. **example.tsx** - React example
   - TypeScript với type definitions
   - 1-2 components hoàn chỉnh
   - Props interfaces

### Bước 3: Tạo các file khuyến nghị

6. **quality-gate.md** - Checklist chất lượng
   - Nội dung bắt buộc
   - Code quality
   - Accessibility
   - Documentation
   - Evaluation criteria
   - Score system

7. **agent-prompt.md** - Prompt template cho agent
   - System prompt
   - User prompt template
   - 3+ example prompts
   - Output format

8. **accessibility.md** - Accessibility guide
   - Contrast requirements
   - Focus states
   - Reduced motion
   - Screen reader support
   - Touch targets
   - Testing checklist

### Bước 4: Cập nhật skills-index.json

```json
{
  "id": "your-skill-id",
  "name": "Your Skill Name",
  "version": "1.0.0",
  "status": "active",
  "description": "Short description",
  "tags": ["tag1", "tag2", "tag3"]
}
```

### Bước 5: Submit PR

```bash
git add .
git commit -m "feat(skills): add {skill-id} skill"
git push origin main
```

Tạo Pull Request với:
- Title: `feat(skills): add {skill-id}`
- Description:
  - Skill name & description
  - Key characteristics
  - Example use cases
  - Screenshots (nếu có)

## Checklist chất lượng

Trước khi submit, đảm bảo skill của bạn:

- [ ] Core Principles < 300 từ
- [ ] Design Tokens đầy đủ
- [ ] 5+ components với code
- [ ] 2+ platform examples
- [ ] Accessibility section
- [ ] Evaluation Criteria
- [ ] Code examples chạy được
- [ ] Không vi phạm copyright
- [ ] Follow structure trong CONTRIBUTING.md

## Cải thiện skill hiện có

### Thêm file mới

```bash
cd skills/{skill-id}
touch quality-gate.md agent-prompt.md accessibility.md
```

Commit message:
```
docs({skill-id}): add quality-gate.md, agent-prompt.md, accessibility.md
```

### Cập nhật nội dung

1. Đọc file hiện tại
2. Xác định phần cần cải thiện
3. Edit và commit

Commit message format:
```
docs({skill-id}): improve {section} section
fix({skill-id}): correct {issue}
feat({skill-id}): add {new-component} examples
```

## Code Style

### Markdown
- Dùng `##` cho section headers
- Dùng `###` cho subsection headers
- Dùng bullet points (`-`) cho lists
- Code blocks với language specifier (```css, ```tsx)
- Links với descriptive text

### CSS
- CSS variables cho design tokens
- Comments giải thích complex styles
- Mobile-first responsive design
- Accessibility considerations

### TypeScript/React
- TypeScript với type definitions
- Functional components với hooks
- Props interfaces rõ ràng
- Comments cho complex logic

## Testing

### Manual Testing
1. Copy code examples vào project thực tế
2. Test trên multiple browsers/devices
3. Check accessibility với tools:
   - Chrome DevTools Lighthouse
   - axe DevTools
   - WebAIM Contrast Checker

### Agent Testing
1. Dùng agent-prompt.md templates
2. Generate components với AI agent
3. Verify output matches Evaluation Criteria

## Questions?

- Mở issue với label `question`
- Join discussion trong existing issues
- Check examples trong `skills/glassmorphism/`, `skills/neumorphism/`, `skills/material-design/`

## Resources

- [Antigravity Skills Format](https://github.com/sickn33/antigravity-awesome-skills)
- [Material Design Guidelines](https://material.io/design)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)

---

Cảm ơn bạn đã đóng góp! 🎨
