# Quality Gate - Liquid Glass

## Checklist chất lượng

### Nội dung bắt buộc
- [ ] Core Principles < 300 từ
- [ ] Design Tokens đầy đủ (gradient, color, blur, radius, shadow, animation)
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
- [ ] Liquid effect không gây chóng mặt

### Documentation
- [ ] SKILL.md có TL;DR section
- [ ] Components.md có hình minh họa (nếu có)
- [ ] Platforms.md có guidance cụ thể per platform
- [ ] Example code có thể copy-paste và chạy được

## Evaluation Criteria

Agent được coi là đã áp dụng đúng skill khi:

1. **Design Tokens**: Sử dụng đúng CSS variables từ SKILL.md
2. **Liquid Effect**: Organic, flowing shapes (border-radius với values khác nhau)
3. **Glass**: Translucent với backdrop blur
4. **Gradient**: Multi-color gradients cho liquid look
5. **Animation**: Subtle liquid movement (nếu có)
6. **Accessibility**: Contrast đủ, liquid effect không gây chóng mặt

## Score

- 0-4 checklist: ❌ Fail
- 5-7 checklist: ⚠️ Needs Improvement
- 8-10 checklist: ✅ Pass
