#!/usr/bin/env node

import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const styles = [
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
const read = (path) => {
  try {
    return readFileSync(path, 'utf8');
  } catch {
    return null;
  }
};
const fail = (message) => failures.push(message);
const mustContain = (text, pattern, label) => {
  if (!text || !pattern.test(text)) fail(`${label}: required quality-gate contract is missing.`);
};

console.log('UI Morphism Quality Gates v1.2.1');

const gatesPath = join(root, 'references/quality-gates.md');
const gates = read(gatesPath);
if (!gates) {
  fail('references/quality-gates.md: missing or unreadable.');
} else {
  mustContain(gates, /Gate A[\s\S]*semantics/i, 'quality-gates.md');
  mustContain(gates, /Gate B[\s\S]*responsive/i, 'quality-gates.md');
  mustContain(gates, /Gate C[\s\S]*motion/i, 'quality-gates.md');
  mustContain(gates, /Gate D[\s\S]*target size/i, 'quality-gates.md');
  mustContain(gates, /Gate E[\s\S]*material-effect budget/i, 'quality-gates.md');
  mustContain(gates, /Gate F[\s\S]*cross-platform equivalence/i, 'quality-gates.md');
  mustContain(gates, /Gate G[\s\S]*React Native adapter/i, 'quality-gates.md');
}

const skill = read(join(root, 'SKILL.md'));
mustContain(skill, /quality-gates\.md/i, 'SKILL.md');
mustContain(skill, /react-native-adapter\.md/i, 'SKILL.md');
mustContain(skill, /decision record[\s\S]*semantic token record[\s\S]*verification record/i, 'SKILL.md');

const componentContract = read(join(root, 'references/component-code-contract.md'));
if (!componentContract) {
  fail('references/component-code-contract.md: missing or unreadable.');
} else {
  for (const [name, pattern] of [
    ['decision record', /\*\*Decision record\*\*/i],
    ['semantic token record', /\*\*Semantic token record\*\*/i],
    ['component recipes', /\*\*Component recipes\*\*/i],
    ['platform mappings', /\*\*Platform mappings\*\*/i],
    ['responsive/adaptive rule', /\*\*Responsive\/adaptive rule\*\*/i],
    ['accessibility rule', /\*\*Accessibility rule\*\*/i],
    ['fallback rule', /\*\*Fallback rule\*\*/i],
    ['verification record', /\*\*Verification record\*\*/i],
    ['auditable output', /auditable/i],
    ['output invariants', /## Output invariants/i],
  ]) {
    mustContain(componentContract, pattern, `component-code-contract.md (${name})`);
  }
}

const adapter = read(join(root, 'references/react-native-adapter.md'));
if (!adapter) {
  fail('references/react-native-adapter.md: missing or unreadable.');
} else {
  for (const pattern of [
    /semantic-first mapping/i,
    /canonical token mapping/i,
    /native interaction primitives/i,
    /responsive adaptation/i,
    /accessibility/i,
    /performance and fallback/i,
  ]) mustContain(adapter, pattern, 'react-native-adapter.md');
}

const skillJson = read(join(root, 'skill.json'));
if (!skillJson) {
  fail('skill.json: missing or unreadable.');
} else {
  try {
    const parsed = JSON.parse(skillJson);
    if (parsed.version !== '1.4.0') {
      fail(`skill.json: expected contract version 1.4.0, found ${parsed.version ?? 'missing'}.`);
    }
    if (!Array.isArray(parsed.contracts) || !parsed.contracts.includes('references/quality-gates.md')) {
      fail('skill.json: quality-gates.md is not declared in contracts.');
    }
    if (!Array.isArray(parsed.contracts) || !parsed.contracts.includes('references/react-native-adapter.md')) {
      fail('skill.json: react-native-adapter.md is not declared in contracts.');
    }
    if (!Array.isArray(parsed.contracts) || !parsed.contracts.includes('references/component-code-contract.md')) {
      fail('skill.json: component-code-contract.md is not declared in contracts.');
    }
  } catch (error) {
    fail(`skill.json: invalid JSON (${error.message})`);
  }
}

for (const style of styles) {
  const dir = join(root, 'skills', style);
  const css = read(join(dir, 'example.css'));
  const tsx = read(join(dir, 'example.tsx'));
  const dart = read(join(dir, 'example.flutter.dart'));

  if (!css) fail(`${style}/example.css: missing or unreadable.`);
  else {
    mustContain(css, /:focus-visible/i, `${style}/example.css`);
    mustContain(css, /@media\s*\(max-width\s*:/i, `${style}/example.css`);
    mustContain(css, /@media\s*\(prefers-reduced-motion/i, `${style}/example.css`);
    mustContain(css, /@media\s*\(forced-colors:\s*active/i, `${style}/example.css`);
  }

  if (!tsx) fail(`${style}/example.tsx: missing or unreadable.`);
  else {
    mustContain(tsx, /<button\b|<a\b|<input\b|<select\b|<textarea\b/i, `${style}/example.tsx`);
    mustContain(tsx, /data-state|disabled|aria-disabled|aria-selected|aria-busy/i, `${style}/example.tsx`);
    mustContain(tsx, /responsive|grid|flex|width/i, `${style}/example.tsx`);
  }

  if (!dart) fail(`${style}/example.flutter.dart: missing or unreadable.`);
  else {
    mustContain(dart, /Button|TextButton|ElevatedButton|OutlinedButton|FilledButton|IconButton|TextField|Switch|Checkbox|Slider|NavigationBar|Tab/i, `${style}/example.flutter.dart`);
    mustContain(dart, /48|minimumSize|tap target|target size|MaterialTapTargetSize/i, `${style}/example.flutter.dart`);
    mustContain(dart, /LayoutBuilder|MediaQuery|Wrap|GridView|responsive|width/i, `${style}/example.flutter.dart`);
  }
}

if (failures.length) {
  console.error(`\nQuality-gate validation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  process.exit(1);
}

console.log(`Quality-gate validation PASSED: ${styles.length} styles covered.`);
