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
const isRecord = (value) => value !== null && typeof value === 'object' && !Array.isArray(value);
const stopOnFailures = () => {
  if (!failures.length) return;
  console.error(`Component parity validation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  process.exit(1);
};

let manifest;
try {
  manifest = JSON.parse(read(manifestPath));
} catch (error) {
  console.error(`Component parity validation FAILED: invalid manifest (${error.message})`);
  process.exit(1);
}

if (!isRecord(manifest)) fail('component-parity.json: manifest must be an object.');
stopOnFailures();

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
if (manifest.responsive !== true || manifest.fallbackRequired !== true) fail('component-parity.json: responsive and fallbackRequired must be boolean true.');

const requiredRenderers = ['html-css', 'react', 'flutter', 'react-native'];
const evidenceFields = ['semanticPrimitive', 'stateSignals', 'nameSignals', 'responsiveSignals', 'fallbackSignals'];
if (!isRecord(manifest.renderers)) {
  fail('component-parity.json: renderers must be an object containing all four supported renderers.');
} else {
  for (const renderer of requiredRenderers) {
    const rules = manifest.renderers[renderer];
    if (!isRecord(rules)) {
      fail(`component-parity.json: ${renderer} must have a renderer rule object.`);
      continue;
    }
    for (const field of evidenceFields) {
      const values = rules[field];
      if (!Array.isArray(values) || values.length === 0 || values.some((value) => typeof value !== 'string' || value.trim().length === 0)) {
        fail(`component-parity.json: ${renderer}.${field} must be a non-empty array of non-blank strings.`);
      }
    }
  }
  for (const renderer of Object.keys(manifest.renderers)) {
    if (!requiredRenderers.includes(renderer)) fail(`component-parity.json: unsupported renderer ${renderer}.`);
  }
}
// Reject malformed contracts before reading examples, so missing rules cannot skip checks.
stopOnFailures();

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

stopOnFailures();

console.log(`Component parity validation PASSED: ${styles.length} styles × ${Object.keys(manifest.renderers).length} renderers.`);
