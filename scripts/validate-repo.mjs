#!/usr/bin/env node

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const stylesRoot = join(root, 'skills');
const requiredFiles = [
  'SKILL.md',
  'components.md',
  'platforms.md',
  'example.css',
  'example.tsx',
  'example.flutter.dart',
];
const expectedStyles = [
  'skeuomorphism',
  'flat-design',
  'neumorphism',
  'material-design',
  'glassmorphism',
  'claymorphism',
  'liquid-glass',
  'aurora-ui',
  'bento-ui',
  'neobrutalism',
];

const failures = [];
const warnings = [];

function fail(message) {
  failures.push(message);
}

function warn(message) {
  warnings.push(message);
}

function read(path) {
  try {
    return readFileSync(path, 'utf8');
  } catch {
    return null;
  }
}

function requireText(path, patterns, label) {
  const text = read(path);
  if (text === null) {
    fail(`${label}: missing or unreadable file`);
    return;
  }
  for (const pattern of patterns) {
    if (!pattern.test(text)) fail(`${label}: missing required pattern ${pattern}`);
  }
}

if (!existsSync(stylesRoot)) fail('skills/: missing');

const actualStyles = existsSync(stylesRoot)
  ? readdirSync(stylesRoot, { withFileTypes: true })
      .filter((entry) => entry.isDirectory())
      .map((entry) => entry.name)
      .filter((name) => !name.startsWith('.'))
      .sort()
  : [];

for (const style of expectedStyles) {
  const dir = join(stylesRoot, style);
  if (!existsSync(dir)) {
    fail(`${style}: missing style directory`);
    continue;
  }
  for (const file of requiredFiles) {
    const path = join(dir, file);
    if (!existsSync(path)) fail(`${style}: missing ${file}`);
  }

  requireText(join(dir, 'SKILL.md'), [/accessib/i, /responsive|adaptive/i, /fallback/i], `${style}/SKILL.md`);
  requireText(join(dir, 'components.md'), [/Button/i, /Card|Panel/i, /Input|Form/i, /state/i], `${style}/components.md`);
  requireText(join(dir, 'platforms.md'), [/HTML|CSS/i, /React/i, /Flutter/i, /React Native|other renderer|Other UI/i, /fallback/i], `${style}/platforms.md`);

  const css = read(join(dir, 'example.css'));
  if (css && !/focus-visible/i.test(css)) warn(`${style}/example.css: no :focus-visible marker found; verify focus is implemented by another explicit mechanism.`);
  if (css && !/prefers-reduced-motion|reduced.?motion/i.test(css)) warn(`${style}/example.css: reduced-motion handling not detected.`);

  const tsx = read(join(dir, 'example.tsx'));
  if (tsx && /<div[^>]+onClick|<span[^>]+onClick/i.test(tsx)) fail(`${style}/example.tsx: possible div/span click control; use semantic interactive elements.`);
  if (tsx && !/<button\b|<a\b|<input\b|<select\b/i.test(tsx)) warn(`${style}/example.tsx: no obvious native interactive element detected.`);

  const dart = read(join(dir, 'example.flutter.dart'));
  if (dart && !/Semantics|Button|TextField|Switch|Checkbox|Slider|Navigation|Tab/i.test(dart)) warn(`${style}/example.flutter.dart: semantic/native interactive primitive not detected.`);
}

const unexpectedStyles = actualStyles.filter((style) => !expectedStyles.includes(style));
if (unexpectedStyles.length) warn(`Unexpected style directories: ${unexpectedStyles.join(', ')}`);

const skillJsonPath = join(root, 'skill.json');
const skillJson = read(skillJsonPath);
if (skillJson === null) {
  fail('skill.json: missing or unreadable');
} else {
  try {
    const parsed = JSON.parse(skillJson);
    const declared = Array.isArray(parsed.styles)
      ? parsed.styles.map((style) => typeof style === 'string' ? style : style.path ?? style.id ?? style.name).filter(Boolean)
      : [];
    for (const style of expectedStyles) {
      if (!declared.some((value) => String(value).includes(style))) fail(`skill.json: ${style} is not declared`);
    }
  } catch (error) {
    fail(`skill.json: invalid JSON (${error.message})`);
  }
}

for (const reference of [
  'references/component-code-contract.md',
  'references/platform-contract.md',
  'references/review-checklist.md',
]) {
  if (!existsSync(join(root, reference))) fail(`${reference}: missing repository contract`);
}

if (failures.length) {
  console.error(`\nValidation FAILED: ${failures.length} error(s)`);
  for (const failure of failures) console.error(`- ${failure}`);
  if (warnings.length) {
    console.error(`\nWarnings: ${warnings.length}`);
    for (const warning of warnings) console.error(`- ${warning}`);
  }
  process.exit(1);
}

console.log(`Validation PASSED: ${expectedStyles.length} style directories checked.`);
if (warnings.length) {
  console.log(`Warnings: ${warnings.length}`);
  for (const warning of warnings) console.log(`- ${warning}`);
}
