import { test, expect } from '@playwright/test';

test('Filter & Cart', async ({ page }) => {
    await page.goto('https://www.saucedemo.com/');
    await page.locator('[data-test="username"]').click();
    await page.locator('[data-test="username"]').fill('standard_user');
    await page.locator('[data-test="password"]').click();
    await page.locator('[data-test="password"]').fill('secret_sauce');
    await page.locator('[data-test="login-button"]').click();
    
    await page.locator('.inventory_item').filter({hasText: 'Sauce Labs Backpack'}).getByRole('button', {name: 'Add to cart'}).click();

    await expect(page.locator('.shopping_cart_badge')).toHaveText('1');

    await page.locator('.inventory_item').filter({hasText: 'Sauce Labs Bike Light'}).getByRole('button', {name: 'Add to cart'}).click();

    await expect(page.locator('.shopping_cart_badge')).toHaveText('2');

    await page.locator('.inventory_item').filter({hasText: 'Sauce Labs Backpack'}).getByRole('button', {name: 'Remove'}).click();
    await expect(page.locator('.shopping_cart_badge')).toHaveText('1');
});