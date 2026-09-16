#!/usr/bin/env node

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const CONTRACT_VERSION = '1.9.0';
const styles = ['skeuomorphism', 'flat-design', 'neumorphism', 'material-design', 'glassmorphism', 'claymorphism', 'liquid-glass', 'aurora-ui', 'bento-ui', 'neobrutalism'];
const failures = [];
const read = (path) => { try { return readFileSync(path, 'utf8'); } catch { return null; } };
const fail = (message) => failures.push(message);
const mustContain = (text, pattern, label) => { if (!text || !pattern.test(text)) fail(`${label}: required quality-gate contract is missing.`); };

console.log(`UI Morphism Quality Gates v${CONTRACT_VERSION}`);

const requiredContracts = [
  ['references/quality-gates.md', /Gate A[\s\S]*Gate I/i],
  ['references/token-convention.md', /--um-<style>-<group>\[-<variant>\]/i],
  ['references/semantic-parity.md', /semantic anatomy[\s\S]*state meaning[\s\S]*responsive intent/i],
  ['references/accessibility-parity.md', /Accessibility behavior is part of cross-platform parity[\s\S]*state semantics/i],
  ['references/component-parity.json', /"component"\s*:\s*"primary-action"[\s\S]*"role"\s*:\s*"button"/i],
  ['references/component-parity.md', /normalized semantics[\s\S]*State normalization/i],
  ['references/react-native-adapter.md', /semantic-first mapping/i],
  ['references/component-code-contract.md', /Decision record[\s\S]*Verification record/i],
];
for (const [relative, pattern] of requiredContracts) mustContain(read(join(root, relative)), pattern, relative);

const skill = read(join(root, 'SKILL.md'));
for (const pattern of [/quality-gates\.md/i, /semantic-parity\.md/i, /accessibility-parity\.md/i, /component-parity\.json/i, /component-parity\.md/i, /token-convention\.md/i, /react-native-adapter\.md/i, /accessibility meaning must not depend on color/i]) mustContain(skill, pattern, 'SKILL.md');

const matrix = read(join(root, 'references/platform-matrix.md'));
for (const pattern of [/HTML\/CSS.*React.*Flutter.*React Native/i, /Required.*Preferred.*Optional/i, /full effect.*reduced effect.*opaque\/static effect.*simpler native surface/i]) mustContain(matrix, pattern, 'platform-matrix.md');

const skillJson = read(join(root, 'skill.json'));
if (!skillJson) fail('skill.json: missing or unreadable.');
else {
  try {
    const parsed = JSON.parse(skillJson);
    if (parsed.version !== CONTRACT_VERSION) fail(`skill.json: expected contract version ${CONTRACT_VERSION}, found ${parsed.version ?? 'missing'}.`);
    for (const contract of requiredContracts.map(([path]) => path)) if (!parsed.contracts?.includes(contract)) fail(`skill.json: ${contract} is not declared in contracts.`);
    if (!parsed.workflow?.includes('validate-component-parity')) fail('skill.json: validate-component-parity workflow step is missing.');
  } catch (error) { fail(`skill.json: invalid JSON (${error.message}).`); }
}

for (const style of styles) {
  const dir = join(root, 'skills', style);
  const css = read(join(dir, 'example.css')) || '';
  const react = read(join(dir, 'example.tsx')) || '';
  const flutter = read(join(dir, 'example.flutter.dart')) || '';
  const native = read(join(dir, 'example.native.tsx')) || '';
  const prefix = `--um-${style}-`;
  mustContain(css, new RegExp(`${prefix}[a-z0-9-]+\\s*:`), `${style}/example.css token definition`);
  mustContain(css, new RegExp(`var\\(${prefix}`), `${style}/example.css token consumption`);
  mustContain(css, /:focus-visible/i, `${style}/example.css focus`);
  mustContain(css, /@media\s*\(max-width\s*:/i, `${style}/example.css responsive`);
  mustContain(css, /@media\s*\(prefers-reduced-motion/i, `${style}/example.css reduced motion`);
  mustContain(css, /@media\s*\(forced-colors:\s*active/i, `${style}/example.css forced colors`);
  mustContain(react, /<button\b|<a\b|<input\b|<select\b|<textarea\b/i, `${style}/example.tsx semantic primitive`);
  mustContain(flutter, /Button|TextButton|ElevatedButton|OutlinedButton|FilledButton|IconButton|TextField|Switch|Checkbox|Slider|NavigationBar|Tab/i, `${style}/example.flutter.dart native primitive`);
  mustContain(native, /Pressable|TextInput|Switch|Slider/i, `${style}/example.native.tsx native primitive`);
  mustContain(`${react}\n${flutter}\n${native}`, /disabled|pressed|selected|loading|error/i, `${style} state`);
  mustContain(`${react}\n${flutter}\n${native}`, /responsive|LayoutBuilder|MediaQuery|useWindowDimensions|flexDirection|width|grid/i, `${style} responsive intent`);
  mustContain(`${react}\n${flutter}\n${native}`, /44|48|minHeight|minWidth|target/i, `${style} target size`);
  mustContain(`${css}\n${react}\n${flutter}\n${native}`, /fallback|remove|unsupported|without.*blur|without.*shadow/i, `${style} fallback`);
  mustContain(`${css}\n${react}\n${flutter}\n${native}`, /Verification:/i, `${style} verification record`);
}

if (failures.length) {
  console.error(`\nQuality-gate validation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  process.exit(1);
}
console.log(`Quality-gate validation PASSED: ${styles.length} styles covered.`);
