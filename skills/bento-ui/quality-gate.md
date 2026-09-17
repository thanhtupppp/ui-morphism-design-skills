# Quality Gate - Bento UI

## Checklist chất lượng

### Nội dung bắt buộc
- [ ] Core Principles < 300 từ
- [ ] Design Tokens đầy đủ (grid, color, spacing, radius, gap)
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
- [ ] Grid layout responsive

### Documentation
- [ ] SKILL.md có TL;DR section
- [ ] Components.md có hình minh họa (nếu có)
- [ ] Platforms.md có guidance cụ thể per platform
- [ ] Example code có thể copy-paste và chạy được

## Evaluation Criteria

Agent được coi là đã áp dụng đúng skill khi:

1. **Design Tokens**: Sử dụng đúng CSS variables từ SKILL.md
2. **Grid System**: Modular grid layout (CSS Grid hoặc Flexbox)
3. **Spacing**: Consistent gaps và padding (8px base unit)
4. **Radius**: Moderate border radius (8-16px) cho cards
5. **Colors**: Clean, organized color palette per module
6. **Responsive**: Grid adapts cho mobile, tablet, desktop
7. **Accessibility**: Contrast đủ, focus states rõ, grid readable

## Score

- 0-4 checklist: ❌ Fail
- 5-7 checklist: ⚠️ Needs Improvement
- 8-10 checklist: ✅ Pass
