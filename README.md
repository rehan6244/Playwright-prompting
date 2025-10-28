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



