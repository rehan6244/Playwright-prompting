# Playwright-prompting
prompting template like more shot one shot and many shots prompting

#login

Generate a Playwright TypeScript/python test stub for a login page.
The page is at '/login'.
It has an email input with the selector '#email', a password input with the selector '#password', and a login button with the text 'Log In'.
After successful login, the user should be redirected to '/dashboard' and a welcome message 'Welcome, User!' (selector: '.welcome-banner') should be visible.
Include necessary imports and a basic test structure.

#Page object model

Create a Playwright TypeScript/python Page Object Model (POM) class named 'SearchResultsPage'.
The page URL is typically '/search-results'.
It should include:
1. A constructor that accepts the Playwright 'Page' object.
2. A method 'getAllResultTitles' that returns an array of strings of all search result titles. The selector for a single result title is 'h2.result-card__title'.
3. A method 'clickFirstResult' that clicks on the first search result link. Assume the link is within an article tag: 'article.result-card a'.
4. A method 'navigateTo' to go to the search results page.

#debugging errors

I'm encountering a 'TimeoutError: waiting for selector "#checkout-button" to be visible' in my Playwright TypeScript test.
Here's the relevant part of my test:
'''typescript
// ... other steps ...
await page.locator('#product-details').waitFor({ state: 'visible' });
console.log('Product details visible');
await page.locator('#checkout-button').click(); // This line throws the error
'''
What are common reasons for this specific error with '#checkout-button' and how can I debug it effectively in Playwright? Suggest specific Playwright APIs or techniques.


#understanding a feature 

Explain Playwright's concept of "web-first assertions" (e.g., `expect(locator).toBeVisible()`).
How do they differ from manual, explicit waits?
Provide a simple Playwright TypeScript code example demonstrating a web-first assertion and why it's beneficial for test stability.


#Converting a Test to Use test.extend for Fixtures


I have a Playwright TypeScript test suite where many tests require a user to be logged in.
Currently, I repeat the login steps in a `test.beforeEach`.
Here's my current login logic:
'''typescript
test.beforeEach(async ({ page }) => {
  await page.goto('/login');
  await page.locator('#username').fill('testuser');
  await page.locator('#password').fill('complexpassword');
  await page.locator('button[type="submit"]').click();
  await expect(page).toHaveURL('/dashboard');
});
'''
Show me how to refactor this using `test.extend` to create a custom fixture named `loggedInPage`.
This fixture should provide an already logged-in `page` object to the tests.


#Generating Test Ideas/Edge Cases

I'm responsible for testing a new file upload feature in a web application using Playwright.
The feature allows users to upload JPG, PNG, and PDF files, with a maximum file size of 10MB.
What are some important positive, negative, and edge case scenarios I should consider for my Playwright tests?
Categorize them if possible.


#Handling Dynamic Content with Auto-Waiting & Retries
Generate a Playwright TypeScript test that handles a dynamically loaded product grid where items appear after an API call. The grid container is #product-grid, each product card is .product-card, and the title inside is h3.
Requirements:
•  Use web-first assertions (expect(locator).toBeVisible())
•  Wait for at least 3 cards to be present
•  Extract and return an array of all visible product titles
•  Include retry logic using expect.poll if initial load fails due to network latency
•  Add tracing and a screenshot on failure
Include full test structure with test.describe, imports, and proper cleanup.


#Page Object Model with Lazy Initialization & Reusability
Create a Playwright Python Page Object Model class CartPage following best practices:

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self._items = None  # lazy

Features to include:
•  URL: /cart
•  Lazy-loaded locators (only resolved on first use)
•  Method get_item_count() -> int
•  Method update_quantity(item_name: str, qty: int) using data-attribute data-test-id="item-{name}"
•  Method proceed_to_checkout() that asserts navigation to /checkout
•  Method remove_all_items() with confirmation dialog handling
•  Type hints, docstrings, and auto-waiting via locator methods
Bonus: Show how to extend this POM in a fixture using pytest-playwright.


#Debugging Flaky Locator in Shadow DOM

I’m getting intermittent TimeoutError on this line: (typescript below)

await page.locator('text=Save Changes').click();

But the button exists in a Shadow DOM inside a custom component <app-modal>.
Provide:
1.  A robust selector strategy using pierceShadow or locator.evaluate
2.  A debugging snippet using page.pause(), locator.highlight(), and console listeners
3.  A fallback polling mechanism with waitForFunction
4.  How to assert visibility inside shadow root using expect(locator).toBeVisible() correctly
Include full TypeScript code example.


#Understanding Auto-Waiting vs Explicit Waits vs Polling
Explain Playwright’s auto-waiting mechanism in depth:
•  How it works under the hood (actionability checks)
•  Difference between auto-wait, explicit waitFor, and polling with expect.poll
•  When to use each
Then provide three equivalent TypeScript snippets for clicking a button that appears after animation:
1.  Using auto-wait only
2.  Using waitFor({ state: 'visible' })
3.  Using expect(locator).toBeEnabled() with retry
Highlight flakiness risk and performance impact of each.


#Creating Reusable Auth Fixtures with Role-Based Login
Refactor this repeated login logic into reusable fixtures using test.extend:

(typescript)

// Current (repeated)
test.beforeEach(async ({ page }) => {
  await login(page, 'admin@example.com', 'admin123');
  await expect(page).toHaveURL('/admin');
});

Create two fixtures:
•  adminPage: Page → logged in as admin
•  customerPage: Page → logged in as customer
Show:
•  fixtures/auth.ts with test.extend
•  Role-based login function with storage state caching (storageState: 'admin.json')
•  How to skip saving state in CI using env var
•  Example test using both fixtures in parallel
Include TypeScript types, JSDoc, and cleanup.


#API-Driven UI Testing with Route Interception
Write a Playwright TypeScript test that:
•  Intercepts GET /api/user-profile
•  Mocks response with delayed latency (500ms) and dynamic data
•  Verifies UI reflects:
	•  Avatar loads from user.avatarUrl
	•  Name shows user.fullName
	•  Badge shows if user.isPremium === true
Use:
•  page.route() with route.fulfill()
•  expect(locator).toHaveText() with web-first assertion
•  Screenshot comparison on change
•  Trace viewer enabled on failure
Show how to parameterize the mock for happy/path and error cases.


#Parallel Execution with Isolated Storage & Worker Reuse
Optimize a test suite with 50+ tests requiring login:
Currently:
(typescript)

test('user can view profile', async ({ page }) => { await login(page); ... });


Refactor using:
•  Worker-scoped fixture with test.use({ storageState: ... })
•  Isolated contexts per worker
•  Pre-login storage state generated once in global-setup.ts
•  Parallel execution with fullyParallel: true
Show:
•  playwright.config.ts changes
•  global-setup.ts
•  How to conditionally skip in CI
•  Benchmark improvement tip


#Smart Waiting for Toast Notifications
Implement a reusable utility waitForToast(page: Page, message: string, options?) that:
•  Waits for toast with role="alert" and text
•  Supports partial match, timeout, dismissal
•  Auto-retries if toast is replaced (common in React)
•  Returns toast locator for further assertions
Provide TypeScript and Python versions.
Then show usage in a test after form submission.


#Testing File Download with Verification
Write a Playwright test that:
•  Triggers download via button #export-report
•  Waits for download event
•  Asserts:
	•  File name matches pattern report_*.csv
	•  File size > 0
	•  First line contains header "Date,Amount,Status"
Use:
•  page.waitForEvent('download')
•  download.path() and fs.readFile
•  Run in headed mode for debug
•  Clean up downloaded files in afterEach
Include error handling if download fails.





