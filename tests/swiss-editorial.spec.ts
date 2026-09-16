import { expect, test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.beforeEach(async ({ page }) => { await page.goto('/?style=swiss-editorial'); });

test('search and category compose; empty-state reset restores all stories', async ({ page }) => {
  await expect(page.getByRole('article')).toHaveCount(3);
  await page.getByRole('button', { name: 'Culture', exact: true }).click();
  await expect(page.getByRole('article')).toHaveCount(1);
  await expect(page.getByRole('heading', { name: 'The city is a type specimen.' })).toBeVisible();
  await page.getByRole('searchbox').fill('grid');
  await expect(page.getByRole('article')).toHaveCount(0);
  await expect(page.getByRole('heading', { name: 'No stories found' })).toBeVisible();
  await page.getByRole('button', { name: 'Reset filters' }).click();
  await expect(page.getByRole('article')).toHaveCount(3);
  await expect(page.getByRole('searchbox')).toHaveValue('');
  await page.getByRole('searchbox').fill('  SPACE FOR AN UNEXPECTED  ');
  await expect(page.getByRole('article')).toHaveCount(1);
  await expect(page.getByRole('heading', { name: 'A grid is a starting point.' })).toBeVisible();
});

test('reading disclosure and bookmarks expose state and survive filtering', async ({ page }) => {
  const story = page.getByRole('article').first();
  const read = story.getByRole('button', { name: /^Read story/ });
  await expect(read).toHaveAttribute('aria-expanded', 'false');
  await read.click();
  await expect(story.getByText(/A clear interface starts/)).toBeVisible();
  await story.getByRole('button', { name: /^Close story/ }).click();
  await expect(story.getByText(/A clear interface starts/)).toBeHidden();
  await story.getByRole('button', { name: /^\+ Save\s*:/ }).click();
  await expect(story.getByRole('button', { name: /^✓ Saved\s*:/ })).toHaveAttribute('aria-pressed', 'true');
  await page.getByRole('button', { name: 'Culture', exact: true }).click();
  await page.getByRole('button', { name: 'All', exact: true }).click();
  await expect(story.getByRole('button', { name: /^✓ Saved\s*:/ })).toHaveAttribute('aria-pressed', 'true');
  await story.getByRole('button', { name: /^✓ Saved\s*:/ }).click();
  await expect(page.getByRole('status')).toHaveText('3 stories / 0 saved');
});

test('explicit theme wins over OS preference in both directions', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'dark' });
  const surface = page.locator('.swiss-demo');
  await expect(surface).toHaveCSS('background-color', 'rgb(29, 30, 28)');
  await page.getByLabel('Theme').selectOption('light');
  await expect(surface).toHaveCSS('background-color', 'rgb(244, 241, 234)');
  await page.emulateMedia({ colorScheme: 'light' });
  await page.getByLabel('Theme').selectOption('dark');
  await expect(surface).toHaveCSS('background-color', 'rgb(29, 30, 28)');
  await page.getByLabel('Theme').selectOption('system');
  await expect(surface).toHaveCSS('background-color', 'rgb(244, 241, 234)');
});

for (const width of [375, 768, 1024, 1440]) {
  test(`layout and controls fit at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await expect(page.getByRole('article')).toHaveCount(3);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    const targets = await page.locator('.swiss-demo button, .swiss-demo input, .swiss-demo a').evaluateAll(elements => elements.map(element => element.getBoundingClientRect().height));
    expect(targets.every(height => height >= 48)).toBe(true);
  });
}

test('keyboard activates filters and retains visible focus in forced colors', async ({ page }) => {
  await page.emulateMedia({ forcedColors: 'active', reducedMotion: 'reduce' });
  const culture = page.getByRole('button', { name: 'Culture', exact: true });
  await culture.focus();
  await page.keyboard.press('Enter');
  await expect(culture).toHaveAttribute('aria-pressed', 'true');
  await expect(culture).toBeFocused();
  await expect(culture).toHaveCSS('outline-style', 'solid');
  await expect(culture).toHaveCSS('outline-width', '3px');
  await expect(page.getByRole('article')).toHaveCount(1);
});

test('large text and RTL keep content in document order without horizontal overflow', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 900 });
  await page.evaluate(() => { document.documentElement.style.fontSize = '200%'; document.documentElement.dir = 'rtl'; });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  await expect(page.getByRole('article').getByRole('heading')).toHaveText(['Less noise. More meaning.', 'The city is a type specimen.', 'A grid is a starting point.']);
});

for (const theme of ['light', 'dark']) {
  test(`automated accessibility checks: ${theme}`, async ({ page }) => {
    await page.getByLabel('Theme').selectOption(theme);
    const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
    expect(results.violations).toEqual([]);
  });
}
