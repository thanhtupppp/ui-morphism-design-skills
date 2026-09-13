#!/usr/bin/env node

import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const VALIDATOR_VERSION = '2.1.0';
const root = process.cwd();
const stylesRoot = join(root, 'skills');
const expectedStyles = ['skeuomorphism', 'flat-design', 'neumorphism', 'material-design', 'glassmorphism', 'claymorphism', 'liquid-glass', 'aurora-ui', 'bento-ui', 'neobrutalism'];
const requiredFiles = ['SKILL.md', 'components.md', 'platforms.md', 'example.css', 'example.tsx', 'example.flutter.dart'];
const requiredRefs = [
  'references/component-code-contract.md',
  'references/platform-contract.md',
  'references/platform-matrix.md',
  'references/review-checklist.md',
  'references/token-convention.md',
  'references/code-examples.md',
  'references/quality-gates.md',
  'references/react-native-adapter.md',
];
const failures = [];
const warnings = [];

const fail = (message) => failures.push(message);
const warn = (message) => warnings.push(message);
const read = (path) => { try { return readFileSync(path, 'utf8'); } catch { return null; } };
const slugToTokenStyle = (style) => style.replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const tokenDefinitions = (text) => [...(text || '').matchAll(/(^|[\s{;])(--[a-z0-9-]+)\s*:/gim)].map((match) => match[2]);
const requireText = (path, patterns, label) => {
  const text = read(path);
  if (text === null) { fail(`${label}: missing or unreadable file`); return null; }
  for (const pattern of patterns) if (!pattern.test(text)) fail(`${label}: missing required contract ${pattern}`);
  return text;
};

console.log(`UI Morphism Design Validator v${VALIDATOR_VERSION}`);

if (!existsSync(stylesRoot)) fail('skills/: missing');
const actualStyles = existsSync(stylesRoot) ? readdirSync(stylesRoot, { withFileTypes: true }).filter((entry) => entry.isDirectory()).map((entry) => entry.name).filter((name) => !name.startsWith('.')) : [];
const missingStyles = expectedStyles.filter((style) => !actualStyles.includes(style));
const unexpectedStyles = actualStyles.filter((style) => !expectedStyles.includes(style));
if (missingStyles.length) fail(`skills/: missing style directories: ${missingStyles.join(', ')}`);
if (unexpectedStyles.length) warn(`skills/: unexpected directories: ${unexpectedStyles.join(', ')}`);

for (const style of expectedStyles) {
  const dir = join(stylesRoot, style);
  if (!existsSync(dir)) continue;
  for (const file of requiredFiles) if (!existsSync(join(dir, file))) fail(`${style}: missing ${file}`);

  const skill = requireText(join(dir, 'SKILL.md'), [/accessib/i, /responsive|adaptive/i, /fallback/i, /performance/i], `${style}/SKILL.md`);
  const components = requireText(join(dir, 'components.md'), [/Button/i, /Card|Panel/i, /Input|Form/i, /state/i, /responsive|compact|medium|expanded/i], `${style}/components.md`);
  const platforms = requireText(join(dir, 'platforms.md'), [/HTML|CSS/i, /React/i, /Flutter/i, /React Native|other renderer|Other UI/i, /fallback/i, /performance/i, /reduced.?motion/i], `${style}/platforms.md`);
  const css = read(join(dir, 'example.css'));
  const tsx = read(join(dir, 'example.tsx'));
  const dart = read(join(dir, 'example.flutter.dart'));

  if (components) {
    const states = [['default', /\bdefault\b/i], ['hover', /\bhover\b/i], ['active\/pressed', /\bactive\b|\bpressed\b/i], ['selected', /\bselected\b/i], ['disabled', /\bdisabled\b/i], ['loading', /\bloading\b/i], ['focus-visible', /focus.?visible/i]];
    for (const [name, pattern] of states) if (!pattern.test(components)) warn(`${style}/components.md: state ${name} is not explicitly documented.`);
    if (!/375|768|1024|1440|compact|medium|expanded/i.test(components)) warn(`${style}/components.md: responsive matrix is not explicit.`);
  }

  if (css) {
    if (!/:focus-visible/i.test(css)) warn(`${style}/example.css: no :focus-visible selector.`);
    if (!/@media\s*\(prefers-reduced-motion/i.test(css)) warn(`${style}/example.css: no prefers-reduced-motion media query.`);
    if (!/@media\s*\(forced-colors:\s*active/i.test(css)) warn(`${style}/example.css: no forced-colors fallback query.`);
    if (!/min-(?:height|width)\s*:/i.test(css)) warn(`${style}/example.css: no explicit minimum control geometry.`);
    if (!/@media[^{]*(?:max-width|min-width)/i.test(css)) warn(`${style}/example.css: no responsive breakpoint rule.`);

    const tokens = tokenDefinitions(css);
    const canonicalPrefix = `--um-${slugToTokenStyle(style)}-`;
    const generic = tokens.filter((token) => /^--(?:primary|secondary|surface|bg|background|text|ink|muted|border|radius|shadow|space|spacing|focus|accent|success|warning|danger|info|control|target|touch)(?:-|$)/i.test(token));
    if (generic.length) fail(`${style}/example.css: generic token namespace detected: ${[...new Set(generic)].join(', ')}`);
    const nonCanonical = tokens.filter((token) => !token.startsWith(canonicalPrefix) && !token.startsWith('--um-'));
    if (nonCanonical.length) warn(`${style}/example.css: legacy/non-canonical token namespace(s): ${[...new Set(nonCanonical)].join(', ')}; prefer ${canonicalPrefix}<group>.`);
    if (/backdrop-filter|filter\s*:|mix-blend-mode/i.test(css) && !/fallback|opaque|progressive enhancement/i.test(`${skill || ''} ${platforms || ''}`)) warn(`${style}: expensive visual effect lacks explicit fallback/progressive-enhancement language.`);
  }

  if (tsx) {
    if (/<(?:div|span)[^>]+(?:onClick|onKeyDown|role=["']button)/i.test(tsx)) fail(`${style}/example.tsx: non-semantic interactive element detected.`);
    if (!/<button\b|<a\b|<input\b|<select\b|<textarea\b/i.test(tsx)) warn(`${style}/example.tsx: no obvious native interactive element detected.`);
    if (/role=["']button["']/i.test(tsx) && !/tabIndex/i.test(tsx)) warn(`${style}/example.tsx: custom button role lacks explicit keyboard focus handling.`);
    if (/<input\b|<select\b|<textarea\b/i.test(tsx) && !/aria-label|aria-labelledby|<label\b/i.test(tsx)) warn(`${style}/example.tsx: form control has no obvious accessible label.`);
    if (!/disabled|aria-disabled|aria-selected|aria-busy|data-state/i.test(tsx)) warn(`${style}/example.tsx: no explicit interactive state marker detected.`);
    if (!/responsive|matchMedia|useMediaQuery|grid|flex|width/i.test(tsx)) warn(`${style}/example.tsx: responsive implementation intent is not obvious.`);
  }

  if (dart) {
    if (!/Semantics|Tooltip|Button|TextButton|ElevatedButton|OutlinedButton|FilledButton|IconButton|TextField|Switch|Checkbox|Slider|NavigationBar|Tab/i.test(dart)) warn(`${style}/example.flutter.dart: native/semantic interactive primitive not detected.`);
    if (!/48|minimumSize|tap target|target size|MaterialTapTargetSize/i.test(dart)) warn(`${style}/example.flutter.dart: 48dp target-size guidance is not explicit.`);
    if (!/LayoutBuilder|MediaQuery|Wrap|GridView|responsive|width/i.test(dart)) warn(`${style}/example.flutter.dart: responsive implementation intent is not obvious.`);
  }
}

const skillJson = read(join(root, 'skill.json'));
if (skillJson === null) fail('skill.json: missing or unreadable');
else {
  try {
    const parsed = JSON.parse(skillJson);
    const declared = Array.isArray(parsed.styles) ? parsed.styles.map((item) => typeof item === 'string' ? item : item?.path ?? item?.id ?? item?.name).filter(Boolean).map(String) : [];
    if (JSON.stringify(declared) !== JSON.stringify(expectedStyles)) fail(`skill.json: styles must exactly match the canonical order: ${expectedStyles.join(', ')}`);
    for (const platform of ['html-css', 'react', 'flutter', 'react-native', 'other-renderers-via-adapter']) if (!Array.isArray(parsed.platforms) || !parsed.platforms.includes(platform)) fail(`skill.json: missing platform ${platform}`);
    for (const step of ['analyze', 'select-primary-style', 'generate-semantic-tokens', 'negotiate-platform-capabilities', 'plan-components', 'implement', 'audit']) if (!Array.isArray(parsed.workflow) || !parsed.workflow.includes(step)) fail(`skill.json: missing workflow step ${step}`);
    if (parsed.source_of_truth !== 'SKILL.md') fail('skill.json: source_of_truth must be SKILL.md');
    for (const contract of ['references/component-code-contract.md', 'references/platform-contract.md', 'references/platform-matrix.md', 'references/quality-gates.md', 'references/react-native-adapter.md']) {
      if (!Array.isArray(parsed.contracts) || !parsed.contracts.includes(contract)) fail(`skill.json: missing contract ${contract}`);
    }
  } catch (error) { fail(`skill.json: invalid JSON (${error.message})`); }
}

for (const reference of requiredRefs) if (!existsSync(join(root, reference))) fail(`${reference}: missing repository contract`);
const tokenConvention = read(join(root, 'references/token-convention.md'));
if (tokenConvention && !/--um-<style>-<group>/i.test(tokenConvention)) fail('references/token-convention.md: canonical token grammar is missing.');
const componentContract = read(join(root, 'references/component-code-contract.md'));
if (componentContract) {
  if (!/semantic-state/i.test(componentContract)) warn('component-code-contract.md: semantic-state rule phrase not found.');
  if (!/responsive rule/i.test(componentContract)) warn('component-code-contract.md: responsive rule phrase not found.');
}
const platformContract = read(join(root, 'references/platform-contract.md'));
if (platformContract) {
  for (const pattern of [/required|preferred|optional/i, /progressive enhancement/i, /reduced.?motion/i, /forced colors/i, /375|768|1024|1440/i, /fallback/i]) if (!pattern.test(platformContract)) warn(`platform-contract.md: missing contract concept ${pattern}`);
}
const qualityGates = read(join(root, 'references/quality-gates.md'));
if (qualityGates) {
  for (const pattern of [/Gate A|semantics/i, /Gate B|responsive/i, /Gate C|motion|fallback/i, /Gate D|target size/i, /Gate E|effect budget/i, /Gate F|cross-platform/i, /Gate G|React Native adapter/i]) if (!pattern.test(qualityGates)) fail(`quality-gates.md: missing quality gate concept ${pattern}`);
}
const reactNativeAdapter = read(join(root, 'references/react-native-adapter.md'));
if (reactNativeAdapter) {
  for (const pattern of [/semantic-first mapping/i, /canonical token mapping/i, /native interaction primitives/i, /responsive adaptation/i, /accessibility/i, /performance|fallback/i]) if (!pattern.test(reactNativeAdapter)) fail(`react-native-adapter.md: missing adapter concept ${pattern}`);
}

const readme = read(join(root, 'README.md'));
if (readme) for (const style of expectedStyles) {
  const displayName = style.split('-').map((part) => part.charAt(0).toUpperCase() + part.slice(1)).join(' ');
  const escaped = displayName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  if (!new RegExp(`${style}|${escaped}`, 'i').test(readme)) warn(`README.md: style ${style} is not mentioned by slug or display name.`);
}

if (failures.length) {
  console.error(`\nValidation FAILED: ${failures.length} error(s)`);
  failures.forEach((message) => console.error(`- ${message}`));
  if (warnings.length) { console.error(`\nWarnings: ${warnings.length}`); warnings.forEach((message) => console.error(`- ${message}`); }
  process.exit(1);
}
console.log(`Validation PASSED: ${expectedStyles.length} styles checked.`);
if (warnings.length) {
  console.log(`Warnings: ${warnings.length}`);
  warnings.forEach((message) => console.log(`- ${message}`));
}
