---
name: glassmorphism
description: Surface kính mờ bằng transparency, border sáng và backdrop blur.
---
# Glassmorphism

## Dùng khi
- Landing page, modal, overlay, player, dashboard có nền giàu màu.

## Quy tắc
- Blur chỉ nằm trong card/modal, không phủ toàn viewport.
- Tăng opacity hoặc dùng opaque fallback khi nền sau làm khó đọc.
- Không lồng nhiều backdrop-filter.

```css
.glass { background:rgb(255 255 255 / .14); border:1px solid rgb(255 255 255 / .28); backdrop-filter:blur(16px); }
```

## Checklist
- [ ] Có fallback `@supports`
- [ ] Test FPS mobile