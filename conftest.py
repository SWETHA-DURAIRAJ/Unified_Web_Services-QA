from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()





    options.add_argument("--incognito")



    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()