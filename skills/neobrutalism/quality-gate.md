# Quality Gate - Neobrutalism

## Checklist chất lượng

### Nội dung bắt buộc
- [ ] Core Principles < 300 từ
- [ ] Design Tokens đầy đủ (color, spacing, radius, border, shadow)
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
- [ ] High contrast không gây mỏi mắt

### Documentation
- [ ] SKILL.md có TL;DR section
- [ ] Components.md có hình minh họa (nếu có)
- [ ] Platforms.md có guidance cụ thể per platform
- [ ] Example code có thể copy-paste và chạy được

## Evaluation Criteria

Agent được coi là đã áp dụng đúng skill khi:

1. **Design Tokens**: Sử dụng đúng CSS variables từ SKILL.md
2. **Bold Borders**: Thick borders (2-4px), thường màu đen
3. **High Contrast**: Màu sắc tương phản mạnh (đen, trắng, neon)
4. **Raw Aesthetic**: Không polish, có thể "ugly on purpose"
5. **Geometric Shapes**: Vuong, chữ nhật, đôi khi méo có chủ đích
6. **Typography**: Bold, condensed, hoặc monospace
7. **Accessibility**: Contrast đủ, focus states rõ, high contrast không gây mỏi

## Score

- 0-4 checklist: ❌ Fail
- 5-7 checklist: ⚠️ Needs Improvement
- 8-10 checklist: ✅ Pass
