# Import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture
def logged_in():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # Inicjalizacja drivera z opcjami
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Wejście na stronę
    driver.get("https://www.saucedemo.com/v1/")
    driver.implicitly_wait(5)

    # Logowanie
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Zwracamy driver do użycia w testach
    yield driver

    # Zamykanie przeglądarki
    driver.quit()