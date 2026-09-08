# Token Convention

## Namespace

All shared design tokens use this grammar:

```text
--um-<style>-<group>[-<variant>]
```

Examples:

```css
--um-glassmorphism-surface-1
--um-glassmorphism-blur-2
--um-neumorphism-shadow-press
--um-liquid-glass-radius-pill
--um-bento-ui-space-4
```

Use the full style name. Do not create short aliases such as `--glass-*` or `--nm-*` inside a reusable skill because aliases collide when multiple styles are previewed in one application.

## Shared groups

- `bg`, `surface`, `ink`, `border`, `accent`, `danger`
- `radius`, `shadow`, `elev`, `blur`, `saturate`
- `space`, `font`, `text`, `weight`, `leading`, `tracking`
- `dur`, `ease`, `focus`, `target`

## Accessibility contract

- `border` may be decorative; `border-strong` is the interactive boundary and must be independently visible.
- `focus` must not depend only on `box-shadow`; provide an outline or border fallback for forced-colors mode.
- Every style exposes a `target-min` token. Use at least 24 CSS pixels as a floor and prefer 44px for primary controls.
- Translucent styles expose an opaque fallback surface token.

## Theme contract

Define tokens on bare `:root`. Put system dark-mode overrides behind `:root:not([data-theme="light"])`, and put explicit dark overrides under `:root[data-theme="dark"]`. Explicit user choice must win over OS preference.

```css
:root {
  color-scheme: light dark;
  --um-glassmorphism-surface-1: rgb(255 255 255 / 0.14);
  --um-glassmorphism-surface-fallback: #f7f8fa;
  --um-glassmorphism-border-strong: rgb(255 255 255 / 0.42);
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --um-glassmorphism-surface-fallback: #171923;
  }
}

:root[data-theme="dark"] {
  --um-glassmorphism-surface-fallback: #171923;
}
```

## Tailwind mapping

Map semantic groups mechanically to Tailwind namespaces: colors to `--color-*`, radius to `--radius-*`, shadows to `--shadow-*`, blur to `--blur-*`, spacing to `--spacing-*`, typography to `--text-*` and `--font-*`. Keep `@theme` top-level; theme switching belongs in ordinary selectors.
