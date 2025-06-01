from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time



def test_open_product(logged_in):
    driver = logged_in
    select_item = driver.find_element(By.ID, "item_5_title_link")
    select_item.click()
    
    driver.implicitly_wait(3)
    
    inventory_name = driver.find_element(By.CSS_SELECTOR, ".inventory_details_name")
    inventory_text = inventory_name.text.strip()

    assert (inventory_text) == "Sauce Labs Fleece Jacket", "Product not available"

    driver.save_screenshot('Screenshots/3_selected_item.png')

    
