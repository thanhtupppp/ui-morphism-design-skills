# Quality Gate - Flat Design

## Checklist chất lượng

### Nội dung bắt buộc
- [ ] Core Principles < 300 từ
- [ ] Design Tokens đầy đủ (color, spacing, radius, typography)
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
- [ ] Color không dùng làm indicator duy nhất

### Documentation
- [ ] SKILL.md có TL;DR section
- [ ] Components.md có hình minh họa (nếu có)
- [ ] Platforms.md có guidance cụ thể per platform
- [ ] Example code có thể copy-paste và chạy được

## Evaluation Criteria

Agent được coi là đã áp dụng đúng skill khi:

1. **Design Tokens**: Sử dụng đúng CSS variables từ SKILL.md
2. **No Depth Effects**: Không dùng gradient, shadow, bevel, emboss
3. **Bold Colors**: Màu sắc tươi sáng, tương phản cao
4. **Simple Shapes**: Hình học cơ bản (vuong, tròn, tam giác)
5. **Typography**: Sans-serif, clean, readable
6. **Minimalism**: Loại bỏ chi tiết thừa, tập trung content
7. **Accessibility**: Contrast đủ, focus states rõ, color không phải indicator duy nhất

## Score

- 0-4 checklist: ❌ Fail
- 5-7 checklist: ⚠️ Needs Improvement
- 8-10 checklist: ✅ Pass
