import { test, expect } from '@playwright/test';

test('Assertions เชิงลึก', async ({ page }) => {
    await page.goto('https://www.saucedemo.com/');
    await page.locator('[data-test="username"]').click();
    await page.locator('[data-test="username"]').fill('standard_user');
    await page.locator('[data-test="password"]').click();
    await page.locator('[data-test="password"]').fill('11111');
    await page.locator('[data-test="login-button"]').click();
  
    await expect(page.locator('[data-test="error"]')).toBeVisible();

    await expect(page.locator('[data-test="error"]')).toContainText('do not match');

    await expect(page.getByPlaceholder('Username')).toHaveClass(/error/);

    await page.locator('.error-button').click();
    await expect(page.locator('[data-test="error"]')).not.toBeVisible();
});