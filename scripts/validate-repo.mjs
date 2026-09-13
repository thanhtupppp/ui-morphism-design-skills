#!/usr/bin/env node

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const stylesRoot = join(root, 'skills');
const requiredFiles = ['SKILL.md', 'components.md', 'platforms.md', 'example.css', 'example.tsx', 'example.flutter.dart'];
const expectedStyles = ['skeuomorphism', 'flat-design', 'neumorphism', 'material-design', 'glassmorphism', 'claymorphism', 'liquid-glass', 'aurora-ui', 'bento-ui', 'neobrutalism'];
const requiredTokenGroups = ['surface|bg', 'ink|text', 'border', 'accent|primary', 'radius', 'space|spacing', 'focus', 'target|touch'];
const requiredStates = ['default', 'hover', 'active|pressed', 'disabled', 'focus'];
const failures = [];
const warnings = [];

const fail = (message) => failures.push(message);
const warn = (message) => warnings.push(message);
const read = (path) => { try { return readFileSync(path, 'utf8'); } catch { return null; } };
const requireText = (path, patterns, label) => {
  const text = read(path);
  if (text === null) { fail(`${label}: missing or unreadable file`); return null; }
  for (const pattern of patterns) if (!pattern.test(text)) fail(`${label}: missing required pattern ${pattern}`);
  return text;
};
const hasAny = (text, pattern) => pattern.test(text || '');

if (!existsSync(stylesRoot)) fail('skills/: missing');
const actualStyles = existsSync(stylesRoot) ? readdirSync(stylesRoot, { withFileTypes: true }).filter(e => e.isDirectory()).map(e => e.name).filter(n => !n.startsWith('.')).sort() : [];
if (actualStyles.length !== expectedStyles.length) fail(`skills/: expected ${expectedStyles.length} style directories, found ${actualStyles.length}`);

for (const style of expectedStyles) {
  const dir = join(stylesRoot, style);
  if (!existsSync(dir)) { fail(`${style}: missing style directory`); continue; }
  for (const file of requiredFiles) if (!existsSync(join(dir, file))) fail(`${style}: missing ${file}`);

  const skill = requireText(join(dir, 'SKILL.md'), [/accessib/i, /responsive|adaptive/i, /fallback/i], `${style}/SKILL.md`);
  const components = requireText(join(dir, 'components.md'), [/Button/i, /Card|Panel/i, /Input|Form/i, /state/i], `${style}/components.md`);
  const platforms = requireText(join(dir, 'platforms.md'), [/HTML|CSS/i, /React/i, /Flutter/i, /React Native|other renderer|Other UI/i, /fallback/i, /performance/i], `${style}/platforms.md`);
  const css = read(join(dir, 'example.css'));
  const tsx = read(join(dir, 'example.tsx'));
  const dart = read(join(dir, 'example.flutter.dart'));

  if (components) {
    for (const group of requiredTokenGroups) if (!new RegExp(`(?:--(?:um-)?${group.split('|')[0]}|${group})`, 'i').test(components)) warn(`${style}/components.md: token group ${group} not detected; verify semantic token coverage.`);
    for (const state of requiredStates) if (!new RegExp(`\\b(?:${state})\\b`, 'i').test(components)) warn(`${style}/components.md: state ${state} not explicitly documented.`);
  }
  if (css) {
    if (!/focus-visible/i.test(css)) warn(`${style}/example.css: no :focus-visible marker found.`);
    if (!/prefers-reduced-motion|reduced.?motion/i.test(css)) warn(`${style}/example.css: reduced-motion handling not detected.`);
    if (!/min-(?:height|width)|min-height|min-width/i.test(css)) warn(`${style}/example.css: no explicit minimum control geometry detected.`);
    if (/--(?:glass|neo|clay|liquid|aurora|bento|brutal)-/i.test(css) && !/--um-/i.test(css)) fail(`${style}/example.css: legacy/short token namespace detected without --um- namespace.`);
  }
  if (tsx) {
    if (/<(?:div|span)[^>]+(?:onClick|onKeyDown|role=["']button)/i.test(tsx)) fail(`${style}/example.tsx: non-semantic interactive element detected.`);
    if (!/<button\b|<a\b|<input\b|<select\b|<textarea\b/i.test(tsx)) warn(`${style}/example.tsx: no obvious native interactive element detected.`);
    if (/role=["']button["']/i.test(tsx) && !/tabIndex/i.test(tsx)) warn(`${style}/example.tsx: custom button role should expose keyboard focus behavior.`);
  }
  if (dart && !/Semantics|Button|TextField|Switch|Checkbox|Slider|Navigation|Tab/i.test(dart)) warn(`${style}/example.flutter.dart: semantic/native interactive primitive not detected.`);
  if (platforms && !/React Native/i.test(platforms) && !/other renderer/i.test(platforms)) warn(`${style}/platforms.md: React Native/other-renderer adapter guidance not explicit.`);
}

const skillJson = read(join(root, 'skill.json'));
if (skillJson === null) fail('skill.json: missing or unreadable');
else try {
  const parsed = JSON.parse(skillJson);
  const declared = Array.isArray(parsed.styles) ? parsed.styles.map(s => typeof s === 'string' ? s : s.path ?? s.id ?? s.name).filter(Boolean).map(String) : [];
  if (declared.length !== expectedStyles.length) fail(`skill.json: expected ${expectedStyles.length} styles, found ${declared.length}`);
  expectedStyles.forEach((style, index) => {
    if (declared[index] !== style) fail(`skill.json: style order mismatch at index ${index}: expected ${style}, found ${declared[index] ?? '<missing>'}`);
  });
} catch (error) { fail(`skill.json: invalid JSON (${error.message})`); }

for (const reference of ['references/component-code-contract.md', 'references/platform-contract.md', 'references/platform-matrix.md', 'references/review-checklist.md', 'references/token-convention.md']) if (!existsSync(join(root, reference))) fail(`${reference}: missing repository contract`);

const tokenConvention = read(join(root, 'references/token-convention.md'));
if (tokenConvention && !/--um-<style>-<group>/i.test(tokenConvention)) warn('token-convention.md: canonical namespace grammar not detected.');

const readme = read(join(root, 'README.md'));
if (readme) for (const style of expectedStyles) if (!new RegExp(style, 'i').test(readme)) warn(`README.md: style ${style} is not mentioned.`);

if (failures.length) {
  console.error(`\nValidation FAILED: ${failures.length} error(s)`);
  failures.forEach(f => console.error(`- ${f}`));
  if (warnings.length) { console.error(`\nWarnings: ${warnings.length}`); warnings.forEach(w => console.error(`- ${w}`)); }
  process.exit(1);
}
console.log(`Validation PASSED: ${expectedStyles.length} styles checked.`);
if (warnings.length) { console.log(`Warnings: ${warnings.length}`); warnings.forEach(w => console.log(`- ${w}`)); }
