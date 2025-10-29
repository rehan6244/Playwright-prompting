// In your test
import { test, expect } from '@playwright/test';

test('flaky button assert', async ({ page }) => {
  await page.goto('/dashboard');
  
  // Poll until visible (retries ~500ms intervals, up to 30s)
  await expect.poll(async () => {
    return page.locator('#save-btn').isVisible();
  }, { timeout: 30000 }).toBe(true);
  
  // Or soft assert (continues on fail, checks all at end)
  await expect.soft(page.locator('.toast')).toContainText('Saved!');
  expect.soft(page).toHaveURL('/dashboard');  // Bundles failures
});