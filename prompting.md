#Login

Playwright TS: Login test  
URL: /login  
Fields: #email, #password  
Button: text="Sign In"  
Success: redirect to /home + .user-greeting contains "Welcome"  
Use expect(locator).toBeVisible() + toHaveURL(). Full test with test.describe.


#POM

Playwright Python POM: LoginPage  
constructor(page)  
locators: email="#email", password="#password", submit="button[type=submit]"  
methods: login(email, pwd), is_error_visible()  
Use lazy locators. Include type hints + docstrings.


#Fill and submit


Playwright TS: Fill form and submit  
Selectors: #name, #email, [name="phone"], button:has-text("Submit")  
Fill values → click → wait for networkidle + assert URL /success  
Auto-wait + screenshot on failure.


#Wait for Toast


Wait for toast message containing "saved"  
Selector: [role="alert"], timeout 5000ms  
Use expect(locator).toContainText() with retry  
Handle auto-dismiss. Return locator.


#upload file 


Upload file via #upload-input  
File: fixtures/test.pdf (5MB)  
Assert: .upload-success visible + filename in list  
Use page.setInputFiles() + expect.toHaveText()


#mock Api

Mock GET /api/user → {id:1, name:"John", role:"admin"}  
Use page.route() + route.fulfill()  
Assert UI shows "John" and admin badge  
Include delay: 200ms


#fixture auth

Create loggedInPage fixture  
Login once → save storageState('user.json')  
Use in test: async ({ loggedInPage }) => { await loggedInPage.goto('/profile') }  
Skip save in CI via env.

#click and wait 

Click #add-to-cart → wait for #mini-cart to update  
Use expect(locator).toHaveText("1 item")  
Auto-wait + fallback expect.poll if animation delay


#table extract 

Extract all rows from table #results-table  
Columns: Name, Status, Actions  
Return array of objects: {name, status, hasEdit: bool}  
Skip empty rows. Use locator.all()

#debug Flaky

Flaky test: button #save sometimes not clickable  
Debug with:  
- page.pause()  
- locator('#save').highlight()  
- console.log(await locator.evaluate(el => el.offsetParent))  
- await page.waitForLoadState('networkidle')  
Suggest fix with toBeEnabled()

#parallel test 

Run 20 tests in parallel  
Use fullyParallel: true  
Each test gets fresh page via fixture  
Login via storageState per worker  
Config + global-setup.ts


#download

Click #export → download CSV  
Wait for download event  
Assert: filename matches report_*.csv, size > 100 bytes  
Save to ./downloads, delete in afterEach


#shadow click

Click button inside <my-modal> shadow DOM  
Text: "Confirm"  
Use page.locator('my-modal').locator('text=Confirm')  
Or evaluate: getShadowRoot().querySelector()  
Assert modal closed after


#form validation 

Submit empty form → assert 3 error messages  
Selectors: .error-message  
Use expect(locator).toHaveCount(3) + toContainText("required")


#network idle 

After login, wait for API calls to finish  
Use page.waitForLoadState('networkidle')  
Or waitForResponse(/profile/) + /permissions/


#screenshot

Take full-page screenshot on failure  
test.fail(() => page.screenshot({ path: `fail.png`, fullPage: true }))  
Add to test.afterEach


#select dropdown

Select "Canada" from #country dropdown  
Use page.selectOption('#country', 'CA')  
Assert selected text = "Canada"


#keyboard Nav

Tab to #submit button → press Enter  
Assert form submits → URL changes  
Use page.keyboard.press('Tab') x3 + 'Enter'

#mobile emulation 

Test on iPhone 13 viewport  
Use device: 'iPhone 13' in playwright.config  
Assert mobile menu toggle works


#trace on failure 

Enable trace on test failure  
test.use({ trace: 'on-first-retry' })  
View with: npx playwright show-trace trace.zip


#parametrized

Parametrize login test: 3 users  
@username, @password, @expectedURL  
Use test('login as @username', ...) + test.skip if invalid


#Api then ui

Call POST /login via page.request → get token  
Set cookie → goto /dashboard  
Assert welcome message without UI login

#lazy locator

POM: lazy getter  
private get submitBtn() { return this.page.locator('button >> text=Save').first(); }  
Use in clickSubmit() with auto-wait

#wait for gone

After delete, wait for #item-123 to disappear  
Use expect(locator).toBeHidden({ timeout: 5000 })

#route abort

Block all .css and .png requests  
Use page.route('**/*.{css,png}', route => route.abort())  
Speed up tests

#soft assert

Continue test after failure  
Use expect.soft(locator).toBeVisible()  
Assert all at end with expect.toPass()

#data-test-Id

Refactor all selectors to data-test-id  
#login-email → [data-test="login-email"]  
Update POM + test

#Ci config 

Playwright config for CI  
- shards: 3/3  
- reporters: html, json  
- retry: 2  
- workers: 4  
- headless: true

#global teardown 

global-teardown.ts: delete all test users via API  
Run after all tests

