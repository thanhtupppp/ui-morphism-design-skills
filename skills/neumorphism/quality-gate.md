# Quality Gate - Neumorphism

## Checklist chất lượng

### Nội dung bắt buộc
- [ ] Core Principles < 300 từ
- [ ] Design Tokens đầy đủ (color, spacing, radius, shadow-light, shadow-dark)
- [ ] 5+ components với ví dụ code
- [ ] 2+ platform examples (web, mobile, Flutter)
- [ ] Accessibility section
- [ ] Pitfalls section
- [ ] Evaluation Criteria

### Code quality
- [ ] Ví dụ CSS có comment giải thích
- [ ] Ví dụ React/TypeScript có type definitions
- [ ] Ví dụ Flutter có widget riêng
- [ ] Ví dụ React Native có StyleSheet

### Accessibility
- [ ] Contrast ratio >= 4.5:1 cho text
- [ ] Focus states rõ ràng
- [ ] Reduced motion support
- [ ] Screen reader friendly
- [ ] Performance optimization (avoid excessive shadows)

### Documentation
- [ ] SKILL.md có TL;DR section
- [ ] Components.md có hình minh họa (nếu có)
- [ ] Platforms.md có guidance cụ thể per platform
- [ ] Example code có thể copy-paste và chạy được

## Evaluation Criteria

Agent được coi là đã áp dụng đúng skill khi:

1. **Design Tokens**: Sử dụng đúng CSS variables từ SKILL.md
2. **Light Source**: Shadow direction consistent (top-left light: shadow-dark bottom-right, shadow-light top-left)
3. **Colors**: Same or similar hue for background and element (monochromatic)
4. **Shadows**: Two shadows (light + dark) tạo emboss/deboss effect
5. **Border Radius**: Moderate to large (8-24px) cho soft look
6. **Accessibility**: Contrast đủ, focus states rõ, performance optimized

## Score

- 0-4 checklist: ❌ Fail
- 5-7 checklist: ⚠️ Needs Improvement
- 8-10 checklist: ✅ Pass
