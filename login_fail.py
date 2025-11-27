import asyncio
from playwright.async_api import async_playwright

async def test_login_fail():
    async with async_playwright() as p:
        
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto("https://www.saucedemo.com")
        
        # Login with locked_out_user
        await page.fill("[data-test=username]", "locked_out_user")
        await page.fill("[data-test=password]", "secret_sauce")
        await page.click("[data-test=login-button]")
        
        # Wait for the error message
        """error = await page.locator("[data-test=error]").text_content()
        print(f"Error message: {error}")"""
        
        await page.locator("[data-test=error]").wait_for_text(
        "Epic sadface: Sorry, this user has been locked out."
         )
        
        assert "Epic sadface: Sorry, this user has been locked out." in error
        
        await browser.close()

asyncio.run(test_login_fail())