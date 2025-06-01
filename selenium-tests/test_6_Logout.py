from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout(logged_in):
    driver = logged_in
    
    #Znajdź menu
    button = driver.find_element(By.XPATH, "//button[text()='Open Menu']")
    button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )

    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()
    
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".login_logo"))
    )
    starting_screen = driver.find_element(By.CSS_SELECTOR, ".login_logo")
    assert starting_screen.is_displayed(), "Logo logowania nie jest widoczne po wylogowaniu!"

    driver.save_screenshot('Screenshots/6_Logout.png')
 
