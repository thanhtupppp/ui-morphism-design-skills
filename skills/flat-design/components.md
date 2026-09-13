# Flat Design — Component Anatomy & Recipes

Flat Design means that hierarchy comes from **semantic color, typography, spacing, alignment, grouping, borders, and explicit states** rather than simulated physical depth. A beginner should be able to remove all shadows from a screen and still understand what is a button, field, card, selected item, error, disabled item, and navigation location.

## 1. Visual anatomy

A flat interface is built in this order:

1. Page background.
2. Content container and spacing rhythm.
3. Typography hierarchy.
4. Surface grouping.
5. Functional boundaries such as borders or separators.
6. Semantic colors.
7. Interaction states.
8. Small optional elevation only where it improves grouping.

### Recognition test
A beginner should recognize:

- **Button:** a clearly bounded action with a verb or understandable icon.
- **Input:** a writable region with a persistent label and visible focus/error treatment.
- **Card:** a grouped content region, not automatically an interactive target.
- **Navigation:** a location selector with a persistent active cue.
- **Alert:** a semantic message with icon/text and an appropriate action.
- **Disabled control:** visibly unavailable and not merely light gray text.
- **Selected control:** selected through more than color alone.

## 2. Design tokens

```css
:root {
  --flat-bg: #f7f8fa;
  --flat-surface: #ffffff;
  --flat-surface-subtle: #f1f5f9;
  --flat-surface-strong: #e2e8f0;
  --flat-ink: #18202a;
  --flat-muted: #52606d;
  --flat-border: #cbd5e1;
  --flat-border-strong: #64748b;
  --flat-primary: #2563eb;
  --flat-primary-hover: #1d4ed8;
  --flat-primary-active: #1e40af;
  --flat-success: #15803d;
  --flat-warning: #a16207;
  --flat-danger: #b91c1c;
  --flat-info: #0369a1;
  --flat-focus: #1d4ed8;
  --flat-on-primary: #ffffff;
  --flat-radius-sm: 6px;
  --flat-radius-md: 8px;
  --flat-radius-lg: 12px;
  --flat-control-height: 44px;
  --flat-spacing-1: 4px;
  --flat-spacing-2: 8px;
  --flat-spacing-3: 12px;
  --flat-spacing-4: 16px;
  --flat-spacing-5: 20px;
  --flat-spacing-6: 24px;
  --flat-spacing-8: 32px;
  --flat-shadow-1: 0 1px 2px rgb(0 0 0 / .08);
}
```

Tokens are semantic. Do not scatter literal colors across components. A dark theme should replace roles, not redesign every component.

### 2.1 Theme profiles

The theme contract changes **semantic roles only**. Component structure, state selectors, spacing relationships, and interaction behavior remain unchanged.

```css
:root,
[data-theme="light"] {
  --flat-bg: #f7f8fa;
  --flat-surface: #ffffff;
  --flat-surface-subtle: #f1f5f9;
  --flat-surface-strong: #e2e8f0;
  --flat-ink: #18202a;
  --flat-muted: #52606d;
  --flat-border: #cbd5e1;
  --flat-border-strong: #64748b;
  --flat-primary: #2563eb;
  --flat-primary-hover: #1d4ed8;
  --flat-primary-active: #1e40af;
  --flat-success: #15803d;
  --flat-warning: #a16207;
  --flat-danger: #b91c1c;
  --flat-info: #0369a1;
  --flat-focus: #1d4ed8;
  --flat-on-primary: #ffffff;
}

[data-theme="dark"] {
  --flat-bg: #0f172a;
  --flat-surface: #111827;
  --flat-surface-subtle: #1e293b;
  --flat-surface-strong: #334155;
  --flat-ink: #f8fafc;
  --flat-muted: #cbd5e1;
  --flat-border: #475569;
  --flat-border-strong: #94a3b8;
  --flat-primary: #60a5fa;
  --flat-primary-hover: #93c5fd;
  --flat-primary-active: #3b82f6;
  --flat-success: #4ade80;
  --flat-warning: #facc15;
  --flat-danger: #f87171;
  --flat-info: #38bdf8;
  --flat-focus: #93c5fd;
  --flat-on-primary: #0f172a;
}
```

The dark profile is role-based rather than a mechanical color inversion. Verify text, borders, controls, and semantic feedback independently for contrast.

### 2.2 Density profiles

