# Semantic Parity Contract

## Purpose

A style is cross-platform only when its examples preserve the same semantic anatomy, interaction states, responsive intent, target size, and fallback behavior across HTML/CSS, React, Flutter, and React Native.

## Canonical checks

For every style, the implementation seeds must expose:

- a canonical `--um-<style>-...` semantic token namespace in CSS;
- at least one token definition and one `var(--um-<style>-...)` consumption;
- a native/semantic interactive primitive;
- an explicit disabled/pressed/selected/loading/error state marker or documented equivalent;
- responsive adaptation based on available width or layout constraints;
- a primary interactive target of at least 44 CSS px on web and 48 logical px on React Native/Flutter;
- a deterministic fallback that preserves content hierarchy and semantic state when decorative effects are unavailable.

## Parity rule

Visual details may differ by renderer. Semantic role, content order, state meaning, responsive intent, accessibility behavior, and minimum target size must not silently diverge.

## Verification record

Every style seed must retain a short `Verification:` note describing the parity checks performed. Fallback notes must identify which decorative effect can be removed and what remains.
