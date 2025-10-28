#debug-flaky

**Problem**:  
Flaky test fails intermittently on:  
```ts
await page.locator('#save-btn').click();

Error: TimeoutError: locator.click: Timeout 30000ms exceeded
Button exists in DOM but not clickable.

(TS)

test('debug flaky save button', async ({ page }) => {
  await page.goto('/settings');

  // 1. PAUSE + INSPECT
  await page.pause(); // Opens Playwright Inspector — interact manually

  // 2. HIGHLIGHT + LOG STATE
  const saveBtn = page.locator('#save-btn');
  await saveBtn.highlight(); // Visual debug
  console.log('Visible:', await saveBtn.isVisible());
  console.log('Enabled:', await saveBtn.isEnabled());
  console.log('OffsetParent:', await saveBtn.evaluate(el => el.offsetParent));
  console.log('Bounding box:', await saveBtn.boundingBox());

  // 3. CHECK OVERLAYS / Z-INDEX
  const isCovered = await saveBtn.evaluate((el) => {
    const rect = el.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const topEl = document.elementFromPoint(centerX, centerY);
    return topEl !== el && topEl !== null;
  });
  console.log('Covered by another element:', isCovered);

  // 4. WAIT FOR ACTIONABILITY EXPLICITLY
  await saveBtn.waitFor({ state: 'visible' });
  await saveBtn.waitFor({ state: 'attached' });
  await expect(saveBtn).toBeEnabled(); // Web-first assertion

  // 5. FORCE CLICK IF NEEDED (bypass actionability)
  // await saveBtn.click({ force: true });

  // 6. ADD NETWORK IDLE (if save triggers API)
  const [response] = await Promise.all([
    page.waitForResponse(resp => resp.url().includes('/save') && resp.status() === 200),
    saveBtn.click() // Now stable
  ]);
  console.log('Save API success:', response.status());
});


Common Root Causes & Fixes

Button disabled  (isEnabled() === false)#detection
Covered by modal/loader   (elementFromPoint check)
Iframe  saveBtn.evaluate(el => el.ownerDocument !== document)

#proactive flaky proof pattern

async function clickStable(locator: Locator) {
  await expect(locator).toBeVisible();
  await expect(locator).toBeEnabled();
  await locator.click();
}

Add to test.config.ts

test.use({
  trace: 'on-first-retry',
  screenshot: 'only-on-failure',
  video: 'retain-on-failure'
});


