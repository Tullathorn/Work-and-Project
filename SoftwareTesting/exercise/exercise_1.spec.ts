import { test, expect } from '@playwright/test';

test('Locators & Login', async ({ page }) => {
    await page.goto('https://www.saucedemo.com/');
    await page.locator('[data-test="username"]').click();
    await page.locator('[data-test="username"]').fill('standard_user');
    await page.locator('[data-test="password"]').click();
    await page.locator('[data-test="password"]').fill('secret_sauce');
    await page.locator('[data-test="login-button"]').click();
    await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
    await expect(page.locator(".title")).toHaveText('Products');
    await expect(page.locator('.inventory_item')).toHaveCount(6);
});
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
