---
name: ui-morphism-design-router
description: Chọn và áp dụng phong cách UI morphism phù hợp với mục tiêu sản phẩm, accessibility và hiệu năng.
---

# UI Morphism Design Router

## Chọn nhanh

| Bối cảnh | Style ưu tiên |
|---|---|
| SaaS, ERP, dashboard IoT/HVAC | Flat hoặc Material + Bento |
| Landing page công nghệ/premium | Glass hoặc Aurora |
| Widget điều khiển đơn lẻ | Neumorphism hoặc Clay |
| Android/cross-platform quy mô lớn | Material Design |
| Portfolio, cộng đồng, brand táo bạo | Neobrutalism |
| UI mô phỏng thiết bị/vật lý | Skeuomorphism có giới hạn |

## Quy trình

1. Chọn một style chủ đạo và tối đa một accent style.
2. Đọc `skills/<style>/SKILL.md` trước khi code.
3. Khai báo design token; không hard-code shadow, blur hoặc radius rải rác.
4. Xây đủ default, hover, active, focus-visible, disabled, loading và error.
5. Test responsive, contrast, keyboard navigation, reduced motion và hiệu năng.

## Done

- Không dùng riêng màu để biểu đạt state.
- Focus ring rõ trên mọi background.
- Blur/motion có fallback và không làm giảm UX trên thiết bị yếu.