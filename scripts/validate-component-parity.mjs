#!/usr/bin/env node

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const styles = ['skeuomorphism', 'flat-design', 'neumorphism', 'material-design', 'glassmorphism', 'claymorphism', 'liquid-glass', 'aurora-ui', 'bento-ui', 'neobrutalism'];
const manifestPath = join(root, 'references', 'component-parity.json');
const failures = [];

const read = (path) => readFileSync(path, 'utf8');
const readOptional = (path) => { try { return read(path); } catch { return ''; } };
const fail = (message) => failures.push(message);

let manifest;
try {
  manifest = JSON.parse(read(manifestPath));
} catch (error) {
  console.error(`Component parity validation FAILED: invalid manifest (${error.message})`);
  process.exit(1);
}

if (manifest.schemaVersion !== '1.0.0') fail(`component-parity.json: unsupported schema version ${manifest.schemaVersion ?? 'missing'}.`);
if (manifest.component !== 'primary-action') fail('component-parity.json: normalized component must be primary-action.');
if (manifest.role !== 'button') fail(`component-parity.json: expected role button, found ${manifest.role ?? 'missing'}.`);
if (manifest.accessibleName !== 'required') fail('component-parity.json: accessibleName must be required.');
if (!Array.isArray(manifest.states) || !['default', 'pressed', 'disabled'].every((state) => manifest.states.includes(state))) {
  fail('component-parity.json: baseline states must include default, pressed, and disabled.');
}
if (manifest.targetSize?.webCssPx !== 44 || manifest.targetSize?.nativeLogicalPx !== 48) {
  fail('component-parity.json: target sizes must be 44 CSS px web and 48 logical px native.');
}
if (!manifest.responsive || !manifest.fallbackRequired) fail('component-parity.json: responsive and fallbackRequired must be enabled.');

const evidence = (text, patterns) => patterns.some((pattern) => text.toLowerCase().includes(pattern.toLowerCase()));
const requireEvidence = (text, patterns, label) => {
  if (!evidence(text, patterns)) fail(`${label}: none of [${patterns.join(', ')}] found.`);
};

for (const style of styles) {
  const dir = join(root, 'skills', style);
  const css = read(join(dir, 'example.css'));
  const react = read(join(dir, 'example.tsx'));
  const flutter = read(join(dir, 'example.flutter.dart'));
  const native = read(join(dir, 'example.native.tsx'));
  const platformContract = readOptional(join(dir, 'platforms.md'));
  const shared = `${css}\n${react}\n${flutter}\n${native}\n${platformContract}`;

  const sources = {
    'html-css': `${css}\n${react}`,
    react: `${css}\n${react}`,
    flutter,
    'react-native': native,
  };

  for (const [renderer, rules] of Object.entries(manifest.renderers)) {
    const text = sources[renderer];
    if (!text) {
      fail(`${style}/${renderer}: missing example source.`);
      continue;
    }

    requireEvidence(text, rules.semanticPrimitive, `${style}/${renderer} semantic primitive`);
    requireEvidence(text, rules.stateSignals, `${style}/${renderer} state semantics`);
    requireEvidence(text, rules.nameSignals, `${style}/${renderer} accessible naming`);
    if (manifest.responsive) requireEvidence(text, rules.responsiveSignals, `${style}/${renderer} responsive intent`);

    if (manifest.fallbackRequired) {
      requireEvidence(shared, rules.fallbackSignals, `${style}/${renderer} deterministic fallback`);
    }

    const isWeb = renderer === 'html-css' || renderer === 'react';
    const targetRequirement = isWeb ? `${manifest.targetSize.webCssPx}px` : `${manifest.targetSize.nativeLogicalPx}`;
    const targetText = isWeb ? `${css}\n${text}` : text;
    requireEvidence(targetText, [targetRequirement, 'target', 'minHeight', 'min-height', 'minimumSize', 'control-height'], `${style}/${renderer} target-size policy`);
  }
}

if (failures.length) {
  console.error(`Component parity validation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  process.exit(1);
}

console.log(`Component parity validation PASSED: ${styles.length} styles × ${Object.keys(manifest.renderers).length} renderers.`);
