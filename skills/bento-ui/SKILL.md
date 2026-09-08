---
name: bento-ui
description: Card grid modular, hierarchy rõ và responsive.
---
# Bento UI

## Dùng khi
- Homepage, dashboard tổng quan, portfolio, analytics, feature discovery.

## Quy tắc
- Mỗi card trả lời một câu hỏi hoặc action chính.
- Card lớn chỉ dành cho nội dung ưu tiên.
- Mobile-first: một cột trước, tăng span ở breakpoint lớn.

```css
.bento { display:grid; gap:var(--space-4); grid-template-columns:repeat(12,minmax(0,1fr)); }
.bento > * { grid-column:span 4; }
@media (max-width:768px) { .bento { grid-template-columns:1fr; } .bento > * { grid-column:auto; } }
```

## Checklist
- [ ] DOM order hợp lý trên mobile
- [ ] Không cắt text khi localization