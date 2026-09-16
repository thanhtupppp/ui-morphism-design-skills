import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, readFileSync, realpathSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const repo = fileURLToPath(new URL('../', import.meta.url));
const validator = join(repo, 'scripts/validate-component-parity.mjs');
const original = JSON.parse(readFileSync(join(repo, 'references/component-parity.json'), 'utf8'));

test('the complete repository contract passes', () => {
  const result = spawnSync(process.execPath, [validator], { cwd: repo, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /10 styles × 4 renderers/);
});

const invalidContracts = [
  ['empty renderer map', (m) => { m.renderers = {}; }, /html-css must have a renderer rule object/],
  ['missing Flutter', (m) => { delete m.renderers.flutter; }, /flutter must have a renderer rule object/],
  ['null renderer map', (m) => { m.renderers = null; }, /renderers must be an object/],
  ['array renderer map', (m) => { m.renderers = []; }, /renderers must be an object/],
  ['unknown renderer', (m) => { m.renderers.other = m.renderers.flutter; }, /unsupported renderer other/],
  ['null renderer rules', (m) => { m.renderers.react = null; }, /react must have a renderer rule object/],
  ['missing signal list', (m) => { delete m.renderers.flutter.nameSignals; }, /flutter.nameSignals must be a non-empty array/],
  ['empty signal list', (m) => { m.renderers.react.stateSignals = []; }, /react.stateSignals must be a non-empty array/],
  ['blank match-all signal', (m) => { m.renderers.react.semanticPrimitive = ['']; }, /react.semanticPrimitive must be a non-empty array/],
  ['non-string signal', (m) => { m.renderers.flutter.nameSignals = [48]; }, /flutter.nameSignals must be a non-empty array/],
  ['string boolean', (m) => { m.responsive = 'false'; }, /must be boolean true/],
  ['disabled fallback', (m) => { m.fallbackRequired = false; }, /must be boolean true/],
];

for (const [name, mutate, expected] of invalidContracts) {
  test(`rejects ${name} before inspecting example sources`, (t) => {
    const parent = realpathSync(tmpdir());
    const fixture = mkdtempSync(join(parent, 'um-parity-test-'));
    t.after(() => {
      assert.equal(dirname(fixture), parent);
      assert.ok(fixture.startsWith(join(parent, 'um-parity-test-')));
      rmSync(fixture, { recursive: true, force: true });
    });
    mkdirSync(join(fixture, 'references'));
    const manifest = structuredClone(original);
    mutate(manifest);
    writeFileSync(join(fixture, 'references/component-parity.json'), JSON.stringify(manifest));
    const result = spawnSync(process.execPath, [validator], { cwd: fixture, encoding: 'utf8' });
    assert.equal(result.status, 1);
    assert.match(result.stderr, expected);
    assert.doesNotMatch(result.stderr, /TypeError|ENOENT/);
    assert.doesNotMatch(result.stdout, /PASSED/);
  });
}
