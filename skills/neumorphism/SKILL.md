---
name: neumorphism
description: Surface nổi/lõm từ cùng màu nền bằng cặp shadow; dùng chọn lọc.
---
# Neumorphism

## Dùng khi
- Widget thermostat, smart-home, media control, quick action.

## Quy tắc
- Raised = có thể bấm; inset = input/active.
- Bổ sung label hoặc border khi shadow thiếu contrast.
- Không dùng toàn màn hình, form, data-grid, cảnh báo nguy hiểm.

```css
.neo-raised { background:#e8edf5; box-shadow:-8px -8px 16px #fff,8px 8px 16px #c3cad6; }
```

## Checklist
- [ ] Focus ring rõ
- [ ] Contrast text/icon đạt yêu cầu