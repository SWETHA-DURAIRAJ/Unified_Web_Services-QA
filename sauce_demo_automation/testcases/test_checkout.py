from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login_checkout(driver):

    wait = WebDriverWait(driver, 10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify login
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Add two products
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify products in cart
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    item_names = [item.text for item in cart_items]

    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bike Light" in item_names

    # Checkout
    driver.find_element(By.ID, "checkout").click()

    # Enter checkout details
    driver.find_element(By.ID, "first-name").send_keys("Swetha")
    driver.find_element(By.ID, "last-name").send_keys("D")
    driver.find_element(By.ID, "postal-code").send_keys("600001")

    driver.find_element(By.ID, "continue").click()

    # Finish order
    driver.find_element(By.ID, "finish").click()

    # Verify success message
    success_message = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text


    assert success_message == "Thank you for your order!"