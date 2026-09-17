# Quality Gate - Material Design

## Checklist chất lượng

### Nội dung bắt buộc
- [ ] Core Principles < 300 từ
- [ ] Design Tokens đầy đủ (color, typography, elevation, shape, motion)
- [ ] 5+ components với ví dụ code
- [ ] 2+ platform examples (web, mobile, Flutter)
- [ ] Versioning (M2 vs M3)
- [ ] Accessibility section
- [ ] Evaluation Criteria

### Code quality
- [ ] Ví dụ CSS có comment giải thích
- [ ] Ví dụ React/TypeScript có type definitions
- [ ] Ví dụ Flutter có widget riêng
- [ ] Ví dụ React Native có StyleSheet
- [ ] Elevation system đúng spec

### Accessibility
- [ ] Contrast ratio >= 4.5:1 cho text
- [ ] Focus states rõ ràng
- [ ] Touch targets >= 48x48dp
- [ ] Screen reader friendly
- [ ] Motion preferences respected

### Documentation
- [ ] SKILL.md có TL;DR section
- [ ] Components.md có hình minh họa (nếu có)
- [ ] Platforms.md có guidance cụ thể per platform
- [ ] Example code có thể copy-paste và chạy được
- [ ] Elevation.md có bảng shadow levels
- [ ] Versioning.md so sánh M2 vs M3

## Evaluation Criteria

Agent được coi là đã áp dụng đúng skill khi:

1. **Design Tokens**: Sử dụng đúng variables từ SKILL.md hoặc tokens chính thức
2. **Elevation**: Đúng shadow levels (0-5 cho M3, 0-24 cho M2)
3. **Typography**: Đúng scale (15 styles cho M3, 13 cho M2)
4. **Shape**: Đúng border radius (20px buttons, 12px cards cho M3)
5. **Color**: Đúng tonal palette (primary, secondary, tertiary containers)
6. **Accessibility**: Contrast đủ, touch targets đúng, focus states rõ
7. **Version Consistency**: Không mix M2 + M3 trong cùng 1 component

## Score

- 0-4 checklist: ❌ Fail
- 5-7 checklist: ⚠️ Needs Improvement
- 8-10 checklist: ✅ Pass
