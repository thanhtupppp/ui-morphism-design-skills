#!/usr/bin/env node

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const styles = ['skeuomorphism', 'flat-design', 'neumorphism', 'material-design', 'glassmorphism', 'claymorphism', 'liquid-glass', 'aurora-ui', 'bento-ui', 'neobrutalism'];
const failures = [];
const read = (path) => { try { return readFileSync(path, 'utf8'); } catch { return null; } };
const fail = (message) => failures.push(message);
const requirePattern = (text, pattern, label) => { if (!text || !pattern.test(text)) fail(`${label}: missing ${pattern}`); };
const escapeRegex = (value) => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

requirePattern(read(join(root, 'references/semantic-parity.md')), /Accessibility parity|accessibility meaning/i, 'semantic-parity.md accessibility parity');
requirePattern(read(join(root, 'references/accessibility-parity.md')), /semantic cue|state semantics/i, 'accessibility-parity.md');

for (const style of styles) {
  const dir = join(root, 'skills', style);
  const prefix = `--um-${style}-`;
  const escapedPrefix = escapeRegex(prefix);
  const css = read(join(dir, 'example.css')) || '';
  const react = read(join(dir, 'example.tsx')) || '';
  const flutter = read(join(dir, 'example.flutter.dart')) || '';
  const native = read(join(dir, 'example.native.tsx')) || '';
  const contract = `${css}\n${react}\n${flutter}\n${native}`;

  requirePattern(css, new RegExp(`${escapedPrefix}[a-z0-9-]+\\s*:`), `${style}/example.css token definition`);
  requirePattern(css, new RegExp(`var\\(${escapedPrefix}`), `${style}/example.css token consumption`);
  requirePattern(react, /<button\b|<a\b|<input\b|<select\b|<textarea\b/i, `${style}/example.tsx semantic primitive`);
  requirePattern(flutter, /Button|TextButton|ElevatedButton|OutlinedButton|FilledButton|IconButton|TextField|Switch|Checkbox|Slider|NavigationBar|Tab/i, `${style}/example.flutter.dart native primitive`);
  requirePattern(native, /Pressable|TextInput|Switch|Slider/i, `${style}/example.native.tsx native primitive`);
  requirePattern(contract, /disabled|pressed|selected|loading|error/i, `${style} state contract`);
  requirePattern(contract, /responsive|LayoutBuilder|MediaQuery|useWindowDimensions|flexDirection|grid|width/i, `${style} responsive contract`);
  requirePattern(contract, /44|48|minHeight|minWidth|target/i, `${style} target-size contract`);
  requirePattern(contract, /fallback|remove|unsupported|without.*blur|without.*shadow/i, `${style} fallback contract`);
  requirePattern(contract, /Verification:/i, `${style} verification record`);
}

if (failures.length) {
  console.error(`Semantic parity validation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  process.exit(1);
}
console.log(`Semantic parity validation PASSED: ${styles.length} styles covered.`);
