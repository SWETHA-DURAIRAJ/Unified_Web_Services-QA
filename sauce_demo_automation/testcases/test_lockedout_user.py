from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_locked_user_login(driver):

    wait = WebDriverWait(driver, 10)

    # Login with locked user
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verify error message
    error_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h3"))
    ).text

    expected_message = "Epic sadface: Sorry, this user has been locked out."

    assert error_message == expected_message