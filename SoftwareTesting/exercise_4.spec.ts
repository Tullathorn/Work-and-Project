import { test, expect } from '@playwright/test';

test('Assertions เชิงลึก', async ({ page }) => {
    await page.goto('https://www.saucedemo.com/');
    await page.locator('[data-test="username"]').click();
    await page.locator('[data-test="username"]').fill('standard_user');
    await page.locator('[data-test="password"]').click();
    await page.locator('[data-test="password"]').fill('secret_sauce');
    await page.locator('[data-test="login-button"]').click();

    await page.locator('[data-test="product-sort-container"]').selectOption('lohi');
    await expect(page.locator('.inventory_item').first()).toContainText('$7.99');
});
