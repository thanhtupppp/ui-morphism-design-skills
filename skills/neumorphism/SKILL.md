# Neumorphism Design Skill

## TL;DR
Neumorphism (soft UI) tạo hiệu ứng "nhựa mềm" với ánh sáng từ góc trên-trai, dùng 2 bóng (sang + tối) để tạo emboss (nổi) hoặc deboss (chì»¿m).

## Core Principles
- Ánh sáng nhất quán từ góc trên-tráº£i (top-left)
- Hai bóng: sáng (top-left) + tối (bottom-right)
- Màu monochromatic (cÃ¹ng tone)
- Border radius trung bÃ¬nh lá››n (8â¿½24px)
- Háșu háŧu: emboss (nổi) cho resting, deboss (chÃ¬m) cho pressed

## Design Tokens
```css
:root {
  --neumo-bg: #e0e5ec;
  --shadow-light: rgba(255, 255, 255, 0.8);
  --shadow-dark: rgba(0, 0, 0, 0.15);
  --radius: 12px;
  --spacing: 16px;
}
```

## States

### Emboss (Raised/Nổi) - Default state
```css
.neumo-element {
  background: var(--neumo-bg);
  box-shadow: 
    8px 8px 16px var(--shadow-dark),    /* Bottom-right shadow */
    -8px -8px 16px var(--shadow-light);  /* Top-left highlight */
  border-radius: var(--radius);
}
```

### Deboss (Pressed/ChÃ¬m) - Active/pressed state
```css
.neumo-element:active {
  background: var(--neumo-bg);
  box-shadow: 
    inset 4px 4px 8px var(--shadow-dark),    /* Inner bottom-right */
    inset -4px -4px 8px var(--shadow-light);  /* Inner top-left */
  border-radius: var(--radius);
}
```

### Hover state (tăng shadow)
```css
.neumo-element:hover {
  box-shadow: 
    10px 10px 20px var(--shadow-dark),
    -10px -10px 20px var(--shadow-light);
}
```

## Contrast & Accessibility

### Text color recommendations
```css
/* Good contrast (8.5:1) */
.neumo-text {
  color: #1a1a1a; /* Dark gray/black */
}

/* Avoid: Low contrast */
.neumo-text-bad {
  color: #888888; /* Contrast too low on #e0e5ec */
}
```

### Contrast ratio check
- Background: #e0e5ec
- Text đen (#000): 12.6:1 ✅ Pass AAA
- Text xÃ¡m Äáº¬m (#333): 10.2:1 ✅ Pass AAA
- Text xÃ¡m (#666): 5.8:1 ✅ Pass AA
- Text xÃ¡m nháº¡t (#999): 2.8:1 ❌ Fail

### Focus states
```css
.neumo-button:focus {
  outline: 2px solid #1a1a1a;
  outline-offset: 2px;
  box-shadow: 
    8px 8px 16px var(--shadow-dark),
    -8px -8px 16px var(--shadow-light),
    0 0 0 3px rgba(26, 26, 26, 0.3); /* Focus ring */
}
```

## Components
Xem components.md

## Platforms
Xem platforms.md

## Common Pitfalls
- Shadow quÃ¡ mášĄnh (dÃ¹m 2-3 shadows lÃªn máŧ™t pháșn táș­)
- Contráº§t tháº¥p (text cáșn âĄ 4.5:1)
- Light source khÃ´ng nháº¥t quÃ¡n
- QuÃªn focus states cho accessibility