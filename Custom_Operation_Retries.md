// utils/retry.ts
import { Page, Locator } from '@playwright/test';

async function retryClick(page: Page, selector: string, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      await page.locator(selector).click();
      return;  // Success!
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await page.waitForTimeout(1000 * (i + 1));  // Backoff
    }
  }
}

// In test
test('retry upload', async ({ page }) => {
  await retryClick(page, '#upload-btn');
  // Assert success
});