Density changes spacing and component geometry while preserving the minimum accessible hit area. `compact` is intended for information-dense layouts; it must not create undersized touch targets.

```css
:root,
[data-density="standard"] {
  --flat-control-height: 44px;
  --flat-density-padding: 16px;
  --flat-density-gap: 12px;
  --flat-density-row: 44px;
}

[data-density="comfortable"] {
  --flat-control-height: 48px;
  --flat-density-padding: 20px;
  --flat-density-gap: 16px;
  --flat-density-row: 48px;
}

[data-density="compact"] {
  --flat-control-height: 44px;
  --flat-density-padding: 12px;
  --flat-density-gap: 8px;
  --flat-density-row: 44px;
}
```

Do not use density to reduce keyboard/touch target size below the platform accessibility requirement. Compact mode should reduce whitespace before reducing interactive affordance.

## 3. Typography

Use typography as the primary depth system:

- Display/hero: high emphasis, short content.
- Heading: section hierarchy.
- Body: default reading text.
- Label: control identification.
- Supporting/meta: secondary information, never critical meaning alone.
- Caption: non-critical supplementary information.

Rules:

- Keep labels persistent for forms.
- Use weight, size, line-height, and spacing before adding decoration.
- Do not use uppercase, italics, or bold on everything.
- Allow text to wrap; never depend on fixed card/button heights for localized copy.

## 4. Buttons

### Primary
Strong semantic fill, clear label, no required shadow.

### Secondary
Lower visual emphasis, usually outlined or neutral-filled.

### Tertiary/Ghost
Minimal surface treatment but still an obvious hit area and hover/focus cue.

### Destructive
Uses semantic danger role and confirmation when the action is irreversible.

### States
Every button has:

- default
- hover (web/pointer)
- pressed/active
- focus-visible
- disabled
- loading when applicable

```css
.flat-button {
  min-height: var(--flat-control-height);
  padding: 10px 16px;
  border: 1px solid transparent;
  border-radius: var(--flat-radius-md);
  background: var(--flat-primary);
  color: var(--flat-on-primary);
  font: inherit;
  font-weight: 650;
  cursor: pointer;
}
```

## 5. Component recipes

The remaining component recipes use the same semantic tokens and inherit the active theme/density profile. Do not create separate dark or compact component classes unless a component has a documented structural reason.

### Card/panel
Use `--flat-surface`, `--flat-border`, and spacing tokens. Shadow is optional grouping only.

### Input/form field
Persistent label, visible border, explicit focus ring, and explicit error/success messaging. Do not communicate validation by color alone.

### Navigation/toolbar
Use semantic navigation landmarks and a persistent active cue such as text weight, indicator, icon treatment, or border in addition to color.

### Table/data grid
Prefer stable row geometry, visible column relationships, semantic headers, and horizontal overflow only when necessary. Never clip critical data to force a desktop table into a narrow viewport.

### Dialog/alert/banner
Use semantic dialog/alert roles where applicable, clear heading/message/action relationships, and a focus treatment independent of background decoration.

### Tabs
Use native or correctly mapped tab semantics. Selected state must remain understandable without color alone.

### Progress/status
Expose a machine-readable value/label where applicable. Pair semantic color with text/icon/state labels.

## 6. State contract

Every interactive component should define: default, hover where supported, focus-visible, pressed/active, selected where applicable, disabled, loading where applicable, and error/success where applicable. Removing color, shadow, animation, and decoration must not erase the state distinction.

## 7. Responsive contract

Validate compact phone (~375px), tablet (~768px), desktop (~1024px), and wide desktop (~1440px). Prefer wrapping and content-driven sizing over fixed coordinates. Localization and text scaling must not clip controls.

## 8. Accessibility contract

- Body text target contrast: 4.5:1; large text: 3:1.
- Focus must be visible and not rely on color alone.
- Interactive targets must remain platform-appropriate; web examples use at least 44px and Flutter targets at least 48 logical pixels.
- Labels and errors must be programmatically associated.
- Keyboard, screen-reader, zoom, and forced-colors behavior must remain usable.

## 9. Motion and fallback

Flat Design does not require animation. Respect `prefers-reduced-motion`. Optional shadow/elevation must degrade to borders/grouping without changing meaning.

## 10. Implementation rule

When adapting Flat Design across platforms, preserve semantic roles, states, hierarchy, density intent, and accessibility behavior. Pixel-perfect parity is not required; semantic parity is.
