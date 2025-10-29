// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  retries: process.env.CI ? 2 : 0,  // 0 locally for fast debugging; 2 in CI
  use: {
    trace: 'on-first-retry',  // Auto-capture traces/videos on retry for diagnosis
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  },
  reporter: [['html'], ['json']]  // Generates flaky reports
});