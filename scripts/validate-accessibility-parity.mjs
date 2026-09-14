#!/usr/bin/env node

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const styles = ['skeuomorphism', 'flat-design', 'neumorphism', 'material-design', 'glassmorphism', 'claymorphism', 'liquid-glass', 'aurora-ui', 'bento-ui', 'neobrutalism'];
const failures = [];
const read = (path) => { try { return readFileSync(path, 'utf8'); } catch { return null; } };
const requirePattern = (text, pattern, label) => { if (!text || !pattern.test(text)) failures.push(`${label}: missing ${pattern}`); };

const contract = read(join(root, 'references/accessibility-parity.md'));
requirePattern(contract, /Accessibility behavior is part of cross-platform parity/i, 'accessibility-parity.md purpose');
requirePattern(contract, /forced-colors: active/i, 'accessibility-parity.md forced colors');
requirePattern(contract, /reduced-motion/i, 'accessibility-parity.md reduced motion');
requirePattern(contract, /48 logical px|48 px/i, 'accessibility-parity.md target size');
requirePattern(contract, /state semantics|semantic cue/i, 'accessibility-parity.md semantic fallback');

for (const style of styles) {
  const dir = join(root, 'skills', style);
  const css = read(join(dir, 'example.css')) || '';
  const react = read(join(dir, 'example.tsx')) || '';
  const flutter = read(join(dir, 'example.flutter.dart')) || '';
  const native = read(join(dir, 'example.native.tsx')) || '';

  requirePattern(css, /:focus-visible/i, `${style}/example.css focus`);
  requirePattern(css, /@media\s*\(forced-colors:\s*active/i, `${style}/example.css forced colors`);
  requirePattern(css, /@media\s*\(prefers-reduced-motion/i, `${style}/example.css reduced motion`);
  requirePattern(css, /min-height\s*:/i, `${style}/example.css minimum geometry`);
  requirePattern(css, /44px|48px|target|min(?:imum)?[-_]?(?:size|height)|control-height/i, `${style}/example.css target-size policy`);

  if (['glassmorphism', 'liquid-glass', 'aurora-ui'].includes(style)) {
    requirePattern(css, /prefers-reduced-transparency|surface-fallback|background:\s*#(?:[0-9a-f]{3,8})/i, `${style}/example.css reduced-transparency fallback`);
  }

  requirePattern(react, /<button\b|<a\b|<input\b|<select\b|<textarea\b/i, `${style}/example.tsx semantic primitive`);
  requirePattern(react, /data-state|aria-(?:disabled|selected|pressed|busy|invalid)|disabled/i, `${style}/example.tsx state semantics`);
  requirePattern(react, /aria-labelledby|aria-label|<label\b|<h[1-6]\b/i, `${style}/example.tsx accessible naming`);

  requirePattern(flutter, /Button|TextButton|ElevatedButton|OutlinedButton|FilledButton|IconButton|TextField|Switch|Checkbox|Slider|NavigationBar|Tab/i, `${style}/example.flutter.dart native control`);
  requirePattern(flutter, /48|minimumSize|tap target|target size|MaterialTapTargetSize/i, `${style}/example.flutter.dart target size`);
  requirePattern(flutter, /LayoutBuilder|MediaQuery|Wrap|GridView|width/i, `${style}/example.flutter.dart responsive behavior`);

  requirePattern(native, /Pressable|TextInput|Switch|Slider/i, `${style}/example.native.tsx native control`);
  requirePattern(native, /accessibilityRole|accessibilityState/i, `${style}/example.native.tsx accessibility`);
  requirePattern(native, /minHeight:\s*48|minimum.*48|48px/i, `${style}/example.native.tsx target size`);
  requirePattern(native, /fallback|remove|without.*blur|without.*shadow/i, `${style}/example.native.tsx fallback`);
}

if (failures.length) {
  console.error(`Accessibility parity validation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  process.exit(1);
}
console.log(`Accessibility parity validation PASSED: ${styles.length} styles covered.`);
