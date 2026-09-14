#!/usr/bin/env node

import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const styles = ['skeuomorphism', 'flat-design', 'neumorphism', 'material-design', 'glassmorphism', 'claymorphism', 'liquid-glass', 'aurora-ui', 'bento-ui', 'neobrutalism'];
const manifestPath = join(root, 'references', 'component-parity.json');
const failures = [];

const read = (path) => readFileSync(path, 'utf8');
const fail = (message) => failures.push(message);

let manifest;
try {
  manifest = JSON.parse(read(manifestPath));
} catch (error) {
  console.error(`Component parity validation FAILED: invalid manifest (${error.message})`);
  process.exit(1);
}

const evidence = (text, patterns) => patterns.some((pattern) => text.toLowerCase().includes(pattern.toLowerCase()));
const requireEvidence = (text, patterns, label) => {
  if (!evidence(text, patterns)) fail(`${label}: none of [${patterns.join(', ')}] found.`);
};

for (const style of styles) {
  const dir = join(root, 'skills', style);
  const sources = {
    'html-css': `${read(join(dir, 'example.css'))}\n${read(join(dir, 'example.tsx'))}`,
    react: read(join(dir, 'example.tsx')),
    flutter: read(join(dir, 'example.flutter.dart')),
    'react-native': read(join(dir, 'example.native.tsx')),
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
    if (manifest.fallbackRequired) requireEvidence(text, rules.fallbackSignals, `${style}/${renderer} deterministic fallback`);

    const targetRequirement = renderer === 'html-css' || renderer === 'react'
      ? `${manifest.targetSize.webCssPx}px`
      : `${manifest.targetSize.nativeLogicalPx}`;
    requireEvidence(text, [targetRequirement, 'target', 'minHeight', 'min-height', 'minimumSize'], `${style}/${renderer} target-size policy`);
  }
}

if (failures.length) {
  console.error(`Component parity validation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  process.exit(1);
}

console.log(`Component parity validation PASSED: ${styles.length} styles × ${Object.keys(manifest.renderers).length} renderers.`);
