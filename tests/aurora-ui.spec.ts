import { expect, test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.beforeEach(async ({ page }) => { await page.goto('/'); });

test('Aurora preview is the default and exposes its primary structure', async ({ page }) => {
  await expect(page.getByLabel('Style')).toHaveValue('aurora-ui');
  await expect(page.getByRole('heading', { name: 'Ideas become visible signals.' })).toBeVisible();
  await expect(page.getByRole('complementary', { name: 'Live Aurora signal' })).toBeVisible();
  await expect(page.getByRole('article')).toHaveCount(4);
});

test('primary action announces the new state', async ({ page }) => {
  await expect(page.getByRole('status')).toHaveText('Ready for exploration.');
  await page.getByRole('button', { name: 'Explore the system' }).click();
  await expect(page.getByRole('status')).toHaveText('System exploration started. Choose a workflow phase below.');
});

test('workflow phase selection exposes persistent state and new content', async ({ page }) => {
  const compose = page.getByRole('button', { name: '02 Compose' });
  await compose.click();
  await expect(compose).toHaveAttribute('aria-pressed', 'true');
  await expect(page.getByRole('heading', { name: 'Turn atmosphere into structure.' })).toBeVisible();
  await page.getByRole('button', { name: '03 Verify' }).click();
  await expect(page.getByRole('heading', { name: 'Keep the experience resilient.' })).toBeVisible();
});

test('effects can be removed without removing content or interactions', async ({ page }) => {
  await page.getByLabel('Effects').selectOption('off');
  await expect(page.locator('.aurora-demo')).toHaveAttribute('data-effects', 'off');
  expect(await page.locator('.aurora-demo').evaluate(element => getComputedStyle(element, '::before').display)).toBe('none');
  await expect(page.getByRole('heading', { name: 'Ideas become visible signals.' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Explore the system' })).toBeEnabled();
});

for (const width of [375, 768, 1440]) {
  test(`Aurora layout and controls fit at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    const targets = await page.locator('.aurora-demo button, .aurora-demo a').evaluateAll(elements => elements.map(element => element.getBoundingClientRect().height));
    expect(targets.filter(height => height > 0).every(height => height >= 48)).toBe(true);
  });
}

test('keyboard focus and selected state survive forced colors', async ({ page }) => {
  await page.emulateMedia({ forcedColors: 'active', reducedMotion: 'reduce' });
  const verify = page.getByRole('button', { name: '03 Verify' });
  await verify.focus();
  await page.keyboard.press('Enter');
  await expect(verify).toBeFocused();
  await expect(verify).toHaveAttribute('aria-pressed', 'true');
  await expect(verify).toHaveCSS('outline-style', 'solid');
  await expect(page.getByRole('heading', { name: 'Keep the experience resilient.' })).toBeVisible();
});

test('automated accessibility checks pass with effects on and off', async ({ page }) => {
  for (const effects of ['full', 'off']) {
    await page.getByLabel('Effects').selectOption(effects);
    const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
    expect(results.violations).toEqual([]);
  }
});